# Regex Cheat Sheet

## 1. The Core (Metacharacters)

```text
.           # Any single character
\           # Escapes a special character
|           # Alternation (OR)
?           # 0 or 1 occurrence
*           # 0 or more occurrences
+           # 1 or more occurrences
```

---

## 2. Character Classes

```text
[abc]       # Any character in the set (a, b, or c)
[^abc]      # Any character NOT in the set
[a-z]       # Any character in the range (a to z)
\d          # Any digit (short for [0-9])
\D          # Any NON-digit
\w          # Any word character (Alphanumeric + _)
\W          # Any NON-word character
\s          # Any whitespace (Space, Tab, Newline)
\S          # Any NON-whitespace
```

---

## 3. Quantifiers

```text
{n}         # Exactly n occurrences
{n,}        # n or more occurrences
{n,m}       # Between n and m occurrences

*           # Greedy (matches as much as possible)
*?          # Lazy (matches as little as possible)
+?          # Lazy +
```

---

## 4. Anchors & Boundaries

```text
^           # Start of line/string
$           # End of line/string
\b          # Word boundary
\B          # NON-word boundary
```

---

## 5. Groups & Capture

```text
(...)       # Capture group (can refer to as \1, \2, etc.)
(?:...)     # NON-capturing group
```

---

## 6. MVP Common Patterns

```text
# Trailing Whitespace
\s\+$

# Email (Simplified)
[\w\.-]+@[\w\.-]+\.\w+

# IP Address (IPv4)
\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}

# URL (Basic)
https\?://[\w\.-]+(/[\w\._/-]*)?

# ISO Date (YYYY-MM-DD)
\d{4}-\d{2}-\d{2}
```
