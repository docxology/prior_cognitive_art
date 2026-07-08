# Testing Philosophy

Tests should guard the project contract:

- Tinbergen quadrants remain a crossed two-axis map with unique keys.
- The termination catalog contains pragmatic, selection, and fixed-point stops.
- Generated figures match the manifest and are real image files (PNG + SVG).
- Manuscript variables cover every token used in the manuscript.
- The formal claim contract is closed: every used symbol is glossed, every
  glossary symbol is used, and no keys or filenames are duplicated.
- The claim ledger, domain profile, and experiment plan parse correctly and
  agree with the conceptual model source records.
- All scripts run as subprocesses and produce the expected output files.
- The conceptual integrity token is stable and 16 characters long.

No mocks are needed for this project. Tests exercise the real workflow into
temporary directories (via `tmp_path`) or the project `output/` directory.

## Current test suite

73 tests, 100% coverage target on `src/`:

- `test_conceptual_model.py` — concept inventory and contract validation
- `test_analysis_workflow.py` — pipeline output and figure generation
- `test_manuscript_variables.py` — token hydration and edge cases
- `test_scripts_smoke.py` — subprocess execution of all scripts
- `test_project_internals.py` — path resolution, runtime, documentation,
  claim ledger, domain profile, experiment plan, contract error branches,
  and figure manifest mismatch detection
