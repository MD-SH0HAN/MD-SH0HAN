#!/usr/bin/env python3
"""Validate local image references and SVG assets in a GitHub profile README.

Run from the repository root: python3 scripts/validate_profile_assets.py
Missing referenced local files, malformed SVGs, and images above 25 MiB fail the
check. Files above 1 MiB produce warnings so existing assets can be optimized
without immediately breaking CI.
"""

from __future__ import annotations

import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path.cwd().resolve()
README = ROOT / "README.md"
WARN_BYTES = 1 * 1024 * 1024
FAIL_BYTES = 25 * 1024 * 1024
IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".svg"}

# Handles standard Markdown images, including angle-bracketed paths with spaces.
MARKDOWN_IMAGE_RE = re.compile(
    r"!\[[^\]]*\]\(\s*(?:<([^>]+)>|([^\s)]+))",
    flags=re.MULTILINE,
)
HTML_IMAGE_SRC_RE = re.compile(
    r"<img\b[^>]*?\bsrc\s*=\s*([\"'])(.*?)\1",
    flags=re.IGNORECASE | re.DOTALL,
)


def local_target(value: str) -> str | None:
    """Return a local path target; ignore remote/data/mail/fragment references."""
    target = value.strip().strip("\"'")
    if not target or target.startswith("#"):
        return None
    parsed = urlsplit(target)
    if parsed.scheme or parsed.netloc:
        return None
    path = unquote(parsed.path)
    if not path:
        return None
    # GitHub README references are normally relative; tolerate repo-root paths too.
    return path.lstrip("/")


def referenced_images(readme_text: str) -> set[Path]:
    refs: set[Path] = set()
    values: list[str] = []
    for match in MARKDOWN_IMAGE_RE.finditer(readme_text):
        values.append(match.group(1) or match.group(2) or "")
    for match in HTML_IMAGE_SRC_RE.finditer(readme_text):
        values.append(match.group(2))

    for value in values:
        path_value = local_target(value)
        if path_value is None:
            continue
        path = (ROOT / path_value).resolve()
        try:
            path.relative_to(ROOT)
        except ValueError:
            print(f"ERROR: image reference escapes repository root: {value}")
            continue
        refs.add(path)
    return refs


def main() -> int:
    errors = 0
    warnings = 0

    if not README.is_file():
        print("ERROR: README.md was not found at the repository root.")
        return 1

    text = README.read_text(encoding="utf-8", errors="replace")
    references = referenced_images(text)

    for path in sorted(references):
        if not path.is_file():
            print(f"ERROR: README references missing local image: {path.relative_to(ROOT)}")
            errors += 1

    image_files = sorted(
        path for path in ROOT.rglob("*")
        if path.is_file()
        and path.suffix.lower() in IMAGE_SUFFIXES
        and ".git" not in path.parts
    )

    for path in image_files:
        rel = path.relative_to(ROOT)
        size = path.stat().st_size

        if path.suffix.lower() == ".svg":
            try:
                ET.parse(path)
            except (ET.ParseError, OSError) as exc:
                print(f"ERROR: invalid SVG {rel}: {exc}")
                errors += 1

        if size > FAIL_BYTES:
            print(
                f"ERROR: {rel} is {size / (1024 * 1024):.2f} MiB; "
                f"hard limit is {FAIL_BYTES / (1024 * 1024):.0f} MiB."
            )
            errors += 1
        elif size > WARN_BYTES:
            print(f"WARNING: {rel} is {size / (1024 * 1024):.2f} MiB; optimize if practical.")
            warnings += 1

        if size > WARN_BYTES and path.resolve() not in references:
            print(f"WARNING: large image is not directly referenced in README.md: {rel}")
            warnings += 1

    print(
        f"Asset validation finished: {len(references)} local image reference(s), "
        f"{len(image_files)} image file(s), {warnings} warning(s), {errors} error(s)."
    )
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
