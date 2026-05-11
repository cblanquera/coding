---
name: api-documentation
description: Use this skill when writing or restructuring API reference documentation for classes, modules, methods, configuration, and type-safe examples. It organizes reference docs for lookup, accuracy, and integration rather than onboarding flow.
---

# API Documentation

This skill defines how to write API reference documentation for developers who
already know what they are looking for and need accurate, scannable details.

Optimize for lookup, correctness, and integration guidance. Do not turn API
reference pages into onboarding tutorials.

## Task Intake

Before writing or restructuring anything, identify:

1. the documented surface: class, module, CLI, config, schema, or mixed API
2. the intended reader: caller, integrator, maintainer, or migration reader
3. the missing information: signatures, behavior, defaults, errors, or examples
4. the expected deliverable: single page, multi-file reference set, or index +
   detail pages

If the task is mostly onboarding, move to `developer-documentation`. If the
task is mostly cleanup and consistency, bring in `documentation-formatting`
after the reference structure is decided.

## Scope

Use this skill for:

- class and module reference docs
- method and property documentation
- configuration and schema reference pages
- API folder organization
- type-safe examples and integration examples

Do not use this skill as the primary rule set for product onboarding, quick
starts, or broad markdown normalization.

For those cases, use:

- `developer-documentation`
- `documentation-formatting`

## File organization

When a project has multiple API reference files:

- place them in an `api/` directory
- use an `api/README.md` or equivalent index page
- prefer one file per major class, module, or component
- use descriptive filenames that match the documented subject

## Default page structure

Unless the codebase has a stronger local pattern, organize API reference pages
in this order:

1. Title and short description
2. Minimal instantiation or import example
3. Table of contents when the page is long enough to need one
4. Properties or configuration
5. Methods or operations
6. Static methods or utility exports when relevant
7. Integration examples
8. Related links

## Method standard

For each public method or operation:

- describe what it does and when to use it
- show a realistic usage example
- document parameters in a table when parameters exist
- document the return value in prose under `**Returns**`
- mention promises, chaining, defaults, and optional parameters when relevant

Do not document protected or private members unless the user explicitly asks.

## Example standard

- Use complete, runnable, or nearly runnable examples.
- Include imports when they help orient the reader.
- Prefer realistic names and values.
- Show TypeScript types when the API is typed.
- Add short comments only for non-obvious behavior.
- Progress from basic usage to integration examples when multiple examples are
  needed.

## Cross-reference rules

- Link related classes, modules, guides, and examples.
- Explain how components fit together.
- Keep reference pages lookup-friendly and independently scannable.

## Deliverables

When the task touches more than one API surface, prefer a small reference set
over one overloaded page.

Typical outputs are:

- one lookup-friendly page per major API surface
- an index page when several reference files now exist
- realistic examples for the public behaviors that readers are most likely to
  copy first
- cross-links to related guides, tasks, or adjacent APIs

## Priority

When this skill is used with other documentation skills:

1. `api-documentation` owns the schema of the reference material.
2. `documentation-formatting` may normalize presentation without changing the
   API schema.
3. `developer-documentation` may provide surrounding onboarding pages, but
   should not force tutorial structure onto pure reference pages.

## Review gate

Do not consider the output complete unless the answer to all of these is yes:

- Is the page optimized for lookup?
- Are public methods, properties, and returns documented clearly?
- Are examples realistic and type-appropriate?
- Are related references and integration paths linked?
- Did the page avoid drifting into onboarding or feature-tour prose?
