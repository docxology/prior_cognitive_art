from __future__ import annotations

import hashlib
import json
from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class Quadrant:
    key: str
    scale: str
    temporality: str
    label: str
    role: str
    regress_status: str


@dataclass(frozen=True)
class Termination:
    key: str
    name: str
    stop_type: str
    answer: str
    limitation: str


@dataclass(frozen=True)
class ArgumentModule:
    key: str
    title: str
    claim: str


@dataclass(frozen=True)
class FigureSpec:
    key: str
    filename: str
    title: str
    purpose: str
    caption: str


@dataclass(frozen=True)
class FormalClaim:
    key: str
    title: str
    expression: str
    reading: str
    symbol_keys: tuple[str, ...]


@dataclass(frozen=True)
class SymbolSpec:
    key: str
    symbol: str
    name: str
    role: str


@dataclass(frozen=True)
class TextValidationCheck:
    key: str
    surface: str
    invariant: str
    evidence: str


@dataclass(frozen=True)
class ClaimDependency:
    """Directed edge in the formal-claim dependency graph."""
    source_claim: str
    target_claim: str
    rationale: str


def quadrant_grid() -> tuple[Quadrant, ...]:
    return (
        Quadrant(
            key="mechanism",
            scale="proximate",
            temporality="static",
            label="Mechanism",
            role="What the prior is doing now inside the system.",
            regress_status="closes locally by naming present causal organization",
        ),
        Quadrant(
            key="function",
            scale="ultimate",
            temporality="static",
            label="Function",
            role="What the prior is for now in selection-structured terms.",
            regress_status="closes locally by naming viability and use",
        ),
        Quadrant(
            key="ontogeny",
            scale="proximate",
            temporality="developmental",
            label="Ontogeny",
            role="How the prior became shaped across an individual history.",
            regress_status="defers the question to the source of that history",
        ),
        Quadrant(
            key="phylogeny",
            scale="ultimate",
            temporality="developmental",
            label="Phylogeny",
            role="How the prior persisted across population histories.",
            regress_status="blocks regress through selection-filtered survival",
        ),
    )


def termination_catalog() -> tuple[Termination, ...]:
    return (
        Termination(
            key="pragmatic",
            name="Pragmatic termination",
            stop_type="formal sufficiency",
            answer="Install a flat or weak hyperprior and stop asking.",
            limitation="It is useful for calculation but thin as an explanation.",
        ),
        Termination(
            key="selection",
            name="Selection termination",
            stop_type="viability filtering",
            answer="Function and phylogeny answer why this prior persists.",
            limitation="It explains persistence, not the fine structure of a single organism.",
        ),
        Termination(
            key="fixed_point",
            name="Self-referential termination",
            stop_type="fixed-point individuation",
            answer="The prior is the settled organization of the process it constrains.",
            limitation="It must be stated as a category shift, not another hidden prior.",
        ),
    )


def argument_modules() -> tuple[ArgumentModule, ...]:
    return (
        ArgumentModule(
            key="tinbergen_axes",
            title="Tinbergen is crossed, not stacked",
            claim=(
                "Mechanism, function, ontogeny, and phylogeny form two axes: "
                "proximate versus ultimate and static versus developmental."
            ),
        ),
        ArgumentModule(
            key="ontogeny_regress",
            title="Ontogeny alone keeps deferring",
            claim=(
                "Treating development as the whole answer to why a prior exists "
                "moves the question to the developmental source of that prior."
            ),
        ),
        ArgumentModule(
            key="hyperprior_parallel",
            title="Biological inheritance mirrors hyperprior inheritance",
            claim=(
                "Prior-selects-prior in developmental language has the same shape "
                "as prior-on-prior in hierarchical Bayes."
            ),
        ),
        ArgumentModule(
            key="termination_set",
            title="Only three endings are live",
            claim=(
                "The regress stops pragmatically, by selection, or by a fixed-point "
                "shift in which the system is the prior-like settlement."
            ),
        ),
        ArgumentModule(
            key="policy_entanglement",
            title="Joint structure precedes factor cleanup",
            claim=(
                "The argument is adjacent to lambda-decomposition work because "
                "joint organization can be prior to the factors later extracted from it."
            ),
        ),
        ArgumentModule(
            key="niche_construction",
            title="Priors are co-shaped by system and niche",
            claim="The prior-like structure is not fully given by the environment nor fully endogenous; it is co-shaped by the organism and its niche.",
        ),
        ArgumentModule(
            key="blanket_achievement",
            title="Markov blankets are achieved, not given",
            claim="The statistical boundary separating internal from external states is part of what the persisting system achieves, not a boundary imposed from outside.",
        ),
        ArgumentModule(
            key="explanatory_complementarity",
            title="Tinbergen questions are complementary, not rival",
            claim="The four questions are complementary perspectives on the same phenomenon; conflating them is the source of the regress, not the framework itself.",
        ),
        ArgumentModule(
            key="active_inference_closure",
            title="Active inference closes the action-perception loop",
            claim="Active inference treats action and perception as two aspects of the same free-energy-minimizing process, which closes the explanatory loop the prior was meant to serve.",
        ),
        ArgumentModule(
            key="scale_invariance_of_priors",
            title="Prior-like structure appears at multiple scales",
            claim="The regress-termination problem recurs at the cellular, organismic, and social scales; the fixed-point move applies at each level without requiring a new hidden prior.",
        ),
    )


