---
tags:
  - rust
  - serde
  - derive
source: serde_examples/src/derive_macros.rs
---

# Derive Macros

`#[derive(Serialize, Deserialize)]` is the primary entry point to serde. It generates serialization (ser) / deserialization (de) implementations at compile time from the struct or enum definition, with zero runtime cost. Field-level attributes fine-tune the generated code.

See [[JSON Basics]] and [[TOML Basics]] for format-specific usage, and [[Custom Serde]] for cases where derive isn't sufficient.

---

## Basic round-trip

```rust
#[derive(Debug, Serialize, Deserialize)]
struct User {
    id:     u32,
    name:   String,
    email:  String,
    active: bool,
}

let json = serde_json::to_string_pretty(&user).unwrap();
let back: User = serde_json::from_str(&json).unwrap();
```

Field names map 1:1 to JSON keys by default. All field types must themselves implement `Serialize`/`Deserialize`.

---

## Nested structs

Nesting is transparent — the inner struct just needs the same derives:

```rust
#[derive(Debug, Serialize, Deserialize)]
struct Person {
    name:    String,
    age:     u8,
    address: Address,  // nested; Address also derives Serialize/Deserialize
}
```

---

## Optional fields

`Option<T>` fields serialize as `null` when `None`, and accept missing keys during de:

```rust
#[derive(Debug, Serialize, Deserialize)]
struct Config {
    host:            String,
    port:            u16,
    timeout:         Option<u32>,  // None -> null in JSON
    max_connections: Option<u32>,
}

// Missing keys in JSON -> None (not an error)
let parsed: Config = serde_json::from_str(r#"{"host":"db","port":5432}"#).unwrap();
```

---

## Field attributes

Attributes go on individual fields inside the struct.

### `#[serde(rename = "...")]`

Maps a Rust field name to a different JSON/TOML key:

```rust
#[serde(rename = "status_code")]
status: u16,  // serializes/deserializes as "status_code"
```

### `#[serde(skip_serializing_if = "...")]`

Takes a function path `fn(&T) -> bool`. If it returns `true`, the field is omitted from output entirely (key absent, not `null`):

```rust
#[serde(skip_serializing_if = "Option::is_none")]
error_message: Option<String>,
```

### `#[serde(default)]`

If the key is missing during de, call `Default::default()` instead of erroring. For `u32` that's `0`, for `String` it's `""`, etc.:

```rust
#[serde(default)]
retries: u32,
```

### `#[serde(default = "fn_name")]`

Like `#[serde(default)]` but calls a named function:

```rust
fn default_port() -> u16 { return 8080; }

#[serde(default = "default_port")]
port: u16,
```

### `#[serde(skip)]`

Excludes a field from both ser and de. On de, the field is populated via `Default::default()`:

```rust
#[serde(skip)]
password_hash: String,  // never appears in JSON
```

---

## Enum serialization

By default serde uses an **externally tagged** representation:

```rust
#[derive(Serialize, Deserialize)]
enum Status {
    Active,                    // -> "Active"
    Inactive,                  // -> "Inactive"
    Banned { reason: String }, // -> {"Banned":{"reason":"..."}}
}
```

### Internally tagged: `#[serde(tag = "type")]`

The discriminant is inlined as a field inside the variant's object. Only works for struct-like variants (not tuple variants):

```rust
#[serde(tag = "type")]
enum Command {
    Quit,                      // -> {"type":"Quit"}
    Move { x: i32, y: i32 },  // -> {"type":"Move","x":1,"y":2}
    Write { text: String },    // -> {"type":"Write","text":"hello"}
}
```

### Other tagging styles (not in examples but worth knowing)

| Attribute | Format |
|-----------|--------|
| `#[serde(tag="t", content="c")]` | `{"t":"Move","c":{"x":1,"y":2}}` — adjacently tagged |
| `#[serde(untagged)]` | `{"x":1,"y":2}` — no discriminant; variants tried in order |

---

## Summary of common attributes

| Attribute | Effect |
|-----------|--------|
| `rename = "key"` | Different key name in output |
| `skip_serializing_if = "fn"` | Conditionally omit field |
| `default` | Use `Default::default()` for missing keys |
| `default = "fn"` | Use named function for missing keys |
| `skip` | Exclude from ser and de entirely |
| `tag = "field"` | Internally tag enum variants |
