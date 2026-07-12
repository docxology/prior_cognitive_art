# Prior Cognitive Art

Prior Cognitive Art is a working manuscript project rewritten from the public
`template_code_project` scaffold as a conceptual paper with a bounded
deterministic illustrative simulation trace. It explores why a prior exists by
first typing the explanatory kind of the question, then separating Tinbergen's four questions into
crossed axes, comparing ontogenetic regress with the hierarchical Bayes
hyperprior problem, and treating selection and fixed-point organization as the
live stopping moves.

The project uses plain text, deterministic conceptual visualizations, and one
authored formal-state trace. It does not run stochastic simulations, synthetic
data experiments, empirical-effect estimation, or numerical performance claims.

## Run

From the template checkout:

```bash
uv run python scripts/build_publication_package.py
```

The canonical build delegates in order to analysis/figures, API docs,
manuscript hydration, template PDF/web/slide rendering, dashboard generation,
project-owned web CSS, render-manifest stamping, and package validation. The
freshness manifest makes stale hydrated Markdown, combined Markdown, HTML, PDF,
or slide artifacts a blocking failure.

## Generated Artifacts

### Figures (18 atlas diagrams + 3 formal-supplement contract diagrams)

- `output/figures/tinbergen_axes.png`
- `output/figures/regress_terminations.png`
- `output/figures/prior_equilibrium_map.png`
- `output/figures/ontogeny_hyperprior_parallel.png`
- `output/figures/selection_filter.png`
- `output/figures/policy_entanglement_bridge.png`
- `output/figures/formal_claim_dependency_map.png`
- `output/figures/symbol_glossary_closure.png`
- `output/figures/text_validation_ladder.png`
- `output/figures/niche_construction_diagram.png`
- `output/figures/markov_blanket_achievement.png`
- `output/figures/explanatory_complementarity_matrix.png`
- `output/figures/active_inference_cycle.png`
- `output/figures/variational_free_energy_landscape.png`
- `output/figures/deterministic_simulation_trace.png`
- `output/figures/scale_recurrence_diagram.png`
- `output/figures/source_claim_boundary_map.png`
- `output/figures/aesthetic_prior_craft_map.png`
- `output/figures/markov_blanket_scope_split.png`
- `output/figures/niche_prior_feedback_field.png`
- `output/figures/first_prior_grounding_stack.png`

The 18 figures in the visual atlas carry the substantive argument. The three
formal-supplement figures (`formal_claim_dependency_map`,
`symbol_glossary_closure`, and `text_validation_ladder`) validate the manuscript
contract. Captions, source sections, and accessibility alt text are owned by
`FigureSpec` in `src/conceptual_model.py` and hydrated into every publication
surface.

### Reports and Data

- `output/reports/conceptual_analysis.json`
- `output/reports/figure_manifest.json`
- `output/reports/cover_art_manifest.json`
- `output/reports/deterministic_simulation_manifest.json`
- `output/reports/render_manifest.json`
- `output/data/conceptual_map.json`
- `output/data/deterministic_simulation_trace.json`
- `output/data/manuscript_variables.json`
- `output/figures/figure_registry.json`

### Cover Art

- `output/cover/prior_cognitive_art_cover_square.png`
- `output/cover/prior_cognitive_art_cover_square.svg`

The cover art is a deterministic 2048 x 2048 square asset for the PDF title
page, preprint cards, dashboard presentation, and venue-neutral promotion. It
is not counted as one of the 21 manuscript figures.

### Web Dashboard

- `output/web/dashboard.html` — styled dashboard with figure gallery, concept
  inventory, formal claims, symbol glossary, and validation checks
- `output/web/dashboard_data.json` — schema-versioned compact JSON payload for
  programmatic consumers, including source-grounding edges and inventory counts

### API Documentation

- `output/docs/api_reference.md` — full source reference generated from the
  conceptual inventory
- `output/docs/api_glossary.md` — auto-generated API glossary (when available)
- `scripts/validate_publication_package.py` — source-count and artifact
  consistency gate for the venue-neutral package

## Conceptual Inventory

| Concept | Count |
|---|---|
| Tinbergen quadrants | 4 |
| Termination modes | 3 |
| Argument modules | 12 |
| Generated figures | 21 |
| Formal claims | 12 |
| Symbol glossary rows | 35 |
| Text-validation checks | 11 |
| Claim dependencies | 14 |
| Claim grounding edges | 12 |

All counts are generated from `src/conceptual_model.py` and validated by a
source contract that checks for symbol glossary closure, figure manifest
alignment, formal-claim key uniqueness, and drift in published documentation
counts.

## Scope

The paper is a venue-neutral working manuscript with a verified source base.
The source layer stores the argument inventory, visualization manifest, formal
claims, symbol glossary, and text-validation checks so the manuscript, figures,
and tests stay aligned while publication prose changes.

## Publication Package

- `docs/publication_readiness_report.md` records the final readiness gate.
- `docs/submission_package.md` provides venue-neutral abstract, keywords,
  contribution statements, reproducibility notes, and remaining submission
  fields.
- `docs/reviewer_risk_register.md` maps likely reviewer objections to the
  current manuscript, figures, claim ledger, and gate evidence.
- `docs/cover_letter_template.md`, `docs/venue_selection_matrix.md`, and
  `docs/preprint_release_checklist.md` support the next submission step without
  changing the manuscript's venue-neutral scope.

## Testing

```bash
uv run pytest projects/working/prior_cognitive_art/tests/ --cov=projects/working/prior_cognitive_art/src
```

The project test suite covers the conceptual inventory, generated artifacts,
hydration, rendering contracts, source-owned visual metadata, freshness gates,
and publication-package negative controls.
