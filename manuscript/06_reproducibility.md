# Reproducibility: Source-Owned Figures, Tokens, and Validation Gates {#sec:reproducibility}

The reproducibility claim is modest: the prose tokens and figures are generated
from explicit project files, and the project states its deterministic-trace
boundary. The formal supplement in [@sec:formal-supplement] provides the
integrity checks that make drift detectable before render.

- Config hash: `{{CONFIG_HASH}}`
- Version: `{{CONFIG_VERSION}}`
- First author: {{CONFIG_FIRST_AUTHOR}}
- Keywords: {{CONFIG_KEYWORDS}}
- Figure artifacts counted: {{ARTIFACT_FIGURES}}
- Data artifacts counted: {{ARTIFACT_DATA_FILES}}
- Report artifacts counted: {{ARTIFACT_REPORTS}}
- Conceptual integrity token: `{{CONCEPTUAL_INTEGRITY_TOKEN}}`
- Formal claims generated: {{FORMAL_CLAIM_COUNT}}
- Symbol glossary rows generated: {{SYMBOL_COUNT}}
- Text-validation checks generated: {{TEXT_VALIDATION_COUNT}}

Regenerate the working artifacts with:

```bash
uv run python projects/working/prior_cognitive_art/scripts/optimization_analysis.py
uv run python projects/working/prior_cognitive_art/scripts/z_generate_manuscript_variables.py
```
