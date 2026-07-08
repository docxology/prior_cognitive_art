from __future__ import annotations

from pathlib import Path

import numpy as np

from ._shared import PALETTE, Circle, FancyArrowPatch, Polygon, Rectangle, plt


COVER_ART_FILENAME = "prior_cognitive_art_cover_square.png"
COVER_ART_SVG_FILENAME = "prior_cognitive_art_cover_square.svg"
COVER_ART_SIZE_PX = 2048


def _hex_to_rgb(value: str) -> tuple[float, float, float]:
    value = value.lstrip("#")
    return tuple(int(value[i : i + 2], 16) / 255 for i in (0, 2, 4))


def _background_field(size: int = 900) -> np.ndarray:
    axis = np.linspace(-1.0, 1.0, size)
    x, y = np.meshgrid(axis, axis)
    radius = np.sqrt(x**2 + y**2)
    angle = np.arctan2(y, x)
    base = np.array(_hex_to_rgb(PALETTE["paper"]))
    blue = np.array(_hex_to_rgb(PALETTE["blue_fill"]))
    green = np.array(_hex_to_rgb(PALETTE["green_fill"]))
    gold = np.array(_hex_to_rgb(PALETTE["gold_fill"]))
    red = np.array(_hex_to_rgb(PALETTE["red_fill"]))
    purple = np.array(_hex_to_rgb(PALETTE["purple_fill"]))
    braid = np.sin(8 * angle + 10 * radius) * np.exp(-1.25 * radius)
    ripples = 0.035 * np.cos(8 * np.pi * x) * np.sin(5 * np.pi * y)
    field = (
        base
        + blue * (0.20 + 0.10 * np.clip(-x + y, 0, 1))[..., None]
        + green * (0.16 + 0.08 * np.clip(x + y, 0, 1))[..., None]
        + gold * (0.13 + 0.09 * np.clip(-x - y, 0, 1))[..., None]
        + red * (0.11 + 0.07 * np.clip(x - y, 0, 1))[..., None]
        + purple * (0.06 + 0.04 * (1 - np.clip(radius, 0, 1)))[..., None]
    ) / 1.72
    field += (braid * 0.020 + ripples)[..., None] * np.array([0.35, 0.25, 0.48])
    vignette = 1 - 0.16 * np.clip(radius, 0, 1.0)[..., None]
    return np.clip(field * vignette, 0, 1)


def _arrow(
    ax,
    start: tuple[float, float],
    end: tuple[float, float],
    color: str,
    *,
    rad: float = 0.0,
    lw: float = 1.8,
    alpha: float = 0.86,
    scale: float = 18,
) -> None:
    ax.add_patch(
        FancyArrowPatch(
            start,
            end,
            arrowstyle="-|>",
            connectionstyle=f"arc3,rad={rad}",
            mutation_scale=scale,
            lw=lw,
            color=color,
            alpha=alpha,
        )
    )


def _panel(
    ax,
    xy: tuple[float, float],
    wh: tuple[float, float],
    edge: str,
    face: str,
    *,
    alpha: float = 0.86,
    lw: float = 1.35,
) -> None:
    ax.add_patch(Rectangle(xy, wh[0], wh[1], facecolor=face, edgecolor=edge, lw=lw, alpha=alpha))


def _label_box(
    ax,
    xy: tuple[float, float],
    text: str,
    edge: str,
    face: str,
    *,
    width: float = 0.145,
    height: float = 0.052,
    size: float = 10.5,
) -> None:
    x, y = xy
    _panel(ax, (x - width / 2, y - height / 2), (width, height), edge, face, alpha=0.92, lw=1.45)
    ax.text(x, y, text, ha="center", va="center", color=edge, fontsize=size, weight="bold", linespacing=0.95)


def _draw_orbital_field(ax) -> None:
    theta = np.linspace(0, 2 * np.pi, 640)
    orbits = [
        (0.285, 0.020, 3, PALETTE["blue"], 0.20),
        (0.232, 0.024, 4, PALETTE["green"], 0.24),
        (0.178, 0.020, 5, PALETTE["gold"], 0.34),
        (0.118, 0.014, 6, PALETTE["red"], 0.42),
    ]
    for radius, wobble, frequency, color, alpha in orbits:
        r = radius + wobble * np.sin(frequency * theta)
        ax.plot(0.5 + r * np.cos(theta), 0.49 + r * np.sin(theta), color=color, lw=2.1, alpha=alpha)
    for radius, color, alpha in [
        (0.328, PALETTE["blue"], 0.14),
        (0.270, PALETTE["green"], 0.18),
        (0.210, PALETTE["gold"], 0.25),
        (0.145, PALETTE["red"], 0.32),
    ]:
        ax.add_patch(Circle((0.5, 0.49), radius, fill=False, edgecolor=color, lw=1.25, alpha=alpha))


