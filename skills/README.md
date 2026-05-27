# ChrisAI Skills

This folder contains the active ChrisAI skill set for the `cblanquera` coding
repositories.

## Included Skills

| Skill | Purpose |
| --- | --- |
| `chrisai-router` | Canonical router for ChrisAI documentation, coding, and QA tasks. |
| `chrisai` | Short alias entrypoint for `chrisai-router`. |
| `chrisai-docs-dev-api-reference` | Write or restructure junior-developer-facing API reference docs. |
| `chrisai-docs-dev-onboarding` | Write or restructure onboarding docs, quick starts, tutorials, and conceptual developer guides. |
| `chrisai-docs-copy-editing` | Proofread and tighten existing developer-facing documentation without changing technical meaning. |
| `chrisai-docs-dev-formatting` | Normalize markdown structure and formatting using the repo's documentation style rules. |
| `chrisai-coding-engineering` | Frame architecture, abstractions, runtime boundaries, and refactor-versus-rewrite decisions before language-specific implementation details. |
| `chrisai-coding-html-css` | Write or review vanilla HTML and CSS for static sites and docs pages. |
| `chrisai-coding-js` | Write or review JavaScript using the repo's coding conventions across `.js`, `.mjs`, and `.cjs`. |
| `chrisai-coding-ts-react` | Write or review React TSX using the repo's conventions. |
| `chrisai-coding-ts-tests` | Write or review TypeScript tests using the repo's testing conventions. |
| `chrisai-coding-ts` | Write or review TypeScript implementation details using the repo's coding conventions, not framework or architecture boundaries. |
| `chrisai-qa-playwright` | QA local web projects through localhost preview detection, Playwright capture, and responsive browser checks. |
| `github-pages-vanilla` | Coordinate vanilla static documentation sites with GitHub Pages-compatible output, `specs/` source docs, generated `docs/`, and repo-local build scripts. |

## Notes

- `old_skills/` remains the migration source for the legacy versions.
- `chrisai-router` is the canonical ChrisAI router for docs, coding, and QA
  work.
- `chrisai` is the preferred short alias for human-facing invocation.
- `chrisai-coding-engineering` is the coding-family design pass for
  architecture-heavy tasks and should usually hand off to a narrower coding
  specialist for implementation and final style normalization.
- `github-pages-vanilla` is an active non-ChrisAI manager skill and is not
  routed through `chrisai-router`.
- Users may optionally create a gitignored `skills/local-environment/` skill
  for machine-specific runtime paths, executable preferences, and other
  host-local toolchain notes.
- `templates/local-environment/` contains a copyable example for creating that
  personal overlay.
- Specialist skills are written for direct invocation and must not behave like
  sibling routers.
- Each skill may include `agents/openai.yaml` for Codex display metadata and a
  default prompt, but `SKILL.md` remains the source of truth for behavior.
