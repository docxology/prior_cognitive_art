# Preprint Release Checklist

Date: 2026-07-10

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
- [ ] Run `uv run python scripts/build_publication_package.py`.
- [ ] Confirm `output/reports/render_manifest.json` is present and current.
- [ ] Run `qpdf --check output/pdf/prior_cognitive_art_combined.pdf`.
- [ ] Run a PDF text scan for stale planning language, unresolved render tokens,
      and task-marker residue.

## Visual QA

- [ ] Inspect all 21 figure PNGs via contact sheet and representative full-size
      views; confirm the atlas has 18 figures and the formal supplement has 3.
- [ ] Inspect representative PDF pages: title page, table of contents,
      abstract, introduction, main visual atlas pages, formal supplement, and
      references.
- [ ] Confirm the late-added figures render:
      `source_claim_boundary_map`, `markov_blanket_scope_split`, and
      `niche_prior_feedback_field`, plus `aesthetic_prior_craft_map` and
      `first_prior_grounding_stack` and `deterministic_simulation_trace`.
- [ ] Confirm the square cover art is 2048 x 2048 pixels and visually legible
      at thumbnail size.
- [ ] Confirm the title page shows the cover art, automatic render date, and
      `DOI: forthcoming`.
- [ ] Serve `output/` as the web root and open `/web/index.html` in a browser;
      confirm no missing images, console errors, broken links, stale counts,
      raw citation markers, or unresolved tokens at desktop and mobile widths.

## Metadata

- [ ] Select release venue or preprint server.
- [ ] Select license.
- [ ] Confirm author order and affiliations.
- [ ] Confirm funding statement.
- [ ] Confirm competing-interest statement.
- [ ] Confirm data and materials statement: no empirical dataset; deterministic
      conceptual artifacts and one deterministic illustrative trace only.
- [ ] Confirm repository/deposition route if code or artifacts are shared.

## Final Release Notes

- [ ] Use the bounded claim from `docs/submission_package.md`.
- [ ] Use reviewer risks from `docs/reviewer_risk_register.md` to avoid
      overstating Markov blanket, active-inference, or niche-construction claims.
- [ ] Archive the final PDF checksum and release date.
- [ ] Record the public URL or DOI after release.