def _draw_quadrant_spine(ax) -> None:
    ax.plot([0.5, 0.5], [0.19, 0.79], color=PALETTE["line"], lw=1.6, alpha=0.78)
    ax.plot([0.18, 0.82], [0.49, 0.49], color=PALETTE["line"], lw=1.6, alpha=0.78)
    quadrant_specs = [
        ((0.206, 0.785), "mechanism", "policy decomposition", PALETTE["blue"], PALETTE["blue_fill"]),
        ((0.684, 0.785), "function", "selection filter", PALETTE["green"], PALETTE["green_fill"]),
        ((0.194, 0.193), "ontogeny", "hyperprior stop", PALETTE["gold"], PALETTE["gold_fill"]),
        ((0.680, 0.193), "phylogeny", "inherited priors", PALETTE["red"], PALETTE["red_fill"]),
    ]
    for (x, y), title, subtitle, edge, face in quadrant_specs:
        _panel(ax, (x - 0.012, y - 0.020), (0.178, 0.064), edge, face, alpha=0.62, lw=1.0)
        ax.text(x, y + 0.018, title, color=edge, fontsize=12.5, weight="bold", ha="left", va="center")
        ax.text(x, y - 0.014, subtitle, color=PALETTE["muted"], fontsize=7.6, ha="left", va="center")


def _draw_source_claim_band(ax) -> None:
    y = 0.735
    labels = [
        ("source\nfamilies", PALETTE["blue"], PALETTE["blue_fill"]),
        ("claim\nledger", PALETTE["purple"], PALETTE["purple_fill"]),
        ("formal\ninventory", PALETTE["gold"], PALETTE["gold_fill"]),
        ("manuscript\nclaims", PALETTE["green"], PALETTE["green_fill"]),
    ]
    xs = [0.232, 0.402, 0.572, 0.742]
    for i, ((label, edge, face), x) in enumerate(zip(labels, xs)):
        _label_box(ax, (x, y), label, edge, face, width=0.125, height=0.064, size=8.6)
        if i < len(xs) - 1:
            _arrow(ax, (x + 0.067, y), (xs[i + 1] - 0.067, y), edge, lw=1.25, scale=12, alpha=0.7)


def _draw_hyperprior_chain(ax) -> None:
    xs = [0.245, 0.345, 0.445]
    ys = [0.622, 0.656, 0.690]
    labels = ["prior", "hyperprior", "stop"]
    for i, (x, y, label) in enumerate(zip(xs, ys, labels)):
        _label_box(ax, (x, y), label, PALETTE["blue"], PALETTE["blue_fill"], width=0.140, height=0.048, size=10.5)
        if i < 2:
            _arrow(ax, (x + 0.075, y + 0.003), (xs[i + 1] - 0.075, ys[i + 1] - 0.002), PALETTE["blue"], lw=1.4, scale=13)
    ax.text(0.288, 0.574, "regress terminates as a\nhigher-order constraint", color=PALETTE["muted"], fontsize=7.8, ha="center")


def _draw_selection_filter(ax) -> None:
    funnel = Polygon(
        [(0.655, 0.655), (0.817, 0.602), (0.817, 0.535), (0.655, 0.477)],
        closed=True,
        facecolor=PALETTE["green_fill"],
        edgecolor=PALETTE["green"],
        lw=2.1,
        alpha=0.92,
    )
    ax.add_patch(funnel)
    ax.text(0.742, 0.575, "selection\nfilter", ha="center", va="center", color=PALETTE["green"], fontsize=12, weight="bold")
    for offset, alpha in [(0.00, 0.32), (0.027, 0.20), (0.054, 0.12)]:
        ax.plot([0.660 + offset, 0.790 + offset], [0.637 - offset, 0.592 - offset], color=PALETTE["green"], lw=1.0, alpha=alpha)
        ax.plot([0.660 + offset, 0.790 + offset], [0.497 + offset, 0.548 + offset], color=PALETTE["green"], lw=1.0, alpha=alpha)


def _draw_blanket_scope(ax) -> None:
    ax.add_patch(Circle((0.276, 0.344), 0.078, fill=False, edgecolor=PALETTE["purple"], lw=2.2, linestyle="--", alpha=0.95))
    ax.add_patch(Circle((0.315, 0.310), 0.048, fill=False, edgecolor=PALETTE["muted"], lw=1.2, alpha=0.48))
    ax.text(0.276, 0.350, "blanket", ha="center", va="center", color=PALETTE["purple"], fontsize=10.4, weight="bold")
    ax.text(0.276, 0.326, "as model", ha="center", va="center", color=PALETTE["purple"], fontsize=8.8, weight="bold")
    ax.text(0.342, 0.287, "realized\ncoupling", ha="center", va="center", color=PALETTE["muted"], fontsize=7.2)
    _arrow(ax, (0.338, 0.356), (0.405, 0.404), PALETTE["purple"], rad=-0.15, lw=1.2, scale=12, alpha=0.72)


