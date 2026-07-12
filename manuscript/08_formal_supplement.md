# Formal Supplement: Minimal Notation for Regress, Closure, and Validation {#sec:formal-supplement}

The formal layer is deliberately small. It does not claim an empirical model,
and its deterministic illustrative simulation trace does not introduce
simulation results. Its purpose is to keep the argument modular enough that
each symbolic move can be checked against the plain-language thesis developed
in [@sec:method].

The source layer currently generates {{FORMAL_CLAIM_COUNT}} formal claims,
{{SYMBOL_COUNT}} glossary rows, {{TEXT_VALIDATION_COUNT}} text-validation
checks, {{CLAIM_DEPENDENCY_COUNT}} claim dependency edges, and
{{CLAIM_GROUNDING_COUNT}} source-grounding edges. The inventory
token for this version is `{{CONCEPTUAL_INTEGRITY_TOKEN}}`. This section owns
{{FORMAL_SUPPLEMENT_FIGURE_COUNT}} contract diagrams from the 21-figure set;
the other {{VISUAL_ATLAS_FIGURE_COUNT}} figures belong to the argument atlas.

## Deterministic Trace Contract

The deterministic trace is a finite ordered object, not a transition kernel.
Let $T=(\sigma_0,\ldots,\sigma_4)$, with
$\delta(\sigma_i)=\sigma_{i+1}$ only for adjacent authored states. The
operator $\delta$ records order; it does not introduce
$p(\sigma_{i+1}\mid\sigma_i)$, an observation model, a reward function, a
sample path, or a cognitive update rule.

The trace therefore has three commitments. First, it must terminate in a named
settlement state rather than adding another hidden prior. Second, each state
must carry a local invariant that blocks numerical, empirical, synthetic-data,
or performance readings. Third, the generated JSON trace must match the
source-owned sequence in `src/conceptual_model.py`; a mismatch is treated as a
publication-package validation failure, not as a harmless visualization drift.

## Numbered Formal Claims

{{FORMAL_CLAIMS}}

## Claim Grounding Map

The formal claims are not independent. Each edge records argumentative support
or provenance, not a theorem-level entailment; in particular, a fixed-point
description does not by itself entail a biological Markov blanket.
{{CLAIM_DEPENDENCIES}}

The grounding edges are a separate provenance surface: they identify which
named source record anchors each numbered claim.

{{CLAIM_GROUNDING}}

[@fig:formal_claim_dependency_map] shows how the numbered claims are grounded
in the same conceptual records that feed the prose, figure registry, and tests.

![{{FIGURE_ALT_FORMAL_CLAIM_DEPENDENCY_MAP}}](../output/figures/formal_claim_dependency_map.png){#fig:formal_claim_dependency_map}

## Symbol Glossary

All named symbols used by the formal claims appear in [@tbl:symbol_glossary].
Operators such as equality, set product, and implication are ordinary logical
notation rather than project-specific symbols.

| Symbol | Name | Role | Used in claims |
|---|---|---|---|
{{SYMBOL_GLOSSARY_ROWS}}

: Glossary for all named symbols used in the formal supplement. {#tbl:symbol_glossary}

[@fig:symbol_glossary_closure] visualizes the closure check. A missing symbol
row or an unused glossary row is treated as a source-contract error.

![{{FIGURE_ALT_SYMBOL_GLOSSARY_CLOSURE}}](../output/figures/symbol_glossary_closure.png){#fig:symbol_glossary_closure}

## Text-Integrity Checks

The manuscript treats prose as an artifact surface. Generated tokens do not make
the argument true, but they make several kinds of drift observable before the
paper is rendered. [@tbl:text_validation_checks] lists the checks that
guard the project contract.

| Check | Surface | Invariant | Evidence |
|---|---|---|---|
{{TEXT_VALIDATION_TABLE_ROWS}}

: Modular text-validation checks for the conceptual manuscript. {#tbl:text_validation_checks}

[@fig:text_validation_ladder] shows the validation posture: authored source
records hydrate the manuscript, figures, reports, and registry, and those
surfaces are checked again at render time.

![{{FIGURE_ALT_TEXT_VALIDATION_LADDER}}](../output/figures/text_validation_ladder.png){#fig:text_validation_ladder}
