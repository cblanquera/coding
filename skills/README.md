# Codex Skills

This folder contains reusable Codex skills that can be installed into your
local Codex skill directory and invoked by name in prompts.

Each skill lives in its own folder and includes a `SKILL.md` file that tells
Codex when to use the skill and how to apply it.

## Included Skills

| Skill | Purpose |
| --- | --- |
| `api-documentation` | Write or restructure API reference docs for classes, modules, methods, configuration, and typed examples. |
| `developer-documentation` | Write onboarding docs, quick starts, tutorials, and conceptual developer guides. |
| `documentation-formatting` | Normalize markdown structure, headings, code fences, links, and general document layout. |
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
cp -R <your-repo>/skills/developer-documentation ~/.codex/skills/
cp -R <your-repo>/skills/documentation-formatting ~/.codex/skills/
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
Use $developer-documentation to turn this draft into a proper quick start.
```

```text
Use $api-documentation and $documentation-formatting to rewrite this API page.
```

Codex can also auto-select a skill when your request clearly matches the
skill's description, but naming the skill explicitly is the most reliable way
to force it on a task.

## Structure

Each skill directory typically contains:

- `SKILL.md`: the instructions Codex reads and follows
- `agents/openai.yaml`: optional display metadata and default prompt text for
  the OpenAI/Codex agent interface

Keep the folder name stable because that is the name you will reference in
prompts.

## Notes

- You can install one skill or all of them.
- If you update a skill from GitHub, copy the updated folder back into
  `~/.codex/skills`.
- These skills are opinionated for the `cblanquera` coding repositories, so
  some coding-style rules are intentionally specific.
