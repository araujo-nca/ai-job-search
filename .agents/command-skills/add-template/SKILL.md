---
name: add-template
description: >-
  Register, list, or switch custom CV and cover letter templates (/add-template,
  /add-template --list, /add-template --use <name>) using LaTeX, Typst, or any
  CLI-compilable PDF toolchain. Triggers on: /add-template, adicionar template de
  curriculo, mudar template de CV, custom CV template, custom cover letter template.
---

# /add-template — Register or Switch Custom CV / Cover Letter Templates (Antigravity Skill)

This skill is the Google Antigravity entry point for the canonical `/add-template` command specification.

## Canonical Specification (Single Source of Truth)

1. First, read the full command specification using `view_file`:
   - [.claude/commands/add-template.md](../../.claude/commands/add-template.md)
2. Follow all steps in `.claude/commands/add-template.md` **exactly in order**, applying the Antigravity tool mappings below.

## Antigravity Runtime & Tool Adaptations

- **File Operations**:
  - Use `view_file` to inspect existing templates and `templates/**/TEMPLATE.md`.
  - Use `write_to_file` and `replace_file_content` to create template files under `templates/` and manage the `ACTIVE-TEMPLATE` block in `05-cv-templates.md` / `06-cover-letter-templates.md`.
  - Note: If modifying `05-cv-templates.md` or `06-cover-letter-templates.md`, remember that `tools/check_framework_version.py` checks `framework_version` in their frontmatter when committing changes.
- **Test Compile (Step 4)**:
  - Use `run_command` with `Cwd` set to the temporary build directory (never use `cd` inside `CommandLine`), and inspect the resulting PDF with `view_file`.
