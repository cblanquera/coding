# Coding Standards

My Coding Standards. Before contributing to anyone's code, be sure to study how the existing project code 
is expressed. It's important that all code in a project closely matches each others.

> ❌ Do not use your own standards irrespective of the existing project's code. Even if they have not
> explicitly set a standard.

## Char Length

Code should be written like a book. A book has pages and each line of each page has a common max length.
Imagine a child's eye moving from left to right when reading a book. As that child reads while growing 
up, their eyes move a lot less. Eventually a person moves from letter to letter, to word by word, to line 
by line, and some can even do page by page *(speed reading)*. This is because as a person reads more and 
more they develop their sight peripherals, but there is a limit to how far peripherals can reach *(less 
than 180 degrees)*. Around when an individual's sight peripherals reach their limit is when the eyes need 
to move. Eyes moving constantly without rest can cause eye stress. Unlike a book, there is no max length 
a line of code could be and contributes to eye stress for everyone reading code not having a standard.

> Every line of code should not exceed **80 characters**.

If you are using VSCode 
 1. Go to File > Preferences > Settings.
 2. Search for "rulers"
 3. Click "Edit in settings.json"
 4. Add the following to `settings.json`

```js
"editor.rulers": [ 72, 80, 100, 120 ],
```

To keep code readable and prevent horizontal scrolling, follow a consistent line breaking (drop down) style.

```js
//✅ Good
import type { ErrorMap } from '../types.js';

//❌ Bad
import type { 
  ErrorMap 
} from '../types.js';

//✅ Good
import type { 
  ErrorMap,
  SchemaColumnInfo, 
  SchemaSerialOptions 
} from '../types.js';

//❌ Bad
import type { ErrorMap, SchemaColumnInfo, SchemaSerialOptions } from '../types.js';

//✅ Good
function fooBar(zoo: number) {
  //...
}

//❌ Bad 
function fooBar(
  zoo: number
) {
  //...
}

//✅ Good 
function fooBar(
  zoo: number, 
  baz: string, 
  hash: Record<string, string>, 
  list?: string[]
) {
  //...
}

//❌ Bad
function fooBar(zoo: number, baz: string, hash: Record<string, string>, list?: string[]) {
  //...
}

//✅ Good
const fooBar = [ 'foo' ];
//❌ Bad
const fooBar = [
  'foo'
];

//✅ Good
const fooBar = [
  'foo',
  'bar',
  'zoo',
  'baz',
  'foobar',
  'zoobaz',
  'foobarzoo'
];
//❌ Bad
const fooBar = [ 'foo', 'bar', 'zoo', 'baz', 'foobar', 'zoobaz', 'foobarzoo'];

//✅ Good
const fooBar = { foo: 'bar' };
//❌ Bad
const fooBar = { 
  foo: 'bar' 
};

//✅ Good
const fooBar = { 
  foo: 'bar',
  bar: 'bar',
  zoo: 'zoo',
  baz: 'baz',
  foobar: 'foobar',
  zoobaz: 'zoobaz',
  foobarzoo: 'foobarzoo'
};
//❌ Bad
const fooBar = { foo: 'bar', bar: 'bar', zoo: 'zoo', baz: 'baz', foobar: 'foobar', zoobaz: 'zoobaz', foobarzoo: 'foobarzoo' };
```

## Indentation

In all circumstances use **2 spaces** for indents.

 - ❌ Do not use 4 spaces for indents.
 - ❌ Do not use *[tab]* for indents.

## Quotes

