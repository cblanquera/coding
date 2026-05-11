---
name: react-ts-developer
description: Use this skill when writing or reviewing TypeScript ReactJS or TSX components in the cblanquera coding repos. It consolidates the repo's typed React frontend standards into one Codex workflow, including story-like code comments, JSX wrapping, typed props and events, component and hook ordering, aggregate hook patterns, controlled and uncontrolled inputs, import grouping, and file organization for reusable versus local React code.
---

# ReactJS Developer

Use this skill for TypeScript ReactJS implementation, refactors, and reviews in
the
`cblanquera` coding repositories.

This skill is intentionally self-contained. It consolidates the relevant
ReactJS guidance and the repo's TypeScript-oriented coding style so Codex does
not need to bounce between multiple documents during implementation.

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
- Use double quotes only when JSX or HTML syntax requires it.
- End statements with semicolons.
- Put opening braces on the same line.
- Keep exactly one blank line between logical blocks.
- Do not leave multiple consecutive blank lines.
- Avoid trailing commas in import lists or parameter lists.
- Keep lines compact and readable.
- Aim for `<= 80` characters when practical.
- Avoid going past `100` characters unless the file already does so
  consistently.

## Commenting Style

The user prefers comments that read like a story and explain the logic while
browsing. In typed React code this preference is strong enough that you should
bias toward more comments, not fewer, when a component has multiple steps,
derived state, branching UI, or side effects.

- Add short `//` comments before each non-trivial logic block when practical.
- Explain why the next block exists, what state it prepares, and how it moves
  the component flow forward.
- Let the comments read top-to-bottom like a guided walkthrough of the file.
- Prefer several small flow comments over one large paragraph.
- Keep comments factual and local to the code they describe.
- Follow the project inline comment style: `//Comment`, not `// Comment`.
- Use `/** ... */` only for exported or important public APIs.
- Do not add `@param`, `@returns`, or similar tags unless the user explicitly
  asks for them.
- Do not leave commented-out code in committed work.

Example:

```tsx
//Read the incoming value first so the rest of the component can work with
//a stable source of truth before it derives any display state.
const { value, onChange } = props;

//Mirror the outside value locally so the field can support both immediate
//typing feedback and external updates from the parent form.
const [ current, setCurrent ] = useState(value ?? '');

//Keep the local mirror aligned whenever the parent pushes in a new value.
useEffect(() => {
  if (typeof value === 'string') {
    setCurrent(value);
  }
}, [ value ]);
```

## Naming

- Use names that another developer can understand without reading comments.
- Avoid single-letter names and unclear abbreviations.
- Use camelCase for variables, hooks, and functions.
- Use PascalCase for components, classes, and component prop types.
- Name prop types with a clear `Props` suffix.
- Name event handlers after intent, such as `handleSubmit` or `handleChange`.
- Prefix custom hooks with `use`.
- Use booleans like `isReady`, `hasError`, `canSubmit`, or `shouldClose`.
- Use kebab-case for folders and most files.
- If a file exports a default component, PascalCase is acceptable for the file
  name.

## JSX Formatting

### Wrapping Returns

Components must wrap returned JSX in parentheses.

- Wrap single-line JSX returns in parentheses.
- Wrap multi-line JSX returns in parentheses.
- Keep indentation consistent inside the returned JSX block.

Good:

```tsx
const AsideMenu = () => (<aside>...</aside>);

function LeftMenu() {
  return (
    <aside>...</aside>
  );
}
```

Bad:

```tsx
const AsideMenu = () => <aside>...</aside>;

function LeftMenu() {
  return <aside>...</aside>;
}
```

### Prop Signatures

Keep component prop signatures readable.

- Prefer a named prop type for non-trivial props.
- Default to typed props and typed events. This skill is for TSX, not plain
  JSX.
- Inline simple prop types when that is still easy to scan.
- If destructuring becomes tall or noisy, accept `props` first and unpack it in
  the component body.
- Avoid awkward multiline destructuring that hides the prop shape.

Prefer:

```tsx
type LeftMenuProps = {
  items: string[],
  active: string,
  error?: string
};

function LeftMenu(props: LeftMenuProps) {
  //Read props first so the rest of the component can use short local names.
  const { items, active, error } = props;
}
```

