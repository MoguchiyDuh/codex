use shared::{print_h2, print_h3};
use std::io::{self, BufRead, Write};

pub fn run() {
    print_h2!("Standard Input");

    print_h3!("Simulated input (non-interactive)");
    let simulated_line: &str = "42";
    let simulated_multi: &str = "10 20 30";
    let simulated_lines: &str = "line1\nline2\nline3";

    print_h3!("Basic string input");
    println!("Pattern: Reading a line");
    println!("  let mut input = String::new();");
    println!("  io::stdin().read_line(&mut input).unwrap();");
    println!("Simulated: '{}'", simulated_line);

    print_h3!("Parsing to number");
    let parsed: Result<i32, _> = simulated_line.trim().parse();
    match parsed {
        Ok(num) => println!("Parsed i32: {}", num),
        Err(e) => println!("Parse error: {}", e),
    }

    let parsed_f64: f64 = simulated_line.trim().parse().unwrap_or(0.0);
    println!("Parsed f64: {}", parsed_f64);

    print_h3!("Multiple inputs (whitespace-separated)");
    let parts: Vec<&str> = simulated_multi.trim().split_whitespace().collect();
    println!("Split '{}' -> {:?}", simulated_multi, parts);

    let numbers: Vec<i32> = parts.iter().filter_map(|s: &&str| s.parse().ok()).collect();
    println!("Parsed numbers: {:?}", numbers);

    let (a, b, c): (i32, i32, i32) = (
        parts
            .get(0)
            .and_then(|s: &&str| s.parse().ok())
            .unwrap_or(0),
        parts
            .get(1)
            .and_then(|s: &&str| s.parse().ok())
            .unwrap_or(0),
        parts
            .get(2)
            .and_then(|s: &&str| s.parse().ok())
            .unwrap_or(0),
    );
    println!("Destructured: a={} b={} c={}", a, b, c);

    print_h3!("Reading multiple lines");
    let lines: Vec<&str> = simulated_lines.lines().collect();
    println!("Lines: {:?}", lines);

    print_h3!("BufReader pattern");
    println!("\nPattern: BufReader for efficient reading");
    println!("  use std::io::{{BufRead, BufReader}};");
    println!("  let reader = BufReader::new(io::stdin());");
    println!("  for line in reader.lines() {{");
    println!("    let line = line.unwrap();");
    println!("  }}");

    let cursor: io::Cursor<&str> = io::Cursor::new(simulated_lines);
    let reader: io::BufReader<io::Cursor<&str>> = io::BufReader::new(cursor);
    let line_count: usize = reader.lines().count();
    println!("BufReader line count: {}", line_count);

    print_h3!("stdout/stderr");
    print!("print! (no newline) ");
    println!("println! (with newline)");

    io::stdout().flush().unwrap();
    eprintln!("eprintln! goes to stderr");

    let mut stdout_handle: io::Stdout = io::stdout();
    write!(stdout_handle, "write! macro ").unwrap();
    writeln!(stdout_handle, "writeln! macro").unwrap();
    stdout_handle.flush().unwrap();

    print_h3!("Command-line args (env::args)");
    println!("\nPattern: Command-line arguments");
    println!("  use std::env;");
    println!("  let args: Vec<String> = env::args().collect();");

    let args: Vec<String> = std::env::args().collect();
    println!("Current args: {:?}", args);
    println!(
        "Program name: {}",
        args.get(0).map_or("none", |s: &String| s.as_str())
    );

    print_h3!("Formatted parsing");
    let formatted: &str = "name:John age:30";
    let parts_colon: Vec<&str> = formatted.split_whitespace().collect();
    for part in parts_colon {
        let kv: Vec<&str> = part.split(':').collect();
        if kv.len() == 2 {
            println!("Key='{}' Value='{}'", kv[0], kv[1]);
        }
    }

    print_h3!("Error handling patterns");
    let bad_input: &str = "not_a_number";
    match bad_input.parse::<i32>() {
        Ok(n) => println!("Parsed: {}", n),
        Err(e) => println!("Parse error: {}", e),
    }

    let with_expect: Result<i32, _> = "123".parse();
    let unwrapped: i32 = with_expect.expect("Failed to parse");
    println!("expect unwrapped: {}", unwrapped);
    // PANIC: "abc".parse::<i32>().expect("msg") would panic with custom message

    let with_default: i32 = "abc".parse().unwrap_or(-1);
    println!("unwrap_or default: {}", with_default);

    print_h3!("Reading until EOF pattern");
    println!("\nPattern: Read until EOF");
    println!("  let mut buffer = String::new();");
    println!("  io::stdin().read_to_string(&mut buffer).unwrap();");

    let mut eof_buffer: String = String::new();
    let mut eof_reader: io::Cursor<&str> = io::Cursor::new("all\ndata\nhere");
    io::Read::read_to_string(&mut eof_reader, &mut eof_buffer).unwrap();
    println!("Read to string: {:?}", eof_buffer);

    print_h3!("Input validation");
    fn validate_positive(input: &str) -> Result<i32, String> {
        let num: i32 = input
            .trim()
            .parse()
            .map_err(|_| "Not a number".to_string())?;
        if num <= 0 {
            return Err("Must be positive".to_string());
        }
        return Ok(num);
    }

    println!("validate_positive('10'): {:?}", validate_positive("10"));
    println!("validate_positive('-5'): {:?}", validate_positive("-5"));
    println!("validate_positive('abc'): {:?}", validate_positive("abc"));
}
