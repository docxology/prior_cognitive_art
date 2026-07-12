from __future__ import annotations

from pathlib import Path

from ._shared import (
    PALETTE,
    Circle,
    Ellipse,
    FancyArrowPatch,
    Polygon,
    Rectangle,
    _arrow,
    _box,
    _clean_axes,
    _save,
    plt,
    topic_pair,
)

from src.conceptual_model import quadrant_grid, termination_catalog

def draw_tinbergen_axes(output_dir: Path) -> Path:
    fig, ax = plt.subplots(figsize=(10.8, 6.8))
    _clean_axes(ax)
    ax.set_xlim(-0.35, 2.12)
    ax.set_ylim(-0.18, 2.38)
    ax.set_facecolor(PALETTE["paper"])

    color_by_key = {key: topic_pair(key)[0] for key in ("mechanism", "function", "ontogeny", "phylogeny")}
    fill_by_key = {key: topic_pair(key)[1] for key in ("mechanism", "function", "ontogeny", "phylogeny")}
    positions = {
        ("proximate", "static"): (0, 1),
        ("ultimate", "static"): (1, 1),
        ("proximate", "developmental"): (0, 0),
        ("ultimate", "developmental"): (1, 0),
    }
    short_text = {
        "mechanism": ("Present causal\norganization", "local closure:\nmechanism"),
        "function": ("Current viability\nand use", "local closure:\nfunction"),
        "ontogeny": ("Individual history\nof tuning", "defers to source\nof history"),
        "phylogeny": ("Population history\nof persistence", "blocks through\nselection filter"),
    }
    for quadrant in quadrant_grid():
        x, y = positions[(quadrant.scale, quadrant.temporality)]
        rect = Rectangle((x + 0.06, y + 0.07), 0.88, 0.82, facecolor=fill_by_key[quadrant.key], edgecolor=color_by_key[quadrant.key], lw=2)
        ax.add_patch(rect)
        role, status = short_text[quadrant.key]
        ax.text(x + 0.14, y + 0.76, quadrant.label, color=color_by_key[quadrant.key], fontsize=15.5, weight="bold")
        ax.text(x + 0.14, y + 0.52, role, color=PALETTE["ink"], fontsize=12.5, linespacing=1.2)
        ax.text(x + 0.14, y + 0.23, status, color=PALETTE["muted"], fontsize=10.7, linespacing=1.18)

    ax.plot([1.0, 1.0], [0.02, 1.95], color=PALETTE["line"], lw=1.2)
    ax.plot([0.0, 2.02], [1.0, 1.0], color=PALETTE["line"], lw=1.2)
    ax.text(0.5, 2.02, "proximate", ha="center", va="bottom", fontsize=12, color=PALETTE["muted"], weight="bold")
    ax.text(1.5, 2.02, "ultimate", ha="center", va="bottom", fontsize=12, color=PALETTE["muted"], weight="bold")
    ax.text(-0.12, 1.5, "static", ha="right", va="center", fontsize=12, color=PALETTE["muted"], rotation=90, weight="bold")
    ax.text(-0.12, 0.5, "developmental", ha="right", va="center", fontsize=12, color=PALETTE["muted"], rotation=90, weight="bold")
    ax.set_title("Tinbergen's crossed axes show where prior-origin questions change kind", fontsize=17, color=PALETTE["ink"], pad=22)
    return _save(fig, output_dir / "tinbergen_axes.png")

def draw_regress_terminations(output_dir: Path) -> Path:
    fig, ax = plt.subplots(figsize=(12, 6.5))
    _clean_axes(ax)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.set_facecolor(PALETTE["paper"])

    chain = [
        ("P", "prior", 1.0),
        ("H(P)", "hyperprior", 2.65),
        ("H(H(P))", "next level", 4.55),
    ]
    chain_edge, chain_face = topic_pair("formal")
    for expression, label, x in chain:
        _box(ax, (x, 5.12), (1.25, 0.72), chain_edge, expression, label, face=chain_face, title_size=14, subtitle_size=9)
    for start, end in [((1.64, 5.12), (2.02, 5.12)), ((3.28, 5.12), (3.9, 5.12)), ((5.2, 5.12), (5.85, 5.12))]:
        _arrow(ax, start, end, color=PALETTE["muted"], lw=1.4)
    ax.text(6.05, 5.05, "...", fontsize=22, color=PALETTE["muted"])
    ax.text(7.15, 5.26, "iteration is easy;\nclosure names the stop", fontsize=11, color=PALETTE["red"], linespacing=1.05)
    _arrow(ax, (7.02, 4.95), (7.02, 4.25), color=PALETTE["red"], lw=1.8)

    display = {
        "pragmatic": ("flat/weak hyperprior", "formal stop", "thin explanation", *topic_pair("pragmatic")),
        "selection": ("function + phylogeny", "filters viable survivors", "not individual detail", *topic_pair("selection")),
        "fixed_point": ("X* = Phi(X*)", "category shift", "no hidden new prior", *topic_pair("fixed_point")),
    }
    y_positions = [3.65, 2.45, 1.25]
    for item, y in zip(termination_catalog(), y_positions, strict=True):
        handle, answer, limit, color, face = display[item.key]
        name = item.name.replace("Self-referential ", "Self-referential\n")
        ax.add_patch(Rectangle((0.72, y - 0.43), 8.8, 0.86, facecolor=face, edgecolor=color, lw=2))
        ax.text(1.0, y + 0.02, name, fontsize=10.8, weight="bold", color=color, va="center", linespacing=0.95)
        ax.text(4.05, y + 0.14, handle, fontsize=10.8, color=PALETTE["ink"], va="center", weight="bold")
        ax.text(4.05, y - 0.17, answer, fontsize=9.6, color=PALETTE["ink"], va="center")
        ax.text(6.82, y - 0.02, f"limit: {limit}", fontsize=9.5, color=PALETTE["muted"], va="center")

    ax.set_title("A hyperprior chain stops only when a termination rule changes the question", fontsize=16, color=PALETTE["ink"], pad=14)
    return _save(fig, output_dir / "regress_terminations.png")

