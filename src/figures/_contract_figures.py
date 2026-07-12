from __future__ import annotations

from pathlib import Path

from ._shared import (
    PALETTE,
    Circle,
    Ellipse,
    Rectangle,
    _arrow,
    _box,
    _clean_axes,
    _save,
    plt,
    topic_pair,
)

from src.conceptual_model import claim_grounding, formal_claims, symbol_glossary, text_validation_checks

def draw_policy_entanglement_bridge(output_dir: Path) -> Path:
    fig, ax = plt.subplots(figsize=(11.2, 6.6))
    _clean_axes(ax)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.set_facecolor(PALETTE["paper"])

    joint_edge, joint_face = topic_pair("formal")
    ax.add_patch(Ellipse((2.2, 3.1), 2.55, 2.15, facecolor=joint_face, edgecolor=joint_edge, lw=2.5))
    ax.text(2.2, 3.55, "Lambda", ha="center", va="center", fontsize=14, color=joint_edge, weight="bold")
    ax.text(2.2, 3.16, "joint\norganization", ha="center", va="center", fontsize=13.5, color=joint_edge, weight="bold", linespacing=1.0)
    ax.text(2.2, 2.45, "prior to the\nfactors extracted", ha="center", va="center", fontsize=10.2, color=PALETTE["muted"], linespacing=1.0)

    _arrow(ax, (3.55, 3.1), (4.75, 3.1), color=PALETTE["ink"], lw=1.8, mutation_scale=18)
    ax.add_patch(Rectangle((3.72, 3.62), 1.18, 0.52, facecolor="white", edgecolor=PALETTE["line"], lw=1.0))
    ax.text(4.31, 3.88, "lambda-\ndecomposition", ha="center", va="center", fontsize=9.8, color=PALETTE["ink"], linespacing=0.95)

    factor_boxes = [
        ("pi\npolicy", 6.45, 4.62, *topic_pair("policy")),
        ("P\nprior-like\nconstraint", 7.66, 3.1, *topic_pair("fixed_point")),
        ("x\nstate factor", 6.45, 1.58, *topic_pair("source")),
    ]
    split_origin = (4.75, 3.1)
    for label, x, y, color, face in factor_boxes:
        _arrow(ax, split_origin, (x - 0.82, y), color=color, lw=1.7)
        ax.add_patch(Rectangle((x - 0.78, y - 0.48), 1.56, 0.96, facecolor=face, edgecolor=color, lw=2))
        ax.text(x, y, label, ha="center", va="center", fontsize=10.8, color=PALETTE["ink"], linespacing=1.0)

    ax.add_patch(Rectangle((1.0, 0.38), 8.0, 0.64, facecolor="white", edgecolor=PALETTE["line"], lw=1.5))
    ax.text(
        5.02,
        0.69,
        "The decomposition makes useful factors; it does not prove the factors came first.",
        ha="center",
        va="center",
        fontsize=11.0,
        color=PALETTE["muted"],
    )
    ax.set_title("Lambda-decomposition clarifies factors after joint organization is already present", fontsize=16, color=PALETTE["ink"], pad=16)
    return _save(fig, output_dir / "policy_entanglement_bridge.png")

