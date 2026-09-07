# Artifact Protocol: Deterministic Generation Without Empirical Simulation {#sec:artifact-protocol}

The project deliberately preserves the template's reproducible artifact surface
while changing the research mode described in [@sec:method]. The reproducibility
claims are detailed in [@sec:reproducibility].

- Project mode: {{PRIMARY_MODE}}
- Simulation policy: {{SIMULATION_POLICY}}
- Conceptual report status: {{CONCEPTUAL_REPORT_STATUS}}
- Formal claims generated: {{FORMAL_CLAIM_COUNT}}
- Symbol glossary rows generated: {{SYMBOL_COUNT}}
- Text-validation checks generated: {{TEXT_VALIDATION_COUNT}}
- Python version: {{PYTHON_VERSION}}
- Platform: {{PLATFORM}}
- Generation timestamp: {{GENERATION_TIMESTAMP}}

The retained analysis-stage script name is compatibility glue for the template
runner. It generates conceptual figures and JSON reports; it does not perform
optimization, empirical metric collection, stochastic sampling, synthetic-data
generation, or cognitive simulation. The deterministic trace artifacts record
only the authored formal-state sequence described in [@sec:visual-atlas].
