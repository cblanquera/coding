---
name: github-pages-docs-builder
description: Build and maintain static technical documentation websites for GitHub Pages from Markdown source. Use this skill when Codex needs to migrate docs source into specs/, generate publishable HTML into docs/, scaffold a repo-local www builder area, reuse existing logos and assets, choose or inspect a template engine, and implement a lightweight docs site with vanilla HTML, CSS, and JavaScript.
---

# GitHub Pages Docs Builder

Use this skill to build or refactor a Markdown-first technical documentation site
for GitHub Pages.

This is primarily an orchestration skill. It owns repo discovery, migration
rules, builder structure, GitHub Pages constraints, and the overall docs-site
workflow. It should delegate specialized implementation work to narrower skills
instead of trying to inline every concern itself.

This skill is opinionated. It assumes:

- authored docs live in `specs/`
- published output lives in `docs/`
- site source and build scripts live in `www/` or `packages/www`
- implementation uses vanilla HTML, CSS, and JavaScript
- generated output is not edited by hand

Use [`html-css-developer`](../html-css-developer/SKILL.md) for frontend
implementation rules, including page structure, template markup, stylesheet
organization, and static-site HTML and CSS quality.

Use [`technical-docs-editor`](../technical-docs-editor/SKILL.md) only when the
site needs editorial help for existing prose or when bridging small missing
connector copy between pages. Do not use it to invent product claims, API
behavior, or feature explanations that are not supported by the local source.

## Delegation Model

This skill coordinates the overall docs-site build. Its role is to decide the
site shape, source-of-truth locations, migration path, and validation flow.

Delegate to `html-css-developer` when the work is mainly about:

- HTML template structure
- CSS architecture or cleanup
- semantic layout decisions
- static-site frontend implementation details

Delegate to `technical-docs-editor` when the work is mainly about:

- clarifying existing technical prose
- smoothing transitions between existing sections
- tightening source-supported homepage or landing-page copy
- improving readability without changing technical meaning

Do not delegate core ownership decisions away from this skill, including:

- whether the site should use `specs/`, `docs/`, and the builder root
- whether the builder belongs in `packages/www` or root `www`
- how existing docs and assets should be migrated
- which template engine is being used and how it should be inspected
- what validation and publishing workflow the repo should follow

## When To Use

Use this skill when the user wants to:

- turn Markdown docs into a static docs website
- publish docs through GitHub Pages
- migrate `docs/` source into `specs/` and keep `docs/` as generated output
- build a lightweight docs site without a framework like Docusaurus or
  VitePress
- restyle or rebuild an existing static docs site while preserving repo-local
  content and assets

Do not use this skill when:

- the user wants a SPA or application frontend
- the repo already has a framework-based docs stack the user wants preserved
- the task is mainly editorial copy work with no site generation
- the user only wants markdown formatting cleanup

## First Questions

Before making structural edits, ask:

1. What is the design concept?
   Examples: blueprint, editorial, handbook, terminal, industrial, minimal.
2. Where are the logos, icons, screenshots, and reusable images?
   Ask for exact files or folders.
3. What template engine should be used?
4. If the template engine is custom, can the user provide local source or a
   link to source or docs?
5. Does the site need light and dark mode?
6. What docs-site features are required beyond the defaults?
   Examples: syntax highlighting, copy buttons, sidebar, table of contents,
   pager, search stub, version banner.
7. What is the public site URL for canonical, Open Graph, and Twitter tags?
8. Is there a social preview image available?

If the user references another static site as an example, ask one clarifying
question before copying any patterns:

- Is that site a visual reference, a build-pattern reference, or both?

If it is only a build-pattern reference, borrow structure, file layout, and
build ideas only. Do not copy its visual design, content hierarchy, or brand
language.

## Repo Detection

Inspect the repo shape before scaffolding.

If the repo has a `packages/` directory:

- use `packages/www` for the docs builder area

If the repo does not have a `packages/` directory:

- use root `www`

Use this layout for monorepos:

```text
specs/
docs/
packages/www/
packages/www/assets/
packages/www/fragments/
packages/www/templates/
packages/www/styles/
packages/www/scripts/
packages/www/build.mjs
packages/www/serve.mjs
packages/www/check.mjs
```

Use this layout for non-monorepos:

```text
specs/
docs/
www/
www/assets/
www/fragments/
www/templates/
www/styles/
www/scripts/
www/build.mjs
www/serve.mjs
www/check.mjs
```

## Defaults

Default assumptions unless the user says otherwise:

- deployment target is GitHub Pages
- source docs are Markdown
- final site output goes in `docs/`
- authored docs live in `specs/`
- reusable site assets live in the builder root `assets/` directory
- package scripts are normalized to:
  - `www:build`
  - `www:serve`
  - `www:check`

