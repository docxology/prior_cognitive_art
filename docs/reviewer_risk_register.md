# Reviewer Risk Register

Date: 2026-07-10

This register anticipates likely reviewer objections and points to the current
manuscript or project surface that answers them. It is a publication-prep tool,
not a substitute for a venue-specific response letter.

| Risk | Likely reviewer concern | Current mitigation | Evidence surface |
|---|---|---|---|
| R1 | The paper may conflate Tinbergen's explanatory questions into a single origin story. | The manuscript treats mechanism, function, ontogeny, and phylogeny as crossed explanatory axes, not a hierarchy. | `docs/manuscript/01_introduction.md`, `tinbergen_axes`, `explanatory_complementarity_matrix` |
| R2 | Hyperprior regress may be solved by another hyperprior rather than by the proposed stopping moves. | The argument distinguishes iteration from termination and names pragmatic, selection, and self-referential stops. | `docs/manuscript/02_methodology.md`, `regress_terminations`, `ontogeny_hyperprior_parallel` |
| R3 | Markov blankets may be overstated as biological membranes. | The paper now frames blankets as model-level structures and explicitly splits model use, realized coupling, and critique boundaries. | `docs/manuscript/07_scope_and_related_work.md`, `markov_blanket_scope_split`, `markov_blanket_achievement` |
| R4 | Niche construction may appear to become a fourth termination mode. | The niche discussion is bounded as a co-forming condition across developmental and cultural timescales, not a regress terminator. | `docs/manuscript/03_results.md`, `niche_construction_diagram`, `niche_prior_feedback_field` |
| R5 | Active inference may be used as an all-purpose explanatory license. | Active inference is treated as a bridge for action-perception closure and variational framing, with no empirical or simulation claims. | `active_inference_cycle`, `variational_free_energy_landscape`, `docs/publication_readiness_report.md` |
| R6 | The figures may look like results even though the paper is conceptual. | The project and manuscript state that figures are deterministic conceptual diagrams, not empirical outputs. | `README.md`, `docs/submission_package.md`, `output/figures/figure_registry.json` |
| R7 | The bibliography may be padded or only loosely connected to claims. | Accepted/deferred scholarship decisions are tied to claim boundaries and ledger records. | `docs/scholarship-audit.md`, `data/claim_ledger.yaml`, `source_claim_boundary_map` |
| R8 | The paper may hide unresolved draft work behind generated artifacts. | Tests and scans cover draft-gap phrases, unresolved tokens, citation closure, figure parity, module-size slop, and package-level artifact consistency. | `tests/`, `scripts/validate_publication_package.py`, `docs/publication_readiness_report.md`, `.omo/ulw-loop/prior-cognitive-art-publication-readiness-20260707-051719/evidence/final-quality-gate-reassess.md` |
| R9 | The variational-free-energy claim may imply literal zero free energy or confuse priors with posteriors. | F10 and the VFE caption now state a relative variational-bound/KL reading and explicitly reject literal zero-energy and prior-origin claims. | `src/conceptual_model.py`, `docs/manuscript/02_methodology.md`, `variational_free_energy_landscape` |
| R10 | The title may appear to claim a general predictive-processing theory of art. | The paper now treats "art" as a bounded analogy: aesthetic practices arrange encounters with expectation, ambiguity, affect, and meaning, while 4E and neuroaesthetic critiques block reductionism. | `docs/manuscript/01_introduction.md`, `docs/manuscript/07_scope_and_related_work.md`, `docs/scholarship-audit.md` |
| R11 | The added material-engagement scholarship may be read as saying artworks literally contain predictive models or directly install priors. | The new art/prior-craft figure and claim-ledger rows frame artworks as material scaffolds for encounters with priors, not as neural mechanisms or empirical updating claims. | `aesthetic_prior_craft_map`, `data/claim_ledger.yaml`, `docs/manuscript/02_methodology.md` |
| R12 | The deterministic simulation trace may be mistaken for a stochastic model, empirical pilot, or performance claim. | The trace is formalized as a finite authored state order, and the publication validator compares the generated JSON against source coordinates, labels, transitions, invariants, schema, path, and manifest metadata. | `docs/manuscript/08_formal_supplement.md`, `deterministic_simulation_trace`, `scripts/validate_publication_package.py`, `output/data/deterministic_simulation_trace.json` |
| R13 | First-prior scholarship may be read as claiming a literal hidden meta-prior before all priors. | The upstream section and figure frame first-prior sources as a constraint stack of viability, regulation, co-homeostasis, development, and niche support, not as an empirical discovery of a prior-before-priors. | `docs/manuscript/02_methodology.md`, `docs/manuscript/07_scope_and_related_work.md`, `first_prior_grounding_stack`, `data/claim_ledger.yaml` |
| R14 | A compact render may make captions, labels, or accessibility metadata drift from the source inventory. | `FigureSpec` owns caption, alt text, and section; hydration, registry, dashboard, and the validator compare all three fields, while representative PDF and browser views are required. | `src/conceptual_model.py`, `output/figures/figure_registry.json`, `scripts/validate_publication_package.py`, `output/reports/render_manifest.json` |
| R15 | A stale PDF or HTML could be mistaken for the current manuscript. | The canonical build stamps a hydrated-source digest and hashes combined Markdown, HTML, PDF, and slide outputs; validation fails on any mismatch. | `scripts/build_publication_package.py`, `src/render_manifest.py`, `docs/rendering_pipeline.md` |

## Pre-Submission Reviewer Strategy

- Lead with the bounded claim: the paper explains explanatory stopping
  practices for priors, not the metaphysical origin of all prior structure.
- Use `markov_blanket_scope_split` early when presenting to active-inference
  audiences; it prevents a predictable overclaim objection.
- Use `source_claim_boundary_map` when presenting to interdisciplinary
  audiences; it shows that scholarship was selected for claim control rather
  than for bibliography volume.
- Use the predictive-aesthetics paragraph as a title clarification, not as a
  mechanism claim about all art.
- Pair that paragraph with `aesthetic_prior_craft_map` when presenting to
  philosophy-of-art or 4E audiences; it shows the material-practice support and
  the mechanism ceiling on the same page.
- Use `first_prior_grounding_stack` when audiences ask "what came before the
  first prior"; it answers with upstream constraints rather than another
  hidden prior.
- Keep the deterministic-trace boundary explicit in abstracts, talks, and
  submission forms. The project is reproducible because its conceptual
  inventory, formal trace, and deterministic figures are reproducible, not
  because it estimates effects.
