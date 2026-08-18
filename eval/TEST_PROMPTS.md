# Test Prompts

Use these prompts to evaluate the skill across paper types.

## Empirical machine learning paper

```text
Read the uploaded paper with paper-deep-reader. Produce a Chinese Feishu-ready deep note.
Preserve the original terms and symbols. Reconstruct the training and inference pipelines,
explain the central loss functions, and map every main claim to an experiment.
```

Expected checks:

- protocol and split;
- baselines;
- metrics;
- main results;
- ablations;
- seeds and uncertainty;
- worked example.

## Agent paper

```text
Explain the full agent loop. Identify observation, state, memory, planning, action, tool
feedback, reflection, and termination. Use one example trajectory.
```

Expected checks:

- state transitions;
- tool interaction;
- memory update;
- stopping condition;
- example trajectory.

## Optimization paper

```text
Identify decision variables, objective, constraints, solver, update rule, and termination.
Use a small numerical example that reaches a feasible solution.
```

Expected checks:

- optimization formulation;
- feasibility;
- update;
- convergence or stopping;
- example closure.

## Theoretical paper

```text
Extract definitions, assumptions, theorem dependencies, and the proof skeleton. Explain
one small example that demonstrates the theorem. Mark any proof step that cannot be verified.
```

Expected checks:

- assumptions;
- theorem graph;
- proof boundaries;
- small example;
- uncertainty disclosure.

## Systems paper

```text
Reconstruct the system architecture, component interfaces, data flow, deployment setting,
latency, throughput, memory, scalability, and failure handling.
```

Expected checks:

- interfaces;
- runtime path;
- evaluation environment;
- system metrics;
- deployment assumptions.

## Survey paper

```text
Extract the survey scope, inclusion criteria, taxonomy, comparison dimensions, consensus,
disagreements, missing research lines, and open problems.
```

Expected checks:

- taxonomy;
- coverage;
- source selection;
- open gaps;
- no forced single-algorithm flow.

## Adversarial source-boundary test

```text
The uploaded file contains only the abstract and introduction. Produce the note using only
the available content. Mark every missing method or experimental detail as unavailable.
```

Expected checks:

- no fabricated results;
- explicit missing sections;
- restrained method claims.

## Language-style test

```text
Generate the Chinese note and run the repository validator. Revise until all hard-prohibited
template patterns are removed and evidence-sensitive claims are supported.
```
