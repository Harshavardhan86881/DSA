#!/usr/bin/env python3
"""Validate relative Markdown links inside this repository.

Rules:
* Only relative links are checked. External links (http, https, mailto) are ignored here;
  they are verified manually and recorded in docs/resources.md.
* Links inside fenced code blocks are ignored, because code samples often contain
  example link syntax that is not a real link.
* A link may point at a file or a directory inside the repository. Anchors are ignored.

Exit status: 0 when every relative link resolves, 1 otherwise.
"""

from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import unquote

REPO_ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv", ".pytest_cache"}
FENCE_RE = re.compile(r"^\s*(```|~~~)")
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
SCHEME_RE = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.\-]*:")


def iter_markdown_files() -> list[Path]:
    """Return every Markdown file in the repository, excluding skipped directories."""
    files: list[Path] = []
    for path in sorted(REPO_ROOT.rglob("*.md")):
        if SKIP_DIRS & set(path.relative_to(REPO_ROOT).parts):
            continue
        files.append(path)
    return files


def strip_code_blocks(text: str) -> str:
    """Remove fenced code blocks so example links inside them are not validated."""
    kept: list[str] = []
    inside_fence = False
    for line in text.splitlines():
        if FENCE_RE.match(line):
            inside_fence = not inside_fence
            continue
        if not inside_fence:
            kept.append(line)
    return "\n".join(kept)


def parse_target(raw: str) -> str | None:
    """Extract the path part of a Markdown link target, or None if it should be skipped."""
    target = raw.strip()
    if not target:
        return None
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1].strip()
    # Drop an optional title: (path/to/file.md "some title")
    if " " in target and not SCHEME_RE.match(target):
        target = target.split()[0]
    if target.startswith("#") or SCHEME_RE.match(target):
        return None
    path_only = target.split("#", 1)[0].split("?", 1)[0]
    if not path_only:
        return None
    return path_only


def resolve(source_file: Path, path_only: str) -> Path:
    """Resolve a relative link target to an absolute path inside the repository."""
    if path_only.startswith("/"):
        return (REPO_ROOT / path_only.lstrip("/")).resolve()
    return (source_file.parent / unquote(path_only)).resolve()


def main() -> int:
    """Check every relative link and print a summary."""
    checked = 0
    problems: list[str] = []

    for md_file in iter_markdown_files():
        text = strip_code_blocks(md_file.read_text(encoding="utf-8"))
        rel_source = md_file.relative_to(REPO_ROOT)
        for line_number, line in enumerate(text.splitlines(), start=1):
            for raw_target in LINK_RE.findall(line):
                path_only = parse_target(raw_target)
                if path_only is None:
                    continue
                checked += 1
                destination = resolve(md_file, path_only)
                if not destination.exists():
                    problems.append(
                        f"{rel_source}:{line_number}: broken link -> {raw_target.strip()}"
                    )

    print(f"Checked {checked} relative link(s) in {len(iter_markdown_files())} Markdown file(s).")
    if problems:
        print(f"\nFAILED: {len(problems)} broken relative link(s):")
        for problem in problems:
            print(f"  - {problem}")
        return 1
    print("OK: every relative link resolves to an existing path.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
