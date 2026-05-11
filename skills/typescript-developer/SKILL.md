---
name: typescript-developer
description: Use this skill when writing or reviewing TypeScript in the cblanquera coding repos. It consolidates the repo's TypeScript and coding standards into one Codex-oriented workflow, including story-like block comments, strict import grouping with `//node`, `//modules`, and `//client`, ordered export sections, ESM-safe local imports, and the project's typing and class conventions.
---

# TypeScript Developer

Use this skill for TypeScript implementation, refactors, and reviews in the
`cblanquera` coding repositories.

## Repo Discovery Workflow

Before applying repo standards, inspect the local codebase in this order:

1. the touched file and nearby sibling files
2. project lint, formatter, and TypeScript config
3. existing import and export patterns in the same package
4. package runtime constraints such as ESM, Node version, and build output

If the repo already has a stronger local convention, preserve it. Use this
skill to fill gaps and make decisions when the local pattern is unclear.

## Task Intake

Decide early whether the work is mainly:

- implementation in an existing module
- refactor for clarity or typing
- module extraction or file split
- review of an existing TypeScript change

For module-boundary decisions and file-splitting guidance, read
`references/module-design.md` when needed.

## Priority Order

Apply rules in this order:

1. Match the existing style of the touched file when it is clear.
2. Apply the standards in this skill.
3. If a local pattern conflicts with this skill, preserve the local pattern
   unless the user asks to normalize the file.

Consistency beats preference. Keep changes small, focused, and easy to review.

## Core Formatting

- Use 2 spaces for indentation. Never use tabs.
- Prefer single quotes for strings.
- Use template literals for interpolation or multiline strings.
- Use double quotes only when the target syntax requires it, such as JSX or
  HTML attributes.
- End statements with semicolons.
- Do not add semicolons after `if`, `for`, or `while` blocks.
- Do end `do...while` statements with a semicolon.
- Keep lines compact and readable.
- Aim for `<= 80` characters when practical.
- Avoid going past `100` characters unless the file already does so
  consistently.
- Put opening braces on the same line.
- Keep exactly one blank line between logical blocks.
- Do not leave multiple consecutive blank lines.
- Do not use trailing commas in import lists or parameter lists.

## Commenting Style

The user prefers comments that read like a story and explain the flow of the
logic while browsing. Bias toward more comments, not fewer, when the code has
multiple steps or hidden assumptions.

- Add short `//` comments before each non-trivial logic block when practical.
- Explain why the next block exists, what state it prepares, and how it moves
  the flow forward.
- Keep comments factual and local to the code they describe.
- Prefer several small flow comments over one large paragraph.
- Let the comments read top-to-bottom like a guided walkthrough of the code.
- Follow the project inline comment style: `//Comment`, not `// Comment`.
- Use `/** ... */` only for JSDoc on exported or important public APIs.
- Do not add `@param`, `@returns`, or similar tags unless the user explicitly
  asks for them.
- Do not leave commented-out code in committed work.

Example:

```ts
//Load the saved session first so the rest of the flow can decide whether
//it should resume an existing login or start from scratch.
const session = await loadSession();

//If there is no usable session, build a fresh one before continuing so all
//later requests can assume authentication already exists.
if (!session) {
  return await createSession();
}
```

## Naming

- Use names that another developer can understand without reading comments.
- Avoid single-letter names and unclear abbreviations.
- Use camelCase for variables and functions.
- Use verb or verb-noun phrasing for functions, such as `getUser`.
- Use PascalCase for classes and components.
- Use nouns for classes, such as `TaskQueue`.
- Use booleans like `isReady`, `hasToken`, `canRetry`, or `shouldPersist`.
- Use kebab-case for folders and most files.
- If a file exports a default class or component, PascalCase is acceptable for
  the file name.

## Data Layout And Spacing

- Keep short arrays and objects on one line when they remain readable.
- Expand arrays and objects vertically when they become long.
- Use spaces inside non-empty arrays and objects.
- Do not use spaces inside empty arrays or objects.

Examples:

```ts
const list = [];
const item = {};
const shortList = [ 'foo', 'bar' ];
const shortMap = { foo: 'bar', baz: 'zoo' };
```

## Imports

Always group imports in exactly this order and label each group with section
comments:

1. `//node`
2. `//modules`
3. `//client`

Within each section, order imports like this:

1. named imports that are types
2. default imports that are types
3. named runtime imports
4. default runtime imports

Rules:

- Prefix native Node modules with `node:`.
- Use `.js` for client imports in ESM code.
- Use `//client`, not `//local`.
- Keep the section comments exactly as `//node`, `//modules`, and `//client`.
- Separate type imports from runtime imports even when they come from the same
  module.
- Separate default and named imports when needed to preserve the required
  ordering.
- If one source module needs multiple import forms, keep them on separate lines
  instead of combining them.
- When there is no stronger local convention, sort imports within the same
  subtype by module specifier.

Example:

```ts
//node
import type { IncomingMessage } from 'node:http';
import type FS from 'node:fs';
import { join } from 'node:path';
import http from 'node:http';

//modules
import type { Bar } from 'foo';
import type Foo from 'foo';
import { baz } from 'foo';
import { zoo } from 'foo/bar';

//client
import type { Jane } from './names.js';
import Jack from './names.js';
```

