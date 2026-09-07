# scripts/

Thin project entry points. Business, data, and presentation logic lives in
`src/`; scripts only bootstrap paths and delegate to one module entrypoint.

| Script | Purpose | Delegates to | Command |
| --- | --- | --- | --- |
| `00_preflight.py` | Check manuscript rendering prerequisites | `infrastructure.rendering.preflight.run_manuscript_preflight` | `uv run python scripts/00_preflight.py` |
| `optimization_analysis.py` | Generate conceptual figures, reports, and data | `src.analysis.workflow` | `uv run python scripts/optimization_analysis.py` |
| `build_publication_package.py` | Fail-fast canonical build + freshness validation | stage scripts below + `src.rendering` + `src.render_manifest` | `uv run python scripts/build_publication_package.py` |
| `build_dashboard.py` | Write styled HTML dashboard + JSON data payload | `src.dashboard.build_dashboard` | `uv run python scripts/build_dashboard.py` |
| `generate_api_docs.py` | Write source reference markdown + API glossary | `src.documentation.build_api_reference_markdown` | `uv run python scripts/generate_api_docs.py` |
| `z_generate_manuscript_variables.py` | Hydrate manuscript variables into output/ | `src.manuscript_variables` + `infrastructure.rendering.manuscript_injection` | `uv run python scripts/z_generate_manuscript_variables.py` |
| `validate_publication_package.py` | Source-count and artifact consistency gate | `src.publication_validation.validate_publication_package` | `uv run python scripts/validate_publication_package.py` |

`__init__.py` marks the directory as a package for test imports;
`CONVENTIONS.md` records the thin-orchestrator rules.

Run order:

```bash
uv run python scripts/optimization_analysis.py
uv run python scripts/build_dashboard.py
uv run python scripts/generate_api_docs.py
uv run python scripts/z_generate_manuscript_variables.py
```
