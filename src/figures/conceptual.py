from __future__ import annotations

from pathlib import Path

from src.conceptual_model import figure_specs

from ._active_scale_figures import (
    draw_active_inference_cycle,
    draw_deterministic_simulation_trace,
    draw_scale_invariance_diagram,
    draw_variational_free_energy_landscape,
)
from ._art_figures import draw_aesthetic_prior_craft_map
from ._argument_figures import (
    draw_ontogeny_hyperprior_parallel,
    draw_prior_equilibrium_map,
    draw_regress_terminations,
    draw_selection_filter,
    draw_tinbergen_axes,
)
from ._boundary_figures import (
    draw_markov_blanket_scope_split,
    draw_niche_prior_feedback_field,
    draw_source_claim_boundary_map,
)
from ._contract_figures import (
    draw_formal_claim_dependency_map,
    draw_policy_entanglement_bridge,
    draw_symbol_glossary_closure,
    draw_text_validation_ladder,
)
from ._niche_blanket_figures import (
    draw_explanatory_complementarity_matrix,
    draw_markov_blanket_achievement,
    draw_niche_construction_diagram,
)
from ._upstream_figures import draw_first_prior_grounding_stack


def generate_all_figures(output_dir: Path) -> list[Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    paths = [
        draw_tinbergen_axes(output_dir),
        draw_regress_terminations(output_dir),
        draw_prior_equilibrium_map(output_dir),
        draw_ontogeny_hyperprior_parallel(output_dir),
        draw_selection_filter(output_dir),
        draw_policy_entanglement_bridge(output_dir),
        draw_formal_claim_dependency_map(output_dir),
        draw_symbol_glossary_closure(output_dir),
        draw_text_validation_ladder(output_dir),
        draw_niche_construction_diagram(output_dir),
        draw_markov_blanket_achievement(output_dir),
        draw_explanatory_complementarity_matrix(output_dir),
        draw_active_inference_cycle(output_dir),
        draw_variational_free_energy_landscape(output_dir),
        draw_deterministic_simulation_trace(output_dir),
        draw_scale_invariance_diagram(output_dir),
        draw_source_claim_boundary_map(output_dir),
        draw_aesthetic_prior_craft_map(output_dir),
        draw_markov_blanket_scope_split(output_dir),
        draw_niche_prior_feedback_field(output_dir),
        draw_first_prior_grounding_stack(output_dir),
    ]
    expected = {spec.filename for spec in figure_specs()}
    produced = {path.name for path in paths}
    if produced != expected:
        missing = ", ".join(sorted(expected - produced))
        extra = ", ".join(sorted(produced - expected))
        raise RuntimeError(f"figure manifest mismatch; missing={missing}; extra={extra}")
    return paths


__all__ = [
    "generate_all_figures",
    "draw_tinbergen_axes",
    "draw_regress_terminations",
    "draw_prior_equilibrium_map",
    "draw_ontogeny_hyperprior_parallel",
    "draw_selection_filter",
    "draw_policy_entanglement_bridge",
    "draw_formal_claim_dependency_map",
    "draw_symbol_glossary_closure",
    "draw_text_validation_ladder",
    "draw_niche_construction_diagram",
    "draw_markov_blanket_achievement",
    "draw_explanatory_complementarity_matrix",
    "draw_active_inference_cycle",
    "draw_variational_free_energy_landscape",
    "draw_deterministic_simulation_trace",
    "draw_scale_invariance_diagram",
    "draw_source_claim_boundary_map",
    "draw_aesthetic_prior_craft_map",
    "draw_markov_blanket_scope_split",
    "draw_niche_prior_feedback_field",
    "draw_first_prior_grounding_stack",
]
