# src/

This package contains the conceptual inventory, visualization builders, and
manuscript hydration logic for the Prior Cognitive Art project.

| Module | Role |
|---|---|
| `conceptual_model.py` | Static argument and figure inventory, formal claims, symbol glossary, text-validation checks, integrity token |
| `figures/conceptual.py` | Public figure-generation orchestrator and stable import surface |
| `figures/_*_figures.py` | Deterministic matplotlib visualization builders split by responsibility (21 figures total) |
| `figures/_shared.py` | Shared semantic palette, drawing helpers, and save routine |
| `analysis/workflow.py` | Output generation for the template analysis stage |
| `manuscript_variables.py` | Token hydration from conceptual inventory and config |
| `documentation.py` | API reference markdown generation |
| `project_paths.py` | Path resolution for project root and output directories |
| `_runtime.py` | Infrastructure-aware logger and project root helpers |

All modules are importable without running scripts. Do not add stochastic
simulations, empirical estimators, synthetic-data experiments, performance
benchmarks, or infrastructure imports to the conceptual model.
