# src/figures/ AGENTS

Agent-facing notes for the deterministic figure builders.

- `conceptual.py` is the public orchestrator and stable import surface;
  everything else (`_argument_figures.py`, `_art_figures.py`,
  `_boundary_figures.py`, `_contract_figures.py`,
  `_niche_blanket_figures.py`, `_upstream_figures.py`,
  `_active_scale_figures.py`, `_cover_art.py`, `_shared.py`) is private.
  Import only through `conceptual.py`.
- `_shared.py` owns the semantic palette, drawing helpers, and save
  routine — change style there once, not per-figure.
- Figures are deterministic: fixed seeds/geometry, no randomness or
  external data. Outputs land in `output/figures/`.
- Adding a figure: extend the relevant `_*.py` builder and register it in
  `conceptual.py` so the figure manifest in `src/conceptual_model.py`
  stays consistent (18-figure contract as of publication readiness).
- Run via the orchestrator, `src/analysis/workflow.py`, or
  `scripts/optimization_analysis.py`.

See `../../AGENTS.md` (project root) for the project contract; each
parent directory's `AGENTS.md` above adds local context.
