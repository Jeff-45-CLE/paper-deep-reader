# Contributing

## Scope

Contributions should improve one of these areas:

- source fidelity;
- method reconstruction;
- terminology and notation handling;
- experiment extraction;
- paper-type adaptation;
- Feishu formatting;
- language quality;
- evaluation coverage.

## Development setup

The validator uses the Python standard library.

Run tests:

```bash
python -m unittest discover -s tests
```

Validate the example note:

```bash
python scripts/validate_note.py examples/toy-paper/note.zh-CN.md
```

## Adding a language rule

1. Add the pattern to `config/style_rules.json`.
2. State whether it is an error or warning.
3. Add a concise revision message.
4. Add a failing fixture or unit test.
5. Check that the pattern does not flag equations, code blocks, or tables.

Avoid broad patterns that suppress legitimate technical language.

## Adding a template

A new deep template must preserve:

- source boundary;
- research logic;
- terms and symbols;
- closed-loop method flow;
- equations;
- worked example;
- experiments;
- claim-evidence map;
- contributions and limitations;
- unresolved points.

## Adding an example

Examples must be licensed for redistribution or explicitly synthetic. Include:

- source material;
- generated note;
- evidence anchors;
- a statement that identifies synthetic values when applicable.

## Pull requests

A pull request should include:

- purpose;
- changed files;
- expected behavior;
- test result;
- compatibility impact.

Keep changes focused. Update `CHANGELOG.md` for user-facing changes.
