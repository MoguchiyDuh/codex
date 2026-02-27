use shared::{print_h2, print_h3};

pub fn run() {
    print_h2!("JSON Basics (serde_json)");

    print_h3!("Dynamic JSON with Value");

    // serde_json::Value is a dynamic JSON tree (enum); use typed structs + derive for production
    // Parse a JSON string into a dynamic Value tree
    let json_str: &str = r#"
        {
            "name": "Alice",
            "age": 30,
            "active": true,
            "scores": [95, 87, 92],
            "address": {
                "city": "Rustville",
                "zip": "12345"
            }
        }
    "#;

    let v: serde_json::Value = serde_json::from_str(json_str).unwrap();

    println!("v[\"name\"]              = {}", v["name"]);
    println!("v[\"age\"]               = {}", v["age"]);
    println!("v[\"active\"]            = {}", v["active"]);
    println!("v[\"scores\"][1]         = {}", v["scores"][1]);
    println!("v[\"address\"][\"city\"]    = {}", v["address"]["city"]);
    // Indexing a missing key returns Value::Null rather than panicking (unlike HashMap indexing)
    println!("v[\"missing\"]           = {}", v["missing"]); // Value::Null

    // Type-checking and extraction
    let age: Option<u64> = v["age"].as_u64();
    println!("v[\"age\"].as_u64()      = {:?}", age);
    let name: Option<&str> = v["name"].as_str();
    println!("v[\"name\"].as_str()     = {:?}", name);

    print_h3!("Constructing JSON with json! macro");

    let constructed: serde_json::Value = serde_json::json!({
        "product": "Ferris",
        "version": 4,
        "tags": ["rust", "crab", "mascot"],
        "meta": {
            "stable": true,
            "year": 2015
        }
    });
    println!("json!() macro result = {}", constructed);

    print_h3!("Serializing to string");

    let compact: String = serde_json::to_string(&constructed).unwrap();
    println!("to_string (compact):\n{}", compact);

    let pretty: String = serde_json::to_string_pretty(&constructed).unwrap();
    println!("to_string_pretty:\n{}", pretty);

    print_h3!("Serialize/deserialize numbers");

    let nums: serde_json::Value = serde_json::json!({
        "integer": 42,
        "float": 3.14,
        "negative": -100,
        "large": 9999999999_u64
    });
    println!(
        "Numbers JSON = {}",
        serde_json::to_string_pretty(&nums).unwrap()
    );

    print_h3!("Arrays");

    let arr: serde_json::Value = serde_json::json!([1, "two", true, null, [3, 4]]);
    println!("Array JSON = {}", arr);

    if let serde_json::Value::Array(items) = &arr {
        println!("Array len = {}", items.len());
        for (i, item) in items.iter().enumerate() {
            println!("  [{}] = {} (type: {})", i, item, item_type(item));
        }
    }

    print_h3!("Merging JSON objects");

    let mut base: serde_json::Value = serde_json::json!({ "a": 1, "b": 2 });
    if let (serde_json::Value::Object(bmap), serde_json::Value::Object(emap)) =
        (&mut base, serde_json::json!({ "b": 99, "c": 3 }))
    {
        for (k, v) in emap {
            bmap.insert(k, v);
        }
    }
    println!("Merged = {}", base);

    print_h3!("Null handling");

    let with_null: serde_json::Value = serde_json::json!({
        "present": "value",
        "absent": null
    });
    println!("is_null(present) = {}", with_null["present"].is_null());
    println!("is_null(absent)  = {}", with_null["absent"].is_null());
    println!(
        "is_null(missing) = {}",
        with_null["totally_missing"].is_null()
    ); // also null
}

fn item_type(v: &serde_json::Value) -> &'static str {
    match v {
        serde_json::Value::Null => "null",
        serde_json::Value::Bool(_) => "bool",
        serde_json::Value::Number(_) => "number",
        serde_json::Value::String(_) => "string",
        serde_json::Value::Array(_) => "array",
        serde_json::Value::Object(_) => "object",
    }
}
