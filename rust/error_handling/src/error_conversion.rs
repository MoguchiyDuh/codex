use shared::{print_h2, print_h3};
use std::error::Error;
use std::fmt;
use std::num::ParseIntError;

pub fn run() {
    print_h2!("Error Conversion");

    print_h3!("Converting between error types with From");
    #[derive(Debug)]
    enum AppError {
        Io(String),
        Parse(ParseIntError),
        Custom(String),
    }

    impl fmt::Display for AppError {
        fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
            match self {
                AppError::Io(msg) => write!(f, "IO error: {}", msg),
                AppError::Parse(e) => write!(f, "Parse error: {}", e),
                AppError::Custom(msg) => write!(f, "Custom error: {}", msg),
            }
        }
    }

    impl Error for AppError {}

    // Implement From to convert ParseIntError to AppError.
    // The ? operator desugars to: .map_err(AppError::from)? when the error types differ.
    // So having From<ParseIntError> for AppError is what enables `?` in functions returning AppError.
    impl From<ParseIntError> for AppError {
        fn from(err: ParseIntError) -> AppError {
            return AppError::Parse(err);
        }
    }

    // Now ? operator can automatically convert ParseIntError to AppError
    fn parse_and_double(input: &str) -> Result<i32, AppError> {
        let num: i32 = input.parse()?; // Auto-converts ParseIntError -> AppError via From
        return Ok(num * 2);
    }

    match parse_and_double("21") {
        Ok(n) => println!("Result: {}", n),
        Err(e) => println!("Error: {}", e),
    }

    match parse_and_double("abc") {
        Ok(n) => println!("Result: {}", n),
        Err(e) => println!("Error: {}", e),
    }

    print_h3!("Multiple From implementations");
    #[derive(Debug)]
    struct IoError {
        message: String,
    }

    impl fmt::Display for IoError {
        fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
            return write!(f, "IO: {}", self.message);
        }
    }

    impl Error for IoError {}

    #[derive(Debug)]
    struct NetworkError {
        code: i32,
    }

    impl fmt::Display for NetworkError {
        fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
            return write!(f, "Network error code {}", self.code);
        }
    }

    impl Error for NetworkError {}

    #[derive(Debug)]
    enum UnifiedError {
        Io(IoError),
        Network(NetworkError),
        Parse(ParseIntError),
    }

    impl fmt::Display for UnifiedError {
        fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
            match self {
                UnifiedError::Io(e) => write!(f, "{}", e),
                UnifiedError::Network(e) => write!(f, "{}", e),
                UnifiedError::Parse(e) => write!(f, "Parse: {}", e),
            }
        }
    }

    impl Error for UnifiedError {}

    impl From<IoError> for UnifiedError {
        fn from(err: IoError) -> UnifiedError {
            return UnifiedError::Io(err);
        }
    }

    impl From<NetworkError> for UnifiedError {
        fn from(err: NetworkError) -> UnifiedError {
            return UnifiedError::Network(err);
        }
    }

    impl From<ParseIntError> for UnifiedError {
        fn from(err: ParseIntError) -> UnifiedError {
            return UnifiedError::Parse(err);
        }
    }

    fn read_file() -> Result<String, IoError> {
        return Err(IoError {
            message: String::from("file not found"),
        });
    }

    fn fetch_data() -> Result<String, NetworkError> {
        return Err(NetworkError { code: 404 });
    }

    // All errors automatically convert to UnifiedError
    fn combined_operation() -> Result<String, UnifiedError> {
        let _file: String = read_file()?; // IoError -> UnifiedError
        let _data: String = fetch_data()?; // NetworkError -> UnifiedError
        let _num: i32 = "abc".parse()?; // ParseIntError -> UnifiedError
        return Ok(String::from("success"));
    }

    match combined_operation() {
        Ok(s) => println!("Success: {}", s),
        Err(e) => println!("Combined error: {}", e),
    }

    print_h3!("Manual error mapping");
    fn manual_conversion(input: &str) -> Result<i32, String> {
        let num: i32 = input
            .parse()
            .map_err(|e: ParseIntError| format!("Failed to parse: {}", e))?;
        return Ok(num);
    }

    match manual_conversion("42") {
        Ok(n) => println!("Parsed: {}", n),
        Err(e) => println!("Error: {}", e),
    }

    match manual_conversion("xyz") {
        Ok(n) => println!("Parsed: {}", n),
        Err(e) => println!("Error: {}", e),
    }

    print_h3!("Converting to Box<dyn Error>");
    fn as_trait_object() -> Result<(), Box<dyn Error>> {
        let err: AppError = AppError::Custom(String::from("something went wrong"));
        return Err(Box::new(err));
    }

    match as_trait_object() {
        Ok(_) => println!("Success"),
        Err(e) => println!("Boxed error: {}", e),
    }

    print_h3!("Downcasting errors");
    fn create_specific_error() -> Result<(), Box<dyn Error>> {
        return Err(Box::new(NetworkError { code: 500 }));
    }

    match create_specific_error() {
        Ok(_) => println!("Success"),
        Err(e) => {
            println!("Error: {}", e);

            // downcast_ref uses the vtable's TypeId to check if the underlying type matches.
            // Returns None if the concrete type doesn't match — safe, no UB.
            if let Some(net_err) = e.downcast_ref::<NetworkError>() {
                println!("It's a NetworkError with code: {}", net_err.code);
            }
        }
    }

    print_h3!("Error context wrapping");
    fn add_context<E: Error>(result: Result<(), E>, context: &str) -> Result<(), String> {
        return result.map_err(|e| format!("{}: {}", context, e));
    }

    let result: Result<(), NetworkError> = Err(NetworkError { code: 503 });
    match add_context(result, "Failed to connect") {
        Ok(_) => println!("Success"),
        Err(e) => println!("{}", e),
    }
}
