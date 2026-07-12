"""Project-owned post-render adjustments for generated web surfaces."""

from __future__ import annotations

from pathlib import Path


_STYLE_MARKER = "data-prior-cognitive-art-layout=\"compact\""


def apply_project_web_style(project_root: Path) -> list[Path]:
    """Append the project stylesheet to rendered manuscript HTML files.

    The shared template renderer owns the base Pandoc CSS. This project-owned
    post-render hook keeps compact layout policy local to this manuscript and
    makes the applied style observable to the package validator.
    """

    css_path = project_root / "manuscript" / "web.css"
    web_dir = project_root / "output" / "web"
    if not css_path.exists() or not web_dir.exists():
        return []

    css = css_path.read_text(encoding="utf-8")
    style_tag = f'<style {_STYLE_MARKER}>{css}</style>'
    applied: list[Path] = []
    candidates = [web_dir / "index.html", *sorted(web_dir.glob("manuscript__*.html"))]
    for path in candidates:
        if not path.exists():
            continue
        content = path.read_text(encoding="utf-8")
        if _STYLE_MARKER in content:
            applied.append(path)
            continue
        if "</head>" not in content:
            raise ValueError(f"rendered HTML has no </head> insertion point: {path}")
        path.write_text(content.replace("</head>", f"\n{style_tag}\n</head>", 1), encoding="utf-8")
        applied.append(path)
    return applied


__all__ = ["apply_project_web_style"]
