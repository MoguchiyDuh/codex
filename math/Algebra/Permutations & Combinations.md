# Permutations and Combinations

Permutations and combinations are fundamental counting principles used to determine the number of ways objects can be arranged or selected.

---

## Factorial Notation

The **factorial** of a non-negative integer $n$ is the product of all positive integers less than or equal to $n$:

$$\boxed{n! = n \times (n-1) \times (n-2) \times \cdots \times 3 \times 2 \times 1}$$

**Special cases:**
- $0! = 1$ (by definition)
- $1! = 1$

**Examples:**
- $5! = 5 \times 4 \times 3 \times 2 \times 1 = 120$
- $4! = 4 \times 3 \times 2 \times 1 = 24$
- $3! = 6$
- $2! = 2$

**Properties:**
- $n! = n \times (n-1)!$
- $\frac{n!}{(n-k)!} = n \times (n-1) \times \cdots \times (n-k+1)$

---

## Fundamental Counting Principle

If one event can occur in $m$ ways and another independent event can occur in $n$ ways, then:
- **Both events** can occur in $\boxed{m \times n}$ ways

**Example:** 
- 3 shirts, 4 pairs of pants
- Total outfits = $3 \times 4 = 12$

---

## Permutations

A **permutation** is an **ordered arrangement** of objects. **The order matters.**

### Formula: Permutations of n objects taken r at a time

$$\boxed{P(n, r) = \frac{n!}{(n-r)!} = n \times (n-1) \times (n-2) \times \cdots \times (n-r+1)}$$

**Alternative notations:** $_nP_r$, $P_r^n$, $P(n,r)$

**Where:**
- $n$ = total number of objects
- $r$ = number of objects selected
- $0 \leq r \leq n$

**Examples:**

1. **$P(5, 3)$:** Arrange 3 objects from 5
   $$P(5,3) = \frac{5!}{(5-3)!} = \frac{5!}{2!} = \frac{120}{2} = 60$$

2. **$P(7, 2)$:** Arrange 2 objects from 7
   $$P(7,2) = \frac{7!}{5!} = 7 \times 6 = 42$$

---

### Permutation of All n Objects

When selecting all $n$ objects ($r = n$):
$$\boxed{P(n, n) = n!}$$

**Example:** Arrange 4 books on a shelf
- $P(4, 4) = 4! = 24$ ways

---

### Permutations with Repetition

When some objects are **identical**, the formula is:

$$\boxed{P = \frac{n!}{n_1! \times n_2! \times \cdots \times n_k!}}$$

**Where:**
- $n$ = total number of objects
- $n_1, n_2, \ldots, n_k$ = number of each type of identical object

**Example:** Arrangements of the word "MISSISSIPPI"
- Total letters: $n = 11$
- I appears 4 times: $n_1 = 4$
- S appears 4 times: $n_2 = 4$
- P appears 2 times: $n_3 = 2$
- M appears 1 time: $n_4 = 1$

$$P = \frac{11!}{4! \times 4! \times 2! \times 1!} = \frac{39,916,800}{24 \times 24 \times 2 \times 1} = 34,650$$

---

### Real-World Example: Permutations

**Scenario:** You have 5 friends and want to arrange 3 of them in a line for a photo. How many arrangements?

$$P(5, 3) = \frac{5!}{2!} = \frac{120}{2} = 60 \text{ arrangements}$$

**Examples of arrangements:** ABC, ACB, BAC, BCA, CAB, CBA (where A, B, C are 3 of the 5 friends)

---

## Combinations

A **combination** is a **selection** of objects where **order does NOT matter**.

### Formula: Combinations of n objects taken r at a time

$$\boxed{C(n, r) = \binom{n}{r} = \frac{n!}{r!(n-r)!}}$$

**Alternative notations:** $_nC_r$, $C_r^n$, $C(n,r)$, $\binom{n}{r}$

**Where:**
- $n$ = total number of objects
- $r$ = number of objects selected
- $0 \leq r \leq n$

**Examples:**

1. **$C(5, 3)$:** Choose 3 objects from 5
   $$C(5,3) = \frac{5!}{3! \times 2!} = \frac{120}{6 \times 2} = 10$$

2. **$C(7, 2)$:** Choose 2 objects from 7
   $$C(7,2) = \frac{7!}{2! \times 5!} = \frac{7 \times 6}{2} = 21$$

---

### Real-World Example: Combinations

**Scenario:** You have 5 friends and want to form a team of 3. How many teams possible?

$$C(5, 3) = \frac{5!}{3! \times 2!} = 10 \text{ teams}$$

**Examples of teams:** {Alice, Bob, Charlie}, {Alice, Bob, Diana}, {Alice, Bob, Emma}, etc.

**Note:** {Alice, Bob, Charlie} is the **same team** as {Charlie, Bob, Alice} because order doesn't matter.

---

## Key Difference: Permutations vs Combinations

| Feature | Permutations | Combinations |
|---------|--------------|--------------|
| **Order** | Matters | Doesn't matter |
| **Formula** | $\frac{n!}{(n-r)!}$ | $\frac{n!}{r!(n-r)!}$ |
| **Example** | Arranging 3 friends in a line | Selecting 3 friends for a team |
| **Result** | ABC ≠ BAC | {A,B,C} = {C,B,A} |
| **Relation** | $P(n,r) = r! \times C(n,r)$ | $C(n,r) = \frac{P(n,r)}{r!}$ |

---

## Special Cases

