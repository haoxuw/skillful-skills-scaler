# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""End-to-end: a source repo, a target repo, and the sss CLI driving the full loop."""
from __future__ import annotations

import json
import os
import subprocess
from pathlib import Path

import pytest

from sss import frontmatter
from sss.cli import main

OMELETTE = """---
name: omelette
description: How to make a plain omelette.
---

# Omelette

To make an omelette, break two eggs, 1 butter, 1 tomato.
See [the pan guide](pan.md).
"""
SALAD = """---
name: salad
description: How to make a green salad.
---

# Salad

Wash lettuce, add dressing.
"""


def git(cwd: Path, *args: str) -> str:
    return subprocess.run(["git", *args], cwd=cwd, check=True, capture_output=True, text=True).stdout


def init_repo(path: Path) -> Path:
    path.mkdir(parents=True, exist_ok=True)
    git(path, "init", "-q", "-b", "main")
    git(path, "config", "user.email", "t@example.com")
    git(path, "config", "user.name", "Test")
    git(path, "config", "commit.gpgsign", "false")
    return path


def commit_all(repo: Path, msg: str) -> str:
    git(repo, "add", "-A")
    git(repo, "commit", "-q", "-m", msg)
    return git(repo, "rev-parse", "HEAD").strip()


def run(root: Path, *args: str) -> tuple[int, dict | list]:
    out = subprocess.run(
        [os.sys.executable, str(Path(__file__).resolve().parent.parent / "sss.py"), "--root", str(root), "--json", *args],
        capture_output=True, text=True,
    )
    data = json.loads(out.stdout) if out.stdout.strip().startswith(("{", "[")) else {"stdout": out.stdout, "stderr": out.stderr}
    return out.returncode, data


@pytest.fixture
def source(tmp_path: Path) -> Path:
    src = init_repo(tmp_path / "cookbook")
    (src / "skills" / "omelette").mkdir(parents=True)
    (src / "skills" / "omelette" / "SKILL.md").write_text(OMELETTE)
    (src / "skills" / "omelette" / "pan.md").write_text("Use a non-stick pan.\n")
    (src / "skills" / "salad").mkdir(parents=True)
    (src / "skills" / "salad" / "SKILL.md").write_text(SALAD)
    (src / "LICENSE").write_text("Apache License 2.0\n")
    commit_all(src, "cookbook v1")
    return src


@pytest.fixture
def target(tmp_path: Path) -> Path:
    t = init_repo(tmp_path / "kitchen")
    (t / "README.md").write_text("# kitchen\n")
    commit_all(t, "init")
    return t


