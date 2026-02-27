# Tmux Ultimate Cheat Sheet (Personalized)

**Prefix**: `Ctrl-a` (Standard `C-b` is unbound)

---

## 1. Installation

\`\`\`bash
# Arch Linux
sudo pacman -S tmux

# Fedora (dnf)
sudo dnf install tmux

# Ubuntu/Debian
sudo apt install tmux

# Windows (via Chocolatey)
choco install tmux
\`\`\`

---

## 2. Session Management

Sessions are persistent environments. Your config adds specific shortcuts.

### CLI Commands
\`\`\`bash
tmux new -s <name>        # Create a named session
tmux ls                   # List all active sessions
tmux attach -t <name>     # Attach to a specific session
tmux rename-session -t <old> <new> # Rename session
tmux kill-session -t <name> # Kill a specific session
tmux kill-server          # Kill all sessions and the server
\`\`\`

### Your Bindings
\`\`\`text
Prefix + C-c              # Create New Session
Prefix + C-x              # Kill Current Session
\`\`\`

---

## 3. Windows & Panes (The Vim Way)

Your setup uses a "Vim-style" philosophy for movement and management.

### Panes (Splits)
\`\`\`text
Prefix + s                # Horizontal Split (current path)
Prefix + v                # Vertical Split (current path)
Prefix + x                # Kill Current Pane

# Navigation (Vim Keys)
Prefix + h / j / k / l    # Move Left / Down / Up / Right

# Resizing (Vim Keys - Repeatable)
Prefix + H / J / K / L    # Resize Left / Down / Up / Right (step of 5)
\`\`\`

### Windows (Tabs)
\`\`\`text
Prefix + c                # New Window (current path)
Prefix + X                # Kill Current Window
Prefix + C-h / C-l        # Previous / Next Window
Prefix + < / >            # Swap Window Left / Right
\`\`\`

---

## 4. Copy Mode & Buffers

Used for scrolling through history and yanking text.

\`\`\`text
Prefix + [                # Enter Copy Mode (Vi Mode active)
\`\`\`

### Vi Bindings (Inside Copy Mode)
\`\`\`text
v                         # Begin Selection
C-v                       # Toggle Rectangle Selection
y                         # Yank (Copy) Selection
Y                         # Yank Entire Line
/                         # Search Down (Incremental)
?                         # Search Up (Incremental)
n / N                     # Next / Previous Search Match
q                         # Exit Copy Mode
\`\`\`

### Pasting
\`\`\`text
Prefix + p                # Paste last yanked buffer
\`\`\`

---

## 5. Global CLI Utilities

Useful for debugging or scripting Tmux.

\`\`\`bash
tmux list-keys            # List all active bindings
tmux list-commands        # List all valid tmux commands
tmux source-file <path>   # Manually reload a config
tmux info                 # Show server/terminal information
\`\`\`

**Your Reload Shortcut**:
\`\`\`text
Prefix + r                # Reload ~/.config/tmux/tmux.conf
\`\`\`

---

### Plugins

| Plugin               | Feature                                                 |
| :------------------- | :------------------------------------------------------ |
| **Resurrect**        | Save/Restore sessions manually.                         |
| **Continuum**        | Auto-saves sessions every 15 minutes.                   |
| **Prefix-Highlight** | Visual indicator on status bar when \`Prefix\` is active. |
| **gitmux**           | Dynamic Git status in your status bar.                  |

---
