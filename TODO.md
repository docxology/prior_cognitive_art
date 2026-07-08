# Prior Cognitive Art TODO

## Current Status
The project is a simulation-free conceptual manuscript with 18 generated figures,
11 formal claims, 20 claim-ledger records, a 25-row symbol glossary, 10
text-validation checks, 12 claim dependency edges, a conceptual-integrity token,
and 76 tests at 100% coverage target. The analysis pipeline, manuscript
hydration, dashboard, API docs, and template render are the publication-readiness
gate for this pass.

The analysis pipeline also generates deterministic square cover art under
`output/cover/`, with metadata in `output/reports/cover_art_manifest.json`.
This asset supports preprint cards and dashboard presentation without changing
the 18-figure manuscript contract.

Figure captions are now a single source of truth: `FigureSpec.caption` in
`src/conceptual_model.py` flows into the figure registry, the API reference, the
dashboard, and the manuscript's figure manifest. Inline figure alt-text in the
manuscript is aligned to the same wording. (Note: per-image `width=` attributes
are dropped by pandoc-crossref in this environment, so figures render at the
pipeline default full width; sizing is not attribute-controlled here.)

## Open Work
- No known publication-blocking manuscript gaps remain after the current pass.
- Venue-neutral submission scaffolding now exists in
  `docs/submission_package.md`, and likely reviewer objections are mapped in
  `docs/reviewer_risk_register.md`.
- `scripts/validate_publication_package.py` now rechecks the venue-neutral
  package from source-owned counts, generated reports, rendered surfaces, and
  required metadata artifacts.
- Submission execution scaffolding now exists in
  `docs/cover_letter_template.md`, `docs/venue_selection_matrix.md`, and
  `docs/preprint_release_checklist.md`.
- Residual venue-specific work is intentionally deferred until venue selection:
  journal style, repository deposition metadata, final cover letter values,
  author/funding declarations, and submission-system formatting.
- If the scope is deliberately expanded later, social/normative-prior sources
  can be considered, but they are not needed for the current argument boundary.

## Resolved
- The "art" framing (title term) is now defined in the abstract and introduction:
  the craft of keeping explanatory kinds distinct and rendering that distinction
  as deterministic figures and checkable claims, rather than as a metaphysical
  theory of priors.
- Figure caption drift (three diverging sources) is resolved by unifying on
  `FigureSpec.caption`.
- Variational closure claim (F10) now explicitly connects to the evidence
  lower bound (ELBO): the variational free energy is the upper bound on negative
  log evidence, and the minimum is reached exactly when the variational posterior
  equals the true posterior (the zero-free-energy limit).
- Deepened the scale-invariance section (02_methodology.md) with three concrete,
  cited instances — cellular (autopoiesis of the cell's Markov blanket),
  organismic (nervous-system prior-like constraints), and social (cultural
  practices as population steady states) — and made the $X^*_k = \Phi(X^*_k)$
  recurrence and $R$ operator explicit, matching the scale_invariance_diagram
  figure and its caption.
- Bibliography scholarship pass: corrected publication years and entry types for
  Hohwy (Predictive Mind 2016; PsyArXiv 2017), Clark (Surfing Uncertainty 2015),
  Bateson (Steps to an Ecology of Mind 1972), Parr et al. (book 2022), Seth (book
  2021), da Costa et al. (Bayesian Mechanics 2023), Ramstead et al. (Phys. Life
  Rev. 2023, with volume/pages/DOI), and Hipólito et al. (Cog. Sys. Res. 2021).
- Publication-readiness scholarship pass promoted only claim-relevant verified
  sources into the manuscript and bibliography; accepted/deferred decisions are
  recorded in `docs/scholarship-audit.md`.
- Markov blankets are now framed as model-level structures whose realized
  boundary readings require explicit assumptions, not as automatic metaphysical
  membranes.
- Niche construction now constrains prior formation across developmental and
  extended-active-inference timescales without becoming a fourth termination
  mode.
- Hyperprior stopping now cites pragmatic weakly informative, reference, and
  penalized-complexity prior practice as a methodological stop rather than a
  proof of regress termination.
- Added three deterministic conceptual figures:
  `source_claim_boundary_map`, `markov_blanket_scope_split`, and
  `niche_prior_feedback_field`.
- Added deterministic 2048 x 2048 square cover art for publication-facing
  visual presentation, kept outside the manuscript figure count.
- Publication readiness is tracked in `docs/publication_readiness_report.md`.
