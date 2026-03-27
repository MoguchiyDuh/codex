## 7. If the variable 𝑥 in predicate 𝑃(𝑥) takes values from the set {0, 1, 2, 3, 4} express the following predicate propositions using disjunction, conjunction, and negation. 

x ∈ {0, 1, 2, 3, 4}
- a. ∀x¬P(x) = ¬P(0) ∧ ¬P(1) ∧ ¬P(2) ∧ ¬P(3) ∧ ¬P(4)
- b. ¬∃xP(x) = ¬(P(0) ∨ P(1) ∨ P(2) ∨ P(3) ∨ P(4)) = ¬P(0) ∧ ¬P(1) ∧ ¬P(2) ∧ ¬P(3) ∧ ¬P(4)

---

## 8. Let 𝑃(𝑛) be the predicate “𝑛 is not an odd number” and 𝑄(𝑛) be the predicate “𝑛 squared is an odd number”. In the language of predicate logic express the statement “If 𝑛 is not an odd number, then 𝑛 squared is not an odd number”.

P(n): n is not an odd number
Q(n): n squared is an odd number

Statement: "If n is not an odd number, then n squared is not an odd number"

Answer: **∀n(P(n) ⇒ ¬Q(n))**

---

## 11. Given the following predicates:

- C(x, y): y is a child of person x
- W(x): x works in a store

Statement: "There is at least one person whose children work in a store"

Answer: **(b) ∃x∀y(C(x, y) ⇒ W(y))**

---

## 12. Given the following predicates:

- C(x): x is a car
- E(x): x has an electric engine
- F(x, y): x is faster than y

Statement: "Every electric car is faster than at least one non-electric car"

Answer: **(d) ∀x∃y(C(x) ∧ E(x) ⇒ C(y) ∧ ¬E(y) ∧ F(x, y))**

---

## 16. Determine truth values of the following predicate propositions, where domain of all variables is the set of integers 𝑍.

Domain: Z (integers)

- a. P(2), where P(x): x ≤ 10
-> 2 ≤ 10 -> **TRUE**
- b. P(4), where P(x): (x = 1) ∨ (x > 5)
-> (4 = 1) ∨ (4 > 5) = F ∨ F -> **FALSE**
- c. ∃x(x = 5) ∧ (x = 6)
-> **FALSE**
- d. ∃x(x = 5) ∧ (x ≤ 5)
->  if x = 5 -> (x = 5) ∧ (x ≤ 5) -> T ∧ T **TRUE**

---

## 19. For which of the following domains of variables 𝑥 and 𝑦 is the predicate proposition ∀𝑥∃𝑦(𝑥2 > 𝑦) true?

- a. x, y ∈ 𝑁
**FALSE** - For x = 0: x² = 0, need y ∈ N with 0 > y -> False
- b. x, y ∈ 𝑍
**TRUE** - Z has no lower bound. For any x, pick y = x² − 1 ∈ Z, then x² > y.
- c. x, y ∈ 𝑅
**TRUE** - same reasoning as Z, R also has no lower bound.
- d. x, y ∈ (0, +∞)
**TRUE** - for any x∈(0,+∞), x² > 0. Pick y = x² / 2 ∈ (0, +∞), then x² > y.

Answer: **b, c, d**

---

## 20. For the following predicate propositions determine their equivalent propositions without negation of quantifiers.

- a. ¬∃xP(x) = **∀x¬P(x)**
- b. ¬∀xP(x) = **∃x¬P(x)**
- c. ¬∃x∀yP(x,y) = **∀x∃y¬P(x,y)**
- d. ¬∃x¬∃yP(x,y) = **∀x∃yP(x,y)**
- e. ∀x¬∃yP(x,y) = **∀x∀y¬P(x,y)**
- f. ¬∀x¬∃yP(x,y) = **∃x∃yP(x,y)**
- g. ¬∃x∃yP(x,y) = **∀x∀y¬P(x,y)**
- h. ¬∀x∃yP(x,y) = **∃x∀y¬P(x,y)**

---

## SETS 1. Specify the following sets as lists of their elements.

- a. {x ∈ Z : x² = 6}
eNo integer squared equals 6 -> **∅**
- b. {x ∈ Z : x² = 9}
x = 3 or x = -3 -> **{-3, 3}**
- c. {x ∈ Z : x = x²}
x² - x = 0 -> x(x-1) = 0 -> x = 0 or x = 1. **{0, 1}**
- d. {𝑥 ∈ 𝑁 ∶ (𝑥 mod 2 = 1) ∧ (𝑥 < 10)}
**{1, 3, 5, 7, 9}**
- e. {𝑥 ∈ 𝑁 ∶ (𝑥 = 6) ∨ (𝑥 ≥ 4)}
just x ≥ 4, x = 6 is already covered. **{4, 5, 6, 7, 8, ...}**