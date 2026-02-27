---
tags:
  - rust
  - smart-pointers
  - zero-copy
source: smart_pointers/src/cow.rs
---

# Cow\<'a, B\>

`Cow<'a, B>` (Clone on Write) is an enum that holds **either a borrowed reference or an owned value**. It allocates only when mutation is actually required. It lives in `std::borrow`.

```rust
pub enum Cow<'a, B: ?Sized + 'a>
where B: ToOwned
{
    Borrowed(&'a B),
    Owned(<B as ToOwned>::Owned),
}
```

Common instantiations:

| Type | Borrowed | Owned |
|---|---|---|
| `Cow<'_, str>` | `&str` | `String` |
| `Cow<'_, [T]>` | `&[T]` | `Vec<T>` |
| `Cow<'_, Path>` | `&Path` | `PathBuf` |

## Core use case — conditional allocation

Return a borrow when no transformation is needed; allocate only when the data actually changes:

```rust
fn ensure_no_spaces(input: &str) -> Cow<'_, str> {
    if !input.contains(' ') {
        return Cow::Borrowed(input);          // no allocation
    }
    return Cow::Owned(input.replace(' ', "_")); // allocates only here
}
```

The caller uses the result as `&str` either way — `Cow<str>` derefs to `str`.

## Deref — transparent usage

`Cow<str>` implements `Deref<Target = str>`, so all `str` methods work without unwrapping:

```rust
let cow: Cow<str> = Cow::Borrowed("hello world");
println!("{}", cow.len());            // str method, no allocation
println!("{}", cow.to_uppercase());
```

## to_mut() — lazy clone

`to_mut()` upgrades `Borrowed` to `Owned` on first call (clones the data), then returns `&mut B::Owned` for subsequent calls without re-cloning:

```rust
let mut cow: Cow<str> = Cow::Borrowed("hello");

cow.to_mut().push_str(" world"); // clones once here
cow.to_mut().push('!');          // no re-clone — already owned
println!("{}", cow);             // "hello world!"
```

## Cow\<'\_, \[T\]\>

Works identically for slices:

```rust
fn ensure_sorted(data: &[i32]) -> Cow<'_, [i32]> {
    if data.windows(2).all(|w| w[0] <= w[1]) {
        return Cow::Borrowed(data);   // already sorted
    }
    let mut v = data.to_vec();
    v.sort();
    return Cow::Owned(v);
}
```

## Accepting both &str and String in an API

```rust
fn process_name(name: impl Into<Cow<'static, str>>) -> String {
    let cow = name.into();
    format!("Hello, {}!", cow)
}

process_name("Alice");               // &str — no allocation
process_name(String::from("Bob"));   // String — moved in, no copy
```

## Error message pattern

Static strings are borrowed (free), dynamic ones are owned (allocate only when needed):

```rust
fn describe_error(code: u32) -> Cow<'static, str> {
    match code {
        404 => Cow::Borrowed("not found"),
        500 => Cow::Borrowed("internal server error"),
        _   => Cow::Owned(format!("unknown error code {}", code)),
    }
}
```

## Size

`Cow<str>` is three words (24 bytes on 64-bit): a discriminant/tag, a pointer, and a length (or pointer + length + capacity when owned). A plain `String` is also three words; a `&str` is two. The discriminant is packed into spare bits so the actual size is the same as `String`.

## When to use

- A function that **sometimes** needs to mutate its input and **sometimes** can return it unchanged
- A function that returns either a static string literal or a dynamically-built `String`
- Avoiding unnecessary `String::from()` allocations in hot paths

**Don't** reach for `Cow` when the function always owns or always borrows — just use `String` or `&str` respectively. The indirection adds complexity.

## See also

- [[Box]] — always owned, no borrowing variant
- [[../basics/Ownership & Borrowing|Ownership & Borrowing]]
