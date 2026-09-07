# .codex_qa/ AGENTS

Agent-facing notes for the local QA artifact directory. Hidden and
untracked; everything here is disposable evidence, not manuscript source.

- Never reference files in this directory from the manuscript or committed
  docs; regenerate via QA tooling after any render instead.
- Do not hand-edit captured screenshots or `final_pdf_text.txt`; re-extract.
- `pdf_pages/` and `pdf_caption_pages/` hold rendered-PDF page screenshots
  (`page-NN.png`) for visual QA of the combined PDF and its caption pages.
- Use contact sheets and `final_pdf_text.txt` for token-residue and
  figure-parity checks before declaring a render clean.

See `../../AGENTS.md` (project root) for the project contract; each
parent directory's `AGENTS.md` above adds local context.
