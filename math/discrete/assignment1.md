## 1.  Which of the following statements are propositions?
- a. it is snowing now -> YES
- b. what is the time? -> NO, question
- c. today is friday -> YES
- d. learn well discrete math -> NO
- e. son, get married -> NO
- f. only odd prime is 2 -> YES (false statement, but proposition)
- g. Novak Djokovic is the GOAT -> YES
- h. do this exercise correctly -> NO

---

## 2.  Determine truth values of the following propositions.

- a. If 2 is even number (T), then 5 = 6 (F)
- b. If 2 is odd number (F), then 5 = 6 (F)
- c. If 4 is even number (T), then 10 = 7 + 3 (T)
- d. If 4 is odd number (F), then 10 = 7 + 3 (T)

---

## 3. Suppose that if it rains, I carry on an umbrella. Can you conclude that (and explain why) it was raining if

a) I was carrying an umbrella?
NO. could be carrying it for other reasons

b) I was not carrying an umbrella?
YES. (R ⇒  U) ∧ ¬U ⇒  ¬R. so If carrying an umbrella is guaranteed when it rains, then *not* carrying one is a guarantee that it wasn't raining — because if it had been raining, you *would* have had it.

---

## 4. What is the contraposition of the implication ¬𝑞 ⇒ ¬𝑝?

contrapositive of (A ⇒ B) is (¬A ⇒ ¬B)
So for ¬q ⇒ ¬p, flip and negate both sides: ¬(¬p) ⇒ ¬(¬q) → p ⇒ q

---

## 5. Construct truth tables for the following propositions and determine those which are tautologies.
- i. (p ∧ q) ∨ (¬p ∧ ¬q)

| p | q | p ∧ q | ¬p | ¬q | ¬p ∧ ¬q | (p ∧ q) ∨ (¬p ∧ ¬q) |
|---|---|-------|----|----|---------|---------------------|
| T | T | T | F | F | F | T |
| T | F | F | F | T | F | F |
| F | T | F | T | F | F | F |
| F | F | F | T | T | T | T |

Not a tautology

- j. (p ∧ ¬q) ⇒ (r ∨ q)

| p | q | r | ¬q | p ∧ ¬q | r ∨ q | (p ∧ ¬q) ⇒ (r ∨ q) |
|---|---|---|----|--------|-------|---------------------|
| T | T | T | F | F | T | T |
| T | T | F | F | F | T | T |
| T | F | T | T | T | T | T |
| T | F | F | T | T | F | F |
| F | T | T | F | F | T | T |
| F | T | F | F | F | T | T |
| F | F | T | T | F | T | T |
| F | F | F | T | F | F | T |

Not a tautology

- k. (¬p ∧ (p ∨ q)) ⇒ q

| p | q | ¬p | p ∨ q | ¬p ∧ (p ∨ q) | (¬p ∧ (p ∨ q)) ⇒ q |
|---|---|----|-------|--------------|---------------------|
| T | T | F | T | F | T |
| T | F | F | T | F | T |
| F | T | T | T | T | T |
| F | F | T | F | F | T |

Tautology

- l. (p ⇒ q) ↔ (¬p ∨ q)

| p | q | p ⇒ q | ¬p | ¬p ∨ q | (p ⇒ q) ↔ (¬p ∨ q) |
|---|---|-------|----|----|---------------------|
| T | T | T | F | T | T |
| T | F | F | F | F | T |
| F | T | T | T | T | T |
| F | F | T | T | T | T |

Tautology

- m. ((p ∧ ¬(q ∧ ¬r)) ∨ (p ∧ q)) ↔ r
= (p ∧ (¬q ∨ r)) ∨ (p ∧ q) ↔ r
= p ∧ ((¬q ∨ r) ∨ q) ↔ r
= p ∧ (¬q ∨ q ∨ r) ↔ r
= p ∧ (T ∨ r) ↔ r
= p ∧ T ↔ r
= p ↔ r

| p | q | r | p ↔ r |
|---|---|---|-------|
| T | T | T | T |
| T | T | F | F |
| T | F | T | T |
| T | F | F | F |
| F | T | T | F |
| F | T | F | T |
| F | F | T | F |
| F | F | F | T |

Not a tautology

- n. ((p ∨ q) ∧ (¬p ∨ r)) ⇒ (q ∨ r)

| p | q | r | p ∨ q | ¬p | ¬p ∨ r | (p ∨ q) ∧ (¬p ∨ r) | q ∨ r | result |
|---|---|---|-------|----|--------|---------------------|-------|--------|
| T | T | T | T | F | T | T | T | T |
| T | T | F | T | F | F | F | T | T |
| T | F | T | T | F | T | T | T | T |
| T | F | F | T | F | F | F | F | T |
| F | T | T | T | T | T | T | T | T |
| F | T | F | T | T | T | T | T | T |
| F | F | T | F | T | T | F | T | T |
| F | F | F | F | T | T | F | F | T |

Tautology
