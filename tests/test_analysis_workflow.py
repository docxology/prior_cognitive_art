import json
from pathlib import Path

from src.analysis.workflow import build_conceptual_report, run_analysis_pipeline


def test_build_conceptual_report_is_simulation_free(tmp_path: Path) -> None:
    report = build_conceptual_report(tmp_path)
    assert report["simulation_free"] is True
    assert report["figure_count"] == 18
    assert report["formal_claim_count"] == 11
    assert report["symbol_count"] == 25
    assert report["text_validation_count"] == 10
    assert report["claim_dependency_count"] == 12
    assert report["contract_errors"] == []
    assert len(report["quadrants"]) == 4


def test_run_analysis_pipeline_writes_manifest_and_figures(tmp_path: Path) -> None:
    paths = run_analysis_pipeline(tmp_path)
    assert paths["conceptual_report"].exists()
    assert paths["conceptual_map"].exists()
    assert paths["manifest"].exists()
    assert paths["cover_art"].exists()
    assert paths["cover_art"].suffix == ".png"
    assert paths["cover_art_svg"].exists()
    assert paths["cover_art_svg"].suffix == ".svg"
    assert paths["cover_art_manifest"].exists()
    assert paths["figure_registry"].exists()
    for key, path in paths.items():
        if key.startswith("figure_") and key != "figure_registry":
            assert path.suffix == ".png"
            assert path.stat().st_size > 0
            assert path.with_suffix(".svg").stat().st_size > 0

    report = json.loads(paths["conceptual_report"].read_text(encoding="utf-8"))
    assert report["mode"] == "plain text plus deterministic conceptual visualization"
    cover_manifest = json.loads(paths["cover_art_manifest"].read_text(encoding="utf-8"))
    assert cover_manifest["format"] == "square"
    assert cover_manifest["width_px"] == 2048
    assert cover_manifest["height_px"] == 2048
    assert cover_manifest["png"].endswith("prior_cognitive_art_cover_square.png")
    registry = json.loads(paths["figure_registry"].read_text(encoding="utf-8"))
    assert set(registry) == {
        "fig:tinbergen_axes",
        "fig:regress_terminations",
        "fig:prior_equilibrium_map",
        "fig:ontogeny_hyperprior_parallel",
        "fig:selection_filter",
        "fig:policy_entanglement_bridge",
        "fig:formal_claim_dependency_map",
        "fig:symbol_glossary_closure",
        "fig:text_validation_ladder",
        "fig:niche_construction_diagram",
        "fig:markov_blanket_achievement",
        "fig:explanatory_complementarity_matrix",
        "fig:active_inference_cycle",
        "fig:variational_free_energy_landscape",
        "fig:scale_invariance_diagram",
        "fig:source_claim_boundary_map",
        "fig:markov_blanket_scope_split",
        "fig:niche_prior_feedback_field",
    }