def figure_specs() -> tuple[FigureSpec, ...]:
    return (
        FigureSpec(
            key="tinbergen_axes",
            filename="tinbergen_axes.png",
            title="Tinbergen axes for priors",
            purpose="Show the crossed proximate/ultimate and static/developmental structure.",
            caption=(
                "Tinbergen's four questions form two crossed axes, not a stacked ladder: "
                "proximate versus ultimate (columns) and static versus developmental (rows). "
                "Mechanism and function close locally; ontogeny defers; phylogeny blocks regress "
                "through selection-filtered persistence. The regress appears only when one cell "
                "is asked to carry the load of all four."
            ),
        ),
        FigureSpec(
            key="regress_terminations",
            filename="regress_terminations.png",
            title="Where the hyperprior regress can stop",
            purpose="Compare pragmatic, selection, and fixed-point endings.",
            caption=(
                "Iterating a prior-on-prior (or a prior-selecting-prior) chain is easy; the "
                "explanatory work is in naming where it stops. Three live terminations are shown: "
                "pragmatic (install a weak hyperprior and stop), selection (filter by viability), "
                "and fixed-point (the system is the prior-like settlement, not a bearer of one more "
                "hidden prior)."
            ),
        ),
        FigureSpec(
            key="prior_equilibrium_map",
            filename="prior_equilibrium_map.png",
            title="Prior as settled organization",
            purpose="Render the fixed-point move as a self-individuating loop, not another level.",
            caption=(
                "The fixed-point reading treats the prior as the settled organization that "
                "persists under its own process, written as the self-map X* = Phi(X*). Blanket "
                "persistence, action-perception closure, and environmental viability circle back "
                "into one self-individuating loop rather than a further explanatory level."
            ),
        ),
        FigureSpec(
            key="ontogeny_hyperprior_parallel",
            filename="ontogeny_hyperprior_parallel.png",
            title="Ontogeny and hyperpriors share a regress shape",
            purpose="Compare prior-on-prior and developmental prior-selection chains.",
            caption=(
                "A prior-on-prior chain in hierarchical Bayes and a current-prior-selecting-a-"
                "developmental-source chain in ontogeny share the same regress shape: each step "
                "defers the question to the next selector. Adding another selector does not answer "
                "why selection terminates."
            ),
        ),
        FigureSpec(
            key="selection_filter",
            filename="selection_filter.png",
            title="Selection as regress blocker",
            purpose="Show function and phylogeny as viability filters rather than another hidden level.",
            caption=(
                "Function and phylogeny act as a viability filter over candidate priors: fragile, "
                "miscalibrated, and overfit forms do not remain available as the objects whose "
                "origin we ask about. Selection blocks regress by naming what persists, not by "
                "adding another hidden level."
            ),
        ),
        FigureSpec(
            key="policy_entanglement_bridge",
            filename="policy_entanglement_bridge.png",
            title="Joint structure before decomposition",
            purpose="Connect the argument to policy entanglement and lambda-decomposition.",
            caption=(
                "Lambda-decomposition extracts policy, prior-like constraint, and state factors "
                "from an already joint organization. The useful factors are analytic cuts, not "
                "proof that the factors were ontologically first; joint organization can precede "
                "the decomposition that later makes it legible."
            ),
        ),
        FigureSpec(
            key="formal_claim_dependency_map",
            filename="formal_claim_dependency_map.png",
            title="Formal claim dependency map",
            purpose="Show how the numbered formal claims depend on axes, regress, termination, and decomposition records.",
            caption=(
                "The auto-numbered formal claims (F1-F11) are generated views over the shared "
                "conceptual inventory: Tinbergen axes, the regress shape, termination moves, joint "
                "structure, niche and blanket, and explanatory complementarity. Source order fixes "
                "the numbering, so the claims cannot drift from the prose or figures they label."
            ),
        ),
        FigureSpec(
            key="symbol_glossary_closure",
            filename="symbol_glossary_closure.png",
            title="Symbol glossary closure",
            purpose="Show the integrity check that every formal symbol used in the supplement is glossaryed.",
            caption=(
                "Every symbol key used by a formal claim must appear exactly once as a glossary "
                "row. Used-symbol and glossary sets are equal; a missing or orphan glossary row is "
                "a source-contract error caught before render."
            ),
        ),
        FigureSpec(
            key="text_validation_ladder",
            filename="text_validation_ladder.png",
            title="Text validation ladder",
            purpose="Show source records, injected tokens, generated artifacts, and rendered paper as linked validation layers.",
            caption=(
                "Authored source records hydrate figures, reports, the figure registry, and the "
                "manuscript token layer; each surface is checked again at render time. The text is "
                "validated as an artifact surface, not trusted as prose."
            ),
        ),
        FigureSpec(
            key="niche_construction_diagram",
            filename="niche_construction_diagram.png",
            title="Niche construction: organism-environment co-shaping of the prior",
            purpose="Show the reciprocal relationship between organism and environment co-shaping the prior.",
            caption=(
                "The prior-like structure is co-shaped, not fully given by the environment nor "
                "fully endogenous: the organism (O) and its niche (N) reciprocally shape the prior "
                "P, written as N(P) <-> P. Viability still filters what can persist, but the filter "
                "is not purely external."
            ),
        ),
        FigureSpec(
            key="markov_blanket_achievement",
            filename="markov_blanket_achievement.png",
            title="Markov blanket as model-bound achievement",
            purpose="Show the Markov blanket as a model-level boundary whose realization depends on the system's dynamics.",
            caption=(
                "The Markov blanket (M = Phi(X*)) is treated here as a model-level boundary "
                "whose realized approximation depends on the persisting system's own dynamics. "
                "It is neither a merely external partition nor a license to read organismal "
                "boundaries directly from the formalism without additional assumptions."
            ),
        ),
        FigureSpec(
            key="explanatory_complementarity_matrix",
            filename="explanatory_complementarity_matrix.png",
            title="Tinbergen questions are complementary, not rival",
            purpose="Show a 4x4 grid of Tinbergen questions indicating complementarity rather than rivalry.",
            caption=(
                "A 4x4 matrix of the four Tinbergen questions: each diagonal cell is one question "
                "asked of the same phenomenon, and every off-diagonal pair contributes "
                "independently. No question subsumes another; conflating them is the source of the "
                "regress, not the framework."
            ),
        ),
        FigureSpec(
            key="active_inference_cycle",
            filename="active_inference_cycle.png",
            title="Active inference action-perception cycle",
            purpose="Show how action and perception close the free-energy-minimizing loop that the prior serves.",
            caption=(
                "Active inference closes the free-energy-minimizing loop through four stages: "
                "perception, inference, action, and policy selection. The prior serves a process "
                "that minimizes variational free energy F through both inference and action, not "
                "inference alone."
            ),
        ),
        FigureSpec(
            key="variational_free_energy_landscape",
            filename="variational_free_energy_landscape.png",
            title="Variational free energy landscape",
            purpose="Show the free-energy landscape as a surface the system settles into, with the prior as the settling point.",
            caption=(
                "The variational free-energy landscape is a surface the system settles into; the "
                "prior-like structure is the settling point P at the basin floor where F* ~ 0. The "
                "zero-energy limit is the exact posterior, anchoring the prior to the system's own "
                "inference rather than to an external parameter."
            ),
        ),
        FigureSpec(
            key="scale_invariance_diagram",
            filename="scale_invariance_diagram.png",
            title="Scale invariance of prior-like structure",
            purpose="Show that the regress-termination problem recurs at cellular, organismic, and social scales.",
            caption=(
                "The fixed-point move recurs at cellular, organismic, and social scales: "
                "the prior-like settlement X*_k at one scale becomes the substrate for the "
                "next via the scale recursion operator R, written X*_k = Phi(X*_k). No new "
                "hidden prior is needed at each transition; the same regress-termination "
                "structure repeats without introducing a new explanatory kind."
            ),
        ),
        FigureSpec(
            key="source_claim_boundary_map",
            filename="source_claim_boundary_map.png",
            title="Source-to-claim boundary map",
            purpose="Show how scholarship is promoted into claims only through the claim ledger and boundary audit.",
            caption=(
                "Publication claims pass through a source boundary: primary or scholarly sources "
                "enter the accepted-source layer, noisy or overextended sources are rejected or "
                "deferred, and only ledger-backed claims reach the manuscript and formal inventory. "
                "The map makes source discipline visible as part of the paper's argument surface."
            ),
        ),
        FigureSpec(
            key="markov_blanket_scope_split",
            filename="markov_blanket_scope_split.png",
            title="Markov blanket scope split",
            purpose="Separate formal Markov blanket use from realized organismal boundary claims.",
            caption=(
                "Markov blankets do different work in different registers: as Pearl-style "
                "conditional-independence structures, as Friston-style model boundaries in active "
                "inference, and as realized biological boundaries only when additional dynamical "
                "and philosophical assumptions are supplied. The split guards the paper against "
                "turning a useful formalism into an unqualified ontology."
            ),
        ),
        FigureSpec(
            key="niche_prior_feedback_field",
            filename="niche_prior_feedback_field.png",
            title="Niche-prior feedback field",
            purpose="Show organism, niche, and cultural resources co-shaping prior-like structure across timescales.",
            caption=(
                "The niche-prior field layers organismal action, developmental resources, and "
                "cultural inheritance across time. Prior-like structure is shown as a feedback "
                "field stabilized by recurrent organism-niche coupling rather than as a parameter "
                "delivered by either the organism or the environment alone."
            ),
        ),
    )


