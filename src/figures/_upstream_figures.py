from __future__ import annotations

from pathlib import Path

from ._shared import PALETTE, Circle, Rectangle, _arrow, _box, _clean_axes, _save, plt, topic_pair


def draw_first_prior_grounding_stack(output_dir: Path) -> Path:
    fig, ax = plt.subplots(figsize=(13.0, 7.4))
    _clean_axes(ax)
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 7.4)
    ax.set_facecolor(PALETTE["paper"])

    ax.text(
        6.5,
        7.03,
        "Before the first prior: constraint history, not a hidden meta-prior",
        ha="center",
        va="center",
        fontsize=17,
        color=PALETTE["ink"],
        weight="bold",
    )
    ax.text(
        6.5,
        6.55,
        "The upstream answer is not another belief above belief. It is the ordered field that makes priors possible.",
        ha="center",
        va="center",
        fontsize=10.9,
        color=PALETTE["muted"],
    )

    layers = [
        (
            "viability\nasymmetry",
            "must stay bounded,\nenergized, repairable",
            "viability",
            1.35,
            4.45,
        ),
        (
            "homeostatic /\nallostatic control",
            "bodily regulation\nanticipates demand",
            "function",
            3.88,
            4.45,
        ),
        (
            "co-embodiment /\nco-homeostasis",
            "early regulation is\nshared before owned",
            "cohomeostasis",
            6.5,
            4.45,
        ),
        (
            "developmental\ntuning",
            "channels become\nexpectation-forming",
            "development",
            9.12,
            4.45,
        ),
        (
            "learned and\ncultural priors",
            "art and niche craft\nmake expectations public",
            "art",
            11.65,
            4.45,
        ),
    ]
    for title, subtitle, topic, x, y in layers:
        edge, face = topic_pair(topic)
        _box(ax, (x, y), (2.05, 1.15), edge, title, subtitle, face=face, title_size=10.1, subtitle_size=8.0)

    for (_, _, topic, x0, y0), (_, _, next_topic, x1, y1) in zip(layers[:-1], layers[1:], strict=True):
        _arrow(ax, (x0 + 1.08, y0), (x1 - 1.08, y1), color=topic_pair(next_topic)[0], lw=1.55, mutation_scale=15)

    ax.add_patch(Rectangle((0.72, 2.35), 11.56, 0.82, facecolor="white", edgecolor=topic_pair("limit")[0], lw=2))
    ax.text(
        6.5,
        2.76,
        "RedTeam boundary: do not smuggle in a prior-before-priors. Upstream bias means constraint, regulation, and shared embodiment before explicit belief.",
        ha="center",
        va="center",
        fontsize=10.7,
        color=PALETTE["ink"],
    )

    left_edge, left_face = topic_pair("regress")
    ax.add_patch(Circle((2.1, 1.25), 0.72, facecolor=left_face, edgecolor=left_edge, lw=2.2))
    ax.text(2.1, 1.4, "question", ha="center", va="center", fontsize=10.5, color=left_edge, weight="bold")
    ax.text(2.1, 1.06, "what grounds\nfirst prior?", ha="center", va="center", fontsize=8.8, color=PALETTE["ink"], linespacing=1.0)

    answer_edge, answer_face = topic_pair("first_prior")
    ax.add_patch(Circle((6.5, 1.25), 0.92, facecolor=answer_face, edgecolor=answer_edge, lw=2.4))
    ax.text(6.5, 1.48, "answer", ha="center", va="center", fontsize=11, color=answer_edge, weight="bold")
    ax.text(
        6.5,
        1.12,
        "a layered\nconstraint stack",
        ha="center",
        va="center",
        fontsize=10.0,
        color=PALETTE["ink"],
        linespacing=1.0,
    )

    end_edge, end_face = topic_pair("fixed_point")
    ax.add_patch(Circle((10.9, 1.25), 0.72, facecolor=end_face, edgecolor=end_edge, lw=2.2))
    ax.text(10.9, 1.4, "stop", ha="center", va="center", fontsize=10.5, color=end_edge, weight="bold")
    ax.text(10.9, 1.06, "category\nshift", ha="center", va="center", fontsize=8.8, color=PALETTE["ink"], linespacing=1.0)

    _arrow(ax, (2.85, 1.25), (5.5, 1.25), color=answer_edge, lw=1.65, mutation_scale=15)
    _arrow(ax, (7.47, 1.25), (10.15, 1.25), color=end_edge, lw=1.65, mutation_scale=15)
    _arrow(ax, (6.5, 2.17), (6.5, 3.86), color=answer_edge, lw=1.4, mutation_scale=14)

    ax.text(
        6.5,
        0.36,
        "First-principles reading: before inferential priors come viability gradients, regulatory control, shared bodily support, and developmental niche structure.",
        ha="center",
        va="center",
        fontsize=9.4,
        color=PALETTE["muted"],
    )
    return _save(fig, output_dir / "first_prior_grounding_stack.png")
