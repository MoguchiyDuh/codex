# Codex Style Guide

## Note types

Two kinds of notes, different rules:

| Type | Location | Frontmatter | Section dividers |
|---|---|---|---|
| **Theory / lang** | `theory/`, `c/notes/`, `rust/notes/`, `python/notes/` | Required | None |
| **Guide** | `guides/` | None | `---` between sections |

## Frontmatter (theory / lang notes)

```yaml
---
tags: [theory, algorithms, sorting]
status: stub | complete
source: c/hashmap.c          # lang notes only — optional
---
```

**Tags:** first tag is always the domain (`theory`, `c`, `rust`, `python`), second is the subdomain (`algorithms`, `data-structures`, `oop`, `os`, `concurrency`, `networking`, `databases`, `computing`), rest are topic-specific. Flat, no namespacing.

**Status:** `stub` until fully written, then `complete`.

## Structure

```
# Title          one per file, matches filename exactly
> Summary        one-line blockquote immediately after title

## Section       major topic
### Subsection   deeper detail

## See also      always last, wikilinks only
```

No `Introduction` or `Overview` as a heading — first `##` is the first real topic.

## Formatting

- Inline backticks for: function names, keywords, values, file paths, commands
- Code blocks always have a language specifier — never bare ` ``` `
- Tables preferred over bullet lists for comparisons
- No horizontal rules (`---`) in theory/lang notes

## Exercises section

Lang notes may include an `## Exercises` section before `## See also` — coding tasks tied to the note's topic, each with a reference to the relevant `src/` file.

```
## Exercises

1. **Task name** — description. `src/file.c`
```

Theory notes do not have exercises — those belong in the course roadmap.

## Cross-references

`## See also` at the bottom of every theory/lang note that has related content. Wikilinks only:

```md
## See also

- [[Stack vs Heap]]
- [[Virtual Memory]]
```

Cross-section links use relative paths: `[[../../rust/notes/Lifetimes]]`

## File naming

- Theory / lang notes: Title Case with spaces — `Stack vs Heap.md`
- Guides: lowercase, no spaces — `git.md`

## Index files

Every subfolder has an `Index.md` acting as a MOC (Map of Content). Links to all notes in the folder with a one-line description each. No prose, just the map.
