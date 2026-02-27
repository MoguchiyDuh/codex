use shared::{print_h2, print_h3};

pub fn run() {
    print_h2!("Iterator Patterns");

    print_h3!("Chaining operations");
    let numbers: Vec<i32> = vec![1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

    let result: Vec<i32> = numbers
        .iter()
        .filter(|&&x| x % 2 == 0) // Keep evens
        .map(|&x| x * x) // Square them
        .filter(|&x| x > 10) // Keep > 10
        .collect();
    println!("Chained pipeline: {:?}", result);

    print_h3!("Grouping elements");
    use std::collections::HashMap;

    let items: Vec<(&str, i32)> = vec![("a", 1), ("b", 2), ("a", 3), ("c", 4), ("b", 5), ("a", 6)];

    let mut grouped: HashMap<&str, Vec<i32>> = HashMap::new();
    for (key, value) in items {
        grouped.entry(key).or_insert_with(Vec::new).push(value);
    }
    println!("\nGrouped: {:?}", grouped);

    print_h3!("Windowed aggregation");
    let temps: Vec<i32> = vec![20, 22, 21, 23, 25, 24, 26];
    let moving_avg: Vec<f64> = temps
        .windows(3)
        .map(|window| window.iter().sum::<i32>() as f64 / 3.0)
        .collect();
    println!("\nMoving average (window 3): {:?}", moving_avg);

    print_h3!("Deduplication");
    let with_dups: Vec<i32> = vec![1, 2, 2, 3, 3, 3, 4, 4, 5];
    let mut deduped: Vec<i32> = Vec::new();
    let mut prev: Option<i32> = None;
    for &x in &with_dups {
        if prev != Some(x) {
            deduped.push(x);
            prev = Some(x);
        }
    }
    println!("\nDeduplicated: {:?}", deduped);

    // Or use itertools-style dedup with peekable
    let mut deduped2: Vec<i32> = Vec::new();
    let mut iter = with_dups.iter().peekable();
    while let Some(&val) = iter.next() {
        deduped2.push(val);
        while iter.peek() == Some(&&val) {
            iter.next();
        }
    }
    println!("Deduplicated (peekable): {:?}", deduped2);

    print_h3!("Chunking with logic");
    let data: Vec<i32> = vec![1, 2, 0, 3, 4, 0, 5, 6, 7];
    let chunks: Vec<Vec<i32>> = data
        .split(|&x| x == 0)
        .filter(|chunk| !chunk.is_empty())
        .map(|chunk| chunk.to_vec())
        .collect();
    println!("\nSplit on 0: {:?}", chunks);

    print_h3!("Parallel iteration pattern");
    let large: Vec<i32> = (1..=100).collect();
    let batch_size: usize = 25;
    let batches: Vec<Vec<i32>> = large
        .chunks(batch_size)
        .map(|chunk| chunk.to_vec())
        .collect();
    println!(
        "\nBatches for parallel processing: {} batches",
        batches.len()
    );

    print_h3!("Two-pass pattern");
    // First pass: collect statistics
    let values: Vec<i32> = vec![10, 20, 30, 40, 50];
    let sum: i32 = values.iter().sum();
    let count: usize = values.len();
    let avg: f64 = sum as f64 / count as f64;

    // Second pass: normalize by average
    let normalized: Vec<f64> = values.iter().map(|&x| x as f64 - avg).collect();
    println!("\nNormalized (mean-centered): {:?}", normalized);

    print_h3!("Filtering with multiple conditions");
    let candidates: Vec<i32> = (1..=100).collect();
    let filtered: Vec<i32> = candidates
        .into_iter()
        .filter(|&x| x % 2 == 0) // Even
        .filter(|&x| x % 3 == 0) // Divisible by 3
        .filter(|&x| x < 50) // Less than 50
        .collect();
    println!("\nMultiple filters: {:?}", filtered);

    print_h3!("Early termination");
    let search: Vec<i32> = (1..=1000).collect();
    let found: Option<&i32> = search.iter().find(|&&x| x * x > 500);
    println!("\nEarly termination (x^2 > 500): {:?}", found);

    print_h3!("Accumulating with state");
    let transactions: Vec<i32> = vec![100, -20, 50, -30, 200];
    let balances: Vec<i32> = transactions
        .iter()
        .scan(0, |balance, &amount| {
            *balance += amount;
            return Some(*balance);
        })
        .collect();
    println!("\nRunning balance: {:?}", balances);

    print_h3!("Interleaving iterators");
    let a: Vec<i32> = vec![1, 3, 5];
    let b: Vec<i32> = vec![2, 4, 6];
    let mut interleaved: Vec<i32> = Vec::new();
    let mut iter_a = a.iter();
    let mut iter_b = b.iter();
    loop {
        match (iter_a.next(), iter_b.next()) {
            (Some(&x), Some(&y)) => {
                interleaved.push(x);
                interleaved.push(y);
            }
            (Some(&x), None) => interleaved.push(x),
            (None, Some(&y)) => interleaved.push(y),
            (None, None) => break,
        }
    }
    println!("\nInterleaved: {:?}", interleaved);

    print_h3!("Conditional mapping");
    let mixed: Vec<i32> = vec![1, -2, 3, -4, 5];
    let transformed: Vec<String> = mixed
        .iter()
        .map(|&x| {
            if x < 0 {
                return format!("negative({})", x.abs());
            } else {
                return format!("positive({})", x);
            }
        })
        .collect();
    println!("\nConditional map: {:?}", transformed);

    print_h3!("Flattening nested structures");
    // Option<Vec<T>> implements IntoIterator (None -> empty, Some(v) -> v.into_iter())
    // so each flatten() peels one nesting layer
    let nested: Vec<Option<Vec<i32>>> = vec![Some(vec![1, 2]), None, Some(vec![3, 4, 5])];
    let flat: Vec<i32> = nested.into_iter().flatten().flatten().collect();
    println!("\nDouble flatten: {:?}", flat);

    print_h3!("Collecting into custom structure");
    struct Stats {
        count: usize,
        sum: i32,
        min: i32,
        max: i32,
    }

    let nums: Vec<i32> = vec![5, 2, 8, 1, 9, 3];
    let stats: Stats = nums.iter().fold(
        Stats {
            count: 0,
            sum: 0,
            min: i32::MAX,
            max: i32::MIN,
        },
        |mut acc, &x| {
            acc.count += 1;
            acc.sum += x;
            acc.min = acc.min.min(x);
            acc.max = acc.max.max(x);
            return acc;
        },
    );
    println!(
        "\nStats: count={}, sum={}, min={}, max={}",
        stats.count, stats.sum, stats.min, stats.max
    );

    print_h3!("Iterator vs for loop performance");
    // Iterators are zero-cost abstractions: the compiler monomorphizes and inlines each adapter,
    // often producing assembly identical to a hand-written loop (no heap allocation, no virtual calls)
    // These compile to similar assembly:

    let data: Vec<i32> = (1..=100).collect();

    // Iterator style (preferred)
    let sum_iter: i32 = data.iter().sum();
    println!("\nIterator sum: {}", sum_iter);

    // For loop style
    let mut sum_loop: i32 = 0;
    for &x in &data {
        sum_loop += x;
    }
    println!("For loop sum: {}", sum_loop);

    print_h3!("Cartesian product");
    let colors: Vec<&str> = vec!["red", "green", "blue"];
    let sizes: Vec<&str> = vec!["small", "large"];
    let combos: Vec<(&str, &str)> = colors
        .iter()
        .flat_map(|&color| sizes.iter().map(move |&size| (color, size)))
        .collect();
    println!("\nCartesian product: {:?}", combos);
}
