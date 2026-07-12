# Agent Instructions

Start from `src/conceptual_model.py` before changing prose, figures, or tests.
That file is the shared source of truth for quadrants, termination modes,
argument modules, figure specs, formal claims, symbol glossary, and
text-validation checks.

## Editing workflow

1. Update `src/conceptual_model.py` with any new records.
2. Update `src/figures/conceptual.py` and the relevant `src/figures/_*_figures.py`
   module if figure rendering needs to change.
3. Run `uv run python scripts/build_publication_package.py` to regenerate the
   complete package in dependency order.
4. Run `uv run pytest tests/` to verify source and generated contracts.

## Figure captions

Captions, accessibility text, and figure grouping live in one place: the
`caption`, `alt_text`, and `section` fields of each `FigureSpec` in
`src/conceptual_model.py`. The figure registry, API reference, dashboard, and
manuscript are generated from those fields. Change the source record and
regenerate; do not edit one surface in isolation.

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
