# Prior Cognitive Art Publication Readiness Report

Date: 2026-07-07

## Readiness Decision

Current decision: ready for venue-neutral preprint / working-paper circulation.
The manuscript has been revised, regenerated, rendered, scanned, and visually
checked. No known publication-blocking gaps remain inside the project contract.

## Scope

This pass targets the docxology project contract, not a target journal package.
It keeps the paper conceptual and simulation-free. No stochastic experiments,
empirical performance numbers, or fake quantitative results were introduced.

## Contract Surface

- Figures: 18 deterministic conceptual figures from `figure_specs()`.
- Formal claims: 11 records in `src/conceptual_model.py`.
- Claim ledger: 20 records in `data/claim_ledger.yaml`.
- Symbols: 25 glossary rows.
- Text checks: 10 validation checks.
- Claim dependency edges: 12.
- Bibliography: 40 BibTeX records in `manuscript/references.bib`.
- Tests: 76 project tests passed in the final gate.

## Evidence Summary

Green command evidence:

- `uv run python scripts/optimization_analysis.py` generated all figures,
  figure registry, conceptual report, and conceptual map.
- `uv run python scripts/build_dashboard.py` refreshed
  `output/web/dashboard.html` and `output/web/dashboard_data.json`.
- `uv run python scripts/generate_api_docs.py` refreshed
  `output/docs/api_reference.md` and `output/docs/api_glossary.md`.
- `uv run python scripts/z_generate_manuscript_variables.py` hydrated 11
  manuscript files and `output/data/manuscript_variables.json`.
- `uv run python scripts/validate_publication_package.py` rechecked required
  metadata, rendered outputs, source-owned counts, generated reports, figure
  artifacts, and unresolved rendered tokens.
- `uv run pytest tests/` passed: 76 tests.
- From `/Users/4d/Documents/GitHub/template`,
  `uv run python -m infrastructure.orchestration link-projects --dry-run`
  reported 0 created, 0 updated, 0 removed, 0 skipped.
- From `/Users/4d/Documents/GitHub/template`,
  `uv run python scripts/03_render_pdf.py --project working/prior_cognitive_art`
  generated `output/pdf/prior_cognitive_art_combined.pdf` at 1.98 MB, with
  18/18 figure references found after the figure-renderer split.
- `qpdf --check output/pdf/prior_cognitive_art_combined.pdf` found no syntax or
  stream-encoding errors.
- `pdftotext` plus `rg` found no broad draft/future-work markers, unresolved
  template tokens, or task-marker residue in the final PDF text.
- Source, hydrated manuscript, combined PDF markdown, and combined web markdown
  scans found no broad draft/future-work markers or unresolved output tokens.
- Final contract closure check reported: 18 figures, 18 PNGs, 18 SVGs, 11
  formal claims, 20 claim-ledger records, 25 symbols, 10 validation checks, 12
  claim dependency edges, 40 BibTeX entries, and 40 cited BibTeX keys.
- The publication-package validator reported no issues and recomputed 18
  figures, 11 formal claims, 25 symbols, 10 text-validation checks, and 12
  claim dependency edges from source-owned records.
- The analysis pipeline now also generates square-format cover art at
  `output/cover/prior_cognitive_art_cover_square.png` with metadata in
  `output/reports/cover_art_manifest.json`; this asset is outside the 18-figure
  manuscript contract.
- Post-review slop coverage split the figure renderer into submodules below
  the 250 pure-LOC ceiling and added a regression test for that ceiling.

## Scholarship Gate

Accepted source decisions are recorded in `docs/scholarship-audit.md`. The
main changes were not bibliography padding: each promoted source tightened a
claim boundary, manuscript section, figure, or ledger row.

## Submission Support

- `docs/submission_package.md` now provides venue-neutral abstract, keywords,
  contribution statements, reproducibility notes, figure-set guidance, and the
  venue-specific fields still requiring author or venue selection.
- `docs/reviewer_risk_register.md` now maps likely objections to manuscript
  sections, figures, the claim ledger, scholarship audit, and final gate
  evidence.
- `docs/cover_letter_template.md`, `docs/venue_selection_matrix.md`, and
  `docs/preprint_release_checklist.md` now support venue choice, cover-letter
  adaptation, and release QA without changing the manuscript's venue-neutral
  scope.

## Visual QA Notes

Manual visual QA passed on:

- All 18 refreshed figure PNGs via
  `.omo/ulw-loop/prior-cognitive-art-publication-readiness-20260707-051719/evidence/figure-contact-sheet-reassess.png`.
- Square cover art via `output/cover/prior_cognitive_art_cover_square.png`.
- Representative final PDF pages 1-4 and 17-22 via
  `.omo/ulw-loop/prior-cognitive-art-publication-readiness-20260707-051719/evidence/pdf-page-contact-sheet-reassess.png`.

The figures are nonblank, framed on page, and the three new visuals render in
the visual atlas without obvious overlap or clipping. The PDF remains
letter-sized, 37 pages, and visually coherent in the sampled front matter,
introduction, results atlas, and formal-supplement pages.

## Remaining Risks

- Venue-specific formatting is not complete because no venue was selected.
- Cover-letter field values, author metadata, funding declarations, license,
  and repository/deposition choices still require author or venue decisions.
- The conceptual figures use deterministic geometry and illustrative fields;
  they are not empirical outputs.
- The Markov blanket discussion is deliberately bounded; readers wanting a full
  literature review of the controversy should treat the cited critique pair as
  scope control rather than exhaustion.
