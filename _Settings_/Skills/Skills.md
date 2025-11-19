# AI4BM Skills

This directory contains Claude Code skills that enhance AI capabilities for PKM workflows.

## What are Skills?

Skills are specialized prompt packages that extend Claude Code's capabilities. Each skill is a self-contained module with instructions, examples, and helper scripts that Claude can use to perform specific tasks.

## Available Skills

### Core PKM Skills (Essential)

#### 1. obsidian-links
Format and validate Obsidian wiki links with proper filename and section conventions.

**Key Features:**
- Validates links resolve to existing files/sections
- Fixes broken links automatically
- Handles section links with character-perfect matching
- Ensures proper filename format (YYYY-MM-DD Title)

**Usage:** Automatically used when creating or checking wiki links in markdown files.

#### 2. obsidian-yaml-frontmatter
Manage YAML frontmatter properties with consistent formatting and value types.

**Key Features:**
- Standardizes property names (lowercase, consistent)
- Ensures tags are plain text (no # prefix in YAML)
- Validates date formats (YYYY-MM-DD)
- Maintains property ordering

**Usage:** Automatically used when creating or updating frontmatter in markdown files.

#### 3. obsidian-markdown-structure
Validate and enforce markdown document structure.

**Key Features:**
- Ensures frontmatter is at document top
- Validates heading hierarchy (no skipped levels)
- Checks content organization patterns
- Enforces content-after-frontmatter rule

**Usage:** Automatically used when creating or validating markdown files.

### Content Creation Skills

#### 4. markdown-to-docx
Convert markdown documents to Microsoft Word (.docx) format with proper formatting.

**Key Features:**
- Korean font support (Malgun Gothic)
- Bold/italic formatting preservation
- Nested list indentation (up to 5 levels)
- Professional styling with proper spacing

**Dependencies:**
```bash
pip install python-docx>=1.1.0
```

**Usage:** Call the skill when you need to export markdown to Word format.

#### 5. interactive-writing-assistant
Comprehensive support for the writing process from ideation through revision.

**Key Features:**
- Co-evolving outline and prose methodology
- Voice-based input processing
- Multiple writing styles (하루키, 윤광준, 구본형)
- PKM system integration for enriched content
- Korean translation support

**Usage:** Call when helping users write essays, articles, or creative pieces through interactive collaboration.

#### 6. youtube-transcript-skill
Download YouTube video transcripts when user provides a YouTube URL.

**Key Features:**
- Automatic transcript download using yt-dlp
- Fallback to Whisper transcription if needed
- Auto-installs dependencies on first use

**Usage:** Call when user wants to download/get/fetch a transcript from YouTube or get captions/subtitles from a video.

## Setup Instructions

### Initial Setup

Skills need to be symlinked from this vault to Claude Code's skills directory for Claude to recognize them:

```bash
# Navigate to skills directory
cd "/path/to/AI4BM/_Settings_/Skills"

# Create symlinks for each skill
for skill in obsidian-links obsidian-yaml-frontmatter obsidian-markdown-structure markdown-to-docx interactive-writing-assistant youtube-transcript-skill; do
    ln -sf "$PWD/$skill" ~/.claude/skills/"$skill"
done
```

### Verify Installation

Check that skills are properly linked:

```bash
ls -la ~/.claude/skills/
```

You should see symlinks pointing to this vault's Skills directory.

### Install Dependencies

Some skills require Python packages:

```bash
# For markdown-to-docx
pip install python-docx>=1.1.0

# For youtube-transcript-skill (auto-installs on first use)
# No manual installation needed
```

## How Skills Work

1. **Discovery**: Claude Code automatically discovers skills in `~/.claude/skills/`
2. **Activation**: Skills activate based on user requests or context
3. **Execution**: Claude follows the skill's instructions and uses provided tools
4. **Integration**: Skills can reference each other (e.g., obsidian-markdown-structure uses obsidian-yaml-frontmatter)

## Skill Development

Each skill follows this structure:

```
skill-name/
├── SKILL.md              # Main skill definition (required)
├── reference/            # Additional documentation (optional)
│   ├── examples.md
│   └── edge-cases.md
├── scripts/              # Helper scripts (optional)
│   └── helper.py
└── requirements.txt      # Python dependencies (if needed)
```

### Creating New Skills

1. Create a new directory in `_Settings_/Skills/`
2. Add `SKILL.md` with clear instructions and examples
3. Test with Claude Code
4. Document in this README
5. Symlink to `~/.claude/skills/`

## Additional Skills Available

These skills exist in the source vault but weren't copied (available if needed):

- **csv-analysis** - Analyze CSV files with auto-visualization
- **claude-d3js-skill** - Create interactive D3.js visualizations
- **markdown-slides** - Convert content to presentation slides (Deckset/Marp)
- **claude-epub-skill** - Convert markdown to EPUB ebooks
- **pdf-skill** - Comprehensive PDF manipulation toolkit
- **data-extraction** - Extract structured data from websites to CSV
- **markdown-video** - Convert slides to narrated MP4 videos (Korean TTS)

Contact vault maintainer if you need any of these additional skills.

## Troubleshooting

**Skill not recognized:**
- Verify symlink exists: `ls -la ~/.claude/skills/skill-name`
- Check symlink points to correct path
- Restart Claude Code session

**Skill errors:**
- Check dependencies are installed (`pip list`)
- Review skill's SKILL.md for requirements
- Check file permissions on skill directory

**Links not validating correctly:**
- Ensure obsidian-links skill is symlinked
- Verify target files exist in vault
- Check filename format matches YYYY-MM-DD pattern

## Team Collaboration Notes

- Skills are version-controlled in this vault
- Team members must run setup script after cloning
- Skill updates propagate automatically (symlinks)
- Dependencies should be documented in requirements.txt
- Test skills thoroughly before committing changes

---

For more information about Claude Code skills system, see: https://code.claude.com/docs/en/skills
