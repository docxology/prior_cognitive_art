#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parent.parent


def _load_project_modules(project_root: Path) -> None:
    sys.path.insert(0, str(project_root))


def _load_json(path: Path, issues: list[str]) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        issues.append(f"missing required JSON artifact: {path.relative_to(PROJECT_ROOT)}")
    except json.JSONDecodeError as exc:
        issues.append(f"invalid JSON in {path.relative_to(PROJECT_ROOT)}: {exc}")
    return None


def _require_files(project_root: Path, relative_paths: tuple[str, ...], issues: list[str]) -> None:
    for relative_path in relative_paths:
        path = project_root / relative_path
        if not path.exists():
            issues.append(f"missing required artifact: {relative_path}")
        elif path.is_file() and path.stat().st_size == 0:
            issues.append(f"empty required artifact: {relative_path}")


def _check_counts(project_root: Path, issues: list[str]) -> dict[str, int]:
    _load_project_modules(project_root)
    from src.conceptual_model import (  # noqa: PLC0415
        claim_dependencies,
        figure_specs,
        formal_claims,
        symbol_glossary,
        text_validation_checks,
        validate_claim_dependencies,
        validate_conceptual_contract,
    )

    expected = {
        "figure_count": len(figure_specs()),
        "formal_claim_count": len(formal_claims()),
        "symbol_count": len(symbol_glossary()),
        "text_validation_count": len(text_validation_checks()),
        "claim_dependency_count": len(claim_dependencies()),
    }

    for error in validate_conceptual_contract():
        issues.append(f"conceptual contract error: {error}")
    for error in validate_claim_dependencies():
        issues.append(f"claim dependency error: {error}")

    report = _load_json(project_root / "output/reports/conceptual_analysis.json", issues)
    if isinstance(report, dict):
        for key, expected_value in expected.items():
            if report.get(key) != expected_value:
                issues.append(
                    f"conceptual_analysis.json {key}={report.get(key)!r}; expected {expected_value}"
                )
        if report.get("simulation_free") is not True:
            issues.append("conceptual_analysis.json must preserve simulation_free=true")
        if report.get("contract_errors") not in ([], ()):
            issues.append("conceptual_analysis.json reports contract_errors")
        if report.get("claim_dependency_errors") not in ([], ()):
            issues.append("conceptual_analysis.json reports claim_dependency_errors")

    manifest = _load_json(project_root / "output/reports/figure_manifest.json", issues)
    if isinstance(manifest, dict) and len(manifest.get("figures", [])) != expected["figure_count"]:
        issues.append("figure_manifest.json figure count does not match source figure_specs()")

    registry = _load_json(project_root / "output/figures/figure_registry.json", issues)
    if isinstance(registry, dict) and len(registry) != expected["figure_count"]:
        issues.append("figure_registry.json count does not match source figure_specs()")

    variables = _load_json(project_root / "output/data/manuscript_variables.json", issues)
    if isinstance(variables, dict):
        variable_map = {
            "FIGURE_COUNT": expected["figure_count"],
            "FORMAL_CLAIM_COUNT": expected["formal_claim_count"],
            "SYMBOL_COUNT": expected["symbol_count"],
            "TEXT_VALIDATION_COUNT": expected["text_validation_count"],
            "CLAIM_DEPENDENCY_COUNT": expected["claim_dependency_count"],
        }
        for key, expected_value in variable_map.items():
            if str(variables.get(key)) != str(expected_value):
                issues.append(f"manuscript_variables.json {key}={variables.get(key)!r}; expected {expected_value}")

    return expected


def _check_figure_artifacts(project_root: Path, expected_figure_count: int, issues: list[str]) -> None:
    figure_dir = project_root / "output/figures"
    pngs = sorted(figure_dir.glob("*.png"))
    svgs = sorted(figure_dir.glob("*.svg"))
    if len(pngs) != expected_figure_count:
        issues.append(f"expected {expected_figure_count} PNG figures, found {len(pngs)}")
    if len(svgs) != expected_figure_count:
        issues.append(f"expected {expected_figure_count} SVG figures, found {len(svgs)}")
    for path in [*pngs, *svgs]:
        if path.stat().st_size == 0:
            issues.append(f"empty figure artifact: {path.relative_to(project_root)}")


