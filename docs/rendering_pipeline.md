# Rendering Pipeline

From the project root, run the canonical package build:

```bash
uv run python scripts/build_publication_package.py
```

The dependency order is source inventory -> figures/reports -> API docs ->
hydrated manuscript plus source fingerprint -> template PDF/web/slides render ->
dashboard refresh -> project-owned compact web CSS -> render-manifest stamping ->
final package validation. The validator is deliberately last: it checks the
rendered surfaces, not just the source files. It rejects stale hydrated
manuscript, combined Markdown, HTML, PDF, and slide artifacts by comparing the
source digest, embedded render fingerprints, and output hashes. It also checks
dashboard JSON parity, section/alt-text metadata, and stale mirrored assets.

The shared template renderer remains untouched. The project stylesheet at
`manuscript/web.css` is injected by `src/rendering.py` after rendering so the
HTML manuscript can use near-edge-to-edge layout without creating a template-
wide behavior change.
