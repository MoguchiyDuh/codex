---
tags:
  - computing/digital-logic
  - k-maps
related:
  - "[[Boolean Algebra]]"
  - "[[00 - Computing MOC]]"
---

## Purpose
Simplifies Boolean algebra expressions visually to create optimal logic circuits.

## Basic Rules

### Grouping
- Rectangles only (2^n cells: 1,2,4,8)
- Maximize group size
- Minimize number of groups
- Groups can wrap around edges (top-bottom, left-right)
- Overlapping groups are allowed

### Reading Groups
- Identify variables that **don't change** within the group
- Eliminate variables that **change** within the group
- Within **one** group: variables are **multiplied** (AND) → ABCD
- Between **different** groups: terms are **added** (OR) → AB + CD

---
## 4-Variable K-Map

<img src="Pictures/kmap.png" width=500 height="auto" style="display: block; margin: auto">

**Solution:**
We have 3 groups:
- orange group: $A \land D$
- green group: $C \land D$
- Purple group: $\lnot B \land \lnot D$

**Result:** $(A \land D) \lor (C \land D) \lor (\lnot B \land \lnot D)$

---
## Limitations
Beyond 6 variables becomes **impractical**. Use Quine-McCluskey algorithm instead.

---

## See Also
- [[Boolean Algebra]] - Boolean operations and laws
- [[00 - Computing MOC]] - Computing topics overview