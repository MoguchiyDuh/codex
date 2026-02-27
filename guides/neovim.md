# Neovim Ultimate Cheat Sheet

**Active Setup**: Modular Lua config (lazy.nvim + OneDark) optimized for `uv`/Python on Neovim 0.12-dev.

**Key Binds**: `<C-s>` (Save), `<C-q>` (Quit), `<C-b>` (Buffers), `<C-n>` (Tree), `<C-/>` (Comment), `<leader>gD` (Diff), `Tab` (Next Buffer).

**AI Integration**: `<leader>cc` (CodeCompanion Chat), `<leader>ca` (Actions), Visual `ga` (Add to chat).

---

## 1. Navigation & Motion

### Basic & Word

```text
h j k l                   # Left, Down, Up, Right
w / b                     # Next / Previous word start
e / ge                    # Next / Previous word end
W / B / E                 # Move by "WORDS" (ignores punctuation)
( / )                     # Previous / Next sentence
{ / }                     # Previous / Next paragraph
```

### Horizontal (Line)

```text
0                         # Absolute start of line (col 1)
^                         # First non-blank character
$                         # End of line
g_                        # Last non-blank character
f / t <char>              # Find / To character (forward)
F / T <char>              # Find / To character (backward)
; / ,                     # Repeat last f/t/F/T (forward / backward)
```

### Vertical (File)

```text
gg / G                    # Top / Bottom of file
<num>G or :<num>          # Go to line <num>
H / M / L                 # High / Middle / Low of current screen
%                         # Match bracket ( { [
```

### Global / Cross-File

```text
<C-o>                     # Jump BACK to previous position (cross-file)
<C-i>                     # Jump FORWARD to next position
<C-^>                     # Toggle between current and last (alternate) file
:jumps                    # View the jump list
```

### Scrolling

```text
<C-u> / <C-d>             # Up / Down (half page)
<C-b> / <C-f>             # Back / Forward (full page)
zz / zt / zb              # Center / Top / Bottom cursor line on screen
```

---

## 2. Editing & Verbs (Operators)

Vim works like a language: `Verb + Count + Noun`.

### Basic Verbs

```text
i / a / s / x             # Insert / Append / Substitute char / Delete char
o / O                     # New line below / above
r / R                     # Replace char / Enter Replace mode
c / d / y                 # Change / Delete / Yank (copy)
~                         # Switch case
gu / gU                   # Lowercase / Uppercase
=                         # Auto-indent
```

### Insert Mode Shortcuts

```text
Ctrl+h / Ctrl+w           # Delete char / word before cursor
Ctrl+u                    # Delete line before cursor
Ctrl+r {reg}              # Paste from {reg} without leaving insert
Ctrl+o                    # Execute ONE normal mode command
```

### Nouns (Text Objects)

Used with verbs (e.g., `ciw` - "Change Inside Word").