def _png_dimensions(path: Path) -> tuple[int, int] | None:
    try:
        header = path.read_bytes()[:24]
    except FileNotFoundError:
        return None
    signature = b"\x89PNG\r\n\x1a\n"
    if len(header) < 24 or not header.startswith(signature):
        return None
    return int.from_bytes(header[16:20], "big"), int.from_bytes(header[20:24], "big")


def _check_cover_art(project_root: Path, issues: list[str]) -> None:
    png_path = project_root / "output/cover/prior_cognitive_art_cover_square.png"
    svg_path = project_root / "output/cover/prior_cognitive_art_cover_square.svg"
    manifest_path = project_root / "output/reports/cover_art_manifest.json"
    for path in (png_path, svg_path, manifest_path):
        if not path.exists():
            issues.append(f"missing cover-art artifact: {path.relative_to(project_root)}")
        elif path.stat().st_size == 0:
            issues.append(f"empty cover-art artifact: {path.relative_to(project_root)}")

    dimensions = _png_dimensions(png_path)
    if dimensions != (2048, 2048):
        issues.append(f"cover PNG dimensions={dimensions!r}; expected (2048, 2048)")

    manifest = _load_json(manifest_path, issues)
    if isinstance(manifest, dict):
        if manifest.get("format") != "square":
            issues.append("cover_art_manifest.json format must be square")
        if manifest.get("width_px") != 2048 or manifest.get("height_px") != 2048:
            issues.append("cover_art_manifest.json must record 2048 x 2048 dimensions")
        if manifest.get("png") != "output/cover/prior_cognitive_art_cover_square.png":
            issues.append("cover_art_manifest.json png path is stale")


def _check_rendered_tokens(project_root: Path, issues: list[str]) -> None:
    token_surfaces = [
        project_root / "output/web/index.html",
        project_root / "output/web/dashboard.html",
        *sorted((project_root / "output/manuscript").glob("*.md")),
    ]
    unresolved_tokens = ("{{", "}}")
    html_only_tokens = ("[@",)

    for path in token_surfaces:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for token in unresolved_tokens:
            if token in text:
                issues.append(f"unresolved template token {token!r} in {path.relative_to(project_root)}")
        if path.suffix == ".html":
            for token in html_only_tokens:
                if token in text:
                    issues.append(f"unresolved citation marker {token!r} in {path.relative_to(project_root)}")

    bib_path = project_root / "manuscript/references.bib"
    html_path = project_root / "output/web/index.html"
    if bib_path.exists() and html_path.exists():
        bib_keys = re.findall(r"@\w+\{([^,\s]+)", bib_path.read_text(encoding="utf-8", errors="replace"))
        html_text = html_path.read_text(encoding="utf-8", errors="replace")
        for key in bib_keys:
            if f"[{key}" in html_text or f"; {key}" in html_text:
                issues.append(f"rendered HTML exposes raw citation key: {key}")


def validate_publication_package(project_root: Path) -> tuple[bool, list[str], dict[str, int]]:
    project_root = project_root.resolve()
    issues: list[str] = []
    if not project_root.exists():
        return False, [f"project root does not exist: {project_root}"], {}

    required = (
        "README.md",
        "TODO.md",
        "CITATION.cff",
        "codemeta.json",
        ".zenodo.json",
        "docs/publication_readiness_report.md",
        "docs/submission_package.md",
        "docs/reviewer_risk_register.md",
        "docs/cover_letter_template.md",
        "docs/venue_selection_matrix.md",
        "docs/preprint_release_checklist.md",
        "docs/scholarship-audit.md",
        "data/claim_ledger.yaml",
        "manuscript/config.yaml",
        "manuscript/references.bib",
        "output/pdf/prior_cognitive_art_combined.pdf",
        "output/web/index.html",
        "output/web/dashboard.html",
        "output/docs/api_reference.md",
        "output/docs/api_glossary.md",
        "output/reports/conceptual_analysis.json",
        "output/reports/figure_manifest.json",
        "output/reports/cover_art_manifest.json",
        "output/data/manuscript_variables.json",
    )
    _require_files(project_root, required, issues)
    expected = _check_counts(project_root, issues)
    if expected:
        _check_figure_artifacts(project_root, expected["figure_count"], issues)
    _check_cover_art(project_root, issues)
    _check_rendered_tokens(project_root, issues)
    return not issues, issues, expected


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
