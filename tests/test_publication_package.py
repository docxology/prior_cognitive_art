from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

from src.conceptual_model import as_records, deterministic_simulation_trace, figure_specs
from src.render_manifest import build_render_manifest, validate_render_manifest
from src.rendering import apply_project_web_style
from scripts.validate_publication_package import (
    _check_dashboard_data,
    _check_deterministic_trace_contract,
    _check_documented_inventory_claims,
    _check_figure_artifacts,
    _check_hydrated_manuscript,
    _check_validation_report,
    validate_publication_package,
)


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = PROJECT_ROOT / "scripts" / "validate_publication_package.py"


def test_publication_package_validator_help() -> None:
    result = subprocess.run(
        [sys.executable, str(SCRIPT), "--help"],
        cwd=PROJECT_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "--project-root" in result.stdout


def test_publication_package_validator_passes_current_package() -> None:
    result = subprocess.run(
        [sys.executable, str(SCRIPT), "--json"],
        cwd=PROJECT_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr
    payload = json.loads(result.stdout)
    assert payload["ok"] is True
    assert payload["expected_counts"]["figure_count"] == len(figure_specs())


def test_publication_package_validator_rejects_missing_root() -> None:
    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--project-root",
            "/tmp/does-not-exist-prior-cognitive-art",
        ],
        cwd=PROJECT_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 1
    assert "project root does not exist" in result.stderr


def test_publication_package_helpers_reject_forged_artifacts(tmp_path: Path) -> None:
    figure_dir = tmp_path / "output" / "figures"
    figure_dir.mkdir(parents=True)
    (figure_dir / "figure.png").write_bytes(b"not-a-png")
    (figure_dir / "figure.svg").write_text("<svg></svg>", encoding="utf-8")
    issues: list[str] = []
    _check_figure_artifacts(tmp_path, 1, ("figure.png",), issues)
    assert any("invalid or undersized PNG" in issue for issue in issues)

    missing_issues: list[str] = []
    _check_figure_artifacts(tmp_path, 1, ("missing.png",), missing_issues)
    assert any("generated PNG filenames do not match" in issue for issue in missing_issues)

    reports_dir = tmp_path / "output" / "reports"
    reports_dir.mkdir(parents=True)
    (reports_dir / "validation_report.json").write_text("[]", encoding="utf-8")
    report_issues: list[str] = []
    _check_validation_report(tmp_path, report_issues)
    assert "validation_report.json must be a JSON object" in report_issues


def test_publication_package_rejects_deterministic_trace_coordinate_drift() -> None:
    expected_steps = as_records(deterministic_simulation_trace())
    forged_steps = [dict(step) for step in expected_steps]
    forged_steps[0]["x"] = float(forged_steps[0]["x"]) + 1.0
    issues: list[str] = []
    _check_deterministic_trace_contract(
        {
            "schema": "prior_cognitive_art.deterministic_simulation_trace.v1",
            "steps": forged_steps,
        },
        expected_steps,
        issues,
    )
    assert any("step 0 field x" in issue for issue in issues)


def test_publication_package_rejects_dashboard_payload_drift() -> None:
    path = PROJECT_ROOT / "output" / "web" / "dashboard_data.json"
    original = path.read_bytes()
    payload = json.loads(original)
    payload["counts"]["Grounding Edges"] += 1
    path.write_text(json.dumps(payload), encoding="utf-8")
    try:
        issues: list[str] = []
        _check_dashboard_data(PROJECT_ROOT, issues)
    finally:
        path.write_bytes(original)
    assert "dashboard_data.json counts drifts from source inventory" in issues


def test_publication_package_rejects_figure_metadata_drift() -> None:
    path = PROJECT_ROOT / "output" / "figures" / "figure_registry.json"
    original = path.read_bytes()
    payload = json.loads(original)
    payload["fig:tinbergen_axes"]["alt_text"] = "forged accessibility text"
    path.write_text(json.dumps(payload), encoding="utf-8")
    try:
        issues: list[str] = []
        from scripts.validate_publication_package import _check_counts

        _check_counts(PROJECT_ROOT, issues)
    finally:
        path.write_bytes(original)
    assert "figure_registry.json metadata drift for tinbergen_axes" in issues


def test_publication_package_rejects_wrong_figure_section() -> None:
    path = PROJECT_ROOT / "output" / "figures" / "figure_registry.json"
    original = path.read_bytes()
    payload = json.loads(original)
    payload["fig:tinbergen_axes"]["section"] = "Formal Supplement"
    path.write_text(json.dumps(payload), encoding="utf-8")
    try:
        issues: list[str] = []
        from scripts.validate_publication_package import _check_counts

        _check_counts(PROJECT_ROOT, issues)
    finally:
        path.write_bytes(original)
    assert "figure_registry.json metadata drift for tinbergen_axes" in issues


def test_publication_package_rejects_hydrated_alt_text_drift() -> None:
    path = PROJECT_ROOT / "output" / "manuscript" / "03_results.md"
    original = path.read_bytes()
    text = path.read_text(encoding="utf-8")
    text = text.replace("Four colored panels arrange mechanism", "FORGED alt text", 1)
    path.write_text(text, encoding="utf-8")
    try:
        issues: list[str] = []
        _check_hydrated_manuscript(PROJECT_ROOT, issues)
    finally:
        path.write_bytes(original)
    assert "hydrated manuscript alt text drift for tinbergen_axes" in issues


def test_publication_package_rejects_stale_render_manifest() -> None:
    path = PROJECT_ROOT / "output" / "reports" / "render_manifest.json"
    original = path.read_bytes()
    payload = json.loads(original)
    payload["source_digest"] = "0" * 64
    path.write_text(json.dumps(payload), encoding="utf-8")
    try:
        from src.render_manifest import validate_render_manifest

        issues = validate_render_manifest(PROJECT_ROOT)
    finally:
        path.write_bytes(original)
    assert any("source_digest" in issue for issue in issues)


def test_publication_package_rejects_simulation_manifest_drift() -> None:
    path = PROJECT_ROOT / "output" / "reports" / "deterministic_simulation_manifest.json"
    original = path.read_bytes()
    payload = json.loads(original)
    payload["trace_path"] = "output/data/stale_trace.json"
    path.write_text(json.dumps(payload), encoding="utf-8")
    try:
        ok, issues, _ = validate_publication_package(PROJECT_ROOT)
    finally:
        path.write_bytes(original)
    assert ok is False
    assert "deterministic_simulation_manifest.json trace_path is stale" in issues


def test_publication_package_rejects_documented_inventory_drift() -> None:
    path = PROJECT_ROOT / "README.md"
    original = path.read_text(encoding="utf-8")
    path.write_text(original.replace("| Generated figures | 21 |", "| Generated figures | 20 |"), encoding="utf-8")
    try:
        issues: list[str] = []
        _check_documented_inventory_claims(
            PROJECT_ROOT,
            {
                "figure_count": len(figure_specs()),
                "formal_claim_count": 12,
                "symbol_count": 35,
                "text_validation_count": 11,
                "claim_dependency_count": 14,
                "claim_grounding_count": 12,
            },
            issues,
        )
    finally:
        path.write_text(original, encoding="utf-8")
    assert "README.md missing documented inventory claim '| Generated figures | 21 |'" in issues


def test_render_manifest_matches_current_outputs() -> None:
    manifest = build_render_manifest(PROJECT_ROOT)
    assert manifest["schema"] == "prior_cognitive_art.render_manifest.v1"
    assert manifest["source_files"]
    assert manifest["outputs"]
    assert validate_render_manifest(PROJECT_ROOT) == []


def test_render_manifest_rejects_invalid_schema(tmp_path: Path) -> None:
    reports = tmp_path / "output" / "reports"
    reports.mkdir(parents=True)
    (reports / "render_manifest.json").write_text('{"schema": "forged"}', encoding="utf-8")
    assert validate_render_manifest(tmp_path) == ["render_manifest.json schema is stale or invalid"]


def test_project_web_style_is_idempotent_and_requires_head(tmp_path: Path) -> None:
    manuscript = tmp_path / "manuscript"
    web = tmp_path / "output" / "web"
    manuscript.mkdir(parents=True)
    web.mkdir(parents=True)
    (manuscript / "web.css").write_text("body { color: #111; }", encoding="utf-8")
    index = web / "index.html"
    index.write_text("<html><head></head><body></body></html>", encoding="utf-8")

    assert apply_project_web_style(tmp_path) == [index]
    first = index.read_text(encoding="utf-8")
    assert 'data-prior-cognitive-art-layout="compact"' in first
    assert apply_project_web_style(tmp_path) == [index]
    assert index.read_text(encoding="utf-8") == first

    broken = web / "manuscript__broken.html"
    broken.write_text("<html><body></body></html>", encoding="utf-8")
    try:
        apply_project_web_style(tmp_path)
    except ValueError as exc:
        assert "no </head> insertion point" in str(exc)
    else:
        raise AssertionError("missing </head> must be rejected")