### 1. Choosing All Objects

$$\boxed{C(n, n) = 1}$$

Only one way to select all $n$ objects.

---

### 2. Choosing None

$$\boxed{C(n, 0) = 1}$$

One way to select nothing (empty set).

---

### 3. Choosing One

$$\boxed{C(n, 1) = n}$$

$n$ ways to select one object from $n$.

---

### 4. Symmetry Property

$$\boxed{C(n, r) = C(n, n-r)}$$

**Example:** $C(10, 3) = C(10, 7) = 120$

**Reason:** Choosing 3 objects to include = choosing 7 objects to exclude

---

### 5. Pascal's Identity

$$\boxed{C(n, r) = C(n-1, r-1) + C(n-1, r)}$$

---

## Circular Permutations

When arranging $n$ objects in a **circle**, the number of distinct arrangements is:

$$\boxed{(n-1)!}$$

**Reason:** Fix one object's position to eliminate rotational duplicates.

**Example:** Seat 5 people around a circular table
- $(5-1)! = 4! = 24$ arrangements

**If reflections are also identical** (like a necklace that can be flipped):
$$\boxed{\frac{(n-1)!}{2}}$$

---

## Combinations with Repetition

When selecting $r$ objects from $n$ types **with replacement** (repetition allowed):

$$\boxed{C(n+r-1, r) = \frac{(n+r-1)!}{r!(n-1)!}}$$

**Example:** Choose 3 fruits from {apple, banana, cherry} with repetition
- $C(3+3-1, 3) = C(5, 3) = 10$
- Possible: {A,A,A}, {A,A,B}, {A,A,C}, {A,B,B}, {A,B,C}, {A,C,C}, {B,B,B}, {B,B,C}, {B,C,C}, {C,C,C}

---

## Applications

### 1. Probability

**Example:** What's the probability of drawing 2 aces from a standard 52-card deck?

- Total ways to choose 2 cards: $C(52, 2) = \frac{52 \times 51}{2} = 1326$
- Ways to choose 2 aces: $C(4, 2) = 6$
- Probability: $\frac{6}{1326} = \frac{1}{221} \approx 0.0045$

---

### 2. Committee Selection

**Example:** From 12 people, select a committee of 5. How many ways?

$$C(12, 5) = \frac{12!}{5! \times 7!} = 792$$

**Follow-up:** If the committee must have 3 women and 2 men from 7 women and 5 men:

$$C(7, 3) \times C(5, 2) = 35 \times 10 = 350$$

---

### 3. Password Combinations

**Example:** How many 4-digit PINs (0-9) are possible?

- With repetition: $10^4 = 10,000$
- Without repetition: $P(10, 4) = 10 \times 9 \times 8 \times 7 = 5,040$

---

### 4. Path Counting

**Example:** Grid paths from (0,0) to (3,2) moving only right (R) or up (U):

- Total moves: 3R + 2U = 5 moves
- Arrangements of "RRRUU": $\frac{5!}{3! \times 2!} = 10$ paths

---

## Complex Examples

### Example 1: Mixed Selection

From 5 men and 4 women, form a committee of 4 people with at least 2 women.

**Cases:**
- 2 women, 2 men: $C(4,2) \times C(5,2) = 6 \times 10 = 60$
- 3 women, 1 man: $C(4,3) \times C(5,1) = 4 \times 5 = 20$
- 4 women, 0 men: $C(4,4) \times C(5,0) = 1 \times 1 = 1$

**Total:** $60 + 20 + 1 = 81$

---

### Example 2: Restricted Arrangements

Arrange 7 books on a shelf where 2 specific books must be together.

- Treat 2 books as one unit: 6 units to arrange = $6! = 720$
- Within the unit, 2 books can be arranged: $2! = 2$
- Total: $720 \times 2 = 1440$

---

### Example 3: Complementary Counting

From 10 people, choose at least 2. How many ways?

**Method 1:** Direct
$$C(10,2) + C(10,3) + \cdots + C(10,10) = 2^{10} - C(10,0) - C(10,1) = 1024 - 1 - 10 = 1013$$

**Method 2:** Complement
- Total subsets: $2^{10} = 1024$
- Subtract (0 people + 1 person): $1024 - 1 - 10 = 1013$

---

## Important Formulas Summary

| Concept | Formula |
|---------|---------|
| Permutations (n, r) | $P(n,r) = \frac{n!}{(n-r)!}$ |
| Permutations (all n) | $n!$ |
| Permutations (with repetition) | $\frac{n!}{n_1! \times n_2! \times \cdots}$ |
| Combinations (n, r) | $C(n,r) = \frac{n!}{r!(n-r)!}$ |
| Circular permutations | $(n-1)!$ |
| Combinations (with repetition) | $C(n+r-1, r)$ |
| Relation | $P(n,r) = r! \times C(n,r)$ |

---

## Common Mistakes

1. **Confusing permutations and combinations** ✗
   - Ask: "Does order matter?" ✓

2. **Forgetting $0! = 1$** ✗
   - Correct: $0! = 1$ by definition ✓

3. **$C(n,r) = \frac{n!}{r!}$** ✗
   - Correct: $C(n,r) = \frac{n!}{r!(n-r)!}$ ✓

4. **Not considering restrictions** ✗
   - Account for "must include," "at least," etc. ✓

---

## See Also
- [[Binomials]] - Binomial coefficients are combinations
- [[00 - Algebra MOC]] - Algebra topics overview
