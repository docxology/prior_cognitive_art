# Prior Cognitive Art TODO

## Current Status

The project is a conceptual manuscript with 21 generated figures, 12 argument
modules, 12 formal claims, 24 claim-ledger records, a 35-row symbol glossary,
11 text-validation checks, 14 claim dependency edges, 12 claim-grounding edges,
a conceptual-integrity token, and 81 BibTeX records. The current pass adds a deterministic
illustrative simulation trace over authored formal states while retaining the
boundary against stochastic simulations, synthetic-data experiments, empirical
effect estimates, and performance benchmarks.

The analysis pipeline generates deterministic manuscript figures under
`output/figures/`, trace artifacts under `output/data/` and `output/reports/`,
plus square cover art under `output/cover/`. Figure captions remain
source-owned in `FigureSpec.caption` inside `src/conceptual_model.py`.

## Upcoming Work

- Select a venue or preprint route, then adapt word count, reference style,
  cover-letter fields, author/funding declarations, license, and repository or
  deposition metadata.
- After venue selection, decide whether the expanded predictive-aesthetics
  scholarship should be shortened for a stricter reference or word budget.
- If the manuscript scope is deliberately expanded later, consider
  social/normative-prior sources; keep them out of the current argument boundary
  unless they change a live claim.
- Before submission, rerun the full publication gate and inspect the rendered
  PDF after any venue-specific formatting changes.

## Workflowz review — 2026-11-10

Coverage note: no concrete improvement survived the bounded packet review. The packet covered 5 project files and excerpts from 13 of 39 source candidates (plus 2 marker excerpts) out of 273 files; it did not include the full conceptual model, analysis workflow, dashboard/validation implementations, tests, lockfile, CI, or rendered artifacts. Re-review on a concrete failure or source change.
