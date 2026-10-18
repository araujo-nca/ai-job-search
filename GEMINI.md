# Google Antigravity Workspace Rules — AI Job Search

This workspace is adapted for **Google Antigravity** while preserving 100% upstream compatibility with `MadsLorentzen/ai-job-search`.

## 1. Candidate Profile & Verification Checklist (`CLAUDE.md`)

@[Candidate Profile and Verification Checklist](CLAUDE.md)

---

## 2. Skill & Slash Command Discovery (`.agents/skills.json`)

Antigravity discovers all workspace skills and slash commands via [.agents/skills.json](.agents/skills.json), which registers three directories:
1. **[.agents/skills/](.agents/skills/)** — Job-portal search CLIs (`linkedin-search`, `freehire-search`, `jobbank-search`, `jobdanmark-search`, `jobindex-search`, `jobnet-search`, plus any added via `/add-portal`). **Never place non-portal skills in `.agents/skills/`**, because `/scrape` and `/add-portal` iterate over `.agents/skills/*/SKILL.md` expecting portal CLIs.
2. **[.claude/skills/](.claude/skills/)** — Core methodology skills (`job-application-assistant`, `scrape` in `job-scraper/`, and `upskill`).
3. **[.agents/command-skills/](.agents/command-skills/)** — Thin-pointer Antigravity skills exposing all 12 `.claude/commands/*.md` workflows as first-class slash commands and semantic skills (`/setup`, `/apply`, `/rank`, `/interview`, `/outcome`, `/expand`, `/add-portal`, `/add-template`, `/html-report`, `/gmail-sync`, `/notion-sync`, `/reset`).

---

## 3. Claude Code to Google Antigravity Tool Mapping

Whenever a canonical workflow in `.claude/commands/*.md` or `.claude/skills/**/*.md` references a Claude Code tool or environment variable, translate it to the native Antigravity equivalent:

| Claude Code Reference | Google Antigravity Equivalent | Mandatory Execution Rules |
| :--- | :--- | :--- |
| `Read` | `view_file` | Supports text files **and binary PDF/image files natively**. For PDF visual inspection (`/apply` Step 5b, `/setup` Path A), call `view_file` with `AbsolutePath` only (omit `StartLine` and `EndLine`). |
| `Write` | `write_to_file` | Set `Overwrite: true` when creating or replacing a file. |
| `Edit` | `replace_file_content` | Use exact `StartLine`, `EndLine`, `TargetContent`, and `ReplacementContent`. |
| `Glob` / `Grep` | `run_command` (or file search) | Use `python -c "import pathlib..."` via `run_command` when listing or searching across directory trees. |
| `Bash` | `run_command` | **CRITICAL:** Antigravity's `run_command` **forbids `cd` commands**. Never run `cd <dir> && <cmd>`. Always pass the target directory via the `Cwd` parameter (e.g., `Cwd: "<workspace>/cv"` for `lualatex`, `Cwd: "<workspace>/cover_letters"` for `xelatex`). On Windows, use `python` (not `python3` unless aliased). |
| `WebFetch` | `read_url_content` | Fetches public URLs as Markdown. On HTTP 403 or empty JS shells, follow [.claude/skills/job-application-assistant/09-web-research.md](.claude/skills/job-application-assistant/09-web-research.md) (`python tools/robots_check.py "<URL>"` -> `curl` with browser headers, or `chrome-devtools-mcp` if permitted by `robots.txt`). |
| `WebSearch` | `search_web` | Performs web searches with optional domain prioritization. |
| `AskUserQuestion` | `ask_question` | Renders an interactive multiple-choice modal in Antigravity. Use for path selection in `/setup`, conflict resolution, and shortlist selection. |
| `Agent` (Subagents) | `invoke_subagent` | Dispatch subagents with `TypeName: "self"` (or `"research"`), `Model: "inherit"`, and a descriptive `Role`. For parallel batches (`/rank` Step 2, `/scrape` Step 1b), pass multiple entries in the `Subagents` array of a single `invoke_subagent` call, then end your turn and wait for reactive wakeup. |
| `${SCRATCHPAD}` | `<appDataDir>/brain/<conversation-id>/scratch` | Write temporary `curl` HTML downloads (`page.html`) or scratch scripts to the conversation's `scratch/` directory, never into the repository root. |

---

## 4. Antigravity Superpowers for Job Search

1. **Parallel Subagent Orchestration (`invoke_subagent`)**:
   - In `/apply` Step 3, spawn a fresh-context `Hiring Manager Reviewer` subagent (`TypeName: "self"`, `Model: "inherit"`) with the inline drafts so content critique is genuinely independent.
   - In `/rank` Step 2, dispatch multiple scoring subagents in a single `invoke_subagent` call (~5 jobs per subagent) to fetch and evaluate all candidate postings concurrently.
2. **Scheduled Job Scraping & Follow-Up Timers (`schedule` tool)**:
   - Use the `schedule` tool (one-shot timers or recurring cron expressions) when the user wants automated daily/weekly `/scrape` + `/rank` checks or `/outcome followup` reminders for quiet applications.
3. **Rich Artifacts (`<appDataDir>/brain/<conversation-id>/`)**:
   - Use Antigravity Artifacts (with Mermaid diagrams, tables, and carousels) when presenting extensive career strategy analyses, interview preparation packs, or visual comparisons. Always still write canonical repo files (`job_search_tracker.csv`, `upskill/report-*.md`, `documents/applications/...`) to their exact repo paths as required by the specs.
4. **Chrome DevTools MCP (`chrome-devtools-mcp`)**:
   - When investigating a new job portal in `/add-portal` or inspecting a JavaScript-rendered careers page whose `robots.txt` permits access, use `chrome-devtools-mcp` to inspect live XHR/JSON endpoints and rendered DOM.
