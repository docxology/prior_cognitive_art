# Conceptual Method: Typed Explanations and Source-Owned Artifacts {#sec:method}

This is a conceptual paper. It includes one deterministic illustrative
simulation trace over authored formal states, but it uses no stochastic
simulation, no synthetic data, no empirical-effect estimate, and no numerical
performance claim. Its method is diagrammatic clarification: keep the
quadrants, regress types, trace states, and termination moves explicit enough
that the prose cannot silently trade one explanatory kind for another. The
methodological commitment is that the distinction between explanatory kinds —
proximate versus ultimate, static versus developmental — must be preserved
through every stage of the argument. When the distinction is lost, the regress
reappears as if it were forced by the framework, when in fact it is forced by a
category error: asking a developmental question to answer a static one.

The source layer records {{QUADRANT_COUNT}} Tinbergen quadrants,
{{TERMINATION_COUNT}} termination modes, {{ARGUMENT_MODULE_COUNT}} argument
modules, {{FIGURE_COUNT}} figure specifications, {{FORMAL_CLAIM_COUNT}} formal
claims, and {{SYMBOL_COUNT}} glossary rows. Those records are rendered into
visual artifacts, supplement formalisms, and manuscript variables during the
analysis stage. The visual inventory is deliberately partitioned: the atlas
contains {{VISUAL_ATLAS_FIGURE_COUNT}} argument diagrams, while the formal
supplement contains {{FORMAL_SUPPLEMENT_FIGURE_COUNT}} contract diagrams.

## Operational Protocol

The manuscript applies a compact five-step protocol to each "why" question:

1. **Type the request.** State whether the question concerns mechanism,
   function, ontogeny, phylogeny, or another explicitly named explanatory kind.
2. **Expose deferral.** Show whether the proposed answer merely moves the
   prior to a hyperprior, selector, or earlier developmental condition.
3. **Name the stop.** Identify pragmatic, selection, or fixed-point closure when
   one of those families does the relevant explanatory work; do not imply the
   list is exhaustive.
4. **State the ceiling.** Mark what the stop explains and what it leaves open,
   especially for Markov blankets, niche construction, and aesthetic analogy.
5. **Render and validate.** Generate the diagram and formal record from the
   source inventory, hydrate the prose, and reject stale or mismatched outputs.

This protocol is an accountability device, not a causal model or an empirical
estimator. It makes category changes visible before they become prose claims.

## Tinbergen Crossed With Prior Explanation

[@tbl:tinbergen_quadrants] lays out the crossed structure. Mechanism and
function are static: they can close locally by saying what a prior is doing now.
Ontogeny and phylogeny are developmental: they explain how a structure came to
be over time. The regress appears when a developmental answer is asked to serve
as the whole explanation.

| Question | Scale | Time-form | Prior question answered | Regress status |
|---|---|---|---|---|
{{QUADRANT_TABLE_ROWS}}

