# Venue-Neutral Submission Package

Date: 2026-07-07

This package is a reusable pre-submission layer for `Prior Cognitive Art`. It is
not a journal-specific checklist; venue house style, word limits, author forms,
and repository deposition choices remain downstream decisions.

## Manuscript Identity

- Title: Prior Cognitive Art
- Subtitle: Tinbergen Axes, Hyperprior Regress, and Fixed-Point Explanation
- Manuscript type: conceptual working paper / preprint
- Scope boundary: one deterministic illustrative formal-state trace; no
  stochastic simulations, empirical performance results, synthetic-data
  experiments, or benchmark claims
- Current readiness decision: ready for venue-neutral preprint / working-paper
  circulation

## Abstract

A prior is not explained by adding earlier and earlier priors. This manuscript
separates four explanatory questions about priors, compares ontogenetic regress
with the Bayesian hyperprior problem, and argues that the regress stops only
when an explanatory practice replaces another hidden prior with a termination
rule: pragmatic weak-prior closure, selection filtering, or self-referential
fixed-point organization. The paper treats Markov blankets as useful
model-level boundary structures whose realized-boundary readings require
explicit assumptions, and treats niche construction as a co-forming condition on
prior formation rather than as an extra regress terminator. The contribution is
a bounded conceptual framework with deterministic figures, a deterministic
illustrative formal-state trace, formal claim records, source-linked validation
surfaces, and a limited predictive-aesthetics account of art as staged
encounters with expectation, ambiguity, affect, and meaning.

## Keywords

- priors
- Tinbergen questions
- hyperprior regress
- active inference
- Markov blankets
- niche construction
- fixed points
- conceptual methodology

## Contribution Statement

1. The paper reframes "why a prior exists" as a separation problem across
   Tinbergen-style explanatory questions rather than as a single causal origin
   question.
2. It distinguishes three regress-stopping moves: pragmatic weak-prior closure,
   selection filtering, and self-referential fixed-point organization.
3. It provides a bounded Markov blanket treatment that separates Pearl/Friston
   model use, biological realization, and critique-sensitive metaphysical
   overreach.
4. It bounds the title's "art" claim with predictive-processing aesthetics,
   neuroaesthetic scope, 4E affordance accounts, and Bayesian-overclaim
   cautions.
5. It adds a reproducible conceptual inventory: 20 deterministic figures, 12
   formal claims, 23 claim-ledger records, 28 glossary rows, 10 text validation
   checks, and one deterministic trace artifact.

## Evidence And Reproducibility

- Source-of-truth argument inventory: `src/conceptual_model.py`
- Claim ledger: `data/claim_ledger.yaml`
- Scholarship decisions: `docs/scholarship-audit.md`
- Readiness report: `docs/publication_readiness_report.md`
- Rendered manuscript: `output/pdf/prior_cognitive_art_combined.pdf`
- Figure registry: `output/figures/figure_registry.json`
- Deterministic trace: `output/data/deterministic_simulation_trace.json`
- Deterministic trace manifest: `output/reports/deterministic_simulation_manifest.json`
- Final ULW gate: `.omo/ulw-loop/prior-cognitive-art-publication-readiness-20260707-051719/evidence/final-quality-gate-reassess.md`

Reproduction commands:

```bash
uv run pytest tests/
uv run python scripts/optimization_analysis.py
uv run python scripts/build_dashboard.py
uv run python scripts/generate_api_docs.py
uv run python scripts/z_generate_manuscript_variables.py
uv run python scripts/validate_publication_package.py
```

From `/Users/4d/Documents/GitHub/template`:

```bash
uv run python -m infrastructure.orchestration link-projects --dry-run
uv run python scripts/03_render_pdf.py --project working/prior_cognitive_art
```

## Figure Set

The manuscript has 19 deterministic conceptual figures. The strongest
submission figures for a short preprint pitch are:

- `tinbergen_axes`: establishes the explanatory separation.
- `regress_terminations`: states the three stopping moves.
- `policy_entanglement_bridge`: prevents overreading decomposition as origin.
- `markov_blanket_scope_split`: bounds model-level and realized-boundary claims.
- `niche_prior_feedback_field`: shows organism, resources, and culture across
  timescales.
- `source_claim_boundary_map`: connects scholarship decisions to manuscript
  claims.

The project also includes square-format cover art at
`output/cover/prior_cognitive_art_cover_square.png`. It is intended for the
PDF title page, preprint cards, dashboard presentation, and venue-neutral
promotion; it is not counted as a manuscript figure.

## Data, Code, And Materials Statement

The project contains no empirical dataset and no simulation results. Code is
used to maintain the conceptual inventory, render deterministic figures,
hydrate manuscript variables, and validate source/manuscript consistency.

## Ethics And Competing Interests

No human-subject, animal-subject, clinical, or field data are used. Author,
funding, competing-interest, and acknowledgement declarations should be set by
the author when a target venue is selected.

## Venue-Specific Items Still Needed

- Target venue or preprint server
- Required word-count and reference style
- Author metadata and affiliations
- Funding and competing-interest declarations
- Repository or archive deposition choice
- Cover letter or submission-system summary
