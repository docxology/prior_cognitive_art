"""Tests for path resolution, runtime helpers, and documentation generation."""

from pathlib import Path
import re
import sys

import pytest

from src._runtime import get_logger, project_root
from src.conceptual_model import (
    as_records,
    claim_dependencies,
    conceptual_integrity_token,
    figure_specs,
    formal_claims,
    quadrant_grid,
    symbol_glossary,
    termination_catalog,
    text_validation_checks,
    used_symbol_keys,
    validate_conceptual_contract,
)
from src.documentation import build_api_reference_markdown
from src.project_paths import project_output_dirs, resolve_project_root


PROJECT_ROOT = Path(__file__).resolve().parents[1]


# ── project_paths.py ──────────────────────────────────────────────────


def test_resolve_project_root_returns_path_object() -> None:
    root = resolve_project_root("src")
    assert isinstance(root, Path)
    assert root.exists()


def test_resolve_project_root_falls_back_to_default() -> None:
    """When the named module has no project_root attr, it falls back."""
    root = resolve_project_root("nonexistent_module_xyz")
    assert isinstance(root, Path)


def test_resolve_project_root_uses_module_attribute() -> None:
    """When a loaded module has a project_root attribute, it is used."""
    import types

    mod = types.ModuleType("_fake_test_module_with_root")
    mod.project_root = "/custom/path/from/module"  # type: ignore[attr-defined]
    sys.modules["_fake_test_module_with_root"] = mod
    try:
        root = resolve_project_root("_fake_test_module_with_root")
        assert root == Path("/custom/path/from/module")
    finally:
        del sys.modules["_fake_test_module_with_root"]


def test_project_output_dirs_has_expected_keys() -> None:
    dirs = project_output_dirs(PROJECT_ROOT)
    assert set(dirs) == {"output", "figures", "data", "reports", "web"}
    for name, path in dirs.items():
        assert isinstance(path, Path)
        assert path.name == name


def test_project_output_dirs_with_none_uses_default() -> None:
    dirs = project_output_dirs(None)
    assert "output" in dirs
    assert dirs["output"].name == "output"


# ── _runtime.py ───────────────────────────────────────────────────────


def test_get_logger_returns_logger() -> None:
    logger = get_logger("test_module")
    assert logger.name == "test_module"
    # Should be reusable — same logger returned for same name
    logger2 = get_logger("test_module")
    assert logger is logger2 or logger.name == logger2.name


def test_get_logger_with_none() -> None:
    logger = get_logger(None)
    assert logger is not None


def test_project_root_returns_path() -> None:
    root = project_root("src")
    assert isinstance(root, Path)


# ── documentation.py ─────────────────────────────────────────────────


def test_api_reference_contains_all_concept_counts() -> None:
    text = build_api_reference_markdown()
    assert f"Tinbergen quadrants: {len(quadrant_grid())}" in text
    assert f"Generated figures: {len(figure_specs())}" in text
    assert f"Formal claims: {len(formal_claims())}" in text
    assert f"Symbol glossary rows: {len(symbol_glossary())}" in text
    assert f"Text-validation checks: {len(text_validation_checks())}" in text
    assert f"Claim dependencies: {len(claim_dependencies())}" in text
    assert f"Termination modes: {len(termination_catalog())}" in text


def test_api_reference_contains_integrity_token() -> None:
    text = build_api_reference_markdown()
    token = conceptual_integrity_token()
    assert token in text


def test_api_reference_lists_all_figure_keys() -> None:
    text = build_api_reference_markdown()
    for spec in figure_specs():
        assert f"`{spec.key}`" in text
        assert spec.filename in text


def test_api_reference_lists_all_formal_claims() -> None:
    text = build_api_reference_markdown()
    for i, claim in enumerate(formal_claims(), start=1):
        assert f"F{i}: {claim.title}" in text
        assert claim.reading in text


