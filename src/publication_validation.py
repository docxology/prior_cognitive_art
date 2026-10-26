"""Publication-package validation against source-owned counts.

Moved verbatim from scripts/validate_publication_package.py so the logic is
importable and tested; the script is a thin orchestrator around
:func:`validate_publication_package`.
"""

from __future__ import annotations

import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parent.parent


def _load_project_modules(project_root: Path) -> None:
    sys.path.insert(0, str(project_root))


def _load_json(path: Path, issues: list[str]) -> Any:
    label = str(path)
    try:
        label = str(path.relative_to(PROJECT_ROOT))
    except ValueError:
        pass
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        issues.append(f"missing required JSON artifact: {label}")
    except json.JSONDecodeError as exc:
        issues.append(f"invalid JSON in {label}: {exc}")
    return None


def _require_files(project_root: Path, relative_paths: tuple[str, ...], issues: list[str]) -> None:
    for relative_path in relative_paths:
        path = project_root / relative_path
        if not path.exists():
            issues.append(f"missing required artifact: {relative_path}")
        elif path.is_file() and path.stat().st_size == 0:
            issues.append(f"empty required artifact: {relative_path}")


def _check_counts(project_root: Path, issues: list[str]) -> dict[str, int]:
    _load_project_modules(project_root)
    from src.conceptual_model import (  # noqa: PLC0415
        as_records,
        argument_modules,
        claim_dependencies,
        claim_grounding,
        deterministic_simulation_trace,
        figure_specs,
        formal_claims,
        conceptual_integrity_token,
        quadrant_grid,
        symbol_glossary,
        termination_catalog,
        text_validation_checks,
        validate_claim_dependencies,
        validate_conceptual_contract,
    )

    expected = {
        "figure_count": len(figure_specs()),
        "formal_claim_count": len(formal_claims()),
        "symbol_count": len(symbol_glossary()),
        "text_validation_count": len(text_validation_checks()),
        "claim_dependency_count": len(claim_dependencies()),
        "claim_grounding_count": len(claim_grounding()),
        "deterministic_simulation_step_count": len(deterministic_simulation_trace()),
    }

    for error in validate_conceptual_contract():
        issues.append(f"conceptual contract error: {error}")
    for error in validate_claim_dependencies():
        issues.append(f"claim dependency error: {error}")

    report = _load_json(project_root / "output/reports/conceptual_analysis.json", issues)
    if report is not None and not isinstance(report, dict):
        issues.append("conceptual_analysis.json must be a JSON object")
    if isinstance(report, dict):
        for key, expected_value in expected.items():
            if report.get(key) != expected_value:
                issues.append(
                    f"conceptual_analysis.json {key}={report.get(key)!r}; expected {expected_value}"
                )
        if report.get("simulation_free") is not True:
            issues.append("conceptual_analysis.json must preserve simulation_free=true")
        for key in (
            "deterministic_illustrative_simulation",
            "empirical_simulation_free",
            "stochastic_simulation_free",
        ):
            if report.get(key) is not True:
                issues.append(f"conceptual_analysis.json must preserve {key}=true")
        if "no stochastic sampling" not in str(report.get("simulation_scope", "")):
            issues.append("conceptual_analysis.json simulation_scope must reject stochastic sampling")
        if report.get("contract_errors") not in ([], ()):
            issues.append("conceptual_analysis.json reports contract_errors")
        if report.get("claim_dependency_errors") not in ([], ()):
            issues.append("conceptual_analysis.json reports claim_dependency_errors")
        if report.get("claim_grounding_errors") not in ([], ()):
            issues.append("conceptual_analysis.json reports claim_grounding_errors")
        expected_sections = {
            "Visual Atlas": sum(1 for spec in figure_specs() if spec.section == "Visual Atlas"),
            "Formal Supplement": sum(1 for spec in figure_specs() if spec.section == "Formal Supplement"),
        }
        if report.get("figure_section_counts") != expected_sections:
            issues.append("conceptual_analysis.json figure_section_counts drift from source inventory")
        generation = report.get("generation")
        if not isinstance(generation, dict) or not all(generation.get(key) for key in ("generated_at", "python_version", "platform")):
            issues.append("conceptual_analysis.json generation metadata is incomplete")
        expected_records = {
            "quadrants": as_records(quadrant_grid()),
            "terminations": as_records(termination_catalog()),
            "argument_modules": as_records(argument_modules()),
            "formal_claims": as_records(formal_claims()),
            "claim_dependencies": as_records(claim_dependencies()),
            "claim_grounding": as_records(claim_grounding()),
            "symbol_glossary": as_records(symbol_glossary()),
            "text_validation_checks": as_records(text_validation_checks()),
            "deterministic_simulation_trace": as_records(deterministic_simulation_trace()),
            "figures": as_records(figure_specs()),
        }
        for key, expected_value in expected_records.items():
            if report.get(key) != json.loads(json.dumps(expected_value)):
                issues.append(f"conceptual_analysis.json {key} records drift from source inventory")
        if report.get("conceptual_integrity_token") != conceptual_integrity_token():
            issues.append("conceptual_analysis.json conceptual_integrity_token drifts from source inventory")

    conceptual_map = _load_json(project_root / "output/data/conceptual_map.json", issues)
    if conceptual_map is not None and not isinstance(conceptual_map, dict):
        issues.append("conceptual_map.json must be a JSON object")
    if isinstance(report, dict) and isinstance(conceptual_map, dict) and conceptual_map != report:
        issues.append("conceptual_map.json drifts from conceptual_analysis.json")

    trace = _load_json(project_root / "output/data/deterministic_simulation_trace.json", issues)
    if trace is not None and not isinstance(trace, dict):
        issues.append("deterministic_simulation_trace.json must be a JSON object")
    if isinstance(trace, dict):
        if len(trace.get("steps", [])) != expected["deterministic_simulation_step_count"]:
            issues.append("deterministic_simulation_trace.json step count does not match source")
        if "no stochastic sampling" not in str(trace.get("scope", "")):
            issues.append("deterministic_simulation_trace.json scope must reject stochastic sampling")
        _check_deterministic_trace_contract(
            trace,
            as_records(deterministic_simulation_trace()),
            issues,
        )

    simulation_manifest = _load_json(project_root / "output/reports/deterministic_simulation_manifest.json", issues)
    if simulation_manifest is not None and not isinstance(simulation_manifest, dict):
        issues.append("deterministic_simulation_manifest.json must be a JSON object")
    if isinstance(simulation_manifest, dict):
        if simulation_manifest.get("schema") != "prior_cognitive_art.deterministic_simulation_manifest.v1":
            issues.append("deterministic_simulation_manifest.json schema is stale")
        if simulation_manifest.get("step_count") != expected["deterministic_simulation_step_count"]:
            issues.append("deterministic_simulation_manifest.json step_count does not match source")
        if simulation_manifest.get("trace_path") != "output/data/deterministic_simulation_trace.json":
            issues.append("deterministic_simulation_manifest.json trace_path is stale")
        if simulation_manifest.get("source") != "src/conceptual_model.py:deterministic_simulation_trace":
            issues.append("deterministic_simulation_manifest.json source is stale")
        for key in (
            "deterministic_illustrative_simulation",
            "empirical_simulation_free",
            "stochastic_simulation_free",
            "performance_claims_free",
        ):
            if simulation_manifest.get(key) is not True:
                issues.append(f"deterministic_simulation_manifest.json must preserve {key}=true")

    expected_figure_paths = [f"output/figures/{spec.filename}" for spec in figure_specs()]
    manifest = _load_json(project_root / "output/reports/figure_manifest.json", issues)
    if manifest is not None and not isinstance(manifest, dict):
        issues.append("figure_manifest.json must be a JSON object")
    if isinstance(manifest, dict) and manifest.get("figures") != expected_figure_paths:
        issues.append("figure_manifest.json paths do not match source figure_specs() in order")

    registry = _load_json(project_root / "output/figures/figure_registry.json", issues)
    if registry is not None and not isinstance(registry, dict):
        issues.append("figure_registry.json must be a JSON object")
    if isinstance(registry, dict):
        expected_labels = {f"fig:{spec.key}" for spec in figure_specs()}
        if set(registry) != expected_labels:
            issues.append("figure_registry.json labels do not match source figure_specs()")
        for index, spec in enumerate(figure_specs()):
            entry = registry.get(f"fig:{spec.key}")
            if not isinstance(entry, dict):
                continue
            if entry.get("filename") != spec.filename:
                issues.append(f"figure_registry.json filename drift for {spec.key}")
            if entry.get("caption") != spec.caption:
                issues.append(f"figure_registry.json caption drift for {spec.key}")
            if entry.get("metadata", {}).get("purpose") != spec.purpose:
                issues.append(f"figure_registry.json purpose drift for {spec.key}")
            expected_entry = {
                "figure_id": f"figure_{index:03d}",
                "filename": spec.filename,
                "caption": spec.caption,
                "label": f"fig:{spec.key}",
                "alt_text": spec.alt_text,
                "section": spec.section,
                "width": "0.86\\textwidth",
                "placement": "h",
                "generated_by": "optimization_analysis.py",
                "metadata": {"purpose": spec.purpose},
            }
            if entry != expected_entry:
                issues.append(f"figure_registry.json metadata drift for {spec.key}")

    variables = _load_json(project_root / "output/data/manuscript_variables.json", issues)
    if variables is not None and not isinstance(variables, dict):
        issues.append("manuscript_variables.json must be a JSON object")
    if isinstance(variables, dict):
        variable_map = {
            "FIGURE_COUNT": expected["figure_count"],
            "FORMAL_CLAIM_COUNT": expected["formal_claim_count"],
            "SYMBOL_COUNT": expected["symbol_count"],
            "TEXT_VALIDATION_COUNT": expected["text_validation_count"],
            "CLAIM_DEPENDENCY_COUNT": expected["claim_dependency_count"],
            "CLAIM_GROUNDING_COUNT": expected["claim_grounding_count"],
        }
        for key, expected_value in variable_map.items():
            if str(variables.get(key)) != str(expected_value):
                issues.append(f"manuscript_variables.json {key}={variables.get(key)!r}; expected {expected_value}")
        if isinstance(report, dict) and isinstance(report.get("generation"), dict):
            generation = report["generation"]
            for variable_key, generation_key in (
                ("GENERATION_TIMESTAMP", "generated_at"),
                ("PYTHON_VERSION", "python_version"),
                ("PLATFORM", "platform"),
            ):
                if str(variables.get(variable_key)) != str(generation.get(generation_key)):
                    issues.append(f"manuscript_variables.json {variable_key} does not match conceptual_analysis.json generation metadata")
        section_counts = {
            "VISUAL_ATLAS_FIGURE_COUNT": sum(1 for spec in figure_specs() if spec.section == "Visual Atlas"),
            "FORMAL_SUPPLEMENT_FIGURE_COUNT": sum(1 for spec in figure_specs() if spec.section == "Formal Supplement"),
        }
        for key, expected_value in section_counts.items():
            if str(variables.get(key)) != str(expected_value):
                issues.append(f"manuscript_variables.json {key}={variables.get(key)!r}; expected {expected_value}")
        for spec in figure_specs():
            key = f"FIGURE_ALT_{spec.key.upper()}"
            if variables.get(key) != spec.alt_text:
                issues.append(f"manuscript_variables.json {key} drifts from source FigureSpec.alt_text")

    return expected


