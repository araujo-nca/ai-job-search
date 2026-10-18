---
name: add-portal
description: >-
  Generate and register a new job-portal search CLI skill under .agents/skills/
  (/add-portal) for a local or international job board, or list installed portal
  skills (/add-portal --list). Investigates endpoints and robots.txt, scaffolds the
  Bun CLI and unit tests, and runs a live query. Triggers on: /add-portal, adicionar
  portal de vagas, novo site de vagas, criar scraper de portal, add job portal.
---

# /add-portal — Generate a Job-Portal Search Skill (Antigravity Skill)

This skill is the Google Antigravity entry point for the canonical `/add-portal` command specification.

## Canonical Specification (Single Source of Truth)

1. First, read the full command specification using `view_file`:
   - [.claude/commands/add-portal.md](../../.claude/commands/add-portal.md)
2. Follow all steps in `.claude/commands/add-portal.md` **exactly in order**, applying the Antigravity tool mappings below.

## Antigravity Runtime & Tool Adaptations

- **Portal Reconnaissance (Step 2)**:
  - Use `read_url_content` or `curl` via `run_command` to inspect search endpoints, JSON APIs, HTML structures, and `robots.txt` (`python tools/robots_check.py "<URL>"`).
  - If the portal renders listings via client-side JavaScript or XHR endpoints and `robots.txt` permits access, you can also use `chrome-devtools-mcp` (`navigate_page`, `list_network_requests`, `get_network_request`) to discover the underlying JSON API endpoints cleanly.
- **Scaffolding & Testing (Steps 3 & 4)**:
  - Read `.agents/skills/linkedin-search/` via `view_file` as the canonical zero-dependency reference.
  - Write the new portal skill under `.agents/skills/<name>/` using `write_to_file` (never in `.agents/command-skills/`).
  - Run `bun test` and live test queries using `run_command` with `Cwd` set appropriately (never use `cd` inside `CommandLine`).
  - When updating `.claude/settings.json` with the new portal permission, also update `ALLOWED_PERMISSIONS` in `tools/security_guards.py` so `python tools/security_guards.py` continues to pass.
