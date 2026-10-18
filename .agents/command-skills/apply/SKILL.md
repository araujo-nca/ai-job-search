---
name: apply
description: >-
  Run the full Drafter-Reviewer job application workflow (/apply <url or posting>):
  fetch and parse a job posting, evaluate fit against the candidate profile, draft a
  tailored LaTeX CV and cover letter, dispatch a Reviewer subagent to research the
  company and critique the drafts, revise, compile and visually verify PDFs, run ATS
  checks, and record the application. Triggers on: /apply, candidatar a vaga, aplicar
  para vaga, criar curriculo e carta para vaga, apply to job, tailor CV and cover letter.
---

# /apply — Drafter-Reviewer Job Application Workflow (Antigravity Skill)

This skill is the Google Antigravity entry point for the canonical `/apply` command specification.

## Canonical Specification (Single Source of Truth)

1. First, read the full command specification using `view_file`:
   - [.claude/commands/apply.md](../../.claude/commands/apply.md)
2. Follow all steps in `.claude/commands/apply.md` **exactly in order**, applying the Antigravity tool mappings below.

## Antigravity Runtime & Tool Adaptations

- **Step 0 (Fetching the Posting)**:
  - For portal CLIs, use `run_command` with `Cwd` set to the workspace root: `bun run .agents/skills/<portal-skill>/cli/src/cli.ts detail "<URL>" --format plain`.
  - Instead of `WebFetch`, use `read_url_content`.
  - If `read_url_content` returns HTTP 403 or an empty JS shell, follow [.claude/skills/job-application-assistant/09-web-research.md](../../.claude/skills/job-application-assistant/09-web-research.md): run `python tools/robots_check.py "<URL>"` first, then retry with `curl` writing to the session scratchpad directory (`<appDataDir>/brain/<conversation-id>/scratch/page.html`) by setting `Cwd` on `run_command` (never use `cd` inside `CommandLine`). If `chrome-devtools-mcp` is available and needed for a JS-rendered careers page permitted by `robots.txt`, you may also inspect the rendered DOM with it.
- **Step 3 (REVIEWER — Subagent Dispatch)**:
  - Instead of Claude Code's `Agent` tool, call `invoke_subagent` with:
    - `TypeName`: `"self"`
    - `Role`: `"Hiring Manager Reviewer"`
    - `Model`: `"inherit"`
    - `Prompt`: the exact inline reviewer prompt from Step 3 of `.claude/commands/apply.md` (with `<COMPANY>`, `<ROLE>`, `<INSERT_JOB_POSTING_TEXT_HERE>`, `<INSERT_CV_DRAFT_HERE>`, and `<INSERT_COVER_LETTER_DRAFT_HERE>` populated inline).
  - After calling `invoke_subagent`, stop calling tools to end your turn; Antigravity will automatically wake you up when the reviewer subagent returns Part A and Part B feedback.
- **Step 4 (Revise Based on Feedback)**:
  - Apply Part A structured edits and Part B narrative revisions using `replace_file_content`.
- **Step 5 (Compile & Visually Inspect PDFs — MANDATORY)**:
  - **5a. Compile**: Never use `cd cv && ...` in `run_command` (`cd` is forbidden in Antigravity `run_command`). Instead:
    - Run `lualatex -interaction=nonstopmode main_<company>_<role>.tex` with `Cwd` set to `<workspace>/cv`.
    - Run `xelatex -interaction=nonstopmode cover_<company>_<role>.tex` with `Cwd` set to `<workspace>/cover_letters`.
  - **5b. Visual PDF Read**: Use `view_file` directly on `<workspace>/cv/main_<company>_<role>.pdf` and `<workspace>/cover_letters/cover_<company>_<role>.pdf` (omit `StartLine` and `EndLine` for binary PDF viewing).
  - **5c & 5d. Layout & ATS Verification**: Run `python tools/verify_pdf.py ...` and `python tools/verify_layout.py ...` with `Cwd` set to the workspace root.
