from __future__ import annotations

import hashlib
import json
import os
import platform
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

from ._runtime import get_logger
from .conceptual_model import (
    argument_modules,
    claim_dependencies,
    claim_grounding,
    conceptual_integrity_token,
    deterministic_simulation_trace,
    figure_specs,
    formal_claims,
    quadrant_grid,
    symbol_glossary,
    termination_catalog,
    text_validation_checks,
)

logger = get_logger(__name__)


def _build_timestamp() -> str:
    epoch = os.environ.get("SOURCE_DATE_EPOCH", "").strip()
    if epoch.isdigit():
        return datetime.fromtimestamp(int(epoch), tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _load_config(project_root: Path) -> dict[str, Any]:
    config_path = project_root / "docs" / "manuscript" / "config.yaml"
    if not config_path.exists():
        logger.warning("Config file not found: %s", config_path)
        return {}
    with config_path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}


def _load_json_report(project_root: Path, name: str) -> dict[str, Any]:
    report_path = project_root / "output" / "reports" / name
    if not report_path.exists():
        logger.warning("Report not found: %s", report_path)
        return {}
    with report_path.open("r", encoding="utf-8") as handle:
        result: dict[str, Any] = json.load(handle)
        return result


def _compute_config_hash(project_root: Path) -> str:
    config_path = project_root / "docs" / "manuscript" / "config.yaml"
    if not config_path.exists():
        return "N/A"
    return hashlib.sha256(config_path.read_bytes()).hexdigest()[:16]


def _count_output_artifacts(project_root: Path) -> dict[str, int]:
    suffixes_by_dir: dict[str, set[str]] = {
        "figures": {".png", ".pdf", ".svg", ".jpg", ".jpeg"},
        "data": {".csv", ".npz", ".json", ".parquet"},
        "reports": {".json", ".md", ".html", ".txt"},
    }
    counts: dict[str, int] = {}
    output_dir = project_root / "output"
    for subdir, suffixes in suffixes_by_dir.items():
        dir_path = output_dir / subdir
        if dir_path.exists():
            counts[subdir] = sum(
                1
                for path in dir_path.iterdir()
                if path.is_file()
                and path.name != "render_manifest.json"
                and path.suffix.lower() in suffixes
            )
        else:
            counts[subdir] = 0
    return counts


def _markdown_quadrant_rows() -> str:
    rows = []
    for quadrant in quadrant_grid():
        rows.append(
            f"| {quadrant.label} | {quadrant.scale} | {quadrant.temporality} | "
            f"{quadrant.role} | {quadrant.regress_status} |"
        )
    return "\n".join(rows)


def _markdown_termination_bullets() -> str:
    bullets = []
    for termination in termination_catalog():
        bullets.append(
            f"- **{termination.name}** ({termination.stop_type}): "
            f"{termination.answer} Limitation: {termination.limitation}"
        )
    return "\n".join(bullets)


def _markdown_argument_modules() -> str:
    return "\n".join(f"- **{item.title}**: {item.claim}" for item in argument_modules())


def _markdown_figure_manifest() -> str:
    return "\n".join(f"- `{spec.filename}`: {spec.caption}" for spec in figure_specs())


def _figure_alt_text_variables() -> dict[str, str]:
    return {
        f"FIGURE_ALT_{spec.key.upper()}": spec.alt_text
        for spec in figure_specs()
    }


def _figure_section_counts() -> dict[str, int]:
    counts: dict[str, int] = {}
    for spec in figure_specs():
        counts[spec.section] = counts.get(spec.section, 0) + 1
    return counts


def _formal_claim_label(index: int) -> str:
    return f"F{index}"


def _symbol_claim_usage() -> dict[str, list[str]]:
    usage: dict[str, list[str]] = {symbol.key: [] for symbol in symbol_glossary()}
    for index, claim in enumerate(formal_claims(), start=1):
        label = _formal_claim_label(index)
        for symbol_key in claim.symbol_keys:
            usage[symbol_key].append(label)
    return usage


def _markdown_formal_claims() -> str:
    blocks: list[str] = []
    for index, claim in enumerate(formal_claims(), start=1):
        label = _formal_claim_label(index)
        blocks.append(f"### Formal Claim {label}: {claim.title}\n\n{claim.expression}\n\n{claim.reading}")
    return "\n\n".join(blocks)


def _markdown_symbol_glossary_rows() -> str:
    usage = _symbol_claim_usage()
    rows = []
    for symbol in symbol_glossary():
        claims = ", ".join(usage[symbol.key])
        rows.append(f"| {symbol.symbol} | {symbol.name} | {symbol.role} | {claims} |")
    return "\n".join(rows)


def _markdown_text_validation_rows() -> str:
    rows = []
    for check in text_validation_checks():
        rows.append(f"| `{check.key}` | {check.surface} | {check.invariant} | {check.evidence} |")
    return "\n".join(rows)


