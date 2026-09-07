#!/usr/bin/env python3
"""Build the styled web dashboard and JSON payload (thin orchestrator)."""

from __future__ import annotations

import os
import sys
from pathlib import Path

os.environ.setdefault("MPLBACKEND", "Agg")

PROJECT_ROOT = Path(__file__).resolve().parent.parent
for _path in (PROJECT_ROOT, PROJECT_ROOT / "src", PROJECT_ROOT.parents[2]):
    path_text = str(_path)
    if path_text not in sys.path:
        sys.path.insert(0, path_text)

from src.dashboard import build_dashboard  # noqa: E402


def cli_main() -> int:
    out_path, json_path = build_dashboard(PROJECT_ROOT)
    print(str(out_path))
    print(str(json_path))
    return 0


if __name__ == "__main__":
    raise SystemExit(cli_main())
