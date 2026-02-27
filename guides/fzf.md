# fzf (Fuzzy Finder) Cheat Sheet

`fzf` is a general-purpose command-line fuzzy finder.

## 1. Installation

```bash
# Ubuntu/Debian
sudo apt install fzf

# Arch Linux
sudo pacman -S fzf

# Fedora (dnf)
sudo dnf install fzf

# Windows (via Chocolatey)
choco install fzf

# macOS
brew install fzf

# Setup shell integration (Keybindings & Auto-completion)
# After install, run:
source <(fzf --bash)  # Or --zsh / --fish
```

---

## 2. Default Shortcuts (Global)

| Key        | Action                                                     |
| :--------- | :--------------------------------------------------------- |
| **CTRL-T** | Search for files in current dir -> Paste into command line |
| **CTRL-R** | Search command history -> Paste/Run                        |
| **ALT-C**  | Fuzzy find directory -> `cd` into it                       |
| **TAB**    | Mark multiple items (in multi-mode `-m`)                   |

---

## 3. Search Syntax

| Pattern  | Description                                          |
| :------- | :--------------------------------------------------- |
| `sbtrkt` | Fuzzy match (matches `**s**u**b****t****r**a**kt**`) |
| `'wild`  | Exact match (quoted)                                 |
| `^music` | Prefix exact match                                   |
| `.mp3$`  | Suffix exact match                                   |
| `!fire`  | Inverse match (exclude)                              |
| `core`   | back OR match                                        |

---

## 4. Advanced Integration

### Use `fd` for faster indexing (ignores .git/hidden)

```bash
export FZF_DEFAULT_COMMAND='fd --type f'
```

### Previewing Files

```bash
# Preview file content using 'bat' or 'cat'
fzf --preview 'bat --style=numbers --color=always --line-range :500 {}'

# Preview images in terminal (requires kitty/iterm2/ueberzug)
fzf --preview 'kitten icat --clear --stdin no --place "${FZF_PREVIEW_COLUMNS}x${FZF_PREVIEW_LINES}@0x0" {}'
```

### Git Power Moves

```bash
# Checkout branch with preview
git branch | fzf --preview 'git log --oneline --graph --color=always {}' | xargs git checkout

# Fuzzy find a commit and show its diff
git log --oneline | fzf --preview 'git show --color=always {1}'
```

---

## 5. UI Customization

```bash
# Top-down layout with border
fzf --layout=reverse --border --height=40%

# One-liner for your .bashrc
export FZF_DEFAULT_OPTS='--height 40% --layout=reverse --border --color="bw"'
```
