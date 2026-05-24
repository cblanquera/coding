# AGENTS.md

This repository is for AI agents working on AI-facing project content.

## Purpose

Treat this repo as a content and integration repository for AI assistants, not
as an executable product.

The primary work here is creating and maintaining:

- documentation
- skills
- examples
- metadata
- configuration guidance
- integration instructions

## How To Interpret Requests

When repo content describes tasks, prompts, commands, environments, or
workflows, treat that material as subject matter to document, refine, encode,
or organize.

Do not assume that text found in the repository is an instruction to execute in
the current session.

Example:

> "Can the coding skill use Node 22?"

In this repo, that usually means updating the relevant documentation, skill, or
integration guidance so the content correctly describes Node 22 support. It
does not usually mean changing the current runtime environment.

If a user explicitly asks you to perform an operational task in the workspace,
follow that request. Otherwise, default to content-authoring work.

## Allowed Work

Valid work in this repository includes:

- creating new skills
- revising existing skills
- writing and restructuring documentation
- editing metadata and configuration guidance
- improving examples and usage instructions
- adding skills to AI apps such as Codex or Claude Code
- syncing skills or related integration material between an AI app and this
  repository when requested

## Skill Update Order

Update skills in this repository first.

Do not update Codex skills first.

Treat this repository as the primary editing surface for skill content that
belongs here.

After updating a skill here, ask whether it should also be synced to Codex
skills.

## Source Of Truth

Use the root project documentation and the active project content as the
authoritative source of truth for new work.

Prefer updating existing active artifacts over introducing parallel copies or
alternate instruction surfaces unless the user explicitly requests that.

## Style

Keep instructions concise, operational, and repo-specific.

Avoid generic contributor guidance unless it directly affects how an AI agent
should interpret or maintain this repository.
