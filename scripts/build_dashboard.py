#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

os.environ.setdefault("MPLBACKEND", "Agg")

PROJECT_ROOT = Path(__file__).resolve().parent.parent
for _path in (PROJECT_ROOT, PROJECT_ROOT / "src", PROJECT_ROOT.parents[2]):
    path_text = str(_path)
    if path_text not in sys.path:
        sys.path.insert(0, path_text)

from src.conceptual_model import (  # noqa: E402
    argument_modules,
    conceptual_integrity_token,
    figure_specs,
    formal_claims,
    quadrant_grid,
    symbol_glossary,
    termination_catalog,
    text_validation_checks,
    validate_conceptual_contract,
)


_CSS = """
:root {
  --ink: #1f2933;
  --muted: #52606d;
  --blue: #2f6f9f;
  --green: #2f855a;
  --gold: #b7791f;
  --red: #b83232;
  --paper: #f8fafc;
  --line: #cbd5e1;
  --blue-fill: #edf7fc;
  --green-fill: #ecf8f1;
  --gold-fill: #fff7e6;
  --red-fill: #fff1f1;
}
* { box-sizing: border-box; }
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  background: var(--paper);
  color: var(--ink);
  margin: 0;
  padding: 2rem;
  line-height: 1.6;
}
h1 { font-size: 1.8rem; margin-bottom: 0.25rem; }
h2 { font-size: 1.3rem; margin-top: 2rem; border-bottom: 2px solid var(--line); padding-bottom: 0.3rem; }
.subtitle { color: var(--muted); margin-bottom: 1.5rem; }
.token {
  display: inline-block;
  font-family: monospace;
  background: var(--ink);
  color: white;
  padding: 0.15rem 0.5rem;
  border-radius: 4px;
  font-size: 0.85rem;
}
.summary-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
  gap: 1rem;
  margin-bottom: 1.5rem;
}
.summary-card {
  background: white;
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 1rem;
  text-align: center;
}
.summary-card .count { font-size: 2rem; font-weight: bold; }
.summary-card .label { color: var(--muted); font-size: 0.85rem; }
.cover-hero {
  display: grid;
  grid-template-columns: minmax(220px, 360px) minmax(260px, 1fr);
  gap: 1.25rem;
  align-items: center;
  background: white;
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 1rem;
  margin: 1.5rem 0;
}
.cover-hero img {
  width: 100%;
  aspect-ratio: 1 / 1;
  object-fit: cover;
  border: 1px solid var(--line);
  border-radius: 6px;
}
.cover-hero .cover-title { font-size: 1.25rem; font-weight: bold; margin-bottom: 0.35rem; }
.cover-hero .cover-note { color: var(--muted); font-size: 0.94rem; }
table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 1rem;
  background: white;
}
th, td {
  text-align: left;
  padding: 0.5rem 0.75rem;
  border-bottom: 1px solid var(--line);
  font-size: 0.9rem;
}
th { background: var(--paper); font-weight: bold; }
.figure-gallery {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 1rem;
}
.figure-card {
  background: white;
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 0.75rem;
  overflow: hidden;
}
.figure-card img { width: 100%; height: auto; border-radius: 4px; }
.figure-card .title { font-weight: bold; margin: 0.5rem 0 0.25rem; font-size: 0.85rem; }
.figure-card .purpose { color: var(--muted); font-size: 0.8rem; }
.claim-block {
  background: white;
  border-left: 4px solid var(--blue);
  border-radius: 0 8px 8px 0;
  padding: 0.75rem 1rem;
  margin-bottom: 0.75rem;
}
.claim-block .title { font-weight: bold; }
.claim-block .expression { font-family: monospace; background: var(--paper); padding: 0.25rem 0.5rem; border-radius: 4px; margin: 0.25rem 0; }
.badge { display: inline-block; padding: 0.1rem 0.5rem; border-radius: 4px; font-size: 0.75rem; font-weight: bold; }
.badge-clean { background: var(--green-fill); color: var(--green); border: 1px solid var(--green); }
.badge-error { background: var(--red-fill); color: var(--red); border: 1px solid var(--red); }
"""


def _cover_hero(figures_dir: Path) -> str:
    cover_path = figures_dir.parent / "cover" / "prior_cognitive_art_cover_square.png"
    if not cover_path.exists():
        return ""
    return (
        "<section class='cover-hero'>"
        "<img src='../cover/prior_cognitive_art_cover_square.png' "
        "alt='Square cover art for Prior Cognitive Art'>"
        "<div>"
        "<div class='cover-title'>Square Cover Art</div>"
        "<div class='cover-note'>A deterministic 2048 x 2048 cover mark that braids the "
        "Tinbergen axes, hyperprior regress, selection filtering, Markov blanket scope, "
        "and fixed-point settlement into one publication-facing visual.</div>"
        "</div></section>"
    )


def _quadrant_table() -> str:
    rows = "".join(
        f"<tr><td><strong>{q.label}</strong></td><td>{q.scale}</td>"
        f"<td>{q.temporality}</td><td>{q.role}</td>"
        f"<td>{q.regress_status}</td></tr>"
        for q in quadrant_grid()
    )
    return (
        "<table><thead><tr><th>Question</th><th>Scale</th><th>Time-form</th>"
        "<th>Role</th><th>Regress status</th></tr></thead>"
        f"<tbody>{rows}</tbody></table>"
    )


