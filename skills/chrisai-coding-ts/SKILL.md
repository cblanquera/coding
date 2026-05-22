---
name: chrisai-coding-ts
description: Use when writing or reviewing TypeScript in the cblanquera coding repos outside React-specific or test-specific work, especially for implementation, refactors, typing improvements, and module-level design cleanup.
---

# ChrisAI Coding TS

Use this skill for TypeScript implementation, refactors, and reviews.

## Repo Discovery Workflow

Before applying repo standards, inspect:

1. the touched file and nearby sibling files
2. project lint, formatter, and TypeScript config
3. existing import and export patterns in the same package
4. package runtime constraints such as ESM, Node version, and build output

If the repo already has a stronger local convention, preserve it.

## Priority Order

1. Match the existing style of the touched file when it is clear.
2. Apply the standards in this skill.
3. Preserve local patterns unless the user explicitly asks to normalize them.

## Core Rules

- Use clear, descriptive names.
- Keep comments factual and local to non-trivial logic blocks.
- Follow the repo's import grouping conventions when they are already in use.
- Keep arrays, objects, and exports readable before trying to compact them.
- Prefer strict typing and small helpers over `any`.

## Module Guidance

- Keep modules focused on one clear responsibility.
- Favor interfaces and types that make call sites easier to understand.
- Preserve ESM-safe local import behavior where the repo expects it.
- Make refactors small, focused, and easy to review.

## Review Gate

Do not consider the output complete unless the answer to all of these is yes:

- Does the file match the surrounding repo conventions?
- Are names and types easy to understand?
- Are imports, exports, and module boundaries readable?
- Did the change stay focused on the intended responsibility?
