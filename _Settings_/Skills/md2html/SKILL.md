---
name: md2html
description: Convert markdown documents to HTML format for website publishing with dark theme styling, image conversion (Excalidraw to PNG/SVG), and proper frontmatter handling
---

# Markdown to HTML Converter for Website Publishing

Convert markdown documents to professionally styled HTML pages ready for web publishing. Includes automatic image conversion, frontmatter processing, and integration with the AI4BM website design system.

## When to Use This Skill

Use this skill when you need to:
- Publish vault markdown content to website
- Convert theory/blog posts to HTML pages
- Handle Excalidraw diagrams and embedded images
- Create HTML pages matching the AI4BM website design
- Batch convert multiple markdown files to website pages

**Trigger phrases:**
- "Convert this markdown to HTML for the website"
- "Publish [filename].md to website"
- "Create HTML page from [markdown-file]"
- "Export vault content to HTML"
- "Generate website page from markdown"

## Features

### ✅ Full Markdown Conversion
- Headers (H1-H6) with proper hierarchy
- Paragraphs with smart formatting
- Lists (ordered, unordered, nested)
- Tables with responsive styling
- Blockquotes with accent borders
- Code blocks with syntax highlighting
- Inline formatting (bold, italic, code)

### ✅ Image Handling
- **Excalidraw conversion**: Automatically converts `.excalidraw.svg` to PNG or inline SVG
- **Embedded images**: Copies and references images from vault
- **Image optimization**: Optional compression and resizing
- **Alt text preservation**: Maintains accessibility

### ✅ Frontmatter Processing
- Extracts YAML frontmatter for meta tags
- Sets page title from frontmatter or H1
- Adds meta description for SEO
- Handles tags and dates
- Preserves custom properties

### ✅ Website Integration
- Uses AI4BM website template (dark theme, gradient accents)
- Includes navigation menu and breadcrumbs
- Adds footer with social links
- Responsive design built-in
- Canvas animation background

### ✅ Wiki Link Conversion
- Converts `[[Wiki Links]]` to relative HTML links
- Handles section links: `[[File#section]]`
- Resolves links to actual file paths
- Warns about broken links

## Usage

### Basic Conversion

```
"Convert Theory/Theory of AI4PKM (1) - Why PKM.md to HTML for the website"
```

**Output:**
- HTML file at `_Sandbox_/Jin/Homepage/theory-part1.html`
- Converted images in `_files_/` directory
- Properly styled with website theme

### Batch Conversion

```
"Convert all files in Theory/ folder to HTML pages"
```

**Result:**
- Multiple HTML files created
- Consistent navigation between pages
- All images processed

### Custom Output Location

```
"Publish Publish/Blog/AI for PKM.md to HTML at _Sandbox_/Jin/Homepage/blog/ai-for-pkm.html"
```

## Configuration

Default settings (can be customized per request):

```yaml
output_dir: "_Sandbox_/Jin/Homepage/"
template_style: "ai4bm-dark"  # AI4BM website design
image_output: "_files_/"
convert_excalidraw: true
convert_format: "png"  # or "svg"
add_navigation: true
add_footer: true
relative_links: true
```

## How It Works

### 1. Parse Markdown
- Read source markdown file
- Extract YAML frontmatter
- Identify document structure (headers, lists, tables)

### 2. Convert Images
- Find all image references: `![[image.png]]`, `![[diagram.excalidraw.svg]]`
- Convert Excalidraw files to PNG/SVG using export functionality
- Copy images to output directory
- Update image paths in HTML

### 3. Process Wiki Links
- Find all wiki links: `[[Target Page]]`, `[[Target#Section]]`
- Resolve to actual file paths in vault
- Convert to relative HTML links
- Warn about broken links

### 4. Generate HTML
- Apply website template (navigation, footer, styles)
- Convert markdown to semantic HTML
- Add meta tags from frontmatter
- Include responsive CSS and JavaScript

### 5. Output File
- Write HTML file to specified location
- Copy referenced assets
- Report conversion summary

## Examples

### Example 1: Theory Article with Diagrams

**Input:** `Theory/Theory of AI4PKM (1) - Why PKM.md`

```markdown
---
title: "Theory of AI4PKM (1) - Why Knowledge"
tags: [ai4pkm, knowledge-management]
---

## 모든 것은 지식의 문제다

우리가 직장과 일상에서 흔히 겪는 문제를 생각해보자...

![[PKM-4-gaps.excalidraw.svg|688x347]]

| 문제 유형 | 마케팅 캠페인 사례 |
|---------|---------------|
| 지식 부족  | 새로운 트렌드를 모름 |
```

