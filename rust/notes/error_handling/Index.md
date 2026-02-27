---
tags:
  - rust
  - error-handling
  - index
source: error_handling/src/
---

# Error Handling — Index

| Module | Source File | Note |
|---|---|---|
| Error Trait | `src/error_trait.rs` | [[Error Trait]] |
| Custom Errors | `src/custom_errors.rs` | [[Custom Errors]] |
| Error Conversion | `src/error_conversion.rs` | [[Error Conversion]] |
| Propagation | `src/propagation.rs` | [[Propagation]] |
| Anyhow | `src/anyhow_example.rs` | [[Anyhow]] |
| Thiserror | `src/thiserror_example.rs` | [[Thiserror]] |

## Concept Map

```
std::error::Error (trait)
├── requires: Debug + Display
├── source() → error chain
└── See: [[Error Trait]]

Custom Error Types
├── enum (multiple variants, exhaustive match)
├── struct (single failure + rich context)
├── Manual: impl Display + impl Error
├── Automated: [[Thiserror]]
└── See: [[Custom Errors]]

Error Conversion
├── From<T> for E  →  enables ? across types
├── map_err(|e| ...)  →  one-off transforms
├── Box<dyn Error>  →  type erasure
├── downcast_ref::<T>()  →  recovery
└── See: [[Error Conversion]]

Propagation
├── ? operator = match + return Err(From::from(e))
├── Works on Result and Option
├── Closures: ? returns from closure, not outer fn
├── Iterator: collect into Result<Vec<T>> to short-circuit
└── See: [[Propagation]]

Application Error Handling (anyhow)
├── anyhow::Result<T> — trait object, no type definition needed
├── anyhow! / bail! / ensure! macros
├── .context() / .with_context() — layered messages
├── .chain() — iterate full error chain
└── See: [[Anyhow]]

Library Error Handling (thiserror)
├── #[derive(Error)] — generates Display + Error
├── #[from] — generates From impl + sets source()
├── #[source] — sets source() without From
├── #[error(transparent)] — delegates to wrapped error
└── See: [[Thiserror]]
```

## Decision Guide

- Defining errors for a **library**? Use [[Thiserror]].
- Writing **application** code (`main`, binary, CLI)? Use [[Anyhow]].
- Need callers to match on specific variants? Use [[Thiserror]] (typed enum).
- Just propagating up to the top? Use [[Anyhow]] (erased type, context chain).
- Multiple source error types in one fn? `From` impls or [[Thiserror]]'s `#[from]` — see [[Error Conversion]].