: Tinbergen quadrant map for prior explanation. {#tbl:tinbergen_quadrants}

The table makes the main constraint visible. Mechanism and function are static
in the relevant sense: they can close locally by saying what a prior is doing
now. Ontogeny and phylogeny are developmental: they explain how a structure came
to be over time. The regress appears when a developmental answer is asked to
serve as the whole explanation. This is why Bateson and Laland's update of
Tinbergen's framework matters: they show that the four questions are
complementary, not competing, and that conflation among them is the source of
persistent confusion in ethology and beyond [@bateson2004toward]. Bergman and
Beehner's cause/consequence leveling is useful because it shows the framework
can be reorganized without losing the need for explanatory distinctions
[@bergman2022leveling]. The same conflation arises when "why is there a prior?"
is answered by only naming a developmental channel. Konner's nine-level
proposal is useful here as a cautionary extension rather than as a replacement:
one can split Tinbergen's questions into finer levels, but this paper depends
only on preserving the kinds of explanation they name [@konner2021nine]. The category-theoretic
distinction between explanatory kinds is not merely terminological: it tracks a
real difference in what an explanation is being asked to do [@smith2000formal;
@godfrey2013theoretical].

## Regress-Closure Strategies

{{TERMINATION_BULLETS}}

These are closure strategies rather than three proofs that one metaphysical
question has been answered. The first move, pragmatic termination, is the standard move in applied
Bayesian statistics: install a weakly informative, reference, or penalized
complexity prior and then test whether the model is adequate for the task
[@gelman2013philosophy; @simpson2017penalising]. It is epistemically honest
about its own limitation: prior predictive checks, posterior predictive checks,
and sensitivity analysis regularize inference without claiming to discover the
origin of the prior. The second move, selection termination, treats the prior as
the surviving form after viability filtering by function and phylogeny
[@friston2015free; @constant2018free]. It explains persistence without
explaining fine structure.
The third move, fixed-point termination, is the most interesting for cognitive
science because it changes the grammar of the question. Instead of asking for a
prior behind the prior, it asks whether the persisting organization of the
system is what the term "prior" was naming.

That is why the free energy principle and Markov blanket self-individuation
matter here [@friston2010free; @ramstead2018answering; @kirchhoff2018markov].
When the Markov blanket is treated as a model-level boundary tied to the
system's self-maintaining dynamics, the prior-like structure becomes a bounded
description of organization rather than a parameter received from a higher
level [@constant2018free; @hohwy2016self]. The critique literature matters
because it blocks an overclaim: the notation does not by itself identify a
literal organism boundary, so the fixed-point move must be stated as a bounded
modeling claim, not a metaphysical shortcut [@bruineberg2022emperor;
@raja2021markov]. The system does not have a prior in the way it has a property;
it persists as the organization that makes prior-like constraint legible.

## Before The First Prior

The first-principles version of the problem asks what is upstream of the first
inferential prior. This paper answers by refusing to treat "before" as another
level in a Bayesian hierarchy. A prior-before-priors would only duplicate the
hyperprior regress. The upstream layer has to be a different explanatory kind:
viability constraints, regulatory asymmetries, embodied support, and
developmental scaffolding that make expectation-forming possible before the
organism can own an explicit prior.

This move draws on four adjacent literatures. Interoceptive predictive
processing treats the body as a first prior for self-modeling, which shifts the
origin question from detached belief to regulatory bodily organization
[@allen2018body_first_prior]. Early-life co-embodiment and co-homeostasis work
pushes farther upstream: bodily regulation is initially shared with caregivers
and environments rather than privately possessed [@ciaunica2021first_prior].
Allostasis names predictive regulation as a core physiological pattern, while
recent developmental work on rhythmic visceral dynamics describes how bodily
regularities can teach early cognition before explicit conceptual learning
[@sterling2012allostasis; @corcoran2025body_first_teacher]. Finally,
morphogenesis and evolutionary active-inference accounts suggest that
constraint histories can be biological and architectural before they are
cognitive in the narrow sense [@kuchling2020morphogenesis;
@pezzulo2022evolution; @linson2018active_ecological].

The RedTeam boundary is therefore strict. These sources license an upstream
constraint stack, not a literal first-prior discovery. "Bias before bias" means
asymmetry before inference: some forms are viable, regulatable, shareable, and
developmentally reachable before they are available as priors in a model.
[@fig:first_prior_grounding_stack] renders that distinction as a visual
constraint stack.

## The Role of Niche Construction

The niche-construction reading of the free energy principle deepens the
selection-termination move. Foundational niche-construction theory argues that
organisms modify the selection pressures they and their descendants face, and
that cultural practices can participate in that feedback
[@laland2000niche; @odling_smee2003niche]. Constant and colleagues add the
variational version: organisms actively structure their niche, and the niche
structures them back, so that the statistical regularities exploited by the
organism are partly of its own making [@constant2018free;
@baltieri2022extended]. Developmental niche construction adds an important
boundary: the constructed environment does not only select among ready-made
forms; it also helps produce developmental variation and transmit resources
across generations [@stotz2017developmental]. This does not eliminate
selection — viability still filters what can persist — but it shows that the
filter is not purely external. The prior-like structure is co-shaped by the
system and its environment. This complicates the selection-termination move
without changing its logical role: it still blocks regress by naming what
persists rather than by adding another hidden level. The visual atlas in
[@sec:visual-atlas] renders this co-shaping diagrammatically.

## Active Inference and Variational Closure

Active inference extends the free energy principle to action and policy
selection [@friston2012agency; @friston2015active; @da_costa2020active;
@friston2017active].
Extended active-inference work makes the same point at the organism-niche
surface: action changes the sensory and material field in which future
inference occurs [@baltieri2022extended]. The prior serves a coupled
perception-action process, but the objectives must not be collapsed:
variational free energy evaluates an approximate posterior, whereas expected
free energy evaluates policies. This closes the explanatory loop without
claiming that inference and policy selection are the same optimization problem.
The variational free energy bounds negative log evidence from above, or
equivalently tightens the evidence lower bound as the approximate posterior
approaches the target posterior within its variational family
[@blei2017variational]. In this paper that formal fact is used narrowly: it
supports a model-internal settling interpretation of prior-like constraint, not
a claim that free energy literally vanishes or that variational inference has
derived the historical origin of the prior [@friston2019free;
@friston2023simpler; @da_costa2023bayesian; @bowers2012bayesian].

The same boundary applies to epistemic value. Active inference can model
information-seeking policies and uncertainty reduction [@friston2015active;
@parr2022active], but epistemic value is not aesthetic value. When the paper
uses aesthetic scholarship, it treats art as a field of staged expectation,
ambiguity, affect, and meaning, not as a proof that aesthetic worth is just
expected free-energy minimization [@van_de_cruys2024order;
@frascaroli2024aesthetics; @burnett2020four_e].

## Aesthetic Prior-Craft As A Bounded Analogy

Predictive-processing aesthetics offers the paper its title discipline. Visual
art, music, and aesthetic experience often involve learned regularities,
expectation, prediction error, affect, and meaning-making
[@van_de_cruys2011putting; @kesner2014predictive; @pearce2018statistical;
@starr2023aesthetic]. Those sources make it legitimate to say that artworks can
arrange encounters with priors: a painting, musical style, performance, or
conceptual work can build expectations, violate or loosen them, and invite a
viewer or listener to recover structure at another level. Neuroaesthetics adds
a useful triad of sensory-motor, emotion-valuation, and meaning-knowledge
systems, which keeps the account from reducing art to low-level perceptual
surprise [@chatterjee2014neuroaesthetics; @pearce2016neuroaesthetics].

The analogy becomes stronger, and safer, when art is treated as material
practice rather than as perception alone. Dewey's art-as-experience frame,
Noe's "strange tools" account, extended-mind theory, and material-engagement
archaeology all support a view in which artworks and art-making are public,
embodied, and artifact-mediated ways of reorganizing attention and action
[@dewey1934art; @noe2015strange; @clark1998extended;
@malafouris2013things; @malafouris2019mind; @wynn2021four_e]. Recent material-engagement work on
art and chance sharpens this point: making is not merely the execution of an
inner plan but an encounter with affordances, accidents, and media that can
change what counts as the next relevant move [@march2023art;
@malafouris2023enactychism]. In the paper's terms, the artwork is not a hidden
predictive model; it is a crafted environment in which prior-like expectations
are exposed, perturbed, and made legible. [@fig:aesthetic_prior_craft_map]
summarizes this source-to-claim boundary.

That analogy is deliberately bounded. Predictive processing is a fruitful lens
for expectation and ambiguity in aesthetic experience, not a master theory of
art. Enactive and 4E accounts emphasize that artworks are embodied,
sociomaterial practices and affordance fields, while neuroaesthetic critics warn
that the arts exceed narrow aesthetic preference or neural reward
[@rietveld2014rich; @burnett2020four_e; @brown2009arts]. Predictive accounts
of imagination and enactive accounts of surprise add the same caution from
another angle: prediction can illuminate imaginative perception and
improvisation, but it should not erase the difference between controlled
imagining, embodied discovery, and aesthetic practice [@jones2020prediction;
@cavedon_taylor2022predictive; @gallagher2022surprise]. The manuscript
therefore treats "prior cognitive art" as the craft of arranging explanatory
encounters with priors, not as a mechanism claim about artists' intentions,
viewers' neural updating, or imagination as prediction alone.

## Scale Recurrence

The regress-termination problem recurs at multiple scales. The fixed-point move
applies at each scale without requiring a new hidden prior: the prior-like
settlement at one scale becomes the substrate for the next. This recurrence is
a structural analogy, not a claim of scale invariance or empirical
self-similarity. Three concrete instances make the recurrence precise.

At the **cellular** level, the Markov blanket of a single cell is a prior-like
model of molecular organization: the cell maintains exchange statistics that
can be represented as a boundary process rather than received from a higher
level [@friston2013life; @kirchhoff2018markov; @bruineberg2022emperor]. At the
**organismic** level, the nervous system maintains prior-like constraints that
guide perception and action; the brain-body system is modeled as maintaining
its own action-perception boundary rather than being handed one from outside
[@friston2010free; @hohwy2016self; @maturana1980autopoiesis]. At the
**social** level, cultural practices and shared models function as prior-like
structures that organize collective behavior, and those practices are themselves
steady states of a population rather than externally supplied rules
[@constant2018free; @ramstead2023encultured]. In each case the same move
terminates the regress: identify the persisting organization rather than posit a selector behind it. The
fixed-point structure $X^*_k = \Phi(X^*_k)$ recurs, and the scale recursion
operator $R$ carries the settlement from one level to the substrate of the next
without introducing a new explanatory kind.

## Formal Supplement Protocol

The supplement uses generated numbering rather than hand-maintained labels. Each
formal claim is derived from source records, and every project-specific symbol in
those claims must appear in the generated glossary table. This gives the text a
lightweight integrity surface: if the formal notation and glossary drift apart,
the source contract fails before render. The contract is deliberately small — {{FORMAL_CLAIM_COUNT}} claims, one glossary of
{{SYMBOL_COUNT}} rows, {{TEXT_VALIDATION_COUNT}} validation checks — because the point is not to
build a formal model but to make drift detectable.
