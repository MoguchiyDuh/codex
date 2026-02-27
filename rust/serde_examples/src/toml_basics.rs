use serde::{Deserialize, Serialize};
use shared::{print_h2, print_h3};

// ------------------- Structs matching TOML structure -------------------

#[derive(Debug, Serialize, Deserialize)]
struct AppConfig {
    title: String,
    version: String,
    debug: bool,
    server: ServerConfig,
    database: DatabaseConfig,
    features: Vec<String>,
}

#[derive(Debug, Serialize, Deserialize)]
struct ServerConfig {
    host: String,
    port: u16,
    workers: u32,
}

#[derive(Debug, Serialize, Deserialize)]
struct DatabaseConfig {
    url: String,
    max_connections: u32,
    timeout_secs: u64,
}

// ------------------- Optional TOML sections -------------------

#[derive(Debug, Serialize, Deserialize)]
struct PartialConfig {
    title: String,
    debug: Option<bool>, // section may be absent
    log_level: Option<String>,
}

pub fn run() {
    print_h2!("TOML Serialization (toml crate)");

    print_h3!("Deserialize from TOML string");

    let toml_str: &str = r#"
        title   = "MyApp"
        version = "1.0.0"
        debug   = false
        features = ["auth", "logging", "metrics"]

        [server]
        host    = "0.0.0.0"
        port    = 8080
        workers = 4

        [database]
        url              = "postgres://localhost/mydb"
        max_connections  = 10
        timeout_secs     = 30
    "#;

    let config: AppConfig = toml::from_str(toml_str).unwrap();
    println!("title    = {}", config.title);
    println!("version  = {}", config.version);
    println!("debug    = {}", config.debug);
    println!("features = {:?}", config.features);
    println!("server   = {}:{}", config.server.host, config.server.port);
    println!("db url   = {}", config.database.url);

    print_h3!("Serialize to TOML string");

    let output: String = toml::to_string(&config).unwrap();
    println!("Serialized TOML:\n{}", output);

    let pretty: String = toml::to_string_pretty(&config).unwrap();
    println!("Pretty TOML:\n{}", pretty);

    print_h3!("toml::Value (dynamic)");

    let dynamic: toml::Value = toml::from_str(toml_str).unwrap();
    println!("dynamic[\"title\"]          = {:?}", dynamic["title"]);
    println!(
        "dynamic[\"server\"][\"port\"] = {:?}",
        dynamic["server"]["port"]
    );

    // Type-checked access
    let port: Option<i64> = dynamic["server"]["port"].as_integer();
    println!("server.port as_integer()  = {:?}", port);

    let features: Option<&Vec<toml::Value>> = dynamic["features"].as_array();
    println!(
        "features as_array len     = {:?}",
        features.map(|a| a.len())
    );

    print_h3!("Constructing toml::Value");

    use toml::value::Table;
    let mut table: Table = Table::new();
    table.insert(
        "name".to_string(),
        toml::Value::String("Ferris".to_string()),
    );
    table.insert("age".to_string(), toml::Value::Integer(8));
    table.insert("happy".to_string(), toml::Value::Boolean(true));

    let val: toml::Value = toml::Value::Table(table);
    println!(
        "Constructed table:\n{}",
        toml::to_string_pretty(&val).unwrap()
    );

    print_h3!("Partial/optional config");

    let minimal: &str = r#"title = "Minimal""#;
    let parsed: PartialConfig = toml::from_str(minimal).unwrap();
    println!("Partial config: {:?}", parsed);

    print_h3!("TOML vs JSON comparison");
    println!("TOML strengths: human-writable config files, comments, multiline strings");
    println!("JSON strengths: APIs, data interchange, universal tooling support");
    println!("TOML -> serde -> JSON: possible via serde_json, same derived types work for both");

    // Round-trip: TOML -> struct -> JSON
    let as_json: String = serde_json::to_string_pretty(&config).unwrap();
    println!("Same struct serialized as JSON:\n{}", &as_json[..200]); // first 200 chars
}
