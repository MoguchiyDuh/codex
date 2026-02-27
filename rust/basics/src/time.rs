use shared::{print_h2, print_h3};
use std::time::{Duration, Instant, SystemTime, UNIX_EPOCH};

pub fn run() {
    print_h2!("std::time");

    print_h3!("Duration");

    let one_sec: Duration = Duration::from_secs(1);
    let half_sec: Duration = Duration::from_millis(500);
    let one_min: Duration = Duration::from_secs(60);
    let tiny: Duration = Duration::from_nanos(250);

    println!("from_secs(1)     = {:?}", one_sec);
    println!("from_millis(500) = {:?}", half_sec);
    println!("from_secs(60)    = {:?}", one_min);
    println!("from_nanos(250)  = {:?}", tiny);

    // Duration arithmetic
    let sum: Duration = one_sec + half_sec;
    let diff: Duration = one_sec - half_sec;
    let scaled: Duration = half_sec * 4;
    println!("1s + 0.5s  = {:?}", sum);
    println!("1s - 0.5s  = {:?}", diff);
    println!("0.5s * 4   = {:?}", scaled);

    // Extracting components
    let d: Duration = Duration::from_millis(12345);
    println!("12345ms: as_secs()  = {}", d.as_secs());
    println!("12345ms: as_millis()= {}", d.as_millis());
    println!("12345ms: as_micros()= {}", d.as_micros());
    println!("12345ms: as_nanos() = {}", d.as_nanos());
    println!("12345ms: as_secs_f64() = {:.3}", d.as_secs_f64());

    // Checked arithmetic (avoids panic on overflow)
    let big: Duration = Duration::MAX;
    let checked: Option<Duration> = big.checked_add(Duration::from_secs(1));
    println!("Duration::MAX.checked_add(1s) = {:?}", checked); // None - overflow

    // Zero and comparisons
    println!("Duration::ZERO = {:?}", Duration::ZERO);
    println!("Duration::MAX  = {:?}", Duration::MAX);
    println!("1s > 500ms: {}", one_sec > half_sec);

    print_h3!("Instant (monotonic, for measuring elapsed time)");

    // Instant is monotonic: always moves forward, unaffected by system clock changes
    // Use Instant for: benchmarks, timeouts, measuring durations
    // Do NOT use SystemTime for measuring elapsed time (can go backward with NTP)

    let start: Instant = Instant::now();

    // Simulate some work
    let mut sum: u64 = 0;
    for i in 0..1_000_000u64 {
        sum = sum.wrapping_add(i);
    }

    let elapsed: Duration = start.elapsed();
    println!("Sum to 1M = {} (computed in {:?})", sum, elapsed);
    println!("elapsed as_micros = {}", elapsed.as_micros());

    // Instant arithmetic
    let t1: Instant = Instant::now();
    std::thread::sleep(Duration::from_millis(1));
    let t2: Instant = Instant::now();
    let between: Duration = t2 - t1; // t2.duration_since(t1)
    println!("sleep(1ms) actual elapsed = {:?}", between);

    // Instant::now() snapshot
    let snapshot: Instant = Instant::now();
    let later_elapsed: Duration = snapshot.elapsed(); // time since snapshot
    println!("snapshot.elapsed() = {:?}", later_elapsed);

    // Timeout check pattern
    let deadline: Instant = Instant::now() + Duration::from_secs(10);
    let time_left: Option<Duration> = deadline.checked_duration_since(Instant::now());
    println!(
        "time_left until 10s deadline: {:?}",
        time_left.map(|d| format!("{:.3}s", d.as_secs_f64()))
    );

    print_h3!("SystemTime (wall clock, for timestamps)");

    // SystemTime can go backward (NTP adjustments), is not monotonic
    // Use SystemTime for: file timestamps, log entries, "what time is it now"

    let now: SystemTime = SystemTime::now();
    println!("SystemTime::now() = {:?}", now);

    // Duration since Unix epoch
    let since_epoch: Duration = now.duration_since(UNIX_EPOCH).unwrap();
    println!("seconds since epoch  = {}", since_epoch.as_secs());
    println!("as Unix timestamp    = {}", since_epoch.as_secs());

    // System time arithmetic
    let future: SystemTime = now + Duration::from_secs(3600); // 1 hour from now
    let past: SystemTime = now - Duration::from_secs(3600); // 1 hour ago

    let until_future: Duration = future.duration_since(now).unwrap();
    println!("1h in future - now   = {:?}", until_future);

    // duration_since returns Err if the argument is later than self
    let err: Result<Duration, _> = past.duration_since(now); // past < now -> Err
    println!("past.duration_since(now) = {:?}", err.is_err());

    print_h3!("Formatting timestamps");

    // std doesn't include formatting - use chrono or time crates for that
    // But you can get raw seconds and format manually
    let epoch_secs: u64 = since_epoch.as_secs();
    let hours: u64 = (epoch_secs / 3600) % 24;
    let mins: u64 = (epoch_secs / 60) % 60;
    let secs: u64 = epoch_secs % 60;
    println!("UTC time (naive) = {:02}:{:02}:{:02}", hours, mins, secs);
    println!("For proper formatting: use the 'chrono' or 'time' crate");

    print_h3!("thread::sleep");

    let before: Instant = Instant::now();
    std::thread::sleep(Duration::from_millis(5));
    println!("sleep(5ms) actual = {:?}", before.elapsed());

    // ZERO sleep yields the thread without busy-waiting
    std::thread::sleep(Duration::ZERO);
    println!("sleep(ZERO) - yields thread");

    print_h3!("Benchmark pattern");

    fn bench<F: FnOnce()>(label: &str, f: F) {
        let start: Instant = Instant::now();
        f();
        println!("{}: {:?}", label, start.elapsed());
    }

    bench("collect 100k", || {
        let _v: Vec<u64> = (0..100_000u64).collect();
    });

    bench("sum 100k", || {
        let _s: u64 = (0..100_000u64).sum();
    });
}
