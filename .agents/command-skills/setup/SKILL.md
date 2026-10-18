---
name: setup
description: >-
  Run the profile onboarding setup (/setup) for the AI Job Search framework:
  import career documents from documents/, import a single CV, or run an interactive
  interview to populate CLAUDE.md, candidate profile files, CV/cover letter templates,
  and job search queries. Also supports /setup --section <name> (e.g. search).
  Triggers on: /setup, configurar perfil, setup profile, onboarding, importar curriculo,
  importar CV, atualizar perfil, configurar busca de vagas.
---

# /setup — Profile Onboarding (Antigravity Skill)

This skill is the Google Antigravity entry point for the canonical `/setup` command specification.

## Canonical Specification (Single Source of Truth)

1. First, read the full command specification using `view_file`:
   - [.claude/commands/setup.md](../../.claude/commands/setup.md)
2. Follow all steps in `.claude/commands/setup.md` **exactly in order**, applying the Antigravity tool mappings below.

## Antigravity Runtime & Tool Adaptations

- **File Reading & Scanning**:
  - Instead of `Read`, use `view_file` (note: `view_file` natively reads PDF files in `documents/cv/`, `documents/linkedin/`, `documents/diplomas/`, and `documents/references/` without needing external extractors).
  - Instead of `Glob` on `documents/**/*`, list files using `run_command` (e.g., `python -c "import pathlib; print([str(p) for p in pathlib.Path('documents').rglob('*') if p.is_file() and p.name != '.gitkeep'])"`).
- **Interactive Questions**:
  - Use `ask_question` when presenting structured multiple-choice decisions (such as choosing between Path A, Path B, or Path C in Step 0, or resolving `[keep]` / `[replace]` / `[manual]` conflicts in Step A6).
- **File Editing & Writing**:
  - Instead of `Edit`, use `replace_file_content`.
  - Instead of `Write`, use `write_to_file` (`Overwrite: true`).
- **Portal Configuration for Non-Danish Markets (Brazil / Remote / Global)**:
  - During Search Configuration (Path C Section 9 / Step A7), if the user is searching outside Denmark (e.g., Brazil, Remote, US/EU), recommend setting `enabled: false` in the frontmatter of the four Danish-only portals (`jobbank-search`, `jobdanmark-search`, `jobindex-search`, `jobnet-search`), keeping `linkedin-search` and `freehire-search` enabled, and using `/add-portal` for local boards.
