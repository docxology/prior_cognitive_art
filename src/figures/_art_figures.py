from __future__ import annotations

from pathlib import Path

from ._shared import PALETTE, Ellipse, _arrow, _box, _clean_axes, _save, plt, topic_pair


def draw_aesthetic_prior_craft_map(output_dir: Path) -> Path:
    fig, ax = plt.subplots(figsize=(12.2, 7.0))
    _clean_axes(ax)
    ax.set_xlim(0, 12.2)
    ax.set_ylim(0, 7.0)
    ax.set_facecolor(PALETTE["paper"])

    sources = [
        ("predictive\naesthetics", "expectation,\nsurprise,\nambiguity", 1.55, 5.55, *topic_pair("perception")),
        ("4E / enactive\nart", "embodied,\nsituated\naffordances", 1.55, 3.55, *topic_pair("embodiment")),
        ("neuroaesthetic\nscope", "sensory,\nvaluation,\nmeaning", 1.55, 1.55, *topic_pair("practice")),
    ]
    for title, subtitle, x, y, color, face in sources:
        _box(ax, (x, y), (2.15, 1.08), color, title, subtitle, face=face, title_size=10.8, subtitle_size=8.5)

    _box(
        ax,
        (5.15, 5.55),
        (2.5, 1.05),
        topic_pair("perception")[0],
        "staged\nexpectation",
        "learned regularities\nare invited or perturbed",
        face=topic_pair("perception")[1],
        title_size=11.2,
        subtitle_size=8.4,
    )
    _box(
        ax,
        (5.15, 3.55),
        (2.5, 1.05),
        topic_pair("embodiment")[0],
        "situated\npractice",
        "meaning emerges in\nembodied engagement",
        face=topic_pair("embodiment")[1],
        title_size=11.2,
        subtitle_size=8.4,
    )
    _box(
        ax,
        (5.15, 1.55),
        (2.5, 1.05),
        topic_pair("practice")[0],
        "scope\nboundary",
        "art exceeds reward\nor prediction error",
        face=topic_pair("practice")[1],
        title_size=11.2,
        subtitle_size=8.4,
    )

    for _, _, x, y, color, _ in sources:
        _arrow(ax, (x + 1.12, y), (3.85, y), color=color, lw=1.55, mutation_scale=13)

    art_edge, art_face = topic_pair("art")
    ax.add_patch(Ellipse((8.4, 3.55), 2.6, 2.15, facecolor=art_face, edgecolor=art_edge, lw=2.5))
    ax.text(8.4, 3.92, "prior-craft", ha="center", va="center", fontsize=15, color=art_edge, weight="bold")
    ax.text(8.4, 3.47, "arrange encounters\nwith priors", ha="center", va="center", fontsize=11.4, color=PALETTE["ink"], linespacing=1.05)
    ax.text(8.4, 2.86, "not a total\ntheory of art", ha="center", va="center", fontsize=8.9, color=PALETTE["red"], weight="bold", linespacing=0.95)

    _arrow(ax, (6.42, 5.35), (7.18, 4.2), color=topic_pair("perception")[0], lw=1.6, mutation_scale=13)
    _arrow(ax, (6.45, 3.55), (7.02, 3.55), color=topic_pair("embodiment")[0], lw=1.6, mutation_scale=13)
    _arrow(ax, (6.42, 1.75), (7.18, 2.9), color=topic_pair("practice")[0], lw=1.6, mutation_scale=13)

    _box(
        ax,
        (10.95, 3.55),
        (1.95, 1.16),
        PALETTE["red"],
        "claim\nceiling",
        "no mechanism claim\nabout artist intent\nor neural updating",
        face=PALETTE["red_fill"],
        title_size=10.8,
        subtitle_size=8.0,
    )
    _arrow(ax, (9.72, 3.55), (9.92, 3.55), color=PALETTE["red"], lw=1.45, mutation_scale=12)

    ax.set_title("Aesthetic prior-craft: art stages bounded encounters with priors", fontsize=16, color=PALETTE["ink"], pad=16)
    return _save(fig, output_dir / "aesthetic_prior_craft_map.png")
