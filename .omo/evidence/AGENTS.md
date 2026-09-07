# .omo/evidence/ AGENTS

Agent-facing notes: evidence artifacts from verification and gate-review
passes (gate-review markdown, task-plan red/green scans, file
inventories, git-baseline snapshots). Filenames encode the producing pass.

- Append-only: add new files from verification tooling; do not edit or
  delete existing ones by hand.
- Regenerate via the corresponding verification tooling rather than
  patching stale numbers.

See `../../AGENTS.md` (project root) for the project contract; each
parent directory's `AGENTS.md` above adds local context.