## Exports

When a module has multiple exports, emit them in this order:

1. Types
2. Constants
3. Functions
4. Classes
5. Default export

Rules:

- End export statements with semicolons, including exported functions and
  classes.
- Use section dividers only for blocks that actually exist.
- Skip empty sections.
- If there are only one or two exports in a category and no grouping benefit,
  plain exports without section dividers are fine.
- When there are enough exports that grouping improves scanning, use this exact
  divider format:

```ts
//--------------------------------------------------------------------//
```

Example:

```ts
//--------------------------------------------------------------------//
// Types

//One shared status code shape for the rest of the module.
export type StatusCode = number;

//--------------------------------------------------------------------//
// Constants

//Expose the common success code so callers do not repeat magic numbers.
export const ok = 200;

//--------------------------------------------------------------------//
// Functions

/**
 * Return the status code that should be sent to the caller.
 */
export function getStatus(code: number) {
  return code;
};

//--------------------------------------------------------------------//
// Classes

/**
 * Keep status-related behavior together in one place.
 */
export class StatusManager {};

//--------------------------------------------------------------------//
// Exports

export default getStatus;
```

## Types And Interfaces

- Prefer `type` for object shapes, function signatures, unions, and aliases.
- Use `interface` for class contracts and shapes that a class will implement.
- Do not add a semicolon after an `interface` block.
- In object types, separate properties with commas, not semicolons.
- Put one space after a type colon and no space before it.
- Put spaces around `|` and `&` in unions and intersections.
- Prefer built-in utility types like `Record`, `Pick`, `Omit`, `Partial`, and
  `Required` when they keep types aligned with parent definitions.
- Prefer explicit types over `unknown` when you know the shape.
- Prefer `unknown` over `any` when a boundary truly is unknown.
- Avoid `any` unless there is no practical alternative.
- Do not commit `ts-ignore` except during temporary troubleshooting, and remove
  it before finishing.

Examples:

```ts
type User = {
  name: string,
  role?: string
};

interface Payments {
  amount: number,
  pay(cc: string): Promise<boolean>
}

type LoginCredentials = Pick<User, 'name' | 'role'>;
type EventMap = Record<string, Function>;
```

## Functions And Methods

- Do not add argument types when TypeScript can naturally infer them from a
  default value or surrounding context.
- Do not add return types when the implementation is clear and inference is
  sufficient.
- Add explicit types when they improve API clarity or prevent ambiguity.
- Use narrowing with `typeof`, `Array.isArray`, or custom predicates before
  acting on unknown input.
- Throw real `Error` objects or subclasses with meaningful messages.
- Do not swallow errors silently.

Example:

```ts
function increment(value: number, by = 1) {
  return value + by;
}

function toArray(value: unknown) {
  if (Array.isArray(value)) {
    return value;
  }

  return [ String(value) ];
}
```

## Classes

- Use explicit access modifiers like `public`, `protected`, and `private`.
- Prefix `protected` and `private` methods with `_`.
- Keep internal helpers `protected` when subclasses may need them.
- Mark composition fields `readonly` when they should not be reassigned.
- Prefer getters to expose internal state instead of public mutable fields.
- For public overloads, declare overload signatures first and follow them with
  one implementation.
- Return `this` from chainable APIs when that pattern matches the file.

Example:

```ts
export default class Router {
  public readonly action: ActionRouter;

  public get routes() {
    return this.action.routes;
  }

  protected _resolveEvent(event: string) {}

  public async resolve(event: string): Promise<void>;
  public async resolve(method: Method, path: string): Promise<void>;
  public async resolve(a: string, b?: string) {
    if (typeof b === 'string') {
      return this._resolveRoute(a, b);
    }

    return this._resolveEvent(a);
  }
};
```

## Runtime And Repo Hygiene

- Use strict ESM-safe local imports with `.js` suffixes.
- Prefer native APIs before adding dependencies.
- Only add packages that are clearly needed.
- Remove unused packages when touched safely.
- Do not hardcode secrets or API keys.
- Keep `.env` files out of version control.
- Do not commit `console.log`, `console.error`, or similar debug output.

## References

Load additional reference material only when the task needs it:

- `references/module-design.md` for file splitting, helper extraction, and
  public boundary decisions

## Review Checklist

Before finishing a TypeScript change, verify:

- the file still matches its existing local style where that style is clear
- indentation, quotes, blank lines, and semicolons are consistent
- lines stay compact and readable without unnecessary wrapping
- non-trivial logic blocks have enough `//Comment` guidance to browse as a
  story
- JSDoc stays short and omits `@param` tags by default
- imports are grouped under `//node`, `//modules`, `//client`
- import lines are split to preserve the required type and runtime ordering
- local imports use `.js`
- export sections are ordered correctly when multiple categories are present
- exported items end with semicolons
- object types use commas and interfaces are reserved for class contracts
- `any`, `ts-ignore`, debug logging, and commented-out code are not left behind
