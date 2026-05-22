---
name: chrisai-coding-html-css
description: Use when writing or reviewing vanilla HTML and CSS in the cblanquera coding repos, especially for static sites, documentation pages, and frontend templates that need semantic markup, durable class structure, and maintainable styling.
---

# ChrisAI Coding HTML CSS

Use this skill for vanilla HTML and CSS implementation, refactors, and reviews
for static sites and frontend templates.

## Repo Discovery Workflow

Before applying standards, inspect:

1. the touched template and stylesheet
2. nearby layout, partial, or page files
3. existing naming, sectioning, and comment patterns
4. any build or hosting constraints that affect emitted markup

If the project already has a stronger local pattern, preserve it.

## Priority Order

1. Match the style of the touched files when it is clear.
2. Apply the standards in this skill.
3. Preserve local patterns unless the user explicitly asks to normalize them.

## HTML Rules

- Start with semantic structure before cosmetic wrappers.
- Keep heading levels in order and use no more than one `<h1>` per page.
- Prefer meaningful, lowercase, dash-separated class names.
- Use IDs only when JavaScript needs them.
- Keep attributes readable and alphabetized when a tag has several.
- All `<a>` tags should have a `title` attribute unless the local pattern
  clearly omits it.
- All `<img>` tags must have an `alt` attribute.
- Prefer deploy-safe links and asset paths for static hosting.

## CSS Rules

- Organize styles by ownership before writing selectors.
- Prefer class selectors over tag selectors.
- Keep selector depth shallow and manageable.
- Order properties alphabetically.
- Use 6-character uppercase hex colors.
- Avoid `!important` unless overriding existing `!important` rules is the only
  clean option.

## Review Gate

Do not consider the output complete unless the answer to all of these is yes:

- Is the HTML semantic and easy to scan?
- Are class names stable and structurally meaningful?
- Do selectors have clear ownership and reasonable depth?
- Do links and assets look safe for the target deploy model?
