# Rendering Pipeline

From the template checkout:

```bash
uv run python projects/working/prior_cognitive_art/scripts/optimization_analysis.py
uv run python projects/working/prior_cognitive_art/scripts/z_generate_manuscript_variables.py
uv run python scripts/03_render_pdf.py --project working/prior_cognitive_art
```

The render consumes `output/manuscript/` after variable hydration.