def draw_prior_equilibrium_map(output_dir: Path) -> Path:
    fig, ax = plt.subplots(figsize=(9.2, 7.2))
    _clean_axes(ax)
    ax.set_xlim(-1.8, 1.8)
    ax.set_ylim(-1.5, 1.62)
    ax.set_aspect("equal")
    ax.set_facecolor(PALETTE["paper"])

    for patch in (
        Circle((0, 0), 0.92, fill=False, edgecolor=topic_pair("boundary")[0], lw=3),
        Circle((0, 0), 0.58, fill=False, edgecolor=topic_pair("action")[0], lw=2.2),
        Circle((0, 0), 0.28, facecolor=topic_pair("fixed_point")[1], edgecolor=topic_pair("fixed_point")[0], lw=2.2),
    ):
        ax.add_patch(patch)

    ax.text(0, 0.05, "prior-like\nsettlement", ha="center", va="center", fontsize=11.4, color=topic_pair("fixed_point")[0], weight="bold", linespacing=1.0)

    arrows = [
        ((0.54, 0.65), (0.87, 0.17)),
        ((0.84, -0.18), (0.45, -0.78)),
        ((-0.44, -0.78), (-0.86, -0.2)),
        ((-0.86, 0.2), (-0.45, 0.78)),
    ]
    for start, end in arrows:
        _arrow(ax, start, end, color=PALETTE["ink"], lw=1.6, mutation_scale=16, rad=0.25)

    callouts = [
        ("blanket\npersistence", (0, 1.12), *topic_pair("boundary")),
        ("action-perception\nclosure", (1.22, 0), *topic_pair("action")),
        ("environmental\nviability", (-1.26, 0), PALETTE["muted"], "white"),
        ("fixed point\nX* = Phi(X*)", (0, -1.12), *topic_pair("fixed_point")),
    ]
    for text, center, color, face in callouts:
        _box(ax, center, (0.78, 0.28), color, text, face=face, title_size=8.8)

    ax.text(
        0,
        -1.4,
        "The fixed-point answer treats the system as the persisting settlement the word 'prior' names.",
        ha="center",
        fontsize=9.8,
        color=PALETTE["muted"],
    )
    ax.set_title("Prior as settled organization maintained by blanket, action, and viability loops", fontsize=16, color=PALETTE["ink"], pad=16)
    return _save(fig, output_dir / "prior_equilibrium_map.png")