## Component Flow

Organize component internals in this order:

1. props
2. hooks
3. derived variables
4. handlers
5. effects
6. render

Do not intermix these sections arbitrarily. This order should make the
component readable from top to bottom like a story: what comes in, what state
exists, what gets derived, what actions can happen, what side effects run, and
what gets rendered.

Example:

```tsx
function LeftMenu(props: LeftMenuProps) {
  //Start with props so the rest of the component can use local values instead
  //of repeatedly reaching back into the original object.
  const { items, error, show, active } = props;

  //Create state next so later logic can derive values and handlers from it.
  const [ opened, setOpened ] = useState(show);
  const [ selected, setSelected ] = useState(active);

  //Derive display values after state exists so the render block stays small.
  const icon = opened ? 'chevron-down' : 'chevron-left';

  //Define handlers before effects so behavior is easy to trace in one pass.
  const toggle = () => setOpened(opened => !opened);

  //Run side effects after the core state and handlers are already defined.
  useEffect(() => {
    if (error) {
      notify('error', error);
    }
  }, [ error ]);

  //Render last so the JSX reads like the final output of all earlier steps.
  return (
    <aside>...</aside>
  );
}
```

## Hooks

### Aggregate Hooks

When a component collects several related hooks, derived values, handlers, and
effects, consider moving that logic into one aggregate custom hook.

- Prefer an aggregate hook when the component body is becoming crowded.
- Keep the aggregate hook in the same file when it only serves one component.
- Move the hook into a shared `hooks` folder only when it is genuinely reused.
- Return only the values the component actually needs.

Example:

```tsx
function useLeftMenu(config: LeftMenuProps) {
  //Read the incoming config first so the hook can build its internal flow from
  //one predictable source.
  const { error, show, active } = config;

  //Create state before any derived values so the rest of the hook has the
  //pieces it needs.
  const [ opened, setOpened ] = useState(show);
  const [ selected, setSelected ] = useState(active);

  //Derive view helpers here so the component can stay mostly declarative.
  const icon = opened ? 'chevron-down' : 'chevron-left';

  //Expose intent-focused handlers instead of raw state setters where possible.
  const toggle = () => setOpened(opened => !opened);

  //Handle side effects inside the hook so the component only consumes results.
  useEffect(() => {
    if (error) {
      notify('error', error);
    }
  }, [ error ]);

  return { opened, selected, icon, toggle };
}

function LeftMenu(props: LeftMenuProps) {
  //Pull the prepared state and handlers from the hook so the component can
  //focus on rendering.
  const { opened, icon, toggle } = useLeftMenu(props);

  return (
    <aside>...</aside>
  );
}
```

### Controlled And Uncontrolled Inputs

For form field components, support both controlled (`value`) and uncontrolled
(`defaultValue`) usage unless there is a strong reason not to.

- Initialize local state from `defaultValue` for uncontrolled usage.
- Mirror external `value` changes into local state for controlled usage.
- Call the incoming `onChange` after updating local state.
- Keep the sync logic explicit so the component behavior is easy to reason
  about.

Example:

```tsx
type InputProps = {
  defaultValue?: string,
  onChange?: (event: ChangeEvent<HTMLInputElement>) => void,
  value?: string
};

function useInput(config: InputProps) {
  //Read the input contract first so the hook can support both control modes.
  const { defaultValue, onChange, value } = config;

  //Start from the default value so uncontrolled usage has local state.
  const [ current, setCurrent ] = useState(defaultValue ?? '');

  //Update the local mirror first, then forward the browser event upstream.
  const change = (event: ChangeEvent<HTMLInputElement>) => {
    setCurrent(event.target.value || '');

    if (onChange) {
      onChange(event);
    }
  };

  //When the parent controls the field, keep the local mirror synchronized.
  useEffect(() => {
    if (typeof value === 'string') {
      setCurrent(value);
    }
  }, [ value ]);

  return { current, change };
}

function Input(props: InputProps) {
  //Use the hook so the component can stay focused on wiring state to markup.
  const { current, change } = useInput(props);

  return (
    <input onChange={change} value={current} />
  );
}
```

## File Layout

When a React file contains enough structure to benefit from clear sections, use
this order:

