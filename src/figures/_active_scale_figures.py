from __future__ import annotations

from pathlib import Path

from src.conceptual_model import deterministic_simulation_trace

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
        ("Perception", (0, ring_radius), *topic_pair("perception")),
        ("Inference", (ring_radius, 0), *topic_pair("inference")),
        ("Action", (0, -ring_radius), *topic_pair("action")),
        ("Policy\nselection", (-ring_radius, 0), *topic_pair("policy")),
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
    colors_cycle = [
        topic_pair("perception")[0],
        topic_pair("inference")[0],
        topic_pair("action")[0],
        topic_pair("policy")[0],
    ]
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
    """Variational-bound landscape as a relative inferential minimum."""
    import numpy as np

    fig, ax = plt.subplots(figsize=(9, 7))
    _clean_axes(ax)
    ax.set_facecolor(PALETTE["paper"])

    x = np.linspace(-3, 3, 300)
    y = np.linspace(-3, 3, 300)
    X, Y = np.meshgrid(x, y)
    relative_floor = 0.18
    relative_range = 1.0 - relative_floor
    Z = relative_floor + relative_range * (1.0 - np.exp(-((X ** 2 + Y ** 2) / 0.5)))

    cf = ax.contourf(X, Y, Z, levels=24, cmap="Blues_r", alpha=0.85)
    cbar = plt.colorbar(cf, ax=ax, fraction=0.035, pad=0.03)
    cbar.set_label("Relative variational bound (a.u.)")

    # Bottom-of-basin contour as a relative KL/bound minimum.
    ax.contour(X, Y, Z, levels=[0.26], colors=[PALETTE["gold"]], linewidths=2.2, linestyles="--")
    ax.text(
        -0.95, -0.75, r"$\Delta\mathcal{F}=D_{KL}(q\|p^*) \downarrow$",
        fontsize=11, color=PALETTE["gold"], weight="bold",
        bbox=dict(boxstyle="round,pad=0.24", facecolor=PALETTE["paper"], edgecolor="none", alpha=0.82),
    )

    # Gold dot at basin centre = target posterior / settled inferential state.
    ax.plot(0, 0, "o", color=PALETTE["gold"], markersize=12, zorder=5)
    ax.text(0.18, -0.28, r"$p^*$  (target posterior)", fontsize=12,
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
        "Variational bound landscape: relative inferential minimum",
        fontsize=14, color=PALETTE["ink"], pad=18,
    )
    return _save(fig, output_dir / "variational_free_energy_landscape.png")


def draw_deterministic_simulation_trace(output_dir: Path) -> Path:
    from textwrap import fill

    trace = deterministic_simulation_trace()
    fig, ax = plt.subplots(figsize=(14.0, 7.2))
    _clean_axes(ax)
    ax.set_facecolor(PALETTE["paper"])
    ax.set_xlim(0, 10)
    ax.set_ylim(0.25, 4.35)

    colors = [
        topic_pair("source"),
        topic_pair("regress"),
        topic_pair("mechanism"),
        topic_pair("selection"),
        topic_pair("fixed_point"),
    ]
    for index, step in enumerate(trace):
        edge, face = colors[index % len(colors)]
        _box(
            ax,
            (step.x, step.y),
            (1.65, 0.86),
            edge,
            f"{step.step}. {step.state}",
            step.formal_state,
            face=face,
            title_size=9.8,
            subtitle_size=9.0,
        )
        ax.text(
            step.x,
            step.y - 0.67,
            fill(step.transition, width=24),
            ha="center",
            va="top",
            fontsize=7.8,
            color=PALETTE["ink"],
            linespacing=1.05,
        )
        ax.text(
            step.x,
            step.y - 1.05,
            fill(step.invariant, width=26),
            ha="center",
            va="top",
            fontsize=7.3,
            color=PALETTE["muted"],
            linespacing=1.05,
        )

    for left, right in zip(trace[:-1], trace[1:], strict=True):
        _arrow(
            ax,
            (left.x + 0.88, left.y),
            (right.x - 0.88, right.y),
            color=PALETTE["line"],
            lw=1.7,
            mutation_scale=16,
            rad=-0.12,
        )

    ax.add_patch(Rectangle((0.55, 0.48), 8.9, 0.68, facecolor="white", edgecolor=PALETTE["line"], lw=1.4))
    ax.text(
        5.0,
        0.82,
        "Deterministic illustrative simulation: formal state order only.\nNo stochastic sampling, synthetic data, empirical effects, or performance metrics.",
        ha="center",
        va="center",
        fontsize=9.4,
        color=PALETTE["muted"],
        linespacing=1.1,
    )
    ax.set_title(
        "Deterministic simulation trace over formal states",
        fontsize=15,
        color=PALETTE["ink"],
        pad=16,
    )
    return _save(fig, output_dir / "deterministic_simulation_trace.png")


def draw_scale_invariance_diagram(output_dir: Path) -> Path:
    """Three stacked panels: the same fixed-point structure at three scales."""
    fig, axes = plt.subplots(3, 1, figsize=(8, 9))
    fig.patch.set_facecolor(PALETTE["paper"])

    scale_configs = [
        ("Cellular scale", r"$X^*_{\mathrm{cell}}$", *topic_pair("mechanism"), 0.38),
        ("Organismic scale", r"$X^*_{\mathrm{organism}}$", *topic_pair("action"), 0.55),
        ("Social scale", r"$X^*_{\mathrm{social}}$", *topic_pair("practice"), 0.72),
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
    return _save(fig, output_dir / "scale_invariance_diagram.png")
