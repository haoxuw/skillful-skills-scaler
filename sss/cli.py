"""sss command line. Deterministic steps only; model steps are done by the agent
following skills/*/SKILL.md, which call these commands."""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

from . import deprecate as depmod, generate, inventory, links, matrix as matrixmod, patches as patchmod, report, sources, status
from .manifest import DECISIONS, LOCAL_DIR, PATCHES_DIR, REPORTS_DIR, SOURCES_DIR, Manifest, ManifestError, Skill
from . import gitutil


def _root(args) -> Path:
    start = Path(args.root).resolve() if args.root else Path.cwd()
    try:
        return gitutil.repo_root(start)
    except gitutil.GitError:
        return start


def _out(args, obj) -> None:
    if getattr(args, "json", False):
        print(json.dumps(obj, indent=2, ensure_ascii=False))
    else:
        _pretty(obj)


def _pretty(obj, indent: int = 0) -> None:
    pad = "  " * indent
    if isinstance(obj, dict):
        for k, v in obj.items():
            if isinstance(v, (dict, list)) and v:
                print(f"{pad}{k}:")
                _pretty(v, indent + 1)
            else:
                print(f"{pad}{k}: {v if not isinstance(v, (dict, list)) else '[]'}")
    elif isinstance(obj, list):
        for v in obj:
            if isinstance(v, (dict, list)):
                print(f"{pad}-")
                _pretty(v, indent + 1)
            else:
                print(f"{pad}- {v}")
    else:
        print(f"{pad}{obj}")


# ---- commands -----------------------------------------------------------

def cmd_init(args) -> int:
    root = _root(args)
    p = root / ".sss" / "manifest.yaml"
    if p.exists() and not args.force:
        m = Manifest.load(root)
    else:
        m = Manifest(root=root, output_dir=args.output_dir, mirror_dirs=list(args.mirror or [".claude/skills"]),
                     link_mode="copy" if args.copy else "symlink")
        m.save()
    for d in (PATCHES_DIR, SOURCES_DIR, LOCAL_DIR, REPORTS_DIR):
        (root / d).mkdir(parents=True, exist_ok=True)
    # Reports are local working documents, never committed.
    (root / REPORTS_DIR / ".gitignore").write_text("*\n!.gitignore\n", encoding="utf-8")
    if not (root / DECISIONS).exists():
        (root / DECISIONS).write_text("# finding-id: accept | {choice: N, note: \"...\"}\n", encoding="utf-8")
    if args.copy and m.link_mode != "copy":
        m.link_mode = "copy"
        m.save()
    res = links.sync_links(m)
    _out(args, {"manifest": str(p.relative_to(root)), "output_dir": m.output_dir, "mirror_dirs": m.mirror_dirs, "link_mode": m.link_mode, "links": res})
    return 0


def cmd_source_add(args) -> int:
    m = Manifest.load(_root(args))
    src = sources.add(m, args.name, args.url, args.ref, args.mode, args.skills_root)
    res = {"source": src.to_dict()}
    if src.mode != "local" and not args.no_sync:
        try:
            res["sync"] = sources.sync(m, src)
        except Exception:
            m.sources = [s for s in m.sources if s.name != src.name]
            m.save()
            shutil.rmtree(m.root / src.path, ignore_errors=True)
            raise
        res["available_skills"] = sources.list_skill_dirs(m, src)
        if not res["available_skills"]:
            res["warning"] = f"no SKILL.md found under {src.path}/{src.skills_root}. Check --skills-root."
    _out(args, res)
    return 0


def cmd_source_remove(args) -> int:
    m = Manifest.load(_root(args))
    res = sources.remove(m, args.name, force=args.force)
    for name in res["skills_dropped"]:
        links.unlink_skill(m, name)
    _out(args, res)
    return 0


def cmd_source_list(args) -> int:
    m = Manifest.load(_root(args))
    _out(args, [{**s.to_dict(), "available_skills": sources.list_skill_dirs(m, s)} for s in m.sources])
    return 0


