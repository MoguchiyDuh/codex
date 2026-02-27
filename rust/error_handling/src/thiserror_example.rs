use shared::{print_h2, print_h3};
use std::num::ParseIntError;
use thiserror::Error;

// thiserror: derive macro for defining custom error types in LIBRARIES
// Automatically implements Display and Error trait with #[derive(Error)]
// Use #[error("message")] for Display formatting, #[from] for automatic From impls
// Best for library crates that need strongly-typed, structured error enums
// Provides compile-time guarantees and type safety for error handling

pub fn run() {
    print_h2!("thiserror Crate");

    print_h3!("Basic thiserror derive");
    // thiserror automatically implements Display and Error trait
    #[derive(Error, Debug)]
    enum DataError {
        #[error("data not found")]
        NotFound,

        #[error("invalid data format")]
        InvalidFormat,

        #[error("data too large: {size} bytes (max {max})")]
        TooLarge { size: usize, max: usize },

        // {0} in the format string refers to the first unnamed field of the variant
        #[error("IO error: {0}")]
        Io(String),
    }

    fn load_data(id: u32) -> Result<String, DataError> {
        if id == 0 {
            return Err(DataError::NotFound);
        }
        if id > 1000 {
            return Err(DataError::TooLarge {
                size: id as usize,
                max: 1000,
            });
        }
        return Ok(format!("Data-{}", id));
    }

    match load_data(42) {
        Ok(data) => println!("Loaded: {}", data),
        Err(e) => println!("Error: {}", e),
    }

    match load_data(0) {
        Ok(data) => println!("Loaded: {}", data),
        Err(e) => println!("Error: {}", e),
    }

    match load_data(2000) {
        Ok(data) => println!("Loaded: {}", data),
        Err(e) => println!("Error: {}", e),
    }

    print_h3!("Wrapping source errors with #[from]");
    #[derive(Error, Debug)]
    enum ParseError {
        #[error("empty input")]
        Empty,

        #[error("invalid number")]
        // #[from] derives From<ParseIntError> for ParseError AND sets that field as the .source()
        InvalidNumber(#[from] ParseIntError),
    }

    fn parse_id(input: &str) -> Result<i32, ParseError> {
        if input.is_empty() {
            return Err(ParseError::Empty);
        }
        let id: i32 = input.parse()?; // Auto-converts ParseIntError
        return Ok(id);
    }

    match parse_id("123") {
        Ok(id) => println!("Parsed ID: {}", id),
        Err(e) => println!("Parse error: {}", e),
    }

    match parse_id("") {
        Ok(id) => println!("Parsed ID: {}", id),
        Err(e) => println!("Parse error: {}", e),
    }

    match parse_id("abc") {
        Ok(id) => println!("Parsed ID: {}", id),
        Err(e) => println!("Parse error: {}", e),
    }

    print_h3!("Multiple source errors");
    #[derive(Error, Debug)]
    enum AppError {
        #[error("configuration error: {0}")]
        Config(String),

        #[error("parse error")]
        Parse(#[from] ParseIntError),

        #[error("data error")]
        Data(#[from] DataError),
    }

    fn initialize_app(config_valid: bool, data_id: u32) -> Result<(), AppError> {
        if !config_valid {
            return Err(AppError::Config(String::from("invalid config")));
        }

        let id: i32 = "42".parse()?; // ParseIntError auto-converts
        println!("Config ID: {}", id);

        let _data: String = load_data(data_id)?; // DataError auto-converts
        return Ok(());
    }

    match initialize_app(true, 42) {
        Ok(_) => println!("App initialized"),
        Err(e) => println!("Init error: {}", e),
    }

    match initialize_app(false, 42) {
        Ok(_) => println!("App initialized"),
        Err(e) => println!("Init error: {}", e),
    }

    match initialize_app(true, 0) {
        Ok(_) => println!("App initialized"),
        Err(e) => println!("Init error: {}", e),
    }

    print_h3!("Transparent errors");
    // #[error(transparent)] delegates Display to wrapped error
    #[derive(Error, Debug)]
    enum WrapperError {
        #[error(transparent)]
        ParseInt(#[from] ParseIntError),

        #[error(transparent)]
        Data(#[from] DataError),
    }

    fn process_with_wrapper(input: &str, id: u32) -> Result<String, WrapperError> {
        let num: i32 = input.parse()?;
        let data: String = load_data(id)?;
        return Ok(format!("{}-{}", num, data));
    }

    match process_with_wrapper("10", 5) {
        Ok(result) => println!("Result: {}", result),
        Err(e) => println!("Wrapper error: {}", e),
    }

    print_h3!("Custom error with source tracking");
    #[derive(Error, Debug)]
    enum NetworkError {
        #[error("connection failed: {message}")]
        ConnectionFailed {
            message: String,
            #[source]
            source: std::io::Error,
        },

        #[error("timeout after {duration}ms")]
        Timeout { duration: u64 },
    }

    fn simulate_connection() -> Result<(), NetworkError> {
        let io_err: std::io::Error =
            std::io::Error::new(std::io::ErrorKind::ConnectionRefused, "refused");

        return Err(NetworkError::ConnectionFailed {
            message: String::from("server unavailable"),
            source: io_err,
        });
    }

    match simulate_connection() {
        Ok(_) => println!("Connected"),
        Err(e) => {
            println!("Error: {}", e);
            if let Some(source) = std::error::Error::source(&e) {
                println!("Caused by: {}", source);
            }
        }
    }

    print_h3!("thiserror vs manual implementation");
    // Without thiserror (manual)
    #[derive(Debug)]
    enum ManualError {
        Simple,
    }

    impl std::fmt::Display for ManualError {
        fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result {
            match self {
                ManualError::Simple => write!(f, "simple error"),
            }
        }
    }

    impl std::error::Error for ManualError {}

    // With thiserror (automatic)
    #[derive(Error, Debug)]
    enum AutoError {
        #[error("simple error")]
        Simple,
    }

    let manual: ManualError = ManualError::Simple;
    let auto: AutoError = AutoError::Simple;

    println!("Manual: {}", manual);
    println!("Auto: {}", auto);

    print_h3!("Real-world example");
    #[derive(Error, Debug)]
    enum ApiError {
        #[error("HTTP {status}: {message}")]
        Http { status: u16, message: String },

        #[error("request timeout")]
        Timeout,

        #[error("invalid response format")]
        InvalidResponse(#[from] serde_json::Error),

        #[error("network error")]
        Network(#[from] std::io::Error),
    }

    fn make_api_call(status: u16) -> Result<String, ApiError> {
        if status == 200 {
            return Ok(String::from("success"));
        }
        return Err(ApiError::Http {
            status,
            message: String::from("server error"),
        });
    }

    match make_api_call(200) {
        Ok(resp) => println!("API response: {}", resp),
        Err(e) => println!("API error: {}", e),
    }

    match make_api_call(500) {
        Ok(resp) => println!("API response: {}", resp),
        Err(e) => println!("API error: {}", e),
    }
}
