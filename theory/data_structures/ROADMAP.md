# Data Structures — Course Roadmap

Structured after **MIT 6.006 — Introduction to Algorithms** (Fall 2011, Demaine / Devadas). That course teaches data structures and algorithms together; this roadmap covers the data structure half. Algorithm design paradigms and graph algorithms are owned by [[../algorithms/ROADMAP|Algorithms — Course Roadmap]].

CLRS 4e (Cormen, Leiserson, Rivest, Stein) is the reference textbook — chapters are cited per phase.

## Phases

### Phase 1 — Abstract types and linear structures

_6.006 Lecture 2; CLRS Ch. 10_

Interface vs implementation. Sequence and set ADTs. Arrays: static, dynamic, amortised $O(1)$ append. Linked lists: singly, doubly, circular, sentinel nodes. Stacks and queues: LIFO, FIFO, deque, ring buffer.

- [[Abstract Data Types]]
- [[Arrays]]
- [[Linked List]]
- [[Stack & Queue]]

### Phase 2 — Trees and binary search trees

_6.006 Lectures 5–6; CLRS Ch. 12_

Tree terminology, binary trees, traversals (in-order, pre-order, post-order, level-order). BST property, search, insert, delete. In-order traversal = sorted output. Degeneration to $O(n)$ in the worst case.

- [[Trees]]
- [[Binary Search Tree]]

### Phase 3 — Balanced BSTs

_6.006 Lectures 6–7; CLRS Ch. 13_

AVL trees: height invariant, rotation types (LL, RR, LR, RL), $O(\log n)$ guarantee. Red-black trees: five properties, rebalancing via recolouring and rotations, used in standard library implementations (`std::map`, `TreeMap`). B-trees: high-fanout, designed for disk I/O, block-aligned pages, used in database indexes.

- [[AVL Tree]]
- [[Red-Black Tree]]
- [[B-Tree]]

### Phase 4 — Priority queues and heaps

_6.006 Lecture 4; CLRS Ch. 6_

Binary heap: max-heap and min-heap properties, complete binary tree stored in an array. `heapify`, `insert`, `extract-min/max` in $O(\log n)$. Heap sort. Priority queue ADT.

- [[Heap]]

### Phase 5 — Hashing

_6.006 Lectures 8–10; CLRS Ch. 11_

Hash functions, collision resolution: chaining vs open addressing (linear probing, quadratic probing, double hashing). Load factor and resizing. Expected $O(1)$ operations. Bloom filter: probabilistic membership, false positives, no false negatives, no deletion.

- [[Hash Tables]]
- [[Bloom Filter]]

### Phase 6 — Graph representations and union-find

_6.006 Lectures 13–14; CLRS Ch. 20–21_

Adjacency list, adjacency matrix, edge list — space and time trade-offs, sparse vs dense choice. Disjoint set (union-find): naive, union by rank, path compression, near-$O(1)$ amortised per operation via inverse Ackermann $\alpha(n)$. Application: Kruskal's MST.

- [[Graphs]]
- [[Disjoint Set]]

## Completion

A phase is **passed** when every note it owns has `status: complete` and an exam is recorded in `PROGRESS.md`. Course complete when all 6 phases passed (grade ≥ C). Final grade = weighted average (later phases weighted higher).

## Reference materials

- Lectures and problem sets: [MIT OCW 6.006 Introduction to Algorithms, Fall 2011](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/)
- Textbook: CLRS — _Introduction to Algorithms_, 4e (Cormen, Leiserson, Rivest, Stein) — commercial, widely available
- Companion course (advanced algorithms): [MIT OCW 6.046J Design and Analysis of Algorithms, Spring 2015](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2015/)

## See also

- [[Index]]
- [[../algorithms/ROADMAP|Algorithms — Course Roadmap]]
- [[../math/discrete/Index|Discrete Math]]
