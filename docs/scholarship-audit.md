# Scholarship Audit

Date: 2026-07-07

This audit records the publication-readiness scholarship decisions for a
simulation-free conceptual manuscript. Sources were promoted only when they
directly changed claim boundaries, formal inventory, prose, or figure contracts.
A high-depth Perplexity synthesis query timed out; the work was split into
targeted Markov blanket, niche construction, hyperprior, active-inference, and
Tinbergen/Konner checks and then verified against direct bibliographic records
where available.

## Accepted Sources

| Key | Use in paper | Verification note |
| --- | --- | --- |
| `bruineberg2022emperor` | Reframes Markov blankets as formal/model-level structures and blocks a metaphysical boundary reading. | [Cambridge Core](https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/article/emperors-new-markov-blankets/715C589A73DDF861DCF8997271DE0B8C) verifies title, journal, DOI `10.1017/S0140525X21002351`, and the critique of metaphysical Markov blanket use. |
| `raja2021markov` | Adds scope pressure on free-energy/active-inference uses of the Markov blanket. | [PubMed](https://pubmed.ncbi.nlm.nih.gov/34563472/) and journal metadata verify DOI `10.1016/j.plrev.2021.09.001`; used as a boundary source, not as a premise for rejecting active inference. |
| `stotz2017developmental` | Separates developmental niche construction from selective niche construction, preventing the niche section from becoming a fourth termination mode. | [Macquarie institutional record](https://researchers.mq.edu.au/en/publications/why-developmental-niche-construction-is-not-selective-niche-const/) verifies Interface Focus 7(5), article `20160157`, DOI `10.1098/rsfs.2016.0157`. |
| `baltieri2022extended` | Supports extended active inference as an organism-environment construction frame. | [PubMed Central](https://pmc.ncbi.nlm.nih.gov/articles/PMC9292365/) and journal metadata verify Mind & Language publication and DOI `10.1111/mila.12330`. |
| `simpson2017penalising` | Grounds the hyperprior stop in penalized-complexity prior practice, alongside weakly informative and reference priors. | [Project Euclid](https://projecteuclid.org/journals/statistical-science/volume-32/issue-1/Penalising-Model-Component-Complexity-A-Principled-Practical-Approach-to-Constructing/10.1214/16-STS576.full) / arXiv metadata verifies Statistical Science 32(1), 1-28, DOI `10.1214/16-STS576`. |
| `konner2021nine` | Extends the Tinbergen-level discussion cautiously beyond four explanatory levels without changing the paper's core two-axis decomposition. | [PubMed](https://pubmed.ncbi.nlm.nih.gov/34739657/) / Springer metadata verifies Human Nature 32(4), 748-793, DOI `10.1007/s12110-021-09414-8`. |

## Existing Sources Reused With Sharper Boundaries

| Key | Boundary |
| --- | --- |
| `tinbergen1963aims` | Kept as the canonical explanatory-level anchor. Konner is used as an extension, not a replacement. |
| `mayr1961cause` | Retained for proximate/ultimate framing. |
| `friston2010freeenergy` and `ramstead2018answering` | Active inference and Markov blanket language is now bounded by the critique literature. |
| `constant2018extended` | Kept for extended active inference and niche construction; strengthened with Baltieri and Stotz. |
| `gelman2006data` and `bernardo1979reference` | Kept as pragmatic/reference-prior anchors; Simpson adds the PC-prior version of the same stop. |
| `maturana1980autopoiesis`, `varela1991embodied`, and `thompson2007mind` | Kept for autopoiesis/enactive closure. No new closure claim was added beyond the already bounded conceptual role. |
| `ramstead2023encultured` | Retained for cultural prior transmission and scale invariance. |

## Rejected or deferred sources

| Source family | Decision |
| --- | --- |
| Social/normative-prior expansion literature | Deferred. It would broaden the paper toward social epistemology rather than sharpening the current prior-termination argument. |
| Additional Markov blanket critique responses beyond Bruineberg/Raja | Deferred. The accepted pair is enough to bound the claim without turning the paper into a literature review of the controversy. |
| Empirical active-inference applications | Rejected for this pass. The manuscript contract is conceptual and simulation-free, so empirical performance examples would create an unsupported evidential layer. |
| New stochastic or numerical attractor/landscape sources | Rejected for this pass. Fixed-point and attractor language remains deterministic and conceptual; no quantitative dynamical claim is introduced. |
| Treating developmental niche construction as a fourth termination type | Rejected. The accepted literature supports a constraint on termination, not a new stop in the formal inventory. |

## Manuscript Changes Driven by the Audit

- Markov blanket prose now distinguishes model-level conditional-independence
  structure, realized organism-environment coupling, and critique boundaries.
- Niche construction prose now names the developmental/selective distinction and
  extended-active-inference role without promoting a fourth termination mode.
- Hyperprior prose now treats stopping as pragmatic modeling discipline rather
  than a proof that regress has disappeared.
- Tinbergen/Konner prose now presents Konner as a cautious extension of
  explanatory-level pluralism.
- Three deterministic figures were added to make these boundaries visible:
  `source_claim_boundary_map`, `markov_blanket_scope_split`, and
  `niche_prior_feedback_field`.
