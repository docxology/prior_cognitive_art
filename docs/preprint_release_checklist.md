# Preprint Release Checklist

Date: 2026-07-07

Use this checklist only after the author chooses to circulate the manuscript as
a preprint or public working paper. It assumes the current venue-neutral
readiness gate remains green.

## Manuscript Files

- [ ] Confirm `output/pdf/prior_cognitive_art_combined.pdf` is the intended
      release PDF.
- [ ] Confirm `output/web/index.html` is acceptable if a web version is shared.
- [ ] Confirm title, subtitle, author names, affiliations, and corresponding
      author details.
- [ ] Confirm abstract and keywords match `docs/submission_package.md`.
- [ ] Confirm `output/cover/prior_cognitive_art_cover_square.png` is
      suitable for square-format preprint or social preview use.
- [ ] Confirm no private notes, local-only paths, or internal process text are
      visible in the release PDF.

## Reproducibility And Source Package

- [ ] Run `uv run pytest tests/`.
- [ ] Run `uv run python scripts/optimization_analysis.py`.
- [ ] Run `uv run python scripts/build_dashboard.py`.
- [ ] Run `uv run python scripts/generate_api_docs.py`.
- [ ] Run `uv run python scripts/z_generate_manuscript_variables.py`.
- [ ] From `/Users/4d/Documents/GitHub/template`, run
      `uv run python scripts/03_render_pdf.py --project working/prior_cognitive_art`.
- [ ] Run `qpdf --check output/pdf/prior_cognitive_art_combined.pdf`.
- [ ] Run a PDF text scan for stale planning language, unresolved render tokens,
      and task-marker residue.

## Visual QA

- [ ] Inspect all 18 figure PNGs.
- [ ] Inspect representative PDF pages: title page, table of contents,
      abstract, introduction, main visual atlas pages, formal supplement, and
      references.
- [ ] Confirm the three late-added figures render:
      `source_claim_boundary_map`, `markov_blanket_scope_split`, and
      `niche_prior_feedback_field`.
- [ ] Confirm the square cover art is 2048 x 2048 pixels and visually legible
      at thumbnail size.

## Metadata

- [ ] Select release venue or preprint server.
- [ ] Select license.
- [ ] Confirm author order and affiliations.
- [ ] Confirm funding statement.
- [ ] Confirm competing-interest statement.
- [ ] Confirm data and materials statement: no empirical dataset; deterministic
      conceptual artifacts only.
- [ ] Confirm repository/deposition route if code or artifacts are shared.

## Final Release Notes

- [ ] Use the bounded claim from `docs/submission_package.md`.
- [ ] Use reviewer risks from `docs/reviewer_risk_register.md` to avoid
      overstating Markov blanket, active-inference, or niche-construction claims.
- [ ] Archive the final PDF checksum and release date.
- [ ] Record the public URL or DOI after release.
