use shared::{print_h2, print_h3};

pub fn run() {
    print_h2!("Iterator Consumers");

    // Consumers trigger evaluation and produce final results
    // They consume the iterator (can't use it after)

    let numbers: Vec<i32> = vec![1, 2, 3, 4, 5];

    print_h3!("collect");
    // Collect into any FromIterator type
    let collected_vec: Vec<i32> = numbers.iter().copied().collect();
    println!("collect Vec: {:?}", collected_vec);

    let collected_string: String = vec!['h', 'e', 'l', 'l', 'o'].into_iter().collect();
    println!("collect String: {}", collected_string);

    use std::collections::{HashMap, HashSet};
    let set: HashSet<i32> = numbers.iter().copied().collect();
    println!("collect HashSet: {:?}", set);

    // Collecting into Result<Vec<T>, E>: if any element is Err, the whole collect returns Err.
    // This is short-circuit collection — stops on first error (vs. collecting all errors).
    let strings: Vec<&str> = vec!["1", "2", "3"];
    let parsed: Result<Vec<i32>, _> = strings.iter().map(|s| s.parse::<i32>()).collect();
    println!("collect Result: {:?}", parsed);

    print_h3!("count");
    let count: usize = numbers.iter().count();
    println!("\ncount: {}", count);

    let count_filtered: usize = numbers.iter().filter(|&&x| x > 2).count();
    println!("count (filtered): {}", count_filtered);

    print_h3!("sum");
    let sum: i32 = numbers.iter().sum();
    println!("\nsum: {}", sum);

    let sum_squares: i32 = numbers.iter().map(|x| x * x).sum();
    println!("sum of squares: {}", sum_squares);

    print_h3!("product");
    let product: i32 = numbers.iter().product();
    println!("\nproduct: {}", product);

    print_h3!("min / max");
    let min: Option<&i32> = numbers.iter().min();
    let max: Option<&i32> = numbers.iter().max();
    println!("\nmin: {:?}, max: {:?}", min, max);

    // min_by / max_by with custom comparator
    let strings: Vec<&str> = vec!["aaa", "bb", "cccc", "d"];
    let longest: Option<&&str> = strings.iter().max_by_key(|s| s.len());
    println!("longest string: {:?}", longest);

    print_h3!("find");
    // Find first element matching predicate
    let found: Option<&i32> = numbers.iter().find(|&&x| x > 3);
    println!("\nfind (>3): {:?}", found);

    let not_found: Option<&i32> = numbers.iter().find(|&&x| x > 10);
    println!("find (>10): {:?}", not_found);

    print_h3!("position");
    // Find index of first matching element
    let pos: Option<usize> = numbers.iter().position(|&x| x == 3);
    println!("\nposition (==3): {:?}", pos);

    print_h3!("any");
    // Check if any element matches predicate
    let has_even: bool = numbers.iter().any(|&x| x % 2 == 0);
    println!("\nany even: {}", has_even);

    let has_negative: bool = numbers.iter().any(|&x| x < 0);
    println!("any negative: {}", has_negative);

    print_h3!("all");
    // Check if all elements match predicate
    let all_positive: bool = numbers.iter().all(|&x| x > 0);
    println!("\nall positive: {}", all_positive);

    let all_even: bool = numbers.iter().all(|&x| x % 2 == 0);
    println!("all even: {}", all_even);

    print_h3!("fold");
    // Accumulate values with initial state
    let sum_fold: i32 = numbers.iter().fold(0, |acc, x| acc + x);
    println!("\nfold sum: {}", sum_fold);

    let product_fold: i32 = numbers.iter().fold(1, |acc, x| acc * x);
    println!("fold product: {}", product_fold);

    // Build string with fold
    let concatenated: String = vec!["a", "b", "c"]
        .iter()
        .fold(String::new(), |acc, s| acc + s);
    println!("fold concat: {}", concatenated);

    print_h3!("reduce");
    // reduce uses the first element as the initial accumulator, so the closure receives T, not &T.
    // Returns None for empty iterators (fold would just return the initial value).
    let sum_reduce: Option<i32> = numbers.iter().copied().reduce(|acc, x| acc + x);
    println!("\nreduce sum: {:?}", sum_reduce);

    let empty: Vec<i32> = vec![];
    let empty_reduce: Option<i32> = empty.iter().copied().reduce(|acc, x| acc + x);
    println!("reduce empty: {:?}", empty_reduce);

    print_h3!("for_each");
    // Execute closure for each element (like for loop)
    println!("\nfor_each:");
    numbers.iter().for_each(|x| println!("  {}", x));

    print_h3!("nth");
    // Get nth element (0-indexed)
    let third: Option<&i32> = numbers.iter().nth(2);
    println!("\nnth(2): {:?}", third);

    // nth consumes elements up to n
    let mut iter = numbers.iter();
    let _skip_to_third: Option<&i32> = iter.nth(2);
    let after_third: Option<&i32> = iter.next();
    println!("after nth(2), next: {:?}", after_third);

    print_h3!("last");
    let last: Option<&i32> = numbers.iter().last();
    println!("\nlast: {:?}", last);

    print_h3!("partition");
    // Split into two collections based on predicate
    let (evens, odds): (Vec<i32>, Vec<i32>) = numbers.iter().copied().partition(|&x| x % 2 == 0);
    println!("\npartition evens: {:?}", evens);
    println!("partition odds: {:?}", odds);

    print_h3!("unzip");
    // Split iterator of tuples into two collections
    let pairs: Vec<(i32, i32)> = vec![(1, 10), (2, 20), (3, 30)];
    let (firsts, seconds): (Vec<i32>, Vec<i32>) = pairs.into_iter().unzip();
    println!("\nunzip firsts: {:?}", firsts);
    println!("unzip seconds: {:?}", seconds);

    print_h3!("try_fold");
    // fold that can short-circuit on error
    let try_sum: Result<i32, String> = numbers.iter().try_fold(0, |acc, &x| {
        if x > 10 {
            return Err(String::from("too large"));
        }
        return Ok(acc + x);
    });
    println!("\ntry_fold: {:?}", try_sum);

    print_h3!("try_for_each");
    let try_result: Result<(), String> = numbers.iter().try_for_each(|&x| {
        if x > 10 {
            return Err(String::from("too large"));
        }
        println!("  Processing: {}", x);
        return Ok(());
    });
    println!("try_for_each result: {:?}", try_result);

    print_h3!("Collecting into HashMap");
    let pairs: Vec<(&str, i32)> = vec![("a", 1), ("b", 2), ("c", 3)];
    let map: HashMap<&str, i32> = pairs.into_iter().collect();
    println!("\nHashMap from collect: {:?}", map);

    print_h3!("Consuming with side effects");
    let mut external_sum: i32 = 0;
    numbers.iter().for_each(|x| {
        external_sum += x;
    });
    println!("\nExternal sum: {}", external_sum);

    print_h3!("Short-circuiting");
    // find, any, all short-circuit on first match/mismatch
    let found_early: Option<i32> = (1..=1_000_000).find(|&x| x > 5);
    println!(
        "\nShort-circuit find: {:?} (didn't iterate 1M times)",
        found_early
    );
}
