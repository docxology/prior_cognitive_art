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

def draw_source_claim_boundary_map(output_dir: Path) -> Path:
    fig, ax = plt.subplots(figsize=(12, 7.2))
    _clean_axes(ax)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7)
    ax.set_facecolor(PALETTE["paper"])

    source_nodes = [
        ("Tinbergen /\nKonner", 1.35, 5.8, PALETTE["blue"], PALETTE["blue_fill"]),
        ("FEP /\nactive inference", 1.35, 4.55, PALETTE["green"], PALETTE["green_fill"]),
        ("niche /\nDST", 1.35, 3.3, PALETTE["gold"], PALETTE["gold_fill"]),
        ("Bayesian\nworkflow", 1.35, 2.05, PALETTE["purple"], PALETTE["purple_fill"]),
        ("boundary\ncritiques", 1.35, 0.8, PALETTE["red"], PALETTE["red_fill"]),
    ]
    for label, x, y, color, face in source_nodes:
        _box(ax, (x, y), (1.7, 0.78), color, label, face=face, title_size=10.2)

    _box(
        ax,
        (4.1, 4.75),
        (2.25, 1.05),
        PALETTE["green"],
        "accepted\nsource layer",
        "primary, scholarly,\nclaim-relevant",
        face=PALETTE["green_fill"],
        title_size=11.0,
        subtitle_size=8.6,
    )
    _box(
        ax,
        (4.1, 2.55),
        (2.25, 1.05),
        PALETTE["red"],
        "rejected /\ndeferred",
        "noisy, indirect,\nor overextended",
        face=PALETTE["red_fill"],
        title_size=11.0,
        subtitle_size=8.6,
    )
    _box(
        ax,
        (6.85, 4.75),
        (2.05, 1.05),
        PALETTE["blue"],
        "claim\nledger",
        "source tier +\nartifact path",
        face=PALETTE["blue_fill"],
        title_size=11.0,
        subtitle_size=8.6,
    )
    _box(
        ax,
        (9.7, 5.65),
        (2.15, 0.86),
        PALETTE["gold"],
        "manuscript\nclaims",
        "bounded prose",
        face=PALETTE["gold_fill"],
        title_size=11.0,
        subtitle_size=8.7,
    )
    _box(
        ax,
        (9.7, 3.85),
        (2.15, 0.86),
        PALETTE["purple"],
        "formal\ninventory",
        "checkable records",
        face=PALETTE["purple_fill"],
        title_size=11.0,
        subtitle_size=8.7,
    )
    _box(
        ax,
        (9.7, 2.05),
        (2.15, 0.86),
        PALETTE["green"],
        "visual\natlas",
        "deterministic figures",
        face=PALETTE["green_fill"],
        title_size=11.0,
        subtitle_size=8.7,
    )

    for _, x, y, color, _ in source_nodes:
        target_y = 4.75 if color != PALETTE["red"] else 2.55
        _arrow(ax, (x + 0.9, y), (2.92, target_y), color=color, lw=1.35, mutation_scale=12)
    _arrow(ax, (5.25, 4.75), (5.82, 4.75), color=PALETTE["green"], lw=1.8)
    _arrow(ax, (7.88, 4.95), (8.62, 5.55), color=PALETTE["gold"], lw=1.7)
    _arrow(ax, (7.88, 4.75), (8.62, 3.92), color=PALETTE["purple"], lw=1.7)
    _arrow(ax, (7.88, 4.55), (8.62, 2.18), color=PALETTE["green"], lw=1.7)

    ax.add_patch(Rectangle((3.0, 0.38), 6.95, 0.56, facecolor="white", edgecolor=PALETTE["line"], lw=1.4))
    ax.text(
        6.48,
        0.66,
        "Perplexity discovers candidates; direct source checks decide what enters the paper.",
        ha="center",
        va="center",
        fontsize=10.5,
        color=PALETTE["muted"],
    )
    ax.set_title("Source-to-claim boundary map", fontsize=16, color=PALETTE["ink"], pad=16)
    return _save(fig, output_dir / "source_claim_boundary_map.png")

