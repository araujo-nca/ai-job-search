---
framework_version: 1.1.0
---

# Agent Guidelines: AI Job Search

This workspace is structured to manage job search activities, scraper tools, CVs, cover letters, and interview preparation.

## Thin-Pointer Design (Single Source of Truth)

To prevent duplication and configuration drift across different AI agent frameworks (Claude Code, Google Antigravity, Codex, Cursor, Gemini CLI, etc.), this workspace uses a unified thin-pointer design. All agent runtimes should load the canonical specifications and candidate profiles from the files and directories below:

1. **Personal Candidate Profile:**
   - The candidate profile, contact details, education, and target preferences are defined in [CLAUDE.md](CLAUDE.md) and the individual profile methodology files under [.claude/skills/job-application-assistant/](.claude/skills/job-application-assistant/) (specifically `01-*.md` etc.).
2. **Canonical Workflow Specifications:**
   - The step-by-step instructions and triggers for tasks (setup, scrape, rank, apply, upskill, interview, outcome, expand, add-portal, add-template, html-report, gmail-sync, notion-sync, reset) are defined in the [.claude/](.claude/) directory (specifically under `.claude/skills/` and `.claude/commands/`).
   - Do not duplicate these rules or specifications. Treat `.claude/` files as the single source of truth.
3. **Portal Search Skills:**
   - Job-portal search CLIs live under [.agents/skills/](.agents/skills/) in the portable Agent Skills format (with a `SKILL.md` per portal). Codex and Antigravity discover these automatically; the `/scrape` workflow in [.claude/skills/job-scraper/](.claude/skills/job-scraper/) orchestrates them.
4. **Google Antigravity Adaptation:**
   - [.agents/skills.json](.agents/skills.json) registers `.agents/skills` (portal CLIs), `.claude/skills` (`job-application-assistant`, `scrape`, `upskill`), and `.agents/command-skills` (thin-pointer skills for all 12 commands in `.claude/commands/*.md`).
   - [GEMINI.md](GEMINI.md) provides the complete Claude Code-to-Antigravity tool mapping (`view_file`, `write_to_file`, `replace_file_content`, `run_command` with `Cwd` and no `cd`, `read_url_content`, `search_web`, `ask_question`, `invoke_subagent`, `schedule`) and automatically includes [CLAUDE.md](CLAUDE.md).
