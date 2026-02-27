use shared::{print_h2, print_h3};

pub fn run() {
    print_h2!("Conditionals");

    print_h3!("Basic if/else");
    let x: i32 = 10;
    if x > 5 {
        println!("x={} is greater than 5", x);
    }

    let y: i32 = 3;
    if y > 5 {
        println!("y > 5");
    } else {
        println!("y={} is not greater than 5", y);
    }

    let z: i32 = 7;
    if z < 5 {
        println!("z < 5");
    } else if z < 10 {
        println!("z={} is between 5 and 10", z);
    } else {
        println!("z >= 10");
    }

    print_h3!("if as expression");
    // if is an expression in Rust: all branches must have the same type
    let condition: bool = true;
    let number: i32 = if condition { 5 } else { 6 };
    println!("number from if expression: {}", number);

    let age: i32 = 20;
    let category: &str = if age < 18 {
        "minor"
    } else if age < 65 {
        "adult"
    } else {
        "senior"
    };
    println!("age={} -> category: {}", age, category);

    print_h3!("Comparison operators");
    let a: i32 = 10;
    let b: i32 = 20;
    println!("a={} b={}", a, b);
    println!("a == b: {}", a == b);
    println!("a != b: {}", a != b);
    println!("a < b: {}", a < b);
    println!("a > b: {}", a > b);
    println!("a <= b: {}", a <= b);
    println!("a >= b: {}", a >= b);

    print_h3!("Logical operators");
    let t: bool = true;
    let f: bool = false;
    println!("t={} f={}", t, f);
    println!("t && f: {}", t && f);
    println!("t || f: {}", t || f);
    println!("!t: {}", !t);
    println!("!f: {}", !f);

    let val: i32 = 15;
    if val > 10 && val < 20 {
        println!("{} is between 10 and 20", val);
    }

    if val < 5 || val > 12 {
        println!("{} is either < 5 or > 12", val);
    }

    print_h3!("Short-circuit evaluation");
    let result: bool = false && expensive_check(); // expensive_check() NOT called
    println!("Short-circuit AND: {}", result);

    let result2: bool = true || expensive_check(); // expensive_check() NOT called
    println!("Short-circuit OR: {}", result2);

    print_h3!("if let");
    let some_val: Option<i32> = Some(42);
    if let Some(v) = some_val {
        println!("if let extracted: {}", v);
    } else {
        println!("None");
    }

    let none_val: Option<i32> = None;
    if let Some(v) = none_val {
        println!("Has value: {}", v);
    } else {
        println!("if let: None case hit");
    }

    print_h3!("if let with multiple patterns");
    let tuple: (i32, i32) = (1, 2);
    if let (1, y) = tuple {
        println!("Matched tuple with first=1, second={}", y);
    }

    print_h3!("while let");
    let mut stack: Vec<i32> = vec![1, 2, 3];
    println!("Popping stack:");
    while let Some(top) = stack.pop() {
        println!("  popped: {}", top);
    }
    println!("Stack empty: {}", stack.is_empty());

    print_h3!("Nested conditionals");
    let outer: bool = true;
    let inner: i32 = 10;
    if outer {
        if inner > 5 {
            println!("Nested: outer && inner>5");
        }
    }

    print_h3!("Helper functions");
    println!("is_even(10): {}", is_even(10));
    println!("is_even(7): {}", is_even(7));
    println!("classify(-5): {}", classify(-5));
    println!("classify(0): {}", classify(0));
    println!("classify(3): {}", classify(3));
}

fn is_even(n: i32) -> bool {
    return n % 2 == 0;
}

fn classify(n: i32) -> &'static str {
    if n < 0 {
        return "negative";
    } else if n == 0 {
        return "zero";
    } else {
        return "positive";
    }
}

fn expensive_check() -> bool {
    println!("  [expensive_check called]");
    return true;
}
