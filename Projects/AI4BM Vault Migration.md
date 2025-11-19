## Goal
Create a team vault for 
1. Dev collaboration (issue & feature mgmt)
2. Contents collaboration (draft review)

For contents,
1. Enable one-source-multi-use
2. Min. effort for update & maintenance

## Location
`~/dev/AI4BM`

## Structure
- `_Settings_`
	- Relevant prompts & workflows
	- `Issues/` - Issue tracking
	- `Goals/` - Team goals & milestones
- `Source` - Summary of source materials (for citation)
	- `Articles/` - Blog posts, web articles
	- `Books/` - Book summaries
	- `Videos/` - Video transcripts/summaries
	- `Research/` - Academic papers
- `Theory`
	- Concepts
	- Methods
- `Products`
	- `Blog/` - Drafts/ and Published/
	- `Lecture/` - Slides/, Notes/, Exercises/
	- `Video/` - Scripts/ and Published/

## Initialization
1. Copy relevant topics (exclude personal content)
	- Keep: Universal concepts, frameworks, methods
	- Remove: Journal entries, personal experiences, individual learnings
	- Topics: PKM, AI Agent, Obsidian
2. Copy relevant sources
	- Sources linked from topics above
	- Other relevant sources
	- Copy summary rather than full text / quotes
3. Move project folders
	- `AI4PKM`
4.  Move publish folders
	- `AI4PKM`
	- `AI4BM`
	- `AI4KW`

## Maintenance
### Challenges
Managing two vaults (personal vs. team)
- Source migration
- Content synchronization
- Link validation

### Workflows
1. **Content Update Protocol**
	- When theory/framework updates in personal vault → sync to team vault
	- Review for personal content before syncing
2. **Source Migration**
	- Auto-create summaries when EIC processes new articles
	- Batch migrate source summaries weekly
3. **Link Validation**
	- Run link checker before each sync
	- Fix broken wiki links immediately

## Success Metrics
- **Completeness**: All theory content migrated with proper attribution
- **Quality**: Zero broken wiki links in team vault
- **Usability**: New team member can contribute in <4 hours
- **Maintainability**: Sync personal→team takes <30min/week
