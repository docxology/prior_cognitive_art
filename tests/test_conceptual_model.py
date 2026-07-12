import pytest

from src.conceptual_model import (
    claim_dependencies,
    claim_grounding,
    conceptual_integrity_token,
    deterministic_simulation_trace,
    figure_specs,
    formal_claims,
    quadrant_grid,
    symbol_glossary,
    termination_catalog,
    text_validation_checks,
    used_symbol_keys,
    validate_claim_dependencies,
    validate_claim_grounding,
    validate_conceptual_contract,
)


def test_tinbergen_grid_is_crossed_two_axis_map() -> None:
    quadrants = quadrant_grid()
    assert len(quadrants) == 4
    assert {item.scale for item in quadrants} == {"proximate", "ultimate"}
    assert {item.temporality for item in quadrants} == {"static", "developmental"}
    assert {item.key for item in quadrants} == {"mechanism", "function", "ontogeny", "phylogeny"}
    assert "defers" in next(item for item in quadrants if item.key == "ontogeny").regress_status
    assert "blocks" in next(item for item in quadrants if item.key == "phylogeny").regress_status


def test_termination_catalog_names_the_three_stops() -> None:
    terminations = termination_catalog()
    assert [item.key for item in terminations] == ["pragmatic", "selection", "fixed_point"]
    assert any("flat or weak hyperprior" in item.answer for item in terminations)
    assert any("settled organization" in item.answer for item in terminations)


def test_argument_and_figure_manifest_are_aligned() -> None:
    figures = figure_specs()
    assert [item.filename for item in figures] == [
        "tinbergen_axes.png",
        "regress_terminations.png",
        "prior_equilibrium_map.png",
        "ontogeny_hyperprior_parallel.png",
        "selection_filter.png",
        "policy_entanglement_bridge.png",
        "formal_claim_dependency_map.png",
        "symbol_glossary_closure.png",
        "text_validation_ladder.png",
        "niche_construction_diagram.png",
        "markov_blanket_achievement.png",
        "explanatory_complementarity_matrix.png",
        "active_inference_cycle.png",
        "variational_free_energy_landscape.png",
        "deterministic_simulation_trace.png",
        "scale_recurrence_diagram.png",
        "source_claim_boundary_map.png",
        "aesthetic_prior_craft_map.png",
        "markov_blanket_scope_split.png",
        "niche_prior_feedback_field.png",
        "first_prior_grounding_stack.png",
    ]


def test_figure_metadata_partitions_and_describes_every_figure() -> None:
    figures = figure_specs()
    assert sum(item.section == "Visual Atlas" for item in figures) == 18
    assert sum(item.section == "Formal Supplement" for item in figures) == 3
    assert all(item.caption and item.alt_text and item.section for item in figures)
    assert {item.key for item in figures if item.section == "Formal Supplement"} == {
        "formal_claim_dependency_map",
        "symbol_glossary_closure",
        "text_validation_ladder",
    }


def test_formal_supplement_contract_is_closed() -> None:
    claims = formal_claims()
    symbols = symbol_glossary()
    checks = text_validation_checks()
    assert [claim.title for claim in claims] == [
        "Axis partition",
        "Regress shape",
        "Selection filter",
        "Fixed-point stop",
        "Decomposition caution",
        "Niche co-construction",
        "Blanket achievement",
        "Explanatory complementarity",
        "Active inference bridge",
        "Variational closure",
        "Scale recurrence",
        "Deterministic trace boundary",
    ]
    assert len(symbols) == len(used_symbol_keys())
    assert {symbol.key for symbol in symbols} == set(used_symbol_keys())
    assert [check.key for check in checks] == [
        "deterministic_simulation_boundary",
        "figure_registry_closure",
        "symbol_glossary_closure",
        "token_hydration",
        "integrity_signature",
        "claim_dependency_closure",
        "claim_grounding_closure",
        "metadata_keyword_consistency",
        "citation_resolution",
        "figure_count_consistency",
        "argument_module_closure",
    ]
    assert validate_conceptual_contract() == ()


def test_conceptual_integrity_token_is_stable_shape() -> None:
    token = conceptual_integrity_token()
    assert len(token) == 16
    assert token == conceptual_integrity_token()


def test_claim_dependencies_reference_valid_claims() -> None:
    deps = claim_dependencies()
    assert len(deps) == 14
    assert validate_claim_dependencies() == ()


def test_claim_dependencies_have_rationales() -> None:
    for dep in claim_dependencies():
        assert dep.source_claim
        assert dep.target_claim
        assert dep.rationale
        assert dep.source_claim != dep.target_claim


def test_claim_grounding_covers_every_formal_claim() -> None:
    assert len(claim_grounding()) == 12
    assert validate_claim_grounding() == ()


def test_deterministic_trace_is_finite_ordered_formal_contract() -> None:
    trace = deterministic_simulation_trace()
    assert [step.step for step in trace] == list(range(len(trace)))
    assert [step.state for step in trace] == [
        "Question typed",
        "Regress exposed",
        "Tinbergen split",
        "Termination chosen",
        "Settlement named",
    ]
    assert trace[0].formal_state.startswith(r"$\sigma_0")
    assert trace[-1].formal_state.startswith(r"$\sigma_4")
    assert "not a hidden prior" in trace[-1].invariant
    assert all("empirical" not in step.invariant.lower() for step in trace)


def test_validate_claim_dependencies_detects_bad_source(monkeypatch: pytest.MonkeyPatch) -> None:
    """A dependency with a bad source_claim key should be caught."""
    from src import conceptual_model
    from src.conceptual_model import ClaimDependency

    original = conceptual_model.claim_dependencies
    bad = original() + (ClaimDependency("nonexistent_claim", "axis_partition", "bad"),)
    monkeypatch.setattr(conceptual_model, "claim_dependencies", lambda: bad)
    errors = conceptual_model.validate_claim_dependencies()
    assert any("source_claim" in e for e in errors)


def test_validate_claim_dependencies_detects_bad_target(monkeypatch: pytest.MonkeyPatch) -> None:
    """A dependency with a bad target_claim key should be caught."""
    from src import conceptual_model
    from src.conceptual_model import ClaimDependency

    original = conceptual_model.claim_dependencies
    bad = original() + (ClaimDependency("axis_partition", "nonexistent_claim", "bad"),)
    monkeypatch.setattr(conceptual_model, "claim_dependencies", lambda: bad)
    errors = conceptual_model.validate_claim_dependencies()
    assert any("target_claim" in e for e in errors)
