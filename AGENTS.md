# AGENTS.md - Prior Cognitive Art

This project lives in the private sidecar under
`ongoing/Uncategorized/` and is mirrored into the public template checkout
as `projects/ongoing/Uncategorized/prior_cognitive_art`.

## Layout map

- `src/` — conceptual model, figure modules (`src/figures/`), analysis workflow (`src/analysis/`), rendering + manuscript variables
- `data/` — claim ledger and inputs (has own AGENTS.md/README.md)
- `docs/manuscript/` — manuscript sections
- `scripts/` — thin orchestrators (see Project Contract below)
- `tests/` — pytest suite
- `docs/` — project documentation incl. `audit/` reports
- `.omo/` — agent-loop campaign state (evidence + timestamped ulw-loop runs); QA/evidence artifacts only
- `.codex_qa/` — rendered PDF-page QA images, contact sheets, and caption pages at the repo root; QA artifacts only, not manuscript sources

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
uv run pytest projects/ongoing/Uncategorized/prior_cognitive_art/tests/
uv run python projects/ongoing/Uncategorized/prior_cognitive_art/scripts/optimization_analysis.py
uv run python projects/ongoing/Uncategorized/prior_cognitive_art/scripts/z_generate_manuscript_variables.py
uv run python scripts/03_render_pdf.py --project ongoing/Uncategorized/prior_cognitive_art
```
