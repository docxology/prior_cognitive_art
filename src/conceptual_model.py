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
            title="Only three endings are live",
            claim=(
                "The regress stops pragmatically, by selection, or by a fixed-point "
                "shift in which the system is the prior-like settlement."
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
            claim="Active inference treats action and perception as two aspects of the same free-energy-minimizing process, which closes the explanatory loop the prior was meant to serve.",
        ),
        ArgumentModule(
            key="scale_invariance_of_priors",
            title="Prior-like structure appears at multiple scales",
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
    return (
        FigureSpec(
            key="tinbergen_axes",
            filename="tinbergen_axes.png",
            title="Tinbergen axes for priors",
            purpose="Stage the crossed explanatory axes as a reading surface for prior-origin questions.",
            caption=(
                "Four colored panels hold Tinbergen's questions in tension rather than stacking "
                "them into a causal ladder. Read across scale and then down temporality: mechanism "
                "and function can close local questions, while ontogeny and phylogeny ask how the "
                "form was shaped and retained. The regress appears when one panel, usually "
                "ontogeny, is asked to speak for the whole grid."
            ),
        ),
        FigureSpec(
            key="regress_terminations",
            filename="regress_terminations.png",
            title="Where the hyperprior regress can stop",
            purpose="Set the repeating hyperprior chain against the three legitimate stopping moves.",
            caption=(
                "The upper chain is deliberately too easy to extend: a prior receives a hyperprior, "
                "then that hyperprior seems to need its own warrant. The lower register names the "
                "three different ways the picture can stop without pretending the next box solves "
                "the problem. Pragmatic, selection, and fixed-point endings are visualized as "
                "explanatory disciplines, not as empirical discoveries of prior origins."
            ),
        ),
        FigureSpec(
            key="prior_equilibrium_map",
            filename="prior_equilibrium_map.png",
            title="Prior as settled organization",
            purpose="Present the fixed-point move as a loop of maintenance rather than a higher cause.",
            caption=(
                "The circular composition makes the fixed-point move visible: the prior is not "
                "another hidden object above the system, but the settled organization of the "
                "system's own process. Blanket persistence, action-perception closure, and "
                "environmental viability feed back into the same maintained form. The claim is a "
                "category shift about what is being explained, not a numerical equilibrium result."
            ),
        ),
        FigureSpec(
            key="ontogeny_hyperprior_parallel",
            filename="ontogeny_hyperprior_parallel.png",
            title="Ontogeny and hyperpriors share a regress shape",
            purpose="Pair developmental deferral with hyperprior deferral to expose their shared silhouette.",
            caption=(
                "The two horizontal chains are drawn as visual echoes. A Bayesian hyperprior and "
                "an ontogenetic selector are not the same biological claim, but both can defer the "
                "question to the source that licensed the current prior. The red bracket marks "
                "that shared silhouette of deferral while preserving the difference between "
                "formal hierarchy and developmental history."
            ),
        ),
        FigureSpec(
            key="selection_filter",
            filename="selection_filter.png",
            title="Selection as regress blocker",
            purpose="Turn function and phylogeny into a filter that explains persistence without another selector.",
            caption=(
                "Candidate prior-like forms enter as a rough population, not as equal explanatory "
                "successes. The function-plus-phylogeny funnel removes forms that cannot remain "
                "available as persisting targets: fragile, miscalibrated, or overfit structures "
                "drop out of the story. Selection blocks regress by explaining availability "
                "through viability rather than placing one more selector behind the filter."
            ),
        ),
        FigureSpec(
            key="policy_entanglement_bridge",
            filename="policy_entanglement_bridge.png",
            title="Joint structure before decomposition",
            purpose="Frame lambda-decomposition as an analytic cut through prior joint organization.",
            caption=(
                "The large joint form on the left is intentionally prior to the separated boxes on "
                "the right. Lambda-decomposition makes policy, prior-like constraint, and state "
                "factor legible after the analytic cut, but it does not prove that those factors "
                "were ontologically first. The bridge keeps the argument focused on how cleaned-up "
                "factors are extracted from an already organized field."
            ),
        ),
        FigureSpec(
            key="formal_claim_dependency_map",
            filename="formal_claim_dependency_map.png",
            title="Formal claim dependency map",
            purpose="Make the formal supplement look like a source-derived map, not decorative theorem labels.",
            caption=(
                "The map turns the formal supplement into a provenance surface. Claims F1-F12 are "
                "not decorative theorem labels; they are routed views over source records for axes, "
                "regress shape, termination moves, joint structure, niche, blanket, complementarity, "
                "and trace boundaries. Numbering follows source order, so prose, figures, and "
                "formal labels have to move together."
            ),
        ),
        FigureSpec(
            key="symbol_glossary_closure",
            filename="symbol_glossary_closure.png",
            title="Symbol glossary closure",
            purpose="Treat notation as a closure surface where every mark must be accounted for.",
            caption=(
                "The paired panels make a simple editorial demand: every formal mark used by a "
                "claim must be defined, and every definition must be used. This turns notation "
                "from ornament into an accountable surface of the manuscript. If the two sides "
                "fall out of correspondence, the package fails before render."
            ),
        ),
        FigureSpec(
            key="text_validation_ladder",
            filename="text_validation_ladder.png",
            title="Text validation ladder",
            purpose="Stack source, generation, rendering, and validation as a single manuscript-making ladder.",
            caption=(
                "The ladder treats the paper as something made, not merely written. Source records "
                "hydrate reports, figures, tokens, and render surfaces; validation then climbs the "
                "same stack after generation. A drifting caption, registry row, or prose token is "
                "therefore not a minor typo but a contract error in the artifact pipeline."
            ),
        ),
        FigureSpec(
            key="niche_construction_diagram",
            filename="niche_construction_diagram.png",
            title="Niche construction: organism-environment co-shaping of the prior",
            purpose="Paint prior formation as reciprocal organism-niche work rather than one-way inheritance.",
            caption=(
                "The central prior is drawn between organism and niche because neither side owns "
                "the explanation alone. Organisms act into environments that answer back as altered "
                "regularities, affordances, and selection pressures. Viability still filters what "
                "persists, but the filter is partly made by the organism-niche loop it later "
                "appears to judge."
            ),
        ),
        FigureSpec(
            key="markov_blanket_achievement",
            filename="markov_blanket_achievement.png",
            title="Markov blanket as model-bound achievement",
            purpose="Draw the blanket as an achieved model boundary with explicit ontological restraint.",
            caption=(
                "The boundary is deliberately drawn as something achieved by the model's settled "
                "organization, not as a line simply read off the world. The blanket can organize "
                "conditional-dependence claims inside an active-inference account, but it does not "
                "automatically become a literal organismal or cognitive border. The image keeps "
                "formal usefulness and ontological restraint in the same frame."
            ),
        ),
        FigureSpec(
            key="explanatory_complementarity_matrix",
            filename="explanatory_complementarity_matrix.png",
            title="Tinbergen questions are complementary, not rival",
            purpose="Turn Tinbergen's questions into a coordination matrix instead of a rivalry table.",
            caption=(
                "The matrix lets each Tinbergen question meet the others without being absorbed by "
                "them. Diagonal cells name each explanatory mode; off-diagonal cells mark places "
                "where coordination is legitimate but reduction is not. The regress is not caused "
                "by asking several questions. It is caused by collapsing their different jobs into "
                "one overburdened answer."
            ),
        ),
        FigureSpec(
            key="active_inference_cycle",
            filename="active_inference_cycle.png",
            title="Active inference action-perception cycle",
            purpose="Show action and perception as one circular practice served by prior-like structure.",
            caption=(
                "The loop makes active inference a practice rather than a passive estimate. "
                "Perception, inference, action, and policy selection keep returning into one "
                "another under a generative model. Prior-like structure serves that circular "
                "organization: it is a constraint in an action-perception loop, not merely a static "
                "number placed before observation."
            ),
        ),
        FigureSpec(
            key="variational_free_energy_landscape",
            filename="variational_free_energy_landscape.png",
            title="Variational bound landscape",
            purpose="Use a basin image for relative variational settlement without implying zero free energy.",
            caption=(
                "The basin is a picture of relative settlement inside a model, not a claim that "
                "free energy literally falls to zero. The marked path shows an approximate "
                "posterior moving toward a target posterior under a tractable bound. The figure "
                "supports a bounded settling metaphor for prior-like constraint while refusing an "
                "empirical origin story for priors."
            ),
        ),
        FigureSpec(
            key="deterministic_simulation_trace",
            filename="deterministic_simulation_trace.png",
            title="Deterministic simulation trace",
            purpose="Present the authored state sequence as a conceptual trace, not simulation evidence.",
            caption=(
                "The trace borrows the visual grammar of a state diagram while staying inside the "
                "paper's conceptual scope. Each node is an authored formal state: question, "
                "regress, Tinbergen partition, termination choice, and fixed-point settlement. "
                "The arrows record argumentative order only; the invariants block stochastic, "
                "synthetic-data, performance, or effect-size readings."
            ),
        ),
        FigureSpec(
            key="scale_invariance_diagram",
            filename="scale_invariance_diagram.png",
            title="Scale invariance of prior-like structure",
            purpose="Repeat the fixed-point grammar across scales while keeping the recurrence conceptual.",
            caption=(
                "The three panels repeat the fixed-point grammar at cellular, organismic, and "
                "social registers. A prior-like settlement at one scale can become substrate for "
                "another through R, but the image does not smuggle in a new hidden prior at each "
                "transition. It shows recurrence of an explanatory problem, not scale-free "
                "empirical proof."
            ),
        ),
        FigureSpec(
            key="source_claim_boundary_map",
            filename="source_claim_boundary_map.png",
            title="Source-to-claim boundary map",
            purpose="Make scholarship promotion visibly pass through verification and claim-boundary gates.",
            caption=(
                "The map makes citation discipline part of the artwork of the paper. Discovery "
                "candidates do not flow directly into prose; they pass through verification and "
                "claim-ledger boundaries before reaching manuscript claims, formal inventory, or "
                "visual atlas. Rejected and deferred sources stay visible so scholarship does not "
                "become unbounded accumulation."
            ),
        ),
        FigureSpec(
            key="aesthetic_prior_craft_map",
            filename="aesthetic_prior_craft_map.png",
            title="Aesthetic prior-craft map",
            purpose="Locate prior-craft between predictive aesthetics, 4E practice, and claim restraint.",
            caption=(
                "This figure is the paper's most self-conscious art claim. Predictive aesthetics, "
                "4E/material engagement, and neuroaesthetic scope converge on prior-craft: artworks "
                "can stage encounters with expectation, ambiguity, affordance, affect, and meaning. "
                "The red ceiling matters as much as the purple center: this is not a total theory "
                "of art, intention, culture, or neural updating."
            ),
        ),
        FigureSpec(
            key="markov_blanket_scope_split",
            filename="markov_blanket_scope_split.png",
            title="Markov blanket scope split",
            purpose="Separate formal blanket use from stronger organism-boundary commitments.",
            caption=(
                "The split makes three registers visible before they can be collapsed: a "
                "conditional-independence structure, an active-inference model boundary, and a "
                "realized biological or cognitive boundary. The first two support the paper's "
                "model-level argument. The third requires additional dynamical and philosophical "
                "premises, so it is held behind an explicit boundary condition."
            ),
        ),
        FigureSpec(
            key="niche_prior_feedback_field",
            filename="niche_prior_feedback_field.png",
            title="Niche-prior feedback field",
            purpose="Layer organismal, developmental, and cultural feedback as one prior-stabilizing field.",
            caption=(
                "The field layers fast organismal action, slower developmental resources, and "
                "still slower cultural inheritance. Prior-like structure stabilizes through the "
                "recurrence among these bands, including material and cultural scaffolds, rather "
                "than arriving from organism or environment alone. The field constrains selection "
                "termination without becoming a fourth stopping rule."
            ),
        ),
        FigureSpec(
            key="first_prior_grounding_stack",
            filename="first_prior_grounding_stack.png",
            title="Before the first prior",
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
                "prior-before-priors."
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
            expression="$\\mathcal{F}(q)-\\mathcal{F}^* = D_{KL}(q\\|p^*) \\ge 0$; at the variational minimum $q = p^*$.",
            reading=(
                "The variational free-energy bound tightens as the approximate posterior $q$ "
                "approaches the target posterior $p^*$. This supports a bounded, model-internal "
                "settling interpretation of prior-like constraint; it is not a literal zero-energy "
                "claim and it does not derive the historical origin of the prior."
            ),
            symbol_keys=("F", "F_star", "q", "p_true", "P"),
        ),
        FormalClaim(
            key="scale_invariance",
            title="Scale invariance",
            expression="$R_k(X^*_k) = X^*_{k+1}$ for scales $k \\in \\{\\text{cell}, \\text{organism}, \\text{social}\\}$.",
            reading="The fixed-point termination recurs at each scale: the prior-like settlement at one scale becomes the substrate for the next. No new hidden prior is needed; the same category shift applies recursively.",
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
        SymbolSpec("F_star", "$\\mathcal{F}^*$", "reference bound minimum", "The variational free-energy value at the selected reference minimum."),
        SymbolSpec("q", "$q$", "variational posterior", "The approximate posterior distribution the system maintains."),
        SymbolSpec("p_true", "$p^*$", "target posterior", "The posterior distribution approached by the variational approximation at the selected minimum."),
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
        ClaimDependency("fixed_point_stop", "variational_closure", "The fixed-point settlement is represented as a relative variational-bound minimum."),
        ClaimDependency("active_inference_bridge", "scale_invariance", "Active inference at one scale provides the substrate for the next."),
        ClaimDependency("variational_closure", "scale_invariance", "The variational closure applies recursively at each scale."),
        ClaimDependency("explanatory_complementarity", "active_inference_bridge", "Complementarity of perspectives is preserved when action and perception are unified."),
        ClaimDependency("regress_shape", "deterministic_trace_boundary", "The trace records the regress shape before any termination claim is accepted."),
        ClaimDependency("deterministic_trace_boundary", "fixed_point_stop", "The trace boundary preserves the fixed-point stop as a conceptual category shift."),
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