def _markdown_claim_dependencies() -> str:
    lines: list[str] = []
    for dep in claim_dependencies():
        lines.append(f"- **{dep.source_claim} → {dep.target_claim}**: {dep.rationale}")
    return "\n".join(lines)


def _markdown_claim_grounding() -> str:
    lines: list[str] = []
    claims = {claim.key: index for index, claim in enumerate(formal_claims(), start=1)}
    for grounding in claim_grounding():
        lines.append(f"- `{grounding.source_record}` → **F{claims[grounding.claim_key]}** ({grounding.claim_key})")
    return "\n".join(lines)


def generate_variables(project_root: Path, *, require_analysis_outputs: bool = False) -> dict[str, str]:
    config = _load_config(project_root)
    report = _load_json_report(project_root, "conceptual_analysis.json")
    if require_analysis_outputs and not report:
        report_path = project_root / "output" / "reports" / "conceptual_analysis.json"
        raise FileNotFoundError(
            f"Analysis outputs required but missing or empty: {report_path}. "
            "Run prior_cognitive_art/scripts/optimization_analysis.py first."
        )

    artifact_counts = _count_output_artifacts(project_root)
    paper = config.get("paper", {})
    metadata = config.get("metadata", {})
    conceptual = metadata.get("conceptual", {})
    generation = report.get("generation", {})
    thesis = conceptual.get(
        "thesis",
        "A prior is not explained by stacking more priors; it is located by mechanism, function, history, and fixed-point organization.",
    )

    section_counts = _figure_section_counts()
    return {
        "PROJECT_TITLE": str(paper.get("title", "Prior Cognitive Art")),
        "PROJECT_SUBTITLE": str(paper.get("subtitle", "")),
        "CONFIG_VERSION": str(paper.get("version", "0.1.0")),
        "THESIS_SENTENCE": str(thesis),
        "PRIMARY_MODE": "plain text, deterministic conceptual visualizations, and one deterministic illustrative simulation trace",
        "SIMULATION_POLICY": (
            "The paper includes one deterministic illustrative simulation trace over authored formal states; "
            "it does not run stochastic simulations, synthetic-data experiments, empirical estimates, or performance benchmarks."
        ),
        "QUADRANT_COUNT": str(len(quadrant_grid())),
        "TERMINATION_COUNT": str(len(termination_catalog())),
        "ARGUMENT_MODULE_COUNT": str(len(argument_modules())),
        "FIGURE_COUNT": str(len(figure_specs())),
        "VISUAL_ATLAS_FIGURE_COUNT": str(section_counts.get("Visual Atlas", 0)),
        "FORMAL_SUPPLEMENT_FIGURE_COUNT": str(section_counts.get("Formal Supplement", 0)),
        "FORMAL_CLAIM_COUNT": str(len(formal_claims())),
        "SYMBOL_COUNT": str(len(symbol_glossary())),
        "TEXT_VALIDATION_COUNT": str(len(text_validation_checks())),
        "CLAIM_DEPENDENCY_COUNT": str(len(claim_dependencies())),
        "CLAIM_GROUNDING_COUNT": str(len(claim_grounding())),
        "DETERMINISTIC_SIMULATION_STEP_COUNT": str(len(deterministic_simulation_trace())),
        "QUADRANT_TABLE_ROWS": _markdown_quadrant_rows(),
        "TERMINATION_BULLETS": _markdown_termination_bullets(),
        "ARGUMENT_MODULES": _markdown_argument_modules(),
        "VISUALIZATION_MANIFEST": _markdown_figure_manifest(),
        "FORMAL_CLAIMS": _markdown_formal_claims(),
        "SYMBOL_GLOSSARY_ROWS": _markdown_symbol_glossary_rows(),
        "TEXT_VALIDATION_TABLE_ROWS": _markdown_text_validation_rows(),
        "CLAIM_DEPENDENCIES": _markdown_claim_dependencies(),
        "CLAIM_GROUNDING": _markdown_claim_grounding(),
        "CONCEPTUAL_INTEGRITY_TOKEN": conceptual_integrity_token(),
        "CONCEPTUAL_REPORT_STATUS": "available" if report else "draft",
        "PYTHON_VERSION": str(generation.get("python_version", platform.python_version())),
        "PLATFORM": str(generation.get("platform", platform.platform())),
        "GENERATION_TIMESTAMP": str(generation.get("generated_at", _build_timestamp())),
        "CONFIG_HASH": _compute_config_hash(project_root),
        "CONFIG_FIRST_AUTHOR": (config.get("authors") or [{}])[0].get("name", "Project Author"),
        "CONFIG_KEYWORDS": ", ".join(config.get("keywords", [])),
        "ARTIFACT_FIGURES": str(artifact_counts.get("figures", 0)),
        "ARTIFACT_DATA_FILES": str(artifact_counts.get("data", 0)),
        "ARTIFACT_REPORTS": str(artifact_counts.get("reports", 0)),
        **_figure_alt_text_variables(),
    }


def save_variables(variables: dict[str, str], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as handle:
        json.dump(variables, handle, indent=2, sort_keys=True)
