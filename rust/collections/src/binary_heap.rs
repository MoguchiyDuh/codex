use shared::{print_h2, print_h3};
use std::cmp::Reverse;
use std::collections::BinaryHeap;

pub fn run() {
    print_h2!("BinaryHeap");

    print_h3!("Creation");

    // BinaryHeap<T>: max-heap - pop() always returns the largest element
    // O(1) peek, O(log n) push/pop
    // Requires T: Ord

    let mut heap: BinaryHeap<i32> = BinaryHeap::new();

    let from_vec: BinaryHeap<i32> = BinaryHeap::from(vec![3, 1, 4, 1, 5, 9, 2, 6]);
    println!("from vec: {:?}", from_vec);
    // Note: internal layout is not sorted, but peek/pop gives you the max

    let with_capacity: BinaryHeap<i32> = BinaryHeap::with_capacity(16);
    println!("with_capacity(16): capacity = {}", with_capacity.capacity());

    print_h3!("Push and Pop (max-heap)");

    heap.push(5);
    heap.push(1);
    heap.push(8);
    heap.push(3);
    heap.push(10);
    heap.push(2);

    println!("Pushed: [5, 1, 8, 3, 10, 2]");
    println!("len = {}", heap.len());

    // pop removes and returns the maximum element
    while let Some(val) = heap.pop() {
        print!("{} ", val); // always descending order
    }
    println!("(descending order)");

    print_h3!("Peek (no removal)");

    let mut h: BinaryHeap<i32> = BinaryHeap::from(vec![3, 7, 1, 5, 9]);
    println!("peek() = {:?}", h.peek()); // Some(9) - max
    println!("peek_mut: double the max");
    if let Some(mut top) = h.peek_mut() {
        *top *= 2; // in-place mutation of the maximum - heap is fixed after drop
    }
    println!("peek after doubling max: {:?}", h.peek()); // Some(18)

    print_h3!("Min-heap with Reverse<T>");

    // Wrap with Reverse to invert ordering: BinaryHeap becomes a min-heap
    let mut min_heap: BinaryHeap<Reverse<i32>> = BinaryHeap::new();
    for x in [5, 1, 8, 3, 10, 2] {
        min_heap.push(Reverse(x));
    }

    print!("Min-heap pop order: ");
    while let Some(Reverse(val)) = min_heap.pop() {
        print!("{} ", val); // ascending order (smallest first)
    }
    println!();

    print_h3!("Priority Queue (custom priority)");

    #[derive(Debug, Eq, PartialEq)]
    struct Task {
        priority: i32,
        name: String,
    }

    // Implement Ord to use Task in BinaryHeap
    impl Ord for Task {
        fn cmp(&self, other: &Self) -> std::cmp::Ordering {
            return self.priority.cmp(&other.priority); // higher priority = larger
        }
    }

    impl PartialOrd for Task {
        fn partial_cmp(&self, other: &Self) -> Option<std::cmp::Ordering> {
            return Some(self.cmp(other));
        }
    }

    let mut queue: BinaryHeap<Task> = BinaryHeap::new();
    queue.push(Task {
        priority: 3,
        name: String::from("refactor"),
    });
    queue.push(Task {
        priority: 10,
        name: String::from("fix prod outage"),
    });
    queue.push(Task {
        priority: 1,
        name: String::from("update docs"),
    });
    queue.push(Task {
        priority: 7,
        name: String::from("code review"),
    });

    println!("Processing tasks by priority:");
    while let Some(task) = queue.pop() {
        println!("  [{}] {}", task.priority, task.name);
    }

    print_h3!("Shortest Path Pattern (Reverse + priority)");

    // Graph shortest-path algorithms use BinaryHeap<Reverse<(cost, node)>>
    // so that lower cost = higher priority

    #[derive(Eq, PartialEq)]
    struct State {
        cost: u32,
        node: usize,
    }

    impl Ord for State {
        fn cmp(&self, other: &Self) -> std::cmp::Ordering {
            return other
                .cost
                .cmp(&self.cost) // reverse: smaller cost = higher priority
                .then_with(|| self.node.cmp(&other.node));
        }
    }

    impl PartialOrd for State {
        fn partial_cmp(&self, other: &Self) -> Option<std::cmp::Ordering> {
            return Some(self.cmp(other));
        }
    }

    let mut frontier: BinaryHeap<State> = BinaryHeap::new();
    frontier.push(State { cost: 10, node: 2 });
    frontier.push(State { cost: 1, node: 0 });
    frontier.push(State { cost: 5, node: 1 });

    println!("Dijkstra-style frontier (min-cost first):");
    while let Some(State { cost, node }) = frontier.pop() {
        println!("  visit node {} with cost {}", node, cost);
    }

    print_h3!("into_sorted_vec and drain_sorted");

    let unsorted: BinaryHeap<i32> = BinaryHeap::from(vec![3, 1, 4, 1, 5, 9, 2, 6]);
    let sorted: Vec<i32> = unsorted.into_sorted_vec(); // consumes heap, returns ascending Vec
    println!("into_sorted_vec() = {:?}", sorted);

    // drain_sorted() is nightly-only; use into_sorted_vec() on stable
    let heap2: BinaryHeap<i32> = BinaryHeap::from(vec![3, 1, 4, 1, 5]);
    let ascending: Vec<i32> = heap2.into_sorted_vec(); // ascending, stable
    println!("into_sorted_vec() = {:?}", ascending);

    print_h3!("Extend and Retain");

    let mut h3: BinaryHeap<i32> = BinaryHeap::from(vec![1, 2, 3]);
    h3.extend([4, 5, 6]);
    println!("After extend: peek = {:?}", h3.peek());

    h3.retain(|x| *x % 2 == 0); // keep evens only
    println!("After retain(even): {:?}", h3.into_sorted_vec());

    print_h3!("When to Use BinaryHeap");
    println!("BinaryHeap: when you always need the min or max of a changing collection");
    println!("  - Task schedulers (highest priority job)");
    println!("  - Dijkstra's algorithm (lowest cost node)");
    println!("  - Top-K elements (pop K times)");
    println!("  - Event queues (earliest timestamp first)");
    println!("NOT for: searching arbitrary elements, range queries -> use BTreeMap/Vec");
}
