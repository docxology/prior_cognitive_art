# scripts/ AGENTS

## Thin-orchestrator contract

Scripts are thin entry points: argparse, path bootstrap, logging, and a single
delegated call into a `src/` entrypoint. Business, data, plot, validation, and
presentation logic lives in `src/` (importable and tested):

- `optimization_analysis.py` -> `src/analysis/workflow.py`
- `build_dashboard.py` -> `src/dashboard.py`
- `generate_api_docs.py` -> `src/documentation.py`
- `z_generate_manuscript_variables.py` -> `src/manuscript_variables.py`
- `validate_publication_package.py` -> `src/publication_validation.py`
- `build_publication_package.py` -> the stage scripts above plus
  `src/rendering.py` and `src/render_manifest.py`

`optimization_analysis.py` is retained because the template analysis stage looks
for project scripts. In this project it generates conceptual figures, JSON
reports, and the deterministic illustrative trace; it does not run stochastic
simulations or empirical analyses.

## Inventory

| Script | Purpose | Delegates to |
| --- | --- | --- |
| `00_preflight.py` | Check manuscript rendering prerequisites | `infrastructure.rendering.preflight` |
| `optimization_analysis.py` | Generate conceptual figures, reports, data | `src/analysis/workflow.py` |
| `build_publication_package.py` | Fail-fast canonical build + freshness validation | stage scripts + `src/rendering.py`, `src/render_manifest.py` |
| `build_dashboard.py` | Styled HTML dashboard + JSON data payload | `src/dashboard.py` |
| `generate_api_docs.py` | API reference markdown + API glossary | `src/documentation.py` |
| `z_generate_manuscript_variables.py` | Hydrate manuscript variables into output/ | `src/manuscript_variables.py` |
| `validate_publication_package.py` | Source-count and artifact consistency gate | `src/publication_validation.py` |

Run order:

```bash
uv run python scripts/optimization_analysis.py
uv run python scripts/build_dashboard.py
uv run python scripts/generate_api_docs.py
uv run python scripts/z_generate_manuscript_variables.py
```

Optional pre-flight check:

```bash
uv run python scripts/00_preflight.py
```
