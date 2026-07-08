# Formal Supplement {#sec:formal-supplement}

The formal layer is deliberately small. It does not claim an empirical model,
and it does not introduce simulation results. Its purpose is to keep the
argument modular enough that each symbolic move can be checked against the
plain-language thesis developed in [@sec:method].

The source layer currently generates {{FORMAL_CLAIM_COUNT}} formal claims,
{{SYMBOL_COUNT}} glossary rows, {{TEXT_VALIDATION_COUNT}} text-validation
checks, and {{CLAIM_DEPENDENCY_COUNT}} claim dependency edges. The inventory
token for this version is `{{CONCEPTUAL_INTEGRITY_TOKEN}}`.

## Numbered Formal Claims

{{FORMAL_CLAIMS}}

## Claim Dependency Graph

The formal claims are not independent. Each claim builds on earlier ones.
{{CLAIM_DEPENDENCIES}}

[@fig:formal_claim_dependency_map] shows how the numbered claims are generated
from the same conceptual records that feed the prose, figure registry, and
tests.

![A dependency map connecting Tinbergen axes, regress shape, termination moves, and joint structure to the auto-numbered formal claims F1-F11.](../output/figures/formal_claim_dependency_map.png){#fig:formal_claim_dependency_map}

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

![Two overlapping closure sets show that every symbol used by the formal claims is defined by a glossary row, with a validation bar underneath.](../output/figures/symbol_glossary_closure.png){#fig:symbol_glossary_closure}

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

![A layered validation ladder runs from source records through analysis artifacts, injected tokens, rendered manuscript outputs, and validation gates.](../output/figures/text_validation_ladder.png){#fig:text_validation_ladder}