def cmd_sync(args) -> int:
    m = Manifest.load(_root(args))
    todo = [m.source(args.source)] if args.source else m.sources
    res = [sources.sync(m, s) for s in todo]
    _out(args, {"synced": res, "status": status.check_all(m)})
    return 0


def cmd_import(args) -> int:
    m = Manifest.load(_root(args))
    src_name, _, skill_dir = args.ref.partition("/")
    src = m.source(src_name)
    if not skill_dir:
        raise ManifestError("use <source>/<skill-dir>")
    if skill_dir not in sources.list_skill_dirs(m, src):
        raise ManifestError(f"{skill_dir} not found in source {src_name}. Available: {', '.join(sources.list_skill_dirs(m, src)) or 'none (run sss sync)'}")
    name = args.as_name or skill_dir.rsplit("/", 1)[-1]
    if m.has_skill(name):
        raise ManifestError(f"skill already in manifest: {name}")
    sk = Skill(name=name, source=src_name, skill_dir=skill_dir)
    m.skills.append(sk)
    m.save()
    res: dict = {"imported": sk.to_dict()}
    if args.patch:
        rel = f"{PATCHES_DIR}/{name}.md"
        fp = m.root / rel
        if not fp.exists():
            fp.write_text(patchmod.template(name, args.patch), encoding="utf-8")
        sk.patches.append(rel)
        m.save()
        res["patch_created"] = rel
        res["next"] = f"edit {rel}, then: sss plan {name}"
    elif not args.no_generate:
        res["generated"] = generate.copy(m, sk)
        links.sync_links(m)
    _out(args, res)
    return 0


def cmd_status(args) -> int:
    m = Manifest.load(_root(args))
    res = status.check_all(m)
    if args.skill:
        res = [r for r in res if r["skill"] == args.skill]
    _out(args, res)
    if args.fail_on_stale and any(r["status"] in ("stale", "pending", "conflict", "failed") for r in res):
        return 1
    return 0


def cmd_generate(args) -> int:
    m = Manifest.load(_root(args))
    todo = [m.skill(args.skill)] if args.skill else [k for k in m.skills if not k.patches]
    res = []
    for k in todo:
        if k.patches:
            res.append({"skill": k.name, "action": "needs_agent", "next": f"sss plan {k.name}"})
        else:
            res.append(generate.copy(m, k))
    links.sync_links(m)
    _out(args, res)
    return 0


def cmd_plan(args) -> int:
    m = Manifest.load(_root(args))
    print(generate.dumps(generate.plan(m, m.skill(args.skill))))
    return 0


def cmd_finalize(args) -> int:
    m = Manifest.load(_root(args))
    res = generate.finalize(m, m.skill(args.skill), model=args.model)
    links.sync_links(m)
    _out(args, res)
    return 1 if res["action"] == "failed" else 0


def cmd_conflict(args) -> int:
    m = Manifest.load(_root(args))
    _out(args, generate.conflict(m, m.skill(args.skill), args.reason))
    return 0


def cmd_patch_new(args) -> int:
    m = Manifest.load(_root(args))
    sk = m.skill(args.skill)
    rel = f"{PATCHES_DIR}/{args.skill}.md" if not args.name else f"{PATCHES_DIR}/{args.name}.md"
    fp = m.root / rel
    if fp.exists():
        raise ManifestError(f"patch exists: {rel}")
    fp.write_text(patchmod.template(args.skill, args.intent or "Describe the intent."), encoding="utf-8")
    if rel not in sk.patches:
        sk.patches.append(rel)
    sk.status = "stale"
    m.save()
    _out(args, {"patch": rel, "next": f"edit {rel}, then: sss plan {args.skill}"})
    return 0


def cmd_links(args) -> int:
    m = Manifest.load(_root(args))
    if args.copy and m.link_mode != "copy":
        m.link_mode = "copy"
        m.save()
    _out(args, links.sync_links(m))
    return 0


