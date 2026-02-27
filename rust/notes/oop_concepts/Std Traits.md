---
tags:
  - rust
  - oop_concepts
  - std_traits
source: oop_concepts/src/std_traits.rs
---

# Std Traits

Standard library traits that most types interact with. These are not special syntax — they are ordinary [[Traits]] the compiler knows about for ergonomics (derive macros, operator dispatch, coercions).

## `Clone`

Explicit deep copy. Calling `.clone()` runs your implementation; nothing is implicit.

```rust
impl Clone for Buffer {
    fn clone(&self) -> Self {
        Buffer {
            data: self.data.clone(),
            label: self.label.clone(),
        }
    }
}
```

`#[derive(Clone)]` generates `self.field.clone()` for each field. All fields must also implement `Clone`.

## `Copy`

Bit-copy instead of move. After `let b = a`, both `a` and `b` are valid. No user-visible method call.

```rust
#[derive(Debug, Clone, Copy, PartialEq)]
struct Color { r: u8, g: u8, b: u8 }

let c1 = Color { r: 255, g: 128, b: 0 };
let c2 = c1;  // bit-copy — c1 is still valid
```

Constraints:
- `Copy` requires `Clone` (it is a subtrait).
- A type containing heap data (`String`, `Vec`) cannot implement `Copy` — heap ownership is not bitwise-copyable.
- All primitive types (`i32`, `f64`, `bool`, `char`, `&T`) are `Copy`.

## `Default`

Provides a "zero value" for a type. Used by struct update syntax and container initializations.

```rust
impl Default for ServerConfig {
    fn default() -> Self {
        ServerConfig {
            host: String::from("127.0.0.1"),
            port: 8080,
            timeout_ms: 5000,
            max_conn: 100,
            tls: false,
        }
    }
}

// Struct update syntax: specify overrides, default the rest
let prod = ServerConfig {
    host: String::from("0.0.0.0"),
    port: 443,
    tls: true,
    ..ServerConfig::default()
};
```

Standard defaults: `i32` → `0`, `f64` → `0.0`, `bool` → `false`, `String` → `""`, `Vec<T>` → `[]`, `Option<T>` → `None`.

## `Display` and `Debug`

Both live in `std::fmt`. They power the `{}` and `{:?}` format specifiers respectively.

```rust
impl fmt::Display for Temperature {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "{:.1}°C / {:.1}°F", self.celsius, self.celsius * 9.0 / 5.0 + 32.0)
    }
}

impl fmt::Debug for Temperature {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        f.debug_struct("Temperature")
            .field("celsius", &self.celsius)
            .finish()
    }
}
```

- `Display` — human-readable output, must be implemented manually.
- `Debug` — developer/diagnostic output, can be derived with `#[derive(Debug)]`.
- `{:#?}` — pretty-printed (multi-line) debug.

Other format traits in `std::fmt`: `Binary` (`{:b}`), `LowerHex` (`{:x}`), `UpperHex` (`{:X}`), `Octal` (`{:o}`).

```rust
impl fmt::Binary for Flags {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "{:08b}", self.0)
    }
}
```

## `PartialEq` and `Eq`

`PartialEq` provides `==` and `!=`. `Eq` is a marker supertrait adding the guarantee of *reflexivity* (`a == a` is always true).

```rust
impl PartialEq for Version {
    fn eq(&self, other: &Self) -> bool {
        self.major == other.major && self.minor == other.minor && self.patch == other.patch
    }
}

impl Eq for Version {}  // marker trait — no methods
```

`f64` implements `PartialEq` but *not* `Eq` because `NaN != NaN`. Types that require `Eq` (e.g. `HashMap` keys) will not accept `f64`.

`#[derive(PartialEq, Eq)]` works when all fields implement both.

## `PartialOrd` and `Ord`

`PartialOrd` provides `<`, `>`, `<=`, `>=` via `partial_cmp() -> Option<Ordering>`. `Ord` provides a *total* order via `cmp() -> Ordering` — no `Option`, always comparable.

```rust
impl PartialOrd for SemVer {
    fn partial_cmp(&self, other: &Self) -> Option<std::cmp::Ordering> {
        Some(self.cmp(other))  // canonical: delegate to Ord when Ord is implemented
    }
}

impl Ord for SemVer {
    fn cmp(&self, other: &Self) -> std::cmp::Ordering {
        self.major.cmp(&other.major)
            .then(self.minor.cmp(&other.minor))
            .then(self.patch.cmp(&other.patch))
    }
}
```

`Vec::sort()` requires `Ord`. `f64` only has `PartialOrd`, so you use `sort_by(|a, b| a.partial_cmp(b).unwrap())` instead.

Hierarchy: `Ord: Eq: PartialEq` and `Ord: PartialOrd: PartialEq`.

## `From` and `Into`

Lossless type conversions. Implementing `From<A> for B` automatically provides `Into<B> for A` — never implement both manually.

```rust
impl From<Km> for Miles {
    fn from(km: Km) -> Self { Miles(km.0 * 0.621371) }
}

let miles = Miles::from(Km(100.0));
let also_miles: Miles = Km(100.0).into();  // Into is free from the From impl
```

Multiple `From` impls on the same type are fine:

```rust
impl From<&str> for CsvLine { ... }
impl From<Vec<&str>> for CsvLine { ... }
```

Standard uses: lossless numeric widening (`i32 -> i64`), `&str -> String`, error conversions (`impl From<IoError> for MyError`).

## `Deref` and `DerefMut`

`Deref` makes `*value` follow a custom reference chain. Combined with *Deref coercion*, the compiler automatically inserts `deref()` calls to match expected types at function boundaries.

```rust
struct Newtype<T>(T);

impl<T> Deref for Newtype<T> {
    type Target = T;
    fn deref(&self) -> &T { &self.0 }
}

impl<T> DerefMut for Newtype<T> {
    fn deref_mut(&mut self) -> &mut T { &mut self.0 }
}

let mut boxed = Newtype(String::from("hello"));
println!("{}", boxed.len());  // Deref coercion: Newtype<String> -> String -> str
*boxed = String::from("world");  // DerefMut
```

Coercion chain example: `Box<String>` → `String` → `str`. Each step calls `deref()`.

## `Index` and `IndexMut`

Overloads the `[]` operator.

```rust
impl Index<(usize, usize)> for Matrix {
    type Output = f64;
    fn index(&self, (row, col): (usize, usize)) -> &f64 {
        &self.data[row][col]
    }
}

let val = mat[(1, 2)];  // calls Index::index
```

## Operator overloading — `Add` and friends

All arithmetic and bitwise operators live in `std::ops`:

```rust
impl Add for Vec2 {
    type Output = Vec2;
    fn add(self, rhs: Vec2) -> Vec2 {
        Vec2 { x: self.x + rhs.x, y: self.y + rhs.y }
    }
}

let sum = a + b;  // calls Add::add
```

Full list in `std::ops`: `Add`, `Sub`, `Mul`, `Div`, `Rem`, `Neg`, `Not`, `BitAnd`, `BitOr`, `BitXor`, `Shl`, `Shr`, `Index`, `IndexMut`, `Fn`, `FnMut`, `FnOnce`.

## Cross-references

- [[Traits]] — how traits are defined, dispatched, and composed.
- [[Generics]] — using these traits as bounds (`T: Clone + PartialOrd`).
- [[Structs]] / [[Enums]] — types that derive or manually implement these traits.
