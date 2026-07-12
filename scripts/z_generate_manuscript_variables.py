#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path

_PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_PROJECT_ROOT))


def _template_root() -> Path:
    candidates = [
        Path.cwd(),
        _PROJECT_ROOT.parents[2],
        _PROJECT_ROOT.parents[2] / "template",
    ]
    for candidate in candidates:
        if (candidate / "infrastructure").is_dir():
            return candidate
    return _PROJECT_ROOT.parents[2]


sys.path.insert(0, str(_template_root()))


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate manuscript variables for prior_cognitive_art")
    parser.add_argument(
        "--allow-draft",
        action="store_true",
        help="Allow draft hydration before conceptual analysis artifacts exist",
    )
    args = parser.parse_args()

    from infrastructure.rendering.manuscript_injection import write_resolved_manuscript_tree
    from src.manuscript_variables import generate_variables, save_variables
    from src.render_manifest import stamp_render_input_fingerprint

    variables = generate_variables(
        _PROJECT_ROOT,
        require_analysis_outputs=not args.allow_draft,
    )
    out_path = _PROJECT_ROOT / "output" / "data" / "manuscript_variables.json"
    save_variables(variables, out_path)
    write_resolved_manuscript_tree(_PROJECT_ROOT, variables)
    stamp_render_input_fingerprint(_PROJECT_ROOT)
    print(str(out_path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
