# tests/

Run from the template checkout:

```bash
uv run pytest projects/working/prior_cognitive_art/tests/
```

Or with coverage:

```bash
uv run pytest projects/working/prior_cognitive_art/tests/ \
  --cov=projects/working/prior_cognitive_art/src \
  --cov-report=term-missing
```

The suite checks concept inventory, figure generation, script smoke behavior,
manuscript token hydration, contract error branches, path resolution, claim
ledger integrity, domain profile consistency, and experiment plan alignment.

The suite is the source-contract gate for `src/`, generated reports, figure
artifacts, manuscript hydration, and publication-package negative controls.
