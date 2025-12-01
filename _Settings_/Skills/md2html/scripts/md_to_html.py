#!/usr/bin/env python3
"""
Markdown to HTML Converter for AI4BM Website
Converts vault markdown files to styled HTML pages with image conversion
"""

import re
import yaml
import argparse
import shutil
from pathlib import Path
from typing import Dict, List, Tuple, Optional
import markdown
from bs4 import BeautifulSoup


class MarkdownToHTMLConverter:
    """Convert markdown files to AI4BM website HTML pages"""

    def __init__(self, vault_root: Path, output_dir: Path, template_path: Optional[Path] = None):
        self.vault_root = Path(vault_root)
        self.output_dir = Path(output_dir)
        self.template_path = template_path
        self.images_output = output_dir / "_files_"
        self.images_output.mkdir(parents=True, exist_ok=True)

        # Markdown extensions
        self.md = markdown.Markdown(extensions=[
            'extra',      # tables, fenced code, etc.
            'codehilite', # syntax highlighting
            'toc',        # table of contents
            'nl2br',      # newline to <br>
        ])

    def extract_frontmatter(self, content: str) -> Tuple[Dict, str]:
        """Extract YAML frontmatter and return (frontmatter_dict, remaining_content)"""
        if not content.startswith('---'):
            return {}, content

        try:
            # Find the end of frontmatter
            parts = content.split('---', 2)
            if len(parts) >= 3:
                frontmatter_str = parts[1].strip()
                remaining = parts[2].strip()
                frontmatter = yaml.safe_load(frontmatter_str) or {}
                return frontmatter, remaining
        except Exception as e:
            print(f"Warning: Failed to parse frontmatter: {e}")

        return {}, content

    def convert_wiki_links(self, content: str) -> str:
        """Convert [[Wiki Links]] to HTML links"""
        # Pattern: [[Target]] or [[Target|Display]] or [[Target#Section]]
        pattern = r'\[\[([^\]|#]+)(?:#([^\]|]+))?(?:\|([^\]]+))?\]\]'

        def replace_link(match):
            target = match.group(1).strip()
            section = match.group(2).strip() if match.group(2) else None
            display = match.group(3).strip() if match.group(3) else target

            # Convert to HTML filename (simplified - assumes theory files)
            # More sophisticated logic would search vault for actual file
            html_file = self._resolve_wiki_link(target)
            if section:
                html_file += f"#{section.lower().replace(' ', '-')}"

            return f'<a href="{html_file}">{display}</a>'

        return re.sub(pattern, replace_link, content)

    def _resolve_wiki_link(self, target: str) -> str:
        """Resolve wiki link target to HTML filename"""
        # Simplified resolution - matches theory parts
        if "Why PKM" in target or "Part 1" in target:
            return "theory-part1.html"
        elif "Why AI for PKM" in target or "Part 2" in target:
            return "theory-part2.html"
        elif "AI4PKM Framework" in target or "Part 3" in target:
            return "theory-part3.html"
        elif "From Knowledge to Goals" in target or "Part 4" in target:
            return "theory-part4.html"
        elif "Theory of AI4PKM" in target:
            return "theory.html"
        else:
            # Default: convert to lowercase hyphenated
            return target.lower().replace(' ', '-') + ".html"

    def process_images(self, content: str, source_file: Path) -> str:
        """Find and process image references, return updated content"""
        # Pattern: ![[image.png]] or ![[image.png|widthxheight]]
        pattern = r'!\[\[([^\]|]+)(?:\|([^\]]+))?\]\]'

        def replace_image(match):
            image_name = match.group(1).strip()
            dimensions = match.group(2).strip() if match.group(2) else None

            # Find image in vault
            image_path = self._find_image(image_name, source_file)
            if not image_path:
                print(f"Warning: Image not found: {image_name}")
                return f"<!-- Image not found: {image_name} -->"

            # Convert Excalidraw if needed
            if image_path.suffix == '.svg' and 'excalidraw' in image_path.name:
                output_image = self._convert_excalidraw(image_path)
            else:
                # Copy image to output
                output_image = self.images_output / image_path.name
                shutil.copy2(image_path, output_image)

            # Generate HTML img tag
            rel_path = f"_files_/{output_image.name}"
            style = ""
            if dimensions:
                # Parse dimensions like "600x400"
                if 'x' in dimensions:
                    width, height = dimensions.split('x')
                    style = f' style="max-width:{width}px; max-height:{height}px;"'

            return f'<img src="{rel_path}" alt="{image_name}"{style}>'

        return re.sub(pattern, replace_image, content)

    def _find_image(self, image_name: str, source_file: Path) -> Optional[Path]:
        """Find image file in vault"""
        # Search in same directory as source file
        same_dir = source_file.parent / image_name
        if same_dir.exists():
            return same_dir

        # Search in attachments/assets folders
        for assets_dir in ['_files_', 'Assets', 'Attachments', 'Images']:
            asset_path = self.vault_root / assets_dir / image_name
            if asset_path.exists():
                return asset_path

        # Search entire vault (slower)
        for path in self.vault_root.rglob(image_name):
            return path

        return None

    def _convert_excalidraw(self, svg_path: Path) -> Path:
        """Convert Excalidraw SVG to PNG"""
        # For now, just copy the SVG
        # In production, could use cairosvg or similar to convert to PNG
        output_path = self.images_output / svg_path.name.replace('.excalidraw.svg', '.svg')
        shutil.copy2(svg_path, output_path)
        return output_path

    def generate_html(self, markdown_content: str, frontmatter: Dict, source_file: Path) -> str:
        """Generate complete HTML page from markdown content"""
        # Convert markdown to HTML
        html_content = self.md.convert(markdown_content)

        # Get title
        title = frontmatter.get('title', source_file.stem)
        description = frontmatter.get('description', '')

        # Build HTML page
        html = f"""<!DOCTYPE html>
<html lang="ko">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - AI for Better Me</title>
    <meta name="description" content="{description}">
    <link rel="stylesheet" href="style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link
        href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&family=Noto+Sans+KR:wght@300;400;500;700&display=swap"
        rel="stylesheet">
</head>

<body>
    <nav class="main-nav">
        <div class="container">
            <a href="index.html" class="nav-logo">AI for Better Me</a>
            <div class="nav-links">
                <a href="theory.html" class="nav-link">Framework</a>
                <a href="index.html#series" class="nav-link">Home</a>
            </div>
        </div>
    </nav>

    <header class="page-header">
        <div class="container">
            <div class="breadcrumb">
                <a href="index.html">Home</a>
                <span>/</span>
                <span>{title}</span>
            </div>
            <h1>{title}</h1>
        </div>
    </header>

    <section class="content">
        <div class="container">
            <div class="article-content">
                {html_content}
            </div>
        </div>
    </section>

    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-brand">
                    <h3>AI for Better Me</h3>
                    <p>Connect with us</p>
                </div>
                <div class="social-links">
                    <a href="https://lifidea.substack.com/" target="_blank" class="social-link">
                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none"
                            stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z" />
                            <polyline points="22,6 12,13 2,6" />
                        </svg>
                        Email List
                    </a>
                    <a href="https://jykim.github.io/AI4PKM/" target="_blank" class="social-link">
                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none"
                            stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path
                                d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22" />
                        </svg>
                        GitHub
                    </a>
                    <a href="https://www.youtube.com/@lifidea" target="_blank" class="social-link">
                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none"
                            stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path
                                d="M22.54 6.42a2.78 2.78 0 0 0-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 0 0-1.94 2A29 29 0 0 0 1 11.75a29 29 0 0 0 .46 5.33A2.78 2.78 0 0 0 3.4 19c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 0 0 1.94-2 29 29 0 0 0 .46-5.25 29 29 0 0 0-.46-5.33z" />
                            <polygon points="9.75 15.02 15.5 11.75 9.75 8.48 9.75 15.02" />
                        </svg>
                        YouTube
                    </a>
                    <a href="https://discord.gg/Bkfe5h4S" target="_blank" class="social-link">
                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 16 16"
                            fill="currentColor">
                            <path
                                d="M13.545 2.907a13.227 13.227 0 0 0-3.257-1.011.05.05 0 0 0-.052.025c-.141.25-.297.577-.406.833a12.19 12.19 0 0 0-3.653 0 2.039 2.039 0 0 0-.409-.833.051.051 0 0 0-.052-.025c-1.125.194-2.22.534-3.257 1.011a.041.041 0 0 0-.021.018C.356 6.024-.213 9.047.066 12.032c.001.014.01.028.021.037a13.276 13.276 0 0 0 3.995 2.02.05.05 0 0 0 .056-.019c.308-.42.582-.863.818-1.329a.05.05 0 0 0-.01-.059.051.051 0 0 0-.018-.011 8.875 8.875 0 0 1-1.248-.595.05.05 0 0 1-.02-.066.051.051 0 0 1 .015-.019c.084-.063.168-.129.248-.195a.05.05 0 0 1 .051-.007c2.619 1.196 5.454 1.196 8.041 0 a.052.052 0 0 1 .053.007c.08.066.164.132.248.195a.051.051 0 0 1-.004.085 8.254 8.254 0 0 1-1.249.594.05.05 0 0 0-.03.03.05.05 0 0 0 .003.029c.243.466.518.909.818 1.329a.05.05 0 0 0 .056.019 13.235 13.235 0 0 0 4.001-2.02.049.049 0 0 0 .021-.037c.334-3.451-.559-6.449-2.366-9.106a.034.034 0 0 0-.02-.019Zm-8.198 7.307c-.789 0-1.438-.724-1.438-1.612 0-.889.637-1.613 1.438-1.613.807 0 1.45.724 1.438 1.613 0 .888-.637 1.612-1.438 1.612Zm5.316 0c-.788 0-1.438-.724-1.438-1.612 0-.889.637-1.613 1.438-1.613.807 0 1.451.724 1.438 1.613 0 .888-.631 1.612-1.438 1.612Z" />
                        </svg>
                        Discord
                    </a>
                </div>
            </div>
            <div class="copyright">
                &copy; 2025 AI for Better Me. All rights reserved.
            </div>
        </div>
    </footer>
    <canvas id="brain-canvas"></canvas>
    <script src="script.js"></script>
</body>

</html>"""

        return html

    def convert_file(self, source_file: Path, output_name: Optional[str] = None) -> Path:
        """Convert a markdown file to HTML"""
        print(f"Converting: {source_file}")

        # Read source file
        content = source_file.read_text(encoding='utf-8')

        # Extract frontmatter
        frontmatter, md_content = self.extract_frontmatter(content)

        # Process wiki links
        md_content = self.convert_wiki_links(md_content)

        # Process images
        md_content = self.process_images(md_content, source_file)

        # Generate HTML
        html = self.generate_html(md_content, frontmatter, source_file)

        # Write output file
        if not output_name:
            output_name = source_file.stem.lower().replace(' ', '-') + '.html'
        output_file = self.output_dir / output_name
        output_file.write_text(html, encoding='utf-8')

        print(f"✓ Created: {output_file}")
        return output_file


def main():
    parser = argparse.ArgumentParser(description='Convert markdown to HTML for AI4BM website')
    parser.add_argument('input', type=Path, help='Input markdown file or directory')
    parser.add_argument('-o', '--output', type=Path, help='Output directory',
                        default=Path('_Sandbox_/Jin/Homepage/'))
    parser.add_argument('-v', '--vault', type=Path, help='Vault root directory',
                        default=Path.cwd())
    parser.add_argument('-n', '--name', help='Output filename (for single file conversion)')

    args = parser.parse_args()

    # Initialize converter
    converter = MarkdownToHTMLConverter(args.vault, args.output)

    # Convert file(s)
    if args.input.is_file():
        converter.convert_file(args.input, args.name)
    elif args.input.is_dir():
        for md_file in args.input.glob('*.md'):
            try:
                converter.convert_file(md_file)
            except Exception as e:
                print(f"Error converting {md_file}: {e}")
    else:
        print(f"Error: {args.input} not found")
        return 1

    print("\n✓ Conversion complete!")
    return 0


if __name__ == '__main__':
    exit(main())
