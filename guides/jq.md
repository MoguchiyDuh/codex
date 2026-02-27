# jq Cheat Sheet (JSON Processor)

`jq` is a lightweight and flexible command-line JSON processor.

## 1. Installation

```bash
# Ubuntu/Debian
sudo apt install jq

# Arch Linux
sudo pacman -S jq

# Fedora (dnf)
sudo dnf install jq

# Windows (via Chocolatey)
choco install jq

# macOS
brew install jq
```

---

## 2. Basic Filters

```bash
jq '.' file.json            # Pretty-print
jq '.foo'                   # Get value of key "foo"
jq '.foo.bar'               # Nested keys
jq '.[0]'                   # First element of array
jq '.[]'                    # Iterate over all elements in array
```

---

## 3. Transformations

### Object Construction

```bash
# Extract subset into new object
jq '{name: .user.name, id: .user.id}'

# Map over an array
jq '.users | map({username: .login})'
```

### Filtering (Select)

```bash
# Filter objects by criteria
jq '.[] | select(.age > 25)'

# Check for existence / null
jq '.[] | select(.email != null)'
```

---

## 4. Functions & Operators

| Operator       | Description                                      |
| :------------- | :----------------------------------------------- |
| **Length**     | `jq '. \| length'` (Array size or string length) |
| **Keys**       | `jq 'keys'` (Get all keys of an object)          |
| **Join/Split** | `jq '. \| join(",")'` / `jq 'split(",")'`        |
| **Math**       | `jq '.price * 1.2'`                              |
| **Composing**  | `jq '.foo \| .bar \| .baz'` (Piping filters)     |

---

## 5. Output Options (CLI Flags)

```bash
jq -r            # Raw output (removes quotes from strings)
jq -c            # Compact output (one line per object)
jq -s            # Slurp (read entire input into one big array)
jq -n            # Null input (use when generator is in filter)
```

**Pro Tip:** Use `jq -R` to process non-JSON raw strings line by line.

---

## 6. Examples

```bash
# Get all container IDs from Docker
docker inspect $(docker ps -q) | jq -r '.[].Id'

# Check if a package has a specific version in package.json
cat package.json | jq '.dependencies | has("react")'

# Filter JSON logs by level
tail -f app.log | jq 'select(.level == "ERROR")'
```
