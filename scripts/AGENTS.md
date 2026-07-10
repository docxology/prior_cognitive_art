# scripts/ AGENTS

Scripts are thin entry points. Keep conceptual work in `src/` and have scripts
delegate.

`optimization_analysis.py` is retained because the template analysis stage looks
for project scripts. In this project it generates conceptual figures, JSON
reports, and the deterministic illustrative trace; it does not run stochastic
simulations or empirical analyses.

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
