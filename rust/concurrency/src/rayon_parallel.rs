use rayon::prelude::*;
use shared::{print_h2, print_h3};
use std::time::Instant;

pub fn run() {
    print_h2!("Rayon Parallelism");
    basic_parallel_iteration();
    parallel_methods();
    thread_pool_config();
    performance_comparison();
}

fn basic_parallel_iteration() {
    print_h3!("Basic Parallel Iteration");
    let mut data: Vec<i32> = vec![1, 2, 3, 4, 5, 6, 7, 8];

    println!("  Original: {:?}", data);

    // Parallel mutable iteration
    data.par_iter_mut().for_each(|x| {
        *x *= 2;
    });

    println!("  After par_iter_mut: {:?}", data);

    // Parallel map and collect
    let squared: Vec<i32> = data.par_iter().map(|x| x * x).collect();
    println!("  Squared: {:?}", squared);

    // Parallel filter
    let evens: Vec<i32> = data.par_iter().filter(|&&x| x % 2 == 0).copied().collect();
    println!("  Even numbers: {:?}", evens);

    // Parallel filter_map
    let processed: Vec<i32> = data
        .par_iter()
        .filter_map(|&x| if x > 5 { Some(x * 2) } else { None })
        .collect();
    println!("  Filtered and mapped: {:?}", processed);
}

fn parallel_methods() {
    print_h3!("Parallel Methods");
    let data: Vec<i32> = (1..=100).collect();

    // par_chunks - process in parallel chunks
    let chunk_sums: Vec<i32> = data
        .par_chunks(10)
        .map(|chunk| chunk.iter().sum())
        .collect();
    println!("  Chunk sums (10 per chunk): {:?}", &chunk_sums[..5]);

    // par_windows - sliding windows (must use sequential)
    // Note: windows doesn't have a parallel version

    // fold splits into per-thread local accumulators (|| 0 = identity factory), then
    // reduce combines those partial results into the final value — two-phase reduction
    let sum: i32 = data
        .par_iter()
        .fold(|| 0, |acc, &x| acc + x)
        .reduce(|| 0, |a, b| a + b);
    println!("  Parallel fold sum: {}", sum);

    // reduce - parallel reduction
    let product: i32 = (1..=10).into_par_iter().reduce(|| 1, |a, b| a * b);
    println!("  Parallel product: {}", product);

    // find_any returns the first match found on ANY thread — result is non-deterministic
    let found: Option<&i32> = data.par_iter().find_any(|&&x| x > 50);
    println!("  Found value > 50: {:?}", found);

    // all and any - parallel predicates
    let all_positive: bool = data.par_iter().all(|&x| x > 0);
    let any_over_50: bool = data.par_iter().any(|&x| x > 50);
    println!(
        "  All positive: {}, Any > 50: {}",
        all_positive, any_over_50
    );

    // partition - split into two collections
    let (evens, odds): (Vec<i32>, Vec<i32>) = data.into_par_iter().partition(|x| x % 2 == 0);
    println!("  Evens count: {}, Odds count: {}", evens.len(), odds.len());
}

fn thread_pool_config() {
    print_h3!("Thread Pool Configuration");
    // Default pool uses all CPU cores
    println!("  Default thread count: {}", rayon::current_num_threads());

    // Custom thread pool
    let pool: rayon::ThreadPool = rayon::ThreadPoolBuilder::new()
        .num_threads(4)
        .build()
        .unwrap(); // ERROR: can fail if invalid config

    pool.install(|| {
        let data: Vec<i32> = (1..=100).collect();
        let sum: i32 = data.par_iter().sum();
        println!("  Sum using custom 4-thread pool: {}", sum);
    });

    // Thread pool with name prefix
    let pool: rayon::ThreadPool = rayon::ThreadPoolBuilder::new()
        .num_threads(2)
        .thread_name(|i| format!("custom-worker-{}", i))
        .build()
        .unwrap();

    pool.install(|| {
        (0..10).into_par_iter().for_each(|i| {
            println!("  Processing {} on {:?}", i, std::thread::current().id());
        });
    });
}

fn performance_comparison() {
    print_h3!("Performance Comparison");
    let size: usize = 10_000_000;
    let data: Vec<u64> = (0..size as u64).collect();

    // Sequential sum
    let start_seq: Instant = Instant::now();
    let sum_seq: u64 = data.iter().sum();
    let dur_seq: std::time::Duration = start_seq.elapsed();
    println!("  Sequential sum: {} in {:?}", sum_seq, dur_seq);

    // Parallel sum
    let start_par: Instant = Instant::now();
    let sum_par: u64 = data.par_iter().sum();
    let dur_par: std::time::Duration = start_par.elapsed();
    println!("  Parallel sum: {} in {:?}", sum_par, dur_par);

    let speedup: f64 = dur_seq.as_secs_f64() / dur_par.as_secs_f64();
    println!("  Speedup: {:.2}x", speedup);

    // Sequential map
    let start_seq: Instant = Instant::now();
    let _: Vec<u64> = data.iter().map(|&x| x * x).collect();
    let dur_seq: std::time::Duration = start_seq.elapsed();
    println!("  Sequential map: {:?}", dur_seq);

    // Parallel map
    let start_par: Instant = Instant::now();
    let _: Vec<u64> = data.par_iter().map(|&x| x * x).collect();
    let dur_par: std::time::Duration = start_par.elapsed();
    println!("  Parallel map: {:?}", dur_par);

    let speedup: f64 = dur_seq.as_secs_f64() / dur_par.as_secs_f64();
    println!("  Map speedup: {:.2}x", speedup);

    // Small workload overhead demonstration
    let small_data: Vec<i32> = (0..100).collect();

    let start_seq: Instant = Instant::now();
    let _: i32 = small_data.iter().sum();
    let dur_seq: std::time::Duration = start_seq.elapsed();

    let start_par: Instant = Instant::now();
    let _: i32 = small_data.par_iter().sum();
    let dur_par: std::time::Duration = start_par.elapsed();

    println!(
        "  Small data (100 elements): seq {:?}, par {:?}",
        dur_seq, dur_par
    );
    println!("  Note: Parallel has overhead, not always faster for small data");
}
