# Prior Cognitive Art

Prior Cognitive Art is a working manuscript project rewritten from the public
`template_code_project` scaffold as a simulation-free conceptual paper. It
explores why a prior exists by separating Tinbergen's four questions into
crossed axes, comparing ontogenetic regress with the hierarchical Bayes
hyperprior problem, and treating selection and fixed-point organization as the
live stopping moves.

The project uses plain text plus deterministic conceptual visualizations. It
does not run simulations, estimate empirical effects, or claim numerical
results.

## Run

From the template checkout:

```bash
uv run python projects/working/prior_cognitive_art/scripts/optimization_analysis.py
uv run python projects/working/prior_cognitive_art/scripts/z_generate_manuscript_variables.py
uv run python projects/working/prior_cognitive_art/scripts/validate_publication_package.py
uv run python scripts/03_render_pdf.py --project working/prior_cognitive_art
```

The first command generates figures and JSON reports under `output/`. The second
hydrates manuscript variables into `output/manuscript/`.

## Generated Artifacts

### Figures (18 conceptual visualizations)

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
- `output/figures/scale_invariance_diagram.png`
- `output/figures/source_claim_boundary_map.png`
- `output/figures/markov_blanket_scope_split.png`
- `output/figures/niche_prior_feedback_field.png`

### Reports and Data

- `output/reports/conceptual_analysis.json`
- `output/reports/figure_manifest.json`
- `output/reports/cover_art_manifest.json`
- `output/data/conceptual_map.json`
- `output/data/manuscript_variables.json`
- `output/figures/figure_registry.json`

### Cover Art

- `output/cover/prior_cognitive_art_cover_square.png`
- `output/cover/prior_cognitive_art_cover_square.svg`

The cover art is a deterministic 2048 x 2048 square asset for preprint cards,
dashboard presentation, and venue-neutral promotion. It is not counted as one
of the 18 manuscript figures.

### Web Dashboard

- `output/web/dashboard.html` — styled dashboard with figure gallery, concept
  inventory, formal claims, symbol glossary, and validation checks
- `output/web/dashboard_data.json` — compact JSON payload for programmatic consumers

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
| Argument modules | 10 |
| Generated figures | 18 |
| Formal claims | 11 |
| Symbol glossary rows | 25 |
| Text-validation checks | 10 |
| Claim dependencies | 12 |

All counts are generated from `src/conceptual_model.py` and validated by a
source contract that checks for symbol glossary closure, figure manifest
alignment, and formal-claim key uniqueness.

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

76 tests, 100% coverage target on `src/`.
