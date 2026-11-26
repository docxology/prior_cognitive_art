#!/usr/bin/env python3
"""Build the complete venue-neutral publication package in dependency order."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent


def _template_root() -> Path:
    candidates = (*PROJECT_ROOT.parents, Path.cwd(), PROJECT_ROOT.parents[2] / "template")
    for candidate in candidates:
        if (candidate / "infrastructure").is_dir() and (candidate / "scripts" / "pipeline" / "stage_03_render.py").exists():
            return candidate
    raise FileNotFoundError("could not locate the template checkout containing infrastructure/")


def _project_slot(template_root: Path) -> str:
    projects = template_root / "projects"
    if PROJECT_ROOT.is_relative_to(projects):
        return PROJECT_ROOT.relative_to(projects).as_posix()
    for slot in ("working/prior_cognitive_art", "ongoing/Uncategorized/prior_cognitive_art"):
        if (projects / slot).resolve() == PROJECT_ROOT:
            return slot
    raise FileNotFoundError("register the checkout under Template's projects directory before building")


def _run(label: str, command: list[str], cwd: Path) -> None:
    print(f"\n== {label} ==", flush=True)
    print("$ " + " ".join(command), flush=True)
    subprocess.run(command, cwd=cwd, check=True)


def build(*, dry_run: bool = False) -> None:
    template_root = _template_root()
    project = _project_slot(template_root)
    local = ["uv", "run", "--no-sync", "python"]
    stages = [
        ("analysis and figures", [*local, "scripts/optimization_analysis.py"], PROJECT_ROOT),
        ("API documentation", [*local, "scripts/generate_api_docs.py"], PROJECT_ROOT),
        ("manuscript hydration", [*local, "scripts/z_generate_manuscript_variables.py"], PROJECT_ROOT),
        (
            "PDF, web, and slide rendering",
            [*local, "scripts/pipeline/stage_03_render.py", "--project", project, "--skip-manuscript-hydration"],
            template_root,
        ),
        ("dashboard generation", [*local, "scripts/build_dashboard.py"], PROJECT_ROOT),
    ]
    for label, command, cwd in stages:
        if dry_run:
            print(f"[dry-run] {label}: {' '.join(command)} (cwd={cwd})")
        else:
            _run(label, command, cwd)

    if dry_run:
        print("[dry-run] apply project web CSS")
        print("[dry-run] write render manifest")
        print("[dry-run] validate rendered outputs (Template stage 04)")
        print("[dry-run] validate publication package")
        return

    sys.path.insert(0, str(PROJECT_ROOT))
    from src.render_manifest import write_render_manifest
    from src.rendering import apply_project_web_style

    styled = apply_project_web_style(PROJECT_ROOT)
    print(f"\n== project web CSS ==\nStyled {len(styled)} rendered manuscript HTML files", flush=True)
    manifest = write_render_manifest(PROJECT_ROOT)
    print(f"\n== render freshness manifest ==\n{manifest}", flush=True)
    _run("validate rendered outputs", [*local, "scripts/pipeline/stage_04_validate.py", "--project", project], template_root)
    _run("publication package validation", [*local, "scripts/validate_publication_package.py", "--json"], PROJECT_ROOT)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="Print the build sequence without running it.")
    args = parser.parse_args()
    build(dry_run=args.dry_run)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