def _check_deterministic_trace_contract(
    trace: dict[str, Any],
    expected_steps: list[dict[str, object]],
    issues: list[str],
) -> None:
    if trace.get("schema") != "prior_cognitive_art.deterministic_simulation_trace.v1":
        issues.append("deterministic_simulation_trace.json schema is stale")

    actual_steps = trace.get("steps")
    if not isinstance(actual_steps, list):
        issues.append("deterministic_simulation_trace.json steps must be a list")
        return

    expected_order = list(range(len(expected_steps)))
    actual_order = [step.get("step") for step in actual_steps if isinstance(step, dict)]
    if actual_order != expected_order:
        issues.append(
            f"deterministic_simulation_trace.json step order={actual_order!r}; "
            f"expected {expected_order!r}"
        )

    source_owned_fields = ("step", "state", "formal_state", "transition", "invariant", "x", "y")
    for index, expected_step in enumerate(expected_steps):
        if index >= len(actual_steps) or not isinstance(actual_steps[index], dict):
            continue
        actual_step = actual_steps[index]
        for field in source_owned_fields:
            if actual_step.get(field) != expected_step[field]:
                issues.append(
                    "deterministic_simulation_trace.json "
                    f"step {index} field {field}={actual_step.get(field)!r}; "
                    f"expected {expected_step[field]!r}"
                )

    forbidden_step_terms = (
        "random",
        "stochastic",
        "monte carlo",
        "synthetic data",
        "empirical effect",
        "effect size",
        "performance metric",
        "benchmark",
    )
    for index, actual_step in enumerate(actual_steps):
        if not isinstance(actual_step, dict):
            continue
        step_text = " ".join(str(actual_step.get(field, "")) for field in source_owned_fields).lower()
        for term in forbidden_step_terms:
            if term in step_text:
                issues.append(
                    "deterministic_simulation_trace.json "
                    f"step {index} uses forbidden empirical/simulation term {term!r}"
                )


