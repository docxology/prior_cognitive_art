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
)

from src.conceptual_model import quadrant_grid

def draw_niche_construction_diagram(output_dir: Path) -> Path:
    """Reciprocal organism–environment co-shaping of the prior."""
    fig, ax = plt.subplots(figsize=(10, 6.5))
    _clean_axes(ax)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.set_facecolor(PALETTE["paper"])

    ax.add_patch(Ellipse((2.2, 3.0), 2.8, 1.8, facecolor=PALETTE["blue_fill"], edgecolor=PALETTE["blue"], lw=2.5))
    ax.text(2.2, 3.0, "Organism", ha="center", va="center", fontsize=15, color=PALETTE["blue"], weight="bold")

    ax.add_patch(Ellipse((7.8, 3.0), 2.8, 1.8, facecolor=PALETTE["green_fill"], edgecolor=PALETTE["green"], lw=2.5))
    ax.text(7.8, 3.12, "Environment /", ha="center", va="center", fontsize=13.5, color=PALETTE["green"], weight="bold")
    ax.text(7.8, 2.78, "Niche", ha="center", va="center", fontsize=13.5, color=PALETTE["green"], weight="bold")

    ax.add_patch(Circle((5.0, 3.0), 0.58, facecolor=PALETTE["gold_fill"], edgecolor=PALETTE["gold"], lw=2.5))
    ax.text(5.0, 3.0, "P", ha="center", va="center", fontsize=18, color=PALETTE["gold"], weight="bold")

    _arrow(ax, (3.62, 3.18), (4.40, 3.18), color=PALETTE["blue"], lw=2.0, mutation_scale=16, rad=0.25)
    _arrow(ax, (4.40, 2.82), (3.62, 2.82), color=PALETTE["blue"], lw=2.0, mutation_scale=16, rad=0.25)
    _arrow(ax, (6.38, 3.18), (5.60, 3.18), color=PALETTE["green"], lw=2.0, mutation_scale=16, rad=-0.25)
    _arrow(ax, (5.60, 2.82), (6.38, 2.82), color=PALETTE["green"], lw=2.0, mutation_scale=16, rad=-0.25)

    ax.text(5.0, 5.18, r"$\mathcal{N}(P) \leftrightarrow P$", ha="center", va="center",
            fontsize=18, color=PALETTE["ink"], weight="bold")

    ax.text(3.62, 1.62, r"$O$ = organism", ha="center", va="center", fontsize=9.6,
            color=PALETTE["blue"], weight="bold")
    ax.text(6.38, 1.62, r"$N$ = niche", ha="center", va="center", fontsize=9.6,
            color=PALETTE["green"], weight="bold")

    _box(
        ax,
        (5.0, 0.72),
        (7.8, 0.72),
        PALETTE["muted"],
        "The prior is co-shaped, not fully given or fully endogenous.",
        face="white",
        title_size=11.2,
    )

    ax.set_title("Niche construction: organism and environment co-shape the prior", fontsize=16, color=PALETTE["ink"], pad=16)
    return _save(fig, output_dir / "niche_construction_diagram.png")

def draw_markov_blanket_achievement(output_dir: Path) -> Path:
    fig, ax = plt.subplots(figsize=(9, 7))
    _clean_axes(ax)
    ax.set_xlim(-2.4, 2.95)
    ax.set_ylim(-2.4, 2.55)
    ax.set_aspect("equal")
    ax.set_facecolor(PALETTE["paper"])

    ax.add_patch(Circle((0, 0), 1.35, facecolor=PALETTE["blue_fill"], edgecolor=PALETTE["blue"], lw=4))

    ax.text(0, 0.18, "settled system", ha="center", va="center", fontsize=13, color=PALETTE["gold"], weight="bold")
    ax.text(0, -0.22, r"$X^* = \Phi(X^*)$", ha="center", va="center", fontsize=13.5, color=PALETTE["gold"], weight="bold")

    ax.text(0, 1.52, r"model boundary  $M = \Phi(X^*)$", ha="center", va="bottom", fontsize=12, color=PALETTE["blue"], weight="bold")

    ax.text(0, -1.05, "internal states", ha="center", va="center", fontsize=10.5, color=PALETTE["muted"])

    ax.text(1.75, 1.55, "external states", ha="left", va="center", fontsize=10.5, color=PALETTE["muted"])
    ax.text(1.72, -1.28, "not read off\nwithout assumptions", ha="left", va="center", fontsize=9.2, color=PALETTE["red"], linespacing=1.0)

    boundary_arrows = [
        ((1.22, 0.57), (0.46, 1.26), 0.45),
        ((-0.46, 1.26), (-1.22, 0.57), 0.45),
        ((-1.22, -0.57), (-0.46, -1.26), 0.45),
        ((0.46, -1.26), (1.22, -0.57), 0.45),
    ]
    for start, end, rad in boundary_arrows:
        ax.add_patch(
            FancyArrowPatch(
                start,
                end,
                arrowstyle="-|>",
                connectionstyle=f"arc3,rad={rad}",
                mutation_scale=16,
                color=PALETTE["blue"],
                lw=2.2,
            )
        )

    _box(
        ax,
        (0, -1.98),
        (4.0, 0.54),
        PALETTE["muted"],
        "The formal boundary is useful; the ontology is bounded.",
        face="white",
        title_size=11.2,
    )

    ax.set_title("Markov blanket as model-bound achievement", fontsize=16, color=PALETTE["ink"], pad=16)
    return _save(fig, output_dir / "markov_blanket_achievement.png")

