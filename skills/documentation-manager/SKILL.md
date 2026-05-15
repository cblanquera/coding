---
name: documentation-manager
description: Coordinate documentation work across developer-documentation, api-documentation, technical-docs-editor, and documentation-formatting. Use when Codex needs to assess a documentation task, choose the right documentation skill or combination, sequence them correctly, and produce clear, technically accurate docs without the user having to specify each role manually.
---

# Documentation Manager

This skill routes documentation work to the right specialist skill or sequence
of skills.

Use it as the default entry point for documentation tasks when the user has not
already chosen a more specific documentation skill. Its job is to classify the
task, choose the minimum necessary skill set, apply those skills in the right
order, and produce one coherent result.

Do not replace the specialist skills. Coordinate them.

## Managed Skills

This skill is responsible for selecting and sequencing:

- `developer-documentation`
- `api-documentation`
- `technical-docs-editor`
- `documentation-formatting`

## Core Rule

Always choose the narrowest skill set that solves the task.

Do not pile on every documentation skill by default. Extra skills increase
instruction conflict and make output less predictable.

## Task Intake

Before choosing a path, identify:

1. the document type: README, guide, quick start, tutorial, explanation, reference, API page, mixed page, or legacy doc
2. the primary reader goal: evaluate, get started, understand, integrate, debug, or look up
3. the dominant problem: poor flow, weak reference structure, rough prose, formatting drift, or mixed concerns
4. whether the output should be a rewrite, restructure, review, or cleanup pass
5. whether the page should remain single-file or split into guide and reference content

## Routing Rules

### Use `developer-documentation` first when:

- the task is mainly onboarding or teaching
- the page needs a better quick start or learning sequence
- the page is a guide, tutorial, README, or conceptual overview
- the reader needs first-success flow more than lookup density

Then optionally apply:

- `technical-docs-editor` to improve junior-developer clarity
- `documentation-formatting` last for cleanup

### Use `api-documentation` first when:

- the page is mainly reference material
- the reader needs methods, properties, configuration, events, or examples for lookup
- the main issue is schema, organization, or reference completeness

Then optionally apply:

- `technical-docs-editor` to improve clarity without changing meaning
- `documentation-formatting` last for cleanup

### Use `technical-docs-editor` first when:

- the structure is mostly correct
- the main problem is wording, clarity, assumptions, or junior-developer readability
- the task is a line edit, polish pass, or accuracy-sensitive simplification

Then optionally apply:

- `documentation-formatting` last when presentation is inconsistent

### Use `documentation-formatting` alone when:

- the content and structure are already correct
- the task is primarily markdown normalization, heading cleanup, code fence cleanup, or link hygiene

## Mixed-Page Rule

If a page mixes onboarding, conceptual explanation, and reference material in a
way that harms readability:

1. separate the content by function
2. use `developer-documentation` for the guide path
3. use `api-documentation` for the lookup path
4. use `technical-docs-editor` to simplify and tighten both
5. use `documentation-formatting` last

Do not leave a page mixed and overloaded just because the original draft was
mixed.

## Sequencing Rules

Apply skills in this order unless there is a strong reason not to:

1. choose the content owner:
   - `developer-documentation` for onboarding and conceptual flow
   - `api-documentation` for reference structure
   - `technical-docs-editor` for editorial-only passes
2. use `technical-docs-editor` after the content owner when clarity is still the issue
3. use `documentation-formatting` last

Never run `documentation-formatting` first when structural or editorial issues
still exist.

## Conflict Rules

- Do not let `documentation-formatting` override teaching flow.
- Do not force onboarding structure onto pure API reference pages.
- Do not let `technical-docs-editor` rewrite semantics for the sake of smooth prose.
- Do not use both `developer-documentation` and `api-documentation` on the same section unless the section is being split or one is clearly subordinate.

## Default Paths

Use these defaults when the task is ambiguous:

- README for an open source library: `developer-documentation` -> `technical-docs-editor` -> `documentation-formatting`
- API class/module reference: `api-documentation` -> `technical-docs-editor` -> `documentation-formatting`
- rough but structurally sound technical explainer: `technical-docs-editor` -> `documentation-formatting`
- messy all-in-one legacy doc: split first, then route guide content to `developer-documentation` and reference content to `api-documentation`, followed by `technical-docs-editor` and `documentation-formatting`

## Output Expectations

When using this skill:

- state the chosen documentation path briefly
- apply the minimum necessary skill sequence
- return one coherent output, not disconnected passes
- mention any proposed split between guide and reference content
- flag technical uncertainties rather than guessing

## Review Gate

Do not consider the task complete unless the answer to all of these is yes:

- Did the correct specialist skill own the document type?
- Was the minimum necessary skill set used?
- Did the sequencing avoid instruction conflicts?
- Is the output clearer and more technically reliable than a manual multi-tag pass?
- If the page was mixed, was that handled intentionally instead of ignored?
