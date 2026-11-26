# Rendering and local verification

Use the [pinned Template revision](https://github.com/docxology/template/tree/87704feae0a4490ef7dad9c931d268e8c30273c2).
Install Pandoc with a compatible pandoc-crossref and XeLaTeX according to
the [Template run guide](https://github.com/docxology/template/blob/87704feae0a4490ef7dad9c931d268e8c30273c2/docs/RUN_GUIDE.md).
Install JuliaMono or DejaVu Sans Mono so the manuscript can typeset
Unicode code listings. The [Template integration guide](https://github.com/docxology/template/blob/87704feae0a4490ef7dad9c931d268e8c30273c2/projects/README.md)
describes the working project slot. The commands assume a
`prior_cognitive_art` checkout next to the new Template checkout.

```sh
git clone https://github.com/docxology/template.git template
cd template
git checkout --detach 87704feae0a4490ef7dad9c931d268e8c30273c2
uv sync --locked --no-dev --python 3.14
mkdir -p projects/working
git -C ../prior_cognitive_art worktree add --detach \
  "$PWD/projects/working/prior_cognitive_art" HEAD
cd projects/working/prior_cognitive_art
export UV_PYTHON=3.14
uv sync --locked --extra dev
export SOURCE_DATE_EPOCH="$(git log -1 --format=%ct)"
uv run --no-sync python scripts/build_publication_package.py
uv run --no-sync pytest tests/
```

The build generates conceptual figures and reports, generates the API
reference, and hydrates `docs/manuscript/` into `output/manuscript/`.
It runs Template Stage 03 to produce PDF, HTML, and slides. After
dashboard generation, it applies the project web CSS, records output
hashes, runs Template Stage 04 against the finished render, and executes
the native publication validator. The validator rejects stale source
or render artifacts and checks dashboard and figure metadata.

Find the combined PDF at `output/pdf/prior_cognitive_art_combined.pdf`,
the HTML paper at `output/web/index.html`, and the slide decks under
`output/slides/`. The dashboard is `output/web/dashboard.html`.
Validation and freshness receipts are under `output/reports/`. The
[output inventory](output_inventory.md) explains which files are
generated and which sources own them.
