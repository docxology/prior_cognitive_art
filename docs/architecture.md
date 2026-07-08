# Architecture

## Layer boundaries

`src/` contains importable conceptual inventory and deterministic visualization
builders. `scripts/` contains thin entry points for the template runner.
`manuscript/` contains the publication prose with `{{VARIABLE}}` tokens hydrated
from `src/manuscript_variables.py`. `tests/` exercises the real workflow without
mocks. `data/` holds the claim ledger. `docs/` holds local workflow
documentation.

## Source modules

| Module | Role |
|---|---|
| `src/conceptual_model.py` | Static argument and figure inventory, formal claims, symbol glossary, validation checks, integrity token |
| `src/figures/conceptual.py` | Public figure-generation orchestrator and stable import surface |
| `src/figures/_*_figures.py` | Deterministic matplotlib visualization builders split by responsibility (18 figures total) |
| `src/figures/_shared.py` | Shared palette, drawing helpers, and save routine |
| `src/analysis/workflow.py` | Output generation for the template analysis stage |
| `src/manuscript_variables.py` | Token hydration from conceptual inventory and config |
| `src/documentation.py` | API reference markdown generation |
| `src/project_paths.py` | Path resolution for project root and output directories |
| `src/_runtime.py` | Infrastructure-aware logger and project root helpers |

## Figure captions

Figure captions have a **single source of truth**: the `caption` field of each
`FigureSpec` in `src/conceptual_model.py`. The figure registry
(`output/figures/figure_registry.json`), the API reference, the dashboard, and
the manuscript's figure manifest are all generated from that field. Inline
alt-text in the manuscript (`03_results.md`, `08_formal_supplement.md`) is
written to match the same wording. Do not hand-edit a caption in only one of
these surfaces; change `FigureSpec.caption` and regenerate artifacts
(`scripts/optimization_analysis.py`, `scripts/generate_api_docs.py`,
`scripts/build_dashboard.py`).

## Scripts

| Script | Role |
|---|---|
| `scripts/optimization_analysis.py` | Generate figures, reports, data (compatibility name) |
| `scripts/build_dashboard.py` | Styled HTML dashboard + JSON data payload |
| `scripts/generate_api_docs.py` | API reference markdown + glossary |
| `scripts/z_generate_manuscript_variables.py` | Hydrate manuscript tokens |
| `scripts/00_preflight.py` | Manuscript rendering pre-flight check |

## The retained name

The retained `optimization_analysis.py` filename is compatibility glue. Its
behavior is conceptual figure generation, not optimization analysis. The
template analysis stage looks for this filename pattern.