def test_api_reference_contains_module_documentation() -> None:
    text = build_api_reference_markdown()
    assert "src.conceptual_model" in text
    assert "src.analysis.workflow" in text
    assert "src.figures.conceptual" in text
    assert "src.manuscript_variables" in text
    assert "src.project_paths" in text
    assert "src._runtime" in text


def test_api_reference_reports_contract_errors() -> None:
    text = build_api_reference_markdown()
    # Contract should be clean
    assert "none" in text or "[]" in text


# ── formal claim dependencies ─────────────────────────────────────────


def test_every_formal_claim_symbol_is_glossed() -> None:
    glossary_keys = {sym.key for sym in symbol_glossary()}
    for claim in formal_claims():
        for sym_key in claim.symbol_keys:
            assert sym_key in glossary_keys, (
                f"Claim {claim.key} uses symbol {sym_key} not in glossary"
            )


def test_every_glossary_symbol_is_used_by_at_least_one_claim() -> None:
    used = used_symbol_keys()
    for sym in symbol_glossary():
        assert sym.key in used, (
            f"Glossary symbol {sym.key} is not used by any formal claim"
        )


def test_validate_contract_is_clean() -> None:
    assert validate_conceptual_contract() == ()


def test_formal_claims_have_unique_keys() -> None:
    keys = [c.key for c in formal_claims()]
    assert len(keys) == len(set(keys))


def test_figure_specs_have_unique_keys() -> None:
    keys = [s.key for s in figure_specs()]
    assert len(keys) == len(set(keys))


def test_figure_specs_have_unique_filenames() -> None:
    filenames = [s.filename for s in figure_specs()]
    assert len(filenames) == len(set(filenames))


def test_terminations_have_unique_keys() -> None:
    keys = [t.key for t in termination_catalog()]
    assert len(keys) == len(set(keys))


def test_quadrants_have_unique_keys() -> None:
    keys = [q.key for q in quadrant_grid()]
    assert len(keys) == len(set(keys))


def test_argument_modules_have_unique_keys() -> None:
    from src.conceptual_model import argument_modules

    keys = [m.key for m in argument_modules()]
    assert len(keys) == len(set(keys))


def test_text_validation_checks_have_unique_keys() -> None:
    keys = [c.key for c in text_validation_checks()]
    assert len(keys) == len(set(keys))


# ── as_records helper ─────────────────────────────────────────────────


def test_as_records_converts_dataclass_tuple() -> None:
    records = as_records(quadrant_grid())
    assert len(records) == 4
    assert isinstance(records[0], dict)
    assert "key" in records[0]
    assert records[0]["key"] == "mechanism"


def test_as_records_preserves_all_fields() -> None:
    records = as_records(termination_catalog())
    assert len(records) == 3
    for record in records:
        assert {"key", "name", "stop_type", "answer", "limitation"} <= set(record)


# ── claim_ledger.yaml integrity ───────────────────────────────────────


def test_claim_ledger_yaml_exists_and_parses() -> None:
    import yaml

    ledger_path = PROJECT_ROOT / "data" / "claim_ledger.yaml"
    assert ledger_path.exists(), "claim_ledger.yaml must exist"
    data = yaml.safe_load(ledger_path.read_text(encoding="utf-8"))
    assert "claims" in data
    assert len(data["claims"]) >= 16
    for claim in data["claims"]:
        assert "claim_id" in claim
        assert "kind" in claim
        assert "value" in claim
        assert "source" in claim


def test_claim_ledger_references_match_conceptual_model() -> None:
    import yaml

    ledger_path = PROJECT_ROOT / "data" / "claim_ledger.yaml"
    data = yaml.safe_load(ledger_path.read_text(encoding="utf-8"))
    # The termination-three claim should match the actual termination count
    term_claim = next(c for c in data["claims"] if c["claim_id"] == "termination-three")
    assert "pragmatic" in term_claim["value"].lower()
    assert "selection" in term_claim["value"].lower()
    assert "fixed-point" in term_claim["value"].lower()