def _termination_list() -> str:
    items = "".join(
        f"<li><strong>{t.name}</strong> <em>({t.stop_type})</em>: "
        f"{t.answer} <span style='color:var(--muted)'>Limitation: {t.limitation}</span></li>"
        for t in termination_catalog()
    )
    return f"<ul>{items}</ul>"


def _argument_list() -> str:
    items = "".join(
        f"<li><strong>{m.title}</strong>: {m.claim}</li>"
        for m in argument_modules()
    )
    return f"<ul>{items}</ul>"


def _figure_gallery(figures_dir: Path) -> str:
    cards = []
    for spec in figure_specs():
        img_path = figures_dir / spec.filename
        src = f"../figures/{spec.filename}" if img_path.exists() else ""
        img_html = f'<img src="{src}" alt="{spec.title}">' if src else ""
        cards.append(
            f'<div class="figure-card">{img_html}'
            f'<div class="title">{spec.title}</div>'
            f'<div class="purpose">{spec.purpose}</div></div>'
        )
    return f'<div class="figure-gallery">{"".join(cards)}</div>'


def _formal_claims() -> str:
    blocks = []
    for i, claim in enumerate(formal_claims(), start=1):
        blocks.append(
            f'<div class="claim-block">'
            f'<div class="title">F{i}: {claim.title}</div>'
            f'<div class="expression">{claim.expression}</div>'
            f'<div>{claim.reading}</div>'
            f'<div style="color:var(--muted);font-size:0.8rem">Symbols: {", ".join(claim.symbol_keys)}</div>'
            f"</div>"
        )
    return "".join(blocks)


def _symbol_table() -> str:
    rows = "".join(
        f"<tr><td>{s.symbol}</td><td>{s.name}</td><td>{s.role}</td></tr>"
        for s in symbol_glossary()
    )
    return (
        "<table><thead><tr><th>Symbol</th><th>Name</th><th>Role</th></tr></thead>"
        f"<tbody>{rows}</tbody></table>"
    )


def _validation_table() -> str:
    rows = "".join(
        f"<tr><td><code>{c.key}</code></td><td>{c.surface}</td>"
        f"<td>{c.invariant}</td><td>{c.evidence}</td></tr>"
        for c in text_validation_checks()
    )
    return (
        "<table><thead><tr><th>Check</th><th>Surface</th>"
        "<th>Invariant</th><th>Evidence</th></tr></thead>"
        f"<tbody>{rows}</tbody></table>"
    )


def cli_main() -> int:
    web_dir = PROJECT_ROOT / "output" / "web"
    web_dir.mkdir(parents=True, exist_ok=True)
    figures_dir = PROJECT_ROOT / "output" / "figures"

    contract_errors = validate_conceptual_contract()
    contract_badge = (
        '<span class="badge badge-clean">Contract clean</span>'
        if not contract_errors
        else f'<span class="badge badge-error">Contract errors: {"; ".join(contract_errors)}</span>'
    )

    counts = {
        "Quadrants": len(quadrant_grid()),
        "Terminations": len(termination_catalog()),
        "Arguments": len(argument_modules()),
        "Figures": len(figure_specs()),
        "Formal Claims": len(formal_claims()),
        "Symbols": len(symbol_glossary()),
        "Validation Checks": len(text_validation_checks()),
    }
    summary_cards = "".join(
        f'<div class="summary-card"><div class="count">{v}</div>'
        f'<div class="label">{k}</div></div>'
        for k, v in counts.items()
    )

    html = (
        f"<!doctype html><html><head><meta charset='utf-8'>"
        f"<title>Prior Cognitive Art — Dashboard</title>"
        f"<style>{_CSS}</style></head><body>"
        f"<h1>Prior Cognitive Art</h1>"
        f"<div class='subtitle'>Tinbergen Axes, Hyperprior Regress, and Fixed-Point Explanation</div>"
        f"<p>Integrity token: <span class='token'>{conceptual_integrity_token()}</span> {contract_badge}</p>"
        f"{_cover_hero(figures_dir)}"
        f"<h2>Conceptual Inventory</h2>"
        f"<div class='summary-grid'>{summary_cards}</div>"
        f"<h2>Tinbergen Quadrants</h2>{_quadrant_table()}"
        f"<h2>Termination Moves</h2>{_termination_list()}"
        f"<h2>Argument Modules</h2>{_argument_list()}"
        f"<h2>Visual Atlas</h2>{_figure_gallery(figures_dir)}"
        f"<h2>Formal Claims</h2>{_formal_claims()}"
        f"<h2>Symbol Glossary</h2>{_symbol_table()}"
        f"<h2>Text-Validation Checks</h2>{_validation_table()}"
        f"</body></html>"
    )

    out_path = web_dir / "dashboard.html"
    out_path.write_text(html, encoding="utf-8")

    # Also write a compact JSON payload for programmatic consumers
    payload = {
        "title": "Prior Cognitive Art",
        "integrity_token": conceptual_integrity_token(),
        "contract_errors": list(contract_errors),
        "counts": counts,
        "argument_modules": [m.title for m in argument_modules()],
        "terminations": [t.name for t in termination_catalog()],
        "figures": [s.filename for s in figure_specs()],
        "cover_art": "cover/prior_cognitive_art_cover_square.png",
    }
    json_path = web_dir / "dashboard_data.json"
    json_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    print(str(out_path))
    print(str(json_path))
    return 0


if __name__ == "__main__":
    raise SystemExit(cli_main())
