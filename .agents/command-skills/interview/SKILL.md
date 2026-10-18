---
name: interview
description: >-
  Prepare for a scheduled interview on a tracked application (/interview <company>):
  load the application archive, research the company and interviewers, build a
  stage-specific interview prep pack (likely questions, STAR mappings, bridge answers
  for gaps, questions to ask), and run an interactive mock interview roleplay.
  Triggers on: /interview, preparar para entrevista, interview prep, simulacao de
  entrevista, mock interview.
---

# /interview — Stage-Specific Interview Preparation & Mock Interview (Antigravity Skill)

This skill is the Google Antigravity entry point for the canonical `/interview` command specification.

## Canonical Specification (Single Source of Truth)

1. First, read the full command specification using `view_file`:
   - [.claude/commands/interview.md](../../.claude/commands/interview.md)
2. Follow all steps in `.claude/commands/interview.md` **exactly in order**, applying the Antigravity tool mappings below.

## Antigravity Runtime & Tool Adaptations

- **Reading Context & Frameworks**:
  - Use `view_file` to read `job_search_tracker.csv`, `documents/applications/<company>_<role>/*`, and the framework files (`07-interview-prep.md`, `01-candidate-profile.md`, `02-behavioral-profile.md`, `04-job-evaluation.md`).
- **Company & Interviewer Research**:
  - Use `search_web` and `read_url_content` (following `09-web-research.md` for HTTP 403 retries and claim verification).
- **Saving the Prep Pack**:
  - Always save the prep pack to `documents/applications/<company>_<role>/interview_prep_<stage>.md` using `write_to_file` as required by the specification.
  - You may also present a copy or interactive summary in the chat or as an Antigravity Artifact if helpful for the user during their interview prep.
