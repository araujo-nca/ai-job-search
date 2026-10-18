---
name: rank
description: >-
  Batch-score scraped jobs in job_scraper/seen_jobs.json against the candidate fit
  framework (/rank) using parallel subagents and return a ranked shortlist with
  strengths, gaps, deal-breaker vetoes, and deadline urgency. Triggers on: /rank,
  rank jobs, ranquear vagas, classificar vagas, triagem de vagas, shortlist jobs.
---

# /rank — Triage Scraped Jobs into a Ranked Shortlist (Antigravity Skill)

This skill is the Google Antigravity entry point for the canonical `/rank` command specification.

## Canonical Specification (Single Source of Truth)

1. First, read the full command specification using `view_file`:
   - [.claude/commands/rank.md](../../.claude/commands/rank.md)
2. Follow all steps in `.claude/commands/rank.md` **exactly in order**, applying the Antigravity tool mappings below.

## Antigravity Runtime & Tool Adaptations

- **Step 1 (Load State)**:
  - Run `python tools/rank_state.py candidates --limit 10` (plus any flags from `$ARGUMENTS`) via `run_command` with `Cwd` set to the workspace root. Never read `job_scraper/seen_jobs.json` directly into context.
- **Step 2 (Batch-Fetch and Score via Parallel Subagents)**:
  - Instead of Claude Code's `Agent` tool, use a single `invoke_subagent` tool call with multiple entries in the `Subagents` array (~5 jobs per subagent, each with `TypeName: "self"`, `Role: "Job Scoring Agent #N"`, `Model: "inherit"`).
  - Pass the job batch and compact scoring rubric inline in each subagent's `Prompt`, instructing each subagent to use `run_command` (for portal CLI `detail`), `read_url_content` (instead of `WebFetch`), and `search_web` (instead of `WebSearch`), and never to use `cd` inside `run_command`.
  - After invoking the parallel subagents, end your turn and wait for Antigravity's reactive wakeup when all scoring subagents finish.
- **Step 4 (Persist Scores)**:
  - Write the batch results via `python tools/rank_state.py record ...` and `python tools/rank_state.py sweep --write` using `run_command`.
