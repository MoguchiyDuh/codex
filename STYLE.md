# Codex Style Guide

## Note types

Two kinds of notes, different rules:

| Type              | Location                                              | Frontmatter | Section dividers       |
| ----------------- | ----------------------------------------------------- | ----------- | ---------------------- |
| **Theory / lang** | `theory/`, `c/notes/`, `rust/notes/`, `python/notes/` | Required    | None                   |
| **Guide**         | `guides/`                                             | None        | `---` between sections |

## Frontmatter (theory / lang notes)

```yaml
---
tags: [algorithms, sorting]
status: stub | complete
source: c/hashmap.c # lang notes only — optional
---
```

**Tags:** start with the note's primary domain or area (`algorithms`, `data-structures`, `math`, `c`, `rust`, `python`), then add narrower topic tags. Flat, no namespacing.

**Status:** `stub` until fully written, then `complete`. A note is `complete` only when it satisfies the **content depth** rules below.

## Structure

```
# Title              one per file, matches filename exactly
> Summary            one-line blockquote immediately after title

## Section           major topic
### Subsection       deeper detail

## Video references  optional, before See also
## See also          always last, wikilinks only
```

No `Introduction` or `Overview` as a heading — first `##` is the first real topic.

## Content depth (theory notes, `status: complete`)

A theory note must teach the topic, not just outline it. Baseline references: `theory/math/linear_algebra/` and `theory/data_structures/`.

- **Prose, not bullet stubs.** Every `##` and `###` has explanatory text.
- **Worked examples** alongside formulas wherever a beginner would otherwise stall.
- **Tables for comparisons, properties, classifications, complexity.** Prefer a table over a bullet list whenever a structural comparison is being made.
- **Images at conceptually heavy spots** — see _Images_ below.
- **Cross-references inline** in prose where another note develops the idea further (e.g. _"developed in [[Vector Spaces]]"_).
- **Course-grounded scope.** Folder `Index.md` names the academic course the material is structured after (e.g. _"Structured after MIT 18.06 (Strang)"_, _"Structured after CLRS 4e and MIT 6.046"_).

## Math (LaTeX)

Obsidian renders KaTeX. Use it for any non-trivial expression.

- Inline: `$A\mathbf{x} = \mathbf{b}$`
- Display: `$$\|\mathbf{v}\| = \sqrt{v_1^2 + \cdots + v_n^2}$$`
- Vectors bold lowercase: `\mathbf{v}`. Matrices uppercase non-bold: `A`.
- Sets: `\mathbb{R}`, `\mathbb{Z}`, `\mathbb{N}`.
- Big-O in algorithm notes: `$O(n \log n)$`, `$\Theta(n)$`, `$\Omega(n^2)$`.

Plain text big-O like `O(n)` is acceptable inside table cells where LaTeX would clutter; be consistent within a note.

## Code blocks

- Always specify a language: ` ```python `, ` ```rust `, ` ```c `, ` ```pseudo `, ` ```text `.
- Never bare ` ``` `.
- Pseudocode for algorithm notes uses ` ```pseudo ` or ` ```text ` and follows CLRS-style conventions (1-indexed arrays acceptable when matching textbook).
- Inline backticks for: function names, keywords, values, file paths, commands, variable names.

## Algorithm notes — code references

Theory notes about a specific algorithm cite the runnable companion file with a single bold-prefixed line directly under the pseudocode block:

```md
**Code:** `theory/algorithms/showcase/dijkstra.py`
```

Convention:

- Each algorithm has one `.py` file in `theory/algorithms/showcase/` containing both the implementation and a matplotlib visualization gated by `if __name__ == "__main__":`.
- The visualization writes its image into `resources/pictures/` under the same base name (e.g. `dijkstra_step.png`) so the note's `![[...]]` embed resolves automatically.
- Filename is the algorithm's snake_case name: `merge_sort.py`, `quick_sort.py`, `bellman_ford.py`.

## Images

Theory notes embed images at points where a diagram materially aids understanding — not decoratively.