def formal_claims() -> tuple[FormalClaim, ...]:
    return (
        FormalClaim(
            key="axis_partition",
            title="Axis partition",
            expression="$Q_T = \\{p,u\\} \\times \\{s,d\\}$ and $O = (p,d)$.",
            reading=(
                "Tinbergen explanation starts as a crossed question space. Ontogeny is one cell, "
                "not a level that can inherit the burden of the whole explanation."
            ),
            symbol_keys=("Q_T", "p", "u", "s", "d", "O"),
        ),
        FormalClaim(
            key="regress_shape",
            title="Regress shape",
            expression="$H(P)$ and $D(P)$ can both be iterated; iteration alone does not supply $\\tau$.",
            reading=(
                "A hyperprior operator and a developmental selector differ in content, but both can "
                "recreate the same prior-of-prior regress unless a termination condition is named."
            ),
            symbol_keys=("H", "P", "D", "tau"),
        ),
        FormalClaim(
            key="selection_filter",
            title="Selection filter",
            expression="$S(P) = P^*$ only for forms that persist under viability constraints.",
            reading=(
                "Function plus phylogeny blocks regress by filtering the forms that remain available "
                "as explanatory targets."
            ),
            symbol_keys=("S", "P", "P_star"),
        ),
        FormalClaim(
            key="fixed_point_stop",
            title="Fixed-point stop",
            expression="$X^* = \\Phi(X^*)$; in that case $P$ names the settled organization of $X^*$.",
            reading=(
                "The fixed-point answer is a category shift: the system is the prior-like settlement, "
                "rather than a bearer of one more hidden prior."
            ),
            symbol_keys=("X_star", "Phi", "P"),
        ),
        FormalClaim(
            key="decomposition_caution",
            title="Decomposition caution",
            expression="$\\Lambda \\to (\\pi, P, x)$ is an analytic map, not proof that $(\\pi, P, x) \\to \\Lambda$.",
            reading=(
                "Policy, prior-like constraint, and state factors can be useful decompositions of joint "
                "organization without being ontologically prior to it."
            ),
            symbol_keys=("Lambda", "pi", "P", "x"),
        ),
        FormalClaim(
            key="niche_co_construction",
            title="Niche co-construction",
            expression="$N(P) \\leftrightarrow P$ where $N$ is the niche-mediated co-shaping operator.",
            reading="The prior is not fully endogenous or exogenous; it is co-shaped by organism and niche. This complicates selection termination without changing its logical role.",
            symbol_keys=("N", "P"),
        ),
        FormalClaim(
            key="blanket_achievement",
            title="Blanket achievement",
            expression="$M = \\Phi(X^*)$ where $M$ is the Markov blanket achieved by the settled process.",
            reading="The Markov blanket is used as a model-level boundary whose realized approximation depends on the system's self-maintaining dynamics. The prior-like structure is part of what the model describes the system as maintaining.",
            symbol_keys=("M", "Phi", "X_star"),
        ),
        FormalClaim(
            key="explanatory_complementarity",
            title="Explanatory complementarity",
            expression="$\\forall q_i, q_j \\in Q_T: q_i \\perp q_j$ yet $\\bigcup q_i = \\text{explanation}$.",
            reading="The four Tinbergen questions are complementary perspectives, not rival hypotheses. Conflating them is the source of the regress, not the framework.",
            symbol_keys=("Q_T",),
        ),
        FormalClaim(
            key="active_inference_bridge",
            title="Active inference bridge",
            expression="$A(P, \\pi) \\to \\min \\mathcal{F}$ where $A$ couples perception and action under prior $P$ and policy $\\pi$.",
            reading="Active inference closes the action-perception loop: the prior serves a process that minimizes free energy through both inference and action, not inference alone.",
            symbol_keys=("A", "P", "pi", "F"),
        ),
        FormalClaim(
            key="variational_closure",
            title="Variational closure",
            expression="$\\mathcal{F}(q) \\geq \\mathcal{F}^*$ and $\\mathcal{F}^* \\approx 0$ iff $q = p$; the prior is the settling point of this bound.",
            reading="The variational free energy bounds the log evidence from above (the evidence lower bound). The variational posterior $q$ equals the true posterior $p$ exactly at the minimum, and the free-energy minimum is then approximately zero, anchoring the prior to the system's own inference rather than to an externally supplied distribution.",
            symbol_keys=("F", "F_star", "q", "p_true", "P"),
        ),
        FormalClaim(
            key="scale_invariance",
            title="Scale invariance",
            expression="$R_k(X^*_k) = X^*_{k+1}$ for scales $k \\in \\{\\text{cell}, \\text{organism}, \\text{social}\\}$.",
            reading="The fixed-point termination recurs at each scale: the prior-like settlement at one scale becomes the substrate for the next. No new hidden prior is needed; the same category shift applies recursively.",
            symbol_keys=("R", "X_star"),
        ),
    )


