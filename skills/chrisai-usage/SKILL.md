---
name: chrisai-usage
description: Use when a task should be handled with the ChrisAI skill family and Codex needs to choose the narrowest documentation, coding, or browser-QA specialist without relying on legacy routers.
---

# ChrisAI Usage

This skill is the only ChrisAI router.

Use it to decide whether a task belongs to the ChrisAI documentation, coding,
or QA skill family, then hand the work to the narrowest matching specialist
skill.

Do not duplicate specialist instructions here. Route, then defer.

## Routing Model

- `chrisai-usage` may auto-route to ChrisAI specialist skills.
- Specialist skills may be invoked directly by a human user.
- Specialist skills must not auto-route to sibling skills.
- Do not reference or rely on deprecated intermediate routers.
- `chrisai-usage` is the only shared ChrisAI skill that may actively consult a
  machine-local `local-environment` overlay.

## Local Environment Overlay

Use `local-environment` only as an optional machine-local override layer for
runtime and executable resolution.

- Look for `local-environment` only when the task likely depends on host-
  specific executables, runtime paths, package managers, browser tooling, or
  similar machine-local details.
- If `local-environment` exists, use it to prefer the local machine's intended
  executable paths or verification commands.
- If `local-environment` does not exist, continue silently with normal
  behavior.
- Do not ask the user about a missing `local-environment`.
- Do not consult `local-environment` for pure documentation, conceptual, or
  routing-only work.
- Do not force specialist skills to repeat this lookup unless they are invoked
  directly and runtime resolution is actually needed.

## Documentation Routes

Choose exactly one documentation specialist unless the task clearly needs a
deliberate sequence.

- Use `chrisai-docs-dev-api-reference` for API pages, module/class/function
  reference docs, config docs, and lookup-oriented examples.
- Use `chrisai-docs-dev-onboarding` for quick starts, tutorials, conceptual
  guides, and junior-developer-first learning flows.
- Use `chrisai-docs-copy-editing` for proofreading, wording cleanup, clarity
  improvement, tone consistency, and prose simplification without changing
  technical meaning.
- Use `chrisai-docs-dev-formatting` for markdown normalization, structure
  cleanup, outline numbering, TOC decisions, and style-guide conformance after
  the document type is already understood.

Only chain documentation specialists when there is a clear owner plus a clear
follow-up:

1. content owner first
2. copy editing second when the prose needs an editorial pass
3. formatting last if the output still needs structure cleanup

Do not default to multi-skill documentation sequences.

## Coding Routes

Choose exactly one coding specialist unless the task crosses a real boundary.

- Use `chrisai-coding-ts` for TypeScript implementation or refactors outside
  React and outside test-specific work.
- Use `chrisai-coding-ts-react` for TSX components, React hooks, and React UI
  code.
- Use `chrisai-coding-ts-tests` for Jest, Mocha, Chai, or test-coverage work
  around TypeScript code.
- Use `chrisai-coding-html-css` for plain HTML and CSS in static sites, docs
  pages, and frontend templates.

## QA Routes

Choose `chrisai-qa-playwright` when the deliverable is browser QA rather than
feature implementation.

- Use `chrisai-qa-playwright` for browser QA, Playwright screenshots, video
  recordings, and localhost responsive checks for local web projects.
- Do not route generic coding work there.
- Do not route explicit manual `@browser` inspection there unless the request
  is clearly about QA or capture through the ChrisAI flow.

## Decision Rules

- Prefer the narrowest specialist that fully owns the task.
- Do not invoke a broader skill when a more specific one clearly matches.
- If the request mixes onboarding and reference, choose the primary user goal
  first; only add formatting later if needed.
- If the request is mainly about proofreading, clarity, transitions, or tone
  rather than document ownership, prefer `chrisai-docs-copy-editing`.
- If the request mixes React code and tests, pick the side that owns the asked
  deliverable. A new test suite belongs to `chrisai-coding-ts-tests`.
- If the request is about rendered browser behavior, screenshots, or recorded
  flows, prefer `chrisai-qa-playwright` over coding specialists.
- If the request needs concrete local runtime or executable paths, consult
  `local-environment` first when it exists.
- If the request is outside the ChrisAI scope, do not force ChrisAI routing.

## Review Gate

Do not consider routing complete unless the answer to all of these is yes:

- Is this task actually a ChrisAI task?
- Did the selected skill match the user's real deliverable?
- Was the narrowest applicable specialist chosen?
- Was any multi-skill sequence justified instead of automatic?
