---
name: outcome
description: >-
  Record the result or progress of a job application (/outcome), draft follow-up
  messages for quiet applications (/outcome followup), or batch-resolve stale
  applications (/outcome stale). Updates job_search_tracker.csv and archives
  materials in documents/applications/<company>_<role>/outcome.md. Triggers on:
  /outcome, registrar resultado de vaga, atualizar status da candidatura, follow up
  candidatura, application outcome, application status.
---

# /outcome — Record Application Results & Follow-Ups (Antigravity Skill)

This skill is the Google Antigravity entry point for the canonical `/outcome` command specification.

## Canonical Specification (Single Source of Truth)

1. First, read the full command specification using `view_file`:
   - [.claude/commands/outcome.md](../../.claude/commands/outcome.md)
2. Follow all steps in `.claude/commands/outcome.md` **exactly in order**, applying the Antigravity tool mappings below.

## Antigravity Runtime & Tool Adaptations

- **File Operations**:
  - Use `view_file` to read `job_search_tracker.csv` and `documents/applications/<company>_<role>/outcome.md`.
  - Use `write_to_file` or `replace_file_content` to update `job_search_tracker.csv` and `outcome.md`.
- **Interactive Selection**:
  - Use `ask_question` when asking the user to pick which open application to update or confirming batch stale resolutions.
- **Scheduled Follow-Up Reminders (Optional Antigravity Superpower)**:
  - If the user asks to be reminded to follow up in N days after recording an application or stage, you can use Antigravity's `schedule` tool (or recommend `/schedule`) to set a timer or recurring check for `/outcome followup`.
