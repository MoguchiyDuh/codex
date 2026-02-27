use shared::{print_h2, print_h3};

pub fn run() {
    print_h2!("Advanced Iterators");

    print_h3!("scan");
    // scan is like fold but yields each intermediate accumulator state as Some(value)
    // returning None from the closure early-terminates the scan (unlike fold which always runs to end)
    let numbers: Vec<i32> = vec![1, 2, 3, 4, 5];
    let running_sum: Vec<i32> = numbers
        .iter()
        .scan(0, |state, x| {
            *state += x;
            return Some(*state);
        })
        .collect();
    println!("scan (running sum): {:?}", running_sum);

    print_h3!("windows");
    // Overlapping slices of size N
    let data: Vec<i32> = vec![1, 2, 3, 4, 5];
    println!("\nwindows(3):");
    for window in data.windows(3) {
        println!("  {:?}", window);
    }

    print_h3!("chunks");
    // Non-overlapping slices of size N
    let data2: Vec<i32> = vec![1, 2, 3, 4, 5, 6, 7];
    println!("\nchunks(3):");
    for chunk in data2.chunks(3) {
        println!("  {:?}", chunk);
    }

    print_h3!("chunks_exact");
    // Like chunks but remainder is separate
    println!("\nchunks_exact(3):");
    let mut iter = data2.chunks_exact(3);
    for chunk in iter.by_ref() {
        println!("  {:?}", chunk);
    }
    println!("  remainder: {:?}", iter.remainder());

    print_h3!("rchunks");
    // Chunks from the end
    println!("\nrchunks(3):");
    for chunk in data2.rchunks(3) {
        println!("  {:?}", chunk);
    }

    print_h3!("split");
    // Split on predicate
    let text: Vec<i32> = vec![1, 0, 2, 3, 0, 4, 5];
    println!("\nsplit (on 0):");
    for part in text.split(|&x| x == 0) {
        println!("  {:?}", part);
    }

    print_h3!("std::iter::once");
    // Create iterator with single element
    let once: Vec<i32> = std::iter::once(42).collect();
    println!("\nonce(42): {:?}", once);

    let combined: Vec<i32> = std::iter::once(0)
        .chain(numbers.iter().copied())
        .chain(std::iter::once(99))
        .collect();
    println!("once + chain: {:?}", combined);

    print_h3!("std::iter::repeat");
    // Infinite iterator repeating value
    let repeated: Vec<i32> = std::iter::repeat(7).take(5).collect();
    println!("\nrepeat(7).take(5): {:?}", repeated);

    print_h3!("std::iter::repeat_with");
    // Repeat with closure (evaluated each time)
    let mut counter: i32 = 0;
    let repeated_fn: Vec<i32> = std::iter::repeat_with(|| {
        counter += 1;
        return counter;
    })
    .take(5)
    .collect();
    println!("\nrepeat_with (counter): {:?}", repeated_fn);

    print_h3!("std::iter::empty");
    // Iterator with no elements
    let empty: Vec<i32> = std::iter::empty().collect();
    println!("\nempty: {:?}", empty);

    print_h3!("std::iter::successors");
    // successors generates a sequence: each step produces next from previous; None stops iteration
    let fibonacci: Vec<u32> = std::iter::successors(Some((0, 1)), |&(a, b)| Some((b, a + b)))
        .map(|(a, _)| a)
        .take(10)
        .collect();
    println!("\nsuccessors (fibonacci): {:?}", fibonacci);

    // Powers of 2
    let powers: Vec<i32> = std::iter::successors(Some(1), |&n| Some(n * 2))
        .take(10)
        .collect();
    println!("successors (powers of 2): {:?}", powers);

    print_h3!("std::iter::from_fn");
    // Create iterator from closure
    let mut count: i32 = 0;
    let from_fn_iter: Vec<i32> = std::iter::from_fn(|| {
        count += 1;
        if count <= 5 {
            return Some(count * 10);
        }
        return None;
    })
    .collect();
    println!("\nfrom_fn: {:?}", from_fn_iter);

    print_h3!("Intersperse");
    // Insert separator between elements (nightly/use itertools)
    // Manual implementation:
    let words: Vec<&str> = vec!["hello", "world", "rust"];
    let mut result: Vec<&str> = Vec::new();
    for (i, word) in words.iter().enumerate() {
        if i > 0 {
            result.push(" ");
        }
        result.push(word);
    }
    println!("\nManual intersperse: {:?}", result);

    print_h3!("Cartesian product");
    let a: Vec<i32> = vec![1, 2];
    let b: Vec<i32> = vec![10, 20];
    let product: Vec<(i32, i32)> = a
        .iter()
        .flat_map(|&x| b.iter().map(move |&y| (x, y)))
        .collect();
    println!("\nCartesian product: {:?}", product);

    print_h3!("Array chunks");
    let arr: [i32; 6] = [1, 2, 3, 4, 5, 6];
    println!("\nslice chunks_exact(2):");
    for chunk in arr.chunks_exact(2) {
        println!("  {:?}", chunk);
    }

    print_h3!("Cycle with take");
    let pattern: Vec<i32> = vec![1, 2, 3];
    let cycled: Vec<i32> = pattern.into_iter().cycle().take(10).collect();
    println!("\ncycle().take(10): {:?}", cycled);

    print_h3!("Map while");
    let result: Vec<i32> = (1..10)
        .map_while(|x| if x < 5 { Some(x * 2) } else { None })
        .collect();
    println!("\nmap_while: {:?}", result);

    print_h3!("Peekable for lookahead");
    let data: Vec<i32> = vec![1, 2, 2, 3, 3, 3, 4];
    let mut peekable = data.iter().peekable();
    println!("\nPeekable (count consecutive):");
    while let Some(&val) = peekable.next() {
        let mut count: usize = 1;
        while peekable.peek() == Some(&&val) {
            count += 1;
            peekable.next();
        }
        println!("  {} appears {} time(s)", val, count);
    }

    print_h3!("Flatten nested Options");
    let nested_opts: Vec<Option<i32>> = vec![Some(1), None, Some(2), Some(3), None];
    let flattened: Vec<i32> = nested_opts.into_iter().flatten().collect();
    println!("\nflatten Options: {:?}", flattened);

    print_h3!("Flatten nested Results");
    let nested_results: Vec<Result<i32, &str>> = vec![Ok(1), Err("error"), Ok(2), Ok(3)];
    let ok_values: Vec<i32> = nested_results.into_iter().flatten().collect();
    println!("flatten Results (Ok only): {:?}", ok_values);

    print_h3!("Step by with offset");
    let offset_step: Vec<i32> = (0..20).skip(1).step_by(3).collect();
    println!("\nskip(1).step_by(3): {:?}", offset_step);

    print_h3!("Parallel batching pattern");
    let large: Vec<i32> = (1..=12).collect();
    let batches: Vec<Vec<i32>> = large.chunks(4).map(|chunk| chunk.to_vec()).collect();
    println!("\nBatches of 4:");
    for (i, batch) in batches.iter().enumerate() {
        println!("  Batch {}: {:?}", i, batch);
    }
}
