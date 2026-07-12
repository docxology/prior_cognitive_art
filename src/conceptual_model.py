from __future__ import annotations

import hashlib
import json
from dataclasses import asdict, dataclass, replace


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
    section: str = ""
    alt_text: str = ""


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


@dataclass(frozen=True)
class ClaimGrounding:
    source_record: str
    claim_key: str


@dataclass(frozen=True)
class DeterministicSimulationStep:
    step: int
    state: str
    formal_state: str
    transition: str
    invariant: str
    x: float
    y: float


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
            title="Three termination families organize the paper",
            claim=(
                "The paper organizes the regress around pragmatic, selection, and "
                "fixed-point termination families without claiming that these exhaust "
                "every possible explanatory stop."
            ),
        ),
        ArgumentModule(
            key="first_prior_grounding",
            title="Before the first prior is constraint history",
            claim=(
                "Going upstream does not reveal a hidden prior before all priors; it "
                "reveals viability, regulation, shared embodiment, developmental "
                "tuning, and niche structure that make learned priors possible."
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
            claim="Active inference couples perception and action while distinguishing variational free energy for inference from expected free energy for policy selection, closing the explanatory loop the prior was meant to serve.",
        ),
        ArgumentModule(
            key="scale_recurrence_of_priors",
            title="Prior-like structure recurs across scales",
            claim="The regress-termination problem recurs at the cellular, organismic, and social scales; the fixed-point move applies at each level without requiring a new hidden prior.",
        ),
        ArgumentModule(
            key="aesthetic_prior_craft",
            title="Art arranges encounters with priors",
            claim=(
                "The paper's art claim is bounded: aesthetic practices arrange cues, "
                "contexts, and meanings that interact with predictive priors; they do "
                "not prove that art directly rewires priors as an empirical mechanism."
            ),
        ),
    )


def deterministic_simulation_trace() -> tuple[DeterministicSimulationStep, ...]:
    return (
        DeterministicSimulationStep(
            step=0,
            state="Question typed",
            formal_state=r"$\sigma_0 = P?$",
            transition="Ask why the prior exists.",
            invariant="No numerical belief update is introduced.",
            x=1.05,
            y=2.65,
        ),
        DeterministicSimulationStep(
            step=1,
            state="Regress exposed",
            formal_state=r"$\sigma_1 = H(P)$",
            transition="A hyperprior answer repeats the question at one level up.",
            invariant="The step records logical deferral only.",
            x=3.1,
            y=3.25,
        ),
        DeterministicSimulationStep(
            step=2,
            state="Tinbergen split",
            formal_state=r"$\sigma_2 \in Q_T$",
            transition="The question is partitioned by explanatory kind.",
            invariant="Quadrants organize scope; they do not estimate effects.",
            x=5.0,
            y=2.6,
        ),
        DeterministicSimulationStep(
            step=3,
            state="Termination chosen",
            formal_state=r"$\sigma_3 \models \tau$",
            transition="Selection or fixed-point criteria provide a stop rule.",
            invariant="The stop rule is conceptual sufficiency, not model fit.",
            x=6.9,
            y=3.25,
        ),
        DeterministicSimulationStep(
            step=4,
            state="Settlement named",
            formal_state=r"$\sigma_4 = X^*=\Phi(X^*)$",
            transition="The prior is redescribed as settled organization.",
            invariant="The trace ends in a category shift, not a hidden prior.",
            x=8.85,
            y=2.6,
        ),
    )