def symbol_glossary() -> tuple[SymbolSpec, ...]:
    return (
        SymbolSpec("Q_T", "$Q_T$", "Tinbergen question space", "The crossed explanatory space used by the paper."),
        SymbolSpec("p", "$p$", "proximate scale", "The mechanism-side explanatory scale."),
        SymbolSpec("u", "$u$", "ultimate scale", "The function or selection-side explanatory scale."),
        SymbolSpec("s", "$s$", "static time-form", "A present-tense explanatory orientation."),
        SymbolSpec("d", "$d$", "developmental time-form", "A historical explanatory orientation."),
        SymbolSpec("O", "$O$", "ontogeny cell", "The proximate-developmental quadrant."),
        SymbolSpec("P", "$P$", "prior-like constraint", "The prior or prior-like organization being explained."),
        SymbolSpec("H", "$H$", "hyperprior operator", "A prior-on-prior move in hierarchical Bayes language."),
        SymbolSpec("D", "$D$", "developmental selector", "An ontogenetic prior-selection move."),
        SymbolSpec("tau", "$\\tau$", "termination condition", "A stop rule that prevents another regress level."),
        SymbolSpec("S", "$S$", "selection filter", "Function-plus-phylogeny filtering of viable forms."),
        SymbolSpec("P_star", "$P^*$", "persisting prior form", "A prior-like form that remains available for explanation."),
        SymbolSpec("X_star", "$X^*$", "settled system state", "A persisting self-individuating organization."),
        SymbolSpec("Phi", "$\\Phi$", "self-mapping process", "The process whose fixed point is the settled system state."),
        SymbolSpec("Lambda", "$\\Lambda$", "joint organization", "The entangled structure before analytic decomposition."),
        SymbolSpec("pi", "$\\pi$", "policy factor", "A policy factor extracted by decomposition."),
        SymbolSpec("x", "$x$", "state factor", "A state factor extracted by decomposition."),
        SymbolSpec("N", "$N$", "niche-mediated co-shaping", "The operator representing organism-niche reciprocal shaping of priors."),
        SymbolSpec("M", "$M$", "Markov blanket", "The statistical boundary achieved by the settled system process."),
        SymbolSpec("A", "$A$", "active inference operator", "The operator coupling perception and action under a prior and policy to minimize free energy."),
        SymbolSpec("F", "$\\mathcal{F}$", "variational free energy", "The upper bound on negative log evidence that the system minimizes."),
        SymbolSpec("F_star", "$\\mathcal{F}^*$", "optimal free energy", "The minimum free energy achieved when the variational posterior equals the true posterior."),
        SymbolSpec("q", "$q$", "variational posterior", "The approximate posterior distribution the system maintains."),
        SymbolSpec("p_true", "$p^*$", "true posterior", "The exact posterior distribution $p$, written $p^*$ at the variational minimum; the zero-free-energy limit of variational inference."),
        SymbolSpec("R", "$R$", "scale recursion operator", "The operator mapping a settled system at one scale to the substrate at the next."),
    )