def cmd_inventory(args) -> int:
    root = _root(args)
    m = Manifest.load(root) if (root / ".sss" / "manifest.yaml").exists() else None
    print(json.dumps(inventory.scan(m, root), indent=2, ensure_ascii=False))
    return 0


def _matrix_paths(args):
    root = _root(args)
    m = Manifest.load(root) if (root / ".sss" / "manifest.yaml").exists() else None
    return root, m, root / REPORTS_DIR / "similarity.json"


def cmd_matrix_pending(args) -> int:
    root, m, mp = _matrix_paths(args)
    inv = inventory.scan(m, root)
    data = matrixmod.load(mp)
    res = matrixmod.pending(inv, data)
    res["stars"] = matrixmod.STARS
    res["identical"] = inv["identical"]
    print(json.dumps(res, indent=2, ensure_ascii=False))
    return 0


def cmd_matrix_apply(args) -> int:
    root, m, mp = _matrix_paths(args)
    inv = inventory.scan(m, root)
    data = matrixmod.load(mp)
    if args.file == "-":
        update = json.load(sys.stdin)
    else:
        fp = Path(args.file)
        if not fp.exists() and (root / fp).exists():
            fp = root / fp
        update = json.loads(fp.read_text(encoding="utf-8"))
    res = matrixmod.apply(inv, data, update)
    matrixmod.save(mp, data)
    print(json.dumps({k: v for k, v in res.items() if k != "summaries_needed" and k != "scores_needed"} | {
        "summaries_still_needed": len(res["summaries_needed"]), "scores_still_needed": len(res["scores_needed"])}, indent=2))
    return 1 if res["errors"] else 0


def cmd_matrix_show(args) -> int:
    root, m, mp = _matrix_paths(args)
    inv = inventory.scan(m, root)
    print(matrixmod.render_table(inv, matrixmod.load(mp)))
    return 0


def cmd_report(args) -> int:
    root = _root(args)
    json_path = Path(args.json_file) if args.json_file else root / REPORTS_DIR / "reorganize-report.json"
    out = Path(args.out) if args.out else root / REPORTS_DIR / "reorganize-report.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    mp = root / REPORTS_DIR / "similarity.json"
    m = Manifest.load(root) if (root / ".sss" / "manifest.yaml").exists() else None
    inv = inventory.scan(m, root) if mp.exists() else None
    warnings = report.render_file(json_path, out, matrix=(inv, matrixmod.load(mp)) if inv else None)
    print(f"wrote {out}")
    for w in warnings:
        print(f"warning: {w}", file=sys.stderr)
    return 0


def cmd_deprecate(args) -> int:
    m = Manifest.load(_root(args))
    _out(args, depmod.run(m, args.skill, keep_patches=args.keep_patches))
    return 0


