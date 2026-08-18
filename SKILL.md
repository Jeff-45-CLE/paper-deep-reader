---
name: paper-deep-reader
description: Deeply read academic papers and produce source-grounded, Feishu-ready learning notes. Reconstructs the research problem, terminology, notation, method pipeline, key equations, worked example, experimental design, claim-evidence links, contributions, limitations, and research context. Use for uploaded PDFs, paper URLs, preprints, journal articles, conference papers, technical reports, and requests to learn or summarize a paper.
---

# Paper Deep Reader

## 1. Purpose

This skill turns an academic paper into a structured learning note that a researcher can study, revisit, and paste into Feishu.

The default goal is deep understanding. The output must answer three questions:

1. What scenario and problem does the paper study, and what method does it propose?
2. How are the experiments configured, and what effects are reported?
3. How does the complete algorithm work from input to output, with the original terminology and notation preserved, plain-language explanations, and one faithful worked example?

The skill also records evidence anchors, separates author claims from analysis, identifies limitations, and positions the paper within its research context.

## 2. When to Use

Load this skill when the user:

- uploads or links an academic paper;
- asks to read, explain, summarize, study, analyze, or review a paper;
- asks for a Feishu-ready paper note;
- wants the method, equations, experiments, terms, or symbols explained;
- wants a paper converted into reusable research notes;
- wants a structured input for a literature review.

Do not use this skill for a pure venue-style peer review unless the user explicitly requests review scores or an accept/reject recommendation.

## 3. Inputs

Supported inputs include:

- uploaded PDF;
- arXiv, DOI, conference, journal, or project-page URL;
- paper text or selected sections;
- supplementary material, appendix, code repository, or author-provided notes.

Record the available source boundary before analysis. If only part of the paper is available, state which parts were read and which parts remain unavailable.

## 4. Default Output Language

- Follow the language used by the user.
- Preserve original technical terms, method names, dataset names, symbols, and abbreviations.
- At first occurrence, give the original term and a concise explanation in the output language.
- Keep standard mathematical notation unchanged unless the paper contains an explicit correction.
- Never silently rename symbols for convenience.

## 5. Core Principles

### 5.1 Source Fidelity

Every substantive statement must be supported by the paper or clearly labeled as explanation, interpretation, or external context.

Use these labels when the distinction matters:

- **Paper stated**: directly stated or shown by the paper.
- **Plain-language explanation**: explanation added to improve understanding.
- **Research interpretation**: reasoned interpretation that goes beyond explicit wording.
- **External context**: information obtained outside the paper.
- **Unclear from source**: information that cannot be verified from the available material.

Never fabricate missing hyperparameters, numerical results, data splits, implementation details, or limitations.

### 5.2 Closed-Loop Method Reconstruction

A method explanation is complete only when every stage has:

- input;
- operation;
- output;
- purpose;
- next consumer.

For iterative methods, also identify:

- initialization;
- update rule;
- stopping condition;
- final output.

For training-based methods, separate the training pipeline from the inference pipeline.

For agent systems, identify observation, state, memory, planning, action, tool or environment interaction, feedback, and termination when applicable.

For optimization methods, identify decision variables, objective, constraints, solver or update procedure, and convergence or termination conditions.

### 5.3 Terminology and Notation Preservation

Build a terminology and notation map before explaining the method.

For each key term, provide:

- original term;
- formal definition;
- role in this paper;
- plain-language explanation;
- relation to adjacent concepts;
- source anchor.

For each key symbol, provide:

- symbol exactly as written;
- meaning;
- type, shape, or dimension when stated;
- first-use location;
- role in the pipeline.

Flag overloaded or inconsistent notation.

### 5.4 Evidence Anchors

Anchor key points to the closest available source location:

- section;
- page;
- equation;
- algorithm;
- figure;
- table;
- appendix.

Use compact forms such as `(Sec. 3.2, Eq. 4)` or `(Table 2, p. 7)`.

Do not infer precise values from a plot unless the estimate is clearly labeled as approximate.

### 5.5 Claim-Evidence Alignment

For every major claim, record:

- exact claim;
- supporting experiment, theorem, or analysis;
- reported result;
- strength of support: strong, partial, weak, or unverified;
- source anchor.

Treat author claims as claims until the evidence has been checked.

### 5.6 Feishu-Ready Formatting

Use Markdown that remains readable after copy and paste:

- short headings with clear hierarchy;
- compact paragraphs;
- bullets for parallel facts;
- tables only for metadata, notation, experiment matrices, and claim-evidence maps;
- fenced text blocks for long pipelines or pseudocode;
- display equations only when they are central to the method;
- no decorative sections that repeat earlier content.

The section “What to Remember” is excluded from the default output.

## 6. Reading Workflow

### Phase 0: Establish Scope