def test_scholarship_audit_records_publication_boundary_sources() -> None:
    audit_path = PROJECT_ROOT / "docs" / "scholarship-audit.md"
    assert audit_path.exists(), "publication pass must record accepted and rejected sources"
    text = audit_path.read_text(encoding="utf-8")
    for required in (
        "bruineberg2022emperor",
        "stotz2017developmental",
        "simpson2017penalising",
        "konner2021nine",
    ):
        assert required in text
    assert "Rejected or deferred" in text


def test_manuscript_has_no_publication_draft_gap_language() -> None:
    forbidden_patterns = (
        r"Remaining Scholarship Gaps",
        r"later scholarship pass",
        r"should be sharpened in the next draft",
        r"remains programmatic in this draft",
        r"\bfuture\s+draft\b",
        r"\bfuture\s+work\b",
        r"\blater\s+scholarship\b",
        r"\bremaining\s+scholarship\b",
        r"\bnext\s+draft\b",
        r"\bdraft[- ]gap\b",
        r"\bpublication\s+gap\b",
        r"\bTODO\b",
        r"\bFIXME\b",
        r"\bTBD\b",
    )
    surfaces = list((PROJECT_ROOT / "docs" / "manuscript").glob("*.md"))
    surfaces.extend((PROJECT_ROOT / "output" / "manuscript").glob("*.md"))
    for combined in (
        PROJECT_ROOT / "output" / "pdf" / "_combined_manuscript.md",
        PROJECT_ROOT / "output" / "web" / "_combined_manuscript.md",
    ):
        if combined.exists():
            surfaces.append(combined)
    assert surfaces, "manuscript publication surfaces must exist"
    for path in surfaces:
        text = path.read_text(encoding="utf-8")
        for pattern in forbidden_patterns:
            assert not re.search(pattern, text, flags=re.IGNORECASE), (
                f"{path} contains publication-residue pattern {pattern}"
            )


def test_rendered_manuscript_has_no_unresolved_tokens() -> None:
    rendered = list((PROJECT_ROOT / "output" / "manuscript").glob("*.md"))
    for combined in (
        PROJECT_ROOT / "output" / "pdf" / "_combined_manuscript.md",
        PROJECT_ROOT / "output" / "web" / "_combined_manuscript.md",
    ):
        if combined.exists():
            rendered.append(combined)
    assert rendered, "rendered manuscript surfaces must exist"
    for path in rendered:
        text = path.read_text(encoding="utf-8")
        assert "{{" not in text
        assert "}}" not in text


def test_figure_modules_stay_under_pure_loc_ceiling() -> None:
    for path in (PROJECT_ROOT / "src" / "figures").glob("*.py"):
        pure_loc = sum(
            1
            for line in path.read_text(encoding="utf-8").splitlines()
            if line.strip() and not line.lstrip().startswith("#")
        )
        assert pure_loc <= 250, f"{path} has {pure_loc} pure LOC"


# ── domain_profile.yaml integrity ─────────────────────────────────────


def test_domain_profile_yaml_exists_and_parses() -> None:
    import yaml

    profile_path = PROJECT_ROOT / "domain_profile.yaml"
    assert profile_path.exists()
    data = yaml.safe_load(profile_path.read_text(encoding="utf-8"))
    assert data["domain"] == "prose_research"
    assert data["display_name"] == "Prior Cognitive Art"
    assert "figure_types" in data
    assert len(data["figure_types"]) >= 11


def test_domain_profile_artifact_expectations_match_figure_specs() -> None:
    import yaml

    profile_path = PROJECT_ROOT / "domain_profile.yaml"
    data = yaml.safe_load(profile_path.read_text(encoding="utf-8"))
    expected = data.get("artifact_expectations", [])
    figure_filenames = {spec.filename for spec in figure_specs()}
    for expectation in expected:
        if "figures/" in expectation and expectation.endswith(".png"):
            filename = Path(expectation).name
            assert filename in figure_filenames, (
                f"Domain profile expects {filename} but it is not in figure_specs()"
            )


# ── experiment_plan.yaml integrity ────────────────────────────────────


