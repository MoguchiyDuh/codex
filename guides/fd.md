# fd Cheat Sheet (Modern Find)

`fd` is a simple, fast, and user-friendly alternative to the `find` command.

## 1. Installation

```bash
# Ubuntu/Debian
sudo apt install fd-find
alias fd='fdfind' # Often installed as fdfind

# Arch Linux
sudo pacman -S fd

# Fedora (dnf)
sudo dnf install fd-find

# Windows (via Chocolatey)
choco install fd

# macOS
brew install fd
```

---

## 2. Basic Search

Unlike `find`, `fd` uses regex by default and ignores `.gitignore` / hidden files.

```bash
fd pattern             # Search for files matching "pattern"
fd -L pattern          # Follow symbolic links
fd -I pattern          # Include ignored files (.gitignore)
fd -H pattern          # Include hidden files
fd -s pattern          # Case-sensitive search
```

---

## 3. Filtering

```bash
fd -e py               # Filter by extension (.py)
fd -t f                # Type: File (f), Directory (d), Symlink (l), Executable (x)
fd -p                  # Match against full path, not just filename
fd -S +10M             # Filter by size (+10MB, -1KB, etc.)
fd --changed-within 2d # Modified in the last 2 days
```

---

## 4. Execution

Run commands on every found file.

```bash
fd -e md -x cat        # Run 'cat' on every .md file found
fd -e jpg -x convert {} {.}.png # Convert all .jpg to .png
fd -e tmp -X rm        # Run 'rm' ONCE with all found files as arguments (much faster)
```

**Placeholder Legend:**

- `{}`: The path of the found item.
- `{.}`: The path without the extension.
- `{/}`: The basename (filename only).
- `{//}`: The parent directory.

---

## 5. Examples

```bash
# Find and delete all .DS_Store files
fd -H ".DS_Store" -X rm

# Find Python files containing 'import' (integration with ripgrep)
fd -e py -x rg "import"

# Find a directory and cd into it (using fzf)
cd $(fd -t d | fzf)
```

---