**Output:** `theory-part1.html` with:
- Converted Excalidraw diagram to PNG
- Responsive table styling
- Dark theme with gradient headers
- Navigation breadcrumbs

### Example 2: Blog Post with Images

**Input:** `Publish/Blog/2025-11-20 AI for PKM Guide.md`

```markdown
---
title: "Complete Guide to AI for PKM"
date: 2025-11-20
---

# Complete Guide to AI for PKM

![Overview diagram](diagrams/overview.png)

Learn about [[Theory of AI4PKM|the framework]]...
```

**Output:** `blog-ai-for-pkm.html` with:
- Image copied to website assets
- Wiki link converted to `theory.html`
- Blog post layout
- Proper meta tags

### Example 3: Batch Conversion

```
"Convert all Theory markdown files to HTML"
```

**Process:**
1. Finds: `Theory/*.md`
2. Converts each to: `theory-partN.html`
3. Links pages together (prev/next)
4. Converts all embedded images
5. Creates index page

## Dependencies

```bash
# Required Python packages
pip install markdown>=3.5.0
pip install Pillow>=10.0.0
pip install pyyaml>=6.0
pip install beautifulsoup4>=4.12.0

# Optional (for advanced features)
pip install cairosvg>=2.7.0  # SVG to PNG conversion
```

## Script Location

Main conversion script:
```
_Settings_/Skills/md2html/scripts/md_to_html.py
```

## Output Structure

```
_Sandbox_/Jin/Homepage/
├── theory.html              # Series index
├── theory-part1.html        # Individual pages
├── theory-part2.html
├── blog/
│   └── post-name.html
├── _files_/                 # Converted assets
│   ├── pkm-4-gaps.png
│   └── pkm-funnel.png
├── style.css               # Shared styles
└── script.js               # Shared scripts
```

## Best Practices

### 1. Image References
**Good:**
```markdown
![[diagram.excalidraw.svg|600x400]]
![[photo.png]]
```

**Avoid:**
```markdown
![](https://external-url.com/image.png)  # External URLs not copied
```

### 2. Wiki Links
**Good:**
```markdown
[[Theory of AI4PKM (1) - Why PKM]]  # Full filename
[[Theory of AI4PKM#section]]        # With section
```

**Avoid:**
```markdown
[[Why PKM]]  # Partial filename (may not resolve)
```

### 3. Frontmatter
**Good:**
```yaml
---
title: "Page Title"
description: "Brief description for SEO"
tags:
  - ai4pkm
  - knowledge-management
created: 2025-11-20
---
```

### 4. Table Structure
**Good:**
```markdown
| Header 1 | Header 2 |
|----------|----------|
| Cell 1   | Cell 2   |
```

## Troubleshooting

**Images not appearing:**
- Check Excalidraw files have `.excalidraw.svg` extension
- Verify image paths in markdown are correct
- Ensure output `_files_/` directory exists

**Wiki links broken:**
- Use full filenames including date prefix
- Check target files exist in vault
- Review conversion warnings for unresolved links

**Styling issues:**
- Verify `style.css` is in output directory
- Check HTML template is correctly applied
- Review browser console for CSS errors

**Excalidraw conversion fails:**
- Ensure Excalidraw CLI tools installed (if needed)
- Try converting to SVG instead of PNG
- Manually export diagrams from Obsidian

## Advanced Usage

### Custom Template

```
"Convert markdown using custom template at _Settings_/Templates/blog-template.html"
```

### Selective Image Conversion

```
"Convert markdown but keep Excalidraw as SVG (don't convert to PNG)"
```

### Dry Run

```
"Preview HTML conversion of Theory files without writing files"
```

## Integration with AI4BM Website

This skill is designed to work seamlessly with the AI4BM website structure:

- **Template**: Uses `_Sandbox_/Jin/Homepage/` as base
- **Styles**: Matches `style.css` (dark theme, gradient accents)
- **Navigation**: Auto-generates breadcrumbs and nav menu
- **Footer**: Includes standard social links
- **Animation**: Adds brain canvas background

## Workflow Example

1. **Write content** in vault: `Theory/New Article.md`
2. **Use skill**: "Convert Theory/New Article.md to HTML"
3. **Review output**: `_Sandbox_/Jin/Homepage/new-article.html`
4. **Adjust if needed**: Edit markdown and reconvert
5. **Deploy**: Copy HTML to production website

---

**Related Skills:**
- `markdown-to-docx` - Export to Word format
- `obsidian-links` - Validate wiki links
- `obsidian-markdown-structure` - Check document structure

**See also:** Homepage.md for website structure and content planning
