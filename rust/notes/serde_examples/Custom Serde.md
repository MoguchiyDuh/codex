---
tags:
  - rust
  - serde
  - custom
source: serde_examples/src/custom_serde.rs
---

# Custom Serde

When `#[derive(Serialize, Deserialize)]` doesn't produce the wire format you need, implement the traits manually. The two main tools are: implementing `Serialize`/`Deserialize` directly, or using `serialize_with`/`deserialize_with` for per-field overrides.

See [[Derive Macros]] for the derive-based baseline, and [[JSON Basics]] for the format layer.

---

## Implementing `Serialize`

`Serialize` has one method: `serialize<S: Serializer>`. Call methods on `S` to emit a value in serde's abstract data model — the serializer translates that to the actual format (JSON, TOML, etc.).

**Example: `Duration` as a fractional `f64` instead of `{secs, nanos}`**

```rust
impl Serialize for Duration {
    fn serialize<S: Serializer>(&self, s: S) -> Result<S::Ok, S::Error> {
        return s.serialize_f64(self.as_secs_f64());
        // -> 1.5  (not {"secs":1,"nanos":500000000})
    }
}
```

**Example: `Point` as a JSON array `[x, y]` instead of `{"x":...,"y":...}`**

```rust
impl Serialize for Point {
    fn serialize<S: Serializer>(&self, s: S) -> Result<S::Ok, S::Error> {
        use serde::ser::SerializeSeq;
        let mut seq = s.serialize_seq(Some(2))?;
        seq.serialize_element(&self.x)?;
        seq.serialize_element(&self.y)?;
        return seq.end();
    }
}
```

---

## Implementing `Deserialize` — the Visitor pattern

Deserialization (de) uses the **Visitor** pattern. You define a `Visitor` struct and implement `visit_*` methods for each JSON type you want to accept. The deserializer calls the correct method based on what it finds in the input.

### Structure

1. Create a zero-size visitor struct.
2. Implement `Visitor<'de>` — set `type Value = YourType` and implement `expecting` plus the relevant `visit_*` methods.
3. Implement `Deserialize<'de>` — call the deserializer with your visitor.

```rust
struct DurationVisitor;

impl<'de> Visitor<'de> for DurationVisitor {
    type Value = Duration;

    // Called when the actual type doesn't match — shown in error messages
    fn expecting(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        return f.write_str("a duration in fractional seconds as f64");
    }

    fn visit_f64<E: de::Error>(self, v: f64) -> Result<Duration, E> {
        return Ok(Duration::from_secs(v));
    }

    // Accept integer literals too (JSON `2` is i64/u64, not f64)
    fn visit_i64<E: de::Error>(self, v: i64) -> Result<Duration, E> {
        return Ok(Duration::from_secs(v as f64));
    }

    fn visit_u64<E: de::Error>(self, v: u64) -> Result<Duration, E> {
        return Ok(Duration::from_secs(v as f64));
    }
}

impl<'de> Deserialize<'de> for Duration {
    fn deserialize<D: Deserializer<'de>>(d: D) -> Result<Duration, D::Error> {
        return d.deserialize_f64(DurationVisitor);
        // hint to the deserializer that we expect a float;
        // the deserializer may still call other visit_* if needed
    }
}
```

The `'de` lifetime bounds the deserialized data — the visitor can borrow from the input buffer if needed (e.g., returning `&str` instead of `String`).

### Visitor for a sequence (`Point` as `[x, y]`)

```rust
impl<'de> Visitor<'de> for PointVisitor {
    type Value = Point;

    fn expecting(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        return f.write_str("a [x, y] array");
    }

    fn visit_seq<A: de::SeqAccess<'de>>(self, mut seq: A) -> Result<Point, A::Error> {
        let x = seq.next_element()?.ok_or_else(|| de::Error::invalid_length(0, &self))?;
        let y = seq.next_element()?.ok_or_else(|| de::Error::invalid_length(1, &self))?;
        return Ok(Point { x, y });
    }
}
```

`de::Error::invalid_length` produces a well-formatted error with the expected length from `expecting`.

---

## Per-field overrides: `serialize_with` / `deserialize_with`

When you only need custom logic for one field — without implementing full traits on the type — use these attributes. The functions must match a specific signature.

```rust
fn serialize_uppercase<S: Serializer>(s: &str, ser: S) -> Result<S::Ok, S::Error> {
    return ser.serialize_str(&s.to_uppercase());
}

fn deserialize_trimmed<'de, D: Deserializer<'de>>(d: D) -> Result<String, D::Error> {
    let s = String::deserialize(d)?;
    return Ok(s.trim().to_string());
}

#[derive(Debug, Serialize, Deserialize)]
struct Tag {
    #[serde(serialize_with = "serialize_uppercase")]
    #[serde(deserialize_with = "deserialize_trimmed")]
    name: String,
    count: u32,
}
```

`serialize_with` and `deserialize_with` can be combined on the same field. They can also be used independently.

---

## Error messages from bad data

The `expecting` method on the `Visitor` feeds directly into serde's error output:

```rust
let bad: Result<Point, _> = serde_json::from_str("[1.0]"); // missing y
// Err: invalid length 1, expected a [x, y] array

let bad: Result<Duration, _> = serde_json::from_str("\"not a number\"");
// Err: invalid type: string "not a number", expected a duration in fractional seconds as f64
```

Write `expecting` strings as noun phrases: "a duration in fractional seconds", "a [x, y] array".

---

## Decision guide

| Situation | Approach |
|-----------|----------|
| Standard struct/enum, default format | `#[derive(Serialize, Deserialize)]` |
| One field needs custom logic | `serialize_with` / `deserialize_with` |
| Whole type needs different wire format | Implement `Serialize` + `Deserialize` manually |
| Accept multiple JSON types for one Rust type | Implement multiple `visit_*` in the `Visitor` |