def draw_ontogeny_hyperprior_parallel(output_dir: Path) -> Path:
    fig, ax = plt.subplots(figsize=(11.5, 6.4))
    _clean_axes(ax)
    ax.set_xlim(0, 10.6)
    ax.set_ylim(0, 6.7)
    ax.set_facecolor(PALETTE["paper"])

    rows = [
        (
            4.25,
            "Hierarchical\nBayes",
            ["prior", "hyperprior", "hyper-hyperprior"],
            topic_pair("formal"),
        ),
        (
            2.05,
            "Ontogeny-only\nanswer",
            ["current prior", "developmental selector", "source of selector"],
            topic_pair("ontogeny"),
        ),
    ]
    x_positions = [2.75, 5.45, 8.15]
    half_width = 0.96
    for y, label, items, (color, face) in rows:
        ax.add_patch(Rectangle((0.42, y - 0.58), 8.92, 1.16, facecolor=face, edgecolor="none", alpha=0.55))
        ax.text(1.35, y + 0.1, label, ha="right", fontsize=11.7, weight="bold", color=color, va="center", linespacing=1.0)
        for x, item in zip(x_positions, items, strict=True):
            ax.add_patch(Rectangle((x - half_width, y - 0.38), half_width * 2, 0.76, facecolor="white", edgecolor=color, lw=2))
            ax.text(x, y, item, ha="center", va="center", fontsize=10.2, color=PALETTE["ink"])
        for start_x, end_x in zip(x_positions[:-1], x_positions[1:], strict=True):
            start = (start_x + half_width + 0.08, y)
            end = (end_x - half_width - 0.08, y)
            _arrow(ax, start, end, color=PALETTE["muted"], lw=1.4)

    ax.add_patch(FancyArrowPatch((9.35, 4.25), (9.35, 2.05), arrowstyle="<->", mutation_scale=18, color=PALETTE["red"], lw=2))
    ax.text(9.5, 3.13, "same\nregress\nshape", fontsize=10.8, color=PALETTE["red"], va="center", linespacing=1.0)
    ax.text(3.95, 4.65, "H", fontsize=11.5, color=topic_pair("formal")[0], weight="bold")
    ax.text(6.63, 4.65, "H", fontsize=11.5, color=topic_pair("formal")[0], weight="bold")
    ax.text(3.95, 2.45, "D", fontsize=11.5, color=topic_pair("ontogeny")[0], weight="bold")
    ax.text(6.63, 2.45, "D", fontsize=11.5, color=topic_pair("ontogeny")[0], weight="bold")
    ax.add_patch(Rectangle((1.95, 0.46), 6.35, 0.62, facecolor="white", edgecolor=PALETTE["red"], lw=1.8))
    ax.text(
        5.12,
        0.77,
        "Adding another selector does not answer why selection terminates.",
        ha="center",
        va="center",
        fontsize=11.5,
        color=PALETTE["ink"],
    )
    ax.set_title("Ontogeny-only explanation repeats the hyperprior chain's deferral shape", fontsize=16, color=PALETTE["ink"], pad=16)
    return _save(fig, output_dir / "ontogeny_hyperprior_parallel.png")

def draw_selection_filter(output_dir: Path) -> Path:
    fig, ax = plt.subplots(figsize=(10.8, 6.5))
    _clean_axes(ax)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.set_facecolor(PALETTE["paper"])

    candidates = [
        ("fragile\nprior", 1.18, 4.85, topic_pair("regress")[0], 0.42),
        ("miscalibrated\nprior", 1.18, 3.65, topic_pair("pragmatic")[0], 0.54),
        ("viable\nprior", 1.18, 2.45, topic_pair("selection")[0], 0.95),
        ("overfit\nprior", 1.18, 1.25, topic_pair("regress")[0], 0.42),
    ]
    for label, x, y, color, alpha in candidates:
        ax.add_patch(Ellipse((x, y), 1.52, 0.68, facecolor=color, edgecolor=color, alpha=alpha))
        ax.text(x, y, label, ha="center", va="center", fontsize=9.2, color="white" if alpha > 0.7 else PALETTE["ink"], linespacing=1.0)
        arrow_color = topic_pair("selection")[0] if "viable" in label else PALETTE["line"]
        _arrow(ax, (1.98, y), (3.28, 3.05), color=arrow_color, lw=1.5 if "viable" in label else 1.2, mutation_scale=13)

    funnel = Polygon(
        [(3.3, 5.24), (6.65, 4.1), (6.65, 2.0), (3.3, 0.86)],
        closed=True,
        facecolor=topic_pair("selection")[1],
        edgecolor=topic_pair("selection")[0],
        lw=2.2,
    )
    ax.add_patch(funnel)
    ax.text(4.98, 3.62, "function", ha="center", fontsize=15, weight="bold", color=topic_pair("function")[0])
    ax.text(4.98, 2.95, "+", ha="center", fontsize=18, color=PALETTE["muted"])
    ax.text(4.98, 2.3, "phylogeny", ha="center", fontsize=15, weight="bold", color=topic_pair("selection")[0])
    ax.text(4.98, 1.45, "viability filter", ha="center", fontsize=11.2, color=PALETTE["muted"])

    _arrow(ax, (6.68, 3.05), (7.9, 3.05), color=topic_pair("selection")[0], lw=2, mutation_scale=17)
    _box(ax, (8.62, 3.05), (1.58, 1.36), topic_pair("selection")[0], "persisting\nprior", "available because\nit lasted", face="white", title_size=12.2, subtitle_size=9.2)
    ax.text(1.18, 5.55, "candidate forms", ha="center", fontsize=10.5, color=PALETTE["muted"], weight="bold")
    ax.set_title("Selection closure explains persistence by filtering viable prior-like forms", fontsize=16, color=PALETTE["ink"], pad=16)
    return _save(fig, output_dir / "selection_filter.png")
