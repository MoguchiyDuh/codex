---
tags: [rust, collections, binaryheap, priority-queue]
source: collections/src/binary_heap.rs
---

# BinaryHeap\<T\>

`BinaryHeap<T>` is a max-heap priority queue. `pop()` always returns the largest element. `T` must implement `Ord`. Complexities: O(1) `peek`, O(log n) `push`/`pop`, O(n) construction from a vector.

The internal layout is not sorted — only the invariant that the root is the maximum is maintained.

## Creation

```rust
use std::collections::BinaryHeap;

let mut heap: BinaryHeap<i32> = BinaryHeap::new();
let heap = BinaryHeap::from(vec![3, 1, 4, 1, 5, 9, 2, 6]);
let heap: BinaryHeap<i32> = BinaryHeap::with_capacity(16);
```

## Push and Pop

```rust
heap.push(5);
heap.push(1);
heap.push(10);

while let Some(val) = heap.pop() {
    print!("{} ", val);  // 10 5 1 — always descending
}
```

## Peek (without removing)

```rust
let max: Option<&i32> = heap.peek();  // Some(&max_val), no removal

// peek_mut lets you mutate the maximum element in place
if let Some(mut top) = heap.peek_mut() {
    *top *= 2;  // heap invariant is restored on drop
}
```

## Min-Heap with `Reverse<T>`

`BinaryHeap` is a max-heap by design. Wrap elements in `std::cmp::Reverse` to flip the ordering and get a min-heap.

```rust
use std::cmp::Reverse;

let mut min_heap: BinaryHeap<Reverse<i32>> = BinaryHeap::new();
for x in [5, 1, 8, 3, 10, 2] {
    min_heap.push(Reverse(x));
}

while let Some(Reverse(val)) = min_heap.pop() {
    print!("{} ", val);  // 1 2 3 5 8 10 — ascending
}
```

## Custom Priority Queue

Implement `Ord` (and `PartialOrd`) on your type to control priority.

```rust
#[derive(Debug, Eq, PartialEq)]
struct Task {
    priority: i32,
    name: String,
}

impl Ord for Task {
    fn cmp(&self, other: &Self) -> std::cmp::Ordering {
        self.priority.cmp(&other.priority)  // higher number = higher priority
    }
}

impl PartialOrd for Task {
    fn partial_cmp(&self, other: &Self) -> Option<std::cmp::Ordering> {
        Some(self.cmp(other))
    }
}

let mut queue: BinaryHeap<Task> = BinaryHeap::new();
queue.push(Task { priority: 10, name: "fix prod outage".into() });
queue.push(Task { priority: 1,  name: "update docs".into() });

while let Some(task) = queue.pop() {
    println!("[{}] {}", task.priority, task.name);
}
// [10] fix prod outage
// [1]  update docs
```

## Dijkstra-Style Min-Cost Frontier

For shortest-path algorithms, reverse the cost comparison so lower cost wins:

```rust
#[derive(Eq, PartialEq)]
struct State { cost: u32, node: usize }

impl Ord for State {
    fn cmp(&self, other: &Self) -> std::cmp::Ordering {
        other.cost.cmp(&self.cost)  // reversed: smaller cost = higher priority
            .then_with(|| self.node.cmp(&other.node))
    }
}
impl PartialOrd for State {
    fn partial_cmp(&self, other: &Self) -> Option<std::cmp::Ordering> {
        Some(self.cmp(other))
    }
}

let mut frontier: BinaryHeap<State> = BinaryHeap::new();
frontier.push(State { cost: 10, node: 2 });
frontier.push(State { cost: 1,  node: 0 });
// pop gives node 0 (cost 1) first
```

## Sorted Output

```rust
let heap = BinaryHeap::from(vec![3, 1, 4, 1, 5, 9]);
let sorted: Vec<i32> = heap.into_sorted_vec();  // ascending, consumes heap
// [1, 1, 3, 4, 5, 9]
```

`drain_sorted()` exists on nightly only; use `into_sorted_vec()` on stable.

## Extend and Retain

```rust
heap.extend([4, 5, 6]);           // push multiple
heap.retain(|x| x % 2 == 0);     // remove elements in-place
```

## When to Use

- Task schedulers — always process highest-priority job next.
- Dijkstra's algorithm — lowest-cost node first via `Reverse` or custom `Ord`.
- Top-K elements — push all, pop K times.
- Event queues — earliest timestamp first.

Do not use `BinaryHeap` for: searching arbitrary elements, range queries, or ordered iteration over all elements. Use [[BTreeMap]]/[[Vec]] for those.

## Capacity

```rust
heap.len();
heap.is_empty();
heap.capacity();
heap.reserve(n);
heap.shrink_to_fit();
```

## See Also

- [[Vec]] — use `into_sorted_vec` result if you just need a sorted list
- [[BTreeMap]] — when range queries or full sorted iteration are needed
- [[VecDeque]] — for FIFO/LIFO without priority ordering
