# uv Cheat Sheet

## Installation

```bash
# Universal (Linux/macOS)
curl -fsSL https://astral.sh/uv/install.sh | sh

# Maintenance
uv self update            # Update uv to latest version
uv version                # Check current uv version

# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

---

## Python Management

```bash
uv python list            # List available Python versions
uv python install 3.12    # Install specific Python version
uv python find            # Find installed Python versions
```

---

## Project Management

```bash
uv init                   # Initialize a new project
uv add <package>          # Add dependency
uv add "pkg>=1.0"         # Version constraint
uv add --dev <package>    # Add dev dependency
uv add git+https://...    # Git dependency
uv add --path ../lib      # Local path dependency
uv remove <package>       # Remove dependency
uv sync                   # Sync project (install dependencies)
uv tree                   # Show dependency tree
uv lock                   # Update lockfile without syncing
```

---

## Running Scripts & Tools

```bash
uv run <script.py>        # Run a script in a managed environment
uv run <command>          # Run an installed tool (e.g., ruff, pytest)
uvx <tool>                # Run a tool without installing (like npx)
```

### Script Metadata (PEP 723)

Run single-file scripts with dependencies (automatically managed):

```python
# script.py
# /// script
# dependencies = ["requests", "rich"]
# ///
import requests
from rich import print
...
```

`uv run script.py` (installs deps in a temporary, cached environment).

---

## Tool Management

```bash
uv tool install <tool>    # Install tool globally in isolated env
uv tool list              # List installed tools
uv tool upgrade <tool>    # Upgrade a specific tool
uv tool upgrade --all     # Upgrade all tools
uv tool uninstall <tool>  # Uninstall a tool
uv tool run <tool>        # Run an installed tool
```

---

## Virtual Environments

```bash
uv venv                   # Create .venv
source .venv/bin/activate # Activate (Linux/macOS)
.venv\Scripts\activate   # Activate (Windows)
```

---

## Pip Replacement (Fast)

```bash
uv pip install -r req.txt # Fast pip install
uv pip freeze             # List installed packages
uv pip compile pyproject.toml -o requirements.txt # Lock dependencies
```

---

## Cleanup & Cache

```bash
uv cache clean            # Remove all cache
uv cache prune            # Remove unused cache
```

---

## Build & Publish

```bash
uv build                  # Build source and wheel distributions
uv publish                # Upload to PyPI
```

---

## Workspaces & CI/CD

```bash
uv init --workspace       # Create a new workspace
uv add --workspace <pkg>  # Add package to workspace

# CI/CD & Enforcement
uv sync --frozen          # Sync ONLY if lockfile is up-to-date
uv sync --locked          # Error if lockfile would be changed
uv run --offline <cmd>    # Run without network access
```

---

## Glossary & Abbreviations

| Term         | Full Name                           | Description                                                                      |
| :----------- | :---------------------------------- | :------------------------------------------------------------------------------- |
| **PEP**      | Python Enhancement Proposal         | Standard documents for the Python ecosystem (e.g., PEP 723 for script metadata). |
| **PyPI**     | Python Package Index                | The official third-party software repository for Python.                         |
| **Venv**     | Virtual Environment                 | An isolated environment for Python projects to manage dependencies.              |
| **CI/CD**    | Continuous Integration / Deployment | Automating the testing and deployment of code (e.g., GitHub Actions).            |
| **Lockfile** | -                                   | A file (`uv.lock`) specifying exact dependency versions for reproducible builds. |

---