def figure_specs() -> tuple[FigureSpec, ...]:
    records = (
        FigureSpec(
            key="tinbergen_axes",
            filename="tinbergen_axes.png",
            title="Tinbergen's crossed axes for locating prior-origin questions",
            purpose="Stage the crossed explanatory axes as a reading surface that prevents ontogeny from carrying every prior-origin question.",
            caption=(
                "Four colored panels hold Tinbergen's questions in tension rather than stacking "
                "them into a causal ladder. Read across scale and then down temporality: mechanism "
                "and function can close local questions about present organization and current use, "
                "while ontogeny and phylogeny ask how that form was shaped and retained. The key "
                "visual warning is that the regress appears when one panel, usually ontogeny, is "
                "asked to speak for the whole grid. The figure therefore turns a familiar taxonomy "
                "into a guardrail against explaining a prior by merely naming its developmental source."
            ),
        ),
        FigureSpec(
            key="regress_terminations",
            filename="regress_terminations.png",
            title="Where the hyperprior regress stops: pragmatic, selection, and fixed-point exits",
            purpose="Set the repeating hyperprior chain against the three legitimate stopping moves and their different explanatory costs.",
            caption=(
                "The upper chain is deliberately too easy to extend: a prior receives a hyperprior, "
                "then that hyperprior seems to need its own warrant. The lower register names the "
                "three different ways the picture can stop without pretending the next box solves "
                "the problem. Pragmatic, selection, and fixed-point endings are visualized as "
                "explanatory disciplines, not as empirical discoveries of prior origins. The point "
                "is not that the endings are interchangeable; each buys closure at a different price: "
                "formal sufficiency, viability filtering, or a category shift from hidden cause to "
                "settled organization."
            ),
        ),
        FigureSpec(
            key="prior_equilibrium_map",
            filename="prior_equilibrium_map.png",
            title="Prior as settled organization in a maintained action-perception loop",
            purpose="Present the fixed-point move as a loop of maintenance rather than a higher cause or numerical equilibrium.",
            caption=(
                "The circular composition makes the fixed-point move visible: the prior is not "
                "another hidden object above the system, but the settled organization of the "
                "system's own process. Blanket persistence, action-perception closure, and "
                "environmental viability feed back into the same maintained form. The claim is a "
                "category shift about what is being explained, not a numerical equilibrium result. "
                "The figure should be read as a maintenance grammar: the explanatory target is the "
                "stable pattern by which the system keeps being the kind of system that can carry "
                "prior-like constraints."
            ),
        ),
        FigureSpec(
            key="ontogeny_hyperprior_parallel",
            filename="ontogeny_hyperprior_parallel.png",
            title="Ontogeny-only explanation and hyperprior recursion share the same deferral shape",
            purpose="Pair developmental deferral with hyperprior deferral to expose their shared silhouette.",
            caption=(
                "The two horizontal chains are drawn as visual echoes. A Bayesian hyperprior and "
                "an ontogenetic selector are not the same biological claim, but both can defer the "
                "question to the source that licensed the current prior. The red bracket marks "
                "that shared silhouette of deferral while preserving the difference between "
                "formal hierarchy and developmental history. The bottom warning is the important "
                "reading instruction: adding another selector, tutor, developmental episode, or "
                "higher prior can continue the chain without explaining why the chain is allowed "
                "to terminate."
            ),
        ),
        FigureSpec(
            key="selection_filter",
            filename="selection_filter.png",
            title="Selection as a viability filter that blocks regress without another selector",
            purpose="Turn function and phylogeny into a filter that explains persistence without another selector.",
            caption=(
                "Candidate prior-like forms enter as a rough population, not as equal explanatory "
                "successes. The function-plus-phylogeny funnel removes forms that cannot remain "
                "available as persisting targets: fragile, miscalibrated, or overfit structures "
                "drop out of the story. Selection blocks regress by explaining availability "
                "through viability rather than placing one more selector behind the filter. The "
                "figure deliberately leaves individual fine structure outside the funnel's answer, "
                "because selection explains why a form is available to inherit, use, or refine, not "
                "every detail of how one organism acquired it."
            ),
        ),
        FigureSpec(
            key="policy_entanglement_bridge",
            filename="policy_entanglement_bridge.png",
            title="Joint organization before lambda-decomposition and cleaned-up factors",
            purpose="Frame lambda-decomposition as an analytic cut through prior joint organization.",
            caption=(
                "The large joint form on the left is intentionally prior to the separated boxes on "
                "the right. Lambda-decomposition makes policy, prior-like constraint, and state "
                "factor legible after the analytic cut, but it does not prove that those factors "
                "were ontologically first. The bridge keeps the argument focused on how cleaned-up "
                "factors are extracted from an already organized field. This matters for the paper's "
                "prior-origin question because a formal decomposition can clarify a system without "
                "becoming a story about the historical order in which the system's parts came to be."
            ),
        ),
        FigureSpec(
            key="formal_claim_dependency_map",
            filename="formal_claim_dependency_map.png",
            title="Formal claim grounding map from source records to numbered supplement claims",
            purpose="Make source-to-claim provenance visible instead of presenting decorative theorem labels.",
            caption=(
                "The map turns the formal supplement into a provenance surface. Claims F1-F12 are "
                "not decorative theorem labels; they are grounded in source records for axes, "
                "regress shape, termination moves, joint structure, niche, blanket, complementarity, "
                "and trace boundaries. Numbering follows source order, so prose, figures, and "
                "formal labels have to move together. The arrows record grounding, not theorem-level "
                "entailment. The figure's job is editorial as much as philosophical: it shows where "
                "a reader can ask which source-owned record authorizes each formal move."
            ),
        ),
        FigureSpec(
            key="symbol_glossary_closure",
            filename="symbol_glossary_closure.png",
            title="Symbol glossary closure as a no-orphan contract for notation",
            purpose="Treat notation as a closure surface where every mark must be accounted for.",
            caption=(
                "The paired panels make a simple editorial demand: every formal mark used by a "
                "claim must be defined, and every definition must be used. This turns notation "
                "from ornament into an accountable surface of the manuscript. If the two sides "
                "fall out of correspondence, the package fails before render. The visual symmetry "
                "is intentionally blunt: a symbol that appears only in prose decoration, or a "
                "glossary row that never serves a claim, would make the formal supplement less "
                "trustworthy rather than more impressive."
            ),
        ),
        FigureSpec(
            key="text_validation_ladder",
            filename="text_validation_ladder.png",
            title="Text validation ladder from source inventory to rendered manuscript",
            purpose="Stack source, generation, rendering, and validation as a single manuscript-making ladder.",
            caption=(
                "The ladder treats the paper as something made, not merely written. Source records "
                "hydrate reports, figures, tokens, and render surfaces; validation then climbs the "
                "same stack after generation. A drifting caption, registry row, or prose token is "
                "therefore not a minor typo but a contract error in the artifact pipeline. The "
                "figure also explains why the project keeps manuscript prose, dashboard data, figure "
                "metadata, and validator output in the same loop instead of treating them as separate "
                "publication chores."
            ),
        ),
        FigureSpec(
            key="niche_construction_diagram",
            filename="niche_construction_diagram.png",
            title="Niche construction as reciprocal organism-environment prior formation",
            purpose="Paint prior formation as reciprocal organism-niche work rather than one-way inheritance.",
            caption=(
                "The central prior is drawn between organism and niche because neither side owns "
                "the explanation alone. Organisms act into environments that answer back as altered "
                "regularities, affordances, and selection pressures. Viability still filters what "
                "persists, but the filter is partly made by the organism-niche loop it later "
                "appears to judge. The two-way arrows prevent the figure from becoming a simple "
                "environmental imprint model: priors are co-shaped by what organisms do, what niches "
                "make available, and what remains viable across that reciprocal history."
            ),
        ),
        FigureSpec(
            key="markov_blanket_achievement",
            filename="markov_blanket_achievement.png",
            title="Markov blanket as a model-bound achievement rather than a literal membrane",
            purpose="Draw the blanket as an achieved model boundary with explicit ontological restraint.",
            caption=(
                "The boundary is deliberately drawn as a model-level partition M=(a,s) whose "
                "conditional-independence relation screens internal from external states. It is "
                "associated with settled organization, not read off the world as a literal membrane. "
                "The image keeps formal usefulness and ontological restraint in the same frame. It "
                "therefore supports the manuscript's blanket language while blocking a stronger claim "
                "that the notation alone discovers the true edge of an organism, artwork, or cognitive system."
            ),
        ),
        FigureSpec(
            key="explanatory_complementarity_matrix",
            filename="explanatory_complementarity_matrix.png",
            title="Tinbergen questions as complementary modes rather than rival explanations",
            purpose="Turn Tinbergen's questions into a coordination matrix instead of a rivalry table.",
            caption=(
                "The matrix lets each Tinbergen question meet the others without being absorbed by "
                "them. Diagonal cells name each explanatory mode; off-diagonal cells mark places "
                "where coordination is legitimate but reduction is not. The regress is not caused "
                "by asking several questions. It is caused by collapsing their different jobs into "
                "one overburdened answer. The plus signs should be read as invitations to coordinate "
                "mechanism, function, ontogeny, and phylogeny, not as permission to translate all four "
                "into a single master vocabulary."
            ),
        ),
        FigureSpec(
            key="active_inference_cycle",
            filename="active_inference_cycle.png",
            title="Active inference action-perception cycle with distinct F and G roles",
            purpose="Show action and perception as one circular practice served by prior-like structure.",
            caption=(
                "The loop makes active inference a practice rather than a passive estimate. "
                "Perception and inference are evaluated through variational free energy, while "
                "policy selection is evaluated through expected free energy; the objectives remain "
                "distinct inside one action-perception loop. Prior-like structure is a constraint "
                "in that coupled organization, not merely a static number placed before observation. "
                "The center of the image marks inferential pressure, while the cycle shows why that "
                "pressure only matters inside an organism-world practice of sensing, selecting, and acting."
            ),
        ),
        FigureSpec(
            key="variational_free_energy_landscape",
            filename="variational_free_energy_landscape.png",
            title="Variational bound landscape for relative settlement, not zero free energy",
            purpose="Use a basin image for relative variational settlement without implying zero free energy.",
            caption=(
                "The basin is a picture of relative settlement inside a model, not a claim that "
                "free energy literally falls to zero. The marked path shows an approximate "
                "posterior moving toward a target posterior under a tractable bound. The figure "
                "supports a bounded settling metaphor for prior-like constraint while refusing an "
                "empirical origin story for priors. The color field is schematic geometry rather than "
                "observed data, so the reader should take it as a disciplined analogy for variational "
                "closure, not as a fitted result."
            ),
        ),
        FigureSpec(
            key="deterministic_simulation_trace",
            filename="deterministic_simulation_trace.png",
            title="Deterministic trace of the argument's formal-state order",
            purpose="Present the authored state sequence as a conceptual trace, not simulation evidence.",
            caption=(
                "The trace borrows the visual grammar of a state diagram while staying inside the "
                "paper's conceptual scope. Each node is an authored formal state: question, "
                "regress, Tinbergen partition, termination choice, and fixed-point settlement. "
                "The arrows record argumentative order only; the invariants block stochastic, "
                "synthetic-data, performance, or effect-size readings. The figure is included because "
                "ordered formal commitments are easier to audit visually, not because the paper runs "
                "a cognitive simulation."
            ),
        ),
        FigureSpec(
            key="scale_recurrence_diagram",
            filename="scale_recurrence_diagram.png",
            title="Scale recurrence of prior-like settlements across cellular, organismic, and social registers",
            purpose="Repeat the fixed-point grammar across scales while keeping the recurrence conceptual.",
            caption=(
                "The three panels repeat the fixed-point grammar at cellular, organismic, and "
                "social registers. A prior-like settlement at one scale can become substrate for "
                "another through R, but the image does not smuggle in a new hidden prior at each "
                "transition. It shows recurrence of an explanatory problem, not mathematical "
                "scale invariance or empirical self-similarity. The repeated grammar invites comparison "
                "without erasing scale-specific mechanisms, histories, and material supports."
            ),
        ),
        FigureSpec(
            key="source_claim_boundary_map",
            filename="source_claim_boundary_map.png",
            title="Source-to-claim boundary map for disciplined scholarship promotion",
            purpose="Make scholarship promotion visibly pass through verification and claim-boundary gates.",
            caption=(
                "The map makes citation discipline part of the artwork of the paper. Discovery "
                "candidates do not flow directly into prose; they pass through verification and "
                "claim-ledger boundaries before reaching manuscript claims, formal inventory, or "
                "visual atlas. Rejected and deferred sources stay visible so scholarship does not "
                "become unbounded accumulation. The image also marks a practical rule for future edits: "
                "a source can expand the paper only when it changes a live claim, a boundary condition, "
                "or a generated artifact contract."
            ),
        ),
        FigureSpec(
            key="aesthetic_prior_craft_map",
            filename="aesthetic_prior_craft_map.png",
            title="Aesthetic prior-craft map: how art stages bounded encounters with expectation",
            purpose="Locate prior-craft between predictive aesthetics, 4E practice, and claim restraint.",
            caption=(
                "This figure is the paper's most self-conscious art claim. Predictive aesthetics, "
                "4E/material engagement, and neuroaesthetic scope converge on prior-craft: artworks "
                "can stage encounters with expectation, ambiguity, affordance, affect, and meaning. "
                "The red ceiling matters as much as the purple center: this is not a total theory "
                "of art, intention, culture, or neural updating. The figure's value is to keep the title "
                "term active without letting it become an empirical claim that art directly installs or "
                "rewires priors."
            ),
        ),
        FigureSpec(
            key="markov_blanket_scope_split",
            filename="markov_blanket_scope_split.png",
            title="Markov blanket scope split between formal use, model boundary, and biological realization",
            purpose="Separate formal blanket use from stronger organism-boundary commitments.",
            caption=(
                "The split makes three registers visible before they can be collapsed: a "
                "conditional-independence structure, an active-inference model boundary, and a "
                "realized biological or cognitive boundary. The first two support the paper's "
                "model-level argument. The third requires additional dynamical and philosophical "
                "premises, so it is held behind an explicit boundary condition. The right-hand boxes "
                "state the operational rule: use blankets to discipline model talk, not to shortcut "
                "the ontology of living or cognitive systems."
            ),
        ),
        FigureSpec(
            key="niche_prior_feedback_field",
            filename="niche_prior_feedback_field.png",
            title="Niche-prior feedback field across organismal, developmental, and cultural timescales",
            purpose="Layer organismal, developmental, and cultural feedback as one prior-stabilizing field.",
            caption=(
                "The field layers fast organismal action, slower developmental resources, and "
                "still slower cultural inheritance. Prior-like structure stabilizes through the "
                "recurrence among these bands, including material and cultural scaffolds, rather "
                "than arriving from organism or environment alone. The field constrains selection "
                "termination without becoming a fourth stopping rule. The timescale arrow is part of "
                "the argument: what looks like an individual's prior may depend on slower supports that "
                "were already arranged by development, culture, and niche construction."
            ),
        ),
        FigureSpec(
            key="first_prior_grounding_stack",
            filename="first_prior_grounding_stack.png",
            title="Before the first prior: constraint history rather than a hidden meta-prior",
            purpose=(
                "Render upstream bias as a layered constraint history before learned priors, "
                "not as another hidden meta-prior."
            ),
            caption=(
                "The stack answers the RedTeam question by refusing the easy move of placing "
                "one more prior behind the first prior. Viability asymmetry, homeostatic and "
                "allostatic regulation, co-embodiment and co-homeostasis, developmental tuning, "
                "and cultural niche craft are shown as enabling constraints before explicit "
                "belief-like priors. The bottom boundary is part of the claim: upstream bias is "
                "a history of regulation and support, not an empirical discovery of a literal "
                "prior-before-priors. The stack improves the manuscript's origin story by showing how "
                "bias can be real, structured, and inherited without being another belief waiting at "
                "the beginning of the chain."
            ),
        ),
    )
    return tuple(
        replace(
            spec,
            section=_FIGURE_SECTION_BY_KEY[spec.key],
            alt_text=_FIGURE_ALT_TEXT_BY_KEY[spec.key],
        )
        for spec in records
    )


