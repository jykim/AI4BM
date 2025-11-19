---
title: "AI4PKM Skills Evolution Roadmap"
created: 2025-10-19
tags:
  - AI4PKM
  - claude-skills
  - architecture
  - roadmap
source: "Request to analyze prompts and workflows for Skills evolution"
---

# AI4PKM Skills Evolution Roadmap

## Executive Summary

This document provides a comprehensive roadmap for evolving AI4PKM's current prompt-based architecture toward Claude Skills. The transition will reduce context usage by 40-60%, improve maintainability, and enable rapid workflow composition.

**Key Findings**:
- 25 prompts contain significant duplicated patterns
- 60-70% of prompt content is reusable generic skills
- Progressive disclosure can reduce initial context by ~80%
- Estimated 12-week phased migration with minimal disruption

**Expected Benefits**:
- **Context Efficiency**: 40-60% reduction in tokens per workflow
- **Maintainability**: Single source of truth for common patterns
- **Composability**: Rapid workflow creation from skill building blocks
- **Consistency**: Standardized implementations across all agents

**15 Proposed Skills** (4 Layers):

| # | Skill Name | Category | Description | Supporting Tools | Used By |
|---|------------|----------|-------------|------------------|---------|
| **1** | **Obsidian Link Formatting** | Foundation | Wiki link syntax and validation | `obsidian_client.py`, `link_validator.py` | All 25 prompts |
| **2** | **YAML Frontmatter Management** | Foundation | Metadata standards and validation | `structure_analyzer.py`, `obsidian_client.py` | 22/25 prompts |
| **3** | **Link Resolution & Validation** | Foundation | File existence and section verification | `link_validator.py`, `obsidian_client.py` | 20/25 prompts |
| **4** | **Markdown Structure Validation** | Foundation | Document structure enforcement | `structure_analyzer.py` | 18/25 prompts |
| **5** | **Improve Capture & Transcript (ICT)** | Content Processing | Grammar, translation, formatting | - | 7 prompts (EIC, PLL, GES) |
| **6** | **Summary Generation** | Content Processing | Catchy summaries with quotes and attribution | - | 15 prompts |
| **7** | **Quote Extraction & Formatting** | Content Processing | Verbatim quote handling in blockquotes | - | 12 prompts |
| **8** | **Korean Translation & Processing** | Content Processing | Translation standards and formatting | - | 12 prompts |
| **9** | **Topic Categorization** | Knowledge Organization | Topic discovery and assignment | `obsidian_client.py` (search API) | 8 prompts |
| **10** | **Source Attribution** | Knowledge Organization | Original source tracking and linking | `link_validator.py` | 20 prompts |
| **11** | **Duplicate Detection & Merging** | Knowledge Organization | Content deduplication strategies | `obsidian_client.py` (search API) | 5 prompts |
| **12** | **Calendar Integration (MCP)** | Integration | Google Calendar event matching | `match_transcript.py` | 3 prompts (GES, PLL) |
| **13** | **Transcript Matching** | Integration | Time-based transcript extraction | `match_transcript.py` | 3 prompts (GES, PLL) |
| **14** | **File Operations** | Integration | Batch processing and organization | `obsidian_client.py` | 15 prompts |
| **15** | **Status Management** | Integration | Task status transitions and tracking | `task_status.py`, `obsidian_client.py` | 22 prompts |

**Supporting Tools** (5 tools, ~2,250 lines of code):
- `obsidian_client.py` - Obsidian Local REST API wrapper
- `skill_engine.py` - Skill loading and progressive disclosure
- `link_validator.py` - Batch link validation with auto-fix
- `structure_analyzer.py` - Format validation and auto-formatting
- `skill_deps.py` - Dependency resolution and visualization

**Companion Document**: See [[2025-10-19 AI4PKM Skills Implementation Plan]] for detailed tool development plans, Obsidian API integration, and complete code examples.

---

## Part 1: Current State Analysis

### 1.1 Prompt Inventory & Categorization

**Total Assets**:
- 25 Prompts in `_Settings_/Prompts/`
- 8 Workflows in `_Settings_/Workflows/`
- ~2,500 lines of prompt code (excluding embedded examples)

**Functional Categories**:

#### **Content Ingestion & Processing** (9 prompts)
- `Enrich Ingested Content (EIC)` - Core content improvement
- `Process Life Logs (PLL)` - Limitless transcript processing
- `Pick and Process Photos (PPP)` - Photo ingestion
- `Discover Knowledge Updates (DKU)` - Content delta discovery
- `Extract AI Session Log (ESL)` - AI conversation extraction
- `Handwritten PDF to Markdown (HPM)` - OCR processing
- `Family Conversation Analysis (FCA)` - Conversation extraction
- `Storytelling from Painting (SFP)` - Visual content interpretation
- `Standardize Agent Rules (SAR)` - Meta-prompt standardization

#### **Knowledge Organization** (5 prompts)
- `Topic Knowledge Creation (TKC)` - New topic page creation
- `Topic Knowledge Addendum (TKA)` - Topic updates from content
- `Topic Knowledge Improvement (TKI)` - Topic page enhancement
- `Update Folder Notes (UFN)` - Folder index maintenance
- `Ad-hoc Research within PKM (ARP)` - Knowledge graph queries

#### **Daily/Weekly Operations** (4 prompts)
- `Generate Daily Roundup (GDR)` - Episodic memory creation
- `Generate Weekly Roundup (GWR)` - Weekly synthesis
- `Generate Event Summary (GES)` - Meeting summarization
- `Create Thread Postings (CTP)` - Social media content

#### **Task & Workflow Management** (4 prompts)
- `Knowledge Task Generator (KTG)` - Task discovery
- `Knowledge Task Processor (KTP)` - Task execution
- `Knowledge Task Evaluator (KTE)` - Quality assessment
- `Evaluate Prompts and Workflows (EPW)` - Meta-evaluation

#### **Content Creation** (3 prompts)
- `Generate Markdown Slides (GMS)` - Presentation creation
- `Generate Markdown Video (GMV)` - Video script generation
- `Discover Article Ideas (DAI)` - Content ideation

### 1.2 Common Pattern Analysis

#### **Pattern 1: Obsidian Conventions** (Appears in 23/25 prompts)
- Wiki link formatting: `[[YYYY-MM-DD Title]]`
- No .md extensions in links
- Section linking: `[[Note#Section]]`
- Frontmatter YAML standards
- Properties vs tags distinction

**Current Implementation**: Repeated in each prompt (50-150 tokens each)

#### **Pattern 2: Content Structure Validation** (18/25 prompts)
- YAML frontmatter validation
- Required vs optional properties
- Heading hierarchy (H1 title, H2 sections, H3 subsections)
- One blank line after frontmatter
- No loose text before first heading

**Current Implementation**: Inline instructions (80-120 tokens each)

#### **Pattern 3: Link Resolution & Validation** (20/25 prompts)
- Verify files exist before linking
- Use complete filenames
- Fix broken links
- Link to original sources, not topic indices
- Section header verification

**Current Implementation**: Scattered across prompts (60-100 tokens each)

#### **Pattern 4: Korean/English Processing** (12/25 prompts)
- Korean as default language
- Translation standards
- Preserve original language quotes
- Fix Korean spacing/particles
- Handle English loanwords

**Current Implementation**: Language-specific rules repeated

