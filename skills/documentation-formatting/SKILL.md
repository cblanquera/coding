---
name: documentation-formatting
description: Use this skill when standardizing markdown documentation structure, formatting, navigation, and legacy-doc conversion. It enforces consistent headings, spacing, code fences, cross-references, and document shape without taking over the editorial sequence.
---

# Documentation Formatting

This skill standardizes markdown documentation so it is consistent, scannable,
and easy to maintain.

Use it after the document's editorial plan is clear, or when the user
explicitly asks for formatting cleanup, normalization, or conversion of messy
docs into a stable structure.

## Task Intake

Before normalizing a document, identify:

1. whether it is a guide, tutorial, explanation, reference, or mixed page
2. whether the real problem is structure, editorial flow, or missing content
3. whether the file needs light cleanup or full legacy-doc conversion
4. whether another documentation skill should own the content order first

Do not start by reformatting everything mechanically. Preserve the intended
reader flow and only normalize once the document type is understood.

## Scope

Use this skill for:

- markdown structure normalization
- heading hierarchy and table of contents cleanup
- spacing, list, and code fence consistency
- link and cross-reference hygiene
- converting legacy docs into a cleaner, more consistent shape

Do not use this skill to decide the teaching order of onboarding docs. Do not
use it to define API reference schemas for classes or modules.

For those cases, use:

- `developer-documentation`
- `api-documentation`

## Priority

When this skill is used with other documentation skills:

1. Preserve the reader journey chosen by `developer-documentation`.
2. Preserve the schema chosen by `api-documentation`.
3. Apply formatting rules only when they improve consistency without making the
   doc harder to learn from.

If a structural rule would make a quick start longer, denser, or harder to
follow, relax the rule.

## Core rules

- Start with one H1 title.
- Add a short description near the top when it helps orient the reader.
- Use a logical heading hierarchy.
- Add a table of contents when the document is long enough to benefit from it.
- Use descriptive headings.
- Separate document blocks with a single empty line.
- Use consistent list formatting and parallel structure.
- Always add a language tag to fenced code blocks.
- Keep code examples syntactically correct and realistic.
- Keep internal links and cross-references working.

## Conversion workflow

When converting or normalizing existing docs:

1. Classify the document type: guide, tutorial, explanation, reference, or
   mixed.
2. Preserve the useful content, but do not preserve bad structure.
3. Remove duplication, broken hierarchy, and formatting noise.
4. Add missing navigational elements only where they help.
5. Keep examples complete enough to be actionable.
6. Re-check links, anchors, and heading order.

## Decision rules

- Prefer consistency, but not at the cost of readability.
- Prefer scannable structure over decorative structure.
- Prefer shorter descriptions when the heading is already clear.
- Do not force numbering on every document unless the existing system or user
  explicitly wants it.
- Do not apply the "at least two" rule mechanically when a single subsection is
  clearer.

## Deliverables

The output should leave the document with:

- a stable heading hierarchy
- normalized spacing, lists, and fenced code blocks
- working links and anchors
- only the navigational elements that improve scanning
- no formatting changes that make the content harder to learn from

## Review gate

Do not consider the output complete unless the answer to all of these is yes:

- Is the heading hierarchy clear and consistent?
- Are spacing, lists, and code fences normalized?
- Are links and anchors correct?
- Does the structure help scanning instead of adding noise?
- Did formatting cleanup avoid damaging the intended reader flow?
