# CSS Style Guide Ruleset

The purpose of this style guide is to improve code quality by documenting a set of expected rules that can consistently apply across all projects.

## 1. Spacing

To simplify styling to be concise across all projects, the following applies.

- **MUST** place selectors separated by commas on a new line.
- **MUST** place each property on a new line, even if there is only one property.

## 2. Stylesheet Structure

Structure **SHOULD** be expressed by comment docing the layout. The following style categories are use to organized your styles.

 - Global
 - Components
 - Partials
 - Pages

It is recommended to add category tags in your CSS like the following.

```css
✅ Good
/* Global - Tags
------------------------------*/
/* Global - Classes
------------------------------*/
/* Global - Bootstrap
------------------------------*/
/* Component - [NAME]
------------------------------*/
/* Component - [NAME]
------------------------------*/
/* Partial - [NAME]
------------------------------*/
/* Partial - [NAME]
------------------------------*/
/* Page - [NAME]
------------------------------*/
/* Page - [NAME]
------------------------------*/
```

- **MUST** organize styles into the following categories: Global, Components, Partials, Pages.
- **SHOULD** add category tags as comments in CSS to indicate structure.

### 2.1 Global

Global styles are applied globally defined by first level selectors.

> First Level Selector Examples

```css
✅ Good
body {
  height: 100%;
}
.wrapper {
  padding: 10px;
}
.text-success {
  color: #00FF00;
}
```

> Second Level Selector Examples

```css
✅ Good
body p {
  height: 100%;
}
.wrapper .item {
  padding: 10px;
}
.text-success span {
  color: #00FF00;
}
```

- **MUST** use only first-level selectors in the Global section.
- **MUST NOT** use second-level (or deeper) selectors in the Global section, except when overriding a class from a library.

### 2.2 Component

Components are commonly used UI elements. Some example of components are **pagination**, **tag field**, **image field**, **date field** etc. When styling components, the first level selector should reference the top level component class name.

```css
✅ Good
.pagination {
  padding: 0;
}
.pagination .pagination-item {
  margin: 0;
}

❌ Bad
.pagination-item {
  margin: 0;
}
```

- **MUST** use the top-level component class name as the first-level selector for components.
- **MUST NOT** style component sub-elements without referencing the top-level component class.

### 2.3 Partials

Partials are HTML blocks usually used with Handlebars in loops and normally is a group of random HTML and UI components. When styling partials, the first level selector should reference the top level partial class name. This implies that partials should have a singular top level parent.

```css
✅ Good
.post-item {
  padding: 0;
}
.post-item .post-title {
  margin: 0;
}

❌ Bad
.post-title {
  margin: 0;
}
```

- **MUST** use the top-level partial class name as the first-level selector for partials.
- **MUST** ensure partials have a singular top-level parent.
- **MUST NOT** style partial sub-elements without referencing the top-level partial class.

### 2.4 Pages

Page sections describes styles that should only be applied per page. By practice we place the page class in the `<html>` tag. Page class names should start with `page-` like `page-about-us`. When styling partials, the first level selector should reference the top level page class name.

```css
✅ Good
.post-about-us {
  padding: 0;
}
.post-about-us .about-us-detail {
  margin: 0;
}

❌ Bad
.about-us-detail {
  margin: 0;
}
```

- **MUST** use page class names that start with `page-` for page-specific styles.
- **MUST** use the top-level page class name as the first-level selector for page styles.

## 3. Selectors

Selectors should be separated by one space only. Selectors should be unique per stylesheet.

```css
✅ Good
.post-item .post-title a {
  color: #FFFFFF;
}

✅ Good
.post-item .post-title h3 a {
  padding: 10px;
}

❌ Bad
.post-item .post-title a {
  color: #FFFFFF;
}
.post-item .post-title a {
  padding: 10px;
}
```

- **MUST** separate selectors by one space only.
- **MUST** ensure selectors are unique per stylesheet.
- **SHOULD** minimize the number of selectors to make overriding easier.
- **MUST NOT** overcomplicate selectors (e.g., avoid unnecessary tag/class combinations).
- **SHOULD** prefer class names over tag names in selectors.
- **MUST NOT** use the same class name in different sibling HTML tags.

A standard practice is to minimize the amount of selectors needed to make it easier to override. The only exception to this rule is when you are attempting to override an existing style without using the `!important` value.

```css
❌ Bad
body .head nav .nav-header span img.brand-logo {
  width: 50px;
}

❌ Bad
.post-item .post-title ul li a {
  padding: 10px;
}
```

The first selector in the example above `body .head nav .nav-header span img.brand-logo` makes it difficult to override this style because we started with the body element and has a total of 6 selectors. In order to properly override this, we need to match the number of selectors or increase the selector count at least by one.

The second selector above `.post-item .post-title ul li a` is also incorrect because having an `<li>` tag implies that there is a `<ul>` parent already.

This implies another practice which is not to over complicate each selector. The first way to do this is prefer to use class names over tag names. This is because tag names are more likely to change than class names and you should not select a tag and a class name in one selector as in `strong.label`.

To make that rule more viable it is considered bad practice for the same class name to be used in different sibling HTML tags.

```css
✅ Good
.post-item .post-title .label {
  padding: 10px;
}
.post-item .post-title.active .label {
  padding: 10px;
}

❌ Bad
.post-item .post-title.active strong.label {
  padding: 10px;
}
.post-item .post-title strong.label {
  padding: 10px;
}
```

### 3.1 Direct Child

**MUST** separate the direct child selector `>` by spaces.

## 4. Properties

**MUST** organize properties in alphabetical order within each rule.

### 4.1 Browser Specific

**MUST** place browser-specific properties (e.g., `-webkit-`) at the top of the property list, then order alphabetically.

## 5. Values

The following sections covers how to style various CSS values.

### 5.1 Decimals

**MUST** express zero-point decimals with a leading zero (e.g., `0.45`).

### 5.2 Colors

When expressing colors using hexadecimal, you should express it using capital letters and in 6 characters. You should use the `rgba` function to explain colors with alpha-transparency and you should not express colors by their word name.

- **MUST** use 6-character uppercase hexadecimal for colors.
- **MUST** use `rgba` for colors with alpha transparency.
- **MUST NOT** use color word names (e.g., `white`).

### 5.3 Important

You should try to avoid the use of `!important` in most circumstances.

- **SHOULD** avoid using `!important` except when overriding a style that also uses `!important`.
- **SHOULD** override styles by selector count or file order instead of using `!important`.

## 6. Responsive

Generally, responsive styles should be placed at the bottom of each Stylesheet Structure.

```css
✅ Good
@media(max-width:767px) {
  .notify {
    left: 10px;
    width: auto;
  }
}

/* Component - Pagination
------------------------------*/

❌ Bad
/* Component - Notify
------------------------------*/
.notify {
  left: 10px;
  width: auto;
}

@media(max-width:767px) {
  .notify {
    left: 10px;
    width: auto;
  }
}

.notify a {
  width: auto;
}

❌ Bad
/* Component - Notify
------------------------------*/
@media(max-width:767px) {
  .notify {
    left: 10px;
    width: auto;
  }
}

.notify {
  left: 10px;
  width: auto;
}
```

- **SHOULD** place responsive styles at the bottom of each stylesheet structure section.
- **SHOULD** use snap responsive design (fixed breakpoints) instead of fluid responsive (percent-based) design.
- **MAY** use mobile-first or desktop-first approaches, but desktop-first is preferred for easier element removal.
