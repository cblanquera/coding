# ReactJS Style Guide

Comprehensive guidelines for writing consistent and maintainable ReactJS code. These standards promote readability, efficient code organization, and best practices for component development. By following these rules, developers can create scalable React applications that are easy to understand and collaborate on.

## 1. Wrapping

Always wrap components inside parenthesis.

```js
//✅ Good
const AsideMenu = () => (<aside>...</aside>); 
//❌ Bad
const AsideMenu = () => <aside>...</aside>; 
//❌ Bad
const AsideMenu = () => <aside>...</aside>

//✅ Good
function LeftMenu() {
  return (<div>...</div>);
}
//✅ Good
function LeftMenu() {
  return (
    <div>...</div>
  );
}
//❌ Bad
function LeftMenu() {
  return <div>...</div>
}
```

## 2. Spacing

When defining component prop arguments, it's important that it's easily readable. For complex props consider separating the type into a separate type definition. Consider the following.

```js
//✅ Good
function LeftMenu(props: LeftMenuProps) {
  //props
  const { items, active, error } = props;
}
//✅ Okay
function LeftMenu(props: { items: string[] }) {}
//✅ Okay
function LeftMenu({ items }: { items: string[] }) {}
//✅ Okay
function LeftMenu({ items, active, error }: {
  items: string[],
  active: string,
  error?: string
}) {
  //...
}
//❌ Bad
function LeftMenu({
  items,
  active,
  error
}: {
  items: string[],
  active: string,
  error?: string
}) {
  //...
}
```

## 3. Code Organization Outline

Organize your components in the following order.

 1. props
 2. hooks
 3. variables
 4. handlers
 5. effects

```ts
function LeftMenu(props: LeftMenuProps) {
  //1. props
  const { items, error, show, active } = props;
  //2. hooks
  const [ opened, open ] = useState(show);
  const [ selected, select ] = useState(active);
  //3. variables
  const icon = opened ? 'chevron-down': 'chevron-left';
  //4. handlers
  const toggle = () => open(opened => !opened);
  //5. effects
  useEffect(() => {
    error && notify('error', error);
  }, []);
  //6. render
  return (
    <aside>...</aside>
  );
}
```

## 4. Aggregate Hooks

Instead of setting up multiple hooks in a component, consider making a hook wrapper.

```js
function useLeftMenu(config: LeftMenuProps) {
  //1. config
  const { items, error, show, active } = config;
  //2. hooks
  const [ opened, open ] = useState(show);
  const [ selected, select ] = useState(active);
  //3. variables
  const icon = opened ? 'chevron-down': 'chevron-left';
  //4. handlers
  const toggle = () => open(opened => !opened);
  //5. effects
  useEffect(() => {
    error && notify('error', error);
  }, []);
  //6. Return usable variables
  return { opened, icon, toggle };
}

function LeftMenu(props: LeftMenuProps) {
  //1. hooks
  const { opened, icon, toggle } = useLeftMenu(props);
  //2. render
  return (
    <aside>...</aside>
  );
}
```

## 5. Controlled and Uncontrolled Values

When creating form field comonents, consider controlled (`value`) and uncontrolled (`defaultValue`) values. The following code shows how to properly implement both at the same time.

```tsx
type InputProps = {
  defaultValue?: string,
  onChange?: (e: ChangeEvent<HTMLInputElement>) => void
  value?: string
};

function useInput(config: InputProps) {
  //config
  const { defaultValue, onChange, value } = config;
  //hooks
  // set defaultValue (uncontrolled)
  const [ current, setCurrent ] = useState(defaultValue);
  //handlers
  const change = (e: ChangeEvent<HTMLInputElement>) => {
    setCurrent(e.target.value || '');
    onChange && onChange(e);
  };
  //effects
  // whenever value (controlled) changes from the outside,
  // update the current value inside
  useEffect(() => {
    if (typeof value === 'string') {
      setCurrent(value);
    }
  }, [ value ]);
  return { current, change };
}

function Input(props: InputProps) {
  const { current, change } = useInput(props);
  return (
    <input onChange={change} value={current} />
  );
};
```

> Very rarely would you need to deviate from this pattern.

## 6. Component File Outline

Add clear dividers in a component file for readability. Dividers could include the following order.

 1. Imports
 2. Types
 3. Constants
 4. Helpers
 5. Hooks
 6. Components

By default you should export all types, variables and functions. An example file could look like the following snippet.

```js
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

export function componentHelper() {};

//--------------------------------------------------------------------//
// Hooks

export function useComponent() {};

//--------------------------------------------------------------------//
// Components

export function Component() {};

export default Object.assign(Component, { useComponent });
```

Use `Object.assign()` to extend functional components with their hooks, helpers and variables.

## 7. File Structure Options

The following points covers acceptable configurations when organizing React component files.

 - Separate general reusable components into their own file in a `components` folder.
 - Separate general reusable hooks into their own file in a `hooks` folder.
 - Components that are not reuable should stay in the same file as the component that uses it.
 - Hooks that are not reusable should stay in the same file as the component that uses it.
 - Keep aggregate hooks in the same file as the component that uses it.
 - Keep contexts and their providers in the same file.