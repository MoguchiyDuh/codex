---
tags: [rust, basics, ownership, borrowing, memory]
source: basics/src/ownership.rs
---

# Ownership & Borrowing

Rust's memory model — no GC (Garbage Collector), no manual `malloc/free`. The compiler enforces rules at compile time.

## Ownership rules

1. Every value has exactly one owner.
2. When the owner goes out of scope, the value is dropped (memory freed).
3. Ownership can be **moved** or **borrowed** — never both at the same time.

## Move vs Copy

Types with heap data (String, Vec, Box…) **move** on assignment — the original is invalidated:

```rust
let s1: String = String::from("hello");
let s2: String = s1;        // s1 moved into s2
// println!("{}", s1);      // ERROR: borrow of moved value
```

Stack-only types implementing `Copy` are silently copied instead:

```rust
let x: i32 = 42;
let y: i32 = x;             // x copied, both remain valid
println!("{} {}", x, y);
```

`Copy` types: integers, floats, `bool`, `char`, tuples/arrays of Copy types.

Use `.clone()` for an explicit heap copy when you need two independent owners:

```rust
let s3 = s1.clone();        // separate allocation, both valid
```

## Borrowing

`&T` borrows a value without taking ownership. The original owner stays valid.

```rust
fn calculate_length(s: &String) -> usize {
    return s.len();
}                           // s not dropped — just a borrow

let s = String::from("hello");
let len = calculate_length(&s);
println!("{} is {} bytes", s, len);  // s still usable
```

### Borrow rules (enforced at compile time)

| Allowed | Count |
|---------|-------|
| Immutable `&T` refs | any number simultaneously |
| Mutable `&mut T` refs | exactly **one**, no other refs active |

```rust
let mut s = String::from("data");

let r1 = &s;
let r2 = &s;                // multiple immutable: OK
println!("{} {}", r1, r2);

// r1, r2 last used above — NLL (Non-Lexical Lifetimes) ends their borrows here

let r3 = &mut s;            // mutable: OK, no other borrows active
r3.push_str("!");
```

NLL (Non-Lexical Lifetimes): a borrow ends at its **last use**, not at the end of the enclosing block.

### Mutable borrow rules

```rust
let mut s = String::from("mutable");
let r = &mut s;
r.push_str(" modified");
// Can't read s while r is active:
// println!("{}", s);       // ERROR: cannot borrow as immutable
println!("{}", r);          // r's last use — borrow ends here
println!("{}", s);          // OK now
```

## Function ownership patterns

```rust
// Moves ownership in — caller loses it
fn takes_ownership(s: String) { /* s dropped at end */ }

// Borrows — caller keeps ownership
fn borrows(s: &String) -> usize { s.len() }

// Mutable borrow — modifies in place
fn mutate(s: &mut String) { s.push_str(" changed"); }

// Return ownership from inside
fn gives_ownership() -> String { String::from("yours") }
```

## Scope and drop

Values drop at `}`. Use `drop(val)` to free early (useful for locks, large allocations):

```rust
{
    let s = String::from("scoped");
    println!("{}", s);
}                           // dropped here

let big: Vec<i32> = vec![0; 1_000_000];
drop(big);                  // freed immediately
println!("memory freed");
```

## Dangling references

The compiler prevents returning references to dropped values:

```rust
// fn dangle() -> &String {
//     let s = String::from("...");
//     &s                   // ERROR: s dropped, reference dangling
// }

fn no_dangle() -> String {
    String::from("hello")   // return owned value, not a reference
}
```

## Slices

`&str` / `&[T]` are fat-pointer borrows into an existing allocation `(ptr, len)`:

```rust
let text = String::from("hello world");
let hello: &str = &text[0..5];
let world: &str = &text[6..11];
// text still owned and valid
```

Slice indices must land on UTF-8 character boundaries or it panics at runtime.

## Common patterns

```rust
// Need two independent copies → clone
let backup = original.clone();
consume(original);
println!("{}", backup);

// Don't need ownership → borrow, can reuse
process(&data);
process(&data);

// Thread ownership → Arc::clone (cheap ref-count bump)
// Interior mutability → RefCell / Mutex (see smart_pointers/)
```

## See also

- [[Lifetimes]] — explicit lifetime annotations when the compiler can't infer them
- [[../smart_pointers/Index|Smart Pointers]] — Rc/Arc for shared ownership, RefCell for interior mutability
