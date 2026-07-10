import json
from pathlib import Path
import subprocess
import sys

from src.conceptual_model import figure_specs, formal_claims, symbol_glossary, text_validation_checks
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


def test_api_reference_markdown_reports_concept_counts() -> None:
    text = build_api_reference_markdown()
    assert "Tinbergen quadrants: 4" in text
    assert f"Generated figures: {len(figure_specs())}" in text
    assert f"Formal claims: {len(formal_claims())}" in text
    assert f"Symbol glossary rows: {len(symbol_glossary())}" in text
    assert f"Text-validation checks: {len(text_validation_checks())}" in text


def test_analysis_and_hydration_scripts_smoke() -> None:
    analysis = _run_script("optimization_analysis.py")
    assert "conceptual_analysis.json" in analysis.stdout
    hydration = _run_script("z_generate_manuscript_variables.py")
    assert "manuscript_variables.json" in hydration.stdout

    variables_path = PROJECT_ROOT / "output" / "data" / "manuscript_variables.json"
    variables = json.loads(variables_path.read_text(encoding="utf-8"))
    assert "deterministic illustrative simulation trace" in variables["SIMULATION_POLICY"]
    assert "stochastic simulations" in variables["SIMULATION_POLICY"]
    assert len(variables["CONCEPTUAL_INTEGRITY_TOKEN"]) == 16
    assert not any("{{" in path.read_text(encoding="utf-8") for path in (PROJECT_ROOT / "output" / "manuscript").glob("*.md"))


def test_dashboard_and_docs_scripts_smoke() -> None:
    dashboard = _run_script("build_dashboard.py")
    assert "dashboard.html" in dashboard.stdout
    assert "dashboard_data.json" in dashboard.stdout
    dashboard_html = (PROJECT_ROOT / "output" / "web" / "dashboard.html").read_text(encoding="utf-8")
    assert "The upper chain is deliberately too easy to extend" in dashboard_html
    web_figures = PROJECT_ROOT / "output" / "web" / "figures"
    assert all((web_figures / spec.filename).exists() for spec in figure_specs())
    assert (PROJECT_ROOT / "output" / "web" / "cover" / "prior_cognitive_art_cover_square.png").exists()
    docs = _run_script("generate_api_docs.py")
    assert "api_reference.md" in docs.stdout
