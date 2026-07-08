# AGENTS.md - Prior Cognitive Art

This project lives in the private sidecar under `working/` and is mirrored into
the public template checkout as `projects/working/prior_cognitive_art`.

## Project Contract

- This is a conceptual manuscript, not a simulation study.
- Keep all argument inventory and figure manifest data in `src/conceptual_model.py`.
- Keep scripts thin. `scripts/optimization_analysis.py` is retained for template
  compatibility, but it generates deterministic conceptual figures and reports.
- Manuscript figures must live under `output/figures/` and be referenced as
  `../output/figures/<name>.png`.
- Do not add stochastic experiments or empirical performance
  numbers unless the manuscript scope is deliberately changed.

## Verification

```bash
uv run pytest projects/working/prior_cognitive_art/tests/
uv run python projects/working/prior_cognitive_art/scripts/optimization_analysis.py
uv run python projects/working/prior_cognitive_art/scripts/z_generate_manuscript_variables.py
uv run python scripts/03_render_pdf.py --project working/prior_cognitive_art
```
