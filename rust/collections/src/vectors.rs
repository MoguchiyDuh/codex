use shared::{print_h2, print_h3};

pub fn run() {
    print_h2!("Vec<T>");

    print_h3!("Creation");
    let v: Vec<i32> = Vec::new(); // Empty vector
    let v2: Vec<i32> = vec![1, 2, 3, 4, 5]; // vec! macro
    let v3: Vec<i32> = Vec::with_capacity(10); // Pre-allocate capacity
    println!("Empty: {:?}, Macro: {:?}", v, v2);
    println!("Capacity pre-allocated: {}", v3.capacity());

    // From iterator
    let v_range: Vec<i32> = (0..5).collect();
    println!("From range: {:?}", v_range);

    // Repeat same value
    let v_repeat: Vec<i32> = vec![0; 5]; // [0, 0, 0, 0, 0]
    println!("Repeated: {:?}", v_repeat);

    print_h3!("Adding elements");
    let mut v4: Vec<i32> = Vec::new();
    v4.push(10); // Add to end
    v4.push(20);
    v4.push(30);
    println!("After pushes: {:?}", v4);

    let mut v5: Vec<i32> = vec![1, 2, 3];
    v5.insert(1, 99); // Insert at index 1, shifts rest right
    println!("After insert at 1: {:?}", v5);
    // PANIC: v5.insert(100, 0) would panic (index out of bounds)

    print_h3!("Accessing elements");
    let v6: Vec<i32> = vec![10, 20, 30, 40];
    let first: i32 = v6[0]; // Direct indexing
    println!("First: {}", first);
    // PANIC: v6[100] would panic (index out of bounds)

    // Safe access with get
    let maybe_second: Option<&i32> = v6.get(1);
    match maybe_second {
        Some(val) => println!("Second: {}", val),
        None => println!("No second element"),
    }
    let out_of_bounds: Option<&i32> = v6.get(100); // Returns None, no panic
    println!("Out of bounds: {:?}", out_of_bounds);

    // First/last shortcuts
    let first_ref: Option<&i32> = v6.first();
    let last_ref: Option<&i32> = v6.last();
    println!("First: {:?}, Last: {:?}", first_ref, last_ref);

    print_h3!("Removing elements");
    let mut v7: Vec<i32> = vec![1, 2, 3, 4, 5];
    let popped: Option<i32> = v7.pop(); // Remove from end
    println!("Popped: {:?}, vec: {:?}", popped, v7);

    let removed: i32 = v7.remove(1); // Remove at index, shifts rest left
    println!("Removed: {}, vec: {:?}", removed, v7);
    // PANIC: v7.remove(100) would panic (index out of bounds)

    let mut v8: Vec<i32> = vec![1, 2, 3, 4, 5];
    // swap_remove is O(1) vs remove's O(n) — it swaps the target with the last element first
    let swapped: i32 = v8.swap_remove(1); // Swap with last, then pop (faster, breaks order)
    println!("Swap removed: {}, vec: {:?}", swapped, v8);

    print_h3!("Length and capacity");
    let mut v9: Vec<i32> = Vec::with_capacity(10);
    v9.push(1);
    v9.push(2);
    println!("Len: {}, Capacity: {}", v9.len(), v9.capacity());
    println!("Is empty: {}", v9.is_empty());

    v9.reserve(20); // Ensure capacity for 20 MORE elements
    println!("After reserve: capacity {}", v9.capacity());

    v9.shrink_to_fit(); // Reduce capacity to len
    println!("After shrink: capacity {}", v9.capacity());

    print_h3!("Modifying content");
    let mut v10: Vec<i32> = vec![1, 2, 3];
    v10.resize(5, 0); // Resize to 5, fill new with 0
    println!("After resize up: {:?}", v10);

    v10.resize(3, 0); // Shrink to 3
    println!("After resize down: {:?}", v10);

    let mut v11: Vec<i32> = vec![1, 2, 3];
    v11.extend([4, 5, 6]); // Add multiple
    println!("After extend: {:?}", v11);

    let mut v12: Vec<i32> = vec![1, 2, 3];
    let mut v13: Vec<i32> = vec![4, 5];
    v12.append(&mut v13); // Move all from v13 to v12
    println!("After append: {:?}", v12);
    println!("v13 now empty: {:?}", v13);

    let mut v14: Vec<i32> = vec![1, 2, 3, 4, 5];
    v14.truncate(3); // Keep only first 3
    println!("After truncate: {:?}", v14);

    let mut v15: Vec<i32> = vec![1, 2, 3, 4, 5];
    v15.clear(); // Remove all
    println!("After clear: {:?}, is_empty: {}", v15, v15.is_empty());

    print_h3!("Iteration");
    let v16: Vec<i32> = vec![10, 20, 30];
    // Immutable iteration
    for val in &v16 {
        println!("  Immutable: {}", val);
    }
    println!("v16 still valid: {:?}", v16);

    // Mutable iteration
    let mut v17: Vec<i32> = vec![1, 2, 3];
    for val in &mut v17 {
        *val *= 2; // Double each
    }
    println!("After doubling: {:?}", v17);

    // Consuming iteration (moves vector)
    let v18: Vec<i32> = vec![100, 200, 300];
    for val in v18 {
        println!("  Consumed: {}", val);
    }
    // ERROR: v18 is moved
    // println!("{:?}", v18); // Would fail

    // Enumerate
    let v19: Vec<&str> = vec!["a", "b", "c"];
    for (i, val) in v19.iter().enumerate() {
        println!("  Index {}: {}", i, val);
    }

    print_h3!("Searching");
    let v20: Vec<i32> = vec![1, 2, 3, 4, 5];
    let contains_3: bool = v20.contains(&3);
    println!("Contains 3: {}", contains_3);

    let position: Option<usize> = v20.iter().position(|&x| x == 3);
    println!("Position of 3: {:?}", position);

    // Binary search (requires sorted): Ok(idx) = found, Err(idx) = insertion point
    let v21: Vec<i32> = vec![1, 2, 3, 4, 5];
    let result: Result<usize, usize> = v21.binary_search(&3);
    match result {
        Ok(idx) => println!("Found at index: {}", idx),
        Err(idx) => println!("Not found, would insert at: {}", idx),
    }

    print_h3!("Sorting");
    let mut v22: Vec<i32> = vec![5, 2, 8, 1, 9];
    v22.sort(); // Ascending
    println!("Sorted: {:?}", v22);

    v22.sort_by(|a, b| b.cmp(a)); // Descending
    println!("Reverse sorted: {:?}", v22);

    let mut v23: Vec<i32> = vec![5, -2, 8, -1, 9];
    v23.sort_by_key(|x| x.abs()); // Sort by absolute value
    println!("Sorted by abs: {:?}", v23);

    print_h3!("Deduplication");
    let mut v24: Vec<i32> = vec![1, 2, 2, 3, 3, 3, 4];
    v24.dedup(); // Remove consecutive duplicates (requires sorted for full dedup)
    println!("After dedup: {:?}", v24);

    let mut v25: Vec<i32> = vec![1, 2, 1, 3, 2, 4];
    v25.sort();
    v25.dedup(); // Full dedup: sort first
    println!("Fully deduped: {:?}", v25);

    print_h3!("Filtering");
    let mut v26: Vec<i32> = vec![1, 2, 3, 4, 5, 6];
    v26.retain(|&x| x % 2 == 0); // Keep only evens
    println!("After retain evens: {:?}", v26);

    let v27: Vec<i32> = vec![1, 2, 3, 4, 5, 6];
    let evens: Vec<i32> = v27.iter().filter(|&&x| x % 2 == 0).copied().collect();
    println!("Filtered evens: {:?}", evens);
    println!("Original still valid: {:?}", v27);

    print_h3!("Splitting");
    let mut v28: Vec<i32> = vec![1, 2, 3, 4, 5];
    let v29: Vec<i32> = v28.split_off(3); // Split at index 3
    println!("First part: {:?}", v28);
    println!("Second part: {:?}", v29);

    let v30: Vec<i32> = vec![1, 2, 3, 4, 5, 6];
    let chunks: Vec<&[i32]> = v30.chunks(2).collect();
    println!("Chunks of 2: {:?}", chunks);

    let windows: Vec<&[i32]> = v30.windows(3).collect();
    println!("Windows of 3: {:?}", windows);

    print_h3!("Transformations (iterators)");
    let v31: Vec<i32> = vec![1, 2, 3, 4, 5];
    let doubled: Vec<i32> = v31.iter().map(|x| x * 2).collect();
    println!("Doubled: {:?}", doubled);

    let sum: i32 = v31.iter().sum();
    println!("Sum: {}", sum);

    let product: i32 = v31.iter().product();
    println!("Product: {}", product);

    print_h3!("Reversing");
    let mut v32: Vec<i32> = vec![1, 2, 3, 4, 5];
    v32.reverse(); // In-place
    println!("Reversed: {:?}", v32);

    let v33: Vec<i32> = vec![1, 2, 3, 4, 5];
    let reversed: Vec<i32> = v33.iter().rev().copied().collect();
    println!("Reversed copy: {:?}", reversed);

    print_h3!("Swapping");
    let mut v34: Vec<i32> = vec![1, 2, 3, 4, 5];
    v34.swap(0, 4); // Swap first and last
    println!("After swap: {:?}", v34);

    print_h3!("Multidimensional vectors");
    let v35: Vec<Vec<i32>> = vec![vec![1, 2], vec![3, 4], vec![5, 6]];
    println!("2D vector: {:?}", v35);
    let element: i32 = v35[1][0];
    println!("Element [1][0]: {}", element);
    // PANIC: v35[10][0] would panic (index out of bounds on outer)

    print_h3!("Cloning and copying");
    let v36: Vec<i32> = vec![1, 2, 3];
    let v37: Vec<i32> = v36.clone(); // Deep copy
    println!("Original: {:?}, Clone: {:?}", v36, v37);

    print_h3!("Common patterns");
    // Pattern: Collect from iterator
    let v38: Vec<i32> = (0..10).filter(|x| x % 2 == 0).collect();
    println!("Evens 0-9: {:?}", v38);

    // Pattern: Flatten nested
    let nested: Vec<Vec<i32>> = vec![vec![1, 2], vec![3, 4]];
    let flat: Vec<i32> = nested.into_iter().flatten().collect();
    println!("Flattened: {:?}", flat);

    // Pattern: Remove while iterating (use retain or filter)
    let mut v39: Vec<i32> = vec![1, 2, 3, 4, 5];
    v39.retain(|&x| x != 3); // Remove 3
    println!("After removing 3: {:?}", v39);
}