_FIGURE_SECTION_BY_KEY = {
    "tinbergen_axes": "Visual Atlas",
    "regress_terminations": "Visual Atlas",
    "prior_equilibrium_map": "Visual Atlas",
    "ontogeny_hyperprior_parallel": "Visual Atlas",
    "selection_filter": "Visual Atlas",
    "policy_entanglement_bridge": "Visual Atlas",
    "formal_claim_dependency_map": "Formal Supplement",
    "symbol_glossary_closure": "Formal Supplement",
    "text_validation_ladder": "Formal Supplement",
    "niche_construction_diagram": "Visual Atlas",
    "markov_blanket_achievement": "Visual Atlas",
    "explanatory_complementarity_matrix": "Visual Atlas",
    "active_inference_cycle": "Visual Atlas",
    "variational_free_energy_landscape": "Visual Atlas",
    "deterministic_simulation_trace": "Visual Atlas",
    "scale_recurrence_diagram": "Visual Atlas",
    "source_claim_boundary_map": "Visual Atlas",
    "aesthetic_prior_craft_map": "Visual Atlas",
    "markov_blanket_scope_split": "Visual Atlas",
    "niche_prior_feedback_field": "Visual Atlas",
    "first_prior_grounding_stack": "Visual Atlas",
}


_FIGURE_ALT_TEXT_BY_KEY = {
    "tinbergen_axes": "Four colored panels arrange mechanism, function, ontogeny, and phylogeny on crossed proximate-ultimate and static-developmental axes.",
    "regress_terminations": "A prior leads to a hyperprior and then another level, above three exits labeled pragmatic, selection, and self-referential termination.",
    "prior_equilibrium_map": "Concentric loops connect blanket persistence, environmental viability, and action-perception closure around a prior-like settled organization.",
    "ontogeny_hyperprior_parallel": "Parallel Bayesian and developmental chains show that adding another prior or selector repeats the same deferral shape.",
    "selection_filter": "Candidate prior-like forms pass through a function-and-phylogeny viability filter, leaving a persisting prior form.",
    "policy_entanglement_bridge": "A joint organization branches into policy, prior-like constraint, and state factors after lambda-decomposition.",
    "formal_claim_dependency_map": "Source records connect by arrows to numbered formal claims F1 through F12 in two columns.",
    "symbol_glossary_closure": "A used-symbol set and a generated glossary set meet at an equality check, with a contract-failure warning below.",
    "text_validation_ladder": "A vertical ladder connects source records, analysis artifacts, injected tokens, rendered manuscript, and validation gates.",
    "niche_construction_diagram": "Organism and environment or niche reciprocally shape a central prior-like structure through two-way arrows.",
    "markov_blanket_achievement": "A settled system sits inside a model boundary separating internal and external states, with a warning against reading the boundary as literal ontology.",
    "explanatory_complementarity_matrix": "A four-by-four matrix highlights each Tinbergen question on the diagonal and coordination signs in off-diagonal cells.",
    "active_inference_cycle": "Perception, inference, action, and policy selection form a clockwise loop with distinct F and G roles.",
    "variational_free_energy_landscape": "A qualitative basin shows an initial approximate posterior moving toward a target posterior under a relative variational bound.",
    "deterministic_simulation_trace": "Five colored formal states progress from asking about a prior through regress, partition, termination, and settled organization.",
    "scale_recurrence_diagram": "Cellular, organismic, and social panels repeat a fixed-point equation and connect downward through a recurrence operator R.",
    "source_claim_boundary_map": "Candidate sources pass through verification, accepted or rejected layers, and a claim ledger before reaching manuscript and formal outputs.",
    "aesthetic_prior_craft_map": "Predictive aesthetics, four-E practice, and neuroaesthetic scope converge on bounded prior-craft beside a claim ceiling.",
    "markov_blanket_scope_split": "Three source registers feed model use, metaphysical use, and biological realization, with the paper's bounded stance at the right.",
    "niche_prior_feedback_field": "Organismic action, developmental resources, and cultural inheritance feed a central prior-like field across timescales.",
    "first_prior_grounding_stack": "A layered stack moves from viability and regulation through co-homeostasis and development to cultural priors, rejecting a hidden prior-before-priors.",
}


