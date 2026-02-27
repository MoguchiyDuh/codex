---
tags: [rust, basics, time, duration]
source: basics/src/time.rs
---

# std::time

Three main types: `Duration`, `Instant`, `SystemTime`.

## Duration

A span of time. Constructed from any unit:

```rust
use std::time::Duration;

let d = Duration::from_secs(1);
let d = Duration::from_millis(500);
let d = Duration::from_micros(250);
let d = Duration::from_nanos(100);
let d = Duration::from_secs_f64(1.5);
```

### Arithmetic

```rust
let sum  = Duration::from_secs(1) + Duration::from_millis(500);  // 1.5s
let diff = Duration::from_secs(1) - Duration::from_millis(500);  // 0.5s
let x4   = Duration::from_millis(500) * 4;                       // 2s
```

### Extracting values

```rust
let d = Duration::from_millis(12345);
d.as_secs()         // 12 (truncated)
d.as_millis()       // 12345
d.as_micros()       // 12345000
d.as_nanos()        // 12345000000
d.as_secs_f64()     // 12.345
```

### Overflow-safe arithmetic

```rust
Duration::MAX.checked_add(Duration::from_secs(1))  // None
```

Constants: `Duration::ZERO`, `Duration::MAX`.

---

## Instant (monotonic clock)

Use for **measuring elapsed time**. Never goes backward (unlike system clock).

```rust
use std::time::Instant;

let start = Instant::now();
// ... do work ...
let elapsed: Duration = start.elapsed();
println!("took {:?}", elapsed);
```

### Arithmetic

```rust
let t1 = Instant::now();
// ...
let t2 = Instant::now();
let between: Duration = t2 - t1;                        // same as t2.duration_since(t1)
let time_left = deadline.checked_duration_since(Instant::now()); // Option<Duration>
```

### Benchmark pattern

```rust
fn bench<F: FnOnce()>(label: &str, f: F) {
    let start = Instant::now();
    f();
    println!("{}: {:?}", label, start.elapsed());
}

bench("collect 100k", || {
    let _v: Vec<u64> = (0..100_000).collect();
});
```

---

## SystemTime (wall clock)

Use for **timestamps** — what time is it right now. Can go backward (NTP — Network Time Protocol — adjustments).

```rust
use std::time::{SystemTime, UNIX_EPOCH};

let now = SystemTime::now();
let since_epoch: Duration = now.duration_since(UNIX_EPOCH).unwrap();
let unix_ts: u64 = since_epoch.as_secs();   // Unix timestamp
```

### Arithmetic

```rust
let future = now + Duration::from_secs(3600);   // 1h from now
let past   = now - Duration::from_secs(3600);   // 1h ago

// duration_since returns Err if argument is later than self
let d: Result<Duration, _> = past.duration_since(now);  // Err — past < now
```

**Do NOT use `SystemTime` to measure elapsed time** — use `Instant` instead.

For proper datetime formatting (RFC3339, timezones, etc.) use the `chrono` or `time` crate.

---

## Thread sleep

```rust
use std::thread;

thread::sleep(Duration::from_millis(100));
thread::sleep(Duration::ZERO);  // yields the thread without busy-waiting
```
