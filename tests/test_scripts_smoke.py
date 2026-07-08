import json
from pathlib import Path
import subprocess
import sys

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
    assert "Generated figures: 18" in text
    assert "Formal claims: 11" in text
    assert "Symbol glossary rows: 25" in text
    assert "Text-validation checks: 10" in text


def test_analysis_and_hydration_scripts_smoke() -> None:
    analysis = _run_script("optimization_analysis.py")
    assert "conceptual_analysis.json" in analysis.stdout
    hydration = _run_script("z_generate_manuscript_variables.py")
    assert "manuscript_variables.json" in hydration.stdout

    variables_path = PROJECT_ROOT / "output" / "data" / "manuscript_variables.json"
    variables = json.loads(variables_path.read_text(encoding="utf-8"))
    assert variables["SIMULATION_POLICY"].startswith("No simulations")
    assert len(variables["CONCEPTUAL_INTEGRITY_TOKEN"]) == 16
    assert not any("{{" in path.read_text(encoding="utf-8") for path in (PROJECT_ROOT / "output" / "manuscript").glob("*.md"))


def test_dashboard_and_docs_scripts_smoke() -> None:
    dashboard = _run_script("build_dashboard.py")
    assert "dashboard.html" in dashboard.stdout
    assert "dashboard_data.json" in dashboard.stdout
    docs = _run_script("generate_api_docs.py")
    assert "api_reference.md" in docs.stdout
