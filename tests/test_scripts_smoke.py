import json
from pathlib import Path
import subprocess
import sys

from src.conceptual_model import claim_grounding, figure_specs, formal_claims, symbol_glossary, text_validation_checks
from src.documentation import build_api_reference_markdown
from src.project_paths import project_output_dirs


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def _run_script(name: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(PROJECT_ROOT / "scripts" / name)],
        cwd=PROJECT_ROOT,
        check=True,
        capture_output=True,
        text=True,
    )


def test_project_output_dirs_include_render_surfaces() -> None:
    dirs = project_output_dirs(PROJECT_ROOT)
    assert set(dirs) == {"output", "figures", "data", "reports", "web"}


def test_canonical_publication_build_help() -> None:
    result = subprocess.run(
        [sys.executable, str(PROJECT_ROOT / "scripts" / "build_publication_package.py"), "--help"],
        cwd=PROJECT_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "--dry-run" in result.stdout


def test_api_reference_markdown_reports_concept_counts() -> None:
    text = build_api_reference_markdown()
    assert "Tinbergen quadrants: 4" in text
    assert f"Generated figures: {len(figure_specs())}" in text
    assert f"Formal claims: {len(formal_claims())}" in text
    assert f"Symbol glossary rows: {len(symbol_glossary())}" in text
    assert f"Text-validation checks: {len(text_validation_checks())}" in text


def test_analysis_and_hydration_scripts_smoke() -> None:
    manuscript_dir = PROJECT_ROOT / "output" / "manuscript"
    variables_path = PROJECT_ROOT / "output" / "data" / "manuscript_variables.json"
    metadata_paths = (
        PROJECT_ROOT / "output" / "reports" / "conceptual_analysis.json",
        PROJECT_ROOT / "output" / "data" / "conceptual_map.json",
    )
    manuscript_snapshot = {
        path: path.read_bytes() for path in manuscript_dir.iterdir() if path.is_file()
    }
    variables_snapshot = variables_path.read_bytes()
    metadata_snapshot = {path: path.read_bytes() for path in metadata_paths}
    try:
        analysis = _run_script("optimization_analysis.py")
        assert "conceptual_analysis.json" in analysis.stdout
        hydration = _run_script("z_generate_manuscript_variables.py")
        assert "manuscript_variables.json" in hydration.stdout

        variables = json.loads(variables_path.read_text(encoding="utf-8"))
        assert "deterministic illustrative simulation trace" in variables["SIMULATION_POLICY"]
        assert "stochastic simulations" in variables["SIMULATION_POLICY"]
        assert len(variables["CONCEPTUAL_INTEGRITY_TOKEN"]) == 16
        assert not any("{{" in path.read_text(encoding="utf-8") for path in manuscript_dir.glob("*.md"))
    finally:
        for path in manuscript_dir.iterdir():
            if path.is_file() and path not in manuscript_snapshot:
                path.unlink()
        for path, content in manuscript_snapshot.items():
            path.write_bytes(content)
        variables_path.write_bytes(variables_snapshot)
        for path, content in metadata_snapshot.items():
            path.write_bytes(content)


def test_dashboard_and_docs_scripts_smoke() -> None:
    web_figures = PROJECT_ROOT / "output" / "web" / "figures"
    stale = web_figures / "legacy_stale_figure.png"
    web_figures.mkdir(parents=True, exist_ok=True)
    stale.write_bytes(b"stale")
    dashboard = _run_script("build_dashboard.py")
    assert "dashboard.html" in dashboard.stdout
    assert "dashboard_data.json" in dashboard.stdout
    dashboard_html = (PROJECT_ROOT / "output" / "web" / "dashboard.html").read_text(encoding="utf-8")
    assert "The upper chain is deliberately too easy to extend" in dashboard_html
    assert "Claim Grounding" in dashboard_html
    assert "<link rel='icon' href='favicon.ico'>" in dashboard_html
    assert not stale.exists()
    dashboard_data = json.loads((PROJECT_ROOT / "output" / "web" / "dashboard_data.json").read_text(encoding="utf-8"))
    assert dashboard_data["schema"] == "prior_cognitive_art.dashboard_data.v1"
    assert dashboard_data["counts"]["Grounding Edges"] == len(claim_grounding())
    assert all((web_figures / spec.filename).exists() for spec in figure_specs())
    assert (PROJECT_ROOT / "output" / "web" / "cover" / "prior_cognitive_art_cover_square.png").exists()
    docs = _run_script("generate_api_docs.py")
    assert "api_reference.md" in docs.stdout