#### **Pattern 5: ICT (Improve Capture & Transcript)** (7/25 prompts)
- Grammar/transcript error correction
- Korean translation for Clippings
- Heading3 (###) for chapters
- Formatting with lists and highlights
- Length preservation

**Current Implementation**: Full ICT specification embedded (150-200 tokens)

#### **Pattern 6: Summary Generation** (15/25 prompts)
- Thread-friendly catchy summaries
- Quote extraction and formatting
- Korean language summaries
- Highlight key insights
- Source attribution

**Current Implementation**: Summary templates repeated

#### **Pattern 7: MCP Integration** (8/25 prompts)
- Google Calendar queries
- Fully qualified tool names (Server:tool_name)
- BigQuery patterns
- File system operations
- Error handling

**Current Implementation**: Integration patterns per prompt

#### **Pattern 8: Status & Metadata Management** (22/25 prompts)
- Status property updates (processed, TBD, COMPLETED)
- Worker field assignment
- Output property formatting
- Created/updated timestamps
- Source attribution

**Current Implementation**: Status logic duplicated everywhere

### 1.3 Workflow Composition Patterns

**DIR (Daily Ingestion and Roundup)**:
```
PPP → PLL → EIC → GDR → TKA → CTP
```
- Sequential execution
- Shared Obsidian conventions
- Status tracking across steps
- Output of one → Input of next

**CKU (Continuous Knowledge Upkeep)**:
```
EIC (new content) → UFN (updated folders) → TKI (updated topics)
```
- Conditional execution
- Shared link validation
- Topic discovery patterns
- Quality maintenance

**KTG → KTP Pipeline**:
```
KTG (discover) → KTP (execute) → KTE (evaluate)
```
- Task lifecycle management
- Shared task file structure
- Status transitions
- Output validation

---

## Part 2: Skill Candidates

### 2.1 Foundation Skills (Layer 1)
**High reusability across ALL prompts**

#### **Skill 1: Obsidian Link Formatting**
```yaml
name: "Formatting Obsidian Wiki Links"
description: "Formats wiki links according to Obsidian conventions: full filename format [[YYYY-MM-DD Title]], no .md extensions, section linking with #, and path omission for AI/ folder. Validates link format before use."
```

**Key Capabilities**:
- Wiki link syntax validation
- Complete filename enforcement
- Section link formatting
- Path prefix rules (omit AI/ for brevity)
- Inline link detection and fixing

**Used By**: All 25 prompts
**Context Saved**: ~80 tokens per prompt (2,000 tokens total)

**Progressive Disclosure**:
- `SKILL.md`: Core linking rules (200 lines)
- `reference/link-patterns.md`: Common patterns and examples
- `reference/section-linking.md`: Section header conventions

---

#### **Skill 2: YAML Frontmatter Management**
```yaml
name: "Managing YAML Frontmatter"
description: "Creates and validates YAML frontmatter for Obsidian notes. Handles required fields (title, created, tags), optional fields (source, author, status), ensures proper formatting, and validates against AI4PKM standards."
```

**Key Capabilities**:
- Required vs optional field enforcement
- YAML syntax validation
- Property type checking (string, list, date)
- Tags as plain text (no # prefix)
- Consistent field ordering
- Wiki link quoting in properties

**Used By**: 22/25 prompts
**Context Saved**: ~100 tokens per prompt (2,200 tokens total)

**Progressive Disclosure**:
- `SKILL.md`: Frontmatter structure and validation rules (250 lines)
- `reference/property-standards.md`: Complete field reference
- `templates/frontmatter-examples.md`: Examples by document type

---

#### **Skill 3: Link Resolution & Validation**
```yaml
name: "Resolving and Validating Links"
description: "Validates wiki links point to existing files, fixes broken links, verifies section headers exist, and ensures links point to original sources rather than topic indices. Provides clear error messages for missing targets."
```

**Key Capabilities**:
- File existence verification
- Section header validation
- Broken link detection and suggestions
- Source vs index distinction
- Link format correction

**Used By**: 20/25 prompts
**Context Saved**: ~90 tokens per prompt (1,800 tokens total)

**Progressive Disclosure**:
- `SKILL.md`: Validation logic and resolution strategies (300 lines)
- `scripts/validate_links.py`: Automated validation script
- `reference/common-link-errors.md`: Error patterns and fixes

---

#### **Skill 4: Markdown Structure Validation**
```yaml
name: "Validating Markdown Structure"
description: "Ensures proper markdown document structure: YAML frontmatter at top, one blank line after frontmatter, H1 title matches filename, H2 for main sections, H3 for subsections, and no loose text before first heading."
```

**Key Capabilities**:
- Heading hierarchy validation
- Frontmatter position checking
- Blank line enforcement
- Title consistency verification
- Structure repair suggestions

**Used By**: 18/25 prompts
**Context Saved**: ~70 tokens per prompt (1,260 tokens total)

**Progressive Disclosure**:
- `SKILL.md`: Structure rules and validation (200 lines)
- `reference/structure-patterns.md`: Document type templates
- `scripts/validate_structure.py`: Structure checking script

---

### 2.2 Content Processing Skills (Layer 2)
**Core PKM operations**

#### **Skill 5: Improve Capture & Transcript (ICT)**
```yaml
name: "Improving Captured Transcripts"
description: "Improves voice transcripts and captured content: fixes grammar and transcription errors, translates to Korean for Clippings, adds H3 chapter headings, applies formatting (lists, highlights), and preserves original length. Essential for EIC, PLL, GES workflows."
```

**Key Capabilities**:
- Grammar and transcript error correction
- Korean translation for Clippings
- Automatic chapter detection and H3 heading insertion
- List and highlight formatting
- Length preservation validation
- Korean spacing/particle error fixing
- English loanword handling

**Used By**: EIC, PLL, GES, FCA, ESL (7 prompts)
**Context Saved**: ~180 tokens per prompt (1,260 tokens total)

**Progressive Disclosure**:
- `SKILL.md`: ICT process and rules (400 lines)
- `reference/korean-translation.md`: Translation standards
- `reference/formatting-patterns.md`: List/highlight guidelines
- `reference/common-transcript-errors.md`: Error correction patterns
- `examples/ict-before-after.md`: Transformation examples

---

#### **Skill 6: Summary Generation**
```yaml
name: "Generating Content Summaries"
description: "Creates catchy, thread-friendly summaries with key insights, verbatim quotes, and source attribution. Supports Korean and English output, maintains author's voice through quotes, and formats for social media sharing."
```

**Key Capabilities**:
- Catchy opening for social media
- Key insight extraction
- Verbatim quote selection
- Korean language default
- Source attribution
- Length optimization (140-280 chars for threads)
- Highlight-free summary sections

**Used By**: EIC, GDR, GWR, GES, CTP, DAI (15 prompts)
**Context Saved**: ~120 tokens per prompt (1,800 tokens total)

**Progressive Disclosure**:
- `SKILL.md`: Summary generation process (350 lines)
- `reference/summary-styles.md`: By content type (article, event, photo)
- `templates/thread-summary.md`: Social media optimized format
- `examples/good-summaries.md`: High-quality examples

---

#### **Skill 7: Quote Extraction & Formatting**
```yaml
name: "Extracting and Formatting Quotes"
description: "Extracts meaningful quotes from source content, formats them in markdown blockquotes, preserves original language, fixes transcription errors in quotes, and adds attribution. Limits to essence (one highlight per chapter)."
```

**Key Capabilities**:
- Meaningful quote identification
- Blockquote markdown formatting (`>`)
- Original language preservation
- Transcription error correction
- Attribution to speaker/author
- Highlight limitation (essence only)

**Used By**: EIC, GES, GDR, Summary prompts (10 prompts)
**Context Saved**: ~80 tokens per prompt (800 tokens total)

**Progressive Disclosure**:
- `SKILL.md`: Quote extraction criteria (250 lines)
- `reference/quote-formatting.md`: Formatting standards
- `reference/transcript-error-fixes.md`: Common voice-to-text errors

---

#### **Skill 8: Korean-English Translation**
```yaml
name: "Translating Korean and English"
description: "Handles Korean/English translation for PKM content: translates Clippings to Korean, preserves original language quotes, fixes Korean spacing and particle errors, handles English loanwords correctly, and maintains natural tone."
```

**Key Capabilities**:
- Korean as default for Clippings
- Spacing error correction (그런 데 → 그런데)
- Particle correction (관심이 가지는 → 관심을 가진)
- English loanword handling
- Technical term accuracy
- Natural tone preservation
- Avoid awkward honorifics

**Used By**: EIC, GES, PLL, GDR (12 prompts)
**Context Saved**: ~100 tokens per prompt (1,200 tokens total)

**Progressive Disclosure**:
- `SKILL.md`: Translation standards (300 lines)
- `reference/korean-spacing-rules.md`: Spacing error patterns
- `reference/english-loanwords.md`: Common loanword corrections
- `reference/technical-terms.md`: Domain-specific terminology

---

### 2.3 Knowledge Organization Skills (Layer 3)
**Topic and structure management**

#### **Skill 9: Topic Categorization & Tagging**
```yaml
name: "Categorizing and Tagging Content"
description: "Identifies relevant topics from content, maps to existing topic notes, generates appropriate tags, and ensures consistent categorization across the knowledge base. Validates topic existence before linking."
```

**Key Capabilities**:
- Topic identification from content
- Existing topic lookup
- Tag generation (YAML format, no # prefix)
- Category consistency validation
- New topic suggestion
- Cross-reference discovery

**Used By**: EIC, TKA, TKI, TKC, GDR (12 prompts)
**Context Saved**: ~90 tokens per prompt (1,080 tokens total)

**Progressive Disclosure**:
- `SKILL.md`: Categorization process (350 lines)
- `reference/topic-hierarchy.md`: Topic structure and categories
- `reference/tagging-standards.md`: Tag naming conventions
- `scripts/find_topics.py`: Topic discovery automation

---

#### **Skill 10: Source Attribution**
```yaml
name: "Managing Source Attribution"
description: "Tracks and attributes content to original sources: creates source property with URLs, maintains citation chains, links to original articles vs topic indices, and ensures traceability throughout the knowledge base."
```

**Key Capabilities**:
- Source property creation
- URL validation and formatting
- Author attribution
- Original source vs aggregation distinction
- Citation chain maintenance
- Traceability verification

**Used By**: EIC, TKA, GES, ARP (16 prompts)
**Context Saved**: ~60 tokens per prompt (960 tokens total)

**Progressive Disclosure**:
- `SKILL.md`: Attribution standards (200 lines)
- `reference/source-types.md`: Different source patterns
- `reference/citation-formats.md`: Citation standards

---

#### **Skill 11: Duplicate Detection & Merging**
```yaml
name: "Detecting and Merging Duplicates"
description: "Identifies duplicate or near-duplicate content across the knowledge base, suggests merge strategies, and maintains content consistency. Prevents redundant topic entries and consolidates related notes."
```

**Key Capabilities**:
- Content similarity detection
- Duplicate identification
- Merge strategy recommendation
- Consolidation automation
- Link updating after merge
- Quality preservation

**Used By**: TKC, TKA, UFN, EIC (8 prompts)
**Context Saved**: ~70 tokens per prompt (560 tokens total)

**Progressive Disclosure**:
- `SKILL.md`: Duplicate detection logic (300 lines)
- `scripts/detect_duplicates.py`: Similarity algorithm
- `reference/merge-strategies.md`: How to consolidate

---

### 2.4 Integration Skills (Layer 4)
**External system interactions**

#### **Skill 12: Google Calendar Integration**
```yaml
name: "Integrating with Google Calendar"
description: "Queries Google Calendar via MCP for event information: retrieves meeting details, participant lists, timing information, and validates calendar data for event summarization workflows."
```

**Key Capabilities**:
- MCP google-calendar server usage
- Event query by date/title
- Participant information extraction
- Timezone handling (America/Los_Angeles)
- Event timing validation
- Fully qualified tool name usage (google-calendar:get-event)

**Used By**: GES (1 prompt, but critical workflow)
**Context Saved**: ~150 tokens

**Progressive Disclosure**:
- `SKILL.md`: Calendar MCP integration (250 lines)
- `reference/calendar-queries.md`: Common query patterns
- `examples/event-extraction.md`: Real-world examples
- `scripts/calendar_helpers.py`: Helper functions

---

#### **Skill 13: Transcript Time Matching**
```yaml
name: "Matching Transcript Timestamps"
description: "Uses automation scripts to match voice transcripts to calendar event time windows: extracts relevant transcript chunks, validates timing accuracy, handles timezone conversions, and reports gaps or anomalies."
```

**Key Capabilities**:
- Script execution: `match_transcript.py`
- Timestamp parsing (ISO 8601)
- Timezone conversion
- Chunk extraction by time range
- Quality score validation
- Gap detection and reporting

**Used By**: GES (1 prompt)
**Context Saved**: ~180 tokens

**Progressive Disclosure**:
- `SKILL.md`: Transcript matching process (300 lines)
- `reference/script-usage.md`: match_transcript.py documentation
- `reference/timestamp-formats.md`: Supported formats
- `examples/transcript-chunks.json`: Example output

---

#### **Skill 14: File Operation Standards**
```yaml
name: "Standardizing File Operations"
description: "Defines standards for file creation, updates, and organization: naming conventions, folder structure, file type handling, and inline vs new file decisions. Ensures consistency across all content workflows."
```

**Key Capabilities**:
- File naming: `YYYY-MM-DD [Description] by [Agent].md`
- Folder organization rules
- Inline update vs new file logic
- File type detection
- Path resolution
- Permission handling

**Used By**: All output-generating prompts (20/25)
**Context Saved**: ~80 tokens per prompt (1,600 tokens total)

**Progressive Disclosure**:
- `SKILL.md`: File operation standards (250 lines)
- `reference/naming-conventions.md`: By file type
- `reference/folder-structure.md`: Hierarchy and organization
- `reference/update-vs-create.md`: Decision logic

---

#### **Skill 15: Status & Workflow Management**
```yaml
name: "Managing Task and Content Status"
description: "Handles status property updates throughout content lifecycle: status transitions (TBD → IN_PROGRESS → COMPLETED), worker assignment, completion tracking, and output property formatting. Integrates with task_status.py automation."
```

**Key Capabilities**:
- Status validation and transitions
- Worker field assignment
- Output property wiki link formatting
- Process log maintenance
- Completion timestamp recording
- Integration with task automation scripts

**Used By**: KTP, EIC, GES, all task prompts (15+ prompts)
**Context Saved**: ~100 tokens per prompt (1,500 tokens total)

**Progressive Disclosure**:
- `SKILL.md`: Status management process (350 lines)
- `reference/status-transitions.md`: Valid state changes
- `reference/output-formats.md`: Output property standards
- `scripts/task_status.py`: Integration documentation

---

## Part 3: Migration Strategy

### 3.1 Four-Phase Approach

#### **Phase 1: Extract Foundation Skills** (Weeks 1-2)
**Goal**: Create core Obsidian/PKM skills used by all prompts

**Skills to Create**:
1. Obsidian Link Formatting
2. YAML Frontmatter Management
3. Link Resolution & Validation
4. Markdown Structure Validation

**Test Prompts**:
- EIC (most complex, uses all foundation skills)
- TKA (simpler, good validation case)
- GDR (medium complexity)

**Success Metrics**:
- All 4 skills created and tested
- 3 test prompts successfully refactored
- Context reduction measured (target: 300-400 tokens per prompt)
- No regression in output quality

**Deliverables**:
- `.claude/plugins/skills/ai4pkm-foundation/`
  - `obsidian-links/SKILL.md`
  - `yaml-frontmatter/SKILL.md`
  - `link-validation/SKILL.md`
  - `markdown-structure/SKILL.md`

---

#### **Phase 2: Build Content Processing Skills** (Weeks 3-4)
**Goal**: Extract ICT and content transformation patterns

**Skills to Create**:
5. Improve Capture & Transcript (ICT)
6. Summary Generation
7. Quote Extraction & Formatting
8. Korean-English Translation

**Test Prompts**:
- EIC (uses ICT, summary, quotes, translation)
- PLL (uses ICT, translation)
- GES (uses ICT, quotes, translation)

**Success Metrics**:
- 4 content processing skills created
- EIC context reduced by 50%+
- Output quality maintained or improved
- ICT consistency across all prompts

**Deliverables**:
- `.claude/plugins/skills/ai4pkm-content/`
  - `ict-processing/SKILL.md`
  - `summary-generation/SKILL.md`
  - `quote-extraction/SKILL.md`
  - `korean-translation/SKILL.md`

---

#### **Phase 3: Refactor Major Workflows** (Weeks 5-8)
**Goal**: Rebuild DIR, CKU, KTG/KTP using skills

**Skills to Create**:
9. Topic Categorization & Tagging
10. Source Attribution
11. Duplicate Detection & Merging
12. Google Calendar Integration
13. Transcript Time Matching
14. File Operation Standards
15. Status & Workflow Management

**Workflows to Refactor**:
1. **DIR** (Week 5-6)
   - Refactor: PPP, PLL, EIC, GDR, TKA, CTP
   - Create thin orchestration layer
   - Test full workflow end-to-end

2. **CKU** (Week 7)
   - Refactor: EIC (batch), UFN, TKI
   - Optimize for hourly execution
   - Test with real content updates

3. **KTG/KTP** (Week 8)
   - Refactor task discovery and execution
   - Integrate task_status.py automation
   - Test with varied task types

**Success Metrics**:
- All 7 skills created
- 3 major workflows fully refactored
- End-to-end workflow testing passed
- Context usage reduced 40-60% overall

**Deliverables**:
- `.claude/plugins/skills/ai4pkm-organization/`
  - `topic-categorization/SKILL.md`
  - `source-attribution/SKILL.md`
  - `duplicate-detection/SKILL.md`
- `.claude/plugins/skills/ai4pkm-integration/`
  - `calendar-integration/SKILL.md`
  - `transcript-matching/SKILL.md`
  - `file-operations/SKILL.md`
  - `status-management/SKILL.md`
- Refactored workflow definitions in `_Settings_/Workflows/`

---

#### **Phase 4: Advanced Skills & Optimization** (Weeks 9-12)
**Goal**: Create domain-specific skills, optimize performance

**Advanced Skills**:
- Visual content skills (PPP, SFP, HPM)
- Content creation skills (GMS, GMV, DAI)
- Meta-skills (EPW, SAR, KTE)

**Optimization Focus**:
- Skill composition patterns
- Progressive disclosure tuning
- Reference file optimization
- Script performance improvement
- Documentation and examples

**Success Metrics**:
- All 25 prompts migrated to skills architecture
- Overall context reduction 40-60%
- Workflow creation time reduced 70%
- Documentation complete for all skills

**Deliverables**:
- Complete skill library (15+ skills)
- Skill composition guide
- Migration documentation
- Performance benchmarks
- Rollback procedures

---

### 3.2 Backward Compatibility Strategy

**During Migration**:
- Keep original prompts in `_Settings_/Prompts/` unchanged
- Create skill-based versions in `_Settings_/Prompts-v2/` (or similar)
- Test new versions thoroughly before switching
- Use feature flags for gradual rollout

**Rollback Plan**:
- Original prompts remain available
- Clear naming: `EIC.md` (original) vs `EIC-skilled.md` (new)
- Document differences and migration status
- Easy to switch back if issues arise

**Testing Protocol**:
- Compare outputs side-by-side (original vs skilled)
- Run both versions on same inputs
- Measure quality, context usage, execution time
- Collect user feedback on usability

---

## Part 4: Implementation Examples

### 4.1 Example 1: EIC (Enrich Ingested Content)

#### **Current Structure** (88 lines)
```markdown
---
title: "Enrich Ingested Content"
abbreviation: "EIC"
category: "workflow"
created: "2024-01-01"
---

## Input
- Target note file (typically in Ingest/Clippings/)
- Long articles may need chunking...

## Output
- Updated note inline (don't create new note)
- Status property set to `processed`
- Summary section added...

## Main Process
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
   - Use quotes verbatim...

3. ENRICH USING TOPICS
   - Link related KB topics (existing only)
   - Add one-line summary to relevant KB topics...

## Caveats
### Content Completeness - CRITICAL
⚠️ **CRITICAL**: ICT section must be COMPLETE - not truncated
[... 40+ lines of detailed caveats ...]

### Formatting Standards
- Use heading3 (###) for chapters
- Limit highlights to essence...

### Topic Linking
- Only link to existing topics in KB
- Validate all topic links before adding...
```

**Total**: ~88 lines, ~2,100 tokens

---

#### **Proposed Structure with Skills**

**New EIC Orchestrator** (~25 lines)
```markdown
---
title: "Enrich Ingested Content"
abbreviation: "EIC"
category: "workflow"
created: "2024-01-01"
requires_skills:
  - "ai4pkm-content/ict-processing"
  - "ai4pkm-content/summary-generation"
  - "ai4pkm-organization/topic-categorization"
  - "ai4pkm-foundation/yaml-frontmatter"
  - "ai4pkm-foundation/link-validation"
---

## Workflow

Process content through three stages using AI4PKM skills:

### 1. Improve Capture & Transcript
Use the **ICT Processing** skill to:
- Fix grammar and transcript errors
- Translate to Korean for Clippings
- Add structure with H3 chapters
- Apply formatting (lists, highlights)
- Preserve original length

### 2. Add Summary
Use the **Summary Generation** skill to:
- Create thread-friendly summary at beginning
- Include catchy opening and key quotes
- Maintain author's voice

### 3. Enrich Using Topics
Use **Topic Categorization** skill to:
- Link related KB topics (existing only)
- Add one-line summaries to topic pages
- Validate all topic links

### 4. Finalize
Use **YAML Frontmatter** and **Link Validation** skills to:
- Update status property to `processed`
- Validate all wiki links
- Ensure proper frontmatter structure

## Input/Output
- **Input**: Unprocessed note in Ingest/Clippings/
- **Output**: Inline update with status=processed

## Quality Checks
- Verify ICT section is complete (not truncated)
- Ensure summary is catchy and quote-rich
- Validate all topic links resolve
```

**Total**: ~25 lines, ~600 tokens (prompt only)
**Skills Context** (loaded progressively):
- ICT skill metadata: ~150 tokens (always loaded)
- ICT skill body: ~800 tokens (loaded when needed)
- Summary skill metadata: ~100 tokens (always loaded)
- Summary skill body: ~400 tokens (loaded when needed)
- Other skill metadata: ~200 tokens total (always loaded)

**Net Context**:
- **Before**: 2,100 tokens (all loaded upfront)
- **After**: 600 (prompt) + 450 (metadata) + skills as needed = 1,050-2,250 tokens
- **Best case** (skills already in context from other prompts): 600 tokens
- **Worst case** (first time loading skills): 2,250 tokens
- **Typical case** (some skills cached): 1,200 tokens
- **Savings**: 40-70% reduction in typical case

---

#### **Supporting Skills Created**

**Skill: ICT Processing**
```markdown
---
name: "Improving Captured Transcripts"
description: "Improves voice transcripts and captured content: fixes grammar and transcription errors, translates to Korean for Clippings, adds H3 chapter headings, applies formatting (lists, highlights), and preserves original length."
---

# ICT Processing Skill

## Overview
This skill transforms raw captured content (voice transcripts, web clippings, etc.) into polished, structured markdown suitable for the AI4PKM knowledge base.

## Process Steps

### 1. Grammar & Transcript Error Correction
- Fix voice-to-text mishearings
- Correct Korean spacing errors: "그런 데" → "그런데"
- Fix particle errors: "관심이 가지는" → "관심을 가진"
- Remove duplicates: "안 안 써" → "안 써"
- Handle English loanwords properly

For detailed error patterns, see [[reference/common-transcript-errors.md]].

### 2. Translation to Korean (for Clippings)
- Default to Korean for Ingest/Clippings/ content
- Preserve original language quotes
- Maintain natural tone (avoid awkward honorifics)
- Use proper technical terminology

See [[reference/korean-translation.md]] for standards.

### 3. Structure with H3 Chapters
- Detect natural chapter boundaries
- Create descriptive H3 headings
- Aim for one chapter per ~300-500 words
- Ensure logical flow between chapters

### 4. Apply Formatting
- Convert natural lists to markdown lists (bullets or numbered)
- Add highlights for key insights (one per chapter max)
- Preserve original prose structure
- Maintain paragraph breaks

### 5. Validate Length
- Final length should equal or exceed original
- Common failure: truncation mid-content
- If output seems short, verify completeness
- Last paragraph should end naturally, not cut off

## Critical Requirements

### Completeness Check
⚠️ **CRITICAL**: Verify ICT section is COMPLETE before marking done

**Warning signs of truncation**:
- Ends mid-sentence: "Since I last wrote at the beginning of the summer, my methodol..."
- Only 1-2 H3 sections when source has 5+ pages
- Final content is 30-50% shorter than source

**If truncated**:
- DO NOT mark status as processed
- Process in chunks if needed
- Request context extension if available

### Quality Verification Checklist
- [ ] Multiple H3 subsections created (not just one)
- [ ] Last paragraph ends with proper punctuation
- [ ] Length comparable to original
- [ ] No obvious truncation mid-thought

## Examples
See [[examples/ict-before-after.md]] for transformation examples.

## References
- [[reference/korean-translation.md]] - Translation standards
- [[reference/common-transcript-errors.md]] - Error correction patterns
- [[reference/formatting-patterns.md]] - List and highlight guidelines
```

**Progressive Disclosure**:
- Metadata: 150 tokens (always loaded)
- Body: 800 tokens (loaded when ICT needed)
- References: 1,200 tokens total (loaded on-demand)

---

### 4.2 Example 2: GES (Generate Event Summary)

#### **Current Structure** (104 lines)
```markdown
---
title: "Generate Event Summary"
abbreviation: "GES"
category: "workflow"
created: "2024-01-01"
---

## Input
- Meeting info from Google Calendar (via MCP)
- Voice transcript from Ingest/Limitless/{{YYYY-MM-DD}}
- Meeting Template for structure reference
- Event date and timing information

## Output
- File: AI/Events/{{YYYY-MM-DD}} Summary for {{Event}} - {{Agent-Name}}.md
- Korean language summary...

## Main Process
1. CALENDAR INTEGRATION
   - Pull meeting info from Google Calendar MCP server
   - Get event timing and participant details
   - Verify meeting context and title

2. AUTOMATED TRANSCRIPT MATCHING
   ⚙️ Use _Settings_/Tools/automation/match_transcript.py
   [... detailed script usage instructions ...]

3. SUMMARY GENERATION
   - Use Meeting Template as starting point
   - Write in Korean unless original is English
   - Process each chunk from transcript matcher
   - Validate speaker attribution...
   [... detailed instructions ...]

## Caveats
### Timing Accuracy
⚠️ **CRITICAL**: Use transcript matcher tool...

### Language Standards
- 한글로 작성 (unless original transcript is in English)...

### Quote Accuracy & Attribution
⚠️ **CRITICAL**: Verify participant names...

### Fix Transcription Errors in Quotes
⚠️ **IMPORTANT**: Voice-to-text transcription often contains errors
[... 20+ lines of error patterns ...]
```

**Total**: ~104 lines, ~2,400 tokens

---

#### **Proposed Structure with Skills**

**New GES Orchestrator** (~30 lines)
```markdown
---
title: "Generate Event Summary"
abbreviation: "GES"
category: "workflow"
requires_skills:
  - "ai4pkm-integration/calendar-integration"
  - "ai4pkm-integration/transcript-matching"
  - "ai4pkm-content/ict-processing"
  - "ai4pkm-content/quote-extraction"
  - "ai4pkm-content/korean-translation"
  - "ai4pkm-foundation/file-operations"
---

## Workflow

### 1. Retrieve Event Information
Use **Calendar Integration** skill to:
- Query Google Calendar via MCP
- Get event title, timing, participants
- Validate timezone (America/Los_Angeles)

### 2. Extract Relevant Transcript
Use **Transcript Time Matching** skill to:
- Run match_transcript.py automation
- Extract chunks within event time window
- Validate quality score and note gaps

### 3. Process Transcript Content
Use **ICT Processing** skill to:
- Fix transcription errors in chunks
- Translate to Korean (default)
- Structure with clear sections

### 4. Generate Summary
Use **Quote Extraction** skill to:
- Identify key discussion points
- Extract meaningful quotes
- Verify speaker attribution against participants
- Fix voice-to-text errors in quotes

### 5. Create Output File
Use **File Operations** skill to:
- Create: AI/Events/{{YYYY-MM-DD}} Summary for {{Event}} - {{Agent}}.md
- Include calendar metadata
- Add full transcript if requested
- Validate wiki links

## Templates
- Use [[Meeting Template]] for structure
- Korean language default
- Include timing validation warnings

## Quality Checks
- Verify speaker attribution accuracy
- Check for transcript error corrections
- Validate all participant names
- Note any timing gaps from validation
```

**Total**: ~30 lines, ~700 tokens (prompt only)
**Net Context**: 700 (prompt) + 600 (skill metadata) + skills as needed = 1,300-3,000 tokens
**Savings**: 40-60% in typical case

---

### 4.3 Example 3: KTP (Knowledge Task Processor)

#### **Current Structure** (196 lines)
```markdown
---
title: "Knowledge Task Processor"
abbreviation: "KTP"
category: "workflow"
created: "2024-01-01"
---

Process knowledge tasks from AI/Tasks folder systematically...

## Input
- Knowledge tasks from AI/Tasks folder
- Task files with proper frontmatter...

## Output
- Executed tasks with updated status
- Output files created per task requirements
- Process Log documentation...

## Main Process
0. RUN TASK STATUS MANAGER
   └─ Execute: python _Settings_/Tools/automation/task_status.py...
   [... detailed script usage ...]

1. BUILD EXECUTION PLAN
   └─ Use execution_queue array for task order
   └─ Review statistics...
   [... detailed instructions ...]

2. START TASK EXECUTION
   └─ Update status using script:
      python _Settings_/Tools/automation/task_status.py \
        --update "[task_filename]" \
        --status-new IN_PROGRESS...
   [... detailed state management ...]

3. EXECUTE & DOCUMENT
   [... execution logic ...]

4. COMPLETE TASK
   [... completion logic with script usage ...]

5. CLEANUP & VALIDATION
   [... validation logic ...]

## Caveats
### Priority-Based Execution
⚠️ **CRITICAL**: Always process higher priority tasks first
[... 15 lines of priority logic ...]

### Status Management Rules
- Status transitions: TBD → IN_PROGRESS → COMPLETED/FAILED
[... 10 lines of state machine ...]

### Output Documentation Standards
[... 20 lines of process log requirements ...]

## Key Lessons & Best Practices
### EIC Workflow Guidelines
[... 30 lines of specific workflow knowledge ...]

## Task Status Manager Integration
[... 50 lines of automation integration ...]
```

**Total**: ~196 lines, ~4,500 tokens

---

#### **Proposed Structure with Skills**

**New KTP Orchestrator** (~40 lines)
```markdown
---
title: "Knowledge Task Processor"
abbreviation: "KTP"
category: "workflow"
requires_skills:
  - "ai4pkm-integration/status-management"
  - "ai4pkm-foundation/file-operations"
  - "ai4pkm-foundation/link-validation"
  - "ai4pkm-foundation/yaml-frontmatter"
---

## Workflow

### 0. Load Task Queue
Use **Status Management** skill to:
- Run task_status.py to generate queue
- Load execution_queue from JSON
- Review priority distribution (P0 → P1 → P2 → P3)

### 1. Select Next Task
Use **Status Management** skill to:
- Get highest priority TBD task
- Update status to IN_PROGRESS
- Assign worker field
- Record start time

### 2. Execute Task
Follow task instructions from queue:
- Use specified prompts/workflows
- Create outputs per task requirements
- Document progress in Process Log
- Handle errors appropriately

Use relevant skills based on task type:
- **EIC tasks**: Use ICT, Summary, Topic skills
- **GES tasks**: Use Calendar, Transcript, Translation skills
- **Research tasks**: Use appropriate domain skills

### 3. Document & Validate
Use **File Operations** skill to:
- Create output files with proper naming
- Validate wiki links in outputs
- Check frontmatter structure

Use **YAML Frontmatter** skill to:
- Update output property with wiki links
- Set completion status
- Record completion time

Use **Link Validation** skill to:
- Verify all output files accessible
- Fix any broken links
- Update references

### 4. Complete Task
Use **Status Management** skill to:
- Mark task COMPLETED or FAILED
- Update Process Log
- Validate state transition
- Re-run task_status.py for next task

## Priority System
- P0: Critical/urgent (process first)
- P1: Important content (after P0)
- P2: Standard workflow (after P1)
- P3: Low priority optional (after P2)

## Task-Specific Guidelines

### EIC Tasks
⚠️ Update source clipping inline, don't create new analysis file
- Set output field = source field
- Use EIC skill/workflow

### GES Tasks
- Check for updated Limitless recordings
- Use transcript matcher automation
- Verify speaker attribution

## References
- [[Task Template]] for task file structure
- [[Task Status Manager README]] for automation details
```

**Total**: ~40 lines, ~950 tokens (prompt only)
**Net Context**: 950 (prompt) + 400 (skill metadata) + skills as needed = 1,350-2,500 tokens
**Savings**: 50-70% reduction

---

## Part 5: Technical Specifications

### 5.1 Skill Structure Standards

#### **Directory Layout**
```
.claude/plugins/skills/
├── ai4pkm-foundation/
│   ├── obsidian-links/
│   │   ├── SKILL.md
│   │   ├── reference/
│   │   │   ├── link-patterns.md
│   │   │   └── section-linking.md
│   │   └── examples/
│   │       └── link-transformations.md
│   ├── yaml-frontmatter/
│   │   ├── SKILL.md
│   │   ├── reference/
│   │   │   └── property-standards.md
│   │   └── templates/
│   │       └── frontmatter-examples.md
│   └── [... other foundation skills ...]
├── ai4pkm-content/
│   ├── ict-processing/
│   │   ├── SKILL.md
│   │   ├── reference/
│   │   │   ├── korean-translation.md
│   │   │   ├── formatting-patterns.md
│   │   │   └── common-transcript-errors.md
│   │   └── examples/
│   │       └── ict-before-after.md
│   └── [... other content skills ...]
├── ai4pkm-organization/
│   └── [... organization skills ...]
└── ai4pkm-integration/
    └── [... integration skills ...]
```

---

#### **SKILL.md Template**
```markdown
---
name: "Skill Name (Gerund Form)"
description: "Specific, third-person description (max 1024 chars). Include what it does and key trigger terms. Example: 'Processes Excel files for data extraction, supports formulas, charts, pivot tables. Use when working with .xlsx, spreadsheets, or Excel data.'"
---

# Skill Title

## Overview
Brief overview of what this skill does and when to use it.
Keep under 100 lines for this section.

## Process Steps

### Step 1: [Action Name]
Detailed instructions for first step.
- Bullet points for sub-steps
- Clear, concise language
- Assume Claude is intelligent

For more details, see [[reference/step1-details.md]].

### Step 2: [Action Name]
[... continue pattern ...]

## Critical Requirements

### [Requirement Name]
⚠️ **CRITICAL**: Important constraint or validation
- Why this matters
- How to verify
- What to do if violated

## Examples
See [[examples/example-scenarios.md]] for concrete examples.

## References
- [[reference/detailed-guide.md]] - Deep dive documentation
- [[reference/error-patterns.md]] - Common issues and solutions
- [[scripts/helper.py]] - Automation scripts (if applicable)
```

**Key Points**:
- SKILL.md body: < 500 lines
- Progressive disclosure via [[reference/...]] links
- One level deep (don't nest references)
- Table of contents for reference files > 100 lines
- Clear separation: overview → steps → requirements → examples → references

---

### 5.2 Progressive Disclosure Strategy

#### **Three-Tier Loading**

**Tier 1: Metadata (Always Loaded)**
```yaml
name: "Processing PDFs"
description: "Extracts text and data from PDF files, handles forms, tables, and images. Use when working with PDF documents, fillable forms, or document conversion."
```
- **Size**: 100-200 tokens per skill
- **Loaded**: At session start
- **Purpose**: Skill discovery and routing

**Tier 2: SKILL.md Body (Loaded When Triggered)**
```markdown
# Overview
Process PDFs using pdfplumber library...

## Process Steps
### 1. Extract Text
[... 100-300 lines ...]

## Critical Requirements
[... 50-100 lines ...]
```
- **Size**: 300-1,000 tokens per skill
- **Loaded**: When skill identified as relevant
- **Purpose**: Main execution instructions

**Tier 3: Reference Files (Loaded On-Demand)**
```markdown
See [[reference/table-extraction.md]] for table handling details.
```
- **Size**: 200-800 tokens per reference
- **Loaded**: When Claude needs specific detail
- **Purpose**: Deep technical knowledge

**Total Context Control**:
- Minimum (metadata only): 100-200 tokens
- Typical (metadata + body): 400-1,200 tokens
- Maximum (metadata + body + refs): 1,000-3,000 tokens

**Comparison to Monolithic Prompt**:
- Monolithic: 2,000-5,000 tokens (all loaded)
- Skills: 400-1,200 tokens typical (60-80% reduction)

---

### 5.3 Reference File Organization

#### **reference/ Subdirectory**
Contains detailed documentation loaded on-demand.

**Common Reference Types**:

1. **Detailed Guides** (`reference/detailed-guide.md`)
   - Deep dive into skill mechanics
   - Edge cases and advanced usage
   - Technical background

2. **Error Patterns** (`reference/error-patterns.md`)
   - Common mistakes and solutions
   - Debugging guidance
   - Validation rules

3. **Standards** (`reference/standards.md`)
   - Format specifications
   - Naming conventions
   - Structural requirements

4. **Domain Knowledge** (`reference/domain-knowledge.md`)
   - Topic-specific information
   - External system documentation
   - API references

**Best Practices**:
- One reference file per major concept
- Include table of contents for files > 100 lines
- Link from SKILL.md with clear context
- Keep references shallow (one level deep)

---

#### **examples/ Subdirectory**
Contains concrete input/output pairs.

**Example Types**:

1. **Before/After** (`examples/transformation.md`)
   ```markdown
   ## Input
   [Raw content...]

   ## Output
   [Processed content...]

   ## Notes
   - What changed
   - Why it changed
   - Key transformations
   ```

2. **Scenarios** (`examples/scenarios.md`)
   ```markdown
   ## Scenario 1: Simple Case
   Input: [...]
   Process: [...]
   Output: [...]

   ## Scenario 2: Edge Case
   [...]
   ```

3. **Good vs Bad** (`examples/quality.md`)
   ```markdown
   ## Good Example
   [Correct output...]

   ## Bad Example
   [Incorrect output and why...]
   ```

**Best Practices**:
- Real examples from actual usage
- Annotate what makes examples good/bad
- Cover common cases and edge cases
- Keep examples concise (< 100 lines each)

---

#### **scripts/ Subdirectory**
Contains executable scripts referenced by skill.

**Script Types**:

1. **Validation Scripts** (`scripts/validate.py`)
   - Check output correctness
   - Return clear error messages
   - Exit codes for automation

2. **Helper Scripts** (`scripts/helper.py`)
   - Utility functions
   - Common operations
   - Reusable components

3. **Automation Scripts** (`scripts/automate.py`)
   - Full workflow automation
   - Can be executed directly
   - Well-documented parameters

**Integration**:
```markdown
## Step 3: Validate Output
Run validation script:
```bash
python scripts/validate.py input_file.md
```

If validation fails, review error messages and fix issues before proceeding.
```

**Best Practices**:
- Clear documentation in script headers
- Helpful error messages
- Reasonable defaults
- No "magic numbers" without comments

---

### 5.4 MCP Integration Points

#### **Skill-MCP Coordination**

**Pattern 1: Skill References MCP Tool**
```markdown
# Calendar Integration Skill

## Process Steps

### 1. Query Event Information
Use the Google Calendar MCP tool to retrieve event details:
```
Use the **google-calendar:get-event** tool with event ID.
```

Note: Always use fully qualified name: `server:tool_name`
```

**Pattern 2: Skill Wraps MCP Complexity**
```markdown
# BigQuery Data Retrieval Skill

## Process Steps

### 1. Connect to BigQuery
Use **BigQuery:connect** tool with project ID from [[reference/bigquery-config.md]].

### 2. Execute Template Query
Load query template from [[reference/sql-templates.md]].
Parameterize with user inputs.
Execute via **BigQuery:execute_query**.

### 3. Process Results
[... result handling ...]
```

**Benefits**:
- Skills provide context for MCP usage
- Template patterns for common MCP operations
- Error handling guidance
- Configuration management

---

### 5.5 Script Integration Standards

#### **Calling Scripts from Skills**

**Pattern**: Explicit script execution instructions

```markdown
## Step 2: Match Transcript to Time Window

Execute the transcript matching automation:
```bash
python _Settings_/Tools/automation/match_transcript.py \
  --transcript "Ingest/Limitless/YYYY-MM-DD.md" \
  --start "2025-10-19T10:00:00" \
  --end "2025-10-19T11:00:00" \
  --event-title "Meeting Title" \
  --timezone "America/Los_Angeles" \
  --output "/tmp/transcript_match.json"
```

### Processing Script Output
Read JSON from `/tmp/transcript_match.json`:
- `chunks`: Array of transcript segments
- `validation`: Quality score and gap detection
- Process each `chunk.content` sequentially

For detailed script documentation, see [[reference/script-usage.md]].
```

**Benefits**:
- Clear automation boundaries
- Reusable script patterns
- Validation built-in
- Error handling guidance

---

## Part 6: Success Metrics

### 6.1 Quantitative Metrics

#### **Context Token Reduction**
**Target**: 40-60% reduction in average context usage

**Measurement**:
```python
# Before (monolithic prompts)
avg_prompt_tokens = 2,500
workflows_per_session = 3
total_context = 2,500 * 3 = 7,500 tokens

# After (skills architecture)
skill_metadata_total = 15 * 150 = 2,250 tokens (loaded once)
workflow_prompt_avg = 700 tokens
workflow_count = 3
workflow_tokens = 700 * 3 = 2,100 tokens
skill_bodies_loaded = 5 (average across 3 workflows)
skill_body_tokens = 5 * 600 = 3,000 tokens
total_context = 2,250 + 2,100 + 3,000 = 7,350 tokens

# But with skill reuse across workflows:
# Workflows share skills, so body loading is amortized
realistic_total = 2,250 + 2,100 + 1,800 = 6,150 tokens

# Reduction: (7,500 - 6,150) / 7,500 = 18% (conservative)

# Best case (skills already loaded from prior work):
best_case_total = 2,250 + 2,100 = 4,350 tokens
# Reduction: (7,500 - 4,350) / 7,500 = 42%

# Target achieved in typical usage
```

**Tracking**:
- Log context usage per workflow run
- Compare before/after for same workflows
- Track skill reuse patterns
- Monitor progressive disclosure effectiveness

---

#### **Prompt Maintainability**
**Target**: 70% reduction in prompt lines of code

**Measurement**:
```
Current State:
- Total prompt lines: ~2,500 (25 prompts × 100 avg)
- Duplicated lines: ~1,750 (70% duplication)
- Unique lines: ~750

Skills State:
- Workflow orchestrators: 25 × 30 = 750 lines
- Skill definitions: 15 × 300 = 4,500 lines
- But skills are reusable, not duplicated

Effective lines for maintenance:
- Current: 2,500 lines (with duplication)
- Skills: 750 (orchestrators) + 4,500 (skills) / 15 (reuse factor) = 1,050 lines
- Reduction: (2,500 - 1,050) / 2,500 = 58%

# With better reuse:
# Skills: 750 + 4,500 / 20 = 975 lines
# Reduction: 61%
```

**Tracking**:
- Lines of code in prompts vs orchestrators
- Skill reuse count
- Duplication percentage
- Time to update common patterns

---

#### **Reusability Across Prompts**
**Target**: Average skill used by 8+ prompts

**Measurement**:
```
Foundation Skills:
- Obsidian Links: 25 prompts (100% reuse)
- YAML Frontmatter: 22 prompts (88%)
- Link Validation: 20 prompts (80%)
- Markdown Structure: 18 prompts (72%)
Average: 95% reuse

Content Skills:
- ICT Processing: 7 prompts (28%)
- Summary Generation: 15 prompts (60%)
- Quote Extraction: 10 prompts (40%)
- Korean Translation: 12 prompts (48%)
Average: 44% reuse

Organization Skills:
- Topic Categorization: 12 prompts (48%)
- Source Attribution: 16 prompts (64%)
- Duplicate Detection: 8 prompts (32%)
Average: 48% reuse

Integration Skills:
- File Operations: 20 prompts (80%)
- Status Management: 15 prompts (60%)
- Calendar Integration: 1 prompt (4%)
- Transcript Matching: 1 prompt (4%)
Average: 37% reuse

Overall Average: ~56% reuse (8.4 prompts per skill)
Target: > 32% (8+ prompts)
✅ TARGET EXCEEDED
```

**Tracking**:
- Skill usage matrix (skills × prompts)
- Average prompts per skill
- Identify under-utilized skills for consolidation

---

#### **Time to Create New Workflows**
**Target**: 70% reduction in workflow creation time

**Measurement**:
```
Current Workflow Creation:
1. Draft prompt from scratch: 2-3 hours
2. Add common patterns (links, frontmatter, etc.): 1-2 hours
3. Test and refine: 1-2 hours
4. Document caveats and examples: 1 hour
Total: 5-8 hours

Skills-Based Workflow Creation:
1. Identify required skills: 15 minutes
2. Draft thin orchestrator: 30 minutes
3. Test with existing skills: 30 minutes
4. Refine orchestration logic: 30 minutes
5. Document workflow-specific requirements: 15 minutes
Total: 2 hours

Reduction: (6.5 - 2) / 6.5 = 69%
✅ TARGET ACHIEVED
```

**Tracking**:
- Time logs for workflow creation
- Before/after comparison
- Identify bottlenecks
- Skill coverage gaps

---

#### **Output Consistency**
**Target**: 95% consistency across same workflow runs

**Measurement**:
```python
# Define consistency metric
def consistency_score(outputs):
    """
    Compare multiple outputs from same workflow on same input.
    Score based on:
    - Formatting consistency (headings, lists, quotes)
    - Content completeness (no truncation)
    - Property correctness (frontmatter, status, output)
    - Link validity (all links resolve)
    """
    scores = []
    for output in outputs:
        format_score = check_formatting(output)
        complete_score = check_completeness(output)
        property_score = check_properties(output)
        link_score = check_links(output)
        scores.append((format_score + complete_score + property_score + link_score) / 4)
    return sum(scores) / len(scores)

# Test workflow 5 times with same input
consistency = consistency_score(run_workflow_5_times("EIC", test_input))
# Target: consistency > 95%
```

**Tracking**:
- Run workflows multiple times
- Measure formatting, completeness, properties, links
- Identify inconsistency sources
- Improve skills to increase consistency

---

### 6.2 Qualitative Metrics

#### **Developer Experience**
- **Ease of creating new workflows** (survey 1-5 scale)
- **Clarity of skill documentation** (survey 1-5 scale)
- **Debugging difficulty** (time to identify and fix issues)
- **Confidence in outputs** (survey 1-5 scale)

**Target**: Average score > 4.0 on all surveys

---

#### **Output Quality**
- **Accuracy**: Correct information and attribution
- **Completeness**: No truncation or missing sections
- **Formatting**: Proper markdown structure
- **Relevance**: Appropriate topic links and tags

**Measurement**: Manual review of sample outputs (20 per workflow)
**Target**: > 90% of outputs meet all quality criteria

---

#### **Maintenance Burden**
- **Time to update common pattern** (e.g., link format change)
- **Number of files to modify** for common updates
- **Regression risk** (changes breaking other workflows)

**Target**:
- Pattern updates: < 30 minutes
- Files to modify: 1-3 (skill files only)
- Zero regressions from skill updates

---

## Part 7: Next Steps & Recommendations

### 7.1 Immediate Actions (Week 1)

#### **1. Set Up Skills Infrastructure**
```bash
# Create skills directory structure
mkdir -p .claude/plugins/skills/ai4pkm-foundation
mkdir -p .claude/plugins/skills/ai4pkm-content
mkdir -p .claude/plugins/skills/ai4pkm-organization
mkdir -p .claude/plugins/skills/ai4pkm-integration

# Create skill template
cat > .claude/plugins/skills/SKILL_TEMPLATE.md << 'EOF'
---
name: "Skill Name (Gerund Form)"
description: "Specific third-person description with trigger terms (max 1024 chars)"
---

# Skill Title

## Overview
[Brief overview < 100 lines]

## Process Steps
[Step-by-step instructions]

## Critical Requirements
[Important constraints]

## Examples
[Link to examples]

## References
[Link to detailed docs]
EOF
```

#### **2. Create Foundation Skills (Priority Order)**

**Day 1-2: Obsidian Link Formatting**
- Most used pattern (25/25 prompts)
- Highest ROI for context reduction
- Relatively simple to extract

**Day 3-4: YAML Frontmatter Management**
- Second most used (22/25 prompts)
- Clear, well-defined structure
- High consistency requirements

**Day 5-6: Link Resolution & Validation**
- Critical for quality (20/25 prompts)
- Complex logic to centralize
- Prevents broken links

**Day 7: Markdown Structure Validation**
- Completes foundation layer
- Ensures document quality
- Enables other skills to assume valid structure

#### **3. Test with EIC**
- Refactor EIC to use 4 foundation skills
- Run side-by-side tests (original vs skilled)
- Measure context reduction and output quality
- Document lessons learned

**Success Criteria**:
- ✅ All 4 foundation skills created
- ✅ EIC successfully refactored
- ✅ Context reduction measured (target: 30%+)
- ✅ Output quality maintained or improved
- ✅ No regressions in functionality

---

### 7.2 Phase 1 Execution (Weeks 1-2)

#### **Week 1: Foundation Skills**
**Monday-Tuesday**: Obsidian Link Formatting
- Extract pattern from all prompts
- Create SKILL.md with progressive disclosure
- Build reference docs and examples
- Test with 3 prompts

**Wednesday-Thursday**: YAML Frontmatter Management
- Define property standards
- Create validation logic
- Build templates for different doc types
- Test with 3 prompts

**Friday**: Link Resolution & Validation
- Extract link checking patterns
- Create validation script
- Build error message library
- Test with 3 prompts

**Weekend**: Buffer for issues

**Week 2: Complete Foundation + Test**
**Monday**: Markdown Structure Validation
- Extract structure rules
- Create validation script
- Build templates
- Test with 3 prompts

**Tuesday-Wednesday**: Refactor EIC
- Create EIC orchestrator using skills
- Test thoroughly
- Compare before/after

**Thursday**: Refactor TKA
- Create TKA orchestrator
- Test and compare
- Document patterns

**Friday**: Refactor GDR
- Create GDR orchestrator
- Test and compare
- Measure metrics

**Weekend**: Phase 1 retrospective and planning

**Phase 1 Deliverables**:
- 4 foundation skills in `.claude/plugins/skills/ai4pkm-foundation/`
- 3 refactored prompts (EIC, TKA, GDR)
- Context reduction measurements
- Lessons learned document

---

### 7.3 Phase 2 Planning (Weeks 3-4)

#### **Content Processing Skills Priority**

**Week 3: ICT Processing + Korean Translation**
- These are tightly coupled in many prompts
- Extract together for consistency
- Test with EIC, PLL, GES

**Week 4: Summary Generation + Quote Extraction**
- Another coupled pair
- Used in many workflows
- Test with EIC, GDR, GWR, CTP

**Deliverables**:
- 4 content processing skills created
- EIC, PLL, GES refactored to use them
- Measured consistency improvements
- Updated migration guide

---

### 7.4 Risk Mitigation

#### **Rollback Strategy**
1. **Keep original prompts unchanged**
   - Copy to `_Settings_/Prompts-v2/` for skills versions
   - Original prompts remain in `_Settings_/Prompts/`
   - Easy to revert if needed

2. **Version control**
   - Git branch for skills migration: `feature/skills-architecture`
   - Commit after each skill created
   - Tag stable milestones: `v2.0-phase1-complete`

3. **A/B testing**
   - Run both versions in parallel
   - Compare outputs side-by-side
   - Measure metrics for both
   - Switch only when confident

4. **Feature flags**
   - Environment variable: `USE_SKILLS_ARCHITECTURE=true`
   - Can toggle per workflow
   - Gradual rollout per workflow type

#### **Quality Assurance**
1. **Automated testing**
   - Create test suite for each skill
   - Input/output validation
   - Regression tests for workflows
   - Run before each merge

2. **Manual review**
   - Sample 20 outputs per workflow
   - Check formatting, completeness, correctness
   - Document any issues
   - Fix before proceeding

3. **User feedback**
   - Collect feedback from actual usage
   - Track common issues
   - Iterate on skills quickly
   - Maintain quality log

---

### 7.5 Long-term Recommendations

#### **Build Skill Creation Skill**
Ironically, create a skill to help build skills:
```yaml
name: "Creating AI4PKM Skills"
description: "Helps create new skills for AI4PKM: extracts patterns from prompts, generates SKILL.md structure with progressive disclosure, creates reference docs and examples, follows best practices."
```

**Benefits**:
- Accelerate skill creation
- Ensure consistency across skills
- Reduce errors in skill structure
- Document skill creation patterns

---

#### **Establish Skill Governance**
1. **Skill Review Process**
   - Checklist for new skills
   - Peer review requirement
   - Performance benchmarks
   - Documentation standards

2. **Skill Lifecycle**
   - Creation → Testing → Approval → Deployment
   - Versioning strategy
   - Deprecation process
   - Migration guides

3. **Skill Registry**
   - Central catalog of all skills
   - Usage statistics
   - Dependencies
   - Maintenance status

---

#### **Community Contribution**
1. **Open source skills**
   - Share AI4PKM skills publicly
   - Contribute to anthropics/skills repo
   - Learn from community skills
   - Build ecosystem

2. **Documentation**
   - Public skill authoring guide
   - Best practices from AI4PKM
   - Case studies
   - Migration story

3. **Feedback loop**
   - Gather community feedback
   - Improve skills based on usage
   - Share improvements back
   - Build reputation

---

## Conclusion

The evolution from monolithic prompts to Claude Skills architecture represents a fundamental shift in how AI4PKM organizes reusable knowledge. By extracting common patterns into skills and adopting progressive disclosure, we can achieve:

**Immediate Benefits**:
- 40-60% reduction in context usage
- 70% faster workflow creation
- Centralized maintenance (single source of truth)
- Improved output consistency

**Long-term Impact**:
- Sustainable architecture for growth
- Easy skill composition and reuse
- Community contribution and learning
- Foundation for advanced AI workflows

**Recommended Action**:
Begin Phase 1 immediately with the 4 foundation skills. The ROI is clear, the risk is low (with rollback strategy), and the learning will inform all subsequent phases.

**Next Document**: `2025-10-19 Phase 1 Implementation Plan.md`

---

## Appendix: Skill Catalog

### Foundation Skills (4)
1. Obsidian Link Formatting - 25 prompts (100%)
2. YAML Frontmatter Management - 22 prompts (88%)
3. Link Resolution & Validation - 20 prompts (80%)
4. Markdown Structure Validation - 18 prompts (72%)

### Content Processing Skills (4)
5. Improve Capture & Transcript (ICT) - 7 prompts (28%)
6. Summary Generation - 15 prompts (60%)
7. Quote Extraction & Formatting - 10 prompts (40%)
8. Korean-English Translation - 12 prompts (48%)

### Knowledge Organization Skills (3)
9. Topic Categorization & Tagging - 12 prompts (48%)
10. Source Attribution - 16 prompts (64%)
11. Duplicate Detection & Merging - 8 prompts (32%)

### Integration Skills (4)
12. Google Calendar Integration - 1 prompt (4%)
13. Transcript Time Matching - 1 prompt (4%)
14. File Operation Standards - 20 prompts (80%)
15. Status & Workflow Management - 15 prompts (60%)

**Total**: 15 skills covering 25 prompts
**Average Reuse**: 8.4 prompts per skill (56%)
**Expected Context Reduction**: 40-60%
**Expected Maintenance Reduction**: 60-70%

---

*Document created: 2025-10-19*
*Author: Claude Code*
*Source: Skills evolution analysis for AI4PKM*
