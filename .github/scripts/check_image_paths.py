#!/usr/bin/env python3
"""Validate that every image reference in the book resolves to a real image.

Runs fully offline (no network calls, no jupyter-book install needed). It
catches two failure modes that the Sphinx build either misses or reports in a
way that's hard to trace back to the offending line:

  1. Local image paths that don't point at an existing file in the repo.
  2. Remote image URLs that will never render as an image -- specifically
     GitHub "/blob/..." links, which serve an HTML *page*, not the raw bytes.
     (Use a repo-relative path, or a raw.githubusercontent.com URL, or append
     "?raw=true" to the blob URL.)

Image references inside HTML comments (<!-- ... -->) are ignored, since those
are not rendered.

Exit status is non-zero if any problem is found, so it can gate a PR.
"""

from __future__ import annotations

import sys
from pathlib import Path
from urllib.parse import unquote, urlparse
import re

ROOT = Path(__file__).resolve().parents[2]

# Not part of the book's table of contents (mirrors exclude_patterns in
# _config.yml). Add more names here if the book grows non-content markdown.
EXCLUDE_NAMES = {"README.md"}
EXCLUDE_DIR_PARTS = {"_build", "docs", ".github"}

# Markdown image:  ![alt](dest "optional title")
#   dest is either <bracketed> (may contain spaces) or runs to whitespace/paren.
MD_IMAGE = re.compile(r"!\[[^\]]*\]\(\s*(<[^>]+>|[^)\s]+)")
# MyST directive fence:  ```{image} dest   or   ```{figure} dest   (``` or :::)
MYST_IMAGE = re.compile(
    r"^\s*(?:`{3,}|:{3,})\{(?:image|figure)\}\s+(\S+)", re.MULTILINE
)
# Raw HTML:  <img ... src="dest" ...>
HTML_IMAGE = re.compile(
    r"""<img\b[^>]*?\bsrc\s*=\s*["']([^"']+)["']""", re.IGNORECASE
)

HTML_COMMENT = re.compile(r"<!--.*?-->", re.DOTALL)


def extract_refs(text: str):
    """Yield every image destination in a markdown file (comments stripped)."""
    text = HTML_COMMENT.sub("", text)
    for pattern in (MD_IMAGE, MYST_IMAGE, HTML_IMAGE):
        for match in pattern.finditer(text):
            dest = match.group(1).strip().strip("<>").strip()
            if dest:
                yield dest


def is_remote(dest: str) -> bool:
    return urlparse(dest).scheme in {"http", "https"}


def bad_github_blob(dest: str) -> bool:
    """A github.com/.../blob/... URL renders HTML unless it says raw=true."""
    parsed = urlparse(dest)
    if parsed.netloc != "github.com" or "/blob/" not in parsed.path:
        return False
    return "raw=true" not in parsed.query and "raw=1" not in parsed.query


def check_file(md_path: Path):
    """Return a list of (dest, reason) problems for one markdown file."""
    problems = []
    text = md_path.read_text(encoding="utf-8", errors="replace")
    for dest in extract_refs(text):
        if dest.startswith(("#", "data:", "mailto:")):
            continue
        if is_remote(dest):
            if bad_github_blob(dest):
                problems.append(
                    (dest, "GitHub /blob/ URL serves an HTML page, not an image "
                           "-- use a repo-relative path or raw.githubusercontent.com")
                )
            continue  # other remote URLs are out of scope for this offline check
        # Local path: drop any ?query/#anchor, URL-decode, resolve vs the file.
        local = unquote(dest.split("#", 1)[0].split("?", 1)[0])
        target = (md_path.parent / local).resolve()
        if not target.is_file():
            problems.append((dest, "file not found"))
    return problems


def main() -> int:
    md_files = sorted(
        p
        for p in ROOT.rglob("*.md")
        if p.name not in EXCLUDE_NAMES
        and not (EXCLUDE_DIR_PARTS & set(p.relative_to(ROOT).parts))
    )

    total = 0
    for md in md_files:
        rel = md.relative_to(ROOT)
        for dest, reason in check_file(md):
            # GitHub Actions annotation -> shows inline on the PR diff.
            print(f"::error file={rel}::Broken image ref '{dest}' -- {reason}")
            print(f"  {rel}: {dest}\n      -> {reason}")
            total += 1

    if total:
        print(f"\n✗ {total} broken image reference(s) found.")
        return 1
    print(f"✓ All image references resolve ({len(md_files)} files scanned).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
