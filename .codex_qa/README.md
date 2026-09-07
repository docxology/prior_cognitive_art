# .codex_qa/

Local QA artifacts from agent QA sessions: rendered PDF page
screenshots, contact sheets, dashboards, and extracted PDF text. Hidden
and untracked; treat as disposable evidence, not manuscript sources.

| Path | Role |
|---|---|
| `pdf_pages/` | Individual rendered PDF page screenshots used during visual QA |
| `pdf_caption_pages/` | Page screenshots focused on figure-caption pages |
| `*_contact_sheet.png` | Grid contact sheets of figures / pages for fast visual review |
| `dashboard*.png`, `title_page.png`, `cover_page.png`, `page_*.png` | Point-in-time captures of the web/dashboard surface and PDF pages |
| `final_pdf_text.txt` | Extracted text of the rendered combined PDF (token-residue checks) |

Safe to regenerate after any render; do not reference these files from
the manuscript or committed docs.
