
# HTML Style Guide

The purpose of this style guide is to improve code quality by documenting a set of expected rules that can consistently apply across all projects. The main benefits are the following.

 - Easier for new developers to on board on a project
 - Easier to troubleshoot code across different projects
 - Easier to contribute additional code
 - Easier to adjust for SEO across all projects
 - Easier to identify strategy and logic that can be applied to different projects

## 1. Typography

Do not use all uppercase text.

```
✅ Good
Cum sociis natoque

✅ Good
cum sociis natoque

✅ Good
Cum Sociis Natoque

❌ Bad
CUM SOCIIS NATOQUE
```

## 2. Spacing and Overflows

Generally, **do not exceed 80 characters per line**. Most IDEs already made visible the *overflow line*. Inline text such as `<p>Inline Text</p>` is acceptable so long as it does not exceed the *overflow line*.

Text that cannot fit inline should be brought to the next line such as the following.

```html
✅ Good
<p>
  Nullam quis risus eget urna mollis ornare vel eu leo. Cum sociis natoque
  penatibus et magnis dis <strong>parturient montes</strong>, nascetur
  ridiculus mus. Nullam id dolor id nibh ultricies vehicula.

  Cum sociis natoque penatibus et magnis dis parturient montes, nascetur
  ridiculus mus.
</p>
```

This implies that text that needs to be overflowed should not start with their parent tag. In other words **the following is NOT allowed**.

```html
❌ Bad
<p>Nullam quis risus eget urna mollis ornare vel eu leo. Cum sociis natoque
penatibus et magnis dis <strong>parturient montes</strong>, nascetur ridiculus
mus. Nullam id dolor id nibh ultricies vehicula.

Cum sociis natoque penatibus et magnis dis parturient montes, nascetur
ridiculus mus.</p>
```

The `<strong>` tag in the above example since it is an inline tag, should also be treated as inline.

```html
❌ Bad
<p>
  Nullam quis risus eget urna mollis ornare vel eu leo. Cum sociis natoque
  penatibus et magnis dis
  <strong>parturient montes</strong>,
  nascetur ridiculus mus. Nullam id dolor id nibh ultricies vehicula.

  Cum sociis natoque penatibus et magnis dis parturient montes, nascetur
  ridiculus mus.
</p>
```

The correct example above does imply that when opening a new tag, its content should be tabbed with **4 spaces** like the following example.

```html
✅ Good
<div>
  <span>Cum sociis natoque penatibus et magnis dis</span>
</div>
```

However if it can still fit within 80 characters the following the acceptable.

```html
✅ Good
<div><span>Cum sociis natoque penatibus et magnis dis</span></div>

❌ Bad
<div><span>Cum sociis natoque penatibus et magnis dis parturient montes
nascetur ridiculus mus.</span></div>
```

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

```
Page
------------------------------------------------
|                        |
|          Header            |
|                        |
------------------------------------------------
|           Body             |
|  ------------------------------------------  |
|  |   ASIDE   |    SECTION     |  |
|  |         |            |  |
|  |  -----------  |  --------------------  |  |
|  |  |     |  |  |          |  |  |
|  |  | BLOCK 1 |  |  |  ARTICLE 1   |  |  |
|  |  |     |  |  |          |  |  |
|  |  -----------  |  --------------------  |  |
|  |         |            |  |
|  |  -----------  |  --------------------  |  |
|  |  |     |  |  |          |  |  |
|  |  | BLOCK 2 |  |  |  ARTICLE 2   |  |  |
|  |  |     |  |  |          |  |  |
|  |  -----------  |  --------------------  |  |
|  ------------------------------------------  |
|                        |
------------------------------------------------
|                        |
|          Footer            |
|                        |
------------------------------------------------
```

Article tags `<article>` should be used to explain content sections. This means, you should use `article` even when describing a post, product, event etc.

### 3.1. Block and Inline

