"""Guards for the Google Antigravity adaptation (.agents/skills.json, .agents/command-skills/, GEMINI.md).

Ensures that:
1. .agents/skills.json registers .agents/skills, .claude/skills, and .agents/command-skills.
2. Every canonical command in .claude/commands/*.md has a matching thin-pointer
   skill in .agents/command-skills/<name>/SKILL.md with valid YAML frontmatter
   and a pointer back to .claude/commands/<name>.md.
3. .agents/skills/ remains strictly for portal search CLIs (*-search) so /scrape
   and /add-portal globs are not polluted by command skills.
4. GEMINI.md exists, includes CLAUDE.md, and documents the Antigravity tool mapping.
"""

import json
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_JSON = REPO_ROOT / ".agents" / "skills.json"
CLAUDE_COMMANDS_DIR = REPO_ROOT / ".claude" / "commands"
AGY_COMMAND_SKILLS_DIR = REPO_ROOT / ".agents" / "command-skills"
PORTAL_SKILLS_DIR = REPO_ROOT / ".agents" / "skills"
GEMINI_MD = REPO_ROOT / "GEMINI.md"


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end == -1:
        return {}
    result: dict[str, str] = {}
    current_key: str | None = None
    for line in text[4:end].splitlines():
        if line and not line[0].isspace() and ":" in line:
            k, _, v = line.partition(":")
            current_key = k.strip()
            result[current_key] = v.strip()
        elif current_key and line.strip():
            result[current_key] = (result[current_key] + " " + line.strip()).strip()
    return result


class AntigravityAdaptationTests(unittest.TestCase):
    def test_skills_json_registers_all_skill_roots(self):
        self.assertTrue(SKILLS_JSON.is_file(), ".agents/skills.json is missing")
        data = json.loads(SKILLS_JSON.read_text(encoding="utf-8"))
        self.assertIsInstance(data, dict)
        entries = data.get("entries", [])
        paths = {entry.get("path") for entry in entries if isinstance(entry, dict)}
        self.assertEqual(
            paths,
            {".agents/skills", ".claude/skills", ".agents/command-skills"},
        )

    def test_every_claude_command_has_a_thin_pointer_antigravity_skill(self):
        commands = sorted(p.stem for p in CLAUDE_COMMANDS_DIR.glob("*.md"))
        self.assertGreaterEqual(len(commands), 12)
        for cmd in commands:
            with self.subTest(command=cmd):
                skill_path = AGY_COMMAND_SKILLS_DIR / cmd / "SKILL.md"
                self.assertTrue(
                    skill_path.is_file(),
                    f"Missing Antigravity command skill for /{cmd} at {skill_path}",
                )
                text = skill_path.read_text(encoding="utf-8")
                fm = parse_frontmatter(text)
                self.assertEqual(fm.get("name"), cmd)
                self.assertTrue(fm.get("description"), f"{skill_path}: empty description")
                self.assertIn(
                    f".claude/commands/{cmd}.md",
                    text,
                    f"{skill_path} must point to .claude/commands/{cmd}.md as single source of truth",
                )

    def test_portal_skills_dir_contains_only_portal_clis(self):
        non_portals = [
            p.name
            for p in PORTAL_SKILLS_DIR.iterdir()
            if p.is_dir() and not p.name.endswith("-search")
        ]
        self.assertEqual(
            non_portals,
            [],
            f"Non-portal directories found in .agents/skills/ (breaks /scrape glob): {non_portals}",
        )

    def test_gemini_md_includes_claude_md_and_tool_mappings(self):
        self.assertTrue(GEMINI_MD.is_file(), "GEMINI.md is missing")
        text = GEMINI_MD.read_text(encoding="utf-8")
        self.assertIn("(CLAUDE.md)", text)
        for tool_name in (
            "view_file",
            "write_to_file",
            "replace_file_content",
            "run_command",
            "read_url_content",
            "search_web",
            "ask_question",
            "invoke_subagent",
        ):
            self.assertIn(tool_name, text, f"GEMINI.md is missing mapping for {tool_name}")


if __name__ == "__main__":
    unittest.main()
