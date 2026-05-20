---
name: static-site-visual-design
description: Shape the visual direction for a static site or documentation site. Use this skill when Codex needs to define or refine the design concept, adapt logos and brand assets, decide homepage composition, and turn product or docs content into a deliberate visual system before or during implementation.
---

# Static Site Visual Design

Use this skill when the main problem is visual direction rather than repo
architecture or browser QA.

This skill owns:

- design concept selection and refinement
- visual hierarchy
- homepage and landing-page composition
- color and background direction
- typography direction
- layout atmosphere and density
- adaptation of provided brand assets into a coherent docs-site system

This skill does not own:

- repo layout decisions
- `specs/` to `docs/` migration policy
- template-engine selection
- preview-server startup workflow
- browser automation or screenshot capture

Use [`github-pages-docs-builder`](../github-pages-docs-builder/SKILL.md) when
the task also needs repo layout, migration, build, or publishing decisions.

Use [`html-css-developer`](../html-css-developer/SKILL.md) to implement the
chosen direction in HTML and CSS once the design call is clear.

## Intake

Before styling, identify:

1. the design concept
2. the available logos, icons, screenshots, and reusable images
3. whether the site needs light mode, dark mode, or both
4. whether the reference site is for visuals, build structure, or both
5. the homepage role: marketing surface, orientation surface, handbook entry,
   or product-doc hybrid
6. any constraints from an existing brand, design system, or product UI

If a reference was provided only for build structure, do not borrow its visual
language.

## Design Rules

The concept drives the system. Do not start styling before the concept, assets,
and constraints are clear.

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

## Homepage Rules

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
- ensure homepage navigation labels describe actual destinations accurately

## Visual System Heuristics

For docs-oriented static sites:

- make navigation and reading surfaces feel intentional, not default
- use decorative elements only when they clarify hierarchy or brand tone
- keep article pages calmer than the homepage
- ensure code examples remain visually subordinate to the page chrome only
  where appropriate; code must stay readable first
- choose spacing systems that create rhythm across sidebar, content, and hero
  regions
- if dual themes exist, ensure both themes feel designed rather than one being
  an afterthought

## Handoff To Implementation

When handing work to `html-css-developer`, define:

- the design concept in one sentence
- the intended homepage role
- the visual tone
- the major layout motifs
- the color strategy
- the typography strategy
- any constraints from brand assets or existing UI

Do not hand off vague directions like "make it modern" or "make it pop."

## Visual Review Checklist

Before considering the design direction stable, check:

- homepage looks like a homepage rather than a raw documentation page
- background treatments remain coherent across the full viewport width
- spacing and alignment are consistent in shared layout areas and hero sections
- decorative elements have a clear purpose and do not confuse the hierarchy
- navigation labels match destination meaning
- code blocks remain readable in all supported themes
- light and dark mode both remain legible and visually coherent when those
  themes are supported
- the visual system still feels like the local product or brand rather than a
  transplanted reference site
