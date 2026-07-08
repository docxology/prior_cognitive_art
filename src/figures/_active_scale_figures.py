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

def draw_active_inference_cycle(output_dir: Path) -> Path:
    """Circular four-stage active-inference loop minimising free energy."""
    import math

    fig, ax = plt.subplots(figsize=(9, 8))
    _clean_axes(ax)
    ax.set_aspect("equal")
    ax.set_facecolor(PALETTE["paper"])

    # Large background circle (guide ring)
    ring_radius = 2.5
    ax.add_patch(Circle((0, 0), ring_radius, fill=False, edgecolor=PALETTE["line"], lw=1.8, linestyle="--"))

    # 4 stage positions: N (top), E (right), S (bottom), W (left)
    stages = [
        ("Perception",      ( 0,             ring_radius),  PALETTE["blue"],   PALETTE["blue_fill"]),
        ("Inference",       ( ring_radius,   0),            PALETTE["green"],  PALETTE["green_fill"]),
        ("Action",          ( 0,            -ring_radius),  PALETTE["gold"],   PALETTE["gold_fill"]),
        ("Policy\nselection", (-ring_radius,  0),           PALETTE["red"],    PALETTE["red_fill"]),
    ]

    node_radius = 0.6
    for label, (cx, cy), edge, face in stages:
        ax.add_patch(Circle((cx, cy), node_radius, facecolor=face, edgecolor=edge, lw=2.5, zorder=3))
        ax.text(cx, cy, label, ha="center", va="center", fontsize=11, color=edge,
                weight="bold", linespacing=1.0, zorder=4)

    # Clockwise curved arrows between the 4 nodes: N->E->S->W->N
    # Each arc is drawn between the node surfaces (offset by node_radius along the ring direction)
    # We compute points on the ring slightly ahead/behind each node, then use a curved arrow.
    arrow_pairs = [
        # (from_stage_angle_deg, to_stage_angle_deg, rad_sign)
        (90,  0,   -0.35),   # Perception -> Inference  (clockwise, i.e. top -> right)
        ( 0, 270,  -0.35),   # Inference  -> Action
        (270, 180, -0.35),   # Action     -> Policy selection
        (180,  90, -0.35),   # Policy selection -> Perception
    ]
    colors_cycle = [PALETTE["blue"], PALETTE["green"], PALETTE["gold"], PALETTE["red"]]
    gap = node_radius / ring_radius  # angular gap in radians to clear the node circle

    for (a_deg, b_deg, rad_sign), color in zip(arrow_pairs, colors_cycle):
        a = math.radians(a_deg)
        b = math.radians(b_deg)
        # clockwise: start just past 'a' node, end just before 'b' node
        # "just past" means: move clockwise from a by gap
        step = -gap  # negative = clockwise in standard math angles
        start_angle = a + step
        end_angle = b - step
        sx = ring_radius * math.cos(start_angle)
        sy = ring_radius * math.sin(start_angle)
        ex = ring_radius * math.cos(end_angle)
        ey = ring_radius * math.sin(end_angle)
        ax.add_patch(
            FancyArrowPatch(
                (sx, sy), (ex, ey),
                arrowstyle="-|>",
                connectionstyle=f"arc3,rad={rad_sign}",
                mutation_scale=18,
                color=color,
                lw=2.0,
                zorder=2,
            )
        )

    # Centre label
    ax.text(0, 0, r"$\min \mathcal{F}$", ha="center", va="center", fontsize=17,
            color=PALETTE["ink"], weight="bold")

    ax.set_xlim(-3.6, 3.6)
    ax.set_ylim(-3.6, 3.95)
    ax.set_title(
        "Active inference: action and perception close the free-energy loop",
        fontsize=14, color=PALETTE["ink"], pad=18,
    )
    return _save(fig, output_dir / "active_inference_cycle.png")

