---
title: Enrich Ingested Content (EIC)
abbreviation: EIC
category: ingestion
---
Improve captured content through transcript correction, summarization, and knowledge linking.

## Input
- Target note file
- Long articles may need chunking to avoid partial processing
- Original content with potential grammar/transcript errors

## Output
- Set `status: processed` per `obsidian-yaml-frontmatter` skill
- Add link to source article / embed video
- Summary section added at beginning
- Improved formatting and structure
- Updated Journal/{{YYYY-MM-DD}}.md with article link in Learnings section

## Main Process
```
1. IMPROVE CAPTURE & TRANSCRIPT (ICT)
   - Fix all grammar or transcript errors
   - Translate to Korean for Clippings
   - Remove extra/duplicated newlines
   - Add chapters using heading3 (###)
   - Add formatting (lists, highlights)
   - Keep overall length equal to original
   - Set status property to processed

2. ADD SUMMARY FOR THREAD
   - Add Summary section at beginning (##)
   - Write catchy summaries for Threads sharing
   - Use quotes verbatim to convey author's voice
   - Don't add highlights in summary

3. ENRICH USING TOPICS
   - Link related KB topics (existing only)
   - Add one-line summary to relevant KB topics
   - Link to related summaries (books, etc.)

4. UPDATE JOURNAL
   - Extract date from output filename (YYYY-MM-DD format)
   - Add entry to Journal/{{YYYY-MM-DD}}.md in Learnings section
   - Format: "- [One-line key insight] [[AI/Articles/{{filename}}]]"
   - Use article's main takeaway or key learning point
   - Write in Korean for Korean articles, English for English articles
   - Add to task frontmatter output field
```

## Caveats
### No Duplicates Allowed
Check the duplicated task before processing
- If the duplicated task is found, update the task status to 'IGNORE' with the reason

### Content Completeness

⚠️ **CRITICAL**: ICT section must be COMPLETE - not truncated

**Common failure pattern:**
- Agent starts ICT section
- Hits token/context limit mid-processing
- ICT cuts off mid-sentence: "Since I last wrote at the beginning of the summer, my methodol..."
- Agent marks status as PROCESSED anyway ❌ WRONG

**Prevention measures:**
1. **Check article length FIRST** before starting
2. **If source >3000 words**, process in chunks OR request context extension
3. **VERIFY ICT ends at natural stopping point** (end of paragraph/section, not mid-sentence)
4. **Self-check before marking PROCESSED**: "Does the last paragraph in ICT feel complete?"
5. **If truncated**, FINISH it before updating status to PROCESSED

**Quality verification:**
- ICT section should have multiple ### subsections (not just one incomplete section)
- Last sentence should end with proper punctuation, not "..." or cut-off text
- Length should be comparable to original source (not 30-50% shorter due to truncation)

**If you cannot complete full ICT:**
- Mark task as NEEDS_INPUT explaining length/complexity issue
- DO NOT mark PROCESSED with incomplete work

### Rename Output Filenames
**Only change output filename; changing input filename may trigger duplicated task**
* Convert " " (curly/typographic quotes) to " (straight quote)
   * Same for single quotes
* Quote " with ' when adding to frontmatters (use relevant [[_Settings_/Skills/obsidian-yaml-frontmatter/SKILL|SKILL]])
* Remove incomplete words -- 40살 전에 알았다면 `얼마ᄂ`
* Remove `Readwise` at the end

### Formatting Standards
- Follow `obsidian-markdown-structure` skill (H3 for chapters, summary first)
- Limit highlights to essence (one per chapter)
- Overall length should equal original

### Journal Updates
**Adding article links to Journal**:
- Extract date from output filename (e.g., "2025-11-11" from "2025-11-11 Article Title - Agent.md")
- Update Journal/{{YYYY-MM-DD}}.md in the **Learnings section**
- If Journal file doesn't exist, create it using Journal template
- If Learnings section doesn't exist, create it
- Format: `- [Concise key insight or main takeaway] [[AI/Articles/{{filename}}]]`
- Keep learning statement to 1 sentence
- Match language: Korean for Korean articles, English for English articles
- Example: `- AI 모델 평가 시 실제 업무 기반 테스트가 표준 벤치마크보다 중요함 [[AI/Articles/2025-11-11 Giving your AI a Job Interview - Claude Code]]`