def formal_claims() -> tuple[FormalClaim, ...]:
    return (
        FormalClaim(
            key="axis_partition",
            title="Axis partition",
            expression="$Q_T = \\{p,u\\} \\times \\{\\mathrm{static},\\mathrm{developmental}\\}$ and $O = (p,\\mathrm{developmental})$.",
            reading=(
                "Tinbergen explanation starts as a crossed question space. Ontogeny is one cell, "
                "not a level that can inherit the burden of the whole explanation."
            ),
            symbol_keys=("Q_T", "p", "u", "O"),
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
            expression="$(P_{t+1},E_{t+1})=N(P_t,E_t)$ where $N$ is a niche-mediated co-shaping operator.",
            reading="The prior-like organization and its environment are updated together in the conceptual recurrence. This complicates selection termination without turning niche construction into a fourth stop rule.",
            symbol_keys=("N", "P", "E", "t"),
        ),
        FormalClaim(
            key="blanket_achievement",
            title="Blanket achievement",
            expression="$X^* = \\Phi(X^*)$ and $M=(a,s)$ with $\\Pr(\\eta\\mid\\mu,a,s)=\\Pr(\\eta\\mid a,s)$.",
            reading=(
                "The blanket claim is conditional and model-level: for a selected state partition, "
                "active and sensory variables M=(a,s) screen internal states \\mu from external states "
                "\\eta. The fixed point supplies an organizational context, not a proof that this "
                "conditional-independence boundary is a literal biological membrane."
            ),
            symbol_keys=("M", "Phi", "X_star", "a", "s", "eta", "mu"),
        ),
        FormalClaim(
            key="explanatory_complementarity",
            title="Explanatory complementarity",
            expression="$Q_T=\\{e_i\\}_{i=1}^{4},\\ e_i\\not\\equiv e_j\\ (i\\ne j),\\ \\operatorname{explanation}=\\bigcup_i e_i$.",
            reading="The four Tinbergen questions are distinct explanatory modes that can be coordinated without one subsuming another. Conflating them is the source of the regress, not the framework.",
            symbol_keys=("Q_T", "e"),
        ),
        FormalClaim(
            key="active_inference_bridge",
            title="Active inference bridge",
            expression="$A(P,\\pi): q^*=\\arg\\min_q \\mathcal{F}(q\\mid\\pi,P),\\quad \\pi^*\\in\\arg\\min_\\pi G(\\pi\\mid P)$.",
            reading="Active inference couples perception and action while distinguishing variational free energy for inference from expected free energy for policy selection. The expression is a bridge between the two objectives, not a claim that they are one scalar process.",
            symbol_keys=("A", "P", "pi", "F", "G", "q"),
        ),
        FormalClaim(
            key="variational_closure",
            title="Variational closure",
            expression="$\\mathcal{F}(q)=D_{KL}(q\\|p^*)+\\mathcal{F}^* \\ge \\mathcal{F}^*$; q^*=p^* only when $p^*\\in\\mathcal{Q}$ and the minimum is attained.",
            reading=(
                "The variational free-energy bound differs from its reference minimum by a KL term "
                "under the stated decomposition. If the target is outside the variational family, "
                "the optimum is a KL projection rather than the target itself. This supports a "
                "bounded, model-internal settling interpretation; it is not a literal zero-energy "
                "claim and it does not derive the historical origin of the prior."
            ),
            symbol_keys=("F", "F_star", "q", "p_true", "Q"),
        ),
        FormalClaim(
            key="scale_recurrence",
            title="Scale recurrence",
            expression="$R_k(X^*_k) = X^*_{k+1}$ for scales $k \\in \\{\\text{cell}, \\text{organism}, \\text{social}\\}$.",
            reading="The fixed-point grammar recurs across scales: a settlement at one scale can become substrate for the next. This is a conceptual recurrence relation, not a claim of scale invariance or empirical self-similarity.",
            symbol_keys=("R", "X_star"),
        ),
        FormalClaim(
            key="deterministic_trace_boundary",
            title="Deterministic trace boundary",
            expression="$T=(\\sigma_0,\\ldots,\\sigma_4)$ and $\\delta(\\sigma_i)=\\sigma_{i+1}$ for authored conceptual states only.",
            reading=(
                "The deterministic illustrative simulation records the formal state path through "
                "regress pressure and termination choice. It is a checkable exposition device, not "
                "a stochastic simulation, synthetic data generator, empirical estimate, or "
                "performance metric."
            ),
            symbol_keys=("T", "sigma", "delta"),
        ),
    )


