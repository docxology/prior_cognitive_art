# src/figures/

Deterministic figure builders for the Prior Cognitive Art manuscript.

| Module | Role |
|---|---|
| `conceptual.py` | Public figure-generation orchestrator and stable import surface |
| `_argument_figures.py` | Argument-structure figures |
| `_art_figures.py` | Bounded-art figures |
| `_boundary_figures.py` | No-simulation boundary figures |
| `_contract_figures.py` | Contract / manifest figures |
| `_niche_blanket_figures.py` | Niche and blanket (Markov boundary) figures |
| `_upstream_figures.py` | Upstream-first-prior figures |
| `_active_scale_figures.py` | Active-inference scale figures |
| `_cover_art.py` | Cover art generation |
| `_shared.py` | Shared semantic palette, drawing helpers, and save routine |

Run the orchestrator (directly or via `src/analysis/workflow.py` /
`scripts/optimization_analysis.py`); outputs land in `output/figures/`.
