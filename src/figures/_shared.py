from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.patches import Circle, Ellipse, FancyArrowPatch, Polygon, Rectangle


PALETTE = {
    "ink": "#1f2933",
    "muted": "#52606d",
    "blue": "#2f6f9f",
    "green": "#2f855a",
    "gold": "#b7791f",
    "red": "#b83232",
    "paper": "#f8fafc",
    "line": "#cbd5e1",
    "blue_fill": "#edf7fc",
    "green_fill": "#ecf8f1",
    "gold_fill": "#fff7e6",
    "red_fill": "#fff1f1",
    "purple": "#7c3aed",
    "purple_fill": "#f3eefe",
}


def _save(fig: plt.Figure, path: Path) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=180, bbox_inches="tight")
    fig.savefig(path.with_suffix(".svg"), bbox_inches="tight")
    plt.close(fig)
    return path


def _clean_axes(ax: Axes) -> None:
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)


def _box(
    ax: Axes,
    center: tuple[float, float],
    size: tuple[float, float],
    edge: str,
    title: str,
    subtitle: str = "",
    *,
    face: str = "white",
    title_size: float = 11.5,
    subtitle_size: float = 9.5,
) -> None:
    x, y = center
    width, height = size
    ax.add_patch(Rectangle((x - width / 2, y - height / 2), width, height, facecolor=face, edgecolor=edge, lw=2))
    if subtitle:
        ax.text(x, y + height * 0.16, title, ha="center", va="center", fontsize=title_size, color=edge, weight="bold", linespacing=1.0)
        ax.text(x, y - height * 0.22, subtitle, ha="center", va="center", fontsize=subtitle_size, color=PALETTE["muted"], linespacing=1.05)
    else:
        ax.text(x, y, title, ha="center", va="center", fontsize=title_size, color=edge, weight="bold", linespacing=1.0)


def _arrow(
    ax: Axes,
    start: tuple[float, float],
    end: tuple[float, float],
    *,
    color: str | None = None,
    lw: float = 1.5,
    mutation_scale: float = 15,
    rad: float = 0,
) -> None:
    style = f"arc3,rad={rad}" if rad else "arc3"
    ax.add_patch(
        FancyArrowPatch(
            start,
            end,
            arrowstyle="-|>",
            connectionstyle=style,
            mutation_scale=mutation_scale,
            color=color or PALETTE["muted"],
            lw=lw,
        )
    )
