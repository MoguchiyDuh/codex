use shared::{print_h2, print_h3};
use std::error::Error;
use std::fmt;

pub fn run() {
    print_h2!("Error Trait");

    print_h3!("Implementing std::error::Error");
    // Custom error that implements Error trait
    #[derive(Debug)]
    enum AppError {
        IoError(String),
        ParseError(String),
        NetworkError(String),
    }

    impl fmt::Display for AppError {
        fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
            match self {
                AppError::IoError(msg) => write!(f, "IO error: {}", msg),
                AppError::ParseError(msg) => write!(f, "Parse error: {}", msg),
                AppError::NetworkError(msg) => write!(f, "Network error: {}", msg),
            }
        }
    }

    // Error trait requires Debug + Display as supertraits.
    // source() returns the lower-level error that caused this one (the error chain).
    // The '+ 'static bound means the returned error must not contain non-static references
    // (ensures it can be stored, passed around, and downcasted safely).
    impl Error for AppError {
        fn source(&self) -> Option<&(dyn Error + 'static)> {
            // No underlying error source in this simple case
            return None;
        }
    }

    fn do_something() -> Result<(), AppError> {
        return Err(AppError::IoError(String::from("disk full")));
    }

    match do_something() {
        Ok(_) => println!("Success"),
        Err(e) => {
            println!("Error: {}", e);
            println!("Debug: {:?}", e);
        }
    }

    print_h3!("Error with source chain");
    #[derive(Debug)]
    struct LowLevelError {
        message: String,
    }

    impl fmt::Display for LowLevelError {
        fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
            return write!(f, "Low level error: {}", self.message);
        }
    }

    impl Error for LowLevelError {}

    #[derive(Debug)]
    struct HighLevelError {
        message: String,
        source: LowLevelError,
    }

    impl fmt::Display for HighLevelError {
        fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
            return write!(f, "High level error: {}", self.message);
        }
    }

    impl Error for HighLevelError {
        fn source(&self) -> Option<&(dyn Error + 'static)> {
            return Some(&self.source);
        }
    }

    fn create_error_chain() -> Result<(), HighLevelError> {
        let low: LowLevelError = LowLevelError {
            message: String::from("hardware failure"),
        };
        return Err(HighLevelError {
            message: String::from("operation failed"),
            source: low,
        });
    }

    match create_error_chain() {
        Ok(_) => println!("Success"),
        Err(e) => {
            println!("Error: {}", e);
            if let Some(source) = e.source() {
                println!("Caused by: {}", source);
            }
        }
    }

    print_h3!("Walking the error chain");
    fn print_error_chain(err: &dyn Error) {
        println!("Error: {}", err);
        let mut current: Option<&dyn Error> = err.source();
        while let Some(source) = current {
            println!("  Caused by: {}", source);
            current = source.source();
        }
    }

    if let Err(e) = create_error_chain() {
        print_error_chain(&e);
    }

    print_h3!("Using Box<dyn Error> as trait object");
    fn might_fail(succeed: bool) -> Result<String, Box<dyn Error>> {
        if succeed {
            return Ok(String::from("success"));
        }
        return Err(Box::new(AppError::NetworkError(String::from(
            "connection timeout",
        ))));
    }

    match might_fail(true) {
        Ok(msg) => println!("Result: {}", msg),
        Err(e) => println!("Boxed error: {}", e),
    }

    match might_fail(false) {
        Ok(msg) => println!("Result: {}", msg),
        Err(e) => println!("Boxed error: {}", e),
    }

    print_h3!("Error trait methods");
    #[derive(Debug)]
    struct DetailedError {
        code: i32,
        message: String,
    }

    impl fmt::Display for DetailedError {
        fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
            return write!(f, "[Error {}] {}", self.code, self.message);
        }
    }

    impl Error for DetailedError {
        // Deprecated but still available
        fn description(&self) -> &str {
            return &self.message;
        }
    }

    let err: DetailedError = DetailedError {
        code: 404,
        message: String::from("Not found"),
    };

    println!("Display: {}", err);
    println!("Debug: {:?}", err);
    #[allow(deprecated)]
    {
        println!("Description: {}", err.description());
    }

    print_h3!("Generic error handling");
    fn handle_any_error<E: Error>(result: Result<(), E>) {
        match result {
            Ok(_) => println!("Operation succeeded"),
            Err(e) => println!("Operation failed: {}", e),
        }
    }

    let result1: Result<(), AppError> = Err(AppError::ParseError(String::from("bad input")));
    handle_any_error(result1);

    let result2: Result<(), DetailedError> = Err(DetailedError {
        code: 500,
        message: String::from("Internal error"),
    });
    handle_any_error(result2);
}
