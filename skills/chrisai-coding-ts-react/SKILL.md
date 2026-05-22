---
name: chrisai-coding-ts-react
description: Use when writing or reviewing React TypeScript or TSX in the cblanquera coding repos, especially for components, hooks, and typed UI flows that should follow the repo's React structure and readability conventions.
---

# ChrisAI Coding TS React

Use this skill for TypeScript React implementation, refactors, and reviews.

## Repo Discovery Workflow

Before applying conventions, inspect:

1. the touched TSX file and nearby sibling components
2. project TypeScript, React, and linting setup
3. existing component, hook, and prop patterns nearby
4. any state-management or rendering constraints already used by the package

If the repo already has a stronger local pattern, preserve it.

## Priority Order

1. Match the existing style of the touched file when it is clear.
2. Apply the standards in this skill.
3. Preserve local patterns unless the user explicitly asks to normalize them.

## Core Rules

- Keep prop types explicit and readable.
- Prefer a named `Props` type for non-trivial prop shapes.
- If destructuring becomes noisy, accept `props` first and unpack in the body.
- Wrap returned JSX in parentheses.
- Keep JSX readable instead of aggressively compact.

## Component Flow

Organize component internals in this order:

1. props
2. hooks
3. derived variables
4. handlers
5. effects
6. render

The component should read top-to-bottom like a story.

## Hooks And State

- Use clear, intent-based names for handlers and booleans.
- Keep side effects below the state and handlers they depend on.
- Prefer user-observable behavior over clever hook choreography.
- Preserve controlled vs uncontrolled input behavior intentionally.

## Review Gate

Do not consider the output complete unless the answer to all of these is yes:

- Are props and types easy to scan?
- Does the component flow read in a stable order?
- Are hooks, handlers, and effects placed coherently?
- Is the JSX readable and aligned with local repo patterns?
