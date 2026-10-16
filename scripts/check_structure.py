#!/usr/bin/env python3
"""Validate the repository structure and guard against placeholder content.

Checks performed:
1. Required files and directories for the 7-week course exist.
2. Every directory that is intentionally empty contains a .gitkeep file, so the layout
   survives a fresh clone.
3. No .gitkeep file is left behind in a directory that has real content.
4. No placeholder markers (TODO, TBD, FIXME, lorem ipsum, "to be added") exist in the
   committed Markdown.

Exit status: 0 when everything is in order, 1 otherwise.
"""

from __future__ import annotations

import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv", ".pytest_cache"}

WEEKS = [
    "week-01-foundations",
    "week-02-two-pointers-sliding-window-binary-search",
    "week-03-linked-lists-stacks-queues",
    "week-04-recursion-trees-heaps",
    "week-05-graphs",
    "week-06-backtracking-greedy-dynamic-programming",
    "week-07-revision-mock-interviews",
]

REQUIRED_FILES = [
    "README.md",
    "CONTRIBUTING.md",
    ".gitignore",
    "docs/course-overview.md",
    "docs/learning-method.md",
    "docs/problem-solving-framework.md",
    "docs/complexity-cheatsheet.md",
    "docs/resources.md",
    "docs/progress-guide.md",
    "templates/lesson-template.md",
    "templates/coding-problem-template.md",
    "templates/daily-study-template.md",
    "templates/mistake-notebook-template.md",
    "progress-tracking/overall-progress.md",
    "progress-tracking/problem-tracker.csv",
    "projects/README.md",
    "scripts/check_links.py",
    "scripts/check_structure.py",
    ".github/workflows/validate.yml",
    *[f"{week}/README.md" for week in WEEKS],
]

REQUIRED_DIRS = [
    "docs",
    "templates",
    "scripts",
    "projects",
    "progress-tracking",
    ".github/workflows",
    # Week 1 has its full planned internal structure.
    "week-01-foundations/curriculum",
    "week-01-foundations/lessons/problem-solving",
    "week-01-foundations/lessons/complexity",
    "week-01-foundations/lessons/arrays",
    "week-01-foundations/lessons/strings",
    "week-01-foundations/lessons/hashing",
    "week-01-foundations/lessons/prefix-sums",
    "week-01-foundations/examples",
    "week-01-foundations/exercises/starter-code",
    "week-01-foundations/exercises/test-cases",
    "week-01-foundations/exercises/solutions",
    "week-01-foundations/problems/easy",
    "week-01-foundations/problems/intermediate",
    "week-01-foundations/interview-prep",
    "week-01-foundations/revision",
    "week-01-foundations/assessments",
    "week-01-foundations/progress",
    # Weeks 2-7 share one internal layout, created when each week is scoped.
    *[
        f"{week}/{sub}"
        for week in WEEKS[1:]
        for sub in (
            "lessons",
            "examples",
            "exercises",
            "problems",
            "interview-prep",
            "revision",
            "assessments",
        )
    ],
]

PLACEHOLDER_PATTERNS = [
    (re.compile(r"\bTODO\b"), "TODO marker"),
    (re.compile(r"\bTBD\b"), "TBD marker"),
    (re.compile(r"\bFIXME\b"), "FIXME marker"),
    (re.compile(r"lorem ipsum", re.IGNORECASE), "lorem ipsum filler text"),
    (re.compile(r"to be added", re.IGNORECASE), "deferred content ('to be added')"),
    (re.compile(r"coming soon", re.IGNORECASE), "deferred content ('coming soon')"),
]


def iter_all_files() -> list[Path]:
    """Return every file in the repository, excluding skipped directories."""
    files: list[Path] = []
    for path in sorted(REPO_ROOT.rglob("*")):
        if not path.is_file():
            continue
        if SKIP_DIRS & set(path.relative_to(REPO_ROOT).parts):
            continue
        files.append(path)
    return files


def iter_all_dirs() -> list[Path]:
    """Return every directory in the repository, excluding skipped directories."""
    dirs: list[Path] = []
    for path in sorted(REPO_ROOT.rglob("*")):
        if not path.is_dir():
            continue
        if SKIP_DIRS & set(path.relative_to(REPO_ROOT).parts):
            continue
        dirs.append(path)
    return dirs


def check_required_paths() -> list[str]:
    """Verify that all required files and directories exist."""
    problems: list[str] = []
    for relative in REQUIRED_FILES:
        if not (REPO_ROOT / relative).is_file():
            problems.append(f"missing required file: {relative}")
    for relative in REQUIRED_DIRS:
        if not (REPO_ROOT / relative).is_dir():
            problems.append(f"missing required directory: {relative}")
    return problems


def check_gitkeep_files() -> list[str]:
    """Empty directories must carry .gitkeep; non-empty ones must not."""
    problems: list[str] = []
    for directory in iter_all_dirs():
        entries = [entry for entry in directory.iterdir()]
        has_gitkeep = any(entry.name == ".gitkeep" for entry in entries)
        other_entries = [entry for entry in entries if entry.name != ".gitkeep"]
        if not entries and not has_gitkeep:
            problems.append(f"empty directory without .gitkeep: {directory.relative_to(REPO_ROOT)}")
        if has_gitkeep and other_entries:
            problems.append(f"obsolete .gitkeep in non-empty directory: {directory.relative_to(REPO_ROOT)}")
    return problems


def check_placeholders() -> list[str]:
    """Reject placeholder markers in committed Markdown."""
    problems: list[str] = []
    for path in iter_all_files():
        if path.suffix != ".md":
            continue
        text = path.read_text(encoding="utf-8")
        for pattern, label in PLACEHOLDER_PATTERNS:
            for line_number, line in enumerate(text.splitlines(), start=1):
                if pattern.search(line):
                    problems.append(
                        f"{path.relative_to(REPO_ROOT)}:{line_number}: {label} -> {line.strip()[:80]}"
                    )
    return problems


def main() -> int:
    """Run every structural check and print a summary."""
    checks = {
        "required files and directories": check_required_paths(),
        ".gitkeep hygiene": check_gitkeep_files(),
        "placeholder content": check_placeholders(),
    }

    print(
        f"Repository root: {REPO_ROOT}\n"
        f"Weeks required: {len(WEEKS)}\n"
        f"Required files: {len(REQUIRED_FILES)}, required directories: {len(REQUIRED_DIRS)}\n"
    )

    failed = False
    for name, problems in checks.items():
        if problems:
            failed = True
            print(f"FAILED: {name} ({len(problems)} problem(s))")
            for problem in problems:
                print(f"  - {problem}")
        else:
            print(f"OK: {name}")

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
