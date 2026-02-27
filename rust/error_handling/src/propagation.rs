use shared::{print_h2, print_h3};

pub fn run() {
    print_h2!("Error Propagation");

    print_h3!("The ? operator");
    fn divide(a: f64, b: f64) -> Result<f64, String> {
        if b == 0.0 {
            return Err(String::from("division by zero"));
        }
        return Ok(a / b);
    }


    fn calculate_manual() -> Result<f64, String> {
        let result1: f64 = match divide(10.0, 2.0) {
            Ok(val) => val,
            Err(e) => return Err(e),
        };

        let result2: f64 = match divide(result1, 5.0) {
            Ok(val) => val,
            Err(e) => return Err(e),
        };

        return Ok(result2);
    }


    fn calculate_auto() -> Result<f64, String> {
        let result1: f64 = divide(10.0, 2.0)?;
        let result2: f64 = divide(result1, 5.0)?;
        return Ok(result2);
    }

    match calculate_manual() {
        Ok(v) => println!("Manual result: {}", v),
        Err(e) => println!("Manual error: {}", e),
    }

    match calculate_auto() {
        Ok(v) => println!("Auto result: {}", v),
        Err(e) => println!("Auto error: {}", e),
    }

    print_h3!("Chaining operations with ?");
    fn parse_number(s: &str) -> Result<i32, String> {
        return s.parse().map_err(|_| String::from("parse failed"));
    }

    fn validate_positive(n: i32) -> Result<i32, String> {
        if n <= 0 {
            return Err(String::from("must be positive"));
        }
        return Ok(n);
    }

    fn double(n: i32) -> Result<i32, String> {
        return Ok(n * 2);
    }

    fn process_input(input: &str) -> Result<i32, String> {
        let num: i32 = parse_number(input)?;
        let validated: i32 = validate_positive(num)?;
        let result: i32 = double(validated)?;
        return Ok(result);
    }

    match process_input("42") {
        Ok(v) => println!("Processed: {}", v),
        Err(e) => println!("Error: {}", e),
    }

    match process_input("-5") {
        Ok(v) => println!("Processed: {}", v),
        Err(e) => println!("Error: {}", e),
    }

    match process_input("abc") {
        Ok(v) => println!("Processed: {}", v),
        Err(e) => println!("Error: {}", e),
    }

    print_h3!("? with Option");
    fn get_first_char(s: &str) -> Option<char> {
        return s.chars().next();
    }

    fn get_uppercase(s: &str) -> Option<char> {
        let c: char = get_first_char(s)?;
        return Some(c.to_ascii_uppercase());
    }

    match get_uppercase("hello") {
        Some(c) => println!("First char uppercase: {}", c),
        None => println!("No first char"),
    }

    match get_uppercase("") {
        Some(c) => println!("First char uppercase: {}", c),
        None => println!("No first char"),
    }

    print_h3!("Early return without ?");
    fn check_multiple_conditions(val: i32) -> Result<i32, String> {
        if val < 0 {
            return Err(String::from("negative"));
        }

        if val > 100 {
            return Err(String::from("too large"));
        }

        if val % 2 != 0 {
            return Err(String::from("not even"));
        }

        return Ok(val);
    }

    match check_multiple_conditions(42) {
        Ok(v) => println!("Valid: {}", v),
        Err(e) => println!("Invalid: {}", e),
    }

    match check_multiple_conditions(43) {
        Ok(v) => println!("Valid: {}", v),
        Err(e) => println!("Invalid: {}", e),
    }

    print_h3!("Propagating different error types");
    #[derive(Debug)]
    enum Error {
        Parse(String),
        Validation(String),
        Compute(String),
    }

    fn parse(s: &str) -> Result<i32, Error> {
        return s
            .parse()
            .map_err(|_| Error::Parse(String::from("invalid number")));
    }

    fn validate(n: i32) -> Result<i32, Error> {
        if n > 1000 {
            return Err(Error::Validation(String::from("too large")));
        }
        return Ok(n);
    }

    fn compute(n: i32) -> Result<i32, Error> {
        if n == 13 {
            return Err(Error::Compute(String::from("unlucky number")));
        }
        return Ok(n * n);
    }

    fn pipeline(input: &str) -> Result<i32, Error> {
        let num: i32 = parse(input)?;
        let validated: i32 = validate(num)?;
        let result: i32 = compute(validated)?;
        return Ok(result);
    }

    match pipeline("10") {
        Ok(v) => println!("Pipeline result: {}", v),
        Err(e) => println!("Pipeline error: {:?}", e),
    }

    match pipeline("2000") {
        Ok(v) => println!("Pipeline result: {}", v),
        Err(e) => println!("Pipeline error: {:?}", e),
    }

    match pipeline("13") {
        Ok(v) => println!("Pipeline result: {}", v),
        Err(e) => println!("Pipeline error: {:?}", e),
    }

    print_h3!("Shortcut methods after ?");
    fn get_value() -> Result<Option<i32>, String> {
        return Ok(Some(42));
    }

    fn extract() -> Result<i32, String> {
        let opt: Option<i32> = get_value()?;
        return opt.ok_or_else(|| String::from("value missing"));
    }

    match extract() {
        Ok(v) => println!("Extracted: {}", v),
        Err(e) => println!("Extract error: {}", e),
    }

    print_h3!("Propagating in closures");
    fn process_list(items: Vec<&str>) -> Result<Vec<i32>, String> {
        // The ? inside a closure returns from the closure, not the outer function.
        // Collecting into Result<Vec<T>, E> short-circuits: first Err stops the iteration.
        // This works because Result implements FromIterator.
        let results: Result<Vec<i32>, String> = items
            .into_iter()
            .map(|item| {
                let num: i32 = item.parse().map_err(|_| String::from("parse failed"))?;
                return Ok(num * 2);
            })
            .collect();

        return results;
    }

    match process_list(vec!["1", "2", "3"]) {
        Ok(v) => println!("Processed list: {:?}", v),
        Err(e) => println!("List error: {}", e),
    }

    match process_list(vec!["1", "bad", "3"]) {
        Ok(v) => println!("Processed list: {:?}", v),
        Err(e) => println!("List error: {}", e),
    }
}
