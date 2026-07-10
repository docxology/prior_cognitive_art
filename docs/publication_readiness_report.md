# Prior Cognitive Art Publication Readiness Report

Date: 2026-07-09

## Readiness Decision

Current decision: ready for venue-neutral preprint / working-paper circulation.
The manuscript has been revised, regenerated, rendered, scanned, and visually
checked. No known publication-blocking gaps remain inside the project contract.

## Scope

This pass targets the Prior Cognitive Art project contract, not a target
journal package.
It keeps the paper conceptual while adding one deterministic illustrative
formal-state trace. No stochastic experiments, synthetic data, empirical
performance numbers, or fake quantitative results were introduced.

## Contract Surface

- Figures: 21 deterministic conceptual figures from `figure_specs()`.
- Argument modules: 12 records in `src/conceptual_model.py`.
- Formal claims: 12 records in `src/conceptual_model.py`.
- Claim ledger: 24 records in `data/claim_ledger.yaml`.
- Symbols: 28 glossary rows.
- Text checks: 10 validation checks.
- Claim dependency edges: 14.
- Bibliography: 77 BibTeX records in `manuscript/references.bib`.
- Tests: 77 project tests passed in the final gate.

## Evidence Summary

Green command evidence:

- `uv run python scripts/optimization_analysis.py` generated all 21 figures,
  figure registry, conceptual report, conceptual map, cover art, deterministic
  trace data, and deterministic trace manifest.
- `uv run python scripts/build_dashboard.py` refreshed
  `output/web/dashboard.html` and `output/web/dashboard_data.json`.
- `uv run python scripts/generate_api_docs.py` refreshed
  `output/docs/api_reference.md` and `output/docs/api_glossary.md`.
- `uv run python scripts/z_generate_manuscript_variables.py` hydrated 11
  manuscript files and `output/data/manuscript_variables.json`.
- `uv run python scripts/validate_publication_package.py` rechecked required
  metadata, rendered outputs, source-owned counts, generated reports, figure
  artifacts, and unresolved rendered tokens.
- `uv run pytest tests/` passed: 77 tests.
- From `/Users/4d/Documents/GitHub/template`,
  `uv run python -m infrastructure.orchestration link-projects --dry-run`
  reported 0 created, 0 updated, 0 removed, 0 skipped.
- From `/Users/4d/Documents/GitHub/template`,
  `uv run python scripts/03_render_pdf.py --project working/prior_cognitive_art`
  generated `output/pdf/prior_cognitive_art_combined.pdf`, with
  22/22 PDF image references found: 21 manuscript figures plus the title-page
  cover art.
- `qpdf --check output/pdf/prior_cognitive_art_combined.pdf` found no syntax or
  stream-encoding errors.
- `pdftotext` plus `rg` found no broad draft/future-work markers, unresolved
  template tokens, or task-marker residue in the final PDF text.
- Source, hydrated manuscript, combined PDF markdown, and combined web markdown
  scans found no broad draft/future-work markers or unresolved output tokens.
- Final contract closure check reported: 21 figures, 21 PNGs, 21 SVGs, 12
  formal claims, 24 claim-ledger records, 28 symbols, 10 validation checks, 14
  claim dependency edges, 77 BibTeX entries, and 77 cited BibTeX keys.
- The publication-package validator reported no issues and recomputed 21
  figures, 12 formal claims, 28 symbols, 10 text-validation checks, 14
  claim dependency edges, and 5 deterministic trace states from source-owned
  records. The validator now also compares the generated deterministic trace
  JSON against the exact source-owned state order, labels, transitions, and
  invariants.
- The analysis pipeline now also generates square-format cover art at
  `output/cover/prior_cognitive_art_cover_square.png` with metadata in
  `output/reports/cover_art_manifest.json`; this asset is used by the PDF title
  page and dashboard hero while remaining outside the manuscript-figure
  contract.
- Post-review slop coverage split the figure renderer into submodules below
  the 250 pure-LOC ceiling and added a regression test for that ceiling.

## Scholarship Gate

Accepted source decisions are recorded in `docs/scholarship-audit.md`. The
main changes were not bibliography padding: each promoted source tightened a
claim boundary, manuscript section, figure, or ledger row.

The 2026-07-08 passes added predictive-processing aesthetics,
material-engagement theory, 4E aesthetics, neuroaesthetic scope, imagination
scholarship, cultural-niche-construction sources, active-inference action-loop
sources, Tinbergen-leveling scholarship, and Bayesian/FEP overclaim controls to
bound the title's "art" claim and keep the variational-free-energy formalism
modest.

The 2026-07-09 upstream-bias pass added first-prior, co-homeostasis,
allostasis, developmental visceral-dynamics, morphogenesis, and evolutionary
active-inference sources to bound the "before the first prior" argument as a
constraint stack rather than a literal hidden meta-prior.

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

Manual visual QA passed on the refreshed artifact set:

- Square cover art via `output/cover/prior_cognitive_art_cover_square.png`.
- The rendered PDF title page via `.codex_qa/title_page.png`, including the
  cover art, `DOI: forthcoming`, and the automatic render date.
- The rendered deterministic trace figure and caption via
  `.codex_qa/page_21.png`.
- The post-render dashboard in Chrome via `.codex_qa/dashboard.png` and the
  mobile viewport via `.codex_qa/dashboard_mobile.png`; both loaded without
  broken image assets or console/page errors.
- Representative final PDF text and syntax checks via `pdftotext` and `qpdf`.

The figures are nonblank, framed on page, and the expanded visual set renders
without obvious overlap or clipping. The PDF remains letter-sized and visually
coherent in the front matter, results atlas, deterministic trace page, and
formal-supplement pages.

## Remaining Risks

- Venue-specific formatting is not complete because no venue was selected.
- Cover-letter field values, author metadata, funding declarations, license,
  and repository/deposition choices still require author or venue decisions.
- The conceptual figures use deterministic geometry and illustrative fields;
  they are not empirical outputs.
- The Markov blanket discussion is deliberately bounded; readers wanting a full
  literature review of the controversy should treat the cited critique pair as
  scope control rather than exhaustion.
