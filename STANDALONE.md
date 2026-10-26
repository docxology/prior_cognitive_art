# Standalone Notes

This repository is the public mirror of a manuscript project that is edited in
the private sidecar and rendered through the sibling `template` checkout.

Use from the project root for local artifact generation:

```bash
uv run python scripts/optimization_analysis.py
uv run python scripts/build_dashboard.py
uv run python scripts/generate_api_docs.py
uv run python scripts/z_generate_manuscript_variables.py
```

Or run the mirror copy and the render stage from the `template` checkout root,
where the project is mirrored as `projects/ongoing/Uncategorized/prior_cognitive_art`:

```bash
uv run python projects/ongoing/Uncategorized/prior_cognitive_art/scripts/optimization_analysis.py
uv run python projects/ongoing/Uncategorized/prior_cognitive_art/scripts/z_generate_manuscript_variables.py
uv run python scripts/pipeline/stage_03_render.py --project ongoing/Uncategorized/prior_cognitive_art
```

Run tests from the project root:

```bash
uv sync --extra dev
uv run --extra dev pytest tests/
```

The current publication-readiness gate is documented in
`docs/publication_readiness_report.md`; accepted and deferred source decisions
are recorded in `docs/scholarship-audit.md`.
