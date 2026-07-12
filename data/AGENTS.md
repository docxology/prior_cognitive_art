# data/ AGENTS

Keep generated artifacts out of `data/`. The only maintained input right now is
`claim_ledger.yaml`; analysis outputs belong under `output/`.

## claim_ledger.yaml

The claim ledger tracks every conceptual and local-invariant claim in the
manuscript. Each entry has:

- `claim_id` — unique identifier
- `kind` — `conceptual-framing` or `local-invariant`
- `value` — the claim text
- `source` — the source reference or artifact
- `source_tier` — `scholarly`, `project-contract`, or `source`
- `freshness` — `stable` or `current`
- `artifact_path` — path to the source artifact

The ledger currently has 24 entries covering the Tinbergen crossed-axes framing,
the no-simulation boundary, the three termination moves, the formal symbol
closure, the generated integrity token, the regress-shape parallel, the
selection filter, the fixed-point category shift, the decomposition caution,
niche co-construction, blanket achievement, explanatory complementarity,
claim dependency closure, active inference bridge, variational closure, and
scale recurrence, plus the bounded art and upstream-first-prior additions.