def text_validation_checks() -> tuple[TextValidationCheck, ...]:
    return (
        TextValidationCheck(
            key="no_simulation_boundary",
            surface="manuscript and analysis report",
            invariant="The project states that it uses no simulations or numerical performance claims.",
            evidence="SIMULATION_POLICY token and conceptual_analysis.json simulation_free flag.",
        ),
        TextValidationCheck(
            key="figure_registry_closure",
            surface="output/figures/figure_registry.json",
            invariant="Every figure specification has a generated artifact and a registry label.",
            evidence="figure_specs() and run_analysis_pipeline() compare expected and produced filenames.",
        ),
        TextValidationCheck(
            key="symbol_glossary_closure",
            surface="formal supplement",
            invariant="Every symbol key used by a formal claim appears in the generated glossary.",
            evidence="validate_conceptual_contract() checks formal_claims() against symbol_glossary().",
        ),
        TextValidationCheck(
            key="token_hydration",
            surface="output/manuscript",
            invariant="Every double-brace manuscript token is generated before render.",
            evidence="test_all_manuscript_tokens_are_generated and hydration script smoke test.",
        ),
        TextValidationCheck(
            key="integrity_signature",
            surface="reproducibility section",
            invariant="A generated token binds the conceptual inventory used by prose, figures, and tests.",
            evidence="CONCEPTUAL_INTEGRITY_TOKEN is derived from source records, not hand-authored prose.",
        ),
        TextValidationCheck(
            key="claim_dependency_closure",
            surface="formal supplement",
            invariant="Every claim dependency edge references a claim key that exists.",
            evidence="claim_dependencies() checks source_claim and target_claim against formal_claims().",
        ),
        TextValidationCheck(
            key="metadata_keyword_consistency",
            surface="metadata files",
            invariant="Keywords in config.yaml are a subset of .zenodo.json, codemeta.json, and CITATION.cff.",
            evidence="test_metadata_keywords_are_consistent_across_all_files checks all metadata files.",
        ),
        TextValidationCheck(
            key="citation_resolution",
            surface="manuscript references",
            invariant="Every citation reference in the manuscript has a bib entry in references.bib.",
            evidence="test_all_manuscript_citations_resolve_to_bib scans all manuscript files.",
        ),
        TextValidationCheck(
            key="figure_count_consistency",
            surface="manuscript and analysis report",
            invariant="The figure count in the manuscript token matches the actual number of generated figure files.",
            evidence="FIGURE_COUNT token and output/figures/*.png file count are compared by the analysis pipeline.",
        ),
        TextValidationCheck(
            key="argument_module_closure",
            surface="manuscript and source inventory",
            invariant="Every argument module key in the source has a corresponding discussion in the manuscript prose.",
            evidence="ARGUMENT_MODULES token injects the full list; the manuscript references each module by title.",
        ),
    )