1. Imports
2. Types
3. Constants
4. Helpers
5. Hooks
6. Components

Use section dividers only when they improve scanning. The exact divider format
is:

```ts
//--------------------------------------------------------------------//
```

Example:

```tsx
//--------------------------------------------------------------------//
// Imports

import { useState } from 'react';

//--------------------------------------------------------------------//
// Types

export type ComponentProps = {};

//--------------------------------------------------------------------//
// Constants

export const DEFAULT_SIZE = 240;

//--------------------------------------------------------------------//
// Helpers

export function componentHelper() {}

//--------------------------------------------------------------------//
// Hooks

export function useComponent() {}

//--------------------------------------------------------------------//
// Components

export function Component() {}

export default Object.assign(Component, { useComponent });
```

### File Structure

- Put reusable shared components in a `components` folder.
- Put reusable shared hooks in a `hooks` folder.
- Keep non-reusable components in the same file as the parent component that
  uses them.
- Keep non-reusable hooks in the same file as the parent component that uses
  them.
- Keep aggregate hooks in the same file as the component when they are local.
- Keep contexts and their providers in the same file.

Use `Object.assign()` to extend functional components with related hooks,
helpers, and constants when that pattern is already used or improves discoverability.

## Imports

Group imports in exactly this order and label each group with section comments:

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
- Use `.js` for local ESM imports when the project expects it.
- Keep the section comments exactly as `//node`, `//modules`, and `//client`.
- Separate type imports from runtime imports even when they come from the same
  module.
- When there is no stronger local convention, sort imports within the same
  subtype by module specifier.

Example:

```tsx
//node
import type { IncomingMessage } from 'node:http';
import { join } from 'node:path';

//modules
import type { ReactNode } from 'react';
import { useEffect, useState } from 'react';

//client
import type { MenuItem } from './types.js';
import { notify } from './notify.js';
```

## Types

- Prefer `type` for props, state shapes, unions, function signatures, and most
  aliases.
- Type React events explicitly when they cross component boundaries or power
  non-trivial handlers.
- Type hook config and return shapes when that improves readability or reuse.
- Use `interface` for class contracts and shapes a class will implement.
- In object types, separate properties with commas, not semicolons.
- Put one space after a type colon and no space before it.
- Put spaces around `|` and `&` in unions and intersections.
- Prefer utility types like `Pick`, `Omit`, `Partial`, and `Required` when they
  keep types aligned with parent definitions.
- Avoid `any` unless there is no practical alternative.
- Prefer `unknown` over `any` at uncertain boundaries.
- Do not leave `ts-ignore` in finished work.

Prefer:

```tsx
type InputProps = {
  defaultValue?: string,
  onChange?: (event: ChangeEvent<HTMLInputElement>) => void,
  value?: string
};
```

Avoid leaving React-facing boundaries untyped in this skill's output unless the
file already follows a stronger local convention.

## Exports

When a module has multiple exports, emit them in this order:

1. Types
2. Constants
3. Functions
4. Classes
5. Default export

- End export statements with semicolons, including exported functions and
  classes.
- Use section dividers only for blocks that actually exist.
- Skip empty sections.
- If there are only one or two exports in a category and no grouping benefit,
  plain exports are fine.

## React Implementation Biases

- Prefer small focused components over one large mixed-responsibility file.
- Prefer derived values over duplicated state.
- Prefer lifting state only when multiple consumers truly need the same source
  of truth.
- Prefer explicit handlers with intent-revealing names over inline anonymous
  logic when the behavior is reused or non-trivial.
- Keep render blocks declarative and push preparation logic upward into hooks,
  helpers, or derived variables.
- Default to `.tsx` component patterns with explicit prop contracts instead of
  loose JavaScript-style component signatures.
- Prefer native React and browser APIs before adding dependencies.

## Review Checklist

When writing or reviewing React code, check for these issues:

- JSX returns are wrapped in parentheses.
- Props and types are easy to scan.
- Component internals follow the expected story order.
- Complex hook logic is aggregated when that improves readability.
- Controlled and uncontrolled field behavior is implemented correctly.
- Reusable pieces are separated from local-only pieces appropriately.
- Imports and exports follow repo conventions.
- Comments explain the flow of the code without becoming noise.
