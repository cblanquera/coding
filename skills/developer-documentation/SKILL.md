---
name: developer-documentation
description: Use this skill when creating or restructuring documentation for developers, especially onboarding guides, quick starts, tutorials, getting-started docs, or platform/framework docs that should move readers from first success to deeper understanding with minimal friction.
---

# Developer Documentation

This skill is an editorial standard for AI-written developer documentation.

Its job is to produce documentation that increases adoption by making the first experience obvious, fast, and low-friction. The standard combines:

- a Diataxis-like separation of tutorial, how-to, explanation, and reference
- progressive disclosure
- Laravel's older standard of very clear, concise documentation

Do not write docs as a knowledge dump. Do not optimize for completeness on the first page. Optimize for successful onboarding first.

## Scope

Use this skill for:

- onboarding guides
- quick starts
- tutorials
- conceptual explanations
- restructuring developer docs for clarity and adoption

Do not use this skill as the primary rule set for:

- markdown formatting normalization
- rigid heading or numbering enforcement
- API reference schema design

For those cases, use:

- `documentation-formatting`
- `api-documentation`

## Priority

When this skill is used with other documentation skills:

1. `developer-documentation` decides what content appears, in what order, and for which reader state.
2. `api-documentation` decides the structure of pure API reference pages.
3. `documentation-formatting` standardizes presentation without overriding the intended reader flow.

Do not force onboarding patterns onto pure API reference pages. Do not let formatting rules override first-success sequencing.

## Non-negotiable rules

- Prioritize time to first success over feature completeness.
- Reduce cognitive load at every step.
- Introduce concepts only when the reader needs them.
- Keep onboarding, explanation, and reference separate.
- Prefer one recommended path before presenting alternatives.
- Use very clear, concise language.
- Remove anything that does not help the reader act or understand.

If the user asks for documentation that mixes tutorial, concept, and reference content into a single dense page, restructure it unless they explicitly require the mixed format.

## Editorial model

Assume the reader is in one of four states:

1. Evaluating: "What is this and why would I use it?"
2. Trying: "Show me the fastest way to make it work."
3. Learning: "Explain how this system works."
4. Returning: "I need a specific detail now."

Write so the reader can move from one state to the next without being forced to absorb later-stage detail too early.

## Required structure

Unless the user explicitly requests another structure, documentation must be organized in this order:

1. `Start here`
2. `Quick start`
3. `What just happened`
4. `Core concepts`
5. `Common tasks`
6. `Next steps`
7. `Reference`

If the deliverable is only one page, compress this structure but preserve the sequence.

## Section standard

### Start here

Must answer all of the following quickly:

- What the product, library, API, or framework does
- Who it is for
- What the reader will accomplish next

Constraints:

- Keep it short.
- Do not lead with architecture.
- Do not lead with philosophy.
- Do not lead with edge cases.

### Quick start

Must provide the shortest realistic path to a visible success state.

Requirements:

- Use one happy path.
- Minimize prerequisites.
- Prefer copy-pasteable steps.
- End with a clear verification step.

Constraints:

- Do not branch early unless most readers would fail without the branch.
- Do not explain every option.
- Do not interrupt the flow with deep background.

### What just happened

Must convert the quick start into understanding.

Cover:

- what the reader built or configured
- why each major step mattered
- what is essential versus optional

Constraints:

- Use plain language.
- Keep the explanation anchored to the quick start.
- Do not repeat setup instructions verbatim.

### Core concepts

Must explain the mental model after the reader has a concrete anchor.

Cover:

- main nouns
- moving parts
- how the pieces fit together

Constraints:

- Keep abstractions grounded.
- Prefer one small example over broad theory.
- Do not repeat task instructions.

### Common tasks

Must be organized by user intent, not implementation detail.

Good examples:

- create a route
- call the API
- add authentication
- deploy the app
- customize configuration

Constraints:

- Each task must be independently scannable.
- Each task must solve a real follow-up need.
- Do not hide core tasks inside long narrative pages.

### Next steps

Must guide the reader to the most likely follow-up actions.

Point to:

- likely tutorials
- production guidance
- advanced capabilities
- troubleshooting when first-run failure is common

### Reference

Must be optimized for lookup, not first reading.

Good reference content:

- configuration options
- CLI commands
- API methods
- events and hooks
- schema details

Constraints:

- Do not let reference material take over onboarding pages.
- Do not explain reference pages like tutorials unless the user explicitly asks for that.

## Writing standard

- Lead with outcomes before internals.
- Use short sections and descriptive headings.
- Introduce one new idea at a time.
- Prefer concrete examples over abstraction.
- Prefer simple sentences over clever sentences.
- Prefer active voice.
- Use jargon only when necessary, and define it at first use.
- State tradeoffs only when the decision matters now.

## Compression standard

AI tends to over-explain. Do not do that.

Before finalizing, cut:

- repeated explanation
- throat-clearing introductions
- feature tours on onboarding pages
- optional branches that do not matter yet
- background that does not help the next action

If a paragraph does not help the reader do something, verify something, or understand a current concept, remove it.

## Decision rules

When there is tension between completeness and usability:

1. Choose usability for the first page.
2. Move extra detail to a later section.
3. Keep the main path intact.

When there is tension between explaining and doing:

1. Let the reader succeed first.
2. Explain immediately after success.

When there is tension between many valid paths:

1. Recommend one path.
2. Mention alternatives briefly.
3. Move full comparison later.

## Restructuring existing docs

When rewriting existing documentation:

1. Identify the current first page for a new developer.
2. Remove or relocate content that blocks first success.
3. Create a shorter happy-path quick start.
4. Separate explanation from tutorial flow.
5. Separate tasks from reference.
6. Verify that each page serves one reader stage well.

## Anti-patterns

Do not:

- start with architecture before the reader has done anything
- explain every feature before showing one useful outcome
- present many installation variants on the first page
- mix onboarding with advanced operations
- mix tutorial content with exhaustive reference
- use completeness as an excuse for poor sequencing

## Review gate

Do not consider the output complete unless the answer to all of these is yes:

- Can a new developer understand the product's purpose within the first minute?
- Can they reach a visible success state quickly?
- Is there one recommended first path?
- Are concepts introduced after first success, not before?
- Are common tasks organized by user intent?
- Is reference separate from onboarding?
- Is the writing clear and concise enough for a distracted developer to follow?

## Output defaults

Default deliverables should be one of:

- a docs outline with section summaries
- a rewritten onboarding page
- a quick start followed by explanation
- a reorganization plan split into tutorial, tasks, explanation, and reference

If the user asks for only one page, still preserve this internal order:

1. orientation
2. fast success path
3. explanation
4. next steps

## Operating prompt

Use this internal prompt when applying the skill:

"Write very clear, concise developer documentation. Optimize for first success, then progressive understanding, then lookup. Keep tutorial flow, task guidance, explanation, and reference separate. Recommend one path first. Remove anything that slows down onboarding."
