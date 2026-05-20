---
name: github-pages-qa-recording
description: Run QA and capture Playwright video recordings for a generated GitHub Pages site. Use this skill when Codex needs to start a localhost preview, validate responsive and visual behavior through scripted browser flows, diagnose preview blockers, and record the generated output.
---

# GitHub Pages QA Recording

Use this skill when the main problem is validating or recording the generated
site, not deciding repo layout or visual direction.

This skill must be usable on its own. Do not require
`github-pages-docs-builder` to be active in order to run preview, QA, or
recording work. If the repo already exposes enough build and preview contract
through its files, proceed directly with this skill.

This skill owns:

- localhost preview startup for generated GitHub Pages sites
- Playwright-driven browser QA workflow
- responsive and visual checks during scripted flows
- video recording capture
- separating repo-side preview gaps from environment-side blockers

This skill does not own:

- repo migration policy
- builder structure decisions
- template or CSS implementation
- broader visual-system direction

Use [`github-pages-docs-builder`](../github-pages-docs-builder/SKILL.md) when
the task still needs build-contract or repo-structure decisions.

## Runtime And Command Rules

Before running QA commands:

- resolve a concrete Node runtime that is version 22 or higher
- prefer the repo's declared toolchain when present, such as `package.json`
  engines, Volta, `nvm`, `.node-version`, or an existing project wrapper
- do not rely on an unspecified ambient Node version when the repo provides a
  clearer runtime contract
- use `yarn` with that resolved Node 22+ runtime for build, serve, and check
  commands
- if Node 22+ cannot be resolved, report that as a blocker because preview
  startup and Playwright recording may be invalid or unavailable without the
  correct runtime

Before installing or using browser automation tooling:

- do not require the target project to add `playwright` as a dependency just
  for docs QA unless the user explicitly asks for that
- prefer a repo-local temporary QA workspace at `.playwright/` when browser
  tooling must be bootstrapped
- treat `.playwright/` as disposable QA infrastructure owned by the skill, not
  as application source
- before creating that workspace, check whether `.playwright/` already exists
  and already contains the required tooling and browser binaries
- if the required tools are already present in `.playwright/`, reuse them
  instead of reinstalling
- if the workspace must be created or updated, notify the user afterward that
  `.playwright/` was added and they may want to remove it later or add it to
  `.gitignore`
- do not scatter temporary Playwright files across the project when the
  `.playwright/` workspace is being used

Treat `.playwright/` as the default local QA workspace layout:

- `.playwright/package.json` for the temporary tool manifest when needed
- `.playwright/node_modules/` for the temporary Playwright package install
- `.playwright/browsers/` for browser binaries via
  `PLAYWRIGHT_BROWSERS_PATH`
- `.playwright/artifacts/` for optional recordings, screenshots, traces, or QA
  outputs when the workflow needs a durable local artifact path
- `.playwright/artifacts/video/` for finalized recording files

When checking whether the temporary workspace is already usable:

- verify the Playwright package is resolvable from `.playwright/node_modules/`
- verify the required browser executable is already present under
  `.playwright/browsers/` or whatever browser cache path the skill configured
- only install missing pieces; do not reinstall both the package and browsers
  when only one is absent

Before choosing preview commands:

- inspect the nearest relevant `package.json` for docs-site scripts
- if `www:serve` exists, use `yarn www:serve` for local preview QA
- if `www:check` exists, use `yarn www:check` before or alongside browser QA
- if `www:build` exists, run it before preview when generated output may be
  stale
- if those `www:*` commands do not exist, fall back to the repo's actual
  build, serve, and check commands instead of inventing new ones
- if no build, serve, or check commands are found, then report that clearly
  instead of inventing new commands or assuming defaults
- when reporting what you ran, name the exact package root and commands used

If the repo has multiple package roots:

- choose the package whose scripts own the generated docs site
- do not assume the workspace root `package.json` is the correct entrypoint
- report ambiguity clearly if more than one package could own preview startup

When doing browser QA for the generated docs site:

- use the repo-root helper at
  `skills/github-pages-qa-screenshot/scripts/localhost_preview.py` to run the
  build and preview commands with `HOST` and `PORT` bound for localhost testing
