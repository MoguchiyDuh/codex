use shared::{print_h2, print_h3};

pub fn run() {
    print_h2!("Pattern Matching");

    print_h3!("Basic match");
    let number: i32 = 3;
    match number {
        1 => println!("One"),
        2 => println!("Two"),
        3 => println!("Three"),
        _ => println!("Other"),
    }
    // ERROR: Without _ or exhaustive cases, match won't compile (non-exhaustive)

    print_h3!("Match as expression");
    let result: &str = match number {
        1 => "one",
        2 => "two",
        3 => "three",
        _ => "other",
    };
    println!("result: {}", result);

    print_h3!("Multiple patterns with |");
    let digit: i32 = 5;
    match digit {
        1 | 2 | 3 => println!("1-3"),
        4 | 5 | 6 => println!("4-6"),
        _ => println!("other"),
    }

    print_h3!("Range patterns");
    let age: i32 = 25;
    match age {
        0..=12 => println!("Child"),
        13..=19 => println!("Teen"),
        20..=64 => println!("Adult"),
        _ => println!("Senior"),
    }

    print_h3!("Guards (if conditions)");
    let pair: (i32, i32) = (5, 10);
    match pair {
        (x, y) if x == y => println!("Equal"),
        (x, y) if x + y == 15 => println!("Sum is 15"),
        (x, y) if x > y => println!("x > y"),
        _ => println!("Other"),
    }

    print_h3!("@ bindings");
    let val: i32 = 15;
    match val {
        // @ binds the matched value to a name while also testing the pattern.
        // Without @, you'd need a guard: n if n >= 10 && n <= 20 (less precise)
        n @ 10..=20 => println!("In range 10-20: {}", n),
        n @ 21..=30 => println!("In range 21-30: {}", n),
        _ => println!("Out of range"),
    }

    print_h3!("Tuple destructuring");
    let point: (i32, i32) = (3, 5);
    match point {
        (0, 0) => println!("Origin"),
        (x, 0) => println!("On X-axis: {}", x),
        (0, y) => println!("On Y-axis: {}", y),
        (x, y) => println!("Point ({}, {})", x, y),
    }

    print_h3!("Struct destructuring");
    struct Point {
        x: i32,
        y: i32,
    }
    let p: Point = Point { x: 10, y: 20 };
    match p {
        Point { x: 0, y: 0 } => println!("Origin"),
        Point { x, y: 0 } => println!("X-axis at {}", x),
        Point { x: 0, y } => println!("Y-axis at {}", y),
        Point { x, y } => println!("Point ({}, {})", x, y),
    }

    print_h3!("Enum matching");
    enum Message {
        Quit,
        Move { x: i32, y: i32 },
        Write(String),
        ChangeColor(i32, i32, i32),
    }
    let msg: Message = Message::Move { x: 10, y: 20 };
    match msg {
        Message::Quit => println!("Quit"),
        Message::Move { x, y } => println!("Move to ({}, {})", x, y),
        Message::Write(text) => println!("Write: {}", text),
        Message::ChangeColor(r, g, b) => println!("Color RGB({}, {}, {})", r, g, b),
    }

    print_h3!("Option matching");
    let some_val: Option<i32> = Some(42);
    match some_val {
        Some(n) => println!("Has value: {}", n),
        None => println!("No value"),
    }

    let maybe: Option<i32> = None;
    let unwrapped: i32 = match maybe {
        Some(n) => n,
        None => 0,
    };
    println!("Unwrapped with default: {}", unwrapped);

    print_h3!("Result matching");
    let result: Result<i32, &str> = Ok(100);
    match result {
        Ok(val) => println!("Success: {}", val),
        Err(e) => println!("Error: {}", e),
    }

    print_h3!("Nested patterns");
    let nested: Option<Option<i32>> = Some(Some(5));
    match nested {
        Some(Some(n)) => println!("Nested value: {}", n),
        Some(None) => println!("Inner None"),
        None => println!("Outer None"),
    }

    print_h3!("Ignoring values with _");
    let triple: (i32, i32, i32) = (1, 2, 3);
    match triple {
        (_, _, z) => println!("Only care about z: {}", z),
    }

    print_h3!("Ignoring remaining with ..");
    let quad: (i32, i32, i32, i32) = (1, 2, 3, 4);
    // .. in a tuple or struct pattern skips any number of fields.
    // In a slice pattern [first, .., last], it matches zero or more middle elements.
    match quad {
        (first, .., last) => println!("First: {}, Last: {}", first, last),
    }

    print_h3!("Reference patterns");
    let ref_val: &i32 = &42;
    match ref_val {
        &n => println!("Dereferenced: {}", n),
    }

    let val2: i32 = 50;
    match &val2 {
        n => println!("Reference: {}", n),
    }

    print_h3!("Slice patterns");
    // Slice patterns work on &[T] (not arrays directly) — call .as_slice() to convert
    let arr: [i32; 5] = [1, 2, 3, 4, 5];
    match arr.as_slice() {
        [first, second, ..] => println!("First two: {}, {}", first, second),
        [] => println!("Empty"),
        _ => println!("Other"),
    }

    let vec: Vec<i32> = vec![10, 20, 30];
    match vec.as_slice() {
        [] => println!("Empty vec"),
        [single] => println!("Single: {}", single),
        [first, .., last] => println!("First: {}, Last: {}", first, last),
    }

    print_h3!("if let");
    let opt: Option<i32> = Some(7);
    if let Some(n) = opt {
        println!("if let extracted: {}", n);
    }

    print_h3!("if let with else");
    let opt2: Option<i32> = None;
    if let Some(n) = opt2 {
        println!("Has: {}", n);
    } else {
        println!("if let else: None");
    }

    print_h3!("while let");
    let mut stack: Vec<i32> = vec![1, 2, 3];
    while let Some(top) = stack.pop() {
        print!("{} ", top);
    }
    println!();

    print_h3!("let destructuring");
    let (a, b, c): (i32, i32, i32) = (1, 2, 3);
    println!("let destructure: a={} b={} c={}", a, b, c);

    let Point { x, y } = Point { x: 100, y: 200 };
    println!("Struct destructure: x={} y={}", x, y);

    print_h3!("Match with multiple statements");
    let code: i32 = 200;
    match code {
        200 => {
            println!("OK");
            println!("Request successful");
        }
        404 => {
            println!("Not Found");
        }
        _ => println!("Other status"),
    }

    print_h3!("Exhaustiveness check");
    enum Color {
        Red,
        Green,
        Blue,
    }
    let color: Color = Color::Red;
    match color {
        Color::Red => println!("Red"),
        Color::Green => println!("Green"),
        Color::Blue => println!("Blue"),
        // ERROR: Removing any case would cause compile error (non-exhaustive)
    }
}
