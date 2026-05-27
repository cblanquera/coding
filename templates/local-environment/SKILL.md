---
name: local-environment
description: Copy this template into skills/local-environment when you want a personal, machine-local overlay for executable paths, runtime preferences, verification commands, and other host-specific notes that should not be committed to the shared repo.
---

# Local Environment Template

This is a copyable template for a personal `local-environment` skill.

Do not use this file in place. Copy it to `skills/local-environment/SKILL.md`,
customize it for your machine, and keep that local skill out of git.

## Purpose

Use `local-environment` to describe host-specific runtime and executable
preferences that are true on your computer but should not become shared repo
instructions.

Examples:

- preferred `node`, `npm`, `yarn`, `pnpm`, or `bun` paths
- preferred browser or Playwright-related executables
- helper CLI locations
- validation commands that confirm the right executable is being used
- machine-local notes that help Codex resolve the right toolchain

Keep this skill open-ended. Add only the details that are useful on your
machine.

## Suggested Pattern

- List the executable paths you want Codex to prefer.
- Add a short note about when each path should be used.
- Add a verification command when it helps confirm the executable is correct.
- Add fallback notes if a tool is missing or should only be used in certain
  repos.

## Example Shape

You may use sections like these if they help, but they are examples only:

- Runtimes
- Package managers
- Browser tooling
- Other executables
- Verification commands
- Notes

## Usage Notes

- `chrisai-router` may consult `local-environment` when a task likely depends
  on host-specific runtime or executable resolution.
- If `local-environment` does not exist, shared ChrisAI skills should continue
  normally without mentioning it.
- Keep real machine-specific paths in your local copy only, not in this
  template.
