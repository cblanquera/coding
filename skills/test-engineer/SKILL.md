---
name: test-engineer
description: Use this skill when writing, expanding, or reviewing tests in the cblanquera coding repos. It consolidates the repo's Jest, Mocha, Chai, and coding standards into one Codex-oriented workflow, including framework selection, coverage targets, deterministic test design, strict TypeScript rules, boundary-only mocking, and comment-heavy test structure.
---

# Test Engineer

Use this skill for test implementation, test refactors, test reviews, and
coverage work in the `cblanquera` coding repositories.

## Priority Order

Apply rules in this order:

1. Match the existing test framework and style in the touched repo or file.
2. Apply the standards in this skill.
3. If a local pattern conflicts with this skill, preserve the local pattern
   unless the user asks to normalize or migrate it.

Do not switch a repo from Jest to Mocha/Chai, or the reverse, unless the user
explicitly asks for a migration.

## Framework Selection

- Use Jest rules when the repo or touched tests already use Jest.
- Use Mocha + Chai rules when the repo or touched tests already use them.
- For React component tests, prefer the repo's existing React testing stack.
- When no framework is obvious, inspect the repo before writing tests and pick
  the framework already present in configuration, dependencies, or nearby test
  files.

## Coverage Targets

- Unless the user says otherwise, acceptable coverage is above `70%`.
- Treat `80%` as the default deployment-ready target.
- Do not stretch for `>90%` coverage unless it happens naturally.
- Increase coverage by adding meaningful tests around real behavior, not by
  padding trivial lines or over-mocking.
- Focus first on conditionals, branches, error paths, loops, and public
  side-effects.

## Shared Testing Principles

- Test behavior, not implementation details.
- Keep tests fast, isolated, deterministic, and runnable in any order.
- Avoid real network, filesystem, clock, randomness, environment, or process
  dependencies unless the test is explicitly integration-level.
- Mock or stub only true boundaries. Do not mock the code under test into
  tautologies.
- Prefer builders or typed factories over large static fixtures.
- Keep one clear behavior theme per test. Multiple related assertions are fine
  when they describe the same behavior.
- Remove `.only`, hidden global state, and order dependence before finishing.
- Fix type errors and remove unused variables before trying to run tests.

## Commenting Style For Tests

The user prefers many comments that explain what each test is trying to prove.
Bias toward more comments, not fewer, when the flow or intent is not obvious.

- Add short `//` comments before setup, action, and assertion blocks when
  practical.
- Explain the scenario, why the setup matters, and what the test is attempting
  to validate.
- Keep comments factual and local to the code they describe.
- Prefer several small comments over one large paragraph.
- Let the comments read top-to-bottom like a guided walkthrough of the test.
- Follow the project inline comment style: `//Comment`, not `// Comment`.
- Use `/** ... */` only for JSDoc on exported test helpers or important shared
  utilities.
- Do not leave commented-out code in committed work.

Example:

```ts
//Build a user with a valid default shape first so this test only changes
//the field that matters for the failing branch.
const user = makeUser({ email: '' });

//Run the public validator instead of touching internal helper methods so
//the test stays stable during refactors.
const result = validateUser(user);

//Confirm the validator rejects the bad email in the same way production
//callers would observe it.
expect(result.ok).to.equal(false);
```

## Test Naming And Structure

- Use descriptive `describe` and `it` titles that read like behavior.
- Avoid vague names like `test getUser` or `works`.
- Group related scenarios together, but keep tests independent.
- Prefer local setup inside the test unless shared hooks clearly reduce noise.
- Use `beforeEach` and `afterEach` for resettable state.
- Use `before` and `after` only for expensive setup that is truly safe to
  share.

## TypeScript Rules In Tests

- Respect strict TypeScript rules in tests the same way as production code.
- Never use `any` unless the user explicitly accepts it. Prefer `unknown` and
  narrow before asserting.
- Prefer `satisfies` over `as` when validating object shapes.
- Add small narrowing helpers when repeated error or union checks would
  otherwise clutter tests.
- Keep test helpers typed so mocks, fixtures, and builders fail loudly when
  production contracts change.

## Determinism And Boundaries

- Fake or control time for time-dependent tests.
- Stub randomness, UUID generation, dates, and unstable environment values.
- Silence logs when they create noise without adding signal.
- Use unique temp paths or in-memory replacements when filesystem behavior
  matters.
- Assert on owned error messages or error shape, not brittle third-party
  wording.

## Jest Rules

- Mirror the repo's existing Jest file placement. If there is no clear local
  pattern, prefer mirrored test paths.
- Always await async work.
- Prefer explicit assertions over large snapshots.
- Use `beforeEach` and `afterEach` to reset mocks and modules when the suite
  needs it.
- Use `findBy` queries, `waitFor`, or resolved promises instead of timeouts.
- Mock only boundaries such as I/O, network, time, randomness, and browser
  APIs.
- For React tests, prefer React Testing Library and user-observable behavior.
- Use `@testing-library/user-event` for interaction flows when that stack is
  present.
- Do not use shallow rendering.

Jest-specific pitfalls:

- If `mockResolvedValue` infers `never`, give the mock an explicit promise
  return type.
- If `describe`, `it`, or `expect` are untyped, make sure test tsconfig types
  include Jest.

## Mocha + Chai Rules

- Standardize on `expect` assertions when the repo uses Chai.
- Use `async/await` and promise-based assertions. Do not use `done` callbacks.
- Use `chai-as-promised` and `sinon-chai` when the repo already depends on
  them.
- Create a Sinon sandbox for suites or tests that stub behavior, and restore it
  in `afterEach`.
- Use fake timers for time-dependent behavior and always restore them.
- Keep Chai assertions focused on observable outcomes and visible side-effects.

## React Test Rules

- Test the DOM and interactions the way a user experiences them.
- Prefer roles, labels, and accessible names over brittle selectors.
- Test effects through visible behavior, not hook internals.
- Avoid giant snapshots and implementation-coupled assertions.

## Coding Standards Inside Tests

- Match the style of the surrounding repo first.
- Use 2 spaces for indentation. Never use tabs.
- Prefer single quotes for strings.
- Use template literals for interpolation or multiline text.
- Use double quotes only when target syntax requires it, such as JSX or HTML
  attributes.
- End statements with semicolons.
- Do not add semicolons after `if`, `for`, or `while` blocks.
- Do end `do...while` statements with a semicolon.
- Aim for `<= 80` characters when practical.
- Avoid going past `100` characters unless the file already does so
  consistently.
- Keep one blank line between logical blocks.
- Avoid multiple consecutive blank lines.
- Use spaces inside non-empty arrays and objects.
- Use empty arrays and objects as `[]` and `{}`.
- Use descriptive names instead of single-letter names or unclear
  abbreviations.

## Review Checklist

Before finishing test work, verify that:

- the chosen framework matches the repo
- the tests assert public behavior
- mocks and stubs stop at real boundaries
- async tests await all meaningful work
- time, randomness, and shared state are controlled
- comments explain the scenario and intent of each non-trivial test
- coverage is above `70%`, with `80%` as the default deployment-ready target
- there is no `.only`, dead code, or unused setup left behind