def draw_formal_claim_dependency_map(output_dir: Path) -> Path:
    fig, ax = plt.subplots(figsize=(12, 8.0))
    _clean_axes(ax)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.set_facecolor(PALETTE["paper"])

    ax.text(1.25, 7.55, "source records", ha="center", fontsize=11.5, color=PALETTE["muted"], weight="bold")
    ax.text(5.5, 7.55, "auto-numbered claims", ha="center", fontsize=11.5, color=PALETTE["muted"], weight="bold")
    sources = [
        ("tinbergen_axes", "Tinbergen\naxes", 1.35, 6.85, topic_pair("mechanism")[0]),
        ("regress_shape", "regress\nshape", 1.35, 5.65, topic_pair("regress")[0]),
        ("termination_moves", "termination\nmoves", 1.35, 4.45, topic_pair("selection")[0]),
        ("joint_structure", "joint\nstructure", 1.35, 3.25, topic_pair("formal")[0]),
        ("niche_blanket", "niche &\nblanket", 1.35, 2.05, topic_pair("niche")[0]),
        ("cross_scale_recurrence", "cross-scale\nrecurrence", 1.35, 0.85, PALETTE["muted"]),
    ]
    # Grounding: which auto-numbered claim each source record anchors.
    # (source_index -> claim index in formal_claims(), 1-based)
    for _, label, x, y, color in sources:
        _box(ax, (x, y), (1.58, 0.72), color, label, face="white", title_size=10.0)

    claims = list(formal_claims())
    # Two columns of claims: left col x=4.5, right col x=7.4; stacked vertically
    col_left_x = 4.5
    col_right_x = 7.6
    n = len(claims)
    left_count = (n + 1) // 2
    right_count = n - left_count
    left_ys = [7.0 - i * 0.92 for i in range(left_count)]
    right_ys = [7.0 - i * 0.92 for i in range(right_count)]
    positions = (
        [(col_left_x, y) for y in left_ys]
        + [(col_right_x, y) for y in right_ys]
    )
    box_width = 2.3
    # Draw grounding arrows from each source record to the claim(s) it anchors.
    claim_positions = {claim.key: positions[index] for index, claim in enumerate(claims)}
    source_positions = {key: (x, y) for key, _, x, y, _ in sources}
    for grounding in claim_grounding():
        sx, sy = source_positions[grounding.source_record]
        cx, cy = claim_positions[grounding.claim_key]
        _arrow(ax, (2.2, sy), (cx - box_width / 2 - 0.08, cy), color=PALETTE["muted"], lw=1.1, mutation_scale=12)
    claim_topics = {
        "axis_partition": "mechanism",
        "regress_shape": "regress",
        "selection_filter": "selection",
        "fixed_point_stop": "fixed_point",
        "decomposition_caution": "formal",
        "niche_co_construction": "niche",
        "blanket_achievement": "boundary",
        "explanatory_complementarity": "validation",
        "active_inference_bridge": "action",
        "variational_closure": "inference",
        "scale_recurrence": "practice",
        "deterministic_trace_boundary": "limit",
    }
    box_width = 2.3
    for index, (claim, (x, y)) in enumerate(zip(claims, positions), start=1):
        color, face = topic_pair(claim_topics[claim.key])
        ax.add_patch(Rectangle((x - box_width / 2, y - 0.33), box_width, 0.66, facecolor=face, edgecolor=color, lw=2))
        ax.text(x, y + 0.1, f"F{index}: {claim.title}", ha="center", va="center", fontsize=9.6, color=PALETTE["ink"])
        ax.text(x, y - 0.15, f"{len(claim.symbol_keys)} symbols", ha="center", va="center", fontsize=8.2, color=PALETTE["muted"])

    _box(ax, (8.55, 0.58), (1.45, 0.54), PALETTE["line"], "source order", f"fixes F1-F{n}", face="white", title_size=9.8, subtitle_size=8.2)
    ax.set_title("Formal claims are grounded views over source records, not freestanding theorems", fontsize=16, color=PALETTE["ink"], pad=16)
    return _save(fig, output_dir / "formal_claim_dependency_map.png")

