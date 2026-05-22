---
name: github-pages-vanilla
description: Use when Codex needs to turn Markdown-first documentation into a vanilla static site with GitHub Pages-compatible output, including repo layout decisions, specs-to-docs migration, builder structure, package script normalization, and specialist-skill sequencing.
---

# GitHub Pages Vanilla

Use this skill as the manager for vanilla static documentation-site work that
targets GitHub Pages-compatible output.

It owns:

- repo discovery
- source-of-truth layout decisions
- migration policy
- builder structure
- GitHub Pages deployment constraints
- template-engine decisions
- specialist-skill routing

It does not try to own every implementation detail itself. Route visual-system
work, documentation shaping, frontend implementation, and browser QA to
narrower skills.

This skill is opinionated. It assumes:

- authored docs live in `specs/`
- published output lives in `docs/`
- site source and build scripts live in `www/` or `packages/www`
- implementation uses vanilla HTML, CSS, and JavaScript unless the repo
  already establishes another static-site pattern
- generated output is not edited by hand

Use `chrisai-coding-html-css` for frontend implementation rules, including
page structure, template markup, stylesheet organization, and static-site HTML
and CSS quality.

Use `chrisai-design-creative` when the work is mainly about creative
direction, visual hierarchy, brand adaptation, homepage composition, or
visual-system decisions.

Use `chrisai-qa-playwright` when the work is mainly about local preview
startup, browser QA, responsive checks, screenshot capture, or Playwright
recordings for the generated site.

Use `chrisai-docs-copy-editing` only when the site needs faithful editorial
help for existing prose or brief connective copy that stays supported by the
local source.

Use `chrisai-docs-dev-onboarding` for getting-started flows, conceptual docs,
and homepage orientation written for junior developers.

Use `chrisai-docs-dev-api-reference` for lookup-oriented reference pages,
module/class/function/config documentation, and structured reference examples.

Use `chrisai-docs-dev-formatting` for final markdown normalization, outline
cleanup, TOC decisions, and structure cleanup after the document type is
already understood.

## Managed Skills

This skill coordinates the minimum necessary sequence across:

- `chrisai-coding-html-css`
- `chrisai-design-creative`
- `chrisai-docs-dev-onboarding`
- `chrisai-docs-dev-api-reference`
- `chrisai-docs-copy-editing`
- `chrisai-docs-dev-formatting`
- `chrisai-qa-playwright`

## Core Rule

Keep ownership boundaries explicit.

- This skill decides the architecture and workflow.
- `chrisai-design-creative` owns the visual direction and visual-system
  decisions.
- `chrisai-docs-dev-onboarding` owns onboarding flow, homepage orientation,
  and junior-developer learning sequence.
- `chrisai-docs-dev-api-reference` owns the structure of lookup-oriented
  reference material.
- `chrisai-docs-copy-editing` owns editorial cleanup for existing prose that
  already has the right content owner and structure.
- `chrisai-docs-dev-formatting` owns final markdown normalization and
  structure cleanup.
- `chrisai-coding-html-css` owns HTML and CSS implementation quality.
- `chrisai-qa-playwright` owns preview startup, browser validation,
  screenshots, and recordings.

Do not collapse all roles back into one long instruction set.

## Routing Rules

Use `chrisai-design-creative` when the task is mainly about:

- defining or refining the design concept
- adapting brand assets into a docs-site system
- homepage visual composition
- color, type, spacing, atmosphere, or hierarchy decisions
- deciding how the site should feel before or during implementation

Use `chrisai-docs-dev-onboarding` when the task is mainly about:

- homepage orientation
- quick starts and getting-started paths
- conceptual developer guides
- junior-developer-first learning flows
- separating high-level guidance from deeper reference material

Use `chrisai-docs-dev-api-reference` when the task is mainly about:

- module, class, function, or configuration reference pages
- structured lookup content
- durable reference schemas
- examples that support integration or usage lookup

Use `chrisai-docs-dev-formatting` when the task is mainly about:

- markdown cleanup
- outline numbering and TOC decisions
- style-guide conformance
- structure cleanup after the document type is already settled

Use `chrisai-docs-copy-editing` when the task is mainly about:

- clarifying existing technical prose
- smoothing transitions between source-supported sections
- tightening copy without changing meaning
- improving readability after the main document type and flow are already set

Use `chrisai-coding-html-css` when the task is mainly about:

- implementing templates or fragments
- cleaning up HTML structure
- reorganizing CSS ownership
- improving static-site frontend maintainability

Use `chrisai-qa-playwright` when the task is mainly about:

- starting a localhost preview for browser testing
- checking responsive or visual issues in the generated site
- capturing screenshots or recordings of the generated output
- validating rendered flows through deterministic browser automation
- separating repo-side issues from environment-side preview blockers

## Sequencing Rules

Apply specialist skills in the narrowest useful sequence.

Default implementation path:

1. This skill decides layout, migration, and build contract.
2. `chrisai-design-creative` sets or validates the visual direction when
   design work is needed.