Default docs-site features:

- responsive layout
- homepage plus doc-page templates
- sidebar navigation
- page table of contents when useful
- previous and next pager
- syntax highlighting for code blocks
- copy button for code examples
- Open Graph meta tags
- Twitter card meta tags

Do not assume Mermaid, search, SSR, React, Vue, or multi-version docs unless
requested.

## Migration Rules

Inspect existing folders before moving anything.

If `docs/` contains Markdown source files and does not clearly look like
generated site output:

- move the Markdown source into `specs/`

If `docs/` appears to already be generated output:

- preserve it unless the user asks to replace it

If `docs/` mixes source Markdown and generated assets:

- stop and ask before moving files

If reusable logos, icons, or images live elsewhere and appear to belong to the
docs site:

- move or copy them into the builder root `assets/` directory
- update templates and build scripts to treat the builder root `assets/`
  directory as the source of truth
- copy those assets into `docs/assets` during the build

The build must be able to fully recreate `docs/` from `specs/` and the builder root.

## Template Engine Rules

Support three modes:

1. no template engine
2. known engine already present in the repo
3. custom engine provided by source or link

If the engine is custom:

- require local source, a local file path, or a URL to source or docs
- inspect the source or docs before using it
- summarize the supported syntax and rendering model
- only proceed once usage is clear enough to implement correctly

Do not guess custom template syntax.

## Build Contract

Set up these responsibilities:

`build.mjs`
- read Markdown from `specs/`
- read templates, fragments, styles, and scripts from the builder root
- generate the final site into `docs/`
- copy assets from the builder root `assets/` directory into `docs/assets`

`serve.mjs`
- locally preview the generated `docs/` output
- read both `HOST` and `PORT` from the environment when provided
- pass `HOST` and `PORT` through to the underlying server bind call so browser
  QA can request a localhost-only preview when needed

`check.mjs`
- validate required structure and files
- validate build output exists for key pages
- check internal links where feasible
- check expected metadata and asset outputs where feasible

Normalize the nearest relevant `package.json` to use:

- `www:build`
- `www:serve`
- `www:check`

## QA Workflow

When doing browser QA for the generated docs site:

- use the installed helper at
  `~/.codex/skills/github-pages-docs-builder/scripts/localhost_preview.py` to
  run the build and preview commands with `HOST` and `PORT` bound for localhost
  testing
- treat that helper as part of the skill installation, not part of the target
  project
- do not search the target project for `scripts/localhost_preview.py`
- do not report a missing repo-local `scripts/localhost_preview.py` as a repo
  gap or propose adding one to the target project
- ensure the target project's `serve.mjs` or equivalent preview entrypoint
  honors both `HOST` and `PORT` before relying on the wrapper for browser
  automation
- if the preview server currently ignores `HOST`, update the project-side serve
  script to pass the requested host into the server bind call
- use the wrapper when the preview server needs an explicit localhost bind for
  Browser or other local browser automation
- keep the actual build and serve commands repo-specific; the script is only a
  wrapper for consistent preview startup
- if local preview or browser automation is blocked by the environment or
  sandbox, say so clearly and separate the repo-side gap from the
  environment-side blocker

## Generator Maintainability Rules

Keep the site generator maintainable as the number of pages and templates grows.

- prefer passing structured data into templates over assembling large HTML
  strings in JavaScript
- keep repeated markup in reusable fragments rather than recreating it in build
  logic
- keep build scripts focused on content discovery, routing, metadata, and data
  shaping
- keep HTML composition in templates whenever the template engine can support it
- avoid one-off inline fragments in JavaScript when a named template or
  fragment would make the output easier to reason about
- separate homepage rendering from article-page rendering when they have
  materially different structure or goals
- after major template refactors, remove dead fragments, dead selectors, and
  stale render paths before finishing

## Content Rules

Preserve Markdown semantics in article content.

For display-only contexts such as titles, nav labels, table-of-contents items,
and pager labels:

- remove raw Markdown formatting artifacts when needed
- preserve article-body inline code formatting where it belongs
- avoid duplicate visible H1 rendering when the page hero already displays the
  page title

If content gaps prevent the site from reading coherently, use
`technical-docs-editor` for brief connective copy only when the needed meaning
is already supported by the local source. If the source does not support the
claim, leave a clear placeholder or ask the user.

## Homepage Content Rules

Treat the homepage as a product and orientation surface, not just the first doc
page.

- use a dedicated homepage layout when the homepage serves a different role
  than article pages
- keep the homepage high level and focused on what the project is, why it
  matters, and where to start
- prefer real content derived from local docs and repo context over generic
  placeholder marketing copy