Under no circumstance should a [block tag](https://developer.mozilla.org/en-US/docs/Web/HTML/Block-level_elements) be found in an [inline tag](https://developer.mozilla.org/en-US/docs/Web/HTML/Inline_elements).

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

### 3.2. Self Closing

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

### 3.3. Headers

Headers are used to help outline a page; to help figure out the important parts of a page there by help making it possible to summarize its content.

There should be no more than one `<h1>` tag per page. Otherwise, there can be multiple instances of header tags, but do not skip header numbers. For example if there is an `<h3>`, you should also have an `<h2>`. Header text should be less than 140 characters.

```html
✅ Good
<h2>Nullam Quis Risus Eget Urna</h2>

❌ Bad
<h2>
  Nullam quis risus eget urna mollis ornare vel eu leo. Cum sociis natoque
  penatibus et magnis dis <strong>parturient montes</strong>, nascetur
  ridiculus mus. Nullam id dolor id nibh ultricies vehicula.

  Cum sociis natoque penatibus et magnis dis parturient montes, nascetur
  ridiculus mus.
</h2>
```

Headers should be treated as subject titles. This implies that the text found inside headers should follow a titling convention.

```html
✅ Good
<h2>A Major Title in Example</h2>

❌ Bad
<h2>a major title in example</h2>

❌ Bad
<h2>A MAJOR TITLE IN EXAMPLE</h2>
```

The above implies that no all caps is incorrect. If there are styles that require the text to be in all caps, you can do so in CSS instead.

### 3.4. Links

All link tags should have the `title=""` attribute. Titles should not exceed 140 characters.

```html
✅ Good
<a href="https://example.com" title="Visit Example Website">Example</a>

❌ Bad
<a href="https://example.com">Example</a>

❌ Bad
<a href="https://example.com" title="This is a very long title that exceeds the recommended 140 character limit. Please keep your titles concise and meaningful for accessibility and SEO purposes.">Example</a>
```

### 3.5. Images

All image tags should have the `alt=""` attribute. Alts should not exceed 140 characters.

```html
✅ Good
<img src="logo.png" alt="Company Logo" />

✅ Good
<img src="profile.jpg" alt="Profile picture of John Doe" />

❌ Bad
<img src="logo.png" />

❌ Bad
<img src="logo.png" alt="This is a very long alternative text that exceeds the recommended 140 character limit. Please keep your alt text concise and meaningful for accessibility and SEO purposes." />
```

### 3.6. Line Breaks

Break Tags `<br />` are only allowed if it is between text.

```html
✅ Good
<p>Nullam quis risus eget urna <br /> mollis ornare vel eu leo.</p>

✅ Good
<span>
  Nullam quis risus eget urna
  <br />
  mollis ornare vel eu leo.
</span>

✅ Good
<div>
  Nullam quis risus eget urna mollis ornare vel eu leo. Cum sociis natoque
  penatibus et magnis dis <strong>parturient montes</strong>, nascetur
  ridiculus mus. Nullam id dolor id nibh ultricies vehicula.
  <br />
  Cum sociis natoque penatibus et magnis dis parturient montes, nascetur
  ridiculus mus.
</div>
```

Do not use `<br />` to space blocks. Use CSS instead.

```html
❌ Bad
<div>
  Nullam quis risus eget urna mollis ornare vel eu leo. Cum sociis natoque
  penatibus et magnis dis <strong>parturient montes</strong>, nascetur
  ridiculus mus. Nullam id dolor id nibh ultricies vehicula.
</div>
<br />
<div>
  Cum sociis natoque penatibus et magnis dis parturient montes, nascetur
  ridiculus mus.
</div>
```

The horizontal ruling tag `<hr />` is used to define a thematic change in the content. Like break tags, do not use it to space blocks.

```html
✅ Good
<h1>HTML</h1>
<p>HTML is a language for describing web pages.....</p>

<hr />

<h1>CSS</h1>
<p>CSS defines how to display HTML elements.....</p>
```

### 3.7. Scripts and Styles

All stylesheet tags `<link>` should have an `href`, `rel` and `type` attribute. Script tags `<script>` should have at least a `type` attribute.

```html
✅ Good
<link href="/custom.css" rel="stylesheet" type="text/css" />

✅ Good
<script type="text/javascript"></script>
<script type="text/javascript" src="custom.js"></script>

❌ Bad
<script src="custom.js"></script>
<script></script>
```

### 3.8. HTML 4

Usage of `<b>` to bold, `<i>` for italics, `<s>` to strike out are prohibited. Please find their HTML5 and/or CSS3 equivalents. Do not use `<font>` under no circumstances.

## 4. Attributes

Attribute values should be within double quotes at all times.

```html
✅ Good
<input value="4" />

❌ Bad
<input value='4' />

❌ Bad
<input value=4 />
```

Attributes should placed in alphabetical order.

```html
✅ Good
<input class="form-control" name="post_count" type="text" value="4" />

❌ Bad
<input name="post_count" class="form-control" value="4" type="text" />
```

### 4.1. IDs

IDs should have unique values per page. IDs should only be used when dealing directly with javascript. You should not add styles to IDs; use classes instead. ID values should use all lowercase and dashes to separate words.

```html
✅ Good
<div id="unique-id-1"></div>
<div id="unique-id-2"></div>

❌ Bad
<div id="unique_id_1"></div>
<div id="unique_id_1"></div>
```

### 4.2. Classes

You should not use classes to indicate a particular style change. The following describes what classes not to use.

```html
❌ Bad
<div class="pad-top margin-bottom center"></div>
```

Exceptions are usage of classes already defined in Twitter Bootstrap. The following for example is acceptable, however you want to try as much as possible to try other ways.

```html
👍 OK
<div class="pull-right pull-left text-success"></div>
```

Classes should have meaningful names and minimized as much as possible. If a class has more than 5 names, you should reconsider and organize your styles. Class names should be unique enough to group HTML while considering its use across the entire site.

```html
✅ Good
<h3 class="post-title">Some Title</h3>

❌ Bad
<h3 class="title">Some Title</h3>
```

As implied above it is best practice to describe each class name with at least two words. Class names should use all lowercase and dashes to separate words.

```html
✅ Good
<div class="post-summary"></div>

❌ Bad
<div class="post_summary"></div>

✅ Good
<div class="post-item">
  <h3 class="post-title">Some Title</h3>
</div>

❌ Bad
<div class="post">
  <h3 class="title">Some Title</h3>
</div>
```

Overall classes should be strategically placed and minimized as much as possible. Lastly, classes should be alphabetical.

```html
✅ Good
<div class="active post-summary pull-right"></div>

❌ Bad
<div class="pull-right post_summary active"></div>
```

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

Just like our backend code, we encourage more comments on the front end code.

## 6. Inline Scripts and Styles

Inline styles are only permitted when dealing directly with javascript or with email HTML. Otherwise inline styles should be placed into a separate file.

```html
✅ Good
<link href="/custom.css" rel="stylesheet" type="text/css" />
<h1>Some Title</h1>

❌ Bad
<style>
h1 {
  font-weight: bold;
}
</style>
<h1>Some Title</h1>

❌ Bad
<h1 style="font-weight: bold;">Some Title</h1>
```

Inline scripts are only permitted when instructed by a third party vendor or inline a tag used to activate a script in a separate file. If it is custom code, it should be placed into a separate file.

```html
✅ Good
<h1 id="post-title-1">Some Title</h1>
<script src="custom.js" type="text/css"></script>

✅ Good
<img onerror="this.parentNode.parentNode.removeChild(this.parentNode)" />

❌ Bad
<h1 id="post-title-1">Some Title</h1>
<script type="text/javascript">
  //do some script
  var title = document.getElementById('post-title-1');
</script>
```

Templates wrapped around script tags however are acceptable.

```html
✅ Good
<script tyle="text/x-template">
  <h1>Some Title</h1>
</script>
```

## 7. Layout

The original purpose of Grids should only be used to layout a page, not to be used within specific blocks. It is recommended to use custom styling instead.

```
Page
------------------------------------------------
|                        |
|          Header            |
|                        |
------------------------------------------------
|           Body             |
|  ------------------------------------------  |
|  |   ASIDE   |    SECTION     |  |
|  |         |            |  |
|  |  -----------  |  --------------------  |  |
|  |  |     |  |  |          |  |  |
|  |  | BLOCK 1 |  |  |  ARTICLE 1   |  |  |
|  |  |     |  |  |          |  |  |
|  |  -----------  |  --------------------  |  |
|  |         |            |  |
|  |  -----------  |  --------------------  |  |
|  |  |     |  |  |          |  |  |
|  |  | BLOCK 2 |  |  |  ARTICLE 2   |  |  |
|  |  |     |  |  |          |  |  |
|  |  -----------  |  --------------------  |  |
|  ------------------------------------------  |
|                        |
------------------------------------------------
|                        |
|          Footer            |
|                        |
------------------------------------------------
```

Before using `rows` and `col-*` be sure you fully understand the subject. Consult with the team lead if you are unsure about using this.

## 8. Template One

All custom website themes should have a template one page made before development. The rationale is to increase the flexibility of UI components and to reduce the need to review custom code everytime we introduce a new UI component.

The following is how a template one page would look like. The minimum requirement for a template one page is HTML and CSS, though having the page JS and handlebars enabled would make it easier to layout different pages with the template one page.

![template-one](https://user-images.githubusercontent.com/120378/33537570-f8971358-d8f6-11e7-9457-09c93d5a0eb4.png)