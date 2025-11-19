# Content Sanitization Criteria

Guidelines for converting personal vault content to team vault format.

## REMOVE: Personal Content

### 1. Time-Stamped Personal Entries
**Patterns:**
- `### Title (YYYY년 MM월 DD일)` sections
- References like `[[Roundup/YYYY-MM-DD]]`, `[[Journal/YYYY-MM-DD]]`
- `[[Limitless/YYYY-MM-DD#section]]`
- `[[AI/Events/YYYY-MM-DD Event Name]]`

### 2. First-Person Narratives
**Examples:**
- "나는", "내가", "저는", "I" describing personal actions/feelings
- Personal project timelines and development logs
- Individual meeting notes and conversations
- "In my experience..." or "나의 경험에서는..."

### 3. Attribution to Specific Individuals
**Examples:**
- "김주성님의", "진혁님의", "Jin의 요구 사항"
- Meeting participant names and personal conversations
- Keep only if public figure/author with published work

### 4. Personal Tool/Service Experiences
**Examples:**
- Subscription costs, personal ROI calculations
- Individual configuration choices
- "나만의" (my own) setups
- "Claude Code Max 활용: '백불이 싸다고 느낀 첫 경험'"

## KEEP: Universal Content

### 1. Concepts and Frameworks
**Keep:**
- Definitions, principles, methodologies
- Framework explanations (PARA, CODE, Zettelkasten, etc.)
- System architectures and patterns

**Transform:**
- "I learned X" → "Key insight: X"
- "In my experience, Y" → "In practice, Y"
- Remove attribution to dates/individuals

### 2. Best Practices and Patterns
**Keep:**
- Anonymized case studies
- Generic tool comparisons
- Methodology guidelines

**Transform:**
- "한국의 한 개발 팀장" → "A development team lead"
- Remove specific dates: "초기에는... 이후에는..." (keep sequence)
- "I prefer X" → "X is suitable for Y use case"

### 3. Quotes from Published Sources
**Keep:**
- Full attribution to original source
- Wiki links to Source/ summaries (not personal articles)
- Published author statements

**Example:**
- ✅ "As Tiago Forte notes in Building a Second Brain..."
- ❌ "김주성님이 말씀하신..." (unless it's a published quote)

### 4. Generic Tool Comparisons
**Keep:**
- Comparative analysis (Obsidian vs Notion)
- Feature descriptions
- Use case suitability

**Remove:**
- Personal preferences without rationale
- Individual setup details
- Specific personal workflows

## Transformation Patterns

### Example 1: Meeting Insights → Generic Principle
**Before:**
```
[[2025-08-07 창발 AI4PKM 미팅 회의록]]에서:
800+ 에버노트를 반나절만에 마크다운 변환
```

**After:**
```
Case study: Large-scale migration of 800+ notes to markdown
using AI-assisted tooling completed in half-day timeframe.
```

### Example 2: Personal Reflection → Remove
**Before:**
```
나는 항상 스스로 하는 일에 좀 더 너무 집중하고...
```

**After:**
```
[REMOVED - personal reflection]
```

### Example 3: Individual Attribution → Universal Principle
**Before:**
```
김주성님의 액션 중심 PKM:
'지식이 쌓이는데 행동이 변하지 않으면 의미가 없다'
```

**After:**
```
Action-oriented PKM principle:
'Knowledge accumulation without behavioral change lacks meaning'
```

### Example 4: Journal Link → Concept Only
**Before:**
```
[[Journal/2025-08-07]]에서 깨달은 점:
Progressive Disclosure가 중요하다
```

**After:**
```
Key insight: Progressive Disclosure mechanism enables
gradual complexity management in knowledge systems.
```

## Automated Detection Patterns

### Regex Patterns for REMOVE
```regex
# Journal/Roundup/Limitless links
\[\[(?:Journal|Roundup|Limitless|AI\/Events)\/\d{4}-\d{2}-\d{2}[^\]]*\]\]

# Dated section headers
^###\s+.+\s+\(\d{4}년\s+\d{1,2}월\s+\d{1,2}일\)

# Korean first-person
(나는|내가|저는|나의|내)

# English first-person narratives
\b(I\s+(?:learned|found|discovered|realized|think|prefer))\b

# Personal attribution markers
님의|님이|님께서
```

### Manual Review Required
- Quotes and citations (verify if published or personal)
- Tool comparisons (separate fact from personal preference)
- Case studies (anonymize properly)
- Framework explanations (ensure no personal examples embedded)

## Quality Checklist

Before committing sanitized content:
- [ ] No wiki links to Journal/, Limitless/, Roundup/, AI/Events/
- [ ] No first-person narratives (나는, I)
- [ ] No individual names (unless published authors)
- [ ] No specific dates in content (use frontmatter instead)
- [ ] All concepts have universal explanations
- [ ] Examples are anonymized or generic
- [ ] Links point to Source/ summaries, not personal articles
- [ ] Frontmatter tags are plain text (no #)
- [ ] Created date in YYYY-MM-DD format
