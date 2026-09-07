# Gate Review - Prior Cognitive Art Publication Readiness After Split

## recommendation

APPROVE

## blockers

None.

## originalIntent

Finish the Prior Cognitive Art publication-readiness plan end to end: add only
claim-relevant verified scholarship, remove draft/future-work/template residue,
add three deterministic conceptual figures while preserving an exact 18-figure
contract, update claim ledger/docs/TODO/readiness reporting, regenerate outputs,
render the PDF through the template pipeline, perform visual QA, and finish with
reviewer approval under the conceptual/no-simulation scope.

## desiredOutcome

The user-visible outcome should be a venue-neutral publication-ready manuscript
package whose source records, generated artifacts, docs, tests, rendered PDF,
manual QA evidence, and review artifacts all agree that no publication-blocking
work remains. Venue-specific submission formatting may remain explicitly
deferred.

## userOutcomeReview

Approved. The after-split artifacts now satisfy the requested outcome.

- The goal status remains `pending` in `goals.json`, but the user explicitly
  instructed not to block solely on that state. All three success criteria in
  `goals.json` are marked `pass` with after-split captured evidence.
- The authoritative evidence files exist and support the criteria:
  `C001-happy-path.log`, `C002-surface-scan.log`, and
  `C003-visual-regression.md`.
- `pytest-after-split.log` reports 73 passed. The render log reports 18/18
  figure references found and generated
  `output/pdf/prior_cognitive_art_combined.pdf` at 1.98 MB. A direct
  `qpdf --check output/pdf/prior_cognitive_art_combined.pdf` run also reported
  no syntax or stream-encoding errors.
- Direct live counts found 18 `figure_specs()`, 18 PNGs, 18 SVGs, 18 manifest
  entries, and 18 registry keys. `generate_all_figures()` still compares
  produced filenames against `figure_specs()`, so the contract is exact rather
  than count-only.
- Direct live LOC measurement found every `src/figures/*.py` file under the
  250 pure-LOC ceiling: `conceptual.py` 81, `_argument_figures.py` 221,
  `_contract_figures.py` 204, `_boundary_figures.py` 204,
  `_niche_blanket_figures.py` 168, `_active_scale_figures.py` 157,
  `_shared.py` 74, and `__init__.py` 2. No `SIZE_OK` exception is present.
- Direct source/render scans found zero draft/future-work/TODO/FIXME/TBD
  residue across 27 docs/manuscript/publication surfaces, and zero unresolved
  `{{`/`}}` template tokens across 13 rendered manuscript, combined PDF
  markdown, and combined web markdown surfaces. `pdftotext` plus `rg` found no
  draft, unresolved token, TODO, or empirical-performance residue in the PDF.
- `docs/scholarship-audit.md` records accepted and rejected/deferred sources
  and ties accepted sources to claim boundaries. `data/claim_ledger.yaml`
  contains the Markov-blanket scope, developmental-niche boundary,
  pragmatic-prior stop, and Tinbergen/Konner extension rows.
- `TODO.md` and `docs/publication_readiness_report.md` accurately state
  venue-neutral readiness while deferring venue-specific formatting and
  repository/submission metadata.
- Visual QA contact sheets were inspected directly. The 18 figure contact sheet
  and sampled PDF pages are nonblank, readable, and framed; the three new
  figures appear in the visual atlas/PDF sample without obvious clipping.
- Direct `remove-ai-slops`/`programming` pass found the prior oversized figure
  module blocker resolved. The new pure-LOC ceiling test is not tautological: it
  scans every `src/figures/*.py` file and fails on the architectural regression
  class. The broadened residue tests cover source and rendered publication
  surfaces rather than merely checking a deleted phrase.

Residual non-blocking notes: `tests/test_project_internals.py` is a large
existing test-aggregation file, and `_shared._box`/`_shared._arrow` are
parameter-heavy Matplotlib primitives. They do not contradict the requested
after-split figure-module ceiling, exact figure contract, publication-readiness
scope, or user-visible manuscript outcome.

## checked artifact paths

- `.omo/ulw-loop/prior-cognitive-art-publication-readiness-20260707-051719/brief.md`
- `.omo/ulw-loop/prior-cognitive-art-publication-readiness-20260707-051719/goals.json`
- `.omo/ulw-loop/prior-cognitive-art-publication-readiness-20260707-051719/ledger.jsonl`
- `.omo/ulw-loop/prior-cognitive-art-publication-readiness-20260707-051719/evidence/C001-happy-path.log`
- `.omo/ulw-loop/prior-cognitive-art-publication-readiness-20260707-051719/evidence/C002-surface-scan.log`
- `.omo/ulw-loop/prior-cognitive-art-publication-readiness-20260707-051719/evidence/C003-visual-regression.md`
- `.omo/ulw-loop/prior-cognitive-art-publication-readiness-20260707-051719/evidence/code-review-slop-report-after-split.md`
- `.omo/ulw-loop/prior-cognitive-art-publication-readiness-20260707-051719/evidence/figure-module-size-after-split.log`
- `.omo/ulw-loop/prior-cognitive-art-publication-readiness-20260707-051719/evidence/pytest-after-split.log`
- `.omo/ulw-loop/prior-cognitive-art-publication-readiness-20260707-051719/evidence/render-pdf-after-split.log`
- `.omo/ulw-loop/prior-cognitive-art-publication-readiness-20260707-051719/evidence/qpdf-check-after-split.log`
- `.omo/ulw-loop/prior-cognitive-art-publication-readiness-20260707-051719/evidence/broad-draft-marker-scan-after-split.log`
- `.omo/ulw-loop/prior-cognitive-art-publication-readiness-20260707-051719/evidence/output-token-scan-after-split.log`
- `.omo/ulw-loop/prior-cognitive-art-publication-readiness-20260707-051719/evidence/pdf-text-scan-after-split.log`
- `.omo/ulw-loop/prior-cognitive-art-publication-readiness-20260707-051719/evidence/final-contract-closure-after-split.log`
- `.omo/ulw-loop/prior-cognitive-art-publication-readiness-20260707-051719/evidence/figure-contact-sheet-after-split.png`
- `.omo/ulw-loop/prior-cognitive-art-publication-readiness-20260707-051719/evidence/pdf-page-contact-sheet-after-split.png`
- `src/figures/conceptual.py`
- `src/figures/_argument_figures.py`
- `src/figures/_contract_figures.py`
- `src/figures/_boundary_figures.py`
- `src/figures/_niche_blanket_figures.py`
- `src/figures/_active_scale_figures.py`
- `src/figures/_shared.py`
- `tests/test_project_internals.py`
- `tests/test_analysis_workflow.py`
- `src/conceptual_model.py`
- `data/claim_ledger.yaml`
- `docs/scholarship-audit.md`
- `docs/publication_readiness_report.md`
- `TODO.md`
- `README.md`
- `output/reports/figure_manifest.json`
- `output/figures/figure_registry.json`
- `output/figures/`
- `output/pdf/prior_cognitive_art_combined.pdf`
- `output/pdf/_combined_manuscript.md`
- `output/web/_combined_manuscript.md`
- `output/manuscript/`

## exactEvidenceGaps

None blocking.

Non-blocking context: the parent repository reports
`working/prior_cognitive_art` as untracked (`?? ./`), so there is no reliable
tracked git diff for this project to use as the authoritative changed-file set.
The review therefore used the user-provided evidence list plus direct live file
and artifact inspection.
