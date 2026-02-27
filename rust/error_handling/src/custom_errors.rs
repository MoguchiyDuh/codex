use shared::{print_h2, print_h3};
use std::fmt;

pub fn run() {
    print_h2!("Custom Errors");

    print_h3!("Custom error enum");
    #[derive(Debug)]
    enum ParseError {
        EmptyInput,
        InvalidFormat,
        NumberTooLarge,
        NumberTooSmall,
    }

    // Display is the user-facing message; Debug (derived) is for {:?} formatting
    // Implementing Display + Debug + std::error::Error makes a type usable everywhere errors appear
    impl fmt::Display for ParseError {
        fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
            match self {
                ParseError::EmptyInput => write!(f, "Input cannot be empty"),
                ParseError::InvalidFormat => write!(f, "Invalid format provided"),
                ParseError::NumberTooLarge => write!(f, "Number exceeds maximum value"),
                ParseError::NumberTooSmall => write!(f, "Number is below minimum value"),
            }
        }
    }

    fn parse_number(input: &str) -> Result<i32, ParseError> {
        if input.is_empty() {
            return Err(ParseError::EmptyInput);
        }

        let num: i32 = match input.parse() {
            Ok(n) => n,
            Err(_) => return Err(ParseError::InvalidFormat),
        };

        if num > 100 {
            return Err(ParseError::NumberTooLarge);
        }
        if num < 0 {
            return Err(ParseError::NumberTooSmall);
        }

        return Ok(num);
    }

    // Successful parse
    match parse_number("42") {
        Ok(n) => println!("Parsed: {}", n),
        Err(e) => println!("Error: {}", e),
    }

    // Empty input error
    match parse_number("") {
        Ok(n) => println!("Parsed: {}", n),
        Err(e) => println!("Error: {}", e),
    }

    // Invalid format error
    match parse_number("abc") {
        Ok(n) => println!("Parsed: {}", n),
        Err(e) => println!("Error: {}", e),
    }

    // Number too large error
    match parse_number("200") {
        Ok(n) => println!("Parsed: {}", n),
        Err(e) => println!("Error: {}", e),
    }

    print_h3!("Pattern matching on custom errors");
    let result: Result<i32, ParseError> = parse_number("150");
    match result {
        Ok(n) => println!("Success: {}", n),
        Err(ParseError::EmptyInput) => println!("Please provide input"),
        Err(ParseError::InvalidFormat) => println!("Use numeric format"),
        Err(ParseError::NumberTooLarge) => println!("Number must be <= 100"),
        Err(ParseError::NumberTooSmall) => println!("Number must be >= 0"),
    }

    print_h3!("Multiple custom error types");
    #[derive(Debug)]
    enum FileError {
        NotFound,
        PermissionDenied,
        AlreadyExists,
    }

    impl fmt::Display for FileError {
        fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
            match self {
                FileError::NotFound => write!(f, "File not found"),
                FileError::PermissionDenied => write!(f, "Permission denied"),
                FileError::AlreadyExists => write!(f, "File already exists"),
            }
        }
    }

    #[derive(Debug)]
    enum DatabaseError {
        ConnectionFailed,
        QueryFailed,
        TransactionRollback,
    }

    impl fmt::Display for DatabaseError {
        fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
            match self {
                DatabaseError::ConnectionFailed => write!(f, "Failed to connect to database"),
                DatabaseError::QueryFailed => write!(f, "Query execution failed"),
                DatabaseError::TransactionRollback => write!(f, "Transaction was rolled back"),
            }
        }
    }

    fn open_file(path: &str) -> Result<String, FileError> {
        if path.is_empty() {
            return Err(FileError::NotFound);
        }
        return Ok(format!("File content: {}", path));
    }

    fn query_database(query: &str) -> Result<Vec<String>, DatabaseError> {
        if query.is_empty() {
            return Err(DatabaseError::QueryFailed);
        }
        return Ok(vec![String::from("result1"), String::from("result2")]);
    }

    match open_file("data.txt") {
        Ok(content) => println!("{}", content),
        Err(e) => println!("File error: {}", e),
    }

    match query_database("SELECT * FROM users") {
        Ok(results) => println!("Query results: {:?}", results),
        Err(e) => println!("Database error: {}", e),
    }

    print_h3!("Error with context (struct)");
    #[derive(Debug)]
    struct ValidationError {
        field: String,
        message: String,
    }

    impl fmt::Display for ValidationError {
        fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
            return write!(f, "Validation error in '{}': {}", self.field, self.message);
        }
    }

    fn validate_email(email: &str) -> Result<(), ValidationError> {
        if !email.contains('@') {
            return Err(ValidationError {
                field: String::from("email"),
                message: String::from("must contain @ symbol"),
            });
        }
        return Ok(());
    }

    match validate_email("invalid.com") {
        Ok(_) => println!("Email is valid"),
        Err(e) => println!("{}", e),
    }

    match validate_email("valid@example.com") {
        Ok(_) => println!("Email is valid"),
        Err(e) => println!("{}", e),
    }

    print_h3!("Error with additional data");
    #[derive(Debug)]
    struct RangeError {
        value: i32,
        min: i32,
        max: i32,
    }

    impl fmt::Display for RangeError {
        fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
            return write!(
                f,
                "Value {} is out of range [{}, {}]",
                self.value, self.min, self.max
            );
        }
    }

    fn check_range(value: i32, min: i32, max: i32) -> Result<i32, RangeError> {
        if value < min || value > max {
            return Err(RangeError { value, min, max });
        }
        return Ok(value);
    }

    match check_range(150, 0, 100) {
        Ok(v) => println!("Value {} is in range", v),
        Err(e) => println!("Error: {}", e),
    }

    match check_range(50, 0, 100) {
        Ok(v) => println!("Value {} is in range", v),
        Err(e) => println!("Error: {}", e),
    }
}