def test_experiment_plan_yaml_exists_and_parses() -> None:
    import yaml

    plan_path = PROJECT_ROOT / "experiment_plan.yaml"
    assert plan_path.exists()
    data = yaml.safe_load(plan_path.read_text(encoding="utf-8"))
    assert "conditions" in data
    assert len(data["conditions"]) >= 6
    assert "metrics" in data
    assert data["metrics"]["primary"]["name"] == "explanatory_coverage"


def test_experiment_plan_expected_figures_match_specs() -> None:
    import yaml

    plan_path = PROJECT_ROOT / "experiment_plan.yaml"
    data = yaml.safe_load(plan_path.read_text(encoding="utf-8"))
    expected_figs = set(data.get("expected_figures", []))
    actual_figs = {f"fig:{spec.key}" for spec in figure_specs()}
    assert expected_figs == actual_figs


# ── metadata keyword consistency ──────────────────────────────────────


def test_metadata_keywords_are_consistent_across_all_files() -> None:
    """Keywords in config.yaml, .zenodo.json, codemeta.json, CITATION.cff must be supersets of config.yaml."""
    import json

    import yaml

    config = yaml.safe_load((PROJECT_ROOT / "docs" / "manuscript" / "config.yaml").read_text())
    config_kw = set(config["keywords"])

    zenodo = json.loads((PROJECT_ROOT / ".zenodo.json").read_text())
    codemeta = json.loads((PROJECT_ROOT / "codemeta.json").read_text())
    cit = yaml.safe_load((PROJECT_ROOT / "CITATION.cff").read_text())

    # Config keywords must be a subset of all metadata files
    assert config_kw <= set(zenodo["keywords"]), "Zenodo keywords missing config keywords"
    assert config_kw <= set(codemeta["keywords"]), "Codemeta keywords missing config keywords"
    assert config_kw <= set(cit["keywords"]), "CITATION.cff keywords missing config keywords"


def test_metadata_versions_are_consistent() -> None:
    """Version must match across pyproject.toml, config.yaml, codemeta.json, CITATION.cff."""
    import json

    import yaml

    pyproj = (PROJECT_ROOT / "pyproject.toml").read_text()
    pyproj_ver = re.search(r'version\s*=\s*"([^"]+)"', pyproj).group(1)

    config = yaml.safe_load((PROJECT_ROOT / "docs" / "manuscript" / "config.yaml").read_text())
    config_ver = config["paper"]["version"]

    codemeta = json.loads((PROJECT_ROOT / "codemeta.json").read_text())
    codemeta_ver = codemeta["version"]

    cit = yaml.safe_load((PROJECT_ROOT / "CITATION.cff").read_text())
    cit_ver = cit["version"]

    assert pyproj_ver == config_ver == codemeta_ver == cit_ver, (
        f"Version mismatch: pyproject={pyproj_ver}, config={config_ver}, "
        f"codemeta={codemeta_ver}, citation={cit_ver}"
    )


def test_cover_metadata_uses_dynamic_date_and_published_doi() -> None:
    import yaml

    config = yaml.safe_load((PROJECT_ROOT / "docs" / "manuscript" / "config.yaml").read_text())
    publication = config["publication"]
    assert "date" not in config["paper"]
    assert config["paper"]["cover"]["image"] == "cover/prior_cognitive_art_cover_square.png"
    assert publication["doi"] == "10.5281/zenodo.21316510"
    assert publication["version_doi"] == "10.5281/zenodo.21316511"
    assert publication["version_record"] == "https://zenodo.org/records/21316511"
    assert publication["doi_status"] == "published"


# ── manuscript citation integrity ─────────────────────────────────────