- surface a concrete quick-start or representative code example above the fold
  when the product benefits from showing how it works early
- avoid front-loading deep caveats, edge-case guidance, or dense conceptual
  lists on the homepage unless the user explicitly wants them there
- make top-level calls to action clear and specific
- ensure homepage navigation labels describe actual destinations accurately;
  reserve `Home` for the homepage and use labels like `Start Here` only when
  they point to a real onboarding path

## SEO Rules

The shared layout should include:

- `<title>`
- meta description
- canonical URL when the site URL is known
- Open Graph title, description, type, URL, and image when available
- Twitter card, title, description, and image when available

If the user does not provide a site URL or preview image, use only the tags that
can be filled accurately from local context.

## GitHub Pages Path Safety

Assume the final site may be served from a repository subpath rather than the
origin root.

- prefer deploy-safe links and asset references that work on GitHub Pages
- avoid assuming absolute-root `/` paths are safe unless the project clearly
  requires them
- keep generated navigation, pager, table-of-contents, and asset paths
  consistent with the intended deployment shape
- ensure copied assets and generated pages preserve relative-link correctness
- when canonical URLs are emitted, build them from the real public site URL
  rather than guessing from local paths

## Visual Design Rules

The design concept drives the system. Do not start styling before the concept,
assets, and constraints are clear.

Use the provided logos, icons, and images to infer:

- likely accent colors
- compatible background treatments
- layout density
- whether the brand direction is playful, editorial, technical, or restrained

Treat design references carefully:

- preserve the repo's brand identity over the reference site's look
- if a reference was provided only for build structure, do not inherit its
  aesthetics
- if a reference was provided for visual direction, still adapt it to the local
  brand assets and documentation needs

Avoid generic docs styling when the concept supports a stronger visual system.

## Terminal-First Verification Mode

The docs workflow must be verifiable without depending on browser automation.

- implement a build script that fully regenerates `docs/`
- implement a local serve script for previewing generated output
- implement a check script that validates the generated site structure
- validate internal links where practical
- validate copied assets and key generated pages exist
- check for obvious generation mistakes such as unresolved placeholders,
  leftover source-only paths, or leaked `.md` links in output HTML where those
  links should have been rewritten
- use browser automation when available for visual confirmation, but do not make
  it a hard dependency of the workflow

## Visual QA Checklist

Before finishing visual work, check the generated site for:

- homepage looks like a homepage rather than a raw documentation page
- background treatments remain coherent across the full viewport width
- spacing and alignment are consistent in shared layout areas and hero sections
- text does not clip, overlap, or drift off-grid at common viewport widths
- decorative elements have a clear purpose and do not confuse the hierarchy
- navigation labels match destination meaning
- code blocks remain readable in all supported themes
- copy buttons are present and visually associated with their code blocks when
  that feature is enabled
- light and dark mode both remain legible and visually coherent when those
  themes are supported

## Workflow

1. Inspect the repo structure.
2. Determine whether the builder belongs in `packages/www` or root `www`.
3. Ask the discovery questions.
4. Inspect docs content, assets, and current output folders.
5. Decide whether `docs/` needs migration to `specs/`.
6. Inspect or confirm the template engine.
7. Move or organize reusable assets into the builder root `assets/` directory.
8. Scaffold the `www` structure.
9. Normalize `package.json` commands to `www:*`.
10. Implement templates, fragments, styles, and scripts.
11. Generate the site into `docs/`.
12. Run `www:check`.
13. Do a cleanup pass on HTML, CSS, templates, and generator code.
14. Summarize the final editing and publishing workflow.

## Finish Pass Requirements

Before considering the task complete, do one maintainability pass over the
output source.

- remove stale HTML structures left behind by earlier layout iterations
- remove dead CSS selectors, duplicate rules, and outdated page-specific hooks
- normalize HTML readability for shared templates and fragments
- normalize CSS organization, selector ownership, and property ordering
- keep generated output and source-of-truth templates clearly separated
- ensure the final source matches the current site architecture rather than an
  accumulation of abandoned experiments

## Validation Checklist

Do not finish until the answer to all of these is yes:

- Do authored docs live in `specs/`?
- Does generated output live in `docs/`?
- Do reusable assets live in the builder root `assets/` directory?
- Can the build recreate `docs/` from source?
- Do `www:build`, `www:serve`, and `www:check` exist?
- Do the homepage and at least one doc page render?
- Do nav, table-of-contents, and pager links resolve where applicable?
- Are code examples readable and copyable when that feature is enabled?
- Are SEO tags present in the shared layout?
- Did the work avoid editing generated output as source?
- Did the source templates and styles receive a cleanup pass after major
  structure changes?
- Can the site be validated from the terminal even when browser automation is
  unavailable?
