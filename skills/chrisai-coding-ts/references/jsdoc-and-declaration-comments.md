# TypeScript JSDoc And Declaration Comments

Use this reference during the final style pass when the code behavior already
works and the remaining job is to document intent clearly.

## JSDoc Coverage

- Every function gets `/** ... */`.
- Every class method gets `/** ... */`.
- Exported functions and exported classes get `/** ... */`.
- Keep JSDoc to a short description by default.
- Do not add `@param`, `@returns`, or similar tags unless the user explicitly
  asks for them.

```ts
/**
 * Build the normalized route name from the incoming event.
 */
function getRouteName(event: string) {
  return event.trim().toLowerCase();
}
```

## Declaration Comments

- Add `//` comments above every class property to explain what it is, where it
  is used, and how it is expected to change.
- Add `//` comments above exported types, constants, properties, and other
  exported declarations to explain what they are, where they are used, and how
  they are used.

```ts
export default class Router {
  //The route table is filled during registration and then read by resolve()
  // and by plugins that inspect the active routes after boot.
  public readonly routes: RouteMap = {};

  //The request handler is reused by resolve() so route execution always flows
  // through the same boundary and plugins can decorate one shared handler.
  public readonly handler: RouteHandler;
}

//The public route table shared by registration code, resolve(), and plugin
// hooks that inspect which route patterns were loaded.
export type RouteMap = Record<string, RouteDefinition>;

//The shared status map exported so route handlers and error formatters can
// compare the same owned status values without repeating magic numbers.
export const ROUTE_STATUS = {
  ok: 200,
  notFound: 404
};
```
