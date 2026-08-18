# Final Quality Checklist

## Source boundary

- [ ] The paper version and available materials are recorded.
- [ ] Missing or unreadable sections are disclosed.
- [ ] External context is labeled.

## Research logic

- [ ] The research scenario is concrete.
- [ ] The task has explicit input and output.
- [ ] The limitation of existing work is specific.
- [ ] The motivation leads to the proposed design.
- [ ] The proposed method and reported result close the chain.

## Terminology and notation

- [ ] Original terms and abbreviations are preserved.
- [ ] Key terms have formal and plain-language explanations.
- [ ] Key symbols have meaning, type or shape, and pipeline role.
- [ ] Overloaded or inconsistent symbols are flagged.

## Method

- [ ] The overall pipeline fits on one screen.
- [ ] Training and inference are separated where applicable.
- [ ] Every step has input, operation, output, purpose, and next consumer.
- [ ] Initialization, update, stopping, and final output are covered.
- [ ] Data shapes or state transitions are included when stated.
- [ ] Key modules are connected to the main pipeline.

## Equations and example

- [ ] Selected equations are central to the method.
- [ ] Every symbol in each selected equation is defined.
- [ ] Each equation has a pipeline position and intuition.
- [ ] The worked example is labeled as constructed.
- [ ] Intermediate results are shown.
- [ ] The example reaches a final output.

## Experiments

- [ ] Research questions are identified.
- [ ] Dataset, task, protocol, baselines, and metrics are recorded.
- [ ] Information access, future-data use, and leakage risks are checked.
- [ ] Baseline fairness and confounders are recorded.
- [ ] Training and inference settings are separated.
- [ ] Main numerical results match the paper.
- [ ] Ablations are mapped to design choices.
- [ ] Seeds, repeated runs, uncertainty, and compute are recorded when available.
- [ ] Reproducibility gaps are listed.

## Claims and boundaries

- [ ] Every major claim has evidence and an anchor.
- [ ] Support strength is assessed.
- [ ] Author-claimed and concrete contributions are separated.
- [ ] Author-stated and inferred limitations are separated.
- [ ] Failure cases and generalization boundaries are recorded.

## Language

- [ ] No prohibited Chinese or English templates appear in normal prose.
- [ ] Performance adjectives have numerical or statistical evidence.
- [ ] Sentences and paragraphs remain compact.
- [ ] Summary, contribution, result, and closing sections do not repeat each other.
- [ ] No “What to Remember” section appears.
- [ ] The automatic checker passes.
