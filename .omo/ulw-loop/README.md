# ulw-loop/

State directories for ulw-loop improvement campaigns run with the omo
tooling. Each timestamped subdirectory is one run and contains:

- `brief.md` — the campaign brief (goals and constraints)
- `goals.json` — structured goal list and status
- `ledger.jsonl` — append-only per-iteration event ledger
- `evidence/` — artifacts captured while proving each goal

Runs are named `<project>-<campaign>-<timestamp>` (or
`<project>-<timestamp>`). Directories are historical records; start a
new run rather than modifying an old one.