def symbol_glossary() -> tuple[SymbolSpec, ...]:
    return (
        SymbolSpec("Q_T", "$Q_T$", "Tinbergen question space", "The crossed explanatory space used by the paper."),
        SymbolSpec("p", "$p$", "proximate scale", "The mechanism-side explanatory scale."),
        SymbolSpec("u", "$u$", "ultimate scale", "The function or selection-side explanatory scale."),
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
        SymbolSpec("E", "$E$", "environmental state", "The environmental or niche state co-shaped with prior-like organization."),
        SymbolSpec("t", "$t$", "conceptual update index", "An index for the ordered niche co-shaping recurrence."),
        SymbolSpec("M", "$M$", "Markov blanket variables", "The active and sensory variables used as a model-level conditional-independence boundary."),
        SymbolSpec("a", "$a$", "active blanket state", "An active state variable in the selected Markov blanket partition."),
        SymbolSpec("s", "$s$", "sensory blanket state", "A sensory state variable in the selected Markov blanket partition."),
        SymbolSpec("eta", "$\\eta$", "external state", "A state outside the selected blanket partition."),
        SymbolSpec("mu", "$\\mu$", "internal state", "A state inside the selected blanket partition."),
        SymbolSpec("A", "$A$", "active inference operator", "The operator coupling perception and action under a prior and policy to minimize free energy."),
        SymbolSpec("F", "$\\mathcal{F}$", "variational free energy", "The upper bound on negative log evidence that the system minimizes."),
        SymbolSpec("G", "$G$", "expected free energy", "The policy-level objective used for action or policy selection in the bounded bridge."),
        SymbolSpec("F_star", "$\\mathcal{F}^*$", "reference bound minimum", "The variational free-energy value at the selected reference minimum."),
        SymbolSpec("Q", "$\\mathcal{Q}$", "variational family", "The family of approximate posteriors over which the variational objective is optimized."),
        SymbolSpec("q", "$q$", "variational posterior", "The approximate posterior distribution the system maintains."),
        SymbolSpec("p_true", "$p^*$", "target posterior", "The posterior distribution approached by the variational approximation at the selected minimum."),
        SymbolSpec("e", "$e_i$", "explanatory mode", "One of the four distinct Tinbergen explanatory modes."),
        SymbolSpec("R", "$R$", "scale recursion operator", "The operator mapping a settled system at one scale to the substrate at the next."),
        SymbolSpec("T", "$T$", "deterministic trace", "The finite authored sequence of conceptual states used for illustration."),
        SymbolSpec("sigma", "$\\sigma_i$", "formal trace state", "A named state in the deterministic illustrative trace."),
        SymbolSpec("delta", "$\\delta$", "deterministic transition", "The transition function that orders adjacent trace states without stochastic sampling."),
    )


