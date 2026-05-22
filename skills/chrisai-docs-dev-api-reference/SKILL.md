---
name: chrisai-docs-dev-api-reference
description: Use when writing or restructuring developer-facing API reference documentation for junior developers who need lookup-friendly docs for classes, modules, methods, configuration, and typed integration examples.
---

# ChrisAI Docs Dev API Reference

This skill writes API reference documentation for junior developers who already
know the surface they need and want accurate, scannable details.

Optimize for lookup, correctness, and integration guidance. Do not turn pure
reference pages into onboarding tutorials.

## Task Intake

Before drafting or restructuring, identify:

1. the documented surface: class, module, function, CLI, config, or schema
2. the intended reader: caller, integrator, maintainer, or migration reader
3. the missing details: signatures, defaults, errors, examples, or return
   behavior
4. the expected deliverable: single file, multi-file reference set, or index +
   detail pages

If the task is mainly onboarding, switch to `chrisai-docs-dev-onboarding`. If
the task is mainly markdown cleanup, apply `chrisai-docs-dev-formatting` after
the reference structure is decided.

## Scope

Use this skill for:

- class and module reference docs
- method, property, and configuration documentation
- type-safe usage examples
- API folder organization and cross-linking

Do not use this skill as the primary rule set for quick starts, tutorials, or
general markdown normalization.

## Default Page Structure

Unless the codebase has a stronger local pattern, organize API pages in this
order:

1. title and short description
2. minimal import or instantiation example
3. TOC when the page is long enough to need one
4. static properties or exports when relevant
5. static methods when relevant
6. instance properties or configuration
7. instance methods or operations
8. integration examples
9. related links

## Method Standard

For each public method or operation:

- describe what it does and when to use it
- show a realistic usage example
- document parameters in a table when parameters exist
- document the return value under `**Returns**` in prose, not a return table
- mention defaults, optional parameters, promises, and chaining when relevant

Do not document protected or private members unless the user explicitly asks.

## Example Standard

- Use complete, runnable, or nearly runnable examples.
- Include imports when they improve orientation.
- Prefer realistic names and values.
- Show TypeScript types when they clarify public usage.
- Progress from basic examples to integration examples when several are needed.

## Review Gate

Do not consider the output complete unless the answer to all of these is yes:

- Is the page optimized for lookup?
- Are public methods, properties, and returns documented clearly?
- Are examples realistic and junior-developer-friendly?
- Are related references and integration paths linked?
- Did the page avoid drifting into onboarding prose?
