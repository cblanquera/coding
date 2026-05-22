---
name: chrisai-docs-dev-onboarding
description: Use when creating or restructuring developer-facing onboarding documentation for junior developers, especially quick starts, tutorials, getting-started guides, and conceptual docs that should lead to first success with low friction.
---

# ChrisAI Docs Dev Onboarding

This skill is the editorial standard for onboarding-oriented developer
documentation aimed at junior developers.

Its job is to make the first experience obvious, fast, and low-friction. Do
not write docs as a knowledge dump. Optimize for successful onboarding first.

## Task Intake

Before drafting or restructuring, identify:

1. who the reader is
2. whether they are evaluating, trying, learning, or returning
3. the first visible success the page should create
4. what content is really reference material and should move out of the main
   flow
5. whether the result should be one page, a short guide set, or a landing page
   with follow-up links

If the request is mainly API lookup content, switch to
`chrisai-docs-dev-api-reference`. If the flow is already sound and the task is
mostly cleanup, apply `chrisai-docs-dev-formatting` after the content plan is
settled.

## Scope

Use this skill for:

- onboarding guides
- quick starts
- tutorials
- conceptual explanations
- restructuring developer docs for clarity and adoption

Do not use this skill as the primary rule set for API reference schema design
or markdown normalization.

## Non-Negotiable Rules

- Prioritize time to first success over feature completeness.
- Reduce cognitive load at every step.
- Introduce concepts only when the reader needs them.
- Keep onboarding, explanation, and reference separate.
- Prefer one recommended path before presenting alternatives.
- Use clear, concise language.
- Remove anything that does not help the reader act or understand.

## Default Reader Flow

Unless the user explicitly requests another structure, organize onboarding docs
in this sequence:

1. `Start here`
2. `Quick start`
3. `What just happened`
4. `Core concepts`
5. `Common tasks`
6. `Next steps`
7. `Reference`

If the deliverable is only one page, compress this structure but preserve the
sequence.

## Section Standard

- `Start here` must answer what this is, who it is for, and what the reader
  will accomplish next.
- `Quick start` must be the shortest realistic path to a visible success
  state.
- `What just happened` must convert the quick start into understanding.
- `Core concepts` must explain the mental model after the reader has a concrete
  anchor.
- `Common tasks` must be organized by user intent, not implementation detail.
- `Next steps` must point to the most likely follow-up actions.
- `Reference` must stay lookup-oriented and not take over the page.

## Review Gate

Do not consider the output complete unless the answer to all of these is yes:

- Does the page create a clear first success?
- Is the order optimized for a junior developer?
- Was dense reference material kept out of the early flow?
- Are follow-up tasks and next steps easy to find?
- Did the page avoid becoming a feature dump?
