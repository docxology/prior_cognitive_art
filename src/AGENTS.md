# src/ AGENTS

Keep this layer importable and deterministic. Store conceptual records in
`conceptual_model.py`, visualization rendering in `figures/`, and manuscript
variable construction in `manuscript_variables.py`.

Subfolders: `figures/` (figure modules; see `figures/AGENTS.md`) and
`analysis/` (deterministic analysis workflow; see `analysis/AGENTS.md`).

Do not add stochastic simulations, empirical estimators, performance benchmarks,
or infrastructure imports to the conceptual model. The only simulation-named
record is the deterministic illustrative trace in `conceptual_model.py`.
