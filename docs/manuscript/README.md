# Prior Cognitive Art manuscript

Sections:

- `00_abstract.md`
- `01_introduction.md`
- `02_methodology.md`
- `03_results.md`
- `04_conclusion.md`
- `05_experimental_setup.md`
- `06_reproducibility.md`
- `07_scope_and_related_work.md`
- `08_formal_supplement.md`
- `99_references.md`

Supporting files:

- `config.yaml` — paper metadata, authors, keywords, render settings
- `config.yaml.example` — template for new configurations
- `preamble.md` — LaTeX preamble injected during PDF compilation
- `references.bib` — BibTeX bibliography; the package validator reports its
  current entry and citation closure.
- `SYNTAX.md` — Pandoc figure/table reference syntax guide
- `layer_contract.yaml` — source/script/manuscript boundary rules

Follow the [pinned build](../rendering_pipeline.md). It generates figures from
the conceptual model, resolves prose tokens into `output/manuscript/`, and
validates the finished PDF, HTML, and slides.

The [reference inventory](../overview.md#conceptual-inventory) and
[scholarship audit](../scholarship-audit.md) document the claim boundaries.