1. Identify the paper title, authors, venue or status, year, DOI or arXiv identifier, field, and paper type.
2. Record available sources and missing material.
3. Determine the requested depth: quick read, deep read, or literature-matrix extraction.
4. Determine the requested output language.
5. Note whether external literature search is allowed or required.

### Phase 1: Complete Paper Pass

Read the following in order:

1. Abstract and introduction.
2. Related work and problem formulation.
3. Method, algorithms, figures, and equations.
4. Experiments, tables, plots, ablations, and case studies.
5. Discussion, limitations, conclusion.
6. Appendix and supplementary material when available.

Inspect captions and algorithm boxes. Important implementation details often appear outside the main prose.

### Phase 2: Reconstruct the Research Logic

Extract the chain:

```text
Research scenario
    ↓
Concrete task
    ↓
Limitation of existing approaches
    ↓
Observed gap or motivation
    ↓
Proposed idea
    ↓
Method
    ↓
Claimed outcome
```

Verify that each transition is supported by the paper.

### Phase 3: Build the Concept and Symbol Map

1. List terms required to understand the paper.
2. Separate standard field terms from paper-specific terms.
3. Record symbols, dimensions, and dependencies.
4. Resolve aliases and overloaded symbols.
5. Explain each item using formal and plain-language descriptions.

### Phase 4: Reconstruct the Method

Start with a one-screen overview:

```text
Input
  ↓
Preprocessing or initialization
  ↓
Core module or iterative procedure
  ↓
Intermediate representation
  ↓
Decision, prediction, generation, or control
  ↓
Output
```

Then explain each stage with Input → Operation → Output → Purpose → Next Step.

Include data shapes, state transitions, optimization variables, losses, and update rules when stated.

### Phase 5: Explain Key Equations

Select equations that define:

- the problem;
- the model;
- the objective or loss;
- the update rule;
- the inference rule;
- the evaluation metric when it is paper-specific.

For each selected equation:

1. reproduce the equation accurately;
2. define every symbol;
3. explain what it computes;
4. explain why the design is needed;
5. state where it appears in the pipeline;
6. give a plain-language intuition;
7. state assumptions or constraints.

Skip equations that do not affect understanding.

### Phase 6: Construct a Worked Example

Create one small example that follows the paper’s actual procedure.

Rules:

- use the paper’s original terms and symbols;
- keep values simple;
- mark invented values as a constructed example;
- do not present invented values as experimental evidence;
- show intermediate states;
- carry the example to the final output;
- explain what each intermediate result means.

### Phase 7: Reconstruct the Experiments

Identify the research questions behind the experiments.

Extract:

- datasets or environments;
- task definition;
- train, validation, test, transductive, or online protocol;
- baselines and comparison fairness;
- protocol validity, information access, and possible leakage;
- metrics;
- backbone and model configuration;
- training and inference settings;
- information-access boundary, data leakage risk, and future-data access;
- hyperparameters;
- random seeds and repeated runs;
- compute and runtime when reported;
- main results;
- ablations;
- sensitivity studies;
- visualizations;
- case studies;
- error analysis;
- statistical tests or uncertainty estimates;
- for agent papers: model version, prompt or system instruction, tool set, maximum steps, retry policy, evaluator, temperature, token cost, and API settings when reported.

For each experiment, explain:

```text
Question → Setup → Comparison → Result → Supported claim
```

### Phase 8: Audit Contributions and Boundaries

Separate:

- authors’ claimed contributions;
- concrete technical contributions visible in the method;
- empirical contributions;
- engineering contributions;
- theoretical contributions;
- limitations stated by the authors;
- limitations inferred from assumptions, experiments, or scope;
- likely failure cases;
- reproducibility gaps.

### Phase 9: Position the Paper

When supported by the source or external search:

- identify the direct predecessor methods;
- state the technical difference;
- identify what the paper retains, modifies, or removes;
- state the paper’s likely role in the research line;
- record transferable ideas for future research.

Clearly label external context.

### Phase 10: Generate the Note

Use `templates/feishu-deep-note.zh-CN.md` or `templates/feishu-deep-note.en.md`.

Omit optional subsections only when the paper type makes them irrelevant. Never omit the research logic, terminology, method flow, experiments, claim-evidence map, or limitations for empirical papers.

### Phase 11: Quality Gate

Before finalizing, verify:

- the full available paper was read;
- the paper type was identified;
- the research scenario, problem, motivation, method, and result form a complete chain;
- key terms and symbols are preserved;
- training and inference are separated where applicable;
- every algorithm stage has input, operation, output, purpose, and next step;
- important equations are explained in context;
- the worked example reaches a final output;
- experiments are mapped to research questions;
- numerical claims match the paper;
- author claims and analysis are separated;
- limitations are source-grounded or labeled as interpretation;
- evidence anchors are present;
- missing information is disclosed;
- the output passes the language-style rules.

## 7. Paper-Type Adaptation