def claim_dependencies() -> tuple[ClaimDependency, ...]:
    return (
        ClaimDependency("axis_partition", "regress_shape", "The crossed axes show which quadrant creates regress pressure."),
        ClaimDependency("regress_shape", "selection_filter", "The regress shape motivates the need for a termination condition."),
        ClaimDependency("regress_shape", "fixed_point_stop", "The regress shape motivates the fixed-point alternative."),
        ClaimDependency("selection_filter", "niche_co_construction", "Selection filtering is complicated by niche co-construction."),
        ClaimDependency("fixed_point_stop", "blanket_achievement", "The fixed-point settlement implies the blanket is achieved."),
        ClaimDependency("axis_partition", "explanatory_complementarity", "The axis partition shows the questions are complementary."),
        ClaimDependency("decomposition_caution", "niche_co_construction", "Joint structure and niche co-construction both resist factor-first readings."),
        ClaimDependency("blanket_achievement", "active_inference_bridge", "The achieved blanket provides the boundary within which active inference operates."),
        ClaimDependency("fixed_point_stop", "variational_closure", "The fixed-point settlement is the zero-energy limit of the variational bound."),
        ClaimDependency("active_inference_bridge", "scale_invariance", "Active inference at one scale provides the substrate for the next."),
        ClaimDependency("variational_closure", "scale_invariance", "The variational closure applies recursively at each scale."),
        ClaimDependency("explanatory_complementarity", "active_inference_bridge", "Complementarity of perspectives is preserved when action and perception are unified."),
    )


