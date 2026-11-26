# tests/

Run from the project root:

```bash
uv sync --extra dev
uv run --extra dev pytest tests/
```

Or with coverage:

```bash
uv run --extra dev pytest tests/ \
  --cov=src \
  --cov-report=term-missing
```

The suite checks concept inventory, figure generation, script smoke behavior,
manuscript token hydration, contract error branches, path resolution, claim
ledger integrity, domain profile consistency, and experiment plan alignment.

The suite is the source-contract gate for `src/`, generated reports, figure
artifacts, manuscript hydration, and publication-package negative controls.
