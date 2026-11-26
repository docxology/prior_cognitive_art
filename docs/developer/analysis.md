# src/analysis/

Analysis stage workflow for the Prior Cognitive Art project.

| Module | Role |
|---|---|
| `workflow.py` | Deterministic output generation for the template analysis stage (reports and figures derived from `src/conceptual_model.py`) |
| `__init__.py` | Package marker |

Run via the project analysis script or the template pipeline's analysis
stage. All artifacts are written under `output/`; nothing here is
stochastic or empirical.