def used_symbol_keys() -> frozenset[str]:
    return frozenset(key for claim in formal_claims() for key in claim.symbol_keys)


def validate_claim_dependencies() -> tuple[str, ...]:
    errors: list[str] = []
    claim_keys = {claim.key for claim in formal_claims()}
    for dep in claim_dependencies():
        if dep.source_claim not in claim_keys:
            errors.append(f"dependency source_claim {dep.source_claim!r} not in formal claims")
        if dep.target_claim not in claim_keys:
            errors.append(f"dependency target_claim {dep.target_claim!r} not in formal claims")
    return tuple(errors)


def validate_conceptual_contract() -> tuple[str, ...]:
    errors: list[str] = []
    symbol_keys = {symbol.key for symbol in symbol_glossary()}
    used_keys = used_symbol_keys()

    missing_symbols = sorted(used_keys - symbol_keys)
    if missing_symbols:
        errors.append(f"missing symbol glossary rows: {', '.join(missing_symbols)}")

    unused_symbols = sorted(symbol_keys - used_keys)
    if unused_symbols:
        errors.append(f"unused symbol glossary rows: {', '.join(unused_symbols)}")

    figure_keys = [spec.key for spec in figure_specs()]
    if len(figure_keys) != len(set(figure_keys)):
        errors.append("duplicate figure keys")

    figure_filenames = [spec.filename for spec in figure_specs()]
    if len(figure_filenames) != len(set(figure_filenames)):
        errors.append("duplicate figure filenames")

    formal_keys = [claim.key for claim in formal_claims()]
    if len(formal_keys) != len(set(formal_keys)):
        errors.append("duplicate formal claim keys")

    errors.extend(validate_claim_dependencies())

    return tuple(errors)


def as_records(items: tuple[object, ...]) -> list[dict[str, object]]:
    return [asdict(item) for item in items]


def conceptual_integrity_token() -> str:
    payload = {
        "argument_modules": as_records(argument_modules()),
        "claim_dependencies": as_records(claim_dependencies()),
        "figures": as_records(figure_specs()),
        "formal_claims": as_records(formal_claims()),
        "quadrants": as_records(quadrant_grid()),
        "symbols": as_records(symbol_glossary()),
        "terminations": as_records(termination_catalog()),
        "validation_checks": as_records(text_validation_checks()),
    }
    blob = json.dumps(payload, ensure_ascii=True, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()[:16]
