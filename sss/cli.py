"""sss command line. Deterministic steps only; model steps are done by the agent
following skills/*/SKILL.md, which call these commands."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from . import deprecate as depmod, generate, inventory, links, patches as patchmod, report, sources, status
from .manifest import DECISIONS, LOCAL_DIR, PATCHES_DIR, SOURCES_DIR, Manifest, ManifestError, Skill
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
        m = Manifest(root=root, output_dir=args.output_dir, mirror_dirs=list(args.mirror or [".claude/skills"]))
        m.save()
    for d in (PATCHES_DIR, SOURCES_DIR, LOCAL_DIR):
        (root / d).mkdir(parents=True, exist_ok=True)
    if not (root / DECISIONS).exists():
        (root / DECISIONS).write_text("# finding-id: accept | {choice: N, note: \"...\"}\n", encoding="utf-8")
    res = links.sync_links(m, copy=args.copy)
    _out(args, {"manifest": str(p.relative_to(root)), "output_dir": m.output_dir, "mirror_dirs": m.mirror_dirs, "links": res})
    return 0


def cmd_source_add(args) -> int:
    m = Manifest.load(_root(args))
    src = sources.add(m, args.name, args.url, args.ref, args.mode, args.skills_root)
    res = {"source": src.to_dict()}
    if src.mode != "local" and not args.no_sync:
        res["sync"] = sources.sync(m, src)
        res["available_skills"] = sources.list_skill_dirs(m, src)
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
    name = args.as_name or skill_dir
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
    _out(args, links.sync_links(m, copy=args.copy))
    return 0


def cmd_inventory(args) -> int:
    root = _root(args)
    m = Manifest.load(root) if (root / ".sss" / "manifest.yaml").exists() else None
    print(json.dumps(inventory.scan(m, root), indent=2, ensure_ascii=False))
    return 0


def cmd_report(args) -> int:
    report.render_file(Path(args.json_file), Path(args.out))
    print(f"wrote {args.out}")
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
    s.add_argument("--copy", action="store_true", help="copy instead of symlink (Windows)")
    s.add_argument("--force", action="store_true", help="rewrite manifest defaults")
    s.set_defaults(fn=cmd_init)

    s = sub.add_parser("source", help="manage sources of truth")
    ss = s.add_subparsers(dest="sub", required=True)
    a = ss.add_parser("add"); a.add_argument("name"); a.add_argument("url", nargs="?")
    a.add_argument("--ref", default="main"); a.add_argument("--mode", default="copy", choices=["copy", "submodule", "local"])
    a.add_argument("--skills-root", default="skills"); a.add_argument("--no-sync", action="store_true")
    a.set_defaults(fn=cmd_source_add)
    ls = ss.add_parser("list"); ls.set_defaults(fn=cmd_source_list)

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
    s = sub.add_parser("report", help="render reorganize-report.md from JSON"); s.add_argument("json_file"); s.add_argument("--out", default="reorganize-report.md"); s.set_defaults(fn=cmd_report)
    s = sub.add_parser("deprecate", help="remove a skill, its patches, output and links; list references"); s.add_argument("skill"); s.add_argument("--keep-patches", action="store_true"); s.set_defaults(fn=cmd_deprecate)
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        return args.fn(args)
    except (ManifestError, FileNotFoundError, gitutil.GitError) as e:
        print(f"error: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
