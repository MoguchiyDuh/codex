# ripgrep (rg) Cheat Sheet

`ripgrep` is a line-oriented search tool that recursively searches the current directory for a regex pattern.

## 1. Installation

```bash
# Ubuntu/Debian
sudo apt install ripgrep

# Arch Linux
sudo pacman -S ripgrep

# Fedora (dnf)
sudo dnf install ripgrep

# Windows (via Chocolatey)
choco install ripgrep

# macOS
brew install ripgrep
```

---

## 2. Basic Search

By default, `rg` respects `.gitignore` and skips hidden files/binary files.

```bash
rg pattern              # Search for "pattern" in current dir
rg pattern <file/dir>   # Search in specific location
rg -i pattern           # Case-insensitive
rg -w pattern           # Match whole word only
rg -F string            # Fixed string search (no regex)
rg -v pattern           # Invert match (lines NOT matching)
```

---

## 3. Filtering & Scope

```bash
rg -u pattern           # Include hidden files
rg -uu pattern          # Include hidden + ignored files (.gitignore)
rg -t py pattern        # Search only in Python files
rg -T js pattern        # Exclude JavaScript files
rg -g "*.md" pattern    # Glob: search only in markdown files
rg -g "!tests/*" pattern # Glob: exclude tests directory
```

---

## 4. Context & Output

```bash
rg -C 3 pattern         # Show 3 lines of context (Above + Below)
rg -A 3 pattern         # Show 3 lines AFTER
rg -B 3 pattern         # Show 3 lines BEFORE
rg -l pattern           # List only filenames with matches
rg -c pattern           # Count matches per file
rg --vimgrep pattern    # Output format for Vim/Neovim (file:line:col:text)
```

---

## 5. Advanced Power Moves

```bash
# Replace: Search for 'foo' and replace with 'bar' in output (not disk)
rg foo --replace bar

# Use PCRE2 engines (for look-ahead/look-behind)
rg -P "(?<=foo)bar"

# Search for multiline patterns
rg -U "start\n.*end"

# Stats: See how many files/lines were searched
rg pattern --stats
```

---

## 6. Configuration

You can set default flags in a `.ripgreprc` file.

```bash
# Export the path in your .bashrc / .zshrc
export RIPGREP_CONFIG_PATH="$HOME/.ripgreprc"
```

**Example `.ripgreprc`:**

```text
--smart-case
--max-columns=150
--max-columns-preview
--type-add
web:*.{html,css,js}*
```
