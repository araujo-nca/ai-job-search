---
name: notion-sync
description: >-
  Publish a one-way, read-only view of ranked jobs and tracked applications to a
  Notion database (/notion-sync) via the Notion MCP server. Triggers on:
  /notion-sync, sincronizar com notion, exportar vagas para notion, sync jobs to notion.
---

# /notion-sync — Push Ranked Jobs and Applications to Notion (Antigravity Skill)

This skill is the Google Antigravity entry point for the canonical `/notion-sync` command specification.

## Canonical Specification (Single Source of Truth)

1. First, read the full command specification using `view_file`:
   - [.claude/commands/notion-sync.md](../../.claude/commands/notion-sync.md)
2. Follow all steps in `.claude/commands/notion-sync.md` **exactly in order**, applying the Antigravity tool mappings below.

## Antigravity Runtime & Tool Adaptations

- **Notion MCP Preflight (Step 1)**:
  - Check `<mcp_servers>` in your system prompt for the Notion MCP server. If Notion MCP is not connected in Antigravity, inform the user that they can configure the Notion MCP server (`https://mcp.notion.com/mcp`) in Antigravity's MCP settings (`mcp_config.json`) and stop cleanly with zero side effects.