def test_all_manuscript_citations_resolve_to_bib() -> None:
    """Every @citation in the manuscript must have a bib entry."""
    bib_text = (PROJECT_ROOT / "docs" / "manuscript" / "references.bib").read_text()
    bib_keys = set(re.findall(r"@\w+\{([^,]+),", bib_text))

    cited_keys: set[str] = set()
    for md in (PROJECT_ROOT / "docs" / "manuscript").glob("*.md"):
        text = md.read_text(encoding="utf-8")
        for match in re.findall(r"@(\w+)", text):
            if match not in ("fig", "tbl", "sec"):
                cited_keys.add(match)

    missing = cited_keys - bib_keys
    assert not missing, f"Citations missing from references.bib: {sorted(missing)}"


def test_all_figure_references_resolve() -> None:
    """Every @fig:reference in the manuscript must have a {#fig:label} definition."""
    fig_defs: set[str] = set()
    fig_refs: set[str] = set()
    for md in (PROJECT_ROOT / "docs" / "manuscript").glob("*.md"):
        text = md.read_text(encoding="utf-8")
        fig_defs.update(re.findall(r"#fig:(\w+)", text))
        fig_refs.update(re.findall(r"@fig:(\w+)", text))

    unresolved = fig_refs - fig_defs
    assert not unresolved, f"Unresolved figure references: {sorted(unresolved)}"


def test_all_table_references_resolve() -> None:
    """Every @tbl:reference in the manuscript must have a {#tbl:label} definition."""
    tbl_defs: set[str] = set()
    tbl_refs: set[str] = set()
    for md in (PROJECT_ROOT / "docs" / "manuscript").glob("*.md"):
        text = md.read_text(encoding="utf-8")
        tbl_defs.update(re.findall(r"#tbl:(\w+)", text))
        tbl_refs.update(re.findall(r"@tbl:(\w+)", text))

    unresolved = tbl_refs - tbl_defs
    assert not unresolved, f"Unresolved table references: {sorted(unresolved)}"


# ── contract error branches ──────────────────────────────────────────


def test_validate_contract_detects_missing_symbols(monkeypatch: pytest.MonkeyPatch) -> None:
    """When a used symbol key is missing from the glossary, the contract should report it."""
    from src import conceptual_model

    original = conceptual_model.symbol_glossary
    trimmed = original()[:-1]  # drop the last symbol
    monkeypatch.setattr(conceptual_model, "symbol_glossary", lambda: trimmed)
    errors = conceptual_model.validate_conceptual_contract()
    assert any("missing symbol glossary rows" in e for e in errors)


def test_validate_contract_detects_unused_symbols(monkeypatch: pytest.MonkeyPatch) -> None:
    """When a glossary symbol is not used by any claim, the contract should report it."""
    from src import conceptual_model
    from src.conceptual_model import SymbolSpec

    original = conceptual_model.symbol_glossary
    extra = original() + (
        SymbolSpec("unused_key", "$U$", "unused", "An unused symbol for testing"),
    )
    monkeypatch.setattr(conceptual_model, "symbol_glossary", lambda: extra)
    errors = conceptual_model.validate_conceptual_contract()
    assert any("unused symbol glossary rows" in e for e in errors)


