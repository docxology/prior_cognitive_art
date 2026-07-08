# Reviewer Risk Register

Date: 2026-07-07

This register anticipates likely reviewer objections and points to the current
manuscript or project surface that answers them. It is a publication-prep tool,
not a substitute for a venue-specific response letter.

| Risk | Likely reviewer concern | Current mitigation | Evidence surface |
|---|---|---|---|
| R1 | The paper may conflate Tinbergen's explanatory questions into a single origin story. | The manuscript treats mechanism, function, ontogeny, and phylogeny as crossed explanatory axes, not a hierarchy. | `manuscript/01_introduction.md`, `tinbergen_axes`, `explanatory_complementarity_matrix` |
| R2 | Hyperprior regress may be solved by another hyperprior rather than by the proposed stopping moves. | The argument distinguishes iteration from termination and names pragmatic, selection, and self-referential stops. | `manuscript/02_methodology.md`, `regress_terminations`, `ontogeny_hyperprior_parallel` |
| R3 | Markov blankets may be overstated as biological membranes. | The paper now frames blankets as model-level structures and explicitly splits model use, realized coupling, and critique boundaries. | `manuscript/07_scope_and_related_work.md`, `markov_blanket_scope_split`, `markov_blanket_achievement` |
| R4 | Niche construction may appear to become a fourth termination mode. | The niche discussion is bounded as a co-forming condition across developmental and cultural timescales, not a regress terminator. | `manuscript/03_results.md`, `niche_construction_diagram`, `niche_prior_feedback_field` |
| R5 | Active inference may be used as an all-purpose explanatory license. | Active inference is treated as a bridge for action-perception closure and variational framing, with no empirical or simulation claims. | `active_inference_cycle`, `variational_free_energy_landscape`, `docs/publication_readiness_report.md` |
| R6 | The figures may look like results even though the paper is conceptual. | The project and manuscript state that figures are deterministic conceptual diagrams, not empirical outputs. | `README.md`, `docs/submission_package.md`, `output/figures/figure_registry.json` |
| R7 | The bibliography may be padded or only loosely connected to claims. | Accepted/deferred scholarship decisions are tied to claim boundaries and ledger records. | `docs/scholarship-audit.md`, `data/claim_ledger.yaml`, `source_claim_boundary_map` |
| R8 | The paper may hide unresolved draft work behind generated artifacts. | Tests and scans cover draft-gap phrases, unresolved tokens, citation closure, figure parity, module-size slop, and package-level artifact consistency. | `tests/`, `scripts/validate_publication_package.py`, `docs/publication_readiness_report.md`, `.omo/ulw-loop/prior-cognitive-art-publication-readiness-20260707-051719/evidence/final-quality-gate-reassess.md` |

## Pre-Submission Reviewer Strategy

- Lead with the bounded claim: the paper explains explanatory stopping
  practices for priors, not the metaphysical origin of all prior structure.
- Use `markov_blanket_scope_split` early when presenting to active-inference
  audiences; it prevents a predictable overclaim objection.
- Use `source_claim_boundary_map` when presenting to interdisciplinary
  audiences; it shows that scholarship was selected for claim control rather
  than for bibliography volume.
- Keep the no-simulation boundary explicit in abstracts, talks, and submission
  forms. The project is reproducible because its conceptual inventory and
  deterministic figures are reproducible, not because it estimates effects.
