# HTML Style Guide

The purpose of this style guide is to improve code quality by documenting a set of expected rules that can consistently apply across all projects. The main benefits are the following.

## 1. Typography

Do not use all uppercase text.

- Text **MUST NOT** be all uppercase.
- Titles in headers **MUST** use title case (not all lowercase or all uppercase).

## 2. Spacing and Overflows

Generally, **do not exceed 80 characters per line**. Most IDEs already made visible the *overflow ruler*. Inline text such as `<p>Inline Text</p>` is acceptable so long as it does not exceed the *overflow ruler*.

- Lines **SHOULD NOT** exceed 80 characters, except for inline text that fits within the overflow line.
- If text cannot fit inline, it **MUST** be brought to the next line.
- Overflowed text **MUST NOT** start with its parent tag on the same line.
- When opening a new tag, its content **SHOULD** be indented with 4 spaces.
- If content fits within 80 characters, it **MAY** be kept inline.
- When tags have many attributes, each attribute **SHOULD** be on its own line, indented, and the closing tag **MUST** be on a new line.
- Attributes in a tag **MUST** be in alphabetical order.

**Long Attributes**

When dealing with tags having a lot of attributes, you should drop and tab each attribute. The closing tag should be separated in a new line.

```html
✅ Good
<a
  class="post-like"
  data-do="post-like"
  data-id="123"
  data-on="click"
  href="javascript:void(0)"
  title="This will send your information to the Job Seeker"
>
  Click Me
</a>

✅ Good
<img
  alt="Logo"
  src="logo.png"
  width="200"
/>

❌ Bad
<a class="post-like" data-do="post-like" data-id="123" data-on="click" href="javascript:void(0)" title="This will send your information to the Job Seeker">
  Click Me
</a>

❌ Bad
<a class="post-like"
  data-do="post-like"
  data-id="123"
  data-on="click"
  href="javascript:void(0)"
  title="This will send your information to the Job Seeker">
  Click Me</a>

❌ Bad
<img src="logo.png"
  alt="Logo"
  width="200" />
```

## 3. Tags

When laying out a page, or laying out a block take advantage of `<header><aside><section><footer>` where applies.

- Layout tags like `<header>`, `<aside>`, `<section>`, and `<footer>` **SHOULD** be used where appropriate.
- `<article>` tags **SHOULD** be used to explain content sections (posts, products, events, etc.).

### 3.1 Block and Inline

Under no circumstance should a [block tag](https://developer.mozilla.org/en-US/docs/Web/HTML/Block-level_elements) be found in an [inline tag](https://developer.mozilla.org/en-US/docs/Web/HTML/Inline_elements).

- Block tags **MUST NOT** be placed inside inline tags.
- Paragraph tags `<p>` **MUST NOT** contain block tags.

```html
✅ Good
<h3><a href="#">A good example</a></h3>
<p><span>A good example</span></p>

❌ Bad
<a href="#"><h3>A bad example</h3></a>
<span><p>A bad example</p></span>
```

Additionally, paragraph tags should not have block tags.

```html
❌ Bad
<p><h3>A bad example</h3></p>
<p><div>A bad example</div></p>
```

### 3.2 Self Closing

[Self closing](http://xahlee.info/js/html5_non-closing_tag.html) tags should have a space followed by a forward slash.

```html
✅ Good
<hr />
<br />
<img alt="" src="" />
<input />

❌ Bad
<hr>
<br>
<img alt="" src="">
<input>
```

Self-closing tags **MUST** have a forward slash and must have a space before the slash (e.g., `<br />`).

### 3.3 Headers

Headers are used to help outline a page; to help figure out the important parts of a page there by help making it possible to summarize its content.

- There **MUST NOT** be more than one `<h1>` per page.
- Header levels **MUST NOT** be skipped (e.g., do not use `<h3>` without a preceding `<h2>`).
- Header text **MUST** be less than 140 characters.
- Header text **MUST** use title case.

### 3.4 Links

All link tags should have the `title=""` attribute. Titles should not exceed 140 characters.

- All `<a>` tags **MUST** have a `title` attribute.
- Link titles **MUST NOT** exceed 140 characters.

### 3.5 Images

All image tags should have the `alt=""` attribute. Alts should not exceed 140 characters.

- All `<img>` tags **MUST** have an `alt` attribute.
- Alt text **MUST NOT** exceed 140 characters.

### 3.6 Line Breaks

Break Tags `<br />` are only allowed if it is between text.

- `<br />` tags **MAY** be used only between text, NOT for spacing blocks.
- `<hr />` tags **MAY** be used to define thematic changes, NOT for spacing blocks.
- **MUST NOT** use `<br />` to vertical space blocks. Use CSS instead.
- **MAY** use `<br />` to separate text or inline tags.

### 3.7 Scripts and Styles

All stylesheet tags `<link>` should have an `href`, `rel` and `type` attribute. Script tags `<script>` should have at least a `type` attribute.

- `<link>` tags **MUST** have `href`, `rel`, and `type` attributes.
- `<script>` tags **MUST** have at least a `type` attribute.

### 3.8 HTML 4

Usage of `<b>` to bold, `<i>` for italics, `<s>` to strike out are prohibited. Please find their HTML5 and/or CSS3 equivalents. Do not use `<font>` under no circumstances.

- `<b>`, `<s>`, and `<font>` tags **MUST NOT** be used. Use HTML5/CSS3 equivalents.
- `<i>` **MAY** be used to represent icons.

## 4. Attributes

Attribute values must be within double quotes at all times.

- Attribute values **MUST** always use double quotes.
- Attributes **MUST** be in alphabetical order.

### 4.1 IDs

IDs should have unique values per page. IDs should only be used when dealing directly with javascript. You should not add styles to IDs; use classes instead. ID values should use all lowercase and dashes to separate words.

- IDs **MUST** be unique per page.
- IDs **MUST** only be used for JavaScript, NOT for styling.
- ID values **MUST** use all lowercase and dashes.

### 4.2 Classes

You should not use classes to indicate a particular style change. The following describes what classes not to use.

- Classes **SHOULD** have meaningful, unique names, and be minimized.
- Class names **SHOULD** use all lowercase, and dashes.
- Classes **SHOULD** be in alphabetical order.

## 5. Comments

Use Comments to describe sections, blocks and states. This is helpful when troubleshooting code and automated acceptance testing. Comments should wrap at least each major section in the following format example.

```html
✅ Good
<!-- START: Post Image -->
<div class="post-image">
  <img alt="This is a post image" height="60" src="avatar.png" />
</div>
<!-- END: Post Image -->

✅ Good
<!-- START: I am logged in -->
<li>
  <a href="/logout">Log Out</a>
</li>
<!-- END: I am logged in -->

❌ Bad
<!-- Post Image -->
<div class="post-image">
  <img alt="This is a post image" height="60" src="avatar.png" />
</div>

❌ Bad
<!-- I am logged in -->
<li>
  <a href="/logout">Log Out</a>
</li>
```

- Comments **SHOULD** be used to describe sections, blocks, and states.
- Major sections **SHOULD** be wrapped with `<!-- START: ... -->` and `<!-- END: ... -->` comments.

## 6. Inline Scripts and Styles

Inline styles are only permitted when dealing directly with javascript or with email HTML. Otherwise inline styles should be placed into a separate file.

- Inline styles **MAY** be used only for JavaScript or email HTML; otherwise, styles **MUST** be in a separate file.
- Inline scripts **MAY** be used only if required by a third-party or to activate a script in a separate file; otherwise, scripts **MUST** be in a separate file.
- Templates in `<script type="text/x-template">` **MAY** be used.
