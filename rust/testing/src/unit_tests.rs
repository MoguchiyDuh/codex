use shared::{print_h2, print_h3};

fn add(a: i32, b: i32) -> i32 {
    return a + b;
}

fn divide(a: f64, b: f64) -> Option<f64> {
    if b == 0.0 {
        return None;
    }
    return Some(a / b);
}

fn is_palindrome(s: &str) -> bool {
    let chars: Vec<char> = s.chars().collect();
    let reversed: Vec<char> = chars.iter().copied().rev().collect();
    return chars == reversed;
}

fn parse_positive(s: &str) -> Result<u32, String> {
    let n: i64 = s.trim().parse::<i64>().map_err(|e| e.to_string())?;
    if n < 0 {
        return Err(format!("{} is negative", n));
    }
    return Ok(n as u32);
}

pub fn run() {
    print_h2!("Unit Tests");

    print_h3!("Functions Being Tested");
    println!("add(2, 3)              = {}", add(2, 3));
    println!("divide(10.0, 3.0)      = {:?}", divide(10.0, 3.0));
    println!("divide(10.0, 0.0)      = {:?}", divide(10.0, 0.0));
    println!("is_palindrome(\"racecar\") = {}", is_palindrome("racecar"));
    println!("is_palindrome(\"hello\")   = {}", is_palindrome("hello"));
    println!("parse_positive(\"42\")   = {:?}", parse_positive("42"));
    println!("parse_positive(\"-1\")   = {:?}", parse_positive("-1"));
    println!("parse_positive(\"abc\")  = {:?}", parse_positive("abc"));

    print_h3!("Test Structure");
    // Tests live in a #[cfg(test)] module - compiled only during `cargo test`
    // Run with: cargo test -p testing
    // Run specific: cargo test -p testing unit_tests
    // Show output: cargo test -p testing -- --nocapture
    println!("Run: cargo test -p testing");
}

// #[cfg(test)] gates the entire module — it's compiled only when running `cargo test`.
// This prevents test helpers and test-only dependencies from bloating release builds.

#[cfg(test)]
mod tests {
    // `use super::*` imports everything from the parent module (the module under test).
    // The test module can access private items this way — intentional for unit testing.
    use super::*;

    // Basic test - function annotated with #[test]
    #[test]
    fn test_add_basic() {
        assert_eq!(add(2, 3), 5);
    }

    #[test]
    fn test_add_zero() {
        assert_eq!(add(0, 0), 0);
        assert_eq!(add(5, 0), 5);
    }

    #[test]
    fn test_add_negative() {
        assert_eq!(add(-1, -1), -2);
        assert_eq!(add(-5, 5), 0);
    }

    // Testing Option return
    #[test]
    fn test_divide_normal() {
        let result: Option<f64> = divide(10.0, 2.0);
        assert_eq!(result, Some(5.0));
    }

    #[test]
    fn test_divide_by_zero() {
        assert_eq!(divide(10.0, 0.0), None);
    }

    // Testing Result return
    #[test]
    fn test_parse_positive_valid() {
        assert_eq!(parse_positive("42"), Ok(42));
        assert_eq!(parse_positive("  7  "), Ok(7)); // trims whitespace
    }

    #[test]
    fn test_parse_positive_negative_number() {
        let result: Result<u32, String> = parse_positive("-1");
        assert!(result.is_err());
        assert!(result.unwrap_err().contains("negative"));
    }

    #[test]
    fn test_parse_positive_invalid_input() {
        assert!(parse_positive("abc").is_err());
        assert!(parse_positive("").is_err());
    }

    // Testing bool return
    #[test]
    fn test_palindrome_true() {
        assert!(is_palindrome("racecar"));
        assert!(is_palindrome("a"));
        assert!(is_palindrome(""));
        assert!(is_palindrome("madam"));
    }

    #[test]
    fn test_palindrome_false() {
        assert!(!is_palindrome("hello"));
        assert!(!is_palindrome("rust"));
    }

    // #[should_panic] - test passes only if it panics
    #[test]
    #[should_panic]
    fn test_expected_panic() {
        let v: Vec<i32> = vec![1, 2, 3];
        let _ = v[99]; // intentional panic
    }

    // #[should_panic(expected = "...")] - also checks the panic message
    #[test]
    #[should_panic(expected = "index out of bounds")]
    fn test_panic_message() {
        let v: Vec<i32> = vec![];
        let _ = v[0];
    }

    // #[ignore] - skipped by default, run with: cargo test -- --include-ignored
    #[test]
    #[ignore = "slow test - run explicitly with --include-ignored"]
    fn test_slow_operation() {
        std::thread::sleep(std::time::Duration::from_millis(100));
        assert_eq!(1 + 1, 2);
    }

    // Tests can return Result<(), E> — if the function returns Err, the test fails
    // with the error's Display message. This lets you use ? instead of .unwrap().
    #[test]
    fn test_with_result_return() -> Result<(), Box<dyn std::error::Error>> {
        let n: u32 = parse_positive("10")?;
        assert_eq!(n, 10);
        return Ok(());
    }
}
