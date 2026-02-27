# Rust Learning Repo - Style Guide

## Code Structure

- Single `pub fn run()` entry point per module
- Organized by concept with dashed section dividers: `// ------------------- Section -------------------`
- Linear, executable examples

## Type Annotations

- **ALWAYS** explicit type annotations on variable declarations
- Example: `let arr: [i32; 5] = [1, 2, 3, 4, 5];`
- Show types even when obvious - pedagogical value

## Comments

- Section dividers only
- Inline comments for:
  - Non-obvious syntax quirks
  - Advanced concepts that need brief explanation (Cow, Pin, Send/Sync, etc.)
  - **Error scenarios**: PANIC/ERROR comments showing what would fail
    - `// PANIC: arr[99] would panic (index out of bounds)`
    - `// ERROR: Can't drop while reference exists`
    - Commented-out code showing compile errors
- Keep explanations 1-2 sentences max
- NO function docstrings
- NO fluff or explanatory prose
- Minimal and sparse

## Code Patterns

- Underscore prefix for unused variants: `let _arr1: [i32; 5] = ...;`
- **Explicit `return` statements** - no implicit returns
- Show multiple creation methods when applicable
- Demonstrate both immutable and mutable patterns
- Group related operations logically

## Coverage

- **Comprehensive** - cover ALL useful methods and features
- Include advanced operations, not just basics
- Show edge cases (out of bounds, empty, etc.)
- Practical conversions and interop

## Output

- Nearly every operation prints result
- Use `{:?}` for debug output
- Occasional type introspection via `get_type()`
- Clear, scannable output format

## Dependencies

- Use `shared` crate utilities: `print_h1!`, `print_h2!`, `print_h3!`, `get_type()`
- External crates when needed (tokio, rayon, etc.)

---

**Target audience:** Middle dev level - assumes basic understanding, shows real-world patterns
