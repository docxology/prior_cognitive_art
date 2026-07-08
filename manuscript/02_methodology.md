# Conceptual Method {#sec:method}

This is a conceptual paper. It uses no simulations, no synthetic data, and no
numerical performance claims. Its method is diagrammatic clarification: keep the
quadrants, regress types, and termination moves explicit enough that the prose
cannot silently trade one explanatory kind for another. The methodological
commitment is that the distinction between explanatory kinds — proximate versus
ultimate, static versus developmental — must be preserved through every stage
of the argument. When the distinction is lost, the regress reappears as if it
were forced by the framework, when in fact it is forced by a category error:
asking a developmental question to answer a static one.

The source layer records {{QUADRANT_COUNT}} Tinbergen quadrants,
{{TERMINATION_COUNT}} termination modes, {{ARGUMENT_MODULE_COUNT}} argument
modules, {{FIGURE_COUNT}} figure specifications, {{FORMAL_CLAIM_COUNT}} formal
claims, and {{SYMBOL_COUNT}} glossary rows. Those records are rendered into
visual artifacts, supplement formalisms, and manuscript variables during the
analysis stage.

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
persistent confusion in ethology and beyond [@bateson2004toward]. The same
conflation arises when "why is there a prior?" is answered by only naming a
developmental channel. Konner's nine-level proposal is useful here as a
cautionary extension rather than as a replacement: one can split Tinbergen's
questions into finer levels, but this paper depends only on preserving the
kinds of explanation they name [@konner2021nine]. The category-theoretic
distinction between explanatory kinds is not merely terminological: it tracks a
real difference in what an explanation is being asked to do [@smith2000formal;
@godfrey2013theoretical].

## Termination Candidates

{{TERMINATION_BULLETS}}

The first move, pragmatic termination, is the standard move in applied
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

## The Role of Niche Construction

The niche-construction reading of the free energy principle deepens the
selection-termination move. Constant and colleagues argue that organisms actively
structure their niche, and the niche structures them back, so that the
statistical regularities exploited by the organism are partly of its own making
[@constant2018free; @baltieri2022extended]. Developmental niche construction
adds an important boundary: the constructed environment does not only select
among ready-made forms; it also helps produce developmental variation and
transmit resources across generations [@stotz2017developmental]. This does not
eliminate selection — viability still filters what can persist — but it shows
that the filter is not purely external. The prior-like structure is co-shaped by
the system and its environment. This complicates the selection-termination move
without changing its logical role: it still blocks regress by naming what
persists rather than by adding another hidden level. The visual atlas in
[@sec:visual-atlas] renders this co-shaping diagrammatically.

## Active Inference and Variational Closure

Active inference extends the free energy principle to action and policy
selection [@friston2015active; @da_costa2020active; @friston2017active].
Extended active-inference work makes the same point at the organism-niche
surface: action changes the sensory and material field in which future
inference occurs [@baltieri2022extended]. The prior serves a process that
minimizes variational free energy through both inference and action, not
inference alone. This closes the explanatory loop: the prior is not merely a
parameter for belief updating but a constraint on the coupled perception-action
system. The variational free energy bounds the
negative log evidence from above [@blei2017variational], and the prior-like
structure is the settling point of this bound — not an external parameter but
the system's own inference achieving its minimum
[@friston2019free; @da_costa2023bayesian]. The zero-energy limit, where the
variational posterior equals the true posterior, anchors the prior to the
system's own inferential process rather than to an externally supplied
distribution [@parr2020prefrontal].

## Scale Invariance

The regress-termination problem recurs at multiple scales. The fixed-point move
applies at each scale without requiring a new hidden prior: the prior-like
settlement at one scale becomes the substrate for the next. This scale
invariance is a structural consequence of the fixed-point termination, not a
separate empirical claim. Three concrete instances make the recurrence precise.

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
