use shared::{print_h2, print_h3};

pub fn run() {
    print_h2!("Printing & Formatting");

    print_h3!("Basic printing");
    println!("Hello, world!"); // With newline
    print!("No newline "); // Without newline
    print!("continues here\n");

    print_h3!("Variables in println");
    let name: &str = "Alice";
    let age: i32 = 30;
    println!("Name: {}, Age: {}", name, age);

    // Positional arguments
    println!("{0} is {1} years old. {0} lives here.", name, age);

    // Named arguments
    println!("{name} is {age} years old", name = "Bob", age = 25);

    print_h3!("Display vs Debug");
    // {} = Display trait (user-facing)
    // {:?} = Debug trait (developer-facing)
    let number: i32 = 42;
    println!("Display: {}", number);
    println!("Debug: {:?}", number);

    let vec: Vec<i32> = vec![1, 2, 3];
    // println!("Vec Display: {}", vec); // ERROR: Vec doesn't impl Display
    println!("Vec Debug: {:?}", vec);

    // Pretty print with {:#?}
    let nested: Vec<Vec<i32>> = vec![vec![1, 2], vec![3, 4]];
    println!("Pretty debug: {:#?}", nested);

    print_h3!("format! macro");
    // Creates String without printing
    let formatted: String = format!("{} + {} = {}", 2, 3, 5);
    println!("Formatted: {}", formatted);

    print_h3!("Number formatting");
    let num: i32 = 255;
    println!("Decimal: {}", num);
    println!("Hex: {:x}", num); // Lowercase
    println!("Hex: {:X}", num); // Uppercase
    println!("Hex with prefix: {:#x}", num);
    println!("Octal: {:o}", num);
    println!("Binary: {:b}", num);
    println!("Binary with prefix: {:#b}", num);

    print_h3!("Float formatting");
    let pi: f64 = 3.14159265359;
    println!("Default: {}", pi);
    println!("2 decimals: {:.2}", pi);
    println!("5 decimals: {:.5}", pi);
    println!("Scientific: {:e}", pi);
    println!("Scientific upper: {:E}", pi);

    print_h3!("Width and alignment");
    let text: &str = "test";
    println!("Default: '{}'", text);
    println!("Width 10: '{:10}'", text); // Right-aligned
    println!("Left-align: '{:<10}'", text);
    println!("Center: '{:^10}'", text);
    println!("Right-align: '{:>10}'", text);

    // With fill character
    println!("Fill with *: '{:*<10}'", text);
    println!("Fill center: '{:*^10}'", text);

    print_h3!("Padding numbers");
    let n: i32 = 42;
    println!("Padded: '{:5}'", n);
    println!("Zero-padded: '{:05}'", n);

    print_h3!("Sign control");
    let pos: i32 = 42;
    let neg: i32 = -42;
    println!("Default: {} {}", pos, neg);
    println!("Force sign: {:+} {:+}", pos, neg);

    print_h3!("Precision with integers");
    let value: i32 = 123;
    println!("Width 5: '{:5}'", value);
    println!("Width 5, zero-pad: '{:05}'", value);

    print_h3!("Combining formats");
    let num: f64 = 12.3456;
    println!("Width 10, 2 decimals: '{:10.2}'", num);
    println!("Zero-pad, 2 decimals: '{:08.2}'", num);

    print_h3!("Pointer formatting");
    let x: i32 = 42;
    let ptr: *const i32 = &x;
    println!("Pointer: {:p}", ptr);

    print_h3!("Escape braces");
    println!("Literal braces: {{}}");
    println!("Mixed: {{value}} = {}", 42);

    print_h3!("eprintln! (stderr)");
    eprintln!("This goes to stderr");
    println!("This goes to stdout");

    print_h3!("Custom types with Debug");
    #[derive(Debug)]
    struct Person {
        name: String,
        age: i32,
    }
    let person: Person = Person {
        name: String::from("Charlie"),
        age: 28,
    };
    println!("Debug: {:?}", person);
    println!("Pretty: {:#?}", person);

    print_h3!("Custom Display implementation");
    struct Point {
        x: i32,
        y: i32,
    }
    impl std::fmt::Display for Point {
        fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result {
            return write!(f, "({}, {})", self.x, self.y);
        }
    }
    let p: Point = Point { x: 10, y: 20 };
    println!("Display: {}", p);
    println!("Debug manually: ({}, {})", p.x, p.y);

    print_h3!("write! and writeln!");
    use std::fmt::Write;
    let mut buffer: String = String::new();
    write!(&mut buffer, "Hello").unwrap();
    write!(&mut buffer, " {}", "world").unwrap();
    println!("Buffer: {}", buffer);

    print_h3!("dbg! macro");
    // Prints file, line, expression, and value to stderr
    let result: i32 = dbg!(2 + 3);
    println!("Result: {}", result);

    let complex: Vec<i32> = vec![1, 2, 3];
    dbg!(&complex); // Borrow to avoid moving

    print_h3!("Conditional formatting");
    let debug_mode: bool = true;
    if debug_mode {
        println!("Debug: value = {}", 42);
    }

    print_h3!("Format args");
    let width: usize = 10;
    println!("{:width$}", "dynamic", width = width);

    let precision: usize = 3;
    println!("{:.precision$}", 3.14159, precision = precision);
}
