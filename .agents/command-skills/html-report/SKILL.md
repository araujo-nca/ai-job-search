---
name: html-report
description: >-
  Generate a self-contained offline HTML dashboard (/html-report) from
  job_search_tracker.csv and documents/applications/*/outcome.md with inline SVG
  charts (status, sector, channel, funnel) and a filterable applications table.
  Triggers on: /html-report, gerar relatorio html, dashboard de candidaturas,
  application tracker dashboard.
---

# /html-report — Generate Application Tracker Dashboard (Antigravity Skill)

This skill is the Google Antigravity entry point for the canonical `/html-report` command specification.

## Canonical Specification (Single Source of Truth)

1. First, read the full command specification using `view_file`:
   - [.claude/commands/html-report.md](../../.claude/commands/html-report.md)
2. Follow all steps in `.claude/commands/html-report.md` **exactly in order**, applying the Antigravity tool mappings below.

## Antigravity Runtime & Tool Adaptations

- **Data Collection & HTML Generation**:
  - Read `job_search_tracker.csv` and `documents/applications/*/outcome.md` using `view_file`.
  - Write the self-contained HTML file to `reports/application-dashboard.html` (or the user-supplied path) using `write_to_file` (`Overwrite: true`).
  - Provide a clickable `[application-dashboard.html](file:///...)` link in your response so the user can open it directly from Antigravity.