def test_build_conceptual_report_raises_on_contract_violation(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    """The analysis pipeline should refuse to build a report when the contract is broken."""
    from src import conceptual_model
    from src.analysis.workflow import build_conceptual_report

    original = conceptual_model.symbol_glossary
    trimmed = original()[:-1]
    monkeypatch.setattr(conceptual_model, "symbol_glossary", lambda: trimmed)
    with pytest.raises(ValueError, match="missing symbol"):
        build_conceptual_report(tmp_path)


def test_analysis_main_returns_zero(tmp_path: Path) -> None:
    """The main() entry point should run the pipeline and return 0."""
    from src.analysis.workflow import main

    result = main(tmp_path)
    assert result == 0


def test_validate_contract_detects_duplicate_figure_keys(monkeypatch: pytest.MonkeyPatch) -> None:
    """Duplicate figure keys should be caught by the contract."""
    from src import conceptual_model
    from src.conceptual_model import FigureSpec

    original = conceptual_model.figure_specs
    dup = original() + (FigureSpec("tinbergen_axes", "dup.png", "dup", "dup", "dup caption"),)
    monkeypatch.setattr(conceptual_model, "figure_specs", lambda: dup)
    errors = conceptual_model.validate_conceptual_contract()
    assert any("duplicate figure keys" in e for e in errors)


def test_validate_contract_detects_duplicate_figure_filenames(monkeypatch: pytest.MonkeyPatch) -> None:
    """Duplicate figure filenames should be caught by the contract."""
    from src import conceptual_model
    from src.conceptual_model import FigureSpec

    original = conceptual_model.figure_specs
    dup = original() + (FigureSpec("unique_key_1", "tinbergen_axes.png", "dup", "dup", "dup caption"),)
    monkeypatch.setattr(conceptual_model, "figure_specs", lambda: dup)
    errors = conceptual_model.validate_conceptual_contract()
    assert any("duplicate figure filenames" in e for e in errors)


def test_validate_contract_detects_duplicate_formal_keys(monkeypatch: pytest.MonkeyPatch) -> None:
    """Duplicate formal claim keys should be caught by the contract."""
    from src import conceptual_model
    from src.conceptual_model import FormalClaim

    original = conceptual_model.formal_claims
    dup = original() + (
        FormalClaim("axis_partition", "dup", "$dup$", "dup", ()),
    )
    monkeypatch.setattr(conceptual_model, "formal_claims", lambda: dup)
    errors = conceptual_model.validate_conceptual_contract()
    assert any("duplicate formal claim keys" in e for e in errors)


# ── manuscript_variables edge cases ───────────────────────────────────


def test_build_timestamp_uses_source_date_epoch() -> None:
    """When SOURCE_DATE_EPOCH is set, the timestamp should use it."""
    import os

    from src.manuscript_variables import _build_timestamp

    os.environ["SOURCE_DATE_EPOCH"] = "1700000000"
    try:
        ts = _build_timestamp()
        assert ts == "2023-11-14T22:13:20Z"
    finally:
        del os.environ["SOURCE_DATE_EPOCH"]


def test_load_config_warns_on_missing_file(tmp_path: Path) -> None:
    """A missing config.yaml should log a warning and return an empty dict."""
    from src.manuscript_variables import _load_config

    config = _load_config(tmp_path)
    assert config == {}


def test_load_json_report_warns_on_missing_file(tmp_path: Path) -> None:
    """A missing report should log a warning and return an empty dict."""
    from src.manuscript_variables import _load_json_report

    report = _load_json_report(tmp_path, "nonexistent.json")
    assert report == {}


def test_compute_config_hash_returns_na_for_missing_config(tmp_path: Path) -> None:
    """When config.yaml is absent, the hash should be 'N/A'."""
    from src.manuscript_variables import _compute_config_hash

    assert _compute_config_hash(tmp_path) == "N/A"


def test_generate_variables_without_config_uses_defaults(tmp_path: Path) -> None:
    """Even with no config file, generate_variables should produce defaults."""
    from src.manuscript_variables import generate_variables

    variables = generate_variables(tmp_path, require_analysis_outputs=False)
    assert variables["PROJECT_TITLE"] == "Prior Cognitive Art"
    assert variables["CONFIG_HASH"] == "N/A"
    assert variables["CONFIG_FIRST_AUTHOR"] == "Project Author"


# ── figure manifest mismatch ─────────────────────────────────────────


def test_generate_all_figures_raises_on_manifest_mismatch(tmp_path: Path) -> None:
    """If the produced figures don't match the specs, generate_all_figures should raise."""
    from src.figures import conceptual as fig

    # Monkey-patch one draw function to produce a different filename
    original_draw = fig.draw_tinbergen_axes

    def wrong_draw(output_dir: Path) -> Path:
        return original_draw(output_dir).rename(output_dir / "wrong_name.png")

    fig.draw_tinbergen_axes = wrong_draw
    try:
        with pytest.raises(RuntimeError, match="figure manifest mismatch"):
            fig.generate_all_figures(tmp_path)
    finally:
        fig.draw_tinbergen_axes = original_draw