def test_full_loop(source: Path, target: Path):
    # init: manifest, dirs, SSS command skills linked into both runtimes' dirs
    rc, res = run(target, "init")
    assert rc == 0, res
    assert (target / ".sss" / "manifest.yaml").is_file()
    assert (target / ".sss" / "reports" / ".gitignore").read_text().startswith("*")
    assert (target / ".agents" / "skills" / "update-skills").is_symlink()
    assert (target / ".claude" / "skills" / "update-skills" / "SKILL.md").is_file()

    # add a source: replica is vendored letter for letter, with LICENSE
    rc, res = run(target, "source", "add", "cookbook", f"file://{source}", "--ref", "main")
    assert rc == 0, res
    assert res["available_skills"] == ["omelette", "salad"]
    replica = target / ".sss" / "sources" / "cookbook"
    assert (replica / "skills" / "omelette" / "SKILL.md").read_text() == OMELETTE
    assert (replica / "LICENSE").is_file()
    assert (replica / ".git").exists() is False

    # import an unpatched skill: deterministic copy with provenance
    rc, res = run(target, "import", "cookbook/salad")
    assert rc == 0, res
    out = target / ".agents" / "skills" / "salad" / "SKILL.md"
    meta, body = frontmatter.read(out)
    assert meta["name"] == "salad"
    assert meta["metadata"]["sss"]["source"] == "cookbook"
    assert "Wash lettuce" in body
    assert (target / ".claude" / "skills" / "salad").is_symlink()

    # import a patched skill: patch template created, nothing generated yet
    rc, res = run(target, "import", "cookbook/omelette", "--patch", "House omelette")
    assert rc == 0, res
    patch = target / ".sss" / "patches" / "omelette.md"
    assert patch.is_file()
    patch.write_text(
        "---\ntarget: omelette\nintent: House omelette\nchecks:\n"
        "  - The final skill says three eggs.\n  - contains: \"three eggs\"\n  - not_contains: \"two eggs\"\n  - file_exists: pan.md\n---\n"
        "Add one more egg and bell pepper. Keep everything else exactly as the source has it.\n"
    )
    rc, st = run(target, "status", "omelette")
    assert st[0]["status"] == "pending"

    # plan hands the agent everything
    rc, plan = run(target, "plan", "omelette")
    assert rc == 0, plan
    assert plan["source"]["dir"] == ".sss/sources/cookbook/skills/omelette"
    assert plan["deterministic_checks"] == [{"contains": "three eggs"}, {"not_contains": "two eggs"}, {"file_exists": "pan.md"}]
    assert plan["sentence_checks"] == ["The final skill says three eggs."]

    # simulate the agent: first a wrong attempt (finalize must fail), then a right one
    out_dir = target / plan["output_dir"]
    out_dir.mkdir(parents=True)
    (out_dir / "SKILL.md").write_text(OMELETTE)  # unchanged: still "two eggs", no pan.md
    rc, res = run(target, "finalize", "omelette")
    assert rc == 1 and res["action"] == "failed"
    assert len(res["failures"]) == 3
    (out_dir / "SKILL.md").write_text(OMELETTE.replace("two eggs", "three eggs").replace("1 tomato.", "1 tomato, bell pepper."))
    (out_dir / "pan.md").write_text("Use a non-stick pan.\n")
    rc, res = run(target, "finalize", "omelette", "--model", "test-model")
    assert rc == 0, res
    meta, body = frontmatter.read(out_dir / "SKILL.md")
    assert meta["metadata"]["sss"]["patches"] == [".sss/patches/omelette.md"]
    assert meta["metadata"]["sss"]["model"] == "test-model"
    assert "three eggs" in body

    # everything committed: all ok, CI gate passes
    commit_all(target, "import skills")
    rc, st = run(target, "status", "--fail-on-stale")
    assert rc == 0, st
    assert {s["status"] for s in st} == {"ok"}

    # upstream changes salad only; sync marks salad stale, omelette stays ok
    (source / "skills" / "salad" / "SKILL.md").write_text(SALAD.replace("add dressing", "add dressing and nuts"))
    v2 = commit_all(source, "cookbook v2")
    rc, res = run(target, "sync")
    assert rc == 0, res
    assert res["synced"][0]["changed"] is True and res["synced"][0]["new"] == v2
    by = {s["skill"]: s for s in res["status"]}
    assert by["salad"]["status"] == "stale", by["salad"]
    assert by["omelette"]["status"] == "ok", by["omelette"]
    rc, _ = run(target, "status", "--fail-on-stale")
    assert rc == 1

    # regenerate the unpatched one; commit; green again
    rc, res = run(target, "generate", "salad")
    assert rc == 0 and res[0]["action"] == "copied"
    assert "nuts" in (target / ".agents" / "skills" / "salad" / "SKILL.md").read_text()
    commit_all(target, "sync cookbook")
    rc, _ = run(target, "status", "--fail-on-stale")
    assert rc == 0

    # editing a patch makes its skill stale even before commit
    patch.write_text(patch.read_text() + "\nAlso add chives.\n")
    rc, st = run(target, "status", "omelette")
    assert st[0]["status"] == "stale" and any("uncommitted" in r for r in st[0]["reasons"])
    commit_all(target, "edit patch")
    rc, st = run(target, "status", "omelette")
    assert st[0]["status"] == "stale" and any("input changed" in r for r in st[0]["reasons"])

    # plan now offers the previous source for a minimal re-apply
    rc, plan = run(target, "plan", "omelette")
    assert plan["previous_output_exists"] is True
    assert plan["previous_source_dir"] and (Path(plan["previous_source_dir"]) / "SKILL.md").is_file()

    # conflict is a first-class state
    rc, res = run(target, "conflict", "omelette", "--reason", "source dropped the eggs step")
    assert rc == 0
    rc, st = run(target, "status", "omelette")
    assert st[0]["status"] == "conflict"

    # inventory sees generated skills once (mirrors deduped), not the replica
    rc, inv = run(target, "inventory")
    ids = sorted(s["id"] for s in inv["skills"])
    assert "salad" in ids and "omelette" in ids
    assert all(not s["path"].startswith(".sss/") for s in inv["skills"])
    assert all(not s["path"].startswith(".claude/") for s in inv["skills"])
    om = next(s for s in inv["skills"] if s["id"] == "omelette")
    assert om["broken_references"] == [] and "pan.md" in om["references"]

    # deprecate removes output, links, patch, and lists leftover references
    (target / "docs.md").write_text("Try the salad skill.\n")
    rc, res = run(target, "deprecate", "salad")
    assert rc == 0, res
    assert not (target / ".agents" / "skills" / "salad").exists()
    assert not (target / ".claude" / "skills" / "salad").exists()
    assert any(r["file"] == "docs.md" for r in res["references"])
    rc, st = run(target, "status")
    assert [s["skill"] for s in st] == ["omelette"]

    # a source in use cannot be removed without --force; with it, replica and skills go
    rc, res = run(target, "source", "remove", "cookbook")
    assert rc == 2
    rc, res = run(target, "source", "remove", "cookbook", "--force")
    assert rc == 0 and res["skills_dropped"] == ["omelette"]
    assert not (target / ".sss" / "sources" / "cookbook").exists()
    assert not (target / ".agents" / "skills" / "omelette").exists()


