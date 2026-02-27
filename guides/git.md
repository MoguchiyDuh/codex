# Git Cheat Sheet

## Configuration

```bash
git config --global user.name "Name"
git config --global user.email "email@example.com"
```

---

## Local Development

```bash
git init                  # Initialize repo
git status                # Check state
git add <file>            # Stage file (. for all)
git add -p                # Interactive stage (hunks)
git rm <file>             # Remove from index and disk
git rm --cached <file>    # Remove from index only (keep on disk)
git commit -v             # Commit with diff preview
git commit -m "msg"       # Commit staged
git commit -am "msg"      # Add MODIFIED files and commit (skips untracked)
git commit --amend        # Edit last commit + message
git commit --amend --no-edit # Add changes to last commit
git diff                  # Show unstaged changes
git diff --staged         # Show staged changes
git show <hash>           # Show changes in commit
```

### .gitignore example

```text
# Dependencies
node_modules/
__pycache__/

# OS files
.DS_Store
Thumbs.db

# Secrets & Config
.env
.vscode/
```

### Undo & Restore

```bash
git restore <file>        # Discard local changes
git restore --staged <f>  # Unstage file
git reset HEAD~1          # Undo commit, keep changes (unstaged)
git reset --soft HEAD~1   # Undo commit, keep changes (staged)
git reset --hard HEAD~1   # Undo commit, DELETE changes
```

---

## Branching

```bash
git branch                # List branches
git switch <name>         # Switch branch (modern)
git switch -c <name>      # Create and switch (modern)
git checkout <name>       # Switch branch
git checkout -b <name>    # Create and switch
git checkout -            # Switch to previous branch
git merge <branch>        # Merge into current
git branch -d <name>      # Delete branch
```

---

## Remotes & Syncing

```bash
git clone <url>           # Clone repository
git remote -v             # List remotes
git remote add <name> <u> # Add remote
git remote set-url <n> <u> # Update URL
git fetch <remote>        # Download metadata
git pull <remote> <branch># Fetch + Merge
git pull --rebase <r> <b> # Fetch + Rebase (cleaner)
git push <remote> <branch># Upload commits
git push -u <r> <b>        # Push and set upstream
git remote prune <remote> # Clean stale remote refs
```

---

## History Integration

### Rebase & Merge

- **Merge**: Preserves history with a merge commit.
- **Rebase**: Replays commits on a new base for linear history.

```bash
git rebase <branch>       # Rebase current onto <branch>
git rebase -i HEAD~n      # Interactive: squash/edit commits
```

### Cherry-Pick

```bash
git cherry-pick <hash>    # Apply specific commit to current branch
```

---

## Tags

```bash
git tag                   # List tags
git tag -a v1.0 -m "msg"  # Create annotated tag
git push origin v1.0      # Push specific tag
git push origin --tags    # Push all tags
```

---

## Conflict Resolution

1. Fix conflicts in files.
2. `git add <file>`
3. `git merge --continue` OR `git rebase --continue`

_Aborting:_ `git merge --abort` or `git rebase --abort`

---

## Utilities

```bash
git log --oneline --graph --all # Visual history (all branches)
git log -p                # Full history with patches
git reflog                # Recovery: history of HEAD moves
git reset --hard <hash>   # Reset to any state from reflog
git stash                 # Save uncommitted work
git stash list            # List stashed changes
git stash apply           # Restore stash (keep in list)
git stash pop             # Restore stash (remove from list)
git blame <file>          # Line-by-line authorship
git clean -fd             # Delete untracked files/dirs
```

---

## Search

```bash
git grep "pattern"        # Search text in codebase
git log -S "string"       # Find commits that changed string
git log --grep "msg"      # Search commit messages
```

---

## Ecosystem Tools

- **[lazygit](https://github.com/jesseduffield/lazygit)**: Full TUI for fast staging, rebasing, and history inspection.
- **[gh (GitHub CLI)](https://cli.github.com/)**: Manage PRs, issues, and repos directly from the terminal.

---

## Glossary & Abbreviations

| Term     | Full Name                | Description                                                                      |
| :------- | :----------------------- | :------------------------------------------------------------------------------- |
| **CLI**  | Command Line Interface   | Tools used by typing text into a terminal.                                       |
| **TUI**  | Terminal User Interface  | Graphical interface built using text characters in a terminal (e.g., `lazygit`). |
| **PR**   | Pull Request             | A GitHub/GitLab mechanism to review code changes before merging.                 |
| **URL**  | Uniform Resource Locator | The address of a remote repository.                                              |
| **HEAD** | -                        | A reference to the current checked-out commit.                                   |
