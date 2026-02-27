use serde::de::{self, Visitor};
use serde::{Deserialize, Deserializer, Serialize, Serializer};
use shared::{print_h2, print_h3};
use std::fmt;

// ------------------- Custom Serialize -------------------

// Serialize a Duration as fractional seconds (f64) instead of {secs, nanos}
#[derive(Debug, PartialEq)]
struct Duration {
    secs: u64,
    nanos: u32,
}

impl Duration {
    fn from_secs(s: f64) -> Self {
        let secs: u64 = s as u64;
        let nanos: u32 = ((s - secs as f64) * 1_000_000_000.0) as u32;
        return Duration { secs, nanos };
    }

    fn as_secs_f64(&self) -> f64 {
        return self.secs as f64 + self.nanos as f64 / 1_000_000_000.0;
    }
}

impl Serialize for Duration {
    fn serialize<S: Serializer>(&self, s: S) -> Result<S::Ok, S::Error> {
        return s.serialize_f64(self.as_secs_f64());
    }
}

// ------------------- Custom Deserialize -------------------

struct DurationVisitor;

// The Visitor pattern separates the serde data model from the Rust type.
// Implement visit_* for each JSON type you want to accept.
// The 'de lifetime bounds the deserialized data — it can borrow from the input if needed.
impl<'de> Visitor<'de> for DurationVisitor {
    type Value = Duration;

    // expecting() is called when the type doesn't match — appears in error messages.
    fn expecting(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        return f.write_str("a duration in fractional seconds as f64");
    }

    fn visit_f64<E: de::Error>(self, v: f64) -> Result<Duration, E> {
        return Ok(Duration::from_secs(v));
    }

    // Implementing visit_i64 and visit_u64 allows JSON integers to deserialize too.
    // Without these, `2` (integer) would fail while `2.0` (float) would succeed.
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
    }
}

// ------------------- serialize_with / deserialize_with -------------------
// Use custom logic for individual fields without implementing full traits

fn serialize_uppercase<S: Serializer>(s: &str, ser: S) -> Result<S::Ok, S::Error> {
    return ser.serialize_str(&s.to_uppercase());
}

fn deserialize_trimmed<'de, D: Deserializer<'de>>(d: D) -> Result<String, D::Error> {
    let s: String = String::deserialize(d)?;
    return Ok(s.trim().to_string());
}

#[derive(Debug, Serialize, Deserialize)]
struct Tag {
    #[serde(serialize_with = "serialize_uppercase")]
    #[serde(deserialize_with = "deserialize_trimmed")]
    name: String,
    count: u32,
}

// ------------------- from / into for transparent conversion -------------------

// Serialize Point as [x, y] array instead of {"x":..., "y":...}
#[derive(Debug, PartialEq)]
struct Point {
    x: f64,
    y: f64,
}

impl Serialize for Point {
    fn serialize<S: Serializer>(&self, s: S) -> Result<S::Ok, S::Error> {
        use serde::ser::SerializeSeq;
        let mut seq = s.serialize_seq(Some(2))?;
        seq.serialize_element(&self.x)?;
        seq.serialize_element(&self.y)?;
        return seq.end();
    }
}

struct PointVisitor;

impl<'de> Visitor<'de> for PointVisitor {
    type Value = Point;

    fn expecting(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        return f.write_str("a [x, y] array");
    }

    fn visit_seq<A: de::SeqAccess<'de>>(self, mut seq: A) -> Result<Point, A::Error> {
        let x: f64 = seq
            .next_element()?
            .ok_or_else(|| de::Error::invalid_length(0, &self))?;
        let y: f64 = seq
            .next_element()?
            .ok_or_else(|| de::Error::invalid_length(1, &self))?;
        return Ok(Point { x, y });
    }
}

impl<'de> Deserialize<'de> for Point {
    fn deserialize<D: Deserializer<'de>>(d: D) -> Result<Point, D::Error> {
        return d.deserialize_seq(PointVisitor);
    }
}

pub fn run() {
    print_h2!("Custom Serialize / Deserialize");

    print_h3!("Custom Duration");

    let d: Duration = Duration {
        secs: 1,
        nanos: 500_000_000,
    };
    let json: String = serde_json::to_string(&d).unwrap();
    println!("Duration {{ 1s, 500ms }} -> {}", json); // 1.5

    let back: Duration = serde_json::from_str(&json).unwrap();
    println!("Parsed back: secs={}, nanos={}", back.secs, back.nanos);

    let from_int: Duration = serde_json::from_str("2").unwrap();
    println!("from_str(\"2\") = secs={}", from_int.secs);

    print_h3!("serialize_with / deserialize_with");

    let tag: Tag = Tag {
        name: String::from("rust"),
        count: 42,
    };
    let json: String = serde_json::to_string(&tag).unwrap();
    println!("Tag {{ name: \"rust\" }} -> {}", json); // name uppercased

    let raw: &str = r#"{"name": "  ferris  ", "count": 1}"#;
    let parsed: Tag = serde_json::from_str(raw).unwrap();
    println!("Tag deserialized (trimmed): {:?}", parsed);

    print_h3!("Point as array");

    let p: Point = Point { x: 3.0, y: 4.0 };
    let json: String = serde_json::to_string(&p).unwrap();
    println!("Point {{ 3.0, 4.0 }} -> {}", json); // [3.0,4.0]

    let back: Point = serde_json::from_str(&json).unwrap();
    println!("Parsed back: {:?}", back);
    assert_eq!(p, back);

    print_h3!("Error messages from bad data");

    let bad_point: Result<Point, _> = serde_json::from_str("[1.0]"); // missing y
    println!("from_str(\"[1.0]\")   = {:?}", bad_point);

    let bad_duration: Result<Duration, _> = serde_json::from_str("\"not a number\"");
    println!("from_str(\"not a number\") = {:?}", bad_duration);
}
