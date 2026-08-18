# Language Style Guide

## Goal

Produce technical notes that read like careful research notes. The language should be direct, specific, and easy to revisit.

## Required writing style

- Use short, complete sentences.
- Keep one main function per paragraph.
- Introduce a term before using it repeatedly.
- Preserve original terminology and notation.
- Prefer concrete verbs and measurable facts.
- Place evidence anchors near claims.
- State uncertainty directly.
- Use paragraphs for reasoning and tables for structured facts.
- Separate paper statements, explanations, interpretations, and external context.
- Remove repeated content across summary, contributions, results, and closing sections.

## Hard-prohibited Chinese templates

The checker reports these as errors in generated notes:

- `不是……而是……`
- `不仅……而且……`
- `值得注意的是`
- `需要指出的是`
- `综上所述`
- `总的来说`
- `随着……的不断发展`
- `在当今……背景下`
- `为……提供了新的思路`
- `为……提供了新的视角`
- `具有重要意义`
- `展现出巨大的潜力`
- `显而易见`
- `不难发现`
- `毋庸置疑`
- `毫无疑问`
- `从本质上讲`
- `归根结底`
- `这无疑……`

## Hard-prohibited English templates

- `not X, but Y`
- `It is worth noting that`
- `It should be noted that`
- `In today's rapidly evolving...`
- `In conclusion`
- `Overall, it is clear that`
- `provides a novel perspective`
- `opens up new avenues`
- unsupported `clearly`, `obviously`, or `significant`

## Evidence-sensitive wording

The following words require evidence:

- significant;
- substantial;
- robust;
- effective;
- generalizable;
- efficient;
- state of the art;
- large improvement;
- strong performance.

Preferred form:

```text
Table 2 reports 74.3%, which is 3.1 percentage points above Baseline A.
```

Avoid:

```text
The method achieves a significant improvement.
```

When no statistical test is reported, describe the numerical difference without statistical language.

## Discouraged repetitive transitions

The checker reports repeated use as warnings:

- `可以看出`
- `这意味着`
- `换句话说`
- `一方面……另一方面……`
- `首先、其次、最后`
- `In other words`
- `This means that`
- `Overall`

A single necessary use may be acceptable. Repeated use usually signals mechanical prose.

## Sentence length

Recommended limits:

- Chinese sentence: 90 characters.
- English sentence: 35 words.
- Paragraph: 450 characters or 140 English words.

Longer units are warnings. Equations, code blocks, and tables are excluded where possible.

## Revision patterns

### Replace generic emphasis with evidence

Before:

```text
值得注意的是，该模块带来了显著提升。
```

After:

```text
Removing the module lowers accuracy from 78.4% to 74.9% in Table 4.
```

### Split a contrast template into direct facts

Before:

```text
该方法不是依赖标签，而是从查询批次估计先验。
```

After:

```text
The method uses no support labels. It estimates the class prior from the query batch.
```

### Remove generic conclusions

Before:

```text
综上所述，该方法具有重要意义，并展现出巨大的潜力。
```

After:

```text
The evidence supports the reported gain on the three evaluated datasets. Cross-domain performance remains untested.
```

## Technical terminology

- Keep the original English term at first occurrence.
- Add a concise Chinese explanation when the output is Chinese.
- Do not translate method names, dataset names, model names, or standard abbreviations.
- Do not replace a symbol with a new symbol for convenience.
- Explain symbol shape or dimension when the paper provides it.

## Tone

- Analytical.
- Neutral.
- Specific.
- Free of promotional language.
- Clear about evidence boundaries.
