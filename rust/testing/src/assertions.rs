use shared::{print_h2, print_h3};

pub fn run() {
    print_h2!("Assertions and Custom Messages");

    print_h3!("assert!");
    assert!(2 + 2 == 4);
    assert!(true);
    assert!(!false);

    let x: i32 = 10;
    assert!(x > 0, "expected positive, got {}", x);
    // PANIC: assert!(x < 0, "expected negative, got {}", x)

    println!("assert!(condition) - panics if false");

    print_h3!("assert_eq! and assert_ne!");
    assert_eq!(2 * 3, 6);
    assert_eq!("hello", "hello");
    assert_eq!(vec![1, 2, 3], vec![1, 2, 3]);

    assert_ne!(1, 2);
    assert_ne!("foo", "bar");

    let result: i32 = 42;
    let expected: i32 = 42;
    assert_eq!(result, expected, "compute() returned wrong value");
    // PANIC: assert_eq!(1, 2) prints: assertion `left == right` failed\n  left: 1\n right: 2

    println!("assert_eq! / assert_ne! - show both values on failure");

    print_h3!("Float Comparison");
    // IEEE 754 floats cannot represent 0.1, 0.2, or 0.3 exactly; their sum accumulates error.
    // assert_eq! on floats is unreliable due to precision
    let a: f64 = 0.1 + 0.2;
    let b: f64 = 0.3;
    println!("0.1 + 0.2 = {:.17}", a);
    println!("0.3       = {:.17}", b);
    println!("0.1 + 0.2 == 0.3: {}", a == b); // false due to float imprecision

    fn approx_eq(a: f64, b: f64, epsilon: f64) -> bool {
        return (a - b).abs() < epsilon;
    }
    assert!(approx_eq(0.1 + 0.2, 0.3, 1e-10));
    println!("approx_eq(0.1+0.2, 0.3, 1e-10) = true");

    print_h3!("Custom Assertion Macros");

    macro_rules! assert_approx_eq {
        ($left:expr, $right:expr) => {
            assert_approx_eq!($left, $right, 1e-10)
        };
        ($left:expr, $right:expr, $eps:expr) => {{
            let diff: f64 = (($left as f64) - ($right as f64)).abs();
            assert!(
                diff < $eps,
                "approx eq failed: |{} - {}| = {} >= {}",
                $left,
                $right,
                diff,
                $eps
            );
        }};
    }

    assert_approx_eq!(0.1 + 0.2, 0.3);
    assert_approx_eq!(std::f64::consts::PI, 3.14159, 1e-4);
    println!("assert_approx_eq!(0.1+0.2, 0.3) passed");

    macro_rules! assert_contains {
        ($haystack:expr, $needle:expr) => {
            assert!(
                $haystack.contains($needle),
                "expected {:?} to contain {:?}",
                $haystack,
                $needle
            );
        };
    }

    let s: &str = "hello world";
    assert_contains!(s, "world");
    println!("assert_contains!(\"hello world\", \"world\") passed");

    macro_rules! assert_sorted {
        ($slice:expr) => {{
            let s = $slice;
            for i in 1..s.len() {
                assert!(
                    s[i - 1] <= s[i],
                    "not sorted at index {}: {} > {}",
                    i,
                    s[i - 1],
                    s[i]
                );
            }
        }};
    }

    let sorted: [i32; 5] = [1, 2, 3, 4, 5];
    assert_sorted!(&sorted);
    println!("assert_sorted!([1,2,3,4,5]) passed");

    print_h3!("debug_assert (release-stripped)");

    debug_assert!(1 < 2);
    debug_assert_eq!(2 + 2, 4);
    debug_assert_ne!(0, 1);
    println!(
        "debug_assert* - only active in debug builds (cfg!(debug_assertions) = {})",
        cfg!(debug_assertions)
    );
}

#[cfg(test)]
mod tests {
    #[allow(unused_imports)]
    use super::*;

    fn approx_eq(a: f64, b: f64, epsilon: f64) -> bool {
        return (a - b).abs() < epsilon;
    }

    #[test]
    fn test_float_approx() {
        assert!(approx_eq(0.1 + 0.2, 0.3, 1e-10));
    }

    // #[should_panic(expected = "...")] verifies the panic message contains the expected substring
    #[test]
    #[should_panic(expected = "assertion")]
    fn test_assert_fails() {
        assert_eq!(1, 2);
    }

    #[test]
    fn test_vec_equality() {
        let a: Vec<i32> = vec![1, 2, 3];
        let b: Vec<i32> = vec![1, 2, 3];
        assert_eq!(a, b);
    }

    #[test]
    fn test_string_assertions() {
        let s: String = String::from("hello world");
        assert!(s.contains("world"));
        assert!(s.starts_with("hello"));
        assert!(s.ends_with("world"));
        assert_eq!(s.len(), 11);
    }
}
