# Standalone checkout

The manuscript and its conceptual model are maintained in this repository.
A separate pinned Template checkout supplies the renderer. Follow the
[render setup](rendering_pipeline.md) to register this checkout and install
both locked environments. The registered worktree is the build working
directory.

Run the local publication build before the full test suite. Some tests
check or regenerate publication artifacts in the project's `output/` tree.
Use a disposable registered worktree when comparing release evidence.

```sh
uv run --no-sync python scripts/build_publication_package.py
uv run --no-sync pytest tests/
```

The [readiness report](publication_readiness_report.md) and
[scholarship audit](scholarship-audit.md) record the publication scope and
source decisions.