- treat that helper as part of this repository's skill source, not part of the
  target project being tested
- do not search the target project for `scripts/localhost_preview.py`
- do not report a missing repo-local `scripts/localhost_preview.py` as a repo
  gap or propose adding one to the target project
- keep the actual build, serve, and check commands repo-specific; the script is
  only a wrapper for consistent preview startup
- when `www:serve` exists, prefer wrapping `yarn www:serve`
- when `www:check` exists, prefer running `yarn www:check` as part of QA
- when `www:build` exists and output freshness is uncertain, prefer running
  `yarn www:build` before preview startup
- when Playwright is needed for scripted QA and it is not already available
  through the active runtime, bootstrap it inside `.playwright/` before
  declaring browser automation unavailable
- when bootstrapping Playwright in `.playwright/`, configure the install so
  package files and browser binaries remain inside that workspace rather than
  inside the target project's normal dependency tree
- use a Playwright-launched browser for recording, not the Codex in-app browser
- if Playwright recording cannot run, report that clearly instead of silently
  switching to Safari, Chrome, or another external browser outside Playwright

Before relying on the wrapper:

- ensure the target project's repo-root `.playwright/serve.mjs` or equivalent
  preview entrypoint honors both `HOST` and `PORT`
- if the preview server ignores `HOST`, update the project-side serve script to
  pass the requested host into the server bind call

If local preview or browser automation is blocked by the environment or
sandbox:

- say so clearly
- separate the repo-side gap from the environment-side blocker
- do not misclassify an environment restriction as a project bug
- distinguish between "Playwright not installed yet" and "Playwright could not
  be bootstrapped into `.playwright/` because of environment restrictions"
- include whether the blocker came from unresolved Node 22+, failed `yarn`
  commands, preview startup failure, or inability to run Playwright recording

## Browser QA Rules

Validate the generated site, not the source tree.

- run or confirm the build before visual QA
- run a repo check command before finishing when one exists; prefer
  `yarn www:check` when that script is available
- prefer localhost-only preview binds when browser automation needs them
- perform visual checks through Playwright automation against the localhost
  preview
- check more than one viewport when layout work was touched
- focus findings on visible defects, broken navigation, missing assets,
  unreadable code blocks, and obvious metadata issues
- record only after confirming the rendered page matches the generated output
  you intend to show
- if scripted browser QA could not be completed, say exactly why and whether
  the root cause was runtime resolution, preview startup, Playwright bootstrap,
  or a repo issue

## Recording Rules

When capturing recordings:

- record to `.playwright/artifacts/video/` unless the user asked for a
  different artifact path
- choose flows that demonstrate the relevant layout, interaction, or bug
  clearly
- record the homepage when visual direction changed materially
- record at least one representative article page when shared layout changed
- note the viewport used for each recording
- finalize the recording by closing the Playwright browser context before
  reporting completion
- report the recorded route or flow and the output path for each artifact
- if a recording is blocked by preview failure, report the exact blocker
  instead of pretending the QA completed

When writing Playwright recording flows:

- keep the flow minimal and deterministic
- prefer stable selectors and explicit waits over fragile timing assumptions
- use `browser.newContext({ recordVideo: ... })` rather than external screen
  capture tools
- keep viewport and recording size aligned unless a mismatch is required for a
  specific reason
- avoid recording irrelevant idle time; capture only the interaction sequence
  needed to validate or demonstrate the page

## QA Checklist

Before finishing visual QA, check the generated site for:

- homepage looks like a homepage rather than a raw documentation page
- text does not clip, overlap, or drift off-grid at common viewport widths
- navigation links reach the expected destinations
- pager and table-of-contents links resolve where applicable
- copied assets load correctly
- code blocks remain readable in all supported themes
- copy buttons are present and visually associated with code blocks when that
  feature is enabled
- obvious metadata surfaces such as title and description appear consistent
- light and dark mode both remain legible and visually coherent when those
  themes are supported

## Reporting Rules

Report findings in this order:

1. preview status
2. resolved Node version and package command entrypoint
3. recording coverage
4. defects or blockers
5. whether the blocker is repo-side, environment-side, or unresolved

If there are no findings, state that explicitly and mention any residual test
gaps such as unverified mobile widths or unavailable browser automation.