### Where to place

- After a definition that is hard to picture from words alone.
- To illustrate a transformation, traversal, rotation, or process.
- Side-by-side comparisons (e.g. adjacency list vs matrix, before/after rotation).

### Where _not_ to place

- Restating a table.
- Decorating a section header.
- Where the formula already conveys the idea (e.g. simple algebraic identities).

### Convention

- Files live flat in `resources/pictures/`.
- Filenames: lowercase, snake_case, descriptive (`avl_rotations.png`, `adjacency_list_vs_matrix.png`).
- Embed with Obsidian wiki-embed: `![[filename.png]]`.
- One image per heavy concept; do not stack multiple images without intervening prose.
- For matplotlib-generated diagrams (axes, plots, function graphs), use `.png` at sensible DPI; for hand-drawn or schematic diagrams, `.png` or `.svg` both fine.

### Matplotlib scripts

Scripts that generate pictures live in `resources/mpl/` and are run with `uv run`.

**File structure**

- One script per output image, filename matches the output: `pascals_triangle.py` → `pascals_triangle.png`.
- Project dependencies and Python version are defined in the root `pyproject.toml`.
- `OUTPUT` path is always `Path(__file__).resolve().parent.parent / "pictures" / "<name>.png"`.
- Config is loaded from `resources/mpl/config.json` at module level; never hardcode values that live there.

All style values (DPI, font sizes, colors, linewidth, font family) are defined in `resources/mpl/config.json` — refer there for current values.

**Script conventions**

- Load config at module level: `_CFG = json.loads((_HERE / "config.json").read_text())`.
- Alias config values to named constants immediately after (`LW`, `BLACK`, `_FS`, etc.).
- Layout constants (geometry, spacing, radii) are module-level named constants — never magic numbers inside drawing functions.
- Position-tweak constants that are likely to need adjustment are named explicitly (e.g. `LABEL_00_DY`, `LABEL_B_Y`) and kept at the top of their function, not buried inline.
- `rcParams` is set once in `main()` from config; never set it in drawing functions.
- Layout engine: `layout="constrained"` on `plt.subplots()`. Never call `tight_layout()`.
- Always `plt.close(fig)` immediately after `savefig`.
- Never call `plt.show()` — scripts are headless generators.
- `fig.savefig(OUTPUT, dpi=..., bbox_inches=...)` — both params always explicit.
- `strict=True` on `zip` wherever panel count must match a list.

**Color semantics**

Use config colors with consistent meaning across all scripts:

| Color    | Role                                                              |
| -------- | ----------------------------------------------------------------- |
| `black`  | curves, axes, structural lines, default labels                    |
| `gray`   | reference grid, guide lines, auxiliary projections, captions      |
| `red`    | primary highlight — the object being studied, errors, key element |
| `blue`   | secondary object — complement, second vector, second curve        |
| `purple` | result or combination — e.g. sum vector, invariant line           |
| `green`  | transformed space grid, third distinct object                     |
| `orange` | fourth distinct object in graph/diagram contexts                  |

Never use raw color strings (`"red"`, `"black"`) — always alias from `_COL`.

**Alpha policy**

`alpha=1` (no transparency) is the default. Exceptions allowed only when alpha carries semantic meaning:

- **Ghost / "old space"**: same color as the original at reduced alpha (e.g. `alpha=0.25`) to show "this was the space before transformation" — the color match is what communicates sameness, the alpha communicates fading.
- **Venn / SCC overlaps**: alpha on filled regions so overlapping areas blend visually, communicating intersection.
- **3D surfaces**: semi-transparent fill on planes/surfaces so the geometry behind remains visible.
- **Displaced copy**: a vector or shape shown at its new position as a ghost of its old self (e.g. translated vector in a tip-to-tail diagram) — `alpha=0.5`.

Never use alpha just to make a color lighter or less visually dominant — use `gray` or a lighter config color instead.

**Line styles**

