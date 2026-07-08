# Code Review And Slop Coverage After Split

Status: APPROVE

Scope:

- `src/figures/conceptual.py`
- `src/figures/_argument_figures.py`
- `src/figures/_contract_figures.py`
- `src/figures/_niche_blanket_figures.py`
- `src/figures/_active_scale_figures.py`
- `src/figures/_boundary_figures.py`
- `src/figures/_shared.py`
- `tests/test_project_internals.py`

Programming and remove-ai-slops criteria:

- Oversized-module rule: resolved. `figure-module-size-after-split.log` reports
  all `src/figures/*.py` files at or below 250 pure LOC:
  `conceptual.py` 81, `_argument_figures.py` 221, `_contract_figures.py` 204,
  `_niche_blanket_figures.py` 168, `_active_scale_figures.py` 157,
  `_boundary_figures.py` 204, `_shared.py` 74, `__init__.py` 2.
- `SIZE_OK`: not used and not needed because no figure module exceeds the
  ceiling after the split.
- Public API preservation: `src.figures.conceptual` still exports
  `generate_all_figures` and all draw functions. The monkeypatch regression
  test for `draw_tinbergen_axes` still passes through the orchestrator.
- Behavior preservation: `optimization_analysis.py` generated the same 18
  expected figure files after the split, and `render-pdf-after-split.log`
  reports 18/18 figure references found.
- Overfit coverage: `test_figure_modules_stay_under_pure_loc_ceiling` prevents
  the oversized renderer from silently returning; draft-residue and rendered
  token tests cover source and generated manuscript surfaces.
- Production marker cleanup: no appended new-figure section marker remains in
  production source.

Verification:

- `optimization-analysis-after-split.log`: generated all 18 figure PNG/SVG
  outputs and refreshed analysis reports.
- `figure-split-focused-tests.log`: focused figure generation tests passed.
- `pytest-after-split.log`: 73 tests passed.
- `render-pdf-after-split.log`: combined PDF rendered with 18/18 figure
  references found.
- `qpdf-check-after-split.log`: no syntax or stream-encoding errors.
- `final-contract-closure-after-split.log`: figure/citation/claim/source counts
  closed and all figure modules <=250 pure LOC.

Residual risk:

- The figure renderer remains a conceptual visualization system rather than an
  empirical or simulation engine. This is intentional and aligned with the
  project contract.
