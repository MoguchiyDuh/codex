---
tags:
  - rust
  - smart-pointers
  - memory
source: smart_pointers/src/box_pointer.rs
---

# Box\<T\>

`Box<T>` is the simplest smart pointer: it allocates a value on the heap and owns it. When the `Box` goes out of scope, the heap memory is freed via RAII (Resource Acquisition Is Initialization — tying resource lifetime to object lifetime). The pointer itself lives on the stack (one word), the data does not.

## Why use Box?

**1. Large data — avoid stack overflow**

```rust
let large: Box<[i32; 1_000_000]> = Box::new([0; 1_000_000]);
```

A `[i32; 1_000_000]` is 4 MB on the stack. `Box` moves it to the heap immediately.

**2. Transfer ownership without copying**

```rust
let data: Box<Vec<i32>> = Box::new(vec![1, 2, 3]);
let moved = data; // only the pointer is copied
```

**3. Trait objects — dynamic dispatch**

```rust
let shape: Box<dyn Drawable> = Box::new(Circle { radius: 5.0 });
shape.draw(); // vtable dispatch
```

`Box<dyn Trait>` is the standard way to erase a concrete type at runtime. The box is two words: a data pointer and a vtable pointer.

## Recursive types

Without `Box`, the compiler rejects recursive types because the size would be infinite. `Box` breaks the recursion by making the variant hold a known-size pointer:

```rust
enum List {
    Cons(i32, Box<List>),
    Nil,
}

let list = List::Cons(1, Box::new(List::Cons(2, Box::new(List::Nil))));
```

Same idea for binary trees: `Option<Box<TreeNode>>` as left/right children.

## Deref coercion

`Box<T>` implements `Deref<Target = T>`, so it auto-converts to `&T` when needed:

```rust
let s: Box<String> = Box::new(String::from("hello"));
takes_str(&s); // Box<String> -> &String -> &str (two coercions)
```

## Drop

`Box` implements `Drop`: when it leaves scope, the heap allocation is freed. No manual `free()` needed.

```rust
{
    let _temp: Box<i32> = Box::new(42);
} // freed here
```

## Box::leak — intentional `'static` reference

```rust
let leaked: &'static mut i32 = Box::leak(Box::new(100));
```

Consumes the `Box` without running `Drop`, producing a `&'static` reference. The memory is never freed. Use sparingly — mainly for:
- Initializing globals from runtime values
- Passing heap data across an FFI (Foreign Function Interface) boundary where the C side manages lifetime

## Box::into_raw / Box::from_raw

```rust
let raw: *mut i32 = Box::into_raw(Box::new(50)); // Box forgotten, no drop
unsafe {
    let reconstructed: Box<i32> = Box::from_raw(raw); // drop runs here
}
```

`into_raw` transfers ownership to a raw pointer. `from_raw` reclaims it. Calling `from_raw` twice on the same pointer is a double-free — UB (Undefined Behavior). This is primarily an FFI tool.

## Dynamically-Sized Types (DST)

`Box` can hold unsized types:

```rust
let slice: Box<[i32]>  = Box::new([1, 2, 3, 4, 5]);
let s: Box<str>        = String::from("boxed str").into_boxed_str();
```

## Moving out of Box

Dereferencing a `Box` and assigning moves the inner value out, consuming the box:

```rust
let boxed: Box<String> = Box::new(String::from("owned"));
let owned: String = *boxed; // Box consumed
```

## Pattern matching

```rust
let maybe: Option<Box<i32>> = Some(Box::new(99));
match maybe {
    Some(val) => println!("{}", val), // auto-deref
    None => {}
}
```

## When to reach for Box

| Situation | Use |
|---|---|
| Large struct on heap | `Box<T>` |
| Recursive / self-referential type | `Box<T>` |
| `dyn Trait` heap allocation | `Box<dyn Trait>` |
| Boxed closure | `Box<dyn Fn(…) -> …>` |
| FFI ownership handoff | `Box::into_raw` / `Box::from_raw` |

## See also

- [[Rc]] — multiple ownership (single-threaded)
- [[Arc]] — multiple ownership (multi-threaded)
- [[Patterns]] — `Box<dyn Trait>` in context
- [[../basics/Ownership & Borrowing|Ownership & Borrowing]]