def draw_variational_free_energy_landscape(output_dir: Path) -> Path:
    """Free-energy landscape as a valley; the prior is the settling point."""
    import numpy as np

    fig, ax = plt.subplots(figsize=(9, 7))
    _clean_axes(ax)
    ax.set_facecolor(PALETTE["paper"])

    # Build Gaussian landscape: high at edges, low at centre
    x = np.linspace(-3, 3, 300)
    y = np.linspace(-3, 3, 300)
    X, Y = np.meshgrid(x, y)
    Z = 1.0 - np.exp(-((X ** 2 + Y ** 2) / 0.5))  # 0 at centre, ~1 at edges

    cf = ax.contourf(X, Y, Z, levels=24, cmap="Blues_r", alpha=0.85)
    plt.colorbar(cf, ax=ax, fraction=0.035, pad=0.03, label="Variational free energy F")

    # Bottom-of-basin contour (F ≈ 0)
    cs = ax.contour(X, Y, Z, levels=[0.08], colors=[PALETTE["gold"]], linewidths=2.2, linestyles="--")
    ax.clabel(cs, fmt=lambda _: r"$\mathcal{F}^* \approx 0$", fontsize=11, colors=PALETTE["gold"])

    # Gold dot at basin centre = prior/settling point P
    ax.plot(0, 0, "o", color=PALETTE["gold"], markersize=12, zorder=5)
    ax.text(0.18, -0.28, r"$P$  (prior / settling point)", fontsize=12,
            color=PALETTE["gold"], weight="bold", va="top")

    # Arrow from initial q (off-centre) down to the basin
    q_start = (-1.8, 1.8)
    ax.plot(*q_start, "o", color=PALETTE["red"], markersize=9, zorder=5)
    ax.text(q_start[0] - 0.12, q_start[1] + 0.18, r"initial $q$", fontsize=11,
            color=PALETTE["red"], weight="bold", ha="right")
    ax.annotate(
        "",
        xy=(0, 0),
        xytext=q_start,
        arrowprops=dict(
            arrowstyle="-|>",
            color=PALETTE["red"],
            lw=2.0,
            connectionstyle="arc3,rad=-0.25",
            mutation_scale=18,
        ),
        zorder=6,
    )

    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3.35)
    ax.set_aspect("equal")
    ax.set_xlabel("Belief state dimension 1", fontsize=10, color=PALETTE["muted"])
    ax.set_ylabel("Belief state dimension 2", fontsize=10, color=PALETTE["muted"])
    ax.set_title(
        "Variational free energy landscape: the prior as settling point",
        fontsize=14, color=PALETTE["ink"], pad=18,
    )
    return _save(fig, output_dir / "variational_free_energy_landscape.png")

def draw_scale_invariance_diagram(output_dir: Path) -> Path:
    """Three stacked panels: the same fixed-point structure at three scales."""
    fig, axes = plt.subplots(3, 1, figsize=(8, 9))
    fig.patch.set_facecolor(PALETTE["paper"])

    scale_configs = [
        ("Cellular scale",    r"$X^*_{\mathrm{cell}}$",     PALETTE["blue"],  PALETTE["blue_fill"],  0.38),
        ("Organismic scale",  r"$X^*_{\mathrm{organism}}$", PALETTE["green"], PALETTE["green_fill"], 0.55),
        ("Social scale",      r"$X^*_{\mathrm{social}}$",   PALETTE["gold"],  PALETTE["gold_fill"],  0.72),
    ]

    for ax, (scale_label, var_label, edge, face, r) in zip(axes, scale_configs):
        _clean_axes(ax)
        ax.set_facecolor(PALETTE["paper"])
        ax.set_xlim(-2.2, 2.2)
        ax.set_ylim(-1.2, 1.2)
        ax.set_aspect("equal")

        # Circle representing the fixed-point attractor at this scale
        ax.add_patch(Circle((0, 0), r, facecolor=face, edgecolor=edge, lw=2.5, zorder=3))

        # Fixed-point equation inside circle
        ax.text(0, 0.12, r"$X^* = \Phi(X^*)$", ha="center", va="center",
                fontsize=9.5, color=edge, weight="bold", zorder=4)

        # Variable label just below equation
        ax.text(0, -0.15, var_label, ha="center", va="center",
                fontsize=9, color=edge, zorder=4)

        # Scale label to the right
        ax.text(1.0, 0, scale_label, ha="left", va="center",
                fontsize=12, color=edge, weight="bold")

    # Downward "R" arrows between panels (drawn in figure coordinates)
    for idx in range(len(axes) - 1):
        # Use figure.transFigure to place arrows between subplots
        ax_top = axes[idx]
        ax_bot = axes[idx + 1]
        # Mid-x in axes[idx] data coords -> figure coords via transform
        mid_x_data = 0.0
        # Place arrow at x=0.42 in figure coords (slightly right of centre)
        fig.text(0.42, (ax_top.get_position().y0 + ax_bot.get_position().y1) / 2,
                 r"$\downarrow \mathbf{R}$",
                 ha="center", va="center", fontsize=14, color=PALETTE["muted"], weight="bold")

    fig.suptitle(
        "Scale invariance: the fixed-point move recurs at each scale",
        fontsize=14, color=PALETTE["ink"], y=0.98,
    )
    fig.tight_layout(rect=(0.0, 0.0, 1.0, 0.96))
    path = output_dir / "scale_invariance_diagram.png"
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=180, bbox_inches="tight")
    fig.savefig(path.with_suffix(".svg"), bbox_inches="tight")
    plt.close(fig)
    return path
