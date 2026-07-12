import json
from pathlib import Path

from src.analysis.workflow import build_conceptual_report, run_analysis_pipeline
from src.conceptual_model import (
    claim_dependencies,
    claim_grounding,
    deterministic_simulation_trace,
    figure_specs,
    formal_claims,
    symbol_glossary,
    text_validation_checks,
)


def test_build_conceptual_report_has_bounded_deterministic_simulation_scope(tmp_path: Path) -> None:
    report = build_conceptual_report(tmp_path)
    assert report["simulation_free"] is True
    assert report["deterministic_illustrative_simulation"] is True
    assert report["empirical_simulation_free"] is True
    assert report["stochastic_simulation_free"] is True
    assert "no stochastic sampling" in report["simulation_scope"]
    assert report["figure_count"] == len(figure_specs())
    assert report["formal_claim_count"] == len(formal_claims())
    assert report["symbol_count"] == len(symbol_glossary())
    assert report["text_validation_count"] == len(text_validation_checks())
    assert report["claim_dependency_count"] == len(claim_dependencies())
    assert report["claim_grounding_count"] == len(claim_grounding())
    assert report["claim_grounding_errors"] == []
    assert set(report["generation"]) == {"generated_at", "python_version", "platform"}
    assert report["deterministic_simulation_step_count"] == len(deterministic_simulation_trace())
    assert report["contract_errors"] == []
    assert len(report["quadrants"]) == 4


def test_run_analysis_pipeline_writes_manifest_and_figures(tmp_path: Path) -> None:
    legacy_stem = "scale_" + "invariance_diagram"
    stale_png = tmp_path / "output" / "figures" / f"{legacy_stem}.png"
    stale_svg = tmp_path / "output" / "figures" / f"{legacy_stem}.svg"
    stale_png.parent.mkdir(parents=True, exist_ok=True)
    stale_png.write_bytes(b"stale")
    stale_svg.write_text("<svg />", encoding="utf-8")

    paths = run_analysis_pipeline(tmp_path)
    assert not stale_png.exists()
    assert not stale_svg.exists()
    assert paths["conceptual_report"].exists()
    assert paths["conceptual_map"].exists()
    assert paths["deterministic_simulation_trace"].exists()
    assert paths["deterministic_simulation_manifest"].exists()
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
    assert report["mode"] == "plain text plus deterministic conceptual visualization and illustrative simulation trace"
    trace = json.loads(paths["deterministic_simulation_trace"].read_text(encoding="utf-8"))
    assert trace["schema"] == "prior_cognitive_art.deterministic_simulation_trace.v1"
    assert len(trace["steps"]) == len(deterministic_simulation_trace())
    assert "formal state" in trace["steps"][0]["invariant"].lower() or trace["steps"][0]["formal_state"]
    simulation_manifest = json.loads(paths["deterministic_simulation_manifest"].read_text(encoding="utf-8"))
    assert simulation_manifest["stochastic_simulation_free"] is True
    assert simulation_manifest["performance_claims_free"] is True
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
        "fig:deterministic_simulation_trace",
        "fig:scale_recurrence_diagram",
        "fig:source_claim_boundary_map",
        "fig:aesthetic_prior_craft_map",
        "fig:markov_blanket_scope_split",
        "fig:niche_prior_feedback_field",
        "fig:first_prior_grounding_stack",
    }
