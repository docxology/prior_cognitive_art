import json
from pathlib import Path
import re

import pytest

from src.manuscript_variables import generate_variables, save_variables


def _write_minimal_project(root: Path) -> None:
    (root / "manuscript").mkdir(parents=True)
    (root / "output" / "reports").mkdir(parents=True)
    (root / "manuscript" / "config.yaml").write_text(
        "paper:\n"
        '  title: "Prior Cognitive Art"\n'
        '  subtitle: "Tinbergen Axes"\n'
        '  version: "0.1.0"\n'
        "authors:\n"
        '  - name: "Daniel Ari Friedman"\n'
        "keywords:\n"
        '  - "priors"\n'
        "metadata:\n"
        "  conceptual:\n"
        '    thesis: "A prior is located by crossed explanatory axes."\n',
        encoding="utf-8",
    )
    (root / "output" / "reports" / "conceptual_analysis.json").write_text(
        json.dumps({"simulation_free": True}),
        encoding="utf-8",
    )


def test_generate_variables_uses_concept_inventory(tmp_path: Path) -> None:
    _write_minimal_project(tmp_path)
    variables = generate_variables(tmp_path, require_analysis_outputs=True)
    assert variables["PROJECT_TITLE"] == "Prior Cognitive Art"
    assert variables["QUADRANT_COUNT"] == "4"
    assert variables["TERMINATION_COUNT"] == "3"
    assert variables["FIGURE_COUNT"] == "18"
    assert variables["FORMAL_CLAIM_COUNT"] == "11"
    assert variables["SYMBOL_COUNT"] == "25"
    assert variables["TEXT_VALIDATION_COUNT"] == "10"
    assert "Ontogeny" in variables["QUADRANT_TABLE_ROWS"]
    assert "fixed-point" in variables["TERMINATION_BULLETS"]
    assert "Formal Claim F1" in variables["FORMAL_CLAIMS"]
    assert "$Q_T$" in variables["SYMBOL_GLOSSARY_ROWS"]
    assert "integrity_signature" in variables["TEXT_VALIDATION_TABLE_ROWS"]
    assert len(variables["CONCEPTUAL_INTEGRITY_TOKEN"]) == 16
    assert variables["CLAIM_DEPENDENCY_COUNT"] == "12"
    assert "axis_partition" in variables["CLAIM_DEPENDENCIES"]
    assert "regress_shape" in variables["CLAIM_DEPENDENCIES"]


def test_generate_variables_requires_analysis_report(tmp_path: Path) -> None:
    (tmp_path / "manuscript").mkdir()
    (tmp_path / "manuscript" / "config.yaml").write_text("paper:\n  title: Draft\n", encoding="utf-8")
    with pytest.raises(FileNotFoundError):
        generate_variables(tmp_path, require_analysis_outputs=True)


def test_save_variables_writes_sorted_json(tmp_path: Path) -> None:
    out_path = tmp_path / "output" / "data" / "manuscript_variables.json"
    save_variables({"B": "2", "A": "1"}, out_path)
    assert out_path.read_text(encoding="utf-8").splitlines()[1].strip().startswith('"A"')


def test_all_manuscript_tokens_are_generated() -> None:
    project_root = Path(__file__).resolve().parents[1]
    variables = generate_variables(project_root, require_analysis_outputs=False)
    tokens: set[str] = set()
    for manuscript_file in (project_root / "manuscript").glob("*.md"):
        tokens.update(re.findall(r"\{\{([A-Z0-9_]+)\}\}", manuscript_file.read_text(encoding="utf-8")))
    assert tokens
    assert tokens <= set(variables)
