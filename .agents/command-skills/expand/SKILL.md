---
name: expand
description: >-
  Enrich the candidate profile (/expand) by scanning documents in documents/ and
  public online presence (GitHub repositories, portfolio, Kaggle, Google Scholar,
  course syllabi) to surface additional competencies and independent projects.
  Triggers on: /expand, expandir perfil, enriquecer perfil, escanear github e cursos,
  expand competencies.
---

# /expand — Competency Expansion from Documents and Online Presence (Antigravity Skill)

This skill is the Google Antigravity entry point for the canonical `/expand` command specification.

## Canonical Specification (Single Source of Truth)

1. First, read the full command specification using `view_file`:
   - [.claude/commands/expand.md](../../.claude/commands/expand.md)
2. Follow all steps in `.claude/commands/expand.md` **exactly in order**, applying the Antigravity tool mappings below.

## Antigravity Runtime & Tool Adaptations

- **File Reading**: Use `view_file` to read `01-candidate-profile.md`, `02-behavioral-profile.md`, and documents under `documents/` (including PDFs).
- **GitHub & Web Discovery**:
  - Use `read_url_content` and `search_web` (or `github-mcp-server` tools if searching GitHub repositories) to inspect the user's public GitHub profile, repositories, READMEs, and course syllabi.
- **Applying Confirmed Additions**:
  - Present the proposed additions first, wait for user confirmation (using `ask_question` or chat confirmation), and apply confirmed items with `replace_file_content`.
