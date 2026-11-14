#!/usr/bin/env python3
"""Build /original for Claude Code and claude.ai from one source.

    python3 build.py            build everything into dist/
    python3 build.py --install  build, then install the Claude Code version into
                                ~/.claude/skills/original/ (keeps runs/)

Source: src/core.md. Blocks wrapped in <!-- if code --> ... <!-- end --> (one or more
target names after "if") appear only in those targets. No nesting.
"""
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
DIST = ROOT / "dist"
INSTALL_DIR = Path.home() / ".claude" / "skills" / "original"
TARGETS = ["code", "claude-ai"]

FRONTMATTER = {
    "code": {
        "description": (
            "Gives a non-default answer to an open task (an essay angle, an argument, a pitch, "
            "a strategy, a product or research idea, a talk, a post). Writes what everyone would "
            "get, asks Anshul a few targeted questions, then builds from what only he knows. Use "
            "for /original, or when he says \"not the generic answer\", \"make this less generic\", "
            "\"what would everyone else get\" or \"give me an angle nobody else has\". Also for "
            "\"/original export\" or \"export this run\" to make a PDF of a run. Not for tasks with "
            "one right answer."
        ),
        "extra": ['user-invocable: true', 'argument-hint: "<the task, pasted as-is> | export [run]"'],
        "max_description": 1024,
    },
    "claude-ai": {
        "description": (
            "Gives a non-default answer to an open task. Writes what everyone would get, asks a few "
            "targeted questions, then builds from your answers. Use for /original or \"not the generic answer\"."
        ),
        "extra": [],
        "max_description": 200,
    },
}
IF_RE = re.compile(r"^<!-- if ([\w\- ]+) -->\s*$")
END_RE = re.compile(r"^<!-- end -->\s*$")


def render(core: str, target: str) -> str:
    out, keep, inside = [], True, False
    for n, line in enumerate(core.splitlines(), 1):
        m = IF_RE.match(line)
        if m:
            if inside:
                sys.exit(f"core.md:{n}: nested <!-- if --> block")
            names = m.group(1).split()
            unknown = set(names) - set(TARGETS)
            if unknown:
                sys.exit(f"core.md:{n}: unknown target(s) {sorted(unknown)}")
            inside, keep = True, target in names
            continue
        if END_RE.match(line):
            if not inside:
                sys.exit(f"core.md:{n}: <!-- end --> without <!-- if -->")
            inside, keep = False, True
            continue
        if keep:
            out.append(line)
    if inside:
        sys.exit("core.md: unclosed <!-- if --> block")
    text = "\n".join(out)
    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"
    if "<!--" in text:
        sys.exit(f"{target}: stray HTML comment left in output")
    return text


def check_description(target: str, desc: str, limit: int) -> None:
    problems = []
    if len(desc) > limit:
        problems.append(f"{len(desc)} chars, limit {limit}")
    if ": " in desc or " #" in desc:
        problems.append("contains ': ' or ' #', which breaks unquoted YAML")
    if desc[:1] in "\"'[{&*!|>%@`":
        problems.append("starts with a YAML special character")
    if problems:
        sys.exit(f"{target} description: " + "; ".join(problems))


def skill_md(target: str, body: str) -> str:
    fm = FRONTMATTER[target]
    check_description(target, fm["description"], fm["max_description"])
    lines = ["---", "name: original", f"description: {fm['description']}", *fm["extra"], "---", ""]
    return "\n".join(lines) + "\n" + body


def yaml_parses(path: Path) -> None:
    """Best-effort YAML check with Ruby's parser, if Ruby is present."""
    if not shutil.which("ruby"):
        return
    code = ('y=YAML.load(File.read(ARGV[0], encoding: "UTF-8").split(/^---$/)[1]); '
            'abort("missing name/description") unless y["name"] && y["description"]')
    r = subprocess.run(["ruby", "-ryaml", "-e", code, str(path)], capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f"{path}: frontmatter does not parse:\n{r.stderr}")


def write_skill_dir(dest: Path, target: str, body: str) -> Path:
    skill = dest / "original"
    (skill / "references").mkdir(parents=True)
    (skill / "SKILL.md").write_text(skill_md(target, body), encoding="utf-8")
    yaml_parses(skill / "SKILL.md")
    for ref in sorted((SRC / "references").glob("*.md")):
        shutil.copy2(ref, skill / "references" / ref.name)
    if target == "code":
        shutil.copy2(SRC / "export_pdf.py", skill / "export_pdf.py")
    return skill


def zip_dir(skill: Path, zip_path: Path) -> None:
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for p in sorted(skill.rglob("*")):
            if p.name.startswith("."):
                continue
            z.write(p, p.relative_to(skill.parent).as_posix())


def build() -> dict:
    core = (SRC / "core.md").read_text(encoding="utf-8")
    if DIST.exists():
        shutil.rmtree(DIST)
    report = {}

    for target in TARGETS:
        body = render(core, target)
        dest = DIST / target
        skill = write_skill_dir(dest, target, body)
        report[target] = {"body": len(body), "description": len(FRONTMATTER[target]["description"])}
        if target != "code":
            zip_dir(skill, dest / "original-skill.zip")

    return report


def install() -> None:
    built = DIST / "code" / "original"
    INSTALL_DIR.mkdir(parents=True, exist_ok=True)
    for p in INSTALL_DIR.iterdir():
        if p.name == "runs":
            continue
        shutil.rmtree(p) if p.is_dir() else p.unlink()
    for p in built.iterdir():
        (shutil.copytree if p.is_dir() else shutil.copy2)(p, INSTALL_DIR / p.name)
    (INSTALL_DIR / "runs").mkdir(exist_ok=True)
    print(f"installed into {INSTALL_DIR} (runs/ kept)")


if __name__ == "__main__":
    for target, r in build().items():
        print(f"{target:11} " + ", ".join(f"{k} {v:,}" for k, v in r.items()))
    print(f"built into {DIST}")
    if "--install" in sys.argv:
        install()
