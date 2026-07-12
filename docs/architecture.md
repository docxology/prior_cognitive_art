# Architecture

## Layer boundaries

`src/` contains importable conceptual inventory and deterministic visualization
builders. `scripts/` contains thin entry points for the template runner, with
`build_publication_package.py` as the fail-fast orchestration boundary.
`manuscript/` contains the publication prose with `{{VARIABLE}}` tokens hydrated
from `src/manuscript_variables.py`. `tests/` exercises the real workflow without
mocks. `data/` holds the claim ledger. `docs/` holds local workflow
documentation.

The analysis stage reconciles stale generated PNG/SVG siblings before writing
the source-owned reports and deterministic figures, so renames cannot leave
orphaned visual artifacts in `output/figures/`.

The dashboard is another generated surface, not a hand-maintained summary:
`output/web/dashboard_data.json` carries a versioned source inventory payload
and the publication validator compares it back to the conceptual model. The
render manifest separately hashes hydrated source inputs and every rendered
Markdown, HTML, PDF, and slide surface.

## Source modules

| Module | Role |
|---|---|
| `src/conceptual_model.py` | Static argument and figure inventory, formal claims, symbol glossary, validation checks, integrity token |
| `src/figures/conceptual.py` | Public figure-generation orchestrator and stable import surface |
| `src/figures/_*_figures.py` | Deterministic matplotlib visualization builders split by responsibility (21 figures total) |
| `src/figures/_shared.py` | Shared semantic palette, drawing helpers, and save routine |
| `src/analysis/workflow.py` | Output generation for the template analysis stage |
| `src/manuscript_variables.py` | Token hydration from conceptual inventory and config |
| `src/render_manifest.py` | Source fingerprinting and rendered-output freshness gate |
| `src/rendering.py` | Project-owned post-render web CSS injection |
| `src/documentation.py` | API reference markdown generation |
| `src/project_paths.py` | Path resolution for project root and output directories |
| `src/_runtime.py` | Infrastructure-aware logger and project root helpers |

## Figure captions

Figure metadata has a **single source of truth**: `FigureSpec.caption` owns the
publication caption, `FigureSpec.alt_text` owns accessibility text, and
`FigureSpec.section` owns the 18-figure atlas versus 3-figure formal-supplement
classification. The figure registry, API reference, dashboard, manuscript
alt-text, and figure manifest are generated from these fields. Do not hand-edit
one surface; change the source record and regenerate artifacts
(`scripts/optimization_analysis.py`, `scripts/generate_api_docs.py`,
`scripts/z_generate_manuscript_variables.py`, `scripts/build_dashboard.py`).

## Scripts

| Script | Role |
|---|---|
| `scripts/optimization_analysis.py` | Generate figures, reports, data (compatibility name) |
| `scripts/build_publication_package.py` | Fail-fast canonical build and freshness validation |
| `scripts/build_dashboard.py` | Styled HTML dashboard + JSON data payload |
| `scripts/generate_api_docs.py` | API reference markdown + glossary |
| `scripts/z_generate_manuscript_variables.py` | Hydrate manuscript tokens |
| `scripts/00_preflight.py` | Manuscript rendering pre-flight check |

## The retained name

The retained `optimization_analysis.py` filename is compatibility glue. Its
behavior is conceptual figure generation, not optimization analysis. The
template analysis stage looks for this filename pattern.
