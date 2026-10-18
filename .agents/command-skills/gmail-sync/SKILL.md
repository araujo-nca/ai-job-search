---
name: gmail-sync
description: >-
  Scan Gmail via MCP for application status updates (/gmail-sync) such as interview
  invitations, assessments, offers, and rejections, and propose batch updates to
  job_search_tracker.csv and outcome.md for user approval. Triggers on: /gmail-sync,
  sincronizar gmail, checar emails de vagas, sync application status from gmail.
---

# /gmail-sync — Sync Application Status from Gmail (Antigravity Skill)

This skill is the Google Antigravity entry point for the canonical `/gmail-sync` command specification.

## Canonical Specification (Single Source of Truth)

1. First, read the full command specification using `view_file`:
   - [.claude/commands/gmail-sync.md](../../.claude/commands/gmail-sync.md)
2. Follow all steps in `.claude/commands/gmail-sync.md` **exactly in order**, applying the Antigravity tool mappings below.

## Antigravity Runtime & Tool Adaptations

- **Gmail MCP Check (Step 0)**:
  - Check your available MCP servers (`<mcp_servers>`) for a Gmail MCP server. If none is configured in Antigravity (`mcp_config.json`), inform the user how to add a Gmail MCP server in Antigravity Settings -> Skills & Customizations -> MCP Servers and stop cleanly without attempting IMAP or shell workarounds.
- **Batch Approval**:
  - Always present proposed status changes citing the source email and wait for explicit user approval (via `ask_question` or chat confirmation) before writing to `job_search_tracker.csv` or `outcome.md` with `replace_file_content` / `write_to_file`.
