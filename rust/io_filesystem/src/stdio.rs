use shared::{print_h2, print_h3};
use std::io::{self, Write};

pub fn run() -> io::Result<()> {
    print_h2!("Standard I/O");

    print_h3!("stdout");

    let mut stdout = io::stdout();
    stdout.write_all(b"Writing to stdout\n")?;
    stdout.flush()?; // Ensure output is written

    // print! and println! macros
    print!("This is ");
    println!("stdout");

    print_h3!("stderr");

    let mut stderr = io::stderr();
    stderr.write_all(b"Writing to stderr\n")?;

    // eprint! and eprintln! macros
    eprint!("This is ");
    eprintln!("stderr");

    print_h3!("stdin - reading lines");
    println!("\n=== Stdin Examples (commented out - uncomment to test) ===");

    // Uncomment to test interactive input:
    /*
    println!("Enter your name:");
    let mut name: String = String::new();
    io::stdin().read_line(&mut name)?;
    println!("Hello, {}!", name.trim());
    */

    print_h3!("stdin - reading with BufRead");
    /*
    println!("\nEnter multiple lines (Ctrl+D to finish):");
    let stdin = io::stdin();
    let reader = stdin.lock();

    for line in reader.lines() {
        let line_content: String = line?;
        println!("  You entered: {}", line_content);
    }
    */

    print_h3!("stdin - reading exact amount");
    /*
    println!("\nEnter exactly 5 characters:");
    let mut buffer: [u8; 5] = [0; 5];
    io::stdin().read_exact(&mut buffer)?;
    println!("Read: {:?}", String::from_utf8_lossy(&buffer));
    */

    print_h3!("Buffered stdin");

    println!("\nBuffered stdin example (commented):");
    /*
    let stdin = io::stdin();
    let mut handle = stdin.lock();

    let mut line1: String = String::new();
    handle.read_line(&mut line1)?;

    let mut line2: String = String::new();
    handle.read_line(&mut line2)?;

    println!("Line 1: {}", line1.trim());
    println!("Line 2: {}", line2.trim());
    */

    print_h3!("stdin - parsing input");
    println!("\nParsing input example (commented):");
    /*
    println!("Enter a number:");
    let mut input: String = String::new();
    io::stdin().read_line(&mut input)?;

    match input.trim().parse::<i32>() {
        Ok(num) => println!("You entered: {}", num),
        Err(e) => println!("Parse error: {}", e),
    }
    */

    print_h3!("Reading until EOF");
    /*
    println!("\nEnter text (Ctrl+D to finish):");
    let mut all_input: String = String::new();
    io::stdin().read_to_string(&mut all_input)?;
    println!("Total input: {} bytes", all_input.len());
    */

    print_h3!("Reading single character");
    /*
    println!("\nPress any key:");
    let mut buffer: [u8; 1] = [0; 1];
    io::stdin().read_exact(&mut buffer)?;
    println!("You pressed: {:?}", buffer[0] as char);
    */

    println!("\nStdout vs stderr:");
    println!("This goes to stdout (fd 1)");
    eprintln!("This goes to stderr (fd 2)");

    print_h3!("Formatting output");
    let value: i32 = 42;
    println!("\nFormatted output:");
    println!("Decimal: {}", value);
    println!("Hex: {:x}", value);
    println!("Binary: {:b}", value);
    println!("Padded: {:05}", value);

    print_h3!("Writing bytes vs strings");
    let mut stdout2 = io::stdout();
    stdout2.write_all(b"Raw bytes\n")?;
    writeln!(stdout2, "Formatted with writeln! macro")?;

    print_h3!("Error handling for stdin");
    fn read_number() -> io::Result<i32> {
        println!("Enter a number (example):");
        // Simulating input
        let input: String = String::from("42");

        let num: i32 = input
            .trim()
            .parse()
            .map_err(|e| io::Error::new(io::ErrorKind::InvalidInput, e))?;

        return Ok(num);
    }

    match read_number() {
        Ok(n) => println!("Parsed number: {}", n),
        Err(e) => println!("Error: {}", e),
    }

    print_h3!("Reading with timeout");
    println!("\nTimeout read would require external crate (e.g., crossterm)");

    print_h3!("Redirecting example");
    println!("\n=== Redirection Examples ===");
    println!("Run program with:");
    println!("  ./program > output.txt     # Redirect stdout");
    println!("  ./program 2> errors.txt    # Redirect stderr");
    println!("  ./program < input.txt      # Redirect stdin");
    println!("  ./program | grep 'text'    # Pipe to another program");

    print_h3!("Flushing output");
    print!("This will be flushed immediately...");
    io::stdout().flush()?;
    println!(" Done!");

    print_h3!("Testing for terminal");
    // IsTerminal::is_terminal() detects whether stdout is connected to a real terminal
    // or being piped/redirected. Useful for deciding whether to emit ANSI color codes.
    use std::io::IsTerminal;
    println!("\nIs stdout a terminal? {}", io::stdout().is_terminal());
    println!("Is stderr a terminal? {}", io::stderr().is_terminal());
    println!("Is stdin a terminal? {}", io::stdin().is_terminal());

    print_h3!("Common patterns");

    fn prompt(message: &str) -> io::Result<String> {
        print!("{}", message);
        io::stdout().flush()?; // Flush to show prompt before input

        // In real usage: io::stdin().read_line(&mut input)?;
        let input: String = String::from("mock input"); // Mock for non-interactive

        return Ok(input.trim().to_string());
    }

    let _result: String = prompt("Enter value: ")?;
    println!("(Mock) Got input");

    // Pattern: Reading multiple values
    println!("\nPattern: Reading space-separated values (mock):");
    let mock_line: &str = "10 20 30";
    let numbers: Vec<i32> = mock_line
        .split_whitespace()
        .filter_map(|s| s.parse().ok())
        .collect();
    println!("Parsed numbers: {:?}", numbers);

    return Ok(());
}
