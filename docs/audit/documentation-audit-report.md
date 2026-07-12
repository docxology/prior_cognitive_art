# Documentation Audit Report — Prior Cognitive Art

**Date:** 2026-07-10
**Scope:** `/Users/4d/Documents/GitHub/projects/working/prior_cognitive_art`
**Method:** source-contract parity, generated-surface freshness, bibliography
closure, rendered-token scans, PDF structural checks, and browser QA.

## Audit Results

| Check | Result |
|---|---|
| Broken internal Markdown links | **0** in the checked project documentation |
| Bibliography bidirectional closure | **Closed**: 81 entries, 81 cited |
| Generated-artifact count vs docs | **21 PNGs** = 21 claimed |
| Figure classification | **Closed**: 18 Visual Atlas + 3 Formal Supplement |
| Caption/alt-text/section ownership | **Closed**: `FigureSpec` registry, hydration, dashboard, and validator agree |
| Dashboard inventory parity | **Closed**: counts, sections, metadata, grounding edges, and integrity token agree |
| Render freshness | **Closed**: hydrated source digest and output hashes agree for Markdown, HTML, PDF, and slides |
| Conceptual scope | **Closed**: no stochastic or empirical performance claims introduced |
| Source tests | **93 passed** |

## Implemented hardening

- `FigureSpec` now owns `section` and accessibility `alt_text` in addition to
  the publication caption.
- The visual atlas is explicitly 18 argument diagrams; the formal supplement
  owns 3 contract diagrams.
- Hydrated manuscript figure alt text is generated from the inventory and
  validated against every figure reference.
- The canonical `scripts/build_publication_package.py` runs analysis, API docs,
  hydration, rendering, dashboard generation, web styling, freshness-manifest
  stamping, and validation in one fail-fast sequence.
- `src/render_manifest.py` hashes source inputs and rendered Markdown, HTML,
  PDF, and slide surfaces; stale files are blocking failures.
- Project-owned `manuscript/web.css` provides compact, near-edge-to-edge HTML
  layout without modifying the shared template renderer.
- The cover was simplified while retaining deterministic 2048 x 2048 PNG/SVG
  outputs. Variational and active-inference semantics were clarified.
- Documentation now names the source-owned contracts and the observed QA
  evidence rather than relying on stale render screenshots.

## Verification Evidence

- Canonical build: `uv run python scripts/build_publication_package.py` -> pass.
- Package validator: `ok: true`, no issues.
- PDF: 43 pages, letter size; `qpdf --check` clean; 22/22 image references.
- Text scans: no unresolved template tokens, raw citation markers, or draft
  residue in rendered manuscript surfaces.
- Visual QA: cover, 21-figure contact sheet, representative full-size figures,
  title page, dense prose, formal supplement, glossary, and references checked.
- Browser QA: `/web/index.html` and `/web/dashboard.html` served from `output/`
  at desktop and 390px mobile widths; no broken images, horizontal overflow,
  console errors, unresolved tokens, or raw citations after the favicon fix.

## Remaining / out of scope

- Venue-specific formatting and submission metadata remain downstream choices.
- The project does not claim empirical validation; its reproducibility claim is
  about source-owned conceptual artifacts and deterministic rendering.

**Status: publication-ready as a venue-neutral working paper.**