| Style        | Use                                                                                            |
| ------------ | ---------------------------------------------------------------------------------------------- |
| `solid`      | main curves, vectors, axes, primary objects                                                    |
| `--` dashed  | reference lines with a fixed value: asymptotes, interval boundaries, directrix, secant lines   |
| `:` dotted   | auxiliary projections and drop-lines (showing where a point lands on an axis); background grid |
| `-.` dashdot | axis of symmetry, invariant lines that are neither the main curve nor a reference value        |

**Grid drawing**

Integer-tick grids skip `t=0` — the x and y axes are drawn separately as `ax.plot` lines so they can have distinct styling (color, linewidth) from the grid. The grid loop uses `range(-n, n+1)` with `if t != 0`.

**Math rendering**

Matplotlib scripts use built-in mathtext (`$...$`) as the standard path. Do not depend on a local TeX installation for diagram generation.

- Keep all math strings valid mathtext.
- Prefer expressions supported directly by matplotlib's parser: `\frac`, `\sqrt`, `\binom`, `\mathbf`, Greek letters, subscripts/superscripts, and standard relations/operators.
- Do not use `text.usetex` as the default rendering path.
- Do not require `latex`, `dvipng`, or TeX font packages to generate images.
- `rcParams` should keep using the config-driven font settings from `resources/mpl/config.json`.

Unsupported or fragile LaTeX-only constructs should be rewritten into mathtext-safe forms:

- `\begin{bmatrix} ... \end{bmatrix}` → use plain-text fallback labels such as `[[a, b], [c, d]]` when needed.
- `\pmod{n}` → use `(\mathrm{mod}\ n)` instead.
- Package-dependent symbols/macros (for example `\bigstar` from `amssymb`) should be avoided in labels.

## Tables

Tables are the default format for:

- Property lists (commutative, associative, ...).
- Operation cost summaries (per-op complexity).
- Variant comparisons (singly vs doubly linked, AVL vs red-black).
- Classifications (graph types, matrix types).

A two-column key/value table beats a bullet list of "X — definition" pairs.

## Video references

Optional section, immediately before `## See also`, when canonical video lectures exist for the topic (3Blue1Brown for linear algebra, MIT OCW lectures, etc).

```md
## Video references

- ![3Blue1Brown - Vectors | Chapter 1, Essence of linear algebra](https://www.youtube.com/watch?v=fNk_zzaMoSs)
```

The leading `!` makes Obsidian render the video preview inline. Use for high-quality, free, durable sources only — not random YouTube tutorials.

## Exercises section

Lang notes may include an `## Exercises` section before `## See also` — coding tasks tied to the note's topic, each with a reference to the relevant `src/` file.

```md
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
- [[Index]]
```

- Cross-section links use relative paths: `[[../../rust/notes/Lifetimes]]`.
- Display labels with pipe: `[[../algorithms/Index|Algorithms]]`.
- Ending with a self-link to `[[Index]]` is encouraged in densely cross-linked folders.

## File naming

- Theory / lang notes: Title Case with spaces — `Stack vs Heap.md`, `Binary Search Tree.md`.
- Guides: lowercase, no spaces — `git.md`.
- Image assets: lowercase snake_case — `avl_rotations.png`.

## Index files

Every subfolder has an `Index.md` acting as a MOC (Map of Content).

- Names the academic course the folder is structured after (one line below the title).
- Lists every note in the folder with a one-line description.
- For folders with > 6 notes, group topics under `##` sub-headings (e.g. `## Foundations`, `## Hierarchical and priority`, `## Hashing`, `## Graphs`).
- Ends with `## See also` linking sibling folders' indexes.
- No prose beyond the one-line course-attribution and per-note descriptions.

## Formatting rules (everything else)

- No horizontal rules (`---`) in theory/lang notes — section breaks are heading-driven.
- En-dashes (`–`) for ranges, em-dashes (`—`) for asides.
- Inline backticks for: function names, keywords, values, file paths, commands.
- Sentence case for headings (`## Hash function`, not `## Hash Function`), except acronyms (`## SVD`, `## ALU`).
- One blank line between every block element. No double blank lines.