```text
iw / aw                   # Inner / Around Word
is / as                   # Inner / Around Sentence
ip / ap                   # Inner / Around Paragraph
i( / a(                   # Inner / Around brackets (or "b")
i{ / a{                   # Inner / Around braces (or "B")
it / at                   # Inner / Around HTML/XML tags
i' / i" / i`              # Inner quotes
```

### Power Combos (Editing)

```text
ciw                       # Change inside word (best for renaming)
ci"                       # Change inside quotes
ci(                       # Change inside parentheses
cit                       # Change inside HTML/XML tags
C                         # Change from cursor to end of line
S                         # Delete current line and start insert
xp                        # Swap two characters (delete and paste)
ddp                       # Swap two lines (delete line and paste below)
>i{                       # Indent the current code block
gg=G                      # Auto-format/indent entire file
```

---

## 3. Visual Mode & Selection

```text
v                         # Visual mode (character)
V                         # Visual Line mode
<C-v>                     # Visual Block mode (column editing)
gv                        # Reselect last selection
o                         # Jump to other end of selection
```

### Visual Block Power

```text
<C-v>jjI// <Esc>          # Comment out multiple lines
<C-v>jjA; <Esc>           # Append ';' to multiple lines
```

### Power Combos (Selection)

```text
viwP                      # Select word and paste over it (stays in register)
yiw                       # Yank (copy) current word
ggVG                      # Select entire file
```

---

## 4. Registers (Copy & Paste)

Vim has multiple clipboards ("registers"). Use them with `"` (e.g., `"ay` yanks into register `a`).

```text
""                        # Unnamed register (default d, c, x, y)
"0                        # Last yank (useful if you delete and lose unnamed)
"_                        # Black hole register (deletes without copying)
"+ / "*                   # System clipboard / Primary selection
": / ". / "%              # Last cmd / Last inserted text / Current filename

p / P                     # Paste after / before cursor
]p / [p                   # Paste with auto-indent
:reg                      # List contents of all registers
```

---

## 5. Marks (Bookmarks)

```text
m<a-z>                    # Set local mark (per file)
m<A-Z>                    # Set global mark (across files)
'<mark>                   # Jump to start of line of mark
`<mark>                   # Jump to exact position (row/col) of mark
''                        # Jump back to position before last jump
:marks                    # List all marks
```

---

## 6. Macros (Recording)

```text
q<letter>                 # Start recording macro into register <letter>
q                         # Stop recording
@<letter>                 # Play macro
@@                        # Play last macro
<num>@<letter>            # Play macro <num> times
```

---

## 7. Buffers, Windows & Tabs

### Buffers (Open Files)

```text
:ls / :buffers            # List open buffers
:bn / :bp                 # Next / Previous buffer
:b<num>                   # Go to buffer #
:bd                       # Delete (close) buffer

# Time Travel
:earlier 2m               # Go to state 2 mins ago
:later 2m                 # Go forward in state
```

### Windows (Splits)

```text
<C-w> v / s               # Split Vertical / Horizontal
<C-w> h/j/k/l             # Move focus (Left/Down/Up/Right)
<C-w> H/J/K/L             # Move the split itself
<C-w> = / _ / |           # Equalize / Max Height / Max Width
<C-w> c / q               # Close / Quit split
```

### Tabs

```text
:tabnew / :tabclose       # New / Close tab
:tabn / :tabp             # Next / Previous tab
gt / gT                   # Shortcuts for Next/Prev tab
```

---

## 8. Search & Replace (Command Line)

### Basic Syntax: `:[range]s/pattern/replacement/[flags]`

```text
/pattern                  # Search forward
?pattern                  # Search backward
n / N                     # Next / Previous match
* / #                     # Search word under cursor (forward/backward)
*N                        # Find word under cursor, then jump back to it
```

### Common Replace Examples

```text
:s/old/new/               # Replace first "old" in CURRENT line
:s/old/new/g              # Replace ALL "old" in CURRENT line
:%s/old/new/g             # Replace ALL "old" in ENTIRE file
:%s/old/new/gc            # Global replace with confirmation (y/n/a/q)
:5,10s/old/new/g          # Replace between lines 5 and 10
:'<,'>s/old/new/g         # Replace in Visual Selection
```

### Advanced Patterns & Regex

```text
:%s/\s\+$//               # Remove all trailing whitespace
:%s/old/new/gi            # Case-insensitive replace
:%s/foo/bar/gn            # COUNT occurrences without replacing
:%s/<C-r><C-w>/new/g      # Replace word under cursor with "new"
```

### Groups & Capture (Backreferences)

Vim requires escaping the parentheses `\(\)` unless you use `\v` (very magic).

```text
:%s/\(foo\)bar/\1baz/g    # Groups: "foobar" -> "foobaz" (\1 refers to group 1)
:%s/\v(foo)bar/\1baz/g    # Same as above, using \v (Very Magic)
:%s/\(\w\+\)\s\+\(\w\+\)/\2 \1/ # Swap two words
```

### Selection / Search Feedback

```text
:set hlsearch             # Highlight all matches
:set incsearch            # Show matches while typing
:nohlsearch or :noh       # Clear temporary highlighting

# Specialized Modes
:set spell                # Enable spell check (z= for suggestions)
]c / [c                   # Next / Previous diff change
```

### Multiple Files (Grep)

```text
:vimgrep /pattern/ **/*   # Search "pattern" in current dir (recursive)
:copen                    # Open Quickfix window with grep results
:cn / :cp                 # Jump to Next / Previous grep match
```

---

## 9. Modern Neovim & LSP

```text
:Lazy                     # Plugin manager
:Mason                    # LSP/Linter/Formatter installer
:checkhealth              # Check setup health

K                         # LSP Hover (Documentation)
gd / gD                   # Go to Definition / Declaration
gr                        # Go to References
gi                        # Go to Implementation
<leader>rn                # Rename symbol (LSP)
<leader>ca                # Code Action
```

---

## 10. Advanced Utilities

### Folds

```text
zf                        # Create fold (Visual selection)
za                        # Toggle fold
zi                        # Toggle all folds
zd                        # Delete fold
```

### External & Shell

```text
:!ls                      # Execute shell command
:r !date                  # Read output of command into file
!!sh                      # Replace line with command output
```

### The Jump List

```text
<C-o>                     # Jump back (older position)
<C-i>                     # Jump forward (newer position)
:jumps                    # View jump list
```

---

## 11. Command Line (:) Power

The command line is a full-featured prompt. Use `q:` to open it as a buffer for editing history.

### File & Environment

```text
:e!                       # Reload current file (discard changes)
:saveas <name>            # "Save As"
:w !sudo tee %            # Save file as root (Linux/macOS)
:cd %:p:h                 # Change directory to current file's folder
:e $MYVIMRC               # Edit your config file
```

### Command History & Navigation

```text
q:                        # Open command history in a buffer (Searchable/Editable)
q/                        # Open search history in a buffer
:<Up/Down>                # Cycle history (filtered if you've typed anything)
<C-f>                     # Switch from command line to history buffer
```

### Multiple Buffer / Window Operations

```text
:bufdo <cmd>              # Run command in ALL open buffers
:windo <cmd>              # Run command in ALL open windows
:argdo %s/old/new/ge | update # Replace in all files in argument list
```

### Options & Settings

```text
:set <opt>?               # Check value of an option
:set no<opt>              # Disable an option
:set inv<opt>             # Toggle an option
:scriptnames              # List all loaded scripts/plugins
:map / :nmap              # List all (or normal mode) keybindings
```

---

## 12. Personal Config: Details & Keybinds

### Current Stack (lazy.nvim)

- **UI**: [OneDark](https://github.com/navarasu/onedark.nvim) (Transparent), [lualine](https://github.com/nvim-lualine/lualine.nvim), [bufferline](https://github.com/akinsho/bufferline.nvim), [alpha-nvim](https://github.com/goolord/alpha-nvim)
- **Explorer**: [Nvim-Tree](https://github.com/nvim-tree/nvim-tree.lua)
- **Fuzzy Finder**: [Telescope](https://github.com/nvim-telescope/telescope.nvim) (+ fzf-native)
- **Syntax**: [Treesitter](https://github.com/nvim-treesitter/nvim-treesitter), [render-markdown](https://github.com/MeanderingProgrammer/render-markdown.nvim)
- **LSP**: [Mason](https://github.com/williamboman/mason.nvim), [nvim-lspconfig](https://github.com/neovim/nvim-lspconfig), [SchemaStore.nvim](https://github.com/b0o/SchemaStore.nvim)
- **Completion**: [nvim-cmp](https://github.com/hrsh7th/nvim-cmp) (LSP, Buffer, Path, LuaSnip)
- **Snippets**: [LuaSnip](https://github.com/L3MON4D3/LuaSnip) (+ friendly-snippets)
- **Format/Lint**: [Conform.nvim](https://github.com/stevearc/conform.nvim), [nvim-lint](https://github.com/mfussenegger/nvim-lint)
- **AI**: [CodeCompanion.nvim](https://github.com/olimorris/codecompanion.nvim) (Ollama/qwen3)
- **Utilities**: [Flash.nvim](https://github.com/folke/flash.nvim), [nvim-surround](https://github.com/kylechui/nvim-surround), [Comment.nvim](https://github.com/numToStr/Comment.nvim), [lazygit.nvim](https://github.com/kdheepak/lazygit.nvim), [gitsigns](https://github.com/lewis6991/gitsigns.nvim), [nvim-autopairs](https://github.com/windwp/nvim-autopairs), [which-key](https://github.com/folke/which-key.nvim), [suda.vim](https://github.com/lambdalisue/suda.vim)

### ⌨️ Custom Keybinds Reference

| Category                 | Keybind               | Action                                 |
| :----------------------- | :-------------------- | :------------------------------------- |
| **General**              | `<C-s>`               | Save file                              |
|                          | `<C-q>`               | Quit file                              |
|                          | `<leader>w` / `W`     | Save / Force Save                      |
|                          | `<leader>q` / `Q`     | Quit / Force Quit All                  |
|                          | `<Esc>`               | Clear search highlights                |
|                          | `<C-_>` (`Ctrl+/`)    | Toggle comment                         |
|                          | `<C-t>`               | Open terminal                          |
| **Navigation**           | `<C-h/j/k/l>`         | Move between splits                    |
|                          | `<Tab>` / `<S-Tab>`   | Next / Previous buffer                 |
|                          | `<C-b>`               | Buffer picker (Telescope)              |
|                          | `<leader>fb`          | Find buffers (Telescope)               |
|                          | `<leader>bn / bp`     | Next / Previous buffer                 |
|                          | `<leader>bd / bD`     | Smart Close / Force Close buffer       |
|                          | `<leader>1-9`         | Jump to buffer 1-9                     |
|                          | `s / S`               | Flash Jump / Treesitter Search         |
| **Splits**               | `<leader>sv`          | Vertical split                         |
|                          | `<leader>sx`          | Horizontal split                       |
|                          | `<leader>sc`          | Close split                            |
|                          | `<leader>se`          | Equalize splits                        |
| **Editing**              | `<A-j / k>`           | Move line/selection Down / Up          |
|                          | `< / >`               | Indent left/right (Visual mode stays)  |
|                          | `gcc`                 | Toggle line comment                    |
|                          | `gc` + motion         | Toggle comment (motion)                |
|                          | `<leader>F`           | Format buffer (Conform)                |
| **File Tree (NvimTree)** | `<C-n>`               | Toggle Nvim-Tree                       |
|                          | `<Enter>` / `o`       | Open file                              |
|                          | `v`                   | Open in vertical split                 |
|                          | `x`                   | Open in horizontal split               |
|                          | `t`                   | Open in new tab                        |
|                          | `h` / `l`             | Close / Open directory                 |
| **Finding**              | `<leader>ff`          | Find files (Telescope)                 |
|                          | `<leader>fg`          | Find git files                         |
|                          | `<leader>fs`          | Live grep (Interactive)                |
| **LSP**                  | `K`                   | Hover Documentation                    |
|                          | `gd / gD`             | Go to Definition / Declaration         |
|                          | `gi / gt`             | Go to Implementation / Type Definition |
|                          | `gr`                  | Show References (Telescope)            |
|                          | `<leader>ca`          | Code Actions                           |
|                          | `<leader>rn`          | Rename symbol                          |
|                          | `<leader>e`           | Show line diagnostics float            |
|                          | `[d / ]d`             | Previous / Next diagnostic             |
|                          | `<C-k>` (Ins)         | Signature help                         |
| **Git (Gitsigns)**       | `<leader>gd`          | Preview hunk diff (popup)              |
|                          | `<leader>gD`          | Full file diff (split)                 |
|                          | `<leader>gb`          | Blame line                             |
|                          | `]h / [h`             | Next / Previous hunk                   |
|                          | `<leader>gs`          | Stage hunk                             |
|                          | `<leader>gu`          | Undo stage hunk                        |
|                          | `<leader>gr`          | Reset hunk                             |
| **Git (LazyGit)**        | `<leader>gg`          | Open LazyGit                           |
| **AI (CodeCompanion)**   | `<leader>cc`          | Toggle Chat                            |
|                          | `<leader>ca`          | Actions Menu                           |
|                          | `ga` (Visual)         | Add selection to chat                  |
|                          | `<leader>cf` (Visual) | Fix code (Inline)                      |
|                          | `<leader>co` (Visual) | Optimize code (Inline)                 |
|                          | `<leader>cp` (Visual) | Complete code (Inline)                 |

---

## Known Issues (Neovim 0.12-dev)

**Telescope Preview - Lua Files Only:**

- Error: `Query error at 74:3. Invalid field name "operator"` when previewing `.lua` files
- **Cause**: Nvim 0.12-dev bundles lua/c/vim parsers with incompatible/broken queries
- **Impact**: Preview still works, just shows error spam
- **Fix**: Wait for 0.12 stable release, or downgrade to 0.11.x
- **Workaround**: Avoid previewing lua files, or disable treesitter in telescope

**Parser Conflicts:**

- Nvim 0.12+ includes built-in parsers: `lua, c, vim, vimdoc, query`
- Don't install these via nvim-treesitter (already excluded in config)
- Other languages (python, rust, cpp, etc.) work fine

---

## Glossary & Abbreviations

| Term         | Full Name                | Description                                                                           |
| :----------- | :----------------------- | :------------------------------------------------------------------------------------ |
| **LSP**      | Language Server Protocol | Protocol for IDE-like features (e.g., auto-complete, go-to-definition).               |
| **CMP**      | Completion               | Refers to `nvim-cmp`, the standard completion engine for Neovim.                      |
| **TUI**      | Terminal User Interface  | Text-based interface used in the terminal (unlike the GUI `nvim-qt`).                 |
| **CLI**      | Command Line Interface   | The text-based prompt where you type commands.                                        |
| **MVP**      | Minimum Viable Product   | Used in this guide to denote essential, high-impact command combinations.             |
| **VIMRC**    | Vim Run Control          | The traditional name for Vim's configuration file (replaced by `init.lua` in Neovim). |
| **Buffer**   | -                        | An in-memory representation of a file (what you are currently editing).               |
| **Register** | -                        | A named storage location for text (clipboards).                                       |
| **Hunk**     | -                        | A contiguous block of changed code (used in Git/diff context).                        |