def draw_markov_blanket_scope_split(output_dir: Path) -> Path:
    fig, ax = plt.subplots(figsize=(11.5, 7.0))
    _clean_axes(ax)
    ax.set_xlim(0, 11.5)
    ax.set_ylim(0, 7.0)
    ax.set_facecolor(PALETTE["paper"])

    layers = [
        ("Pearl blanket", "conditional\nindependence", "epistemic tool", PALETTE["blue"], PALETTE["blue_fill"], 5.7),
        ("Friston blanket", "active-inference\nmodel boundary", "formal organism\nmodeling", PALETTE["green"], PALETTE["green_fill"], 3.75),
        ("Realized boundary", "biological /\ncognitive system", "requires extra\ndynamical premises", PALETTE["gold"], PALETTE["gold_fill"], 1.8),
    ]
    for title, middle, footer, color, face, y in layers:
        ax.add_patch(Rectangle((1.0, y - 0.62), 3.1, 1.24, facecolor=face, edgecolor=color, lw=2.2))
        ax.text(1.25, y + 0.32, title, ha="left", va="center", fontsize=11.5, color=color, weight="bold")
        ax.text(2.55, y, middle, ha="center", va="center", fontsize=12.2, color=PALETTE["ink"], weight="bold", linespacing=1.0)
        ax.text(2.55, y - 0.38, footer, ha="center", va="center", fontsize=9.2, color=PALETTE["muted"], linespacing=1.0)

    _arrow(ax, (4.25, 5.7), (5.02, 5.7), color=PALETTE["blue"], lw=1.6)
    _arrow(ax, (4.25, 3.75), (5.02, 3.75), color=PALETTE["green"], lw=1.6)
    _arrow(ax, (4.25, 1.8), (5.02, 1.8), color=PALETTE["gold"], lw=1.6)

    ax.add_patch(Ellipse((6.35, 3.75), 2.0, 4.7, facecolor="white", edgecolor=PALETTE["line"], lw=1.8))
    ax.text(6.35, 5.75, "scope split", ha="center", va="center", fontsize=13, color=PALETTE["ink"], weight="bold")
    ax.text(6.35, 4.55, "model\nuse", ha="center", va="center", fontsize=11.8, color=PALETTE["blue"], weight="bold", linespacing=1.0)
    ax.text(6.35, 3.3, "metaphysical\nuse", ha="center", va="center", fontsize=11.8, color=PALETTE["red"], weight="bold", linespacing=1.0)
    ax.text(6.35, 2.05, "biological\nrealization", ha="center", va="center", fontsize=11.8, color=PALETTE["green"], weight="bold", linespacing=1.0)

    _box(
        ax,
        (9.45, 4.9),
        (2.5, 1.08),
        PALETTE["red"],
        "boundary\ncondition",
        "do not infer organism\nontology from notation alone",
        face=PALETTE["red_fill"],
        title_size=11.4,
        subtitle_size=8.5,
    )
    _box(
        ax,
        (9.45, 2.35),
        (2.5, 1.08),
        PALETTE["green"],
        "paper's\nstance",
        "use blankets as bounded\nmodel-level achievements",
        face=PALETTE["green_fill"],
        title_size=11.4,
        subtitle_size=8.5,
    )
    _arrow(ax, (7.35, 4.35), (8.2, 4.8), color=PALETTE["red"], lw=1.6)
    _arrow(ax, (7.35, 3.05), (8.2, 2.55), color=PALETTE["green"], lw=1.6)

    ax.set_title("Markov blanket scope split", fontsize=16, color=PALETTE["ink"], pad=16)
    return _save(fig, output_dir / "markov_blanket_scope_split.png")

def draw_niche_prior_feedback_field(output_dir: Path) -> Path:
    fig, ax = plt.subplots(figsize=(11.5, 7.0))
    _clean_axes(ax)
    ax.set_xlim(0, 11.5)
    ax.set_ylim(0, 7.0)
    ax.set_facecolor(PALETTE["paper"])

    bands = [
        ("organismic action", 5.75, PALETTE["blue"], PALETTE["blue_fill"]),
        ("developmental resources", 3.75, PALETTE["green"], PALETTE["green_fill"]),
        ("cultural inheritance", 1.75, PALETTE["gold"], PALETTE["gold_fill"]),
    ]
    for label, y, color, face in bands:
        ax.add_patch(Rectangle((1.0, y - 0.55), 9.5, 1.1, facecolor=face, edgecolor=color, lw=2.0, alpha=0.92))
        ax.text(1.28, y + 0.28, label, ha="left", va="center", fontsize=12.0, color=color, weight="bold")
        for x in (3.0, 5.0, 7.0, 9.0):
            ax.add_patch(Circle((x, y), 0.22, facecolor="white", edgecolor=color, lw=1.6))

    for x in (3.0, 5.0, 7.0, 9.0):
        _arrow(ax, (x, 5.48), (x + 0.35, 4.25), color=PALETTE["muted"], lw=1.15, mutation_scale=10, rad=-0.15)
        _arrow(ax, (x + 0.35, 3.25), (x, 2.25), color=PALETTE["muted"], lw=1.15, mutation_scale=10, rad=0.15)
        _arrow(ax, (x, 1.25), (x - 0.35, 5.25), color=PALETTE["muted"], lw=1.05, mutation_scale=10, rad=0.18)

    ax.add_patch(Ellipse((5.95, 3.75), 2.2, 1.3, facecolor="white", edgecolor=PALETTE["purple"], lw=2.4, zorder=4))
    ax.text(5.95, 3.93, "prior-like\nfield", ha="center", va="center", fontsize=13, color=PALETTE["purple"], weight="bold", linespacing=1.0, zorder=5)
    ax.text(5.95, 3.45, r"$P_t \leftrightarrow N_t$", ha="center", va="center", fontsize=12.5, color=PALETTE["purple"], zorder=5)

    ax.text(1.05, 6.58, "faster", ha="left", va="center", fontsize=10.0, color=PALETTE["muted"])
    ax.text(1.05, 0.72, "slower", ha="left", va="center", fontsize=10.0, color=PALETTE["muted"])
    _arrow(ax, (0.7, 6.28), (0.7, 1.05), color=PALETTE["muted"], lw=1.2, mutation_scale=12)
    ax.text(0.42, 3.65, "timescale", ha="center", va="center", fontsize=10.0, color=PALETTE["muted"], rotation=90)

    ax.add_patch(Rectangle((2.25, 0.34), 7.0, 0.56, facecolor="white", edgecolor=PALETTE["line"], lw=1.4))
    ax.text(
        5.75,
        0.62,
        "The field stabilizes through recurrent organism-niche coupling, not one-way inheritance.",
        ha="center",
        va="center",
        fontsize=10.3,
        color=PALETTE["muted"],
    )
    ax.set_title("Niche-prior feedback field across timescales", fontsize=16, color=PALETTE["ink"], pad=16)
    return _save(fig, output_dir / "niche_prior_feedback_field.png")