3. Use documentation specialists as needed:
   - `chrisai-docs-dev-onboarding` for guide, homepage, and start-here flow
   - `chrisai-docs-dev-api-reference` for lookup-oriented reference pages
   - `chrisai-docs-copy-editing` for second-pass editorial cleanup
   - `chrisai-docs-dev-formatting` last for cleanup
4. `chrisai-coding-html-css` implements the templates, fragments, and styles.
5. `chrisai-qa-playwright` validates the generated output and captures
   screenshots or recordings when browser QA artifacts are needed and the
   environment allows.

Do not run browser QA first when the repo layout or preview contract is still
unclear.

## When To Use

Use this skill when the user wants to:

- turn Markdown docs into a static docs website
- publish docs through GitHub Pages-compatible output
- migrate `docs/` source into `specs/` and keep `docs/` as generated output
- build a lightweight docs site without a framework like Docusaurus or
  VitePress
- restyle or rebuild an existing static docs site while preserving repo-local
  content and assets
- coordinate layout, design, implementation, documentation shaping, and QA
  across multiple skills

Do not use this skill when:

- the user wants a SPA or application frontend
- the repo already has a framework-based docs stack the user wants preserved
- the task is mainly editorial copy work with no site generation
- the task is only browser QA, screenshots, or recordings for an already-built
  site
- the task is only visual direction work with no docs-site architecture

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
.playwright/
.playwright/serve.mjs
.playwright/check.mjs
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
.playwright/
.playwright/serve.mjs
.playwright/check.mjs
```

## Defaults

Default assumptions unless the user says otherwise:

- deployment target is GitHub Pages-compatible output
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

Do not assume SSR, React, Vue, or multi-version docs unless requested.

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

The build must be able to fully recreate `docs/` from `specs/` and the builder
root.

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
- lives in repo-root `.playwright/` because preview startup is QA-facing
  infrastructure rather than builder logic
- locally preview the generated `docs/` output
- read both `HOST` and `PORT` from the environment when provided
- pass `HOST` and `PORT` through to the underlying server bind call so browser
  QA can request a localhost-only preview when needed

`check.mjs`
- lives in repo-root `.playwright/` because site validation is QA-facing
  infrastructure rather than build generation logic
- validate required structure and files
- validate build output exists for key pages
- check internal links where feasible
- check expected metadata and asset outputs where feasible

Normalize the nearest relevant `package.json` to use:

- `www:build`
- `www:serve`
- `www:check`

## Generator Maintainability Rules

Keep the site generator maintainable as the number of pages and templates
grows.

- prefer passing structured data into templates over assembling large HTML
  strings in JavaScript
- keep repeated markup in reusable fragments rather than recreating it in
  build logic
- keep build scripts focused on content discovery, routing, metadata, and data
  shaping
- keep HTML composition in templates whenever the template engine can support
  it
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
`chrisai-docs-copy-editing` for brief connective copy only when the needed
meaning is already supported by the local source. If the source does not
support the claim, leave a clear placeholder or ask the user.

## Homepage Content Rules

Treat the homepage as a product and orientation surface, not just the first
doc page.

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

If the user does not provide a site URL or preview image, use only the tags
that can be filled accurately from local context.

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

## Terminal-First Verification Mode

The docs workflow must be verifiable without depending on browser automation.

- implement a build script that fully regenerates `docs/`
- implement a repo-root `.playwright/serve.mjs` script for previewing
  generated output
- implement a repo-root `.playwright/check.mjs` script that validates the
  generated site structure
- validate internal links where practical
- validate copied assets and key generated pages exist
- check for obvious generation mistakes such as unresolved placeholders,
  leftover source-only paths, or leaked `.md` links in output HTML where those
  links should have been rewritten
- use browser automation when available for visual confirmation, but do not
  make it a hard dependency of the workflow

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
10. Route visual direction work to `chrisai-design-creative` when needed.
11. Route docs shaping to `chrisai-docs-dev-onboarding`,
    `chrisai-docs-dev-api-reference`, and `chrisai-docs-dev-formatting` as
    needed.
12. Implement templates, fragments, styles, and scripts.
13. Generate the site into `docs/`.
14. Run `www:check`.
15. Route browser validation to `chrisai-qa-playwright` when browser QA or
    capture artifacts are needed and possible.
16. Do a cleanup pass on HTML, CSS, templates, and generator code.
17. Summarize the final editing and publishing workflow.

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
- Did the correct specialist skills own design, documentation shaping, and QA
  concerns when those concerns mattered?
- Do the homepage and at least one doc page render?
- Do nav, table-of-contents, and pager links resolve where applicable?
- Are code examples readable and copyable when that feature is enabled?
- Are SEO tags present in the shared layout?
- Did the work avoid editing generated output as source?
- Did the source templates and styles receive a cleanup pass after major
  structure changes?
- Can the site be validated from the terminal even when browser automation is
  unavailable?
