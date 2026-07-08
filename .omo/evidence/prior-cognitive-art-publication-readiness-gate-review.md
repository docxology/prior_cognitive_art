# Gate Review - Prior Cognitive Art Publication Readiness

## recommendation

REJECT

## originalIntent

The requested work was to finish the Prior Cognitive Art publication-readiness
plan end to end: promote only directly useful verified scholarship, remove
draft-gap/future-work/template-token residue from publication surfaces, add
three deterministic conceptual figures while preserving an exact 18-figure
contract, update claim ledger/docs/TODO/readiness reporting, regenerate outputs,
render the PDF through the template pipeline, capture current evidence, perform
visual QA, and finish with reviewer approval.

## desiredOutcome

The user-visible outcome should be a venue-neutral publication-ready manuscript
package whose source records, docs, generated artifacts, tests, rendered PDF,
visual QA, and loop evidence all agree that no publication-blocking work remains.

## userOutcomeReview

The manuscript package is substantially advanced: direct checks confirmed 18
figure specs, 18 draw calls, 18 PNGs, 18 SVGs, 18 manifest entries, current
generated outputs after source edits, 20 claim-ledger records, accepted/deferred
scholarship decisions, rendered-output token scans, and a valid sampled PDF.
However, the shipped artifact does not satisfy the requested final closure
because the durable loop still records the goal as pending, expected evidence
paths in the goal are missing, no reviewer/code-review/slop-coverage report is
present, and the direct remove-ai-slops/programming pass found unresolved
production/test slop.

## blockers

1. Durable loop status contradicts completion.
   Evidence: `.omo/ulw-loop/prior-cognitive-art-publication-readiness-20260707-051719/goals.json`
   still has `goals[0].status = "pending"` for
   `G001-implement-the-prior-cognitive-art-pu`, even though criteria rows are
   marked pass. A final gate cannot approve a plan whose own durable goal state
   remains pending.

2. Goal-declared evidence artifacts are missing.
   Evidence from direct path check:
   `C001` expects `.omo/ulw-loop/prior-cognitive-art-publication-readiness-20260707-051719/evidence/C001-happy-path.log`;
   `C002` expects `.omo/ulw-loop/prior-cognitive-art-publication-readiness-20260707-051719/evidence/C002-surface-scan.log`;
   `C003` expects `.omo/ulw-loop/prior-cognitive-art-publication-readiness-20260707-051719/evidence/C003-visual-regression.md`.
   None of these files exists. Alternate logs exist, but the authoritative
   `goals.json` expected-evidence contract was not satisfied.

3. Required reviewer/code-review/slop coverage artifact is absent.
   Evidence: `find .omo -type f | rg "review|qa|manual|gate|approval|slop|code-review"`
   found no code review report, reviewer approval report, manual QA matrix, or
   overfit/slop coverage report. The brief objective explicitly includes
   "finish with reviewer approval", and the final-gate protocol requires the
   code review report to show the same skill-perspective and overfit/slop
   criterion coverage.

4. Direct remove-ai-slops/programming pass found unresolved production slop.
   Evidence: `src/figures/conceptual.py` is 987 pure LOC, contains an appended
   `# NEW FIGURES` section, and includes many obvious drawing comments in the
   newly added figure region. Under the loaded `programming` and
   `remove-ai-slops` criteria, an oversized production module and obvious
   comments/section markers are unresolved maintenance burden. The project
   contract requires deterministic conceptual figures, but it does not require
   appending all rendering logic to a single oversized module.

5. Direct overfit/slop pass found false-confidence tests.
   Evidence: `tests/test_project_internals.py::test_manuscript_has_no_publication_draft_gap_language`
   only checks a small hard-coded phrase list for a requested deletion class,
   while the broader proof lives in external `rg` scan logs. This is a
   deletion-only/narrow residue test and does not prove the broader
   no-residue contract by itself.

## checked artifact paths

- `.omo/ulw-loop/prior-cognitive-art-publication-readiness-20260707-051719/goals.json`
- `.omo/ulw-loop/prior-cognitive-art-publication-readiness-20260707-051719/ledger.jsonl`
- `.omo/ulw-loop/prior-cognitive-art-publication-readiness-20260707-051719/evidence/pytest-final-final.log`
- `.omo/ulw-loop/prior-cognitive-art-publication-readiness-20260707-051719/evidence/render-pdf-final.log`
- `.omo/ulw-loop/prior-cognitive-art-publication-readiness-20260707-051719/evidence/qpdf-check-final.log`
- `.omo/ulw-loop/prior-cognitive-art-publication-readiness-20260707-051719/evidence/pdf-text-scan-final.log`
- `.omo/ulw-loop/prior-cognitive-art-publication-readiness-20260707-051719/evidence/output-token-scan-final.log`
- `.omo/ulw-loop/prior-cognitive-art-publication-readiness-20260707-051719/evidence/final-contract-closure.log`
- `.omo/ulw-loop/prior-cognitive-art-publication-readiness-20260707-051719/evidence/publication-surface-stale-phrase-scan-final.log`
- `.omo/ulw-loop/prior-cognitive-art-publication-readiness-20260707-051719/evidence/figure-contact-sheet.png`
- `.omo/ulw-loop/prior-cognitive-art-publication-readiness-20260707-051719/evidence/pdf-page-contact-sheet-final.png`
- `docs/scholarship-audit.md`
- `docs/publication_readiness_report.md`
- `TODO.md`
- `data/claim_ledger.yaml`
- `src/conceptual_model.py`
- `src/figures/conceptual.py`
- `tests/test_project_internals.py`
- `tests/test_analysis_workflow.py`
- `tests/test_manuscript_variables.py`
- `tests/test_scripts_smoke.py`
- `domain_profile.yaml`
- `experiment_plan.yaml`
- `README.md`
- `STANDALONE.md`
- `docs/README.md`
- `docs/architecture.md`
- `docs/output_inventory.md`
- `output/figures/figure_registry.json`
- `output/reports/figure_manifest.json`
- `output/pdf/prior_cognitive_art_combined.pdf`

## exactEvidenceGaps

- Missing `.omo/ulw-loop/prior-cognitive-art-publication-readiness-20260707-051719/evidence/C001-happy-path.log`.
- Missing `.omo/ulw-loop/prior-cognitive-art-publication-readiness-20260707-051719/evidence/C002-surface-scan.log`.
- Missing `.omo/ulw-loop/prior-cognitive-art-publication-readiness-20260707-051719/evidence/C003-visual-regression.md`.
- Missing explicit reviewer approval/code-review report.
- Missing explicit manual QA matrix beyond contact-sheet images and ledger prose.
- Missing explicit remove-ai-slops/programming overfit/slop report coverage.
