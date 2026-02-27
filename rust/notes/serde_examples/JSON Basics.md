---
tags:
  - rust
  - serde
  - json
source: serde_examples/src/json_basics.rs
---

# JSON Basics

JSON (JavaScript Object Notation) is a text-based data interchange format. The `serde_json` crate provides both dynamic and typed interfaces for working with it in Rust.

See [[Derive Macros]] for how to use typed structs instead of dynamic values, and [[Custom Serde]] for advanced control over the serialization (ser) / deserialization (de) process.

---

## serde_json::Value — dynamic JSON

`serde_json::Value` is an enum that represents any valid JSON node. Use it when the shape of the data is unknown at compile time.

```rust
let v: serde_json::Value = serde_json::from_str(json_str).unwrap();
```

Variant mapping:

| JSON type | Rust variant           |
|-----------|------------------------|
| null      | `Value::Null`          |
| boolean   | `Value::Bool(bool)`    |
| number    | `Value::Number(...)`   |
| string    | `Value::String(String)`|
| array     | `Value::Array(Vec<Value>)` |
| object    | `Value::Object(Map<String, Value>)` |

### Indexing

```rust
v["name"]          // -> Value::String("Alice")
v["scores"][1]     // -> Value::Number(87)
v["missing"]       // -> Value::Null  (no panic, unlike HashMap)
```

Missing keys return `Value::Null` rather than panicking. Both missing keys and explicit `null` values satisfy `.is_null()`.

### Type-safe extraction

```rust
let age:  Option<u64>  = v["age"].as_u64();
let name: Option<&str> = v["name"].as_str();
```

The `as_*` family returns `Option<T>` — `None` if the variant doesn't match.

---

## Constructing JSON with the `json!` macro

`serde_json::json!` builds a `Value` from a JSON-like literal at compile time:

```rust
let val = serde_json::json!({
    "product": "Ferris",
    "version": 4,
    "tags": ["rust", "crab"],
    "meta": { "stable": true }
});
```

---

## Serialization

```rust
// Compact — single line
let compact: String = serde_json::to_string(&val).unwrap();

// Pretty — indented
let pretty: String = serde_json::to_string_pretty(&val).unwrap();
```

Both return `Result<String, serde_json::Error>`. Use `.unwrap()` only in examples; propagate errors in production.

---

## Merging objects

`Value::Object` wraps a `serde_json::Map<String, Value>` (a `BTreeMap`-like type). Merge by iterating the extension map and inserting into the base:

```rust
let mut base = serde_json::json!({ "a": 1, "b": 2 });
if let (Value::Object(bmap), Value::Object(emap)) =
    (&mut base, serde_json::json!({ "b": 99, "c": 3 }))
{
    for (k, v) in emap { bmap.insert(k, v); }
}
// base = { "a": 1, "b": 99, "c": 3 }
```

---

## When to use `Value` vs. typed structs

| Scenario | Recommendation |
|----------|----------------|
| Known schema | Typed struct + `#[derive(Serialize, Deserialize)]` |
| Dynamic / unknown keys | `serde_json::Value` |
| Config / protocol work | Typed structs; avoids runtime type checks |

`Value` is convenient for exploration but shifts type errors from compile time to runtime.