def test_local_source(target: Path):
    assert run(target, "init")[0] == 0
    rc, res = run(target, "source", "add", "mine", "--mode", "local")
    assert rc == 0, res
    d = target / ".sss" / "local" / "toast"
    d.mkdir(parents=True)
    (d / "SKILL.md").write_text("---\nname: toast\ndescription: Make toast.\n---\n\nToast bread.\n")
    rc, res = run(target, "import", "mine/toast")
    assert rc == 0, res
    meta, body = frontmatter.read(target / ".agents" / "skills" / "toast" / "SKILL.md")
    assert meta["metadata"]["sss"]["source"] == "mine" and "Toast bread" in body
    commit_all(target, "local skill")
    rc, st = run(target, "status", "--fail-on-stale")
    assert rc == 0 and st[0]["status"] == "ok"
    (d / "SKILL.md").write_text("---\nname: toast\ndescription: Make toast.\n---\n\nToast bread well.\n")
    rc, st = run(target, "status", "toast")
    assert st[0]["status"] == "stale"


def test_copy_mode(source: Path, target: Path):
    assert run(target, "init", "--copy")[0] == 0
    assert not (target / ".agents" / "skills" / "update-skills").is_symlink()
    assert run(target, "source", "add", "cookbook", f"file://{source}")[0] == 0
    assert run(target, "import", "cookbook/salad")[0] == 0
    mirror = target / ".claude" / "skills" / "salad"
    assert mirror.is_dir() and not mirror.is_symlink(), "copy mode must persist across commands"
    assert (mirror / "SKILL.md").read_text() == (target / ".agents" / "skills" / "salad" / "SKILL.md").read_text()


def test_matrix(source: Path, target: Path):
    assert run(target, "init")[0] == 0
    assert run(target, "source", "add", "cookbook", f"file://{source}")[0] == 0
    for sk in ("salad", "omelette"):
        assert run(target, "import", f"cookbook/{sk}")[0] == 0
    rc, pend = run(target, "matrix", "pending")
    assert rc == 0 and pend["pairs_total"] == 1 and len(pend["summaries_needed"]) == 2 and len(pend["scores_needed"]) == 1
    (target / "scores.json").write_text(json.dumps({
        "summaries": {"salad": "Makes a salad.", "omelette": "Makes an omelette."},
        "scores": [{"a": "salad", "b": "omelette", "stars": 4, "reason": ""}]}))
    rc, res = run(target, "matrix", "apply", "scores.json")
    assert rc == 0 and res["scores_still_needed"] == 0 and res["summaries_still_needed"] == 0, res
    # a low score without a reason is rejected
    (target / "bad.json").write_text(json.dumps({"scores": [{"a": "salad", "b": "omelette", "stars": 1}]}))
    rc, res = run(target, "matrix", "apply", "bad.json")
    assert rc == 1 and res["errors"]
    # changing a skill invalidates only its pairs
    (target / ".sss" / "sources" / "cookbook" / "skills" / "salad" / "SKILL.md").write_text(SALAD + "\nAdd nuts.\n")
    assert run(target, "generate", "salad")[0] == 0
    rc, pend = run(target, "matrix", "pending")
    assert [x["id"] for x in pend["summaries_needed"]] == ["salad"] and len(pend["scores_needed"]) == 1
    # the report appends the matrix
    (target / ".sss" / "reports" / "reorganize-report.json").write_text(json.dumps({"inventory": [], "findings": []}))
    assert run(target, "report")[0] == 0
    md = (target / ".sss" / "reports" / "reorganize-report.md").read_text()
    assert "## Appendix: coverage matrix" in md and "| **S1** omelette |" in md


