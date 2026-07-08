from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from src.conceptual_model import (
    argument_modules,
    as_records,
    claim_dependencies,
    conceptual_integrity_token,
    figure_specs,
    formal_claims,
    quadrant_grid,
    symbol_glossary,
    termination_catalog,
    text_validation_checks,
    validate_conceptual_contract,
    validate_claim_dependencies,
)
from src.figures import COVER_ART_FILENAME, COVER_ART_SIZE_PX, COVER_ART_SVG_FILENAME, draw_square_cover_art, generate_all_figures
from src.project_paths import project_output_dirs


def _figure_registry() -> dict[str, dict[str, object]]:
    registry: dict[str, dict[str, object]] = {}
    for index, spec in enumerate(figure_specs()):
        label = f"fig:{spec.key}"
        registry[label] = {
            "figure_id": f"figure_{index:03d}",
            "filename": spec.filename,
            "caption": spec.caption,
            "label": label,
            "section": "Visual Atlas",
            "width": "0.86\\textwidth",
            "placement": "h",
            "generated_by": "optimization_analysis.py",
            "metadata": {"purpose": spec.purpose},
        }
    return registry


def build_conceptual_report(project_root: Path) -> dict[str, Any]:
    figures = figure_specs()
    contract_errors = validate_conceptual_contract()
    if contract_errors:
        raise ValueError("; ".join(contract_errors))
    return {
        "project": "prior_cognitive_art",
        "mode": "plain text plus deterministic conceptual visualization",
        "simulation_free": True,
        "quadrants": as_records(quadrant_grid()),
        "terminations": as_records(termination_catalog()),
        "argument_modules": as_records(argument_modules()),
        "formal_claims": as_records(formal_claims()),
        "claim_dependencies": as_records(claim_dependencies()),
        "symbol_glossary": as_records(symbol_glossary()),
        "text_validation_checks": as_records(text_validation_checks()),
        "conceptual_integrity_token": conceptual_integrity_token(),
        "contract_errors": [],
        "claim_dependency_errors": list(validate_claim_dependencies()),
        "figures": as_records(figures),
        "figure_count": len(figures),
        "formal_claim_count": len(formal_claims()),
        "symbol_count": len(symbol_glossary()),
        "text_validation_count": len(text_validation_checks()),
        "claim_dependency_count": len(claim_dependencies()),
        "project_root": str(project_root),
    }


def run_analysis_pipeline(project_root: Path | None = None) -> dict[str, Path]:
    root = project_root or Path(__file__).resolve().parents[2]
    dirs = project_output_dirs(root)
    for directory in dirs.values():
        directory.mkdir(parents=True, exist_ok=True)

    figure_paths = generate_all_figures(dirs["figures"])
    cover_path = draw_square_cover_art(dirs["output"] / "cover")
    report = build_conceptual_report(root)

    report_path = dirs["reports"] / "conceptual_analysis.json"
    report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")

    data_path = dirs["data"] / "conceptual_map.json"
    data_path.write_text(json.dumps(report, indent=2), encoding="utf-8")

    manifest_path = dirs["reports"] / "figure_manifest.json"
    manifest_path.write_text(
        json.dumps({"figures": [str(path.relative_to(root)) for path in figure_paths]}, indent=2),
        encoding="utf-8",
    )

    cover_manifest_path = dirs["reports"] / "cover_art_manifest.json"
    cover_manifest_path.write_text(
        json.dumps(
            {
                "id": "cover:prior_cognitive_art_square",
                "title": "Prior Cognitive Art square cover",
                "png": str(cover_path.relative_to(root)),
                "svg": str(cover_path.with_suffix(".svg").relative_to(root)),
                "filename": COVER_ART_FILENAME,
                "svg_filename": COVER_ART_SVG_FILENAME,
                "format": "square",
                "width_px": COVER_ART_SIZE_PX,
                "height_px": COVER_ART_SIZE_PX,
                "generated_by": "optimization_analysis.py",
                "role": "preprint cover art and dashboard hero; stored outside output/figures so it is not counted as a manuscript figure",
                "concept": "Tinbergen quadrants, hyperprior chain, selection filter, Markov blanket boundary, and central prior settlement",
            },
            indent=2,
        ),
        encoding="utf-8",
    )

    registry_path = dirs["figures"] / "figure_registry.json"
    registry_path.write_text(json.dumps(_figure_registry(), indent=2), encoding="utf-8")

    return {
        "conceptual_report": report_path,
        "conceptual_map": data_path,
        "manifest": manifest_path,
        "cover_art_manifest": cover_manifest_path,
        "cover_art": cover_path,
        "cover_art_svg": cover_path.with_suffix(".svg"),
        "figure_registry": registry_path,
        **{f"figure_{path.stem}": path for path in figure_paths},
    }


def main() -> int:
    paths = run_analysis_pipeline()
    for path in paths.values():
        print(path)
    return 0
