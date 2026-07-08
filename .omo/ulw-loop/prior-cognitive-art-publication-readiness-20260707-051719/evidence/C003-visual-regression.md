# C003 Visual Regression And Cleanup

Status: PASS

Visual QA evidence:

- `figure-contact-sheet.png` shows all 18 refreshed figure PNGs.
- `pdf-page-contact-sheet-final.png` shows final PDF pages 1-4 and 17-22.
- `figure-contact-sheet-after-split.png` shows all 18 figure PNGs after the
  renderer module split.
- `pdf-page-contact-sheet-after-split.png` shows final PDF pages 1-4 and 17-22
  after the renderer module split and final render.
- `qpdf-check-final.log` reports no syntax or stream-encoding errors.
- `qpdf-check-after-split.log` reports no syntax or stream-encoding errors
  after the split.
- `figure-parity.log` and `final-contract-closure-after-split.log`
  report exact 18 PNG / 18 SVG / 18 `figure_specs()` parity.

Manual visual observations:

- All 18 figure PNGs are nonblank and framed.
- The three new figures render in the visual atlas: source-claim boundary map,
  Markov blanket scope split, and niche-prior feedback field.
- Representative final PDF pages are letter-sized, coherent, and not visibly
  clipped in the sampled front matter, introduction, visual-atlas, and formal
  supplement pages.

Slop and overfit coverage:

- The post-review test suite now includes broad no-residue patterns across
  source and rendered manuscript surfaces, not only the original narrow phrase
  list.
- The post-split test suite now includes a 250 pure-LOC ceiling guard for
  every `src/figures/*.py` module.
- The rendered-output token test checks hydrated manuscript, combined PDF
  markdown, and combined web markdown for unresolved `{{` / `}}` tokens.
- `src/figures/conceptual.py` was split into responsibility modules:
  `_argument_figures.py`, `_contract_figures.py`, `_niche_blanket_figures.py`,
  `_active_scale_figures.py`, `_boundary_figures.py`, and `_shared.py`.
- `figure-module-size-after-split.log` shows every figure module at or below
  the 250 pure-LOC ceiling, so no `SIZE_OK` exception is needed.

Cleanup:

- No dev server, browser session, tmux session, or long-running background
  process was started for this pass.
- Generated contact sheets and PDF page PNGs are retained as audit evidence.
