# Discrete Math — Course Roadmap

Structured after **MIT 6.042J — Mathematics for Computer Science** (Fall 2010, Leighton / van Dijk). Free textbook and lecture videos on MIT OCW. Four units split into ten phases; each phase is one or two notes.

The course teaches the mathematical maturity that every later CS course assumes — proofs, induction, number theory, sets and relations, graphs, counting, and discrete probability. Notes flag CS applications inline where 6.042J does (RSA from modular arithmetic, hashing from probability, invariants from state machines, coloring from register allocation).

## Phases

### Phase 1 — Proofs and propositional logic

_6.042J Unit 1, Ch. 1–3.5_

Propositions, truth tables, equivalences, predicates, quantifiers. Direct proof, contrapositive, contradiction, cases, well-ordering principle.

- [[Logic & Proofs]]

### Phase 2 — Induction

_6.042J Unit 1, Ch. 5_

Ordinary induction, strong induction, structural induction. Invariants and termination as proof tools. Connection to recursion and recurrences.

- [[Induction]]

### Phase 3 — Number theory

_6.042J Unit 2, Ch. 8_

Divisibility, gcd and Euclid's algorithm, Bezout's identity, modular arithmetic, Fermat's little theorem, Euler's theorem, Chinese remainder, RSA. The CS payoff: cryptography, hashing, error-detecting codes.

- [[Number Theory]]

### Phase 4 — Sets, relations, functions

_6.042J Unit 2, Ch. 4 + 9_

Set algebra, Russell's paradox, relations and equivalence classes, partial vs total orders, function injectivity / surjectivity / bijection, cardinality, Cantor's theorem.

- [[Sets]]
- [[Relations]]
- [[Functions]]

### Phase 5 — State machines and invariants

_6.042J Unit 2, Ch. 6–7_

State machines as proof tool, preserved invariants, derived variables, partial correctness, termination. Foundation for later concurrency and OS reasoning.

- [[State Machines]]

### Phase 6 — Graphs and trees

_6.042J Unit 2, Ch. 11–12_

Math view only — definitions, theorems, proofs. Walks, paths, cycles, connectivity, handshake lemma, Euler tours, Hamiltonian sketch, bipartite matching, planarity, coloring, chromatic number. Free trees, spanning trees, characterizations, Cayley's formula.

Storage and traversal algorithms are owned by [[../../data_structures/Graphs|Graphs (data structures)]] and [[../../algorithms/Graph Basics|Graph Basics]] respectively — this phase is purely mathematical.

- [[Graphs]]
- [[Trees]]

### Phase 7 — Counting

_6.042J Unit 3, Ch. 13–14_

Sum, product, bijection, and division rules. Permutations, combinations, binomial theorem, multinomial coefficients, stars and bars, inclusion-exclusion, pigeonhole. Counting as proof technique.

- [[Counting]]

### Phase 8 — Discrete probability foundations

_6.042J Unit 4, Ch. 17_

Sample spaces, events, axioms, conditional probability, independence, Bayes' rule, the four-step method. Birthday paradox, Monty Hall.

- [[Probability]]

### Phase 9 — Random variables and expectation

_6.042J Unit 4, Ch. 18–19_

Discrete random variables, PMF, CDF, expectation, linearity of expectation, indicator variables, variance, common distributions (Bernoulli, binomial, geometric).

- [[Random Variables]]

### Phase 10 — Concentration and random walks

_6.042J Unit 4, Ch. 19–20_

Markov's inequality, Chebyshev's inequality, Chernoff bound sketch, weak law of large numbers. Random walks on graphs, gambler's ruin. Connection to randomized algorithms and Markov chains.

- [[Concentration & Random Walks]]

## Status

**Complete.** Final grade: **B** (university exam, 2026-04-29)

## Reference materials

- Textbook (free PDF): [Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-fall-2010/resources/mit6_042jf10_notes/) — Lehman, Leighton, Meyer
- Lecture videos: [MIT 6.042J Mathematics for Computer Science, Fall 2010 - Playlist](https://www.youtube.com/playlist?list=PLB7540DEDD482705B)

- Lookup textbook (broader, encyclopedic): Rosen, _Discrete Mathematics and Its Applications_, 8e

## See also

- [[Index]]
- [[../linear_algebra/Index|Linear Algebra]]
- [[../../algorithms/ROADMAP|Algorithms — Course Roadmap]]
