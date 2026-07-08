"""Pytest configuration for prior_cognitive_art tests."""

import os
import sys

# Force headless backend for matplotlib in tests
os.environ.setdefault("MPLBACKEND", "Agg")

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC = os.path.join(ROOT, "src")
candidate_roots = [
    os.getcwd(),
    os.path.abspath(os.path.join(ROOT, "..", "..", "..")),
    os.path.abspath(os.path.join(ROOT, "..", "..", "..", "template")),
]
REPO_ROOT = next((path for path in candidate_roots if os.path.isdir(os.path.join(path, "infrastructure"))), candidate_roots[1])
for _path in (REPO_ROOT, SRC):
    if _path not in sys.path:
        sys.path.insert(0, _path)
