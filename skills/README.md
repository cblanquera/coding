# Codex Skills

This folder contains reusable Codex skills that can be installed into your
local Codex skill directory and invoked by name in prompts.

Each skill lives in its own folder and includes a `SKILL.md` file that tells
Codex when to use the skill and how to apply it.

## Included Skills

| Skill | Purpose |
| --- | --- |
| `api-documentation` | Write or restructure API reference docs for classes, modules, methods, configuration, and typed examples. |
| `documentation-manager` | Route documentation tasks across the repo's documentation skills and sequence them correctly. |
| `developer-documentation` | Write onboarding docs, quick starts, tutorials, and conceptual developer guides. |
| `documentation-formatting` | Normalize markdown structure, headings, code fences, links, and general document layout. |
| `github-pages-docs-builder` | Build Markdown-first technical documentation sites for GitHub Pages with source in `specs/`, generated output in `docs/`, and repo-local build scripts. |
| `github-pages-qa-screenshot` | Run browser QA and capture screenshots for generated GitHub Pages sites using a repo-local preview helper. |
| `html-css-developer` | Write or review vanilla HTML and CSS for static sites, docs pages, and GitHub Pages style projects. |
| `static-site-visual-design` | Define or refine the visual direction for static sites and documentation homepages before or during implementation. |
| `technical-docs-editor` | Edit technical documentation for junior developers without changing technical meaning. |
| `react-ts-developer` | Write or review TypeScript ReactJS / TSX using the conventions used in these repos. |
| `test-engineer` | Write or review Jest or Mocha + Chai tests using the conventions used in these repos. |
| `typescript-developer` | Write or review TypeScript using the conventions used in these repos. |

## Install

Clone this repository somewhere on your machine:

```bash
git clone https://github.com/<your-user>/<your-repo>.git
```

Create the Codex skills directory if it does not already exist:

```bash
mkdir -p ~/.codex/skills
```

Copy any skill folders you want to install into `~/.codex/skills`:

```bash
cp -R <your-repo>/skills/typescript-developer ~/.codex/skills/
cp -R <your-repo>/skills/react-ts-developer ~/.codex/skills/
cp -R <your-repo>/skills/test-engineer ~/.codex/skills/
cp -R <your-repo>/skills/api-documentation ~/.codex/skills/
cp -R <your-repo>/skills/documentation-manager ~/.codex/skills/
cp -R <your-repo>/skills/developer-documentation ~/.codex/skills/
cp -R <your-repo>/skills/documentation-formatting ~/.codex/skills/
cp -R <your-repo>/skills/github-pages-docs-builder ~/.codex/skills/
cp -R <your-repo>/skills/github-pages-qa-screenshot ~/.codex/skills/
cp -R <your-repo>/skills/html-css-developer ~/.codex/skills/
cp -R <your-repo>/skills/static-site-visual-design ~/.codex/skills/
cp -R <your-repo>/skills/technical-docs-editor ~/.codex/skills/
```

If Codex is already running, restart it so it reloads the installed skills.

## Use In Codex

Reference a skill directly in your prompt with `$<skill-name>`.

Examples:

```text
Use $typescript-developer to refactor this module.
```

```text
Use $react-ts-developer to clean up this TSX component.
```

```text
Use $documentation-manager to figure out how to rewrite this library documentation set without me tagging multiple roles.
```

```text
Use $html-css-developer to clean up this HTML template and the CSS that styles it.
```

```text
Use $github-pages-docs-builder to turn these Markdown docs into a GitHub Pages site with source in specs/ and generated output in docs/.
```

```text
Use $static-site-visual-design to define the visual direction for this docs homepage before touching the CSS.
```

```text
Use $github-pages-qa-screenshot to preview the generated GitHub Pages site locally and capture screenshots of the homepage and one article page.
```

```text
Use $developer-documentation to turn this draft into a proper quick start.
```

```text
Use $api-documentation and $documentation-formatting to rewrite this API page.
```

```text
Use $technical-docs-editor to simplify this library guide for junior developers without changing the API behavior.
```

Codex can also auto-select a skill when your request clearly matches the
skill's description, but naming the skill explicitly is the most reliable way
to force it on a task.

## Structure

Each skill directory typically contains:

- `SKILL.md`: the instructions Codex reads and follows
- `agents/openai.yaml`: optional display metadata and default prompt text for
  the OpenAI/Codex agent interface
- `scripts/`: optional helper scripts used by the skill

Keep the folder name stable because that is the name you will reference in
prompts.

## Notes

- You can install one skill or all of them.
- If you update a skill from GitHub, copy the updated folder back into
  `~/.codex/skills`.
- Some skills include helper scripts under `scripts/`; install the whole skill
  directory so those helpers are available.
- These skills are opinionated for the `cblanquera` coding repositories, so
  some coding-style rules are intentionally specific.
