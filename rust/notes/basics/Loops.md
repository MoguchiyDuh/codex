---
tags: [rust, basics, loops, iteration]
source: basics/src/loops.rs
---

# Loops

## `loop` (infinite)

Runs forever until `break`. Can return a value.

```rust
let mut n = 0;
let result: i32 = loop {
    n += 1;
    if n == 10 {
        break n * 2;    // loop evaluates to this value
    }
};
```

## `while`

```rust
while i < 5 { i += 1; }
```

## `while let`

Continues as long as pattern matches — common for draining collections:

```rust
while let Some(top) = stack.pop() {
    println!("{}", top);
}
```

## `for` with ranges

```rust
for i in 0..5  { }     // exclusive: 0,1,2,3,4
for i in 0..=5 { }     // inclusive: 0,1,2,3,4,5

for i in (0..5).rev()          { }  // reversed
for i in (0..10).step_by(2)    { }  // 0,2,4,6,8
```

## `for` over collections

```rust
for item in arr        { }   // arr moved into loop
for item in arr.iter() { }   // borrows arr, arr still usable after
for item in arr.iter_mut() { *item *= 10; }     // mutable borrow

for (idx, val) in arr.iter().enumerate() { }
```

## `break` and `continue`

```rust
for i in 0..10 {
    if i == 3 { continue; }     // skip 3
    if i == 7 { break; }        // stop at 7
}
```

## Labeled loops

Labels allow `break`/`continue` to target an outer loop:

```rust
'outer: for x in 0..3 {
    for y in 0..3 {
        if x == 1 && y == 1 { break 'outer; }
    }
}

'outer2: for x in 0..3 {
    for y in 0..3 {
        if y == 1 { continue 'outer2; }     // skip rest of inner, next x
        print!("({},{}) ", x, y);
    }
}
```

## Iterator adapters in loops

```rust
for i in (0..10).skip(2)            { }     // skip first 2
for i in (0..10).take(3)            { }     // first 3 only
for i in (0..10).skip(2).take(3)    { }     // chainable

// cycle repeats infinitely — must bound with take
for item in arr.iter().cycle().take(8) { }
```

## Functional style (collect)

```rust
let doubled: Vec<i32> = (1..6).map(|x| x * 2).collect();
let evens:   Vec<i32> = (0..10).filter(|x| x % 2 == 0).collect();
```

See [[../iterators/Index|iterators]] for the full iterator API.
