# Standalone Notes

This project can be edited directly in the private sidecar, but rendering is
expected to happen through the sibling `template` checkout.

Use from the project directory for local artifact generation:

```bash
uv run python scripts/optimization_analysis.py
uv run python scripts/build_dashboard.py
uv run python scripts/generate_api_docs.py
uv run python scripts/z_generate_manuscript_variables.py
```

Or run the template render command from `/Users/4d/Documents/GitHub/template`:

```bash
uv run python projects/working/prior_cognitive_art/scripts/optimization_analysis.py
uv run python projects/working/prior_cognitive_art/scripts/z_generate_manuscript_variables.py
uv run python scripts/03_render_pdf.py --project working/prior_cognitive_art
```

Run tests from the template checkout:

```bash
uv run pytest projects/working/prior_cognitive_art/tests/
```

The current publication-readiness gate is documented in
`docs/publication_readiness_report.md`; accepted and deferred source decisions
are recorded in `docs/scholarship-audit.md`.
