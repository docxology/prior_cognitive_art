# Agent Instructions

Start from `src/conceptual_model.py` before changing prose, figures, or tests.
That file is the shared source of truth for quadrants, termination modes,
argument modules, figure specs, formal claims, symbol glossary, and
text-validation checks.

## Editing workflow

1. Update `src/conceptual_model.py` with any new records.
2. Update `src/figures/conceptual.py` and the relevant `src/figures/_*_figures.py`
   module if figure rendering needs to change.
3. Run `scripts/optimization_analysis.py` to regenerate figures and reports.
4. Run `scripts/z_generate_manuscript_variables.py` to hydrate manuscript tokens.
5. Run `scripts/build_dashboard.py` and `scripts/generate_api_docs.py` for docs.
6. Run `uv run pytest projects/working/prior_cognitive_art/tests/` to verify.

## Figure captions

Captions live in one place: the `caption` field of each `FigureSpec` in
`src/conceptual_model.py`. The figure registry, API reference, dashboard, and
manuscript figure manifest are generated from it. Change `FigureSpec.caption`
and regenerate; do not edit a caption in only one surface.

## Project constraints

The project intentionally avoids simulations. If a change needs generated data,
it should be deterministic inventory or visualization metadata unless the user
explicitly changes the paper scope.

Do not reintroduce inherited optimization, metric, or convergence language from
the template scaffold. The retained `optimization_analysis.py` filename is
compatibility glue; its behavior is conceptual figure generation.

## No-mocks policy

Tests must use real data and computation. No `MagicMock`, `unittest.mock`, or
patching of library functions. Use `tmp_path` for temporary directories,
`pytest-httpserver` for HTTP, and `reportlab` for PDF generation if needed.
pytest's `monkeypatch` fixture is acceptable for setting/restoring environment
variables and module attributes during contract-validation tests.