def text_validation_checks() -> tuple[TextValidationCheck, ...]:
    return (
        TextValidationCheck(
            key="deterministic_simulation_boundary",
            surface="manuscript and analysis report",
            invariant="The project limits simulation language to a deterministic illustrative trace and rejects stochastic, empirical, synthetic-data, and performance claims.",
            evidence="SIMULATION_POLICY token, deterministic_simulation_manifest.json, and conceptual_analysis.json scope flags.",
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
            key="claim_grounding_closure",
            surface="formal grounding map",
            invariant="Every formal claim is grounded in at least one named source record used by the grounding map.",
            evidence="validate_claim_grounding() checks claim_grounding() against formal_claims().",
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
        ClaimDependency("fixed_point_stop", "blanket_achievement", "The fixed-point settlement supplies an organizational context for a bounded blanket model; it does not entail a literal biological boundary."),
        ClaimDependency("axis_partition", "explanatory_complementarity", "The axis partition shows the questions are complementary."),
        ClaimDependency("decomposition_caution", "niche_co_construction", "Joint structure and niche co-construction both resist factor-first readings."),
        ClaimDependency("blanket_achievement", "active_inference_bridge", "The achieved blanket provides the boundary within which active inference operates."),
        ClaimDependency("fixed_point_stop", "variational_closure", "The fixed-point settlement is represented as a relative variational-bound minimum."),
        ClaimDependency("active_inference_bridge", "scale_recurrence", "Active inference at one scale provides the substrate for the next."),
        ClaimDependency("variational_closure", "scale_recurrence", "The variational closure applies recursively at each scale."),
        ClaimDependency("explanatory_complementarity", "active_inference_bridge", "Complementarity of perspectives is preserved when action and perception are unified."),
        ClaimDependency("regress_shape", "deterministic_trace_boundary", "The trace records the regress shape before any termination claim is accepted."),
        ClaimDependency("deterministic_trace_boundary", "fixed_point_stop", "The trace boundary preserves the fixed-point stop as a conceptual category shift."),
    )


def claim_grounding() -> tuple[ClaimGrounding, ...]:
    return (
        ClaimGrounding("tinbergen_axes", "axis_partition"),
        ClaimGrounding("tinbergen_axes", "explanatory_complementarity"),
        ClaimGrounding("regress_shape", "regress_shape"),
        ClaimGrounding("regress_shape", "deterministic_trace_boundary"),
        ClaimGrounding("termination_moves", "selection_filter"),
        ClaimGrounding("termination_moves", "fixed_point_stop"),
        ClaimGrounding("joint_structure", "decomposition_caution"),
        ClaimGrounding("joint_structure", "active_inference_bridge"),
        ClaimGrounding("niche_blanket", "niche_co_construction"),
        ClaimGrounding("niche_blanket", "blanket_achievement"),
        ClaimGrounding("niche_blanket", "variational_closure"),
        ClaimGrounding("cross_scale_recurrence", "scale_recurrence"),
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


def validate_claim_grounding() -> tuple[str, ...]:
    errors: list[str] = []
    claim_keys = {claim.key for claim in formal_claims()}
    source_keys = {
        "tinbergen_axes",
        "regress_shape",
        "termination_moves",
        "joint_structure",
        "niche_blanket",
        "cross_scale_recurrence",
    }
    seen: set[tuple[str, str]] = set()
    for grounding in claim_grounding():
        edge = (grounding.source_record, grounding.claim_key)
        if edge in seen:
            errors.append(f"duplicate claim grounding {edge!r}")
        seen.add(edge)
        if grounding.source_record not in source_keys:
            errors.append(f"grounding source_record {grounding.source_record!r} is not a named source record")
        if grounding.claim_key not in claim_keys:
            errors.append(f"grounding claim_key {grounding.claim_key!r} not in formal claims")
    grounded_claims = {grounding.claim_key for grounding in claim_grounding()}
    missing_claims = sorted(claim_keys - grounded_claims)
    if missing_claims:
        errors.append(f"formal claims without source grounding: {', '.join(missing_claims)}")
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

    figure_keys = {spec.key for spec in figure_specs()}
    if figure_keys != set(_FIGURE_SECTION_BY_KEY):
        errors.append("figure section metadata does not cover figure specs")
    if figure_keys != set(_FIGURE_ALT_TEXT_BY_KEY):
        errors.append("figure alt-text metadata does not cover figure specs")
    for spec in figure_specs():
        if not spec.section:
            errors.append(f"figure {spec.key} has no section metadata")
        if not spec.alt_text:
            errors.append(f"figure {spec.key} has no alt-text metadata")

    errors.extend(validate_claim_dependencies())
    errors.extend(validate_claim_grounding())

    return tuple(errors)


def as_records(items: tuple[object, ...]) -> list[dict[str, object]]:
    return [asdict(item) for item in items]


def conceptual_integrity_token() -> str:
    payload = {
        "argument_modules": as_records(argument_modules()),
        "claim_dependencies": as_records(claim_dependencies()),
        "claim_grounding": as_records(claim_grounding()),
        "deterministic_simulation_trace": as_records(deterministic_simulation_trace()),
        "figures": as_records(figure_specs()),
        "formal_claims": as_records(formal_claims()),
        "quadrants": as_records(quadrant_grid()),
        "symbols": as_records(symbol_glossary()),
        "terminations": as_records(termination_catalog()),
        "validation_checks": as_records(text_validation_checks()),
    }
    blob = json.dumps(payload, ensure_ascii=True, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()[:16]
