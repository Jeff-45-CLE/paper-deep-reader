# Output Specification

## Required sections for a deep note

1. Paper information and source boundary.
2. One-sentence closed-loop summary.
3. Research scenario, problem, motivation, and proposed method.
4. Key concepts, terminology, and notation.
5. Method overview and step-by-step algorithm.
6. Key equations.
7. Worked example.
8. Experimental questions, setup, results, and ablations.
9. Claim-evidence map.
10. Contributions, strengths, limitations, and failure cases.
11. Research context and transferable insights.
12. Ambiguities and unresolved points.

## Source-status labels

Use labels when a statement could be mistaken for a paper claim:

- **Paper stated**
- **Plain-language explanation**
- **Research interpretation**
- **External context**
- **Unclear from source**

A label may apply to a paragraph, bullet, or table row. Avoid labeling every sentence when the source status is already clear.

## Evidence anchors

Preferred forms:

- `(Sec. 2.1)`
- `(Sec. 3.2, Eq. 4)`
- `(Algorithm 1, lines 5–9)`
- `(Fig. 2, p. 5)`
- `(Table 3)`
- `(Appendix B.2)`

Place the anchor next to the supported content.

## Method-step contract

Every method step must answer:

| Field | Requirement |
|---|---|
| Input | What enters the step |
| Operation | What transformation or decision occurs |
| Output | What leaves the step |
| Purpose | Why the step exists |
| Next step | Where the output is consumed |

## Equation contract

Each selected equation must include:

- original equation;
- symbol definitions;
- shape or type when stated;
- computational meaning;
- design reason;
- pipeline position;
- intuitive explanation;
- assumptions and constraints.

## Worked-example contract

The example must:

- be explicitly labeled as constructed;
- use simple values;
- follow the paper’s real order;
- show intermediate outputs;
- reach a final result;
- avoid claiming that constructed values are reported results.

## Experiment contract

For every major experiment, record:

- research question;
- dataset or environment;
- task and protocol;
- baseline;
- information-access boundary and leakage risk;
- fairness and confounders;
- metric;
- setting;
- result;
- interpretation;
- supported claim;
- source anchor.

## Conditional sections by paper type

### Empirical

Require protocol, baselines, metrics, main results, ablations, and reliability.

### Theoretical

Replace experimental detail with assumptions, theorem dependencies, proof skeleton, and a small example when appropriate.

### Systems

Require architecture, interfaces, deployment setting, latency, throughput, memory, scalability, and failure handling when reported.

### Survey

Require scope, inclusion criteria, taxonomy, comparison dimensions, coverage gaps, and open questions. A single algorithm walkthrough is optional.

### Position

Require thesis, argument chain, evidence, assumptions, counterarguments, and implications.

## Formatting constraints

- Keep heading depth at four levels or fewer.
- Use tables only for structured comparisons.
- Keep prose paragraphs compact.
- Avoid redundant summary sections.
- Do not include a “What to Remember” section.
- Preserve original symbols and method names.
