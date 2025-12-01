# AI4BM Team Vault

Knowledge vault for AI for Better Me (AI4BM) project - team collaboration on theory, sources, and content production.

## Purpose

1. **Dev Collaboration**: Issue tracking, feature management, team goals
2. **Content Collaboration**: Draft review, multi-format content production
3. **One-Source-Multi-Use**: Theory → Blog/Lecture/Video
4. **Knowledge Foundation**: Shared concepts, methods, and source materials

## Structure

### `_Settings_/`
Infrastructure and configuration
- `Prompts/` - AI agent prompts for content workflows
- `Templates/` - Document templates (source summaries, etc.)
- `Workflows/` - Multi-step process definitions
- `Skills/` - Claude Code skills for enhanced AI capabilities
- `Issues/` - Bug reports, improvement requests
- `Goals/` - Team goals and milestones

### `Source/`
Summaries of source materials for citation
- Articles, books, videos, research papers
- 1-2 paragraph summaries with attribution
- Tracks what theory/products cite each source

### `Theory/`
Core concepts and methods
- `Concepts/` - Framework definitions, principles
- `Methods/` - How-to guides, methodologies
- Content is universal (no personal experiences)

### `Publish/`
Content outputs in various formats
- `Blog/` - Drafts/ and Published/ blog posts
- `Lecture/` - Slides/, Notes/, Exercises/
- `Video/` - Scripts/ and Published/ videos
- `Talks/` - Presentation slides and materials

### `Projects/`
Project planning and specifications
- Feature requests, architecture docs
- Migration plans, development specs

## Content Guidelines

### What Belongs Here
✅ Universal concepts and frameworks
✅ Best practices (anonymized if needed)
✅ Published source summaries
✅ Team-reviewed theory articles
✅ Production-ready content (blog/lecture/video/talks)

### What Stays in Personal Vaults
❌ Personal journal entries and daily logs
❌ First-person narratives and experiences
❌ Meeting notes with individuals
❌ Personal tool configurations
❌ Draft thoughts and unprocessed captures

## Wiki Link Convention

- Use simplified filenames: `[[PKM Framework]]` not `[[2025-11-18 PKM Framework]]`
- Dates go in frontmatter `created` field
- Always link to existing files (no broken links)
- Link to original sources, not topic indices

## Getting Started

1. **Clone this repository**
   ```bash
   git clone <repository-url>
   cd AI4BM
   ```

2. **Run initialization script** (sets up Claude Code skills and dependencies)
   ```bash
   ./_Settings_/Scripts/init_vault.sh
   ```

3. **Open in Obsidian** (`.obsidian/` settings included)

4. **Review framework**
   - `Theory/` content to understand AI4PKM concepts
   - `_Settings_/Templates/` for contribution formats
   - `_Settings_/Skills/Skills.md` for available AI capabilities

5. **Start contributing**
   - Add sources to `Source/` before citing in theory
   - Draft content in appropriate `Publish/` subfolder

### AI Agent Configuration

This vault includes configuration files for AI agents:
- `AGENTS.md` - Generic rules for all AI agents
- `CLAUDE.md` - Claude Code-specific rules
- `GEMINI.md` - Gemini-specific configuration

These files are automatically loaded by AI agents to ensure consistent vault interaction patterns.

## Maintenance

- **Content updates**: Sync from personal vaults weekly
- **Source migration**: Add summaries as articles are processed
- **Link validation**: Check before committing changes
- **Review process**: Drafts → team review → Published/

## Questions?

See `Projects/AI4PKM/AI4BM Vault Migration.md` for detailed migration plan and rationale.
