#  CSS Style Guide

The purpose of this style guide is to improve code quality by documenting a set of expected rules that can consistently apply across all projects. The main benefits are the following.

 - Easier for new developers to on board on a project
 - Easier to troubleshoot code across different projects
 - Easier to contribute additional code
 - Easier to identify strategy and logic that can be applied to different projects

## 1. Spacing

To simplify styling to be concise across all projects, the following should apply.

 - Selectors separated by commas should be on a new line.
 - Each property should be on a new line. *(Even if it is one property)*

```css
✅ Good
html,
body {
  font-size: 15px;
  height: 100%;
  margin: 0;
}

✅ Good
.post-title {
  font-size: 15px;
}

❌ Bad
html, body { font-size: 15px; height: 100%; margin: 0; }

❌ Bad
.post-title { font-size: 15px; }
```

## 2. Stylesheet Structure

Structure should be expressed by comment docing the layout. The following style categories are use to organized your styles.

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

### 2.1. Global

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

You should not have second level (or more) selectors in global sections. Exceptions to this rule is overriding a class from a library.

### 2.2. Component

Components are commonly used UI elements. Some example of components are
**pagination**, **tag field**, **image field**, **date field** etc.

When styling components, the first level selector should reference the top level component class name.

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

### 2.3. Partials

Partials are HTML blocks usually used with Handlebars in loops and normally is a group of random HTML and UI components.

When styling partials, the first level selector should reference the top level partial class name. This implies that partials should have a singular top level parent.

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


### 2.4. Pages

Page sections describes styles that should only be applied per page. By practice we place the page class in the `<html>` tag.

Page class names should start with `page-` like `page-about-us`. When styling partials, the first level selector should reference the top level page class name.

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

## 3.1 Direct Child

Direct child separator `>` should be separated by spaces.

```css
✅ Good
.post-item > .post-title > .label {
  padding: 10px;
}

❌ Bad
.post-item>.post-title>.label {
  padding: 10px;
}
```

## 4. Properties

Properties should be organized in alphabetical order.

```css
✅ Good
body {
  font-size: 15px;
  height: 100%;
  margin: 0;
}

❌ Bad
body {
  margin: 0;
  height: 100%;
  font-size: 15px;
}
```

## 4.1. Browser Specific

Browser specific properties denoted by `-` as in `-webkit-user-select` should be placed on the top order of selectors and then alphabetical.

```css
✅ Good
.mobile-pointer {
  -moz-user-select: none;
  -webkit-pointer-events: none;
  -webkit-user-select: none;
  pointer-events: none;
  user-select: none;
}

❌ Bad
.mobile-pointer {
  -webkit-pointer-events: none;
  pointer-events: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  user-select: none;
}
```


### 5. Values

The following sections covers how to style various CSS values.

### 5.1 Decimals

When using zero-point decimals, you should express the zero `0` before the
decimal.

```css
✅ Good
opacity: 0.45

❌ Bad
opacity: .45
```


### 5.2. Colors

When expressing colors using hexadecimal, you should express it using capital letters and in 6 characters. You should use the `rgba` function to explain colors with alpha-transparency and you should not express colors by their word name.

```css
✅ Good
#000000
#A14C24
rgba(40, 40, 40, 0.45)

❌ Bad
#000
#a14c24
white
```

### 5.3. Important

You should try to avoid the use of `!important` in most circumstances. Styles can be overriden in two other ways.

 1. Simply use the same selector count later in the file or in a file that is declared after the original file.
 2. Add an extra selector count like from `.post-detail` to `.post .post-detail`.

The only acceptable use of `!important` is if you are overriding a style that is also using the `!important` value.


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

Instead of fluid responsive (which measures HTML by percent(%)), it is much easier to design snap responsive (when the browser window resizes to 960ox, 767px, 420px or 360px, the webpage will snap it in place respective to those widths). 

> Snap Responsive Example
```css
.wrapper {
  width: 900px;
}

@media(max-width: 767px) {
  .wrapper {
    width: 600px;
  }
}

@media(max-width: 420px) {
  .wrapper {
    width: 300px;
  }
}
```

This order of responsive does imply that we do not do mobile first. The main reason why desktop first is preferred is because it is much easier to remove elements than it is to unhide elements. Though, both ways provide the same results, mobile responsive is a forward compatible design concept while the latter is a backwards compatible design concept.

> Mobile Responsive
```css
.wrapper {
  width: 300px;
}

@media(min-width: 300px) {
  .wrapper {
    width: 600px;
  }
}

@media(min-width: 600px) {
  .wrapper {
    width: 900px;
  }
}
```