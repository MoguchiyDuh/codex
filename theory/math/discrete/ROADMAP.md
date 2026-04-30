# Discrete Math — Course Roadmap

Structured after **MIT 6.042J — Mathematics for Computer Science** (Spring 2015, Lehman / Leighton / Meyer). Free textbook and lecture videos on MIT OCW. Four units split into ten phases; each phase is one or two notes.

The course teaches the mathematical maturity that every later CS course assumes — proofs, induction, number theory, sets and relations, graphs, counting, and discrete probability. Notes flag CS applications inline where 6.042J does (RSA from modular arithmetic, hashing from probability, invariants from state machines, coloring from register allocation).

## Phases

### Phase 1 — Proofs and propositional logic

*6.042J Unit 1, Ch. 1–3.5*

Propositions, truth tables, equivalences, predicates, quantifiers. Direct proof, contrapositive, contradiction, cases, well-ordering principle.

- [[Logic & Proofs]]

### Phase 2 — Induction

*6.042J Unit 1, Ch. 5*

Ordinary induction, strong induction, structural induction. Invariants and termination as proof tools. Connection to recursion and recurrences.

- [[Induction]]

### Phase 3 — Number theory

*6.042J Unit 2, Ch. 8*

Divisibility, gcd and Euclid's algorithm, Bezout's identity, modular arithmetic, Fermat's little theorem, Euler's theorem, Chinese remainder, RSA. The CS payoff: cryptography, hashing, error-detecting codes.

- [[Number Theory]]

### Phase 4 — Sets, relations, functions

*6.042J Unit 2, Ch. 4 + 9*

Set algebra, Russell's paradox, relations and equivalence classes, partial vs total orders, function injectivity / surjectivity / bijection, cardinality, Cantor's theorem.

- [[Sets]]
- [[Relations]]
- [[Functions]]

### Phase 5 — State machines and invariants

*6.042J Unit 2, Ch. 6–7*

State machines as proof tool, preserved invariants, derived variables, partial correctness, termination. Foundation for later concurrency and OS reasoning.

- [[State Machines]]

### Phase 6 — Graphs and trees

*6.042J Unit 2, Ch. 11–12*

Math view only — definitions, theorems, proofs. Walks, paths, cycles, connectivity, handshake lemma, Euler tours, Hamiltonian sketch, bipartite matching, planarity, coloring, chromatic number. Free trees, spanning trees, characterizations, Cayley's formula.

Storage and traversal algorithms are owned by [[../../data_structures/Graphs|Graphs (data structures)]] and [[../../algorithms/Graph Basics|Graph Basics]] respectively — this phase is purely mathematical.

- [[Graphs]]
- [[Trees]]

### Phase 7 — Counting

*6.042J Unit 3, Ch. 13–14*

Sum, product, bijection, and division rules. Permutations, combinations, binomial theorem, multinomial coefficients, stars and bars, inclusion-exclusion, pigeonhole. Counting as proof technique.

- [[Counting]]

### Phase 8 — Discrete probability foundations

*6.042J Unit 4, Ch. 17*

Sample spaces, events, axioms, conditional probability, independence, Bayes' rule, the four-step method. Birthday paradox, Monty Hall.

- [[Probability]]

### Phase 9 — Random variables and expectation

*6.042J Unit 4, Ch. 18–19*

Discrete random variables, PMF, CDF, expectation, linearity of expectation, indicator variables, variance, common distributions (Bernoulli, binomial, geometric).

- [[Random Variables]]

### Phase 10 — Concentration and random walks

*6.042J Unit 4, Ch. 19–20*

Markov's inequality, Chebyshev's inequality, Chernoff bound sketch, weak law of large numbers. Random walks on graphs, gambler's ruin. Connection to randomized algorithms and Markov chains.

- [[Concentration & Random Walks]]

## Status

**Complete.** Final grade: **B** (university exam, 2026-04-29)

## Reference materials

- Textbook (free PDF): [Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/resources/mit6_042js15_textbook/) — Lehman, Leighton, Meyer
- Lecture videos: [MIT OCW 6.042J Spring 2015](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/)
- Lookup textbook (broader, encyclopedic): Rosen, *Discrete Mathematics and Its Applications*, 8e

## See also

- [[Index]]
- [[../linear_algebra/Index|Linear Algebra]]
- [[../../algorithms/ROADMAP|Algorithms — Course Roadmap]]
