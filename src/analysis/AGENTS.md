# src/analysis/ AGENTS

Agent-facing notes for the analysis stage workflow.

- `workflow.py` performs deterministic output generation for the template
  analysis stage: reports and figures derived from
  `src/conceptual_model.py`. `__init__.py` is the package marker.
- Invoke via `scripts/optimization_analysis.py` or the template
  pipeline's analysis stage; all artifacts land under `output/`.
- Keep this layer deterministic: no stochastic experiments, empirical
  estimators, or performance numbers. Import the conceptual model, never
  duplicate its records.
- New derived outputs belong in `output/` and must be referenced from the
  manuscript as `../output/...` paths.

See `../../AGENTS.md` (project root) for the project contract; each
parent directory's `AGENTS.md` above adds local context.