def _check_dashboard_data(project_root: Path, issues: list[str]) -> None:
    payload = _load_json(project_root / "output/web/dashboard_data.json", issues)
    if payload is not None and not isinstance(payload, dict):
        issues.append("dashboard_data.json must be a JSON object")
        return
    if not isinstance(payload, dict):
        return

    _load_project_modules(project_root)
    from src.conceptual_model import (  # noqa: PLC0415
        argument_modules,
        as_records,
        claim_dependencies,
        claim_grounding,
        conceptual_integrity_token,
        figure_specs,
        formal_claims,
        quadrant_grid,
        symbol_glossary,
        termination_catalog,
        text_validation_checks,
    )

    expected = {
        "schema": "prior_cognitive_art.dashboard_data.v1",
        "title": "Prior Cognitive Art",
        "integrity_token": conceptual_integrity_token(),
        "contract_errors": [],
        "counts": {
            "Quadrants": len(quadrant_grid()),
            "Terminations": len(termination_catalog()),
            "Arguments": len(argument_modules()),
            "Figures": len(figure_specs()),
            "Formal Claims": len(formal_claims()),
            "Symbols": len(symbol_glossary()),
            "Validation Checks": len(text_validation_checks()),
            "Claim Dependencies": len(claim_dependencies()),
            "Grounding Edges": len(claim_grounding()),
        },
        "argument_modules": [module.title for module in argument_modules()],
        "terminations": [termination.name for termination in termination_catalog()],
        "figures": [spec.filename for spec in figure_specs()],
        "figure_sections": {
            section: [spec.filename for spec in figure_specs() if spec.section == section]
            for section in sorted({spec.section for spec in figure_specs()})
        },
        "figure_section_counts": {
            section: sum(1 for spec in figure_specs() if spec.section == section)
            for section in sorted({spec.section for spec in figure_specs()})
        },
        "figure_metadata": {
            f"fig:{spec.key}": {
                "filename": spec.filename,
                "caption": spec.caption,
                "alt_text": spec.alt_text,
                "section": spec.section,
            }
            for spec in figure_specs()
        },
        "claim_grounding": as_records(claim_grounding()),
        "cover_art": "cover/prior_cognitive_art_cover_square.png",
    }
    for key, expected_value in expected.items():
        if payload.get(key) != expected_value:
            issues.append(f"dashboard_data.json {key} drifts from source inventory")