# ---- parser -------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="sss", description="Skillful-skills-scaler")
    p.add_argument("--root", help="target repo root (default: git toplevel of cwd)")
    p.add_argument("--json", action="store_true", help="machine-readable output")
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("init", help="create .sss/ and link SSS command skills into the repo")
    s.add_argument("--output-dir", default=".agents/skills")
    s.add_argument("--mirror", action="append", help="extra skill dirs to link into (default .claude/skills)")
    s.add_argument("--copy", action="store_true", help="copy instead of symlink (Windows); remembered in the manifest as link_mode")
    s.add_argument("--force", action="store_true", help="rewrite manifest defaults")
    s.set_defaults(fn=cmd_init)

    s = sub.add_parser("source", help="manage sources of truth")
    ss = s.add_subparsers(dest="sub", required=True)
    a = ss.add_parser("add"); a.add_argument("name"); a.add_argument("url", nargs="?")
    a.add_argument("--ref", default="main"); a.add_argument("--mode", default="copy", choices=["copy", "submodule", "local"])
    a.add_argument("--skills-root", default="skills"); a.add_argument("--no-sync", action="store_true")
    a.set_defaults(fn=cmd_source_add)
    ls = ss.add_parser("list"); ls.set_defaults(fn=cmd_source_list)
    rm = ss.add_parser("remove"); rm.add_argument("name"); rm.add_argument("--force", action="store_true", help="also drop skills imported from it")
    rm.set_defaults(fn=cmd_source_remove)

    s = sub.add_parser("sync", help="refresh replicas and report staleness"); s.add_argument("source", nargs="?"); s.set_defaults(fn=cmd_sync)

    s = sub.add_parser("import", help="add <source>/<skill-dir> to the manifest")
    s.add_argument("ref"); s.add_argument("--as", dest="as_name"); s.add_argument("--patch", metavar="INTENT", help="also create a patch with this intent")
    s.add_argument("--no-generate", action="store_true"); s.set_defaults(fn=cmd_import)

    s = sub.add_parser("status", help="fresh, stale, pending, conflict or failed, per skill")
    s.add_argument("skill", nargs="?"); s.add_argument("--fail-on-stale", action="store_true", help="exit 1 if anything is not ok (for CI)")
    s.set_defaults(fn=cmd_status)

    s = sub.add_parser("generate", help="copy unpatched skills into the output dir"); s.add_argument("skill", nargs="?"); s.set_defaults(fn=cmd_generate)
    s = sub.add_parser("plan", help="print the job for the agent to apply a skill's patches"); s.add_argument("skill"); s.set_defaults(fn=cmd_plan)
    s = sub.add_parser("finalize", help="validate and stamp an agent-written skill"); s.add_argument("skill"); s.add_argument("--model"); s.set_defaults(fn=cmd_finalize)
    s = sub.add_parser("conflict", help="record that a patch no longer applies"); s.add_argument("skill"); s.add_argument("--reason", required=True); s.set_defaults(fn=cmd_conflict)

    s = sub.add_parser("patch", help="manage patches"); ps = s.add_subparsers(dest="sub", required=True)
    n = ps.add_parser("new"); n.add_argument("skill"); n.add_argument("--intent"); n.add_argument("--name"); n.set_defaults(fn=cmd_patch_new)

    s = sub.add_parser("links", help="re-link skills into output and mirror dirs"); s.add_argument("--copy", action="store_true"); s.set_defaults(fn=cmd_links)
    s = sub.add_parser("inventory", help="JSON of every skill in the repo plus duplicate candidates"); s.set_defaults(fn=cmd_inventory)
    s = sub.add_parser("matrix", help="coverage matrix bookkeeping: pending work, apply agent scores, show the table")
    ms = s.add_subparsers(dest="sub", required=True)
    mp_ = ms.add_parser("pending", help="skills needing a summary and pairs needing a 0-5 star score"); mp_.set_defaults(fn=cmd_matrix_pending)
    ma = ms.add_parser("apply", help="merge {summaries:{id:text}, scores:[{a,b,stars,reason}]} from a JSON file or '-'"); ma.add_argument("file"); ma.set_defaults(fn=cmd_matrix_apply)
    msh = ms.add_parser("show", help="print the matrix as markdown"); msh.set_defaults(fn=cmd_matrix_show)

    s = sub.add_parser("report", help="render the reorganize report (markdown) from its JSON; both live in .sss/reports/, which is gitignored")
    s.add_argument("json_file", nargs="?", help="default .sss/reports/reorganize-report.json"); s.add_argument("--out", help="default .sss/reports/reorganize-report.md"); s.set_defaults(fn=cmd_report)
    s = sub.add_parser("deprecate", help="remove a skill, its patches, output and links; list references"); s.add_argument("skill"); s.add_argument("--keep-patches", action="store_true"); s.set_defaults(fn=cmd_deprecate)
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        return args.fn(args)
    except (ManifestError, gitutil.GitError, OSError, subprocess.CalledProcessError) as e:
        print(f"error: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
