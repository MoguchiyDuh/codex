use shared::{print_h2, print_h3};

pub fn run() {
    print_h2!("Option & Result");

    print_h3!("Option basics");
    let some_val: Option<i32> = Some(42);
    let none_val: Option<i32> = None;
    println!("Some: {:?}, None: {:?}", some_val, none_val);

    print_h3!("is_some / is_none");
    println!(
        "is_some: {}, is_none: {}",
        some_val.is_some(),
        some_val.is_none()
    );
    println!("none is_some: {}", none_val.is_some());

    print_h3!("unwrap variants");
    let unwrapped: i32 = some_val.unwrap();
    println!("unwrap: {}", unwrapped);
    // PANIC: none_val.unwrap() would panic

    let with_default: i32 = none_val.unwrap_or(0);
    println!("unwrap_or: {}", with_default);

    let with_fn: i32 = none_val.unwrap_or_else(|| 100);
    println!("unwrap_or_else: {}", with_fn);

    let expected: i32 = some_val.expect("Should have value");
    println!("expect: {}", expected);
    // PANIC: none_val.expect("msg") would panic with custom message

    print_h3!("map");
    let doubled: Option<i32> = some_val.map(|x: i32| x * 2);
    println!("map doubled: {:?}", doubled);

    let none_doubled: Option<i32> = none_val.map(|x: i32| x * 2);
    println!("map on None: {:?}", none_doubled);

    print_h3!("and_then (flatMap)");
    // and_then is monadic bind: if Some, applies fn returning Option; avoids Option<Option<T>>
    let result: Option<i32> = some_val.and_then(|x: i32| {
        if x > 10 {
            return Some(x * 2);
        }
        return None;
    });
    println!("and_then: {:?}", result);

    print_h3!("or / or_else");
    let fallback: Option<i32> = none_val.or(Some(999));
    println!("or: {:?}", fallback);

    let lazy_fallback: Option<i32> = none_val.or_else(|| Some(888));
    println!("or_else: {:?}", lazy_fallback);

    print_h3!("filter");
    let filtered: Option<i32> = some_val.filter(|&x: &i32| x > 50);
    println!("filter(>50): {:?}", filtered);

    let filtered2: Option<i32> = some_val.filter(|&x: &i32| x > 10);
    println!("filter(>10): {:?}", filtered2);

    print_h3!("ok_or / ok_or_else");
    // ok_or converts Option -> Result: Some(v) => Ok(v), None => Err(e)
    let as_result: Result<i32, &str> = some_val.ok_or("No value");
    println!("ok_or: {:?}", as_result);

    let none_as_result: Result<i32, &str> = none_val.ok_or("No value");
    println!("None ok_or: {:?}", none_as_result);

    print_h3!("take / replace");
    let mut opt: Option<i32> = Some(5);
    let taken: Option<i32> = opt.take();
    println!("take: {:?}, opt after: {:?}", taken, opt);

    let replaced: Option<i32> = opt.replace(10);
    println!("replace: {:?}, opt after: {:?}", replaced, opt);

    print_h3!("Pattern matching");
    match some_val {
        Some(v) => println!("match Some: {}", v),
        None => println!("match None"),
    }

    if let Some(v) = some_val {
        println!("if let Some: {}", v);
    }

    print_h3!("Result basics");
    let ok_val: Result<i32, &str> = Ok(100);
    let err_val: Result<i32, &str> = Err("error occurred");
    println!("Ok: {:?}, Err: {:?}", ok_val, err_val);

    print_h3!("is_ok / is_err");
    println!("is_ok: {}, is_err: {}", ok_val.is_ok(), ok_val.is_err());

    print_h3!("unwrap variants (Result)");
    let ok_unwrapped: i32 = ok_val.unwrap();
    println!("Result unwrap: {}", ok_unwrapped);
    // PANIC: err_val.unwrap() would panic

    let err_default: i32 = err_val.unwrap_or(0);
    println!("Result unwrap_or: {}", err_default);

    let err_expected: Result<i32, &str> = Ok(200);
    let val: i32 = err_expected.expect("Should be Ok");
    println!("Result expect: {}", val);

    print_h3!("map / map_err");
    let mapped: Result<i32, &str> = ok_val.map(|x: i32| x * 2);
    println!("Result map: {:?}", mapped);

    let mapped_err: Result<i32, String> = err_val.map_err(|e: &str| format!("Error: {}", e));
    println!("map_err: {:?}", mapped_err);

    print_h3!("and_then (Result)");
    let chained: Result<i32, &str> = ok_val.and_then(|x: i32| {
        if x > 50 {
            return Ok(x * 2);
        }
        return Err("too small");
    });
    println!("Result and_then: {:?}", chained);

    print_h3!("or / or_else (Result)");
    let recovered: Result<i32, &str> = err_val.or(Ok(999));
    println!("Result or: {:?}", recovered);

    let lazy_recovered: Result<i32, &str> = err_val.or_else(|_| Ok(888));
    println!("Result or_else: {:?}", lazy_recovered);

    print_h3!("? operator");
    let calc_result: Result<f64, String> = calculate();
    println!("? operator result: {:?}", calc_result);

    print_h3!("ok / err");
    let opt_from_ok: Option<i32> = ok_val.ok();
    println!("Result.ok(): {:?}", opt_from_ok);

    let opt_from_err: Option<&str> = err_val.err();
    println!("Result.err(): {:?}", opt_from_err);

    print_h3!("transpose");
    // transpose flips Option<Result<T,E>> <-> Result<Option<T>,E>, useful when combining both
    let opt_result: Option<Result<i32, &str>> = Some(Ok(42));
    let transposed: Result<Option<i32>, &str> = opt_result.transpose();
    println!("transpose: {:?}", transposed);

    print_h3!("Helper functions");
    println!("safe_divide(10, 2): {:?}", safe_divide(10, 2));
    println!("safe_divide(10, 0): {:?}", safe_divide(10, 0));

    println!("parse_int('42'): {:?}", parse_int("42"));
    println!("parse_int('abc'): {:?}", parse_int("abc"));
}

fn safe_divide(a: i32, b: i32) -> Option<i32> {
    if b == 0 {
        return None;
    }
    return Some(a / b);
}

fn parse_int(s: &str) -> Result<i32, String> {
    return s.parse::<i32>().map_err(|e| format!("Parse error: {}", e));
}

fn calculate() -> Result<f64, String> {
    let x: f64 = divide_res(10.0, 2.0)?;
    let y: f64 = divide_res(x, 5.0)?;
    return Ok(y);
}

fn divide_res(a: f64, b: f64) -> Result<f64, String> {
    if b == 0.0 {
        return Err("Division by zero".to_string());
    }
    return Ok(a / b);
}