def test_inventory_when_claude_skills_is_a_symlink_to_agents_skills(target: Path):
    # Some repos point .claude/skills at .agents/skills as one directory link.
    (target / ".agents" / "skills" / "local-one").mkdir(parents=True)
    (target / ".agents" / "skills" / "local-one" / "SKILL.md").write_text("---\nname: local-one\ndescription: One.\n---\n\nBody.\n")
    (target / ".claude").mkdir()
    os.symlink("../.agents/skills", target / ".claude" / "skills")
    assert run(target, "init")[0] == 0
    rc, inv = run(target, "inventory")
    assert rc == 0 and [s["id"] for s in inv["skills"]] == ["local-one"], inv
    assert inv["skills"][0]["path"] == ".agents/skills/local-one"   # real location, never the mirror


def test_frontmatter_repair_keeps_structure():
    bad = "---\nname: audit\ndescription: Use when asked to run an audit: a run collects and publishes.\nmetadata:\n  version: 1\nallowed-tools:\n  - Bash\n---\n\nBody.\n"
    meta, body = frontmatter.split(bad)
    assert meta["name"] == "audit" and meta["description"].startswith("Use when asked to run an audit: a run")
    assert meta["metadata"] == {"version": 1} and meta["allowed-tools"] == ["Bash"]   # nested shapes survive
    assert "_frontmatter_error" in meta and body.strip() == "Body."
    # internal flags never reach disk
    assert "_frontmatter_error" not in frontmatter.join(meta, body)


def test_generate_refuses_invalid_frontmatter(source: Path, target: Path):
    (source / "skills" / "broken").mkdir()
    (source / "skills" / "broken" / "SKILL.md").write_text("---\nname: broken\ndescription: a: b: [c\n---\n\nx\n")
    commit_all(source, "broken skill")
    assert run(target, "init")[0] == 0
    assert run(target, "source", "add", "cookbook", f"file://{source}")[0] == 0
    rc, res = run(target, "import", "cookbook/broken")
    assert rc == 2 and "not valid YAML" in res["stderr"]
    assert not (target / ".agents" / "skills" / "broken" / "SKILL.md").exists()


def test_report_render(tmp_path: Path):
    data = {
        "inventory": [{"id": "a", "source": "local", "path": "x/a", "files": 1, "words": 10},
                      {"id": "b", "source": "cookbook", "path": "x/b", "files": 1, "words": 12}],
        "findings": [
            {"type": "duplicate", "skills": ["a", "b"], "why_it_matters": "Both explain the same thing.",
             "evidence": [{"skill": "a", "file": "SKILL.md", "line": 3, "quote": "wash lettuce"}],
             "recommendation": "Keep b.", "confidence": "likely", "proposed_action": {"verb": "remove", "from": ["a"]}},
            {"type": "conflict", "skills": ["a", "b"], "why_it_matters": "Agents get two answers.",
             "evidence": [{"skill": "a", "quote": "two eggs"}, {"skill": "b", "quote": "three eggs"}],
             "recommendation": "Keep b.", "confidence": "confident", "proposed_action": {"verb": "patch"}},
        ],
    }
    jp = tmp_path / "r.json"; jp.write_text(json.dumps(data))
    rc = main(["report", str(jp), "--out", str(tmp_path / "r.md")])
    assert rc == 0
    md = (tmp_path / "r.md").read_text()
    back = json.loads(jp.read_text())
    for i in range(1, 10):
        assert f"## {i}. " in md
    assert "## 10. " not in md and "left alone" not in md.lower()
    assert md.index("## 2. Conflicts") < md.index("## 3. Out of date") < md.index("## 7. What we looked at")
    assert "| Are any skills duplicated? | Yes, 1 |" in md
    assert "| Are any skills out of date? | No |" in md
    assert back["summary"]["decisions_needed"] == 2          # remove and conflict are distinct actions
    assert back["summary"]["findings_total"] == 2
    assert back["findings"][0]["id"].startswith("dup-") and back["findings"][1]["id"].startswith("conf-")
    assert "Open an issue upstream" in md and "Waiting on your decision" in md
    assert "Nothing found." in md                              # empty sections still appear
    assert "## Appendix: every skill we found" in md
    assert "### a" in md and "duplicate with b [dup-" in md and "- **Concerns:** none" not in md.split("### a")[1].split("### b")[0]
