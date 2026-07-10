# Documentation Audit Report — Prior Cognitive Art

**Date:** 2026-07-09
**Scope:** `/Users/4d/Documents/GitHub/template/projects/working/prior_cognitive_art`
**Method:** `documentation-audit` skill (broken-link scan, bibliography closure,
executable API-claim validation, generated-artifact count check, caption-system
source-of-truth review, publication-readiness refresh).

## Pre-audit state (carried over from the line-by-line review)

The following were already fixed before this audit pass:

- Figure captions unified to a single source of truth (`FigureSpec.caption` in
  `src/conceptual_model.py`); figure registry, API docs, dashboard, and
  manuscript manifest all consume it.
- Stale documentation counts corrected and refreshed again after the
  art/prior-craft and deterministic-trace expansions: `src/documentation.py`,
  `docs/architecture.md`, `src/README.md`, and `manuscript/README.md` now
  match the 20-figure and 70-entry bibliography contracts.
- "Art" framing (previously undefined title term) defined in abstract + intro.
- Figure layout defects fixed: `markov_blanket_achievement` label overflow,
  `ontogeny_hyperprior_parallel` "same regress shape" overflow,
  `formal_claim_dependency_map` edges now distributed across both claim columns.

## Audit results (this pass)

| Check | Result |
|-------|--------|
| Broken internal Markdown links | **0** across all `*.md` |
| Bibliography bidirectional closure | **Closed**: 70 entries, 70 cited, 0 orphan, 0 phantom |
| Generated-artifact count vs docs | **20 PNGs** = 20 claimed (README, architecture.md, src/README) - no drift |
| Mermaid blocks / alt-text | **0 mermaid blocks** (none used) |
| Executable API-claim validation (Phase 12.5) | **ALL PASS**: every documented symbol in `src/documentation.py` / `docs/architecture.md` imports and behaves as documented (counts 4/3/11/20/12/28/10/14; token len 16; `FigureSpec.caption` present; `generate_all_figures` -> 20 real PNGs; report/vars/api-doc counts consistent) |
| `src/__init__.py` re-exports vs `__all__` | Not separately asserted; `from src import …` used throughout tests imports cleanly |

## Documentation improvements added this pass

- `docs/architecture.md` — new **"Figure captions"** section documenting the
  single source of truth (`FigureSpec.caption`) and the regenerate command set,
  so captions cannot silently re-diverge.
- `docs/agent_instructions.md` - added a **"Figure captions"** note to the
  editing workflow enforcing the same contract.
- `docs/scholarship-audit.md` - accepted/deferred source decisions for the
  publication-readiness pass.
- `docs/publication_readiness_report.md` - final readiness gate, evidence, and
  visual QA notes for the current pass.
- `docs/submission_package.md` - venue-neutral abstract, keywords,
  contribution statements, reproducibility notes, figure guidance, and
  remaining venue-specific fields.
- `docs/reviewer_risk_register.md` - likely reviewer concerns mapped to
  manuscript sections, figures, source ledgers, and final gate evidence.
- `docs/cover_letter_template.md` - venue-adaptable cover letter language with
  explicit author/venue fields.
- `docs/venue_selection_matrix.md` - scoring aid for candidate journals,
  preprint routes, and scope-fit risk.
- `docs/preprint_release_checklist.md` - release QA checklist for PDF,
  reproducibility, visual inspection, metadata, and archive notes.
- `output/cover/prior_cognitive_art_cover_square.png` plus
  `output/reports/cover_art_manifest.json` - square-format deterministic cover
  art for the PDF title page, preprint cards, and dashboard presentation,
  outside the manuscript figure set.
- `output/data/deterministic_simulation_trace.json` plus
  `output/reports/deterministic_simulation_manifest.json` - deterministic
  formal-state trace artifacts, validated against the source-owned sequence.

## Verification

- `uv run pytest tests/` -> **77 passed**.
- Full PDF render via `scripts/03_render_pdf.py --project working/prior_cognitive_art`
  -> valid `prior_cognitive_art_combined.pdf` (3.3 MB, 20 manuscript figures
  plus title-page cover art, no LaTeX errors).
- `qpdf --check output/pdf/prior_cognitive_art_combined.pdf` -> no syntax or
  stream-encoding errors.
- Final source/rendered/PDF text scans -> no broad draft markers, unresolved
  template tokens, or task-marker residue.

## Remaining / out-of-scope (honest disclosure)

- Per-image `width=` attributes are dropped by pandoc-crossref in this
  environment; figures render at the pipeline default full width. Sizing is not
  attribute-controllable here without infrastructure changes — left as-is.
- Venue-specific formatting remains out of scope for this project-level pass.
- Journal submission metadata, final cover-letter field values, author/funding
  declarations, and repository deposition records are deferred until a target
  venue is selected; venue-neutral scaffolding is now in
  `docs/submission_package.md`, `docs/cover_letter_template.md`,
  `docs/venue_selection_matrix.md`, and `docs/preprint_release_checklist.md`.

**Status: publication-ready as a venue-neutral working paper.** No known
source/manuscript/doc count drift remains.
