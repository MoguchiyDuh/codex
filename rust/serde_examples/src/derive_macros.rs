use serde::{Deserialize, Serialize};
use shared::{print_h2, print_h3};

// ------------------- Basic derive -------------------

#[derive(Debug, Serialize, Deserialize)]
struct User {
    id: u32,
    name: String,
    email: String,
    active: bool,
}

// ------------------- Nested structs -------------------

#[derive(Debug, Serialize, Deserialize)]
struct Address {
    street: String,
    city: String,
    country: String,
}

#[derive(Debug, Serialize, Deserialize)]
struct Person {
    name: String,
    age: u8,
    address: Address, // nested
}

// ------------------- Optional fields -------------------

#[derive(Debug, Serialize, Deserialize)]
struct Config {
    host: String,
    port: u16,
    timeout: Option<u32>, // serializes as null or omits if using skip_serializing_if
    max_connections: Option<u32>,
}

// ------------------- serde field attributes -------------------

#[derive(Debug, Serialize, Deserialize)]
struct ApiResponse {
    #[serde(rename = "status_code")] // JSON key differs from field name — the Rust field is `status`
    status: u16,

    #[serde(rename = "response_body")]
    body: String,

    // skip_serializing_if takes a function path that accepts &T and returns bool.
    // "Option::is_none" means: omit the field from JSON when the value is None.
    // Without this, None serializes as `null`; with it, the key is absent entirely.
    #[serde(skip_serializing_if = "Option::is_none")]
    error_message: Option<String>,

    // #[serde(default)]: if the key is missing during deserialization, call Default::default().
    // For u32 that's 0. Without this, missing keys are an error.
    #[serde(default)]
    retries: u32,
}

// ------------------- skip fields -------------------

#[derive(Debug, Serialize, Deserialize)]
struct WithSecret {
    username: String,
    #[serde(skip)] // never serialize or deserialize this field
    password_hash: String,
    score: u32,
}

// ------------------- Enum serialization -------------------

#[derive(Debug, Serialize, Deserialize, PartialEq)]
enum Status {
    Active,
    Inactive,
    Banned { reason: String },
}

// ------------------- Enum tag styles -------------------

// #[serde(tag = "type")]: internally tagged — the discriminant field is inlined
// into the variant's object: { "type": "Move", "x": 1, "y": 2 }
// Only works for struct-like variants (not tuple variants).
#[derive(Debug, Serialize, Deserialize)]
#[serde(tag = "type")]
enum Command {
    Quit,
    Move { x: i32, y: i32 },
    Write { text: String },
}

// #[serde(tag = "t", content = "c")]: adjacently tagged: {"t": "Move", "c": {"x":1,"y":2}}
// #[serde(untagged)]: no discriminant — tries each variant in order; ambiguous if shapes overlap

// ------------------- Custom default values -------------------

fn default_port() -> u16 {
    return 8080;
}

#[derive(Debug, Serialize, Deserialize)]
struct ServerConfig {
    host: String,
    #[serde(default = "default_port")]
    port: u16,
}

pub fn run() {
    print_h2!("Derive Macros (Serialize / Deserialize)");

    print_h3!("Basic round-trip");

    let user: User = User {
        id: 1,
        name: String::from("Alice"),
        email: String::from("alice@example.com"),
        active: true,
    };
    let json: String = serde_json::to_string_pretty(&user).unwrap();
    println!("Serialized User:\n{}", json);

    let deserialized: User = serde_json::from_str(&json).unwrap();
    println!("Deserialized: {:?}", deserialized);

    print_h3!("Nested structs");

    let person: Person = Person {
        name: String::from("Bob"),
        age: 25,
        address: Address {
            street: String::from("123 Main St"),
            city: String::from("Rustville"),
            country: String::from("Ferrisland"),
        },
    };
    let json: String = serde_json::to_string_pretty(&person).unwrap();
    println!("Nested struct:\n{}", json);

    print_h3!("Optional fields");

    let cfg: Config = Config {
        host: String::from("localhost"),
        port: 5432,
        timeout: Some(30),
        max_connections: None,
    };
    println!(
        "Config with None:\n{}",
        serde_json::to_string_pretty(&cfg).unwrap()
    );

    // Deserialize with missing optional field
    let partial: &str = r#"{"host": "db.local", "port": 3306}"#;
    let parsed: Config = serde_json::from_str(partial).unwrap();
    println!("Parsed partial Config: {:?}", parsed);

    print_h3!("Field attributes");

    let resp: ApiResponse = ApiResponse {
        status: 200,
        body: String::from("OK"),
        error_message: None, // will be omitted due to skip_serializing_if
        retries: 0,
    };
    println!(
        "ApiResponse (no error):\n{}",
        serde_json::to_string_pretty(&resp).unwrap()
    );

    let err_resp: ApiResponse = ApiResponse {
        status: 500,
        body: String::from("Internal Error"),
        error_message: Some(String::from("database timeout")),
        retries: 3,
    };
    println!(
        "ApiResponse (with error):\n{}",
        serde_json::to_string_pretty(&err_resp).unwrap()
    );

    // Deserialize with rename - JSON uses "status_code", not "status"
    let raw: &str = r#"{"status_code": 404, "response_body": "Not Found"}"#;
    let parsed: ApiResponse = serde_json::from_str(raw).unwrap();
    println!("Parsed renamed fields: {:?}", parsed);

    print_h3!("Skip fields");

    let secret: WithSecret = WithSecret {
        username: String::from("kirill"),
        password_hash: String::from("bcrypt:$2b$..."),
        score: 9001,
    };
    let json: String = serde_json::to_string(&secret).unwrap();
    println!("WithSecret serialized (no hash): {}", json);

    // Deserializing: missing password_hash is fine (uses Default = "")
    let from_json: WithSecret = serde_json::from_str(&json).unwrap();
    println!("Deserialized: {:?}", from_json);

    print_h3!("Enum serialization");

    let statuses: Vec<Status> = vec![
        Status::Active,
        Status::Inactive,
        Status::Banned {
            reason: String::from("spam"),
        },
    ];
    for s in &statuses {
        println!("{:?} -> {}", s, serde_json::to_string(s).unwrap());
    }

    print_h3!("Internally tagged enum");

    let cmds: Vec<Command> = vec![
        Command::Quit,
        Command::Move { x: 10, y: 20 },
        Command::Write {
            text: String::from("hello"),
        },
    ];
    for c in &cmds {
        println!("{:?} -> {}", c, serde_json::to_string(c).unwrap());
    }

    print_h3!("Default field values");

    // JSON without "port" - uses default_port() = 8080
    let raw: &str = r#"{"host": "api.example.com"}"#;
    let server: ServerConfig = serde_json::from_str(raw).unwrap();
    println!("ServerConfig with default port: {:?}", server);
}