def _draw_niche_feedback(ax) -> None:
    points = [(0.678, 0.356), (0.775, 0.325), (0.748, 0.435)]
    labels = [("O", PALETTE["red"]), ("N", PALETTE["gold"]), ("C", PALETTE["green"])]
    for (x, y), (label, color) in zip(points, labels):
        ax.add_patch(Circle((x, y), 0.030, facecolor="white", edgecolor=color, lw=1.7, alpha=0.96))
        ax.text(x, y, label, ha="center", va="center", color=color, fontsize=10.5, weight="bold")
    _arrow(ax, points[0], points[1], PALETTE["red"], rad=0.18, lw=1.3, scale=12)
    _arrow(ax, points[1], points[2], PALETTE["gold"], rad=0.18, lw=1.3, scale=12)
    _arrow(ax, points[2], points[0], PALETTE["green"], rad=0.18, lw=1.3, scale=12)
    ax.text(0.735, 0.273, "organism / niche / culture\nfeedback loop", ha="center", color=PALETTE["muted"], fontsize=7.4)


def _draw_center(ax) -> None:
    ax.add_patch(Circle((0.5, 0.49), 0.069, facecolor="#fffaf0", edgecolor=PALETTE["gold"], lw=2.5, alpha=0.98))
    ax.add_patch(Circle((0.5, 0.49), 0.036, facecolor="#ffffff", edgecolor=PALETTE["line"], lw=1.1, alpha=0.95))
    ax.text(0.5, 0.501, "P*", ha="center", va="center", fontsize=25, color=PALETTE["gold"], weight="bold")
    ax.text(0.5, 0.456, "settling prior", ha="center", va="center", fontsize=9.2, color=PALETTE["muted"])
    _arrow(ax, (0.294, 0.500), (0.411, 0.556), PALETTE["blue"], rad=0.28, lw=2.0)
    _arrow(ax, (0.589, 0.556), (0.704, 0.503), PALETTE["green"], rad=0.28, lw=2.0)
    _arrow(ax, (0.704, 0.448), (0.584, 0.395), PALETTE["red"], rad=0.28, lw=2.0)
    _arrow(ax, (0.416, 0.395), (0.294, 0.448), PALETTE["gold"], rad=0.28, lw=2.0)


def draw_square_cover_art(output_dir: Path) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    png_path = output_dir / COVER_ART_FILENAME
    svg_path = output_dir / COVER_ART_SVG_FILENAME

    fig = plt.figure(figsize=(8, 8), dpi=256)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.imshow(_background_field(), extent=(0, 1, 0, 1), origin="lower")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect("equal")
    ax.axis("off")

    for margin, lw, alpha in [(0.032, 2.4, 0.72), (0.052, 1.15, 0.40), (0.073, 0.75, 0.20)]:
        ax.add_patch(
            Rectangle((margin, margin), 1 - 2 * margin, 1 - 2 * margin, fill=False, edgecolor=PALETTE["ink"], lw=lw, alpha=alpha)
        )

    _draw_quadrant_spine(ax)
    _draw_orbital_field(ax)
    _draw_source_claim_band(ax)
    _draw_hyperprior_chain(ax)
    _draw_selection_filter(ax)
    _draw_blanket_scope(ax)
    _draw_niche_feedback(ax)
    _draw_center(ax)

    ax.text(0.5, 0.912, "PRIOR COGNITIVE ART", ha="center", va="center", fontsize=34, color=PALETTE["ink"], weight="bold")
    ax.text(
        0.5,
        0.870,
        "Tinbergen axes / hyperprior stopping / model-level blankets / niche-prior feedback",
        ha="center",
        va="center",
        fontsize=11.8,
        color=PALETTE["muted"],
    )
    ax.text(
        0.5,
        0.111,
        "A deterministic square cover for a simulation-free conceptual manuscript",
        ha="center",
        va="center",
        fontsize=10.8,
        color=PALETTE["muted"],
    )
    ax.text(0.5, 0.080, "Daniel Ari Friedman", ha="center", va="center", fontsize=12.4, color=PALETTE["ink"])

    fig.savefig(png_path, dpi=256, facecolor=fig.get_facecolor(), edgecolor="none")
    fig.savefig(svg_path, facecolor=fig.get_facecolor(), edgecolor="none")
    plt.close(fig)
    return png_path
