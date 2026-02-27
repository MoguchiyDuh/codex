use shared::{print_h2, print_h3};
use std::collections::VecDeque;

pub fn run() {
    print_h2!("VecDeque<T>");

    print_h3!("Creation");
    let deque: VecDeque<i32> = VecDeque::new();
    println!("Empty deque: {:?}", deque);

    let deque2: VecDeque<i32> = VecDeque::from([1, 2, 3, 4, 5]);
    println!("From array: {:?}", deque2);

    let vec: Vec<i32> = vec![1, 2, 3];
    let deque3: VecDeque<i32> = VecDeque::from(vec);
    println!("From vec: {:?}", deque3);

    let deque4: VecDeque<i32> = VecDeque::with_capacity(10);
    println!("With capacity: capacity {}", deque4.capacity());

    print_h3!("Adding elements (front)");
    let mut deque5: VecDeque<i32> = VecDeque::new();
    deque5.push_front(10); // Add to front
    deque5.push_front(20);
    deque5.push_front(30);
    println!("After push_front: {:?}", deque5); // [30, 20, 10]

    print_h3!("Adding elements (back)");
    let mut deque6: VecDeque<i32> = VecDeque::new();
    deque6.push_back(1); // Add to back
    deque6.push_back(2);
    deque6.push_back(3);
    println!("After push_back: {:?}", deque6); // [1, 2, 3]

    print_h3!("Removing elements (front)");
    let mut deque7: VecDeque<i32> = VecDeque::from([1, 2, 3, 4, 5]);
    let front: Option<i32> = deque7.pop_front(); // Remove from front
    println!("Popped front: {:?}, deque: {:?}", front, deque7);

    print_h3!("Removing elements (back)");
    let mut deque8: VecDeque<i32> = VecDeque::from([1, 2, 3, 4, 5]);
    let back: Option<i32> = deque8.pop_back(); // Remove from back
    println!("Popped back: {:?}, deque: {:?}", back, deque8);

    print_h3!("Accessing elements");
    let deque9: VecDeque<i32> = VecDeque::from([10, 20, 30, 40, 50]);

    // Front and back
    let front_ref: Option<&i32> = deque9.front();
    let back_ref: Option<&i32> = deque9.back();
    println!("Front: {:?}, Back: {:?}", front_ref, back_ref);

    // Index access
    let element: i32 = deque9[2];
    println!("Element at index 2: {}", element);
    // PANIC: deque9[100] would panic (index out of bounds)

    // Safe access with get
    let safe: Option<&i32> = deque9.get(2);
    let out_of_bounds: Option<&i32> = deque9.get(100);
    println!("Get(2): {:?}, Get(100): {:?}", safe, out_of_bounds);

    print_h3!("Mutable access");
    let mut deque10: VecDeque<i32> = VecDeque::from([1, 2, 3, 4, 5]);

    if let Some(front_mut) = deque10.front_mut() {
        *front_mut *= 10;
    }
    if let Some(back_mut) = deque10.back_mut() {
        *back_mut *= 10;
    }
    println!("After mutating front/back: {:?}", deque10);

    if let Some(element_mut) = deque10.get_mut(2) {
        *element_mut = 999;
    }
    println!("After mutating index 2: {:?}", deque10);

    print_h3!("Length and capacity");
    let mut deque11: VecDeque<i32> = VecDeque::with_capacity(10);
    deque11.push_back(1);
    deque11.push_back(2);
    println!("Len: {}, Capacity: {}", deque11.len(), deque11.capacity());
    println!("Is empty: {}", deque11.is_empty());

    deque11.reserve(20); // Reserve space for 20 MORE elements
    println!("After reserve: capacity {}", deque11.capacity());

    deque11.shrink_to_fit(); // Reduce capacity to fit current len
    println!("After shrink: capacity {}", deque11.capacity());

    print_h3!("Inserting at arbitrary position");
    let mut deque12: VecDeque<i32> = VecDeque::from([1, 2, 4, 5]);
    deque12.insert(2, 3); // Insert 3 at index 2
    println!("After insert at 2: {:?}", deque12);
    // PANIC: deque12.insert(100, 0) would panic (index out of bounds)

    print_h3!("Removing at arbitrary position");
    let mut deque13: VecDeque<i32> = VecDeque::from([1, 2, 3, 4, 5]);
    let removed: Option<i32> = deque13.remove(2); // Remove element at index 2
    println!("Removed: {:?}, deque: {:?}", removed, deque13);
    // PANIC: deque13.remove(100) returns None (out of bounds doesn't panic for remove)

    print_h3!("Rotating");
    let mut deque14: VecDeque<i32> = VecDeque::from([1, 2, 3, 4, 5]);
    println!("Original: {:?}", deque14);

    deque14.rotate_left(2); // Rotate left by 2
    println!("After rotate_left(2): {:?}", deque14); // [3, 4, 5, 1, 2]

    deque14.rotate_right(1); // Rotate right by 1
    println!("After rotate_right(1): {:?}", deque14); // [2, 3, 4, 5, 1]

    print_h3!("Resizing");
    let mut deque15: VecDeque<i32> = VecDeque::from([1, 2, 3]);
    deque15.resize(6, 0); // Resize to 6, fill new with 0
    println!("After resize up: {:?}", deque15);

    deque15.resize(4, 0); // Shrink to 4
    println!("After resize down: {:?}", deque15);

    print_h3!("Truncating");
    let mut deque16: VecDeque<i32> = VecDeque::from([1, 2, 3, 4, 5]);
    deque16.truncate(3); // Keep only first 3
    println!("After truncate: {:?}", deque16);

    print_h3!("Clearing");
    let mut deque17: VecDeque<i32> = VecDeque::from([1, 2, 3, 4, 5]);
    deque17.clear();
    println!(
        "After clear: {:?}, is_empty: {}",
        deque17,
        deque17.is_empty()
    );

    print_h3!("Iteration");
    let deque18: VecDeque<i32> = VecDeque::from([10, 20, 30]);

    // Immutable iteration
    println!("Elements:");
    for element in &deque18 {
        println!("  {}", element);
    }
    println!("deque18 still valid: {:?}", deque18);

    // Mutable iteration
    let mut deque19: VecDeque<i32> = VecDeque::from([1, 2, 3]);
    for element in &mut deque19 {
        *element *= 2;
    }
    println!("After doubling: {:?}", deque19);

    // Consuming iteration (moves deque)
    let deque20: VecDeque<i32> = VecDeque::from([100, 200, 300]);
    for element in deque20 {
        println!("  Consumed: {}", element);
    }
    // ERROR: deque20 is moved
    // println!("{:?}", deque20); // Would fail

    print_h3!("Extending");
    let mut deque21: VecDeque<i32> = VecDeque::from([1, 2, 3]);
    deque21.extend([4, 5, 6]); // Add multiple to back
    println!("After extend: {:?}", deque21);

    print_h3!("Appending");
    let mut deque22: VecDeque<i32> = VecDeque::from([1, 2, 3]);
    let mut deque23: VecDeque<i32> = VecDeque::from([4, 5]);
    deque22.append(&mut deque23); // Move all from deque23 to deque22
    println!("After append: {:?}", deque22);
    println!("deque23 now empty: {:?}", deque23);

    print_h3!("Splitting");
    let mut deque24: VecDeque<i32> = VecDeque::from([1, 2, 3, 4, 5]);
    let deque25: VecDeque<i32> = deque24.split_off(3); // Split at index 3
    println!("First part: {:?}", deque24);
    println!("Second part: {:?}", deque25);

    print_h3!("Retaining");
    let mut deque26: VecDeque<i32> = VecDeque::from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
    deque26.retain(|&x| x % 2 == 0); // Keep only evens
    println!("After retain evens: {:?}", deque26);

    print_h3!("Swapping");
    let mut deque27: VecDeque<i32> = VecDeque::from([1, 2, 3, 4, 5]);
    deque27.swap(0, 4); // Swap first and last
    println!("After swap(0, 4): {:?}", deque27);

    print_h3!("Make contiguous");
    // VecDeque is backed by a ring buffer; its elements may span a wrap-around in memory.
    // make_contiguous() reorganizes them into one contiguous slice — needed for APIs
    // that require &[T] (like sort_unstable_by, or passing to C functions)
    let mut deque28: VecDeque<i32> = VecDeque::from([1, 2, 3, 4, 5]);
    deque28.pop_front();
    deque28.pop_front();
    deque28.push_back(6);
    deque28.push_back(7);
    println!("Before make_contiguous: {:?}", deque28);

    let slice: &[i32] = deque28.make_contiguous();
    println!("Contiguous slice: {:?}", slice);

    print_h3!("As slices");
    let deque29: VecDeque<i32> = VecDeque::from([1, 2, 3, 4, 5]);
    let (slice1, slice2): (&[i32], &[i32]) = deque29.as_slices();
    println!("As slices: {:?} {:?}", slice1, slice2);

    print_h3!("Searching");
    let deque30: VecDeque<i32> = VecDeque::from([10, 20, 30, 40, 50]);
    let contains: bool = deque30.contains(&30);
    println!("Contains 30: {}", contains);

    // Binary search (requires sorted)
    let deque31: VecDeque<i32> = VecDeque::from([1, 2, 3, 4, 5]);
    let result: Result<usize, usize> = deque31.binary_search(&3);
    match result {
        Ok(idx) => println!("Found at index: {}", idx),
        Err(idx) => println!("Not found, would insert at: {}", idx),
    }

    print_h3!("Common patterns");
    // Pattern: Queue (FIFO)
    let mut queue: VecDeque<&str> = VecDeque::new();
    queue.push_back("first");
    queue.push_back("second");
    queue.push_back("third");
    while let Some(item) = queue.pop_front() {
        println!("  Dequeued: {}", item);
    }

    // Pattern: Stack (LIFO)
    let mut stack: VecDeque<i32> = VecDeque::new();
    stack.push_back(1);
    stack.push_back(2);
    stack.push_back(3);
    while let Some(item) = stack.pop_back() {
        println!("  Popped: {}", item);
    }

    // Pattern: Rotating buffer
    let mut buffer: VecDeque<i32> = VecDeque::from([1, 2, 3, 4, 5]);
    buffer.rotate_left(1);
    println!("Rotated buffer: {:?}", buffer);
}