def draw_explanatory_complementarity_matrix(output_dir: Path) -> Path:
    """4×4 grid: Tinbergen questions are complementary, not rival."""
    fig, ax = plt.subplots(figsize=(9, 7.5))
    _clean_axes(ax)
    ax.set_facecolor(PALETTE["paper"])

    questions = [q.label for q in quadrant_grid()]  # Mechanism, Function, Ontogeny, Phylogeny
    n = len(questions)

    diag_colors = [PALETTE["blue"], PALETTE["green"], PALETTE["gold"], PALETTE["red"]]
    diag_fills = [PALETTE["blue_fill"], PALETTE["green_fill"], PALETTE["gold_fill"], PALETTE["red_fill"]]

    cell_size = 1.0
    origin_x = 1.2  # left margin for row labels
    origin_y = 0.6  # bottom margin for col labels

    # Draw cells
    for row in range(n):
        for col in range(n):
            x = origin_x + col * cell_size
            y = origin_y + (n - 1 - row) * cell_size  # top row = row 0

            if row == col:
                face = diag_fills[row]
                edge = diag_colors[row]
                lw = 2.5
            else:
                face = "#e8edf2"
                edge = PALETTE["line"]
                lw = 1.2

            ax.add_patch(Rectangle((x, y), cell_size, cell_size, facecolor=face, edgecolor=edge, lw=lw))

            if row == col:
                ax.text(
                    x + cell_size / 2,
                    y + cell_size / 2,
                    questions[row],
                    ha="center",
                    va="center",
                    fontsize=10.5,
                    color=diag_colors[row],
                    weight="bold",
                    linespacing=1.0,
                )
            else:
                ax.text(
                    x + cell_size / 2,
                    y + cell_size / 2,
                    "+",
                    ha="center",
                    va="center",
                    fontsize=16,
                    color=PALETTE["muted"],
                    weight="bold",
                )

    # Column headers (top)
    for col in range(n):
        x = origin_x + col * cell_size + cell_size / 2
        y_header = origin_y + n * cell_size + 0.18
        ax.text(x, y_header, questions[col], ha="center", va="bottom", fontsize=10.2,
                color=diag_colors[col], weight="bold", rotation=0)

    # Row headers (left)
    for row in range(n):
        y = origin_y + (n - 1 - row) * cell_size + cell_size / 2
        x_header = origin_x - 0.12
        ax.text(x_header, y, questions[row], ha="right", va="center", fontsize=10.2,
                color=diag_colors[row], weight="bold")

    # Axis limit to fit content
    ax.set_xlim(0, origin_x + n * cell_size + 0.4)
    ax.set_ylim(0, origin_y + n * cell_size + 0.85)

    # Caption box below grid
    caption_y = origin_y - 0.48
    ax.add_patch(Rectangle((origin_x, caption_y - 0.22), n * cell_size, 0.44,
                            facecolor="white", edgecolor=PALETTE["line"], lw=1.5))
    ax.text(
        origin_x + n * cell_size / 2,
        caption_y,
        "Each pair of questions contributes independently — no question subsumes another.",
        ha="center",
        va="center",
        fontsize=9.8,
        color=PALETTE["muted"],
    )

    ax.set_title("Tinbergen questions are complementary, not rival", fontsize=16, color=PALETTE["ink"], pad=16)
    return _save(fig, output_dir / "explanatory_complementarity_matrix.png")
