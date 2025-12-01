#!/bin/bash
# AI4BM Vault Initialization Script
# Sets up Claude Code skills and Python dependencies

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Get the vault root directory (2 levels up from this script)
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
VAULT_ROOT="$( cd "$SCRIPT_DIR/../.." && pwd )"
SKILLS_DIR="$VAULT_ROOT/_Settings_/Skills"

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}AI4BM Vault Initialization${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""
echo -e "Vault location: ${YELLOW}$VAULT_ROOT${NC}"
echo ""

# Function to print status
print_status() {
    echo -e "${GREEN}✓${NC} $1"
}

print_error() {
    echo -e "${RED}✗${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}⚠${NC} $1"
}

# Check if Claude Code skills directory exists
echo -e "${BLUE}Step 1: Setting up Claude Code skills${NC}"
if [ ! -d ~/.claude/skills ]; then
    echo "Creating ~/.claude/skills directory..."
    mkdir -p ~/.claude/skills
    print_status "Created ~/.claude/skills directory"
else
    print_status "~/.claude/skills directory exists"
fi

# Symlink skills
echo ""
echo "Symlinking skills..."
SKILLS_CREATED=0
SKILLS_SKIPPED=0

cd "$SKILLS_DIR"
for skill in obsidian-links obsidian-yaml-frontmatter obsidian-markdown-structure markdown-to-docx interactive-writing-assistant youtube-transcript-skill; do
    if [ -d "$skill" ]; then
        TARGET_LINK=~/.claude/skills/"$skill"

        if [ -L "$TARGET_LINK" ]; then
            # Symlink exists, check if it points to the right place
            CURRENT_TARGET=$(readlink "$TARGET_LINK")
            if [ "$CURRENT_TARGET" = "$SKILLS_DIR/$skill" ]; then
                print_status "$skill (already linked)"
                SKILLS_SKIPPED=$((SKILLS_SKIPPED + 1))
            else
                print_warning "$skill (updating link)"
                rm "$TARGET_LINK"
                ln -sf "$SKILLS_DIR/$skill" "$TARGET_LINK"
                SKILLS_CREATED=$((SKILLS_CREATED + 1))
            fi
        elif [ -e "$TARGET_LINK" ]; then
            print_error "$skill (file exists but not a symlink - skipping)"
        else
            ln -sf "$SKILLS_DIR/$skill" "$TARGET_LINK"
            print_status "$skill (linked)"
            SKILLS_CREATED=$((SKILLS_CREATED + 1))
        fi
    else
        print_error "$skill directory not found"
    fi
done

echo ""
echo -e "Skills summary: ${GREEN}$SKILLS_CREATED created${NC}, ${YELLOW}$SKILLS_SKIPPED already linked${NC}"

# Check Python dependencies
echo ""
echo -e "${BLUE}Step 2: Checking Python dependencies${NC}"

# Check if pip is available
if ! command -v pip &> /dev/null && ! command -v pip3 &> /dev/null; then
    print_error "pip/pip3 not found. Please install Python first."
    echo "  See: https://www.python.org/downloads/"
    exit 1
else
    print_status "pip/pip3 found"
fi

# Determine pip command
PIP_CMD="pip"
if command -v pip3 &> /dev/null; then
    PIP_CMD="pip3"
fi

# Check if python-docx is installed
echo ""
echo "Checking python-docx (required for markdown-to-docx skill)..."
if $PIP_CMD show python-docx &> /dev/null; then
    VERSION=$($PIP_CMD show python-docx | grep Version | cut -d' ' -f2)
    print_status "python-docx $VERSION installed"
else
    print_warning "python-docx not installed"
    echo ""
    read -p "Install python-docx>=1.1.0? [Y/n] " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]] || [[ -z $REPLY ]]; then
        echo "Installing python-docx..."
        $PIP_CMD install "python-docx>=1.1.0"
        print_status "python-docx installed"
    else
        print_warning "Skipped python-docx installation (markdown-to-docx skill will not work)"
    fi
fi

# Verify skills are accessible
echo ""
echo -e "${BLUE}Step 3: Verifying installation${NC}"
VERIFIED=0
FAILED=0

for skill in obsidian-links obsidian-yaml-frontmatter obsidian-markdown-structure markdown-to-docx interactive-writing-assistant youtube-transcript-skill; do
    if [ -L ~/.claude/skills/"$skill" ] && [ -e ~/.claude/skills/"$skill" ]; then
        VERIFIED=$((VERIFIED + 1))
    else
        print_error "$skill not accessible"
        FAILED=$((FAILED + 1))
    fi
done

if [ $FAILED -eq 0 ]; then
    print_status "All $VERIFIED skills verified"
else
    print_error "$FAILED skills failed verification"
fi

# Summary
echo ""
echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}Setup Complete!${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

if [ $FAILED -eq 0 ]; then
    echo -e "${GREEN}✓ All skills are ready to use${NC}"
    echo ""
    echo "Next steps:"
    echo "  1. Open this vault in Obsidian"
    echo "  2. Start Claude Code in this directory"
    echo "  3. Skills will be automatically available"
else
    echo -e "${YELLOW}⚠ Setup completed with $FAILED errors${NC}"
    echo ""
    echo "Please review errors above and fix manually."
fi

echo ""
echo "For more information, see: _Settings_/Skills/Skills.md"
echo ""