def _check_documented_inventory_claims(
    project_root: Path,
    expected: dict[str, int],
    issues: list[str],
) -> None:
    _load_project_modules(project_root)
    from src.conceptual_model import argument_modules, quadrant_grid, termination_catalog  # noqa: PLC0415

    try:
        import yaml  # noqa: PLC0415
    except ImportError:
        issues.append("PyYAML is required to validate documented inventory claims")
        return

    ledger_path = project_root / "data/claim_ledger.yaml"
    bib_path = project_root / "docs/manuscript/references.bib"
    try:
        ledger = yaml.safe_load(ledger_path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as exc:
        issues.append(f"cannot parse claim ledger for documented counts: {exc}")
        ledger = {}
    try:
        bib_text = bib_path.read_text(encoding="utf-8", errors="replace")
    except OSError as exc:
        issues.append(f"cannot read references.bib for documented counts: {exc}")
        bib_text = ""

    documented = {
        "Tinbergen quadrants": len(quadrant_grid()),
        "Termination modes": len(termination_catalog()),
        "Argument modules": len(argument_modules()),
        "Generated figures": expected["figure_count"],
        "Figures": expected["figure_count"],
        "Formal claims": expected["formal_claim_count"],
        "Symbols": expected["symbol_count"],
        "Symbol glossary rows": expected["symbol_count"],
        "Text checks": expected["text_validation_count"],
        "Text-validation checks": expected["text_validation_count"],
        "Claim dependencies": expected["claim_dependency_count"],
        "Claim dependency edges": expected["claim_dependency_count"],
        "Claim grounding edges": expected["claim_grounding_count"],
        "Claim-grounding edges": expected["claim_grounding_count"],
        "Claim ledger": len(ledger.get("claims", [])) if isinstance(ledger, dict) else 0,
        "Bibliography": len(re.findall(r"@\w+\{([^,\s]+)", bib_text)),
    }
    surfaces = (
        project_root / "README.md",
        project_root / "TODO.md",
        project_root / "docs/publication_readiness_report.md",
        project_root / "docs/audit/documentation-audit-report.md",
    )
    required_claims = {
        "README.md": (
            ("Tinbergen quadrants", "| Tinbergen quadrants | {value} |"),
            ("Termination modes", "| Termination modes | {value} |"),
            ("Argument modules", "| Argument modules | {value} |"),
            ("Generated figures", "| Generated figures | {value} |"),
            ("Formal claims", "| Formal claims | {value} |"),
            ("Symbol glossary rows", "| Symbol glossary rows | {value} |"),
            ("Text-validation checks", "| Text-validation checks | {value} |"),
            ("Claim dependencies", "| Claim dependencies | {value} |"),
            ("Claim grounding edges", "| Claim grounding edges | {value} |"),
        ),
        "TODO.md": (
            ("Generated figures", "{value} generated figures"),
            ("Argument modules", "{value} argument\nmodules"),
            ("Formal claims", "{value} formal claims"),
            ("Claim ledger", "{value} claim-ledger records"),
            ("Symbol glossary rows", "{value}-row symbol glossary"),
            ("Text-validation checks", "{value} text-validation checks"),
            ("Claim dependency edges", "{value} claim dependency edges"),
            ("Claim-grounding edges", "{value} claim-grounding edges"),
            ("Bibliography", "{value} BibTeX records"),
        ),
        "docs/publication_readiness_report.md": (
            ("Figures", "Figures: {value} deterministic conceptual figures"),
            ("Argument modules", "Argument modules: {value} records"),
            ("Formal claims", "Formal claims: {value} records"),
            ("Claim ledger", "Claim ledger: {value} records"),
            ("Symbols", "Symbols: {value} glossary rows"),
            ("Text checks", "Text checks: {value} validation checks"),
            ("Claim dependency edges", "Claim dependency edges: {value}."),
            ("Claim-grounding edges", "Claim-grounding edges: {value}."),
            ("Bibliography", "Bibliography: {value} BibTeX records"),
        ),
        "docs/audit/documentation-audit-report.md": (
            ("Bibliography", "Bibliography bidirectional closure | **Closed**: {value} entries, {value} cited"),
            ("Generated figures", "Generated-artifact count vs docs | **{value} PNGs** = {value} claimed"),
        ),
    }
    stale_paths = (
        "/Users/4d/Documents/GitHub",
        "projects/working/prior_cognitive_art",
    )

    for path in surfaces:
        try:
            text = path.read_text(encoding="utf-8")
        except OSError as exc:
            issues.append(f"cannot read documented inventory surface {path.relative_to(project_root)}: {exc}")
            continue
        if any(pattern in text for pattern in stale_paths):
            issues.append(f"{path.relative_to(project_root)} contains stale template-side project path")
        for label, template in required_claims.get(str(path.relative_to(project_root)), ()):
            expected_text = template.format(value=documented[label])
            if expected_text not in text:
                issues.append(
                    f"{path.relative_to(project_root)} missing documented inventory claim {expected_text!r}"
                )


def _check_figure_artifacts(
    project_root: Path,
    expected_figure_count: int,
    expected_filenames: tuple[str, ...],
    issues: list[str],
) -> None:
    figure_dir = project_root / "output/figures"
    pngs = sorted(figure_dir.glob("*.png"))
    svgs = sorted(figure_dir.glob("*.svg"))
    if len(pngs) != expected_figure_count:
        issues.append(f"expected {expected_figure_count} PNG figures, found {len(pngs)}")
    if len(svgs) != expected_figure_count:
        issues.append(f"expected {expected_figure_count} SVG figures, found {len(svgs)}")
    expected_pngs = set(expected_filenames)
    expected_svgs = {Path(filename).with_suffix(".svg").name for filename in expected_filenames}
    actual_pngs = {path.name for path in pngs}
    actual_svgs = {path.name for path in svgs}
    if actual_pngs != expected_pngs:
        issues.append("generated PNG filenames do not match source figure_specs()")
    if actual_svgs != expected_svgs:
        issues.append("generated SVG filenames do not match source figure_specs()")
    for path in [*pngs, *svgs]:
        if path.stat().st_size == 0:
            issues.append(f"empty figure artifact: {path.relative_to(project_root)}")
    for path in pngs:
        dimensions = _png_dimensions(path)
        if dimensions is None or min(dimensions) < 100:
            issues.append(f"invalid or undersized PNG figure: {path.relative_to(project_root)}")
    for path in svgs:
        if not _valid_svg(path):
            issues.append(f"invalid SVG figure: {path.relative_to(project_root)}")


def _png_dimensions(path: Path) -> tuple[int, int] | None:
    try:
        from PIL import Image  # noqa: PLC0415

        with Image.open(path) as image:
            image.verify()
        with Image.open(path) as image:
            return image.size
    except (FileNotFoundError, ImportError, OSError, SyntaxError, ValueError):
        return None


def _valid_svg(path: Path) -> bool:
    try:
        root = ET.fromstring(path.read_text(encoding="utf-8"))
    except (FileNotFoundError, ET.ParseError, UnicodeDecodeError):
        return False
    return root.tag.rsplit("}", 1)[-1].lower() == "svg"


def _check_cover_art(project_root: Path, issues: list[str]) -> None:
    png_path = project_root / "output/cover/prior_cognitive_art_cover_square.png"
    svg_path = project_root / "output/cover/prior_cognitive_art_cover_square.svg"
    manifest_path = project_root / "output/reports/cover_art_manifest.json"
    for path in (png_path, svg_path, manifest_path):
        if not path.exists():
            issues.append(f"missing cover-art artifact: {path.relative_to(project_root)}")
        elif path.stat().st_size == 0:
            issues.append(f"empty cover-art artifact: {path.relative_to(project_root)}")

    dimensions = _png_dimensions(png_path)
    if dimensions != (2048, 2048):
        issues.append(f"cover PNG dimensions={dimensions!r}; expected (2048, 2048)")

    manifest = _load_json(manifest_path, issues)
    if manifest is not None and not isinstance(manifest, dict):
        issues.append("cover_art_manifest.json must be a JSON object")
    if isinstance(manifest, dict):
        if manifest.get("format") != "square":
            issues.append("cover_art_manifest.json format must be square")
        if manifest.get("width_px") != 2048 or manifest.get("height_px") != 2048:
            issues.append("cover_art_manifest.json must record 2048 x 2048 dimensions")
        if manifest.get("png") != "output/cover/prior_cognitive_art_cover_square.png":
            issues.append("cover_art_manifest.json png path is stale")
        if manifest.get("svg") != "output/cover/prior_cognitive_art_cover_square.svg":
            issues.append("cover_art_manifest.json svg path is stale")
        if manifest.get("filename") != "prior_cognitive_art_cover_square.png":
            issues.append("cover_art_manifest.json filename is stale")
        if manifest.get("svg_filename") != "prior_cognitive_art_cover_square.svg":
            issues.append("cover_art_manifest.json svg_filename is stale")
    if svg_path.exists() and not _valid_svg(svg_path):
        issues.append("cover SVG is not a valid SVG artifact")


def _check_validation_report(project_root: Path, issues: list[str]) -> None:
    report = _load_json(project_root / "output/reports/validation_report.json", issues)
    if report is None:
        return
    if not isinstance(report, dict):
        issues.append("validation_report.json must be a JSON object")
        return
    summary = report.get("summary")
    checks = report.get("checks")
    if not isinstance(summary, dict) or summary.get("all_passed") is not True or summary.get("failed") != 0:
        issues.append("validation_report.json must report all_passed=true and failed=0")
    if not isinstance(checks, dict) or not checks or any(value is not True for value in checks.values()):
        issues.append("validation_report.json checks must be a non-empty all-true object")


def _check_pdf(project_root: Path, issues: list[str]) -> None:
    path = project_root / "output/pdf/prior_cognitive_art_combined.pdf"
    if not path.exists():
        return
    try:
        payload = path.read_bytes()
    except OSError:
        issues.append("combined PDF cannot be read")
        return
    if not payload.startswith(b"%PDF-") or b"%%EOF" not in payload[-2048:]:
        issues.append("combined PDF failed structural header/EOF validation")


def _check_hydrated_manuscript(project_root: Path, issues: list[str]) -> None:
    source_files = {path.name for path in (project_root / "docs" / "manuscript").glob("[0-9][0-9]_*.md")}
    output_dir = project_root / "output/manuscript"
    for name in sorted(source_files):
        path = output_dir / name
        if not path.exists():
            issues.append(f"missing hydrated manuscript section: output/manuscript/{name}")
        elif not path.read_text(encoding="utf-8", errors="replace").strip():
            issues.append(f"empty hydrated manuscript section: output/manuscript/{name}")

    _load_project_modules(project_root)
    from src.conceptual_model import figure_specs  # noqa: PLC0415

    hydrated = {
        path.name: path.read_text(encoding="utf-8", errors="replace")
        for path in output_dir.glob("[0-9][0-9]_*.md")
        if path.exists()
    }
    for spec in figure_specs():
        marker = f"(../output/figures/{spec.filename}){{#fig:{spec.key}}}"
        pattern = re.compile(rf"!\[([^\]]*)\]{re.escape(marker)}")
        matches = [
            alt_text
            for manuscript_text in hydrated.values()
            for alt_text in pattern.findall(manuscript_text)
        ]
        if not matches:
            issues.append(f"hydrated manuscript is missing figure reference for {spec.key}")
        elif matches != [spec.alt_text]:
            issues.append(f"hydrated manuscript alt text drift for {spec.key}")


def _check_scholarship_audit_keys(project_root: Path, issues: list[str]) -> None:
    audit_path = project_root / "docs/scholarship-audit.md"
    bib_path = project_root / "docs/manuscript/references.bib"
    if not audit_path.exists() or not bib_path.exists():
        return
    bib_keys = set(re.findall(r"@\w+\{([^,\s]+)", bib_path.read_text(encoding="utf-8", errors="replace")))
    for line_number, line in enumerate(audit_path.read_text(encoding="utf-8", errors="replace").splitlines(), start=1):
        if not line.startswith("|"):
            continue
        first_cell = line.split("|", 2)[1]
        for key in re.findall(r"`([a-z][a-z0-9_]+)`", first_cell):
            if key not in bib_keys:
                issues.append(f"scholarship-audit.md line {line_number} references missing BibTeX key {key!r}")


def _check_rendered_tokens(project_root: Path, issues: list[str]) -> None:
    token_surfaces = [
        *sorted((project_root / "output/web").glob("*.html")),
        *sorted((project_root / "output/manuscript").glob("*.md")),
    ]
    unresolved_tokens = ("{{", "}}")
    html_only_tokens = ("[@",)

    for path in token_surfaces:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for token in unresolved_tokens:
            if token in text:
                issues.append(f"unresolved template token {token!r} in {path.relative_to(project_root)}")
        if path.suffix == ".html":
            for token in html_only_tokens:
                if token in text:
                    issues.append(f"unresolved citation marker {token!r} in {path.relative_to(project_root)}")

    bib_path = project_root / "docs/manuscript/references.bib"
    html_paths = [project_root / "output/web/index.html", project_root / "output/web/dashboard.html"]
    if bib_path.exists() and any(path.exists() for path in html_paths):
        bib_keys = re.findall(r"@\w+\{([^,\s]+)", bib_path.read_text(encoding="utf-8", errors="replace"))
        for html_path in html_paths:
            if not html_path.exists():
                continue
            html_text = html_path.read_text(encoding="utf-8", errors="replace")
            for key in bib_keys:
                if f"[{key}" in html_text or f"; {key}" in html_text:
                    issues.append(f"rendered HTML exposes raw citation key: {key}")


def validate_publication_package(project_root: Path) -> tuple[bool, list[str], dict[str, int]]:
    project_root = project_root.resolve()
    issues: list[str] = []
    if not project_root.exists():
        return False, [f"project root does not exist: {project_root}"], {}

    required = (
        "README.md",
        "TODO.md",
        "CITATION.cff",
        "codemeta.json",
        ".zenodo.json",
        "docs/publication_readiness_report.md",
        "docs/submission_package.md",
        "docs/reviewer_risk_register.md",
        "docs/cover_letter_template.md",
        "docs/venue_selection_matrix.md",
        "docs/preprint_release_checklist.md",
        "docs/scholarship-audit.md",
        "data/claim_ledger.yaml",
        "docs/manuscript/config.yaml",
        "docs/manuscript/references.bib",
        "output/pdf/prior_cognitive_art_combined.pdf",
        "output/web/index.html",
        "output/web/dashboard.html",
        "output/web/dashboard_data.json",
        "output/docs/api_reference.md",
        "output/docs/api_glossary.md",
        "output/reports/conceptual_analysis.json",
        "output/reports/figure_manifest.json",
        "output/reports/cover_art_manifest.json",
        "output/reports/deterministic_simulation_manifest.json",
        "output/reports/render_manifest.json",
        "output/reports/validation_report.md",
        "output/data/deterministic_simulation_trace.json",
        "output/data/conceptual_map.json",
        "output/data/manuscript_variables.json",
        "output/figures/figure_registry.json",
        "output/reports/validation_report.json",
    )
    _require_files(project_root, required, issues)
    expected = _check_counts(project_root, issues)
    if expected:
        _load_project_modules(project_root)
        from src.conceptual_model import figure_specs  # noqa: PLC0415

        specs = figure_specs()
        _check_figure_artifacts(project_root, expected["figure_count"], tuple(spec.filename for spec in specs), issues)
    _check_cover_art(project_root, issues)
    _check_pdf(project_root, issues)
    _check_hydrated_manuscript(project_root, issues)
    _check_validation_report(project_root, issues)
    _check_scholarship_audit_keys(project_root, issues)
    _check_rendered_tokens(project_root, issues)
    _load_project_modules(project_root)
    from src.render_manifest import validate_render_manifest  # noqa: PLC0415

    issues.extend(validate_render_manifest(project_root))
    _check_dashboard_data(project_root, issues)
    if expected:
        _check_documented_inventory_claims(project_root, expected, issues)
    return not issues, issues, expected
