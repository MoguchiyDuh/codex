use shared::{print_h2, print_h3};

pub fn run() {
    print_h2!("Built-in Standard Macros");

    print_h3!("Formatting macros");
    println!("println! - prints with newline to stdout");
    print!("print! - no newline ");
    print!("continues here\n");
    eprintln!("eprintln! - prints to stderr");

    let s: String = format!("format! returns a String: {}", 42);
    println!("{}", s);

    print_h3!("Assertion macros");
    assert!(1 + 1 == 2);
    assert_eq!(2 + 2, 4);
    assert_ne!(2 + 2, 5);
    assert!(true, "custom message: {}", "detail"); // supports format args
    // PANIC: assert!(false) panics immediately

    // debug_assert* only fires in debug builds (stripped in --release)
    debug_assert!(1 < 2);
    debug_assert_eq!(3 * 3, 9);
    debug_assert_ne!(0, 1);
    println!("All assertions passed");

    print_h3!("dbg!");
    let x: i32 = 5;
    // dbg! prints [file:line] expr = value to stderr, then returns the value
    let y: i32 = dbg!(x * 2) + 1;
    println!("y after dbg! = {}", y);

    let v: Vec<i32> = dbg!(vec![1, 2, 3]);
    println!("v = {:?}", v);

    print_h3!("Placeholders (todo!, unimplemented!, unreachable!)");

    fn in_progress() -> i32 {
        todo!("implement this later") // panics with: not yet implemented: ...
    }
    fn not_supported() -> i32 {
        unimplemented!("this variant is not supported")
    }
    // PANIC: in_progress() -> "not yet implemented: implement this later"
    // PANIC: not_supported() -> "not implemented: this variant is not supported"
    let _ = (in_progress, not_supported); // suppress unused warnings

    let n: u32 = 7;
    let _parity: &str = match n % 2 {
        0 => "even",
        1 => "odd",
        _ => unreachable!("modulo 2 is always 0 or 1"),
    };
    println!("todo!/unimplemented!/unreachable! - panic with descriptive message");

    print_h3!("matches!");
    // matches! expands to a match expression returning bool; supports guards (if x > 0) and | patterns
    let val: Option<i32> = Some(42);
    let is_positive: bool = matches!(val, Some(x) if x > 0);
    println!("matches!(Some(42), Some(x) if x > 0) = {}", is_positive);

    let color: &str = "red";
    let is_warm: bool = matches!(color, "red" | "orange" | "yellow");
    println!("matches!({:?}, red|orange|yellow) = {}", color, is_warm);

    let none_val: Option<i32> = None;
    println!("matches!(None, None) = {}", matches!(none_val, None));

    print_h3!("write! and writeln!");
    // Two Write traits exist: fmt::Write for String/str targets, io::Write for byte streams
    // They must be aliased (as FmtWrite / IoWrite) when both are in scope
    use std::fmt::Write as FmtWrite;
    let mut buf: String = String::new();
    write!(buf, "hello ").unwrap();
    writeln!(buf, "world {}", 42).unwrap();
    println!("String buffer after write!/writeln! = {:?}", buf);

    // Writing to a Vec<u8> with std::io::Write
    use std::io::Write as IoWrite;
    let mut bytes: Vec<u8> = Vec::new();
    write!(bytes, "binary data: {}", 255).unwrap();
    println!(
        "Vec<u8> after write! = {:?}",
        String::from_utf8(bytes).unwrap()
    );

    print_h3!("env! and option_env!");
    // env! reads env vars at compile time - panics if missing
    let pkg: &str = env!("CARGO_PKG_NAME");
    let ver: &str = env!("CARGO_PKG_VERSION");
    println!("env!(CARGO_PKG_NAME) = {}", pkg);
    println!("env!(CARGO_PKG_VERSION) = {}", ver);

    // option_env! returns Option<&str> - no panic if missing
    let maybe: Option<&str> = option_env!("NONEXISTENT_VAR_XYZ");
    println!("option_env!(NONEXISTENT_VAR_XYZ) = {:?}", maybe);

    print_h3!("Compile-time location info (file!, line!, etc.)");
    println!("file!()        = {}", file!());
    println!("line!()        = {}", line!());
    println!("column!()      = {}", column!());
    println!("module_path!() = {}", module_path!());

    print_h3!("concat! and stringify!");
    let combined: &str = concat!("Hello", ", ", "world", "!"); // joins at compile time
    println!("concat!(...) = {}", combined);

    let tokens: &str = stringify!(1 + 2 * 3); // token stream as string literal
    println!("stringify!(1 + 2 * 3) = \"{}\"", tokens);

    print_h3!("cfg!");
    let is_debug: bool = cfg!(debug_assertions);
    println!("cfg!(debug_assertions) = {}", is_debug);
    let is_unix: bool = cfg!(target_family = "unix");
    println!("cfg!(target_family = \"unix\") = {}", is_unix);
    let is_64bit: bool = cfg!(target_pointer_width = "64");
    println!("cfg!(target_pointer_width = \"64\") = {}", is_64bit);

    print_h3!("include family (include!, include_str!, include_bytes!)");
    // include!("file.rs")         - embeds a .rs file as source code
    // include_str!("file.txt")    - embeds file content as &'static str
    // include_bytes!("file.bin")  - embeds file content as &'static [u8]
    // All resolved at compile time relative to the current file
    println!("include_str! / include_bytes! embed files at compile time");

    print_h3!("vec!");
    let v1: Vec<i32> = vec![1, 2, 3];
    let v2: Vec<i32> = vec![0; 10]; // 10 zeros
    println!("vec![1,2,3]  = {:?}", v1);
    println!("vec![0; 10]  = {:?}", v2);

    print_h3!("compile_error!");
    // Used inside cfg blocks to emit a hard compiler error with a custom message
    // #[cfg(not(any(target_os = "linux", target_os = "macos")))]
    // compile_error!("Only Linux and macOS are supported");
    println!("compile_error! produces a build-time error - useful in platform guards");
}