def draw_symbol_glossary_closure(output_dir: Path) -> Path:
    fig, ax = plt.subplots(figsize=(10.8, 6.4))
    _clean_axes(ax)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.set_facecolor(PALETTE["paper"])

    counts = {
        "claims": len(formal_claims()),
        "symbols": len(symbol_glossary()),
    }
    _box(
        ax,
        (2.55, 3.25),
        (3.0, 2.15),
        topic_pair("formal")[0],
        "symbols used\nby formal claims",
        f"{counts['symbols']} keys across F1-F{counts['claims']}",
        face=topic_pair("formal")[1],
        title_size=12.4,
        subtitle_size=10.2,
    )
    _box(
        ax,
        (7.45, 3.25),
        (3.0, 2.15),
        topic_pair("validation")[0],
        "glossary rows\ngenerated as table",
        f"{counts['symbols']} rows in the supplement",
        face=topic_pair("validation")[1],
        title_size=12.4,
        subtitle_size=10.2,
    )
    ax.add_patch(Circle((5.0, 3.25), 0.62, facecolor="white", edgecolor=PALETTE["line"], lw=2))
    ax.text(5.0, 3.36, "used", ha="center", va="center", fontsize=10.5, color=PALETTE["ink"])
    ax.text(5.0, 3.12, "=", ha="center", va="center", fontsize=15, color=PALETTE["muted"], weight="bold")
    ax.text(5.0, 2.88, "defined", ha="center", va="center", fontsize=10.5, color=PALETTE["ink"])
    _arrow(ax, (4.05, 3.25), (4.38, 3.25), color=PALETTE["muted"], lw=1.3)
    _arrow(ax, (5.62, 3.25), (5.95, 3.25), color=PALETTE["muted"], lw=1.3)

    ax.add_patch(Rectangle((1.45, 0.72), 7.1, 0.78, facecolor="white", edgecolor=PALETTE["gold"], lw=2))
    ax.text(
        5.0,
        1.11,
        "contract fails if used_symbols and glossary_symbols\ndo not match exactly",
        ha="center",
        va="center",
        fontsize=10.4,
        color=PALETTE["ink"],
        linespacing=1.1,
    )
    ax.text(5.0, 5.25, f"{counts['claims']} formal claims share one glossary contract", ha="center", fontsize=12, color=PALETTE["muted"])
    ax.set_title("Symbol glossary closure keeps every formal mark defined and every definition used", fontsize=16, color=PALETTE["ink"], pad=16)
    return _save(fig, output_dir / "symbol_glossary_closure.png")

def draw_text_validation_ladder(output_dir: Path) -> Path:
    fig, ax = plt.subplots(figsize=(11, 6.8))
    _clean_axes(ax)
    ax.set_xlim(0, 10.4)
    ax.set_ylim(0, 6)
    ax.set_facecolor(PALETTE["paper"])

    layers = [
        ("source records", "quadrants / figures / formalisms / symbols", topic_pair("source")[0]),
        ("analysis artifacts", "conceptual report + figure registry", topic_pair("formal")[0]),
        ("injected tokens", "counts, glossary, claims, integrity token", topic_pair("practice")[0]),
        ("rendered manuscript", "PDF / HTML / slides from hydrated text", topic_pair("limit")[0]),
        ("validation gates", f"{len(text_validation_checks())} contract checks", PALETTE["ink"]),
    ]
    y_positions = [5.15, 4.05, 2.95, 1.85, 0.75]
    for (title, subtitle, color), y in zip(layers, y_positions, strict=True):
        fill = {
            PALETTE["blue"]: PALETTE["blue_fill"],
            PALETTE["green"]: PALETTE["green_fill"],
            PALETTE["gold"]: PALETTE["gold_fill"],
            PALETTE["red"]: PALETTE["red_fill"],
            PALETTE["purple"]: PALETTE["purple_fill"],
        }.get(color, "white")
        ax.add_patch(Rectangle((1.45, y - 0.35), 6.25, 0.72, facecolor=fill, edgecolor=color, lw=2))
        ax.text(1.75, y + 0.12, title, ha="left", va="center", fontsize=12.2, color=color, weight="bold")
        ax.text(1.75, y - 0.16, subtitle, ha="left", va="center", fontsize=9.8, color=PALETTE["muted"])
    for start_y, end_y in zip(y_positions[:-1], y_positions[1:], strict=True):
        _arrow(ax, (4.58, start_y - 0.42), (4.58, end_y + 0.42), color=PALETTE["muted"], lw=1.4)

    ax.add_patch(Rectangle((8.08, 2.2), 1.72, 1.48, facecolor="white", edgecolor=PALETTE["line"], lw=1.5))
    ax.text(8.94, 3.05, "the text is\nvalidated as an\nartifact surface", ha="center", va="center", fontsize=10.5, color=PALETTE["muted"], linespacing=1.12)
    _arrow(ax, (7.72, 2.95), (8.05, 2.95), color=PALETTE["line"], lw=1.3, mutation_scale=13)
    ax.set_title("Text validation ladder binds source records to rendered manuscript surfaces", fontsize=16, color=PALETTE["ink"], pad=16)
    return _save(fig, output_dir / "text_validation_ladder.png")
