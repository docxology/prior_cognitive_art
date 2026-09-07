#!/usr/bin/env python3
"""Validate the venue-neutral publication package (thin orchestrator)."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
for _path in (PROJECT_ROOT, PROJECT_ROOT / "src", PROJECT_ROOT.parents[2]):
    path_text = str(_path)
    if path_text not in sys.path:
        sys.path.insert(0, path_text)

from src.publication_validation import validate_publication_package  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate the venue-neutral publication package against source-owned counts."
    )
    parser.add_argument(
        "--project-root",
        type=Path,
        default=PROJECT_ROOT,
        help="Project root to validate. Defaults to this script's parent project.",
    )
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
    args = parser.parse_args()

    ok, issues, expected = validate_publication_package(args.project_root)
    if args.json:
        print(json.dumps({"ok": ok, "issues": issues, "expected_counts": expected}, indent=2, sort_keys=True))
    elif ok:
        print(
            "Publication package OK: "
            f"{expected.get('figure_count', 0)} figures, "
            f"{expected.get('formal_claim_count', 0)} claims, "
            f"{expected.get('symbol_count', 0)} symbols"
        )
    else:
        print("Publication package issues:", file=sys.stderr)
        for issue in issues:
            print(f"- {issue}", file=sys.stderr)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
