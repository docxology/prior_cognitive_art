from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

from src.conceptual_model import figure_specs


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
