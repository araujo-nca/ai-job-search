---
name: reset
description: >-
  Reset candidate profile data in skill files, user documents in documents/, or both
  (/reset profile, /reset documents, /reset all) back to a blank state after explicit
  user confirmation. Triggers on: /reset, resetar perfil, limpar dados do perfil,
  reset profile data.
---

# /reset — Reset Candidate Profile Data (Antigravity Skill)

This skill is the Google Antigravity entry point for the canonical `/reset` command specification.

## Canonical Specification (Single Source of Truth)

1. First, read the full command specification using `view_file`:
   - [.claude/commands/reset.md](../../.claude/commands/reset.md)
2. Follow all steps in `.claude/commands/reset.md` **exactly in order**, applying the Antigravity tool mappings below.

## Antigravity Runtime & Tool Adaptations

- **Confirmation Gate (Step 2)**:
  - Never delete or overwrite any file until the user explicitly replies `RESET` after seeing the Step 1 preview.
- **File Operations (Step 3)**:
  - Use `write_to_file` (`Overwrite: true`) and `replace_file_content` to restore the blank templates while preserving `framework_version` frontmatter in all `.claude/skills/job-application-assistant/*.md` files.
  - When clearing `documents/` subfolders on Windows, use Python via `run_command` or shell commands carefully so `.gitkeep` and `documents/README.md` are preserved.
