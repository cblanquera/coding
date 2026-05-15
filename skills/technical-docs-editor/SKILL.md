---
name: technical-docs-editor
description: Edit technical documentation for open source libraries with a junior-developer audience. Use when Codex needs to proofread, clarify, simplify, restructure, or standardize docs such as API references, guides, walkthroughs, README sections, architecture notes, and conceptual explanations while preserving technical accuracy, code identifiers, API meaning, and intended behavior.
---

# Technical Docs Editor

This skill edits developer-facing documentation so junior developers can
understand it without losing technical precision.

Its role is editorial, not authorial. Improve clarity, sequencing, grammar,
consistency, and teaching value while preserving API meaning, behavioral
claims, code identifiers, and documented constraints.

## Task Intake

Before editing, identify:

1. the document type: reference, guide, walkthrough, README, explanation, or mixed page
2. the intended reader task: evaluating, integrating, debugging, or learning
3. whether the problem is wording, structure, missing context, or technical ambiguity
4. whether the request needs a light edit, standard edit, or substantive edit
5. whether another documentation skill should own the page shape first

If the task is mainly about building onboarding flow, quick starts, or
developer learning sequence, use `developer-documentation`. If the task is
mainly about API lookup structure, use `api-documentation`. If the task is
mainly about markdown cleanup, apply `documentation-formatting` after the
editorial issues are resolved.

## Scope

Use this skill for:

- editing existing technical prose
- improving junior-developer readability
- clarifying library behavior and integration guidance
- tightening conceptual explanations
- making terminology, assumptions, and transitions explicit
- standardizing tone and phrasing across related docs

Do not use this skill as the primary rule set for:

- generating a documentation set from scratch when information architecture is the main task
- defining API reference schemas
- mechanical markdown normalization without editorial review

For those cases, use:

- `developer-documentation`
- `api-documentation`
- `documentation-formatting`

## Audience Model

Assume the reader is a junior developer who:

- can read code and follow examples
- may not know framework jargon or project-specific shorthand
- benefits from explicit definitions and visible cause-and-effect
- needs assumptions stated clearly
- needs help understanding both what to do and why it works

Do not write down to the reader. Be direct, concrete, and technically
respectful.

## Editing Priorities

Apply these priorities in order:

1. Preserve technical truth.
2. Improve comprehension for junior developers.
3. Remove ambiguity, vagueness, and unexplained assumptions.
4. Improve structure, flow, and consistency.
5. Fix grammar, punctuation, and style.

## Core Rules

- Preserve API names, type names, file names, commands, and code identifiers exactly unless the source clearly shows they are wrong.
- Preserve semantics. Do not silently change behavior, requirements, defaults, side effects, guarantees, or limitations.
- Prefer plain language over expert shorthand.
- Define unfamiliar terms near first use.
- Expand vague statements into concrete ones when the source supports it.
- Make prerequisites and assumptions explicit.
- Prefer active voice and direct sentence structure.
- Prefer short paragraphs and example-led explanation when useful.
- Keep warnings, caveats, and constraints intact.
- If a technical claim cannot be verified from the local source, flag it instead of strengthening it.

## What To Improve

Improve:

- grammar, punctuation, spelling, and syntax
- dense or compressed explanations
- missing transitions
- undefined terminology
- inconsistent naming
- over-abstract phrasing
- explanations that assume too much prior knowledge
- explanations that describe mechanics without user meaning
- sections that bury the main point or sequence

## What To Protect

Do not:

- invent features, guarantees, or limitations
- smooth away important distinctions
- replace precise terms with looser ones when precision matters
- rewrite code examples unless needed for correctness or clarity
- remove caveats that affect correct usage
- present guesses as facts

## Preferred Editorial Moves

When useful:

- add one short framing sentence before deep detail
- convert abstract wording into concrete outcomes
- explain a concept before listing its edge cases
- add brief "why this matters" context when it improves understanding
- distinguish similar concepts explicitly
- make sequencing and dependency visible
- break overloaded paragraphs into smaller units
- use examples to anchor behavior claims

## Edit Modes

Choose the lightest mode that fits the request.

### Light Edit

Use for small cleanup passes.

- fix grammar, punctuation, wording, and obvious clarity issues
- preserve the existing structure

### Standard Edit

Use for most documentation passes.

- improve wording, transitions, local flow, consistency, and readability
- reorganize locally when needed
- keep the overall document shape unless it is actively harmful

### Substantive Edit

Use when the draft is technically correct but hard to learn from.

- restructure sections
- rewrite for teaching clarity
- add clearer framing and sequencing
- preserve meaning and technical claims

## Workflow

1. Read the full local context before editing so behavior claims are not changed casually.
2. Identify the target reader task and the main source of confusion.
3. Decide whether the page needs light, standard, or substantive editing.
4. Clarify the main idea of each section before rewriting sentences.
5. Rewrite for junior-developer comprehension while preserving precise meaning.
6. Check terminology, identifiers, defaults, and constraints against the local source.
7. Flag technical uncertainties instead of guessing.
8. If the document also suffers from weak onboarding or weak reference structure, hand off to `developer-documentation` or `api-documentation` as appropriate.
9. Apply `documentation-formatting` last when formatting cleanup is needed.

## Output Expectations

When editing, return:

- the revised text
- a short summary of the main improvements
- any flagged technical uncertainties or open questions

When reviewing without rewriting, return:

- specific clarity issues
- specific accuracy risks
- concrete revision recommendations

## Review Gate

Do not consider the output complete unless the answer to all of these is yes:

- Can a junior developer understand the main point of the page?
- Are terms defined before they are used heavily?
- Are claims precise and not overstated?
- Are assumptions and prerequisites explicit?
- Does the section flow match the learning path?
- Did code identifiers and technical behavior remain accurate?
- Is the revised version clearer without becoming less correct?
