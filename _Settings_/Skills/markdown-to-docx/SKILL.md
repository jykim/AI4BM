---
name: markdown-to-docx
description: Convert markdown documents to Microsoft Word (.docx) format with Korean font support, bold/italic formatting, nested list indentation, and professional styling
---

# Markdown to DOCX Converter

Convert markdown documents to professionally formatted Microsoft Word (.docx) files with full support for Korean text, inline formatting, and nested lists.

## When to Use This Skill

Use this skill when you need to:
- Convert markdown documents to Word format for sharing or editing
- Create DOCX files with proper Korean font rendering
- Preserve formatting like bold, italic, headers, and lists
- Export vault notes to Word documents
- Generate professional documents from markdown content

**Trigger phrases:**
- "Convert this markdown to DOCX"
- "Export [filename].md to Word"
- "Create a Word document from this markdown"
- "Generate DOCX from [filename]"

## Features

### ✅ Korean Language Support
- Default font: **Malgun Gothic** (맑은 고딕)
- Proper rendering of Korean characters
- Mixed Korean/English text support

### ✅ Inline Formatting
- **Bold text**: `**text**` or `__text__`
- *Italic text*: `*text*` or `_text*`
- Preserves formatting in headers, lists, and paragraphs

### ✅ Nested List Support
- Bullet lists with proper indentation
- Numbered lists with hierarchy
- Automatic indent calculation (2 spaces = 0.5 inch)
- Checkbox support: `- [ ]` and `- [x]`

### ✅ Document Structure
- Headers: H1, H2, H3, H4
- Block quotes with indentation
- Regular paragraphs
- Comment filtering (`%%comment%%`)

## How It Works

1. **Parse Markdown**: Reads markdown content line by line
2. **Process Structure**: Identifies headers, lists, quotes, paragraphs
3. **Apply Formatting**: Converts markdown syntax to DOCX formatting
4. **Set Fonts**: Applies Korean-friendly fonts throughout
5. **Generate File**: Creates .docx file ready for Word/Google Docs

## Usage Examples

### Example 1: Convert Korean Document
```
"Convert this markdown to DOCX:

# 한국어 문서 제목

## 소개
이것은 **굵은 글씨**이고 이것은 *기울임*입니다.

- 항목 1
  - 중첩된 항목
- 항목 2"
```

### Example 2: Export Vault Note
```
"Export 'Publish/AI for Better Me/AI for Better Me - FastCampus Class.md' to DOCX"
```

### Example 3: Mixed Language Content
```
"Create a Word document from this:

# AI for PKM

## Core Concepts
- **지식 관리** (Knowledge Management)
  - Information capture
  - 자동 정리 (Auto-organization)
- AI Integration"
```

## Supported Markdown Elements

| Markdown Syntax | DOCX Output | Notes |
|----------------|-------------|-------|
| `# Heading 1` | Heading Level 1 | H1 style |
| `## Heading 2` | Heading Level 2 | H2 style |
| `### Heading 3` | Heading Level 3 | H3 style |
| `**bold**` | **Bold text** | Run-level formatting |
| `*italic*` | *Italic text* | Run-level formatting |
| `- Item` | • Bullet list | List Bullet style |
| `  - Nested` | ◦ Indented bullet | 0.5" indent |
| `1. Item` | 1. Numbered list | List Number style |
| `- [ ]` | ☐ Checkbox | Unchecked |
| `- [x]` | ☑ Checkbox | Checked |
| `> Quote` | Indented quote | Italic, 0.5" indent |
| `%%comment%%` | (removed) | Filtered out |

## Technical Details

### Font Configuration
- **Default**: Malgun Gothic (11pt)
- Applied to all runs and paragraphs
- Consistent rendering across Korean/English

### Indentation Rules
- Base indent: 0.5 inches per level
- Calculated from leading spaces (2 spaces = 1 level)
- Applies to both bullet and numbered lists

### Processing Steps
```python
# Main workflow
1. Read markdown file or content
2. Skip YAML frontmatter (---...---)
3. Process each line:
   - Detect type (header, list, paragraph)
   - Calculate indent level
   - Apply inline formatting (bold/italic)
   - Create DOCX element with proper style
4. Save to .docx file
```

## Scripts

### docx_generator.py
Main conversion script with:
- `DOCXGenerator` class for document creation
- `process_inline_formatting()` for **bold** and *italic*
- `get_indent_level()` for nested list calculation
- `create_docx_from_markdown()` entry point

## Tips for Best Results

1. **Clean Frontmatter**: The converter skips YAML frontmatter automatically
2. **Consistent Spacing**: Use 2 spaces for each indentation level
3. **List Markers**: Use `-` for bullets, `1.` for numbers
4. **Korean Text**: No special handling needed - just write normally
5. **File Size**: Works well with documents up to ~500 lines

## Limitations

- Does not support tables (requires complex DOCX table API)
- Images are not embedded (wiki links are preserved as text)
- Internal links (`[[wikilinks]]`) rendered as plain text
- Code blocks rendered as regular paragraphs

## Output Format

Generated DOCX files include:
- Professional document styling
- Proper heading hierarchy
- Consistent font throughout (Malgun Gothic)
- Preserved formatting and structure
- Ready for Microsoft Word, Google Docs, LibreOffice

## Example Output Structure

```
Document Properties:
├── Default Font: Malgun Gothic 11pt
├── Page Size: Letter (8.5" × 11")
└── Margins: Normal (1" all sides)

Content Hierarchy:
├── Heading 1 (Title level)
├── Heading 2 (Section)
│   ├── Paragraph with bold/italic
│   ├── Bullet List
│   │   └── Nested Bullet (indented)
│   └── Numbered List
└── Heading 2 (Next section)
```

## Dependencies

Requires `python-docx` library:
```bash
pip install python-docx>=1.1.0
```

## Related Skills

- **csv-analysis**: Analyze CSV files and export to Excel
- **pdf-skill**: Work with PDF documents
- **claude-epub-skill**: Convert markdown to EPUB format
