# scripts/

Thin project entry points:

| Script | Role |
| --- | --- |
| `optimization_analysis.py` | Generate conceptual figures, reports, and data |
| `build_dashboard.py` | Write styled HTML dashboard + JSON data payload |
| `generate_api_docs.py` | Write source reference markdown + API glossary |
| `z_generate_manuscript_variables.py` | Hydrate manuscript variables into output/ |
| `00_preflight.py` | Check manuscript rendering prerequisites |

Run order:

```bash
uv run python scripts/optimization_analysis.py
uv run python scripts/build_dashboard.py
uv run python scripts/generate_api_docs.py
uv run python scripts/z_generate_manuscript_variables.py
```