By default, prefer single quotes (**'**) over double quotes (").

 - Use template quotes (`) for templating use or for quotes with multiple lines.
 - Use double quotes for HTML and React attributes

| Context             | Preferred               |
| ------------------- | ----------------------- |
| JavaScript strings  | `'single quotes'`       |
| Multiline/templates | `` `template string` `` |
| HTML/JSX attributes | `"double quotes"`       |

## Semicolons

In general end statements with a semicolon.

```js
//✅ Good
const name = 'John';
//❌ Bad
const name = 'John'

//✅ Good
const { name } = props;
//❌ Bad
const { name } = props

//✅ Good
fooBar();
//❌ Bad
fooBar()
```

Conditional blocks should not end with semicolons.

```js
//✅ Good
if (true) {}
//❌ Bad
if (true) {};
```

`while` and `for` iteration blocks should not end with semicolons. `do while` blocks should end with semicolon.

```js
//✅ Good
while (true) {}
//❌ Bad
while (true) {};

//✅ Good
do {} while (true);
//❌ Bad
do {} while (true)

//✅ Good
for (;;) {}
//❌ Bad
for (;;) {};
```

Function declarations should not have semicolons.

```js
//✅ Good
function fooBar() {}
//❌ Bad
function fooBar() {};
```

All exported variables should have semicolons.

```js
//✅ Good
export const fooBar = 'foobar';
//❌ Bad
export const fooBar = 'foobar'

//✅ Good
export function fooBar() {};
//❌ Bad
export function fooBar() {}

//✅ Good
export default function fooBar() {};
//❌ Bad
export default function fooBar() {}
```

## Comments

Only use `/*...*/` for JSDoc-style comments. In Typescript there is no need to add `@param` to the JSDoc.

```js
//✅ Good
/**
 * Does the foobar
 */
function fooBar(foo: string) {}

//❌ Bad
/**
 * Does the foobar
 *
 * @param string foo
 */
function fooBar(foo: string) {}
```

Only use inline comments `//` inside of functions and blocks. For single line inline comments, do not add a space after `//`.

```js
//This is a good comment
// This is a bad comment

//This is a long comment that describes
// complicated logic. You can use spaces
// so they know it's connected as one
// comment block

//These are directions
// 1. Step 1
// 2. Step 2

//These are flows
// - if good then send
// - otherwise dont send
```

## Spaces Between Data Block

A data block are non scalar data structure like arrays and objects. Data blocks should have a space in between the opening and closing where values are present. Consider the following examples.

```js
//✅ Good
const fooBar = [];
//❌ Bad
const fooBar = [ ];

//✅ Good
const fooBar = {};
//❌ Bad
const fooBar = { };

//✅ Good
const fooBar = [ 'foo', 'bar' ];
//❌ Bad
const fooBar = ['foo','bar'];

//✅ Good
const fooBar = { foo: 'foo', bar: 'bar' };
//❌ Bad
const fooBar = {foo:'foo',bar:'bar'};

//✅ Good
const fooBar = { foo, bar };
//❌ Bad
const fooBar = {foo,bar};
```

## Naming Conventions

When deciding on a name please consider the following.

 - Other developers need to be able to clearly understand what the variable, function, class, etc. is without looking at the JavaDoc or comment about it.
 - Other foreign developers use translation to figure out what a variable, function, class is.

With that said, avoid single letter or abbreviations for names. 

```js
//❌ Bad
const x = 'foobar';
//❌ Bad
const lat = 90.123;
//❌ Bad
const cntry = 'United States';
//❌ Bad
function getCLR() {}
```

**Variables**

 - Use camelCase
 - Use nouns for values: `user`, `orderList`
 - Variables representing booleans, can use `is`, `has`, `can`, `should`, `valid`
 - Variables representing functions, follow function naming
 - Variables representing class definitions, follow class naming

**Functions**

 - Use camelCase
 - Use verbs or verb phrasing (verb followed by noun): `get()`, `getUser()`, `submitForm()`, `resetTimer()`
 - For React components, follow class naming

**Classes & Components**

 - Use PascalCase
 - Use nouns for values: `User`, `EventEmitter`, `TaskQueue`

**Folders & Files**

In general you should use kebab-case to name your folders and files. Files that `export default` a class or component should use PascalCase.

| Item            | Naming     | Example                 |
| --------------- | ---------- | ----------------------- |
| Files (JS/TS)   | kebab-case | `user-service.ts`       |
| Classes         | PascalCase | `User.ts`               |
| Components      | PascalCase | `UserCard.tsx`          |
| Folders         | kebab-case | `user-profile/`         |
| Class Index     | PascalCase | `User/index.ts`         |
| Component Index | PascalCase | `UserCard/index.tsx`    |

## Imports

Organize imports by node modules like `node:path`, `node:fs`, packages (in `node_modules`) and local imports as well as type imports and actual imports. Consider the following.

```js
//node
import type { IncomingMessage } from 'node:http';
import { resolve } from 'node:path';
import fs from 'node:fs';
//modules
import type { Request } from '@whatwg/fetch';
import { Mailer, send } from 'simple-mailer'; 
import mustache from 'mustache';
//local
import type { User, Auth } from '../types.js';
import { getUser } from './helpers';
import Session from './Session.js';
```

When importing native node modules, prefix the name with `node:`.

```js
//✅ Good
import fs from 'node:fs';
//❌ Bad
import fs from 'fs';
```

## Components

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

Organize your components in the following order.

```js
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

## Git Commits

When committing your code please consider the following.

- Use clear, concise commit messages. Longer messages are encouraged.
- Start your message with a verb: `Added`, `Created`, `Removed`, etc.
- Be specific about the file types you are committing: `pages`, `views`, `model`, etc.
- If the commit is not working yet add `(wip)` tag which means work in **progress**.
- Add the Github Issue number/s (ie `#123`) related to this commit.
- Add how long you spent on this commit using short hand time format: `5m` meaning 5 minutes, `42h` meaning 42 hours. Do not use days, weeks, months. 
- Avoid committing all your unsaved changes blindly. Manually design your commits per issue or logical grouping.

```bash
//❌ Bad
updated code
//❌ Bad
login form
//❌ Bad
did this and that and that and this..
✅ Good
"Created login form view components (wip) #123 4h"
```

## Dependencies

- Only install packages you truly need.
- Actively remove packages you are no longer using.
- Prefer native APIs and utilities before reaching for libraries.
- Document why a non-obvious package is used.

## Environment Variables

 - Do not hardcode secrets or API keys.
 - Keep .env files out of git.

## Final Notes

 - Syntax and formatting mistakes are generally forgivable as long as they are methodical, logical and consistent.
 - Consistency beats preference. When in doubt, match existing patterns.
 - Don’t be afraid to ask questions or propose improvements.
 - Keep your pull requests small and focused.
