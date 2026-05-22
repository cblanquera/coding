---
name: chrisai-coding-ts-tests
description: Use when writing, expanding, or reviewing TypeScript tests in the cblanquera coding repos, especially when choosing between Jest and Mocha/Chai patterns, improving coverage, or keeping tests deterministic and behavior-focused.
---

# ChrisAI Coding TS Tests

Use this skill for test implementation, test refactors, test reviews, and
coverage work in the `cblanquera` coding repositories.

## Repo Discovery Workflow

Before enforcing conventions, inspect:

1. the touched test file and nearby suites
2. test runner, assertion, and mocking libraries in config and dependencies
3. helper builders, fixtures, and shared setup already used nearby
4. whether the package expects unit, integration, DOM, or mixed testing

If the repo already has a stronger local pattern, preserve it.

## Priority Order

1. Match the existing test framework and style in the touched repo or file.
2. Apply the standards in this skill.
3. Preserve local patterns unless the user explicitly asks to normalize or
   migrate them.

## Shared Testing Principles

- Test behavior, not implementation details.
- Keep tests fast, isolated, deterministic, and runnable in any order.
- Mock or stub only true boundaries.
- Prefer builders or typed factories over large static fixtures.
- Use descriptive `describe` and `it` names.
- Fix type errors and unused variables before trying to run tests.

## Framework Rules

- Use Jest rules when the repo already uses Jest.
- Use Mocha + Chai rules when the repo already uses them.
- Do not switch frameworks unless the user explicitly asks for a migration.
- For React tests, prefer the repo's existing React testing stack.

## Commenting And Structure

- Add short `//` comments before setup, action, and assertion blocks when that
  improves readability.
- Keep comments factual and local to the code they describe.
- Prefer comments that explain what a scenario is trying to prove.

## Review Gate

Do not consider the output complete unless the answer to all of these is yes:

- Does the chosen framework match the repo?
- Do the tests assert public behavior?
- Are the tests deterministic and isolated?
- Are comments and names clear enough for another developer to follow?