### 7.1 Empirical Paper

Prioritize:

- protocol;
- baselines;
- metrics;
- main results;
- ablations;
- statistical reliability;
- generalization;
- compute and reproducibility.

### 7.2 Theoretical Paper

Prioritize:

- assumptions;
- definitions;
- theorem statements;
- proof skeleton;
- logical dependencies;
- bound tightness;
- relation between theory and practical use.

A worked example may use a small synthetic case that demonstrates the theorem or algorithm.

### 7.3 Systems Paper

Prioritize:

- architecture;
- components and interfaces;
- data flow;
- deployment assumptions;
- latency, throughput, memory, and scalability;
- failure recovery;
- real-world evaluation.

### 7.4 Survey Paper

Prioritize:

- scope and inclusion criteria;
- taxonomy;
- coverage;
- comparison dimensions;
- consensus and disagreements;
- open problems;
- missing research lines.

Do not force a single algorithm walkthrough when no single algorithm exists.

### 7.5 Position or Perspective Paper

Prioritize:

- central thesis;
- argument chain;
- evidence quality;
- assumptions;
- counterarguments;
- implications.

## 8. Output Structure

The default deep note uses this structure:

1. Paper information and source boundary.
2. One-sentence closed-loop summary.
3. Research scenario, problem, motivation, and proposed method.
4. Key concepts, terminology, and notation.
5. Complete method and algorithm flow.
6. Key equations.
7. Worked example.
8. Experimental questions, setup, results, and ablations.
9. Claim-evidence map.
10. Contributions, strengths, limitations, and failure cases.
11. Research context and transferable insights.
12. Ambiguities and unresolved points.

Use the detailed template in `templates/`.

## 9. Language and Style Rules

### 9.1 Required Style

- Use direct, concise sentences.
- Keep one main function per paragraph.
- Prefer concrete nouns, verbs, numbers, and source anchors.
- Explain jargon immediately.
- Preserve technical precision without stacking unnecessary jargon.
- Use active voice when possible.
- Keep sentence structure simple.
- Avoid repeated summaries across sections.
- Replace vague praise with measurable evidence.
- Report exact values, confidence intervals, or table references when available.
- State uncertainty directly.

### 9.2 Prohibited Chinese Templates

Do not generate these patterns in normal prose:

- “不是……而是……”
- “不仅……而且……”
- “值得注意的是”
- “需要指出的是”
- “综上所述”
- “总的来说”
- “随着……的不断发展”
- “在当今……背景下”
- “为……提供了新的思路/视角”
- “具有重要意义”
- “展现出巨大的潜力”
- “显而易见”
- “不难发现”
- “毋庸置疑”
- “毫无疑问”
- “从本质上讲”
- “归根结底”
- “这无疑……”

### 9.3 Prohibited English Templates

Do not generate these patterns in normal prose:

- “not X, but Y”
- “It is worth noting that”
- “It should be noted that”
- “In today’s rapidly evolving…”
- “In conclusion”
- “Overall, it is clear that”
- “provides a novel perspective”
- “opens up new avenues”
- unsupported uses of “clearly,” “obviously,” or “significant”

### 9.4 Evidence-Sensitive Words

Words such as “significant,” “substantial,” “effective,” “robust,” “generalizable,” “efficient,” and “state of the art” require direct evidence.

When no statistical test is reported, use “the reported mean is higher by X” instead of “significantly better.”

### 9.5 Structural Patterns to Avoid

- rigid “first, second, third, finally” sequences when the content is not procedural;
- repeated “this means” or “in other words” transitions;
- generic opening paragraphs;
- generic conclusion paragraphs;
- stacked adjectives;
- long sentences with several nested clauses;
- headings with only one vague sentence;
- duplicated content under summary, contributions, results, and conclusion.

## 10. Failure Handling

When the paper is incomplete, unreadable, or ambiguous:

- state the exact limitation;
- analyze only the available content;
- do not fill gaps from general knowledge;
- request or search for additional material only when the user permits it;
- distinguish verified facts from likely interpretations.

When a proof, figure, or result cannot be verified, say so directly.

## 11. Optional Modes

### Quick Read

Use `templates/quick-read.zh-CN.md` for paper triage. Keep the research logic, method sketch, experiment headline, and limitations.

### Literature Matrix

Use `templates/literature-matrix.zh-CN.md` after multiple papers have been processed. Keep extraction criteria consistent across papers.

### Venue Review

If the user explicitly requests peer review, add a separate review section with soundness, novelty, reproducibility, experimental design, and recommendation. Do not mix venue scoring into the default learning note.

## 12. Output Files

When file output is available:

- save the note as Markdown;
- use a descriptive filename such as `notes/{short-paper-title}.md`;
- preserve UTF-8 encoding;
- run `scripts/validate_note.py` before delivery when the repository tools are available.
