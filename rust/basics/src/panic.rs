use shared::{print_h2, print_h3};

pub fn run() {
    print_h2!("Panic");

    print_h3!("Recoverable errors (Result)");
    // These are covered in option_result.rs
    // Result<T, E> for operations that can fail gracefully

    print_h3!("Unrecoverable errors (panic)");
    // panic! terminates program (or unwinds stack)
    println!("Before potential panic...");

    // Controlled panic examples (commented to avoid crashing)
    // panic!("Something went wrong!"); // Terminates with message

    print_h3!("Common panic triggers");
    // 1. Index out of bounds
    let arr: [i32; 3] = [1, 2, 3];
    println!("Valid access: {}", arr[0]);
    // PANIC: arr[10] would panic with "index out of bounds"

    // 2. unwrap on None
    let some_val: Option<i32> = Some(42);
    let unwrapped: i32 = some_val.unwrap();
    println!("Unwrapped: {}", unwrapped);

    let _none_val: Option<i32> = None;
    // PANIC: none_val.unwrap() would panic with "called `Option::unwrap()` on a `None` value"

    // 3. unwrap on Err
    let ok_result: Result<i32, &str> = Ok(100);
    let ok_unwrapped: i32 = ok_result.unwrap();
    println!("Result unwrapped: {}", ok_unwrapped);

    let _err_result: Result<i32, &str> = Err("failed");
    // PANIC: err_result.unwrap() would panic with the error message

    print_h3!("expect (custom panic message)");
    let val: Option<i32> = Some(5);
    let extracted: i32 = val.expect("Value should exist");
    println!("Extracted: {}", extracted);

    // PANIC: None.expect("custom msg") panics with custom message
    // Better for debugging than plain unwrap

    print_h3!("assert!");
    let x: i32 = 5;
    assert!(x == 5); // OK: condition true
    println!("assert! passed");

    // PANIC: assert!(x == 10) would panic with "assertion failed: x == 10"

    assert!(x > 0, "x must be positive"); // With custom message
    println!("assert! with message passed");

    print_h3!("assert_eq!");
    let a: i32 = 2 + 2;
    assert_eq!(a, 4); // OK: values equal
    println!("assert_eq! passed");

    // PANIC: assert_eq!(a, 5) would panic showing both values
    // "assertion failed: `(left == right)`\n  left: `4`,\n right: `5`"

    assert_eq!(a, 4, "Math is broken"); // Custom message
    println!("assert_eq! with message passed");

    print_h3!("assert_ne!");
    let b: i32 = 10;
    assert_ne!(b, 20); // OK: not equal
    println!("assert_ne! passed");

    // PANIC: assert_ne!(b, 10) would panic

    print_h3!("debug_assert! variants");
    // Only checked in debug builds, removed in release
    debug_assert!(true);
    debug_assert_eq!(2 + 2, 4);
    debug_assert_ne!(5, 10);
    println!("debug_assert variants passed");
    // Use for expensive checks that shouldn't impact production performance

    print_h3!("Panic behavior");
    // By default: stack unwinding (cleanup, run destructors)
    // Alternative: abort (no cleanup, faster)
    // Configured in Cargo.toml: panic = 'abort'

    print_h3!("catch_unwind (advanced)");
    // catch_unwind catches stack-unwinding panics but NOT abort-mode panics.
    // Intended for FFI boundaries or test harnesses — not general error handling.
    use std::panic;

    let result = panic::catch_unwind(|| {
        println!("Code that might panic");
        let safe: Vec<i32> = vec![1, 2, 3];
        return safe[0];
    });

    match result {
        Ok(val) => println!("Caught: {}", val),
        Err(_) => println!("Panic was caught"),
    }

    // PANIC example (caught)
    let caught = panic::catch_unwind(|| {
        panic!("Controlled panic");
    });

    if caught.is_err() {
        println!("Successfully caught panic");
    }

    print_h3!("Panic in tests");
    // #[should_panic] attribute in tests expects panic
    // Example:
    // #[test]
    // #[should_panic]
    // fn test_panic() {
    //     panic!("Expected");
    // }

    print_h3!("Unwrap alternatives");
    let opt: Option<i32> = None;

    // unwrap_or - provide default
    let val1: i32 = opt.unwrap_or(0);
    println!("unwrap_or: {}", val1);

    // unwrap_or_else - lazy default
    let val2: i32 = opt.unwrap_or_else(|| 42);
    println!("unwrap_or_else: {}", val2);

    // unwrap_or_default - type's default
    let val3: i32 = opt.unwrap_or_default();
    println!("unwrap_or_default: {}", val3);

    print_h3!("? operator (early return)");
    // Propagates errors instead of panicking
    // Covered in option_result.rs
    fn might_fail() -> Result<i32, String> {
        let val: Result<i32, String> = Ok(10);
        let extracted: i32 = val?; // Returns Err if error, continues if Ok
        return Ok(extracted * 2);
    }

    match might_fail() {
        Ok(v) => println!("? operator result: {}", v),
        Err(e) => println!("Error: {}", e),
    }

    print_h3!("Best practices");
    // 1. Prefer Result over panic for recoverable errors
    // 2. Use expect with descriptive messages over unwrap
    // 3. Use assertions for invariants and tests
    // 4. Use debug_assert for expensive checks
    // 5. Document when/why functions might panic

    println!("\nAll panic demonstrations completed safely!");
}
