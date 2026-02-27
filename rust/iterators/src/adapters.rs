use shared::{print_h2, print_h3};

pub fn run() {
    print_h2!("Iterator Adapters");

    // Adapters transform iterators lazily (return new iterators)
    // Nothing happens until consumed (collect, for loop, etc.)

    print_h3!("map");
    let numbers: Vec<i32> = vec![1, 2, 3, 4, 5];
    let doubled: Vec<i32> = numbers.iter().map(|x| x * 2).collect();
    println!("map (x2): {:?}", doubled);

    let squared: Vec<i32> = numbers.iter().map(|x| x * x).collect();
    println!("map (x^2): {:?}", squared);

    print_h3!("filter");
    let evens: Vec<i32> = numbers.iter().copied().filter(|&x| x % 2 == 0).collect();
    println!("\nfilter (evens): {:?}", evens);

    let greater_than_3: Vec<i32> = numbers.iter().copied().filter(|&x| x > 3).collect();
    println!("filter (>3): {:?}", greater_than_3);

    print_h3!("filter_map");
    // Combines filter + map, returns Option
    let strings: Vec<&str> = vec!["1", "two", "3", "four", "5"];
    let parsed: Vec<i32> = strings
        .iter()
        .filter_map(|s| s.parse::<i32>().ok())
        .collect();
    println!("\nfilter_map (parse): {:?}", parsed);

    print_h3!("flat_map");
    // Maps each element to iterator, then flattens
    let nested: Vec<Vec<i32>> = vec![vec![1, 2], vec![3, 4], vec![5]];
    let flattened: Vec<i32> = nested.iter().flat_map(|v| v.iter()).copied().collect();
    println!("\nflat_map: {:?}", flattened);

    let words: Vec<&str> = vec!["hello", "world"];
    let chars: Vec<char> = words.iter().flat_map(|s| s.chars()).collect();
    println!("flat_map chars: {:?}", chars);

    print_h3!("flatten");
    // Flattens nested iterators (like flat_map with identity)
    let nested2: Vec<Vec<i32>> = vec![vec![1, 2], vec![3, 4]];
    let flat: Vec<i32> = nested2.into_iter().flatten().collect();
    println!("\nflatten: {:?}", flat);

    print_h3!("take");
    // Take first N elements
    let first_3: Vec<i32> = numbers.iter().copied().take(3).collect();
    println!("\ntake(3): {:?}", first_3);

    let range_take: Vec<i32> = (1..=100).take(5).collect();
    println!("range take(5): {:?}", range_take);

    print_h3!("skip");
    // Skip first N elements
    let skip_2: Vec<i32> = numbers.iter().copied().skip(2).collect();
    println!("\nskip(2): {:?}", skip_2);

    // Combine skip + take for slicing
    let middle: Vec<i32> = numbers.iter().copied().skip(1).take(3).collect();
    println!("skip(1).take(3): {:?}", middle);

    print_h3!("take_while");
    // Take while predicate is true
    let take_while_result: Vec<i32> = numbers.iter().copied().take_while(|&x| x < 4).collect();
    println!("\ntake_while (<4): {:?}", take_while_result);

    print_h3!("skip_while");
    // Skip while predicate is true
    let skip_while_result: Vec<i32> = numbers.iter().copied().skip_while(|&x| x < 3).collect();
    println!("\nskip_while (<3): {:?}", skip_while_result);

    print_h3!("step_by");
    // Take every Nth element
    let every_2nd: Vec<i32> = numbers.iter().copied().step_by(2).collect();
    println!("\nstep_by(2): {:?}", every_2nd);

    let range_step: Vec<i32> = (0..10).step_by(3).collect();
    println!("range step_by(3): {:?}", range_step);

    print_h3!("chain");
    // Chain two iterators together
    let a: Vec<i32> = vec![1, 2, 3];
    let b: Vec<i32> = vec![4, 5, 6];
    let chained: Vec<i32> = a.iter().chain(b.iter()).copied().collect();
    println!("\nchain: {:?}", chained);

    // Chain multiple
    let c: Vec<i32> = vec![7, 8];
    let triple_chain: Vec<i32> = a.iter().chain(b.iter()).chain(c.iter()).copied().collect();
    println!("triple chain: {:?}", triple_chain);

    print_h3!("zip");
    // Zip two iterators into tuples
    let names: Vec<&str> = vec!["Alice", "Bob", "Charlie"];
    let ages: Vec<i32> = vec![25, 30, 35];
    let zipped: Vec<(&str, i32)> = names.iter().copied().zip(ages.iter().copied()).collect();
    println!("\nzip: {:?}", zipped);

    // Zip stops at shortest
    let short: Vec<i32> = vec![1, 2];
    let long: Vec<i32> = vec![10, 20, 30, 40];
    let zipped_short: Vec<(i32, i32)> = short.iter().copied().zip(long.iter().copied()).collect();
    println!("zip (shortest): {:?}", zipped_short);

    print_h3!("enumerate");
    // Add index to each element
    let fruits: Vec<&str> = vec!["apple", "banana", "cherry"];
    let indexed: Vec<(usize, &str)> = fruits.iter().copied().enumerate().collect();
    println!("\nenumerate: {:?}", indexed);

    print_h3!("peekable");
    // Peek at next element without consuming
    let vec: Vec<i32> = vec![1, 2, 3];
    let mut peekable = vec.iter().peekable();

    println!("\npeekable:");
    while let Some(&val) = peekable.peek() {
        println!("  Peeked: {}", val);
        if *val == 2 {
            println!("  Found 2, advancing");
        }
        peekable.next();
    }

    print_h3!("fuse");
    // Ensures iterator stays None after first None
    // (Most iterators already behave this way)
    let fused = numbers.iter().fuse();
    let count: usize = fused.count();
    println!("\nfuse count: {}", count);

    print_h3!("inspect");
    // Peek at values as they pass through (for debugging)
    let result: Vec<i32> = numbers
        .iter()
        .copied()
        .inspect(|x| println!("  inspect: before map = {}", x))
        .map(|x| x * 2)
        .inspect(|x| println!("  inspect: after map = {}", x))
        .collect();
    println!("inspect result: {:?}", result);

    print_h3!("rev");
    // Reverse iterator (requires DoubleEndedIterator)
    let reversed: Vec<i32> = numbers.iter().copied().rev().collect();
    println!("\nrev: {:?}", reversed);

    print_h3!("cycle");
    // Repeat iterator infinitely
    let cycle_3: Vec<i32> = vec![1, 2, 3].into_iter().cycle().take(10).collect();
    println!("\ncycle().take(10): {:?}", cycle_3);

    print_h3!("cloned and copied");
    let vec_ref: Vec<i32> = vec![1, 2, 3];

    // copied() for Copy types
    let copied_vec: Vec<i32> = vec_ref.iter().copied().collect();
    println!("\ncopied: {:?}", copied_vec);

    // cloned() for Clone types
    let strings: Vec<String> = vec![String::from("a"), String::from("b")];
    let cloned_strings: Vec<String> = strings.iter().cloned().collect();
    println!("cloned: {:?}", cloned_strings);

    print_h3!("Chaining adapters");
    let complex: Vec<i32> = (1..=20)
        .filter(|x| x % 2 == 0) // Keep evens
        .map(|x| x * 3) // Triple them
        .skip(2) // Skip first 2
        .take(4) // Take next 4
        .collect();
    println!("\nChained adapters: {:?}", complex);
}
