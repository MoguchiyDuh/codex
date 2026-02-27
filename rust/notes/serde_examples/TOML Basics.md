---
tags:
  - rust
  - serde
  - toml
source: serde_examples/src/toml_basics.rs
---

# TOML Basics

TOML (Tom's Obvious Minimal Language) is a configuration file format designed for human readability. The `toml` crate integrates with serde, so the same `#[derive(Serialize, Deserialize)]` structs used for JSON work for TOML without modification.

See [[Derive Macros]] for how derived traits work, and [[JSON Basics]] for the parallel `serde_json` patterns.

---

## Typed deserialization (de)

Define structs that mirror the TOML structure, derive the traits, call `toml::from_str`:

```rust
#[derive(Debug, Serialize, Deserialize)]
struct AppConfig {
    title:    String,
    version:  String,
    debug:    bool,
    server:   ServerConfig,
    database: DatabaseConfig,
    features: Vec<String>,
}

let config: AppConfig = toml::from_str(toml_str).unwrap();
```

TOML tables (`[server]`) map directly to nested structs. Arrays map to `Vec<T>`.

### Optional / absent sections

Wrap fields in `Option<T>` to handle keys that may not appear in the file:

```rust
#[derive(Debug, Serialize, Deserialize)]
struct PartialConfig {
    title:     String,
    debug:     Option<bool>,    // absent -> None
    log_level: Option<String>,
}

let parsed: PartialConfig = toml::from_str(r#"title = "Minimal""#).unwrap();
// parsed.debug == None
```

---

## Typed serialization (ser)

```rust
let output: String       = toml::to_string(&config).unwrap();
let pretty: String       = toml::to_string_pretty(&config).unwrap();
```

`to_string_pretty` produces canonical TOML with section headers and sorted keys.

---

## Dynamic `toml::Value`

When the schema is unknown, parse into `toml::Value` — the TOML counterpart of `serde_json::Value`:

```rust
let dynamic: toml::Value = toml::from_str(toml_str).unwrap();

// Index-based access
println!("{:?}", dynamic["title"]);
println!("{:?}", dynamic["server"]["port"]);

// Type-safe extraction
let port: Option<i64>            = dynamic["server"]["port"].as_integer();
let features: Option<&Vec<toml::Value>> = dynamic["features"].as_array();
```

Note that TOML integers deserialize as `i64`, not `u64`.

### Constructing `toml::Value` programmatically

```rust
use toml::value::Table;

let mut table = Table::new();
table.insert("name".to_string(), toml::Value::String("Ferris".to_string()));
table.insert("age".to_string(),  toml::Value::Integer(8));

let val = toml::Value::Table(table);
println!("{}", toml::to_string_pretty(&val).unwrap());
```

---

## TOML vs JSON

| Aspect | TOML | JSON |
|--------|------|------|
| Primary use | Config files | Data interchange / APIs |
| Comments | Supported (`#`) | Not supported |
| Multiline strings | Yes | No (requires `\n`) |
| Tooling support | Cargo, many CLIs | Universal |
| Serde compatibility | Same derived structs work | Same derived structs work |

Because both formats go through serde's data model, the same struct can round-trip through either:

```rust
let config: AppConfig = toml::from_str(toml_str).unwrap();
let as_json = serde_json::to_string_pretty(&config).unwrap(); // works
```
