"""Freshness manifest for the generated manuscript render surfaces."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any


RENDER_MANIFEST_SCHEMA = "prior_cognitive_art.render_manifest.v1"
_FINGERPRINT_RE = re.compile(r"<!-- prior-cognitive-art-render-input: ([0-9a-f]{64}) -->\n*")


def _manuscript_paths(project_root: Path) -> list[Path]:
    return sorted((project_root / "output" / "manuscript").glob("[0-9][0-9]_*.md"))


def _without_fingerprint(text: str) -> str:
    return _FINGERPRINT_RE.sub("", text, count=1)


def _hash_paths(project_root: Path, paths: list[Path]) -> str:
    digest = hashlib.sha256()
    for path in paths:
        digest.update(str(path.relative_to(project_root)).encode("utf-8"))
        digest.update(b"\0")
        text = path.read_text(encoding="utf-8")
        digest.update(_without_fingerprint(text).encode("utf-8"))
        digest.update(b"\0")
    return digest.hexdigest()


def render_input_digest(project_root: Path) -> str:
    """Hash the ordered hydrated manuscript while ignoring its marker."""

    paths = _manuscript_paths(project_root)
    if not paths:
        raise FileNotFoundError(f"no hydrated manuscript sections under {project_root / 'output/manuscript'}")
    return _hash_paths(project_root, paths)


def stamp_render_input_fingerprint(project_root: Path) -> str:
    """Stamp hydrated Markdown with the digest the renderer must consume."""

    paths = _manuscript_paths(project_root)
    digest = render_input_digest(project_root)
    first = paths[0]
    clean = _without_fingerprint(first.read_text(encoding="utf-8"))
    marker = f"<!-- prior-cognitive-art-render-input: {digest} -->\n\n"
    first.write_text(marker + clean, encoding="utf-8")
    return digest


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _render_output_paths(project_root: Path) -> list[Path]:
    output = project_root / "output"
    candidates = [
        output / "web" / "_combined_manuscript.md",
        *sorted((output / "web").glob("*.html")),
        output / "web" / "index.html",
        output / "pdf" / "_combined_manuscript.md",
        output / "pdf" / "prior_cognitive_art_combined.pdf",
        *sorted((output / "slides").glob("*.pdf")),
    ]
    return list(dict.fromkeys(path for path in candidates if path.exists()))


def build_render_manifest(project_root: Path) -> dict[str, Any]:
    project_root = project_root.resolve()
    source_paths = _manuscript_paths(project_root)
    source_digest = render_input_digest(project_root)
    outputs = _render_output_paths(project_root)
    return {
        "schema": RENDER_MANIFEST_SCHEMA,
        "source_digest": source_digest,
        "source_files": [str(path.relative_to(project_root)) for path in source_paths],
        "render_fingerprints": {
            str(path.relative_to(project_root)): _extract_fingerprint(path)
            for path in (
                project_root / "output" / "web" / "_combined_manuscript.md",
                project_root / "output" / "pdf" / "_combined_manuscript.md",
            )
            if path.exists()
        },
        "outputs": {
            str(path.relative_to(project_root)): _sha256(path)
            for path in outputs
        },
    }


def _extract_fingerprint(path: Path) -> str | None:
    match = _FINGERPRINT_RE.search(path.read_text(encoding="utf-8", errors="replace"))
    return match.group(1) if match else None


def write_render_manifest(project_root: Path) -> Path:
    path = project_root / "output" / "reports" / "render_manifest.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(build_render_manifest(project_root), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return path


def validate_render_manifest(project_root: Path) -> list[str]:
    """Return blocking freshness issues for generated render surfaces."""

    project_root = project_root.resolve()
    path = project_root / "output" / "reports" / "render_manifest.json"
    if not path.exists():
        return ["missing output/reports/render_manifest.json"]
    try:
        manifest = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"cannot parse output/reports/render_manifest.json: {exc}"]

    issues: list[str] = []
    if not isinstance(manifest, dict) or manifest.get("schema") != RENDER_MANIFEST_SCHEMA:
        return ["render_manifest.json schema is stale or invalid"]
    try:
        current_digest = render_input_digest(project_root)
    except (FileNotFoundError, OSError) as exc:
        return [f"cannot hash hydrated manuscript for render freshness: {exc}"]
    if manifest.get("source_digest") != current_digest:
        issues.append("render_manifest.json source_digest does not match hydrated manuscript")

    current_sources = [str(path.relative_to(project_root)) for path in _manuscript_paths(project_root)]
    if manifest.get("source_files") != current_sources:
        issues.append("render_manifest.json source_files do not match hydrated manuscript")

    expected_fingerprints = manifest.get("render_fingerprints")
    if not isinstance(expected_fingerprints, dict):
        issues.append("render_manifest.json render_fingerprints is missing")
        expected_fingerprints = {}
    for relative in ("output/web/_combined_manuscript.md", "output/pdf/_combined_manuscript.md"):
        combined = project_root / relative
        fingerprint = _extract_fingerprint(combined) if combined.exists() else None
        if fingerprint != current_digest:
            issues.append(f"{relative} is stale relative to hydrated manuscript")
        if expected_fingerprints.get(relative) != fingerprint:
            issues.append(f"render_manifest.json fingerprint drifts for {relative}")

    expected_outputs = manifest.get("outputs")
    if not isinstance(expected_outputs, dict):
        issues.append("render_manifest.json outputs is missing")
        expected_outputs = {}
    current_outputs = {
        str(path.relative_to(project_root))
        for path in _render_output_paths(project_root)
    }
    if set(expected_outputs) != current_outputs:
        issues.append("render_manifest.json output set does not match rendered output files")
    for relative, expected_hash in expected_outputs.items():
        output = project_root / relative
        if not output.exists():
            issues.append(f"render output is missing: {relative}")
        elif _sha256(output) != expected_hash:
            issues.append(f"render output hash drift: {relative}")
    return issues


__all__ = [
    "RENDER_MANIFEST_SCHEMA",
    "build_render_manifest",
    "render_input_digest",
    "stamp_render_input_fingerprint",
    "validate_render_manifest",
    "write_render_manifest",
]
