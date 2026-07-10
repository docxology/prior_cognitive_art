from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.lines import Line2D
from matplotlib.patches import (
    Circle as _MplCircle,
    Ellipse as _MplEllipse,
    FancyArrowPatch as _MplFancyArrowPatch,
    Polygon as _MplPolygon,
    Rectangle as _MplRectangle,
)


plt.rcParams.update(
    {
        "font.size": 11.0,
        "axes.titlesize": 16.5,
        "axes.labelsize": 11.0,
        "xtick.labelsize": 9.5,
        "ytick.labelsize": 9.5,
    }
)


PALETTE = {
    "ink": "#20232b",
    "muted": "#596372",
    "blue": "#245f7d",
    "green": "#24745a",
    "gold": "#ad7417",
    "red": "#b53a3a",
    "paper": "#f5ead8",
    "line": "#c9bfae",
    "blue_fill": "#e3f1f4",
    "green_fill": "#e4f1e7",
    "gold_fill": "#fff0cf",
    "red_fill": "#f8e0df",
    "purple": "#6a3fd1",
    "purple_fill": "#ece2ff",
    "teal": "#00796b",
    "teal_fill": "#dff2ef",
}


TOPIC_COLORS = {
    "default": ("ink", "paper"),
    "mechanism": ("blue", "blue_fill"),
    "proximate": ("blue", "blue_fill"),
    "perception": ("blue", "blue_fill"),
    "boundary": ("blue", "blue_fill"),
    "source": ("blue", "blue_fill"),
    "function": ("green", "green_fill"),
    "selection": ("green", "green_fill"),
    "viability": ("green", "green_fill"),
    "action": ("green", "green_fill"),
    "ontogeny": ("gold", "gold_fill"),
    "development": ("gold", "gold_fill"),
    "pragmatic": ("gold", "gold_fill"),
    "practice": ("gold", "gold_fill"),
    "phylogeny": ("red", "red_fill"),
    "regress": ("red", "red_fill"),
    "limit": ("red", "red_fill"),
    "policy": ("red", "red_fill"),
    "formal": ("purple", "purple_fill"),
    "inference": ("purple", "purple_fill"),
    "fixed_point": ("purple", "purple_fill"),
    "art": ("purple", "purple_fill"),
    "niche": ("teal", "teal_fill"),
    "embodiment": ("teal", "teal_fill"),
    "cohomeostasis": ("teal", "teal_fill"),
    "first_prior": ("teal", "teal_fill"),
    "validation": ("muted", "paper"),
}


def topic_pair(topic: str) -> tuple[str, str]:
    edge_key, fill_key = TOPIC_COLORS.get(topic, TOPIC_COLORS["default"])
    return PALETTE[edge_key], PALETTE[fill_key]


FIGURE_PROVENANCE = "Conceptual schematic | deterministic source-owned figure | no empirical simulation"


def _style_patch(patch):
    if hasattr(patch, "set_joinstyle"):
        patch.set_joinstyle("round")
    if hasattr(patch, "set_capstyle"):
        patch.set_capstyle("round")
    if hasattr(patch, "set_antialiased"):
        patch.set_antialiased(True)
    if hasattr(patch, "set_sketch_params"):
        patch.set_sketch_params(scale=0.42, length=88, randomness=0.55)
    return patch


def Circle(*args, **kwargs):
    return _style_patch(_MplCircle(*args, **kwargs))


def Ellipse(*args, **kwargs):
    return _style_patch(_MplEllipse(*args, **kwargs))


def FancyArrowPatch(*args, **kwargs):
    return _style_patch(_MplFancyArrowPatch(*args, **kwargs))


def Polygon(*args, **kwargs):
    return _style_patch(_MplPolygon(*args, **kwargs))


def Rectangle(*args, **kwargs):
    return _style_patch(_MplRectangle(*args, **kwargs))


def _stamp_provenance(fig: plt.Figure) -> None:
    fig.patch.set_facecolor(PALETTE["paper"])
    for y, color, alpha in ((0.972, PALETTE["purple"], 0.18), (0.958, PALETTE["teal"], 0.12)):
        fig.lines.append(
            Line2D(
                [0.025, 0.975],
                [y, y],
                transform=fig.transFigure,
                color=color,
                alpha=alpha,
                lw=1.15,
                solid_capstyle="round",
            )
        )
    fig.text(
        0.985,
        0.012,
        FIGURE_PROVENANCE,
        ha="right",
        va="bottom",
        fontsize=7.2,
        color=PALETTE["muted"],
        alpha=0.78,
    )


def _save(fig: plt.Figure, path: Path) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    _stamp_provenance(fig)
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
    title_size: float = 12.2,
    subtitle_size: float = 10.0,
) -> None:
    x, y = center
    width, height = size
    wash = Rectangle(
        (x - width / 2 + width * 0.025, y - height / 2 - height * 0.025),
        width,
        height,
        facecolor=edge,
        edgecolor="none",
        lw=0,
        alpha=0.08,
    )
    ax.add_patch(wash)
    ax.add_patch(Rectangle((x - width / 2, y - height / 2), width, height, facecolor=face, edgecolor=edge, lw=2.1))
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
