use anyhow::{Context, Result, anyhow, bail, ensure};
use shared::{print_h2, print_h3};

// anyhow: ergonomic error handling for APPLICATIONS (not libraries)
// Provides Result<T> = Result<T, anyhow::Error> type alias with trait object error
// Key macros: anyhow!() creates errors, bail!() early returns, ensure!() validates conditions
// Context trait adds error context chains with .context() and .with_context()

pub fn run() {
    print_h2!("anyhow Crate");

    print_h3!("anyhow::Result type alias");
    // Result<T, anyhow::Error> is aliased as anyhow::Result<T>
    fn might_fail(succeed: bool) -> Result<String> {
        if succeed {
            return Ok(String::from("success"));
        }
        return Err(anyhow!("operation failed"));
    }

    match might_fail(true) {
        Ok(msg) => println!("Result: {}", msg),
        Err(e) => println!("Error: {}", e),
    }

    match might_fail(false) {
        Ok(msg) => println!("Result: {}", msg),
        Err(e) => println!("Error: {}", e),
    }

    print_h3!("anyhow! macro for ad-hoc errors");
    fn parse_config(valid: bool) -> Result<()> {
        if !valid {
            return Err(anyhow!("invalid configuration"));
        }
        return Ok(());
    }

    if let Err(e) = parse_config(false) {
        println!("Config error: {}", e);
    }

    // With formatted message
    fn check_version(version: u32, required: u32) -> Result<()> {
        if version < required {
            return Err(anyhow!(
                "version {} is too old, need at least {}",
                version,
                required
            ));
        }
        return Ok(());
    }

    if let Err(e) = check_version(1, 5) {
        println!("Version error: {}", e);
    }

    print_h3!("bail! macro for early return");
    fn validate_input(input: &str) -> Result<i32> {
        if input.is_empty() {
            bail!("input cannot be empty");
        }

        let num: i32 = input.parse()?;

        if num < 0 {
            bail!("number must be non-negative");
        }

        return Ok(num);
    }

    match validate_input("42") {
        Ok(n) => println!("Valid input: {}", n),
        Err(e) => println!("Validation error: {}", e),
    }

    match validate_input("") {
        Ok(n) => println!("Valid input: {}", n),
        Err(e) => println!("Validation error: {}", e),
    }

    match validate_input("-5") {
        Ok(n) => println!("Valid input: {}", n),
        Err(e) => println!("Validation error: {}", e),
    }

    print_h3!("ensure! macro (like assert!)");
    fn check_range(value: i32, min: i32, max: i32) -> Result<i32> {
        ensure!(value >= min, "value {} is below minimum {}", value, min);
        ensure!(value <= max, "value {} exceeds maximum {}", value, max);
        return Ok(value);
    }

    match check_range(50, 0, 100) {
        Ok(v) => println!("In range: {}", v),
        Err(e) => println!("Range error: {}", e),
    }

    match check_range(150, 0, 100) {
        Ok(v) => println!("In range: {}", v),
        Err(e) => println!("Range error: {}", e),
    }

    print_h3!("Context trait for adding context");
    fn read_file(path: &str) -> Result<String> {
        if path.is_empty() {
            bail!("empty path");
        }

        // Simulate file read error
        let result: std::result::Result<String, std::io::Error> = Err(std::io::Error::new(
            std::io::ErrorKind::NotFound,
            "file not found",
        ));

        // Add context to the error
        let content: String = result.context(format!("failed to read file '{}'", path))?;

        return Ok(content);
    }

    if let Err(e) = read_file("config.toml") {
        println!("File error: {}", e);
    }

    print_h3!("with_context for lazy context");
    fn process_record(id: u32) -> Result<String> {
        if id == 0 {
            bail!("invalid ID");
        }

        // with_context takes a closure (evaluated only on error)
        let data: String = "42"
            .parse::<i32>()
            .with_context(|| format!("failed to parse data for record {}", id))?
            .to_string();

        return Ok(data);
    }

    match process_record(123) {
        Ok(data) => println!("Processed: {}", data),
        Err(e) => println!("Process error: {}", e),
    }

    print_h3!("Automatic error conversion");
    fn parse_and_compute(input: &str) -> Result<i32> {
        let num: i32 = input.parse()?;
        return Ok(num * 2);
    }

    match parse_and_compute("21") {
        Ok(n) => println!("Computed: {}", n),
        Err(e) => println!("Compute error: {}", e),
    }

    match parse_and_compute("abc") {
        Ok(n) => println!("Computed: {}", n),
        Err(e) => println!("Compute error: {}", e),
    }

    print_h3!("Chaining context");
    fn load_config() -> Result<String> {
        return Err(anyhow!("file corrupted"));
    }

    fn initialize_system() -> Result<()> {
        let _config: String = load_config()
            .context("failed to load configuration")
            .context("system initialization failed")?;
        return Ok(());
    }

    if let Err(e) = initialize_system() {
        println!("Init error: {}", e);

        // Print full error chain
        for cause in e.chain() {
            println!("  caused by: {}", cause);
        }
    }

    print_h3!("Downcasting errors");
    #[derive(Debug)]
    struct CustomError {
        code: i32,
    }

    impl std::fmt::Display for CustomError {
        fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result {
            return write!(f, "custom error code {}", self.code);
        }
    }

    impl std::error::Error for CustomError {}

    fn create_custom_error() -> Result<()> {
        return Err(anyhow::Error::new(CustomError { code: 42 }));
    }

    if let Err(e) = create_custom_error() {
        println!("Error: {}", e);

        if let Some(custom) = e.downcast_ref::<CustomError>() {
            println!("Custom error code: {}", custom.code);
        }
    }

    print_h3!("Real-world example: nested operations");
    fn connect_database(url: &str) -> Result<String> {
        ensure!(!url.is_empty(), "database URL cannot be empty");
        // Simulate connection
        bail!("connection refused");
    }

    fn load_user(id: u32) -> Result<String> {
        let _conn: String = connect_database("localhost:5432")
            .context("failed to connect to database")
            .context(format!("cannot load user {}", id))?;

        return Ok(format!("User-{}", id));
    }

    fn get_user_profile(id: u32) -> Result<String> {
        let user: String = load_user(id).context("failed to retrieve user profile")?;
        return Ok(format!("Profile: {}", user));
    }

    if let Err(e) = get_user_profile(123) {
        println!("Profile error: {}", e);
        println!("\nFull error chain:");
        for (i, cause) in e.chain().enumerate() {
            println!("  {}: {}", i, cause);
        }
    }

    print_h3!("anyhow vs thiserror");
    // anyhow: for applications, propagating errors up to main
    // thiserror: for libraries, defining custom error types

    fn application_logic() -> Result<()> {
        // Use anyhow::Result in application code
        let _value: i32 = "not a number"
            .parse::<i32>()
            .context("failed to parse configuration value")?;

        return Ok(());
    }

    if let Err(e) = application_logic() {
        println!("Application error: {}", e);
    }
}
