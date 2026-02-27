use shared::{print_h2, print_h3};
use std::fs::{File, OpenOptions};
use std::io::{self, BufRead, BufReader, BufWriter, Read, Seek, SeekFrom, Write};

pub fn run() -> io::Result<()> {
    print_h2!("File I/O");

    let filename: &str = "test_file.txt";

    print_h3!("Creating and writing");
    let mut file: File = File::create(filename)?;
    file.write_all(b"Hello, Rust!\n")?;
    file.write_all(b"Line 2\n")?;
    println!("Created and wrote to {}", filename);

    print_h3!("Reading entire file");
    let content: String = std::fs::read_to_string(filename)?;
    println!("\nFull content:\n{}", content);

    print_h3!("Reading as bytes");
    let bytes: Vec<u8> = std::fs::read(filename)?;
    println!("Read {} bytes", bytes.len());

    print_h3!("OpenOptions");

    let mut file: File = OpenOptions::new()
        .read(true)
        .write(true)
        .create(true)
        .append(false)
        .truncate(false)
        .open("options.txt")?;
    file.write_all(b"OpenOptions example\n")?;
    println!("\nOpenOptions file created");

    let mut file: File = OpenOptions::new().append(true).open(filename)?;
    writeln!(file, "Appended line")?;
    println!("Appended to file");

    print_h3!("BufReader");

    // BufReader wraps any Read in an 8KB buffer.
    // Without it, every read_line() would call the syscall separately — very slow.
    // BufReader<File> is a newtype that impls BufRead, giving access to .lines() and .read_line().
    let file: File = File::open(filename)?;
    let reader: BufReader<File> = BufReader::new(file);

    println!("\nBufReader lines:");
    for (i, line) in reader.lines().enumerate() {
        let line_content: String = line?;
        println!("  Line {}: {}", i + 1, line_content);
    }

    let file: File = File::open(filename)?;
    let mut reader: BufReader<File> = BufReader::new(file);
    let mut line: String = String::new();
    let bytes_read: usize = reader.read_line(&mut line)?;
    println!("\nFirst line ({} bytes): {}", bytes_read, line.trim());

    print_h3!("BufWriter");

    let file: File = File::create("buffered.txt")?;
    let mut writer: BufWriter<File> = BufWriter::new(file);

    for i in 0..5 {
        writeln!(writer, "Buffered line {}", i)?;
    }
    writer.flush()?; // Ensure all data is written
    println!("\nBufWriter wrote 5 lines");

    print_h3!("Read trait methods");
    let mut file: File = File::open(filename)?;

    let mut buffer: [u8; 10] = [0; 10];
    let n: usize = file.read(&mut buffer)?;
    println!("\nRead {} bytes: {:?}", n, &buffer[..n]);

    let mut file: File = File::open(filename)?;
    let mut exact_buf: [u8; 5] = [0; 5];
    file.read_exact(&mut exact_buf)?;
    println!("Read exact 5 bytes: {:?}", exact_buf);

    let mut file: File = File::open(filename)?;
    let mut contents: Vec<u8> = Vec::new();
    let bytes: usize = file.read_to_end(&mut contents)?;
    println!("Read to end: {} bytes total", bytes);

    let mut file: File = File::open(filename)?;
    let mut text: String = String::new();
    file.read_to_string(&mut text)?;
    println!("Read as string: {} chars", text.len());

    print_h3!("Seeking (file positioning)");
    // Seek requires the Seek trait in scope. SeekFrom has three variants:
    // Start(n) = absolute offset from beginning, Current(n) = relative to cursor, End(n) = from EOF.
    // SeekFrom::End(-5) means "5 bytes before the end".
    let mut file: File = File::open(filename)?;

    // Seek to start
    file.seek(SeekFrom::Start(0))?;
    println!("\nSeeked to start");

    // Seek relative to current position
    file.seek(SeekFrom::Current(5))?;
    let mut buf: [u8; 5] = [0; 5];
    file.read_exact(&mut buf)?;
    println!("After seeking +5: {:?}", String::from_utf8_lossy(&buf));

    // Seek from end (negative offset)
    file.seek(SeekFrom::End(-5))?;
    println!("Seeked to 5 bytes from end");

    // stream_position() - get current position
    let pos: u64 = file.stream_position()?;
    println!("Current position: {}", pos);

    file.rewind()?;
    println!("Rewound to start");

    print_h3!("Writing methods");
    let mut file: File = File::create("write_methods.txt")?;

    // write() - writes bytes, returns count
    let written: usize = file.write(b"Hello")?;
    println!("\nWrote {} bytes", written);

    // write_all() - writes all or error
    file.write_all(b" World")?;
    println!("Write_all succeeded");

    // write! and writeln! macros
    writeln!(file, "\nFormatted: {}", 42)?;
    write!(file, "No newline")?;
    println!("Format macros used");

    print_h3!("File metadata during I/O");
    let file: File = File::open(filename)?;
    let metadata: std::fs::Metadata = file.metadata()?;
    println!("\nFile metadata:");
    println!("  Size: {} bytes", metadata.len());
    println!("  Read-only: {}", metadata.permissions().readonly());

    print_h3!("try_clone");
    // Clone file handle (shares position)
    let file: File = File::open(filename)?;
    let mut file_clone: File = file.try_clone()?;
    let mut content1: String = String::new();
    file_clone.read_to_string(&mut content1)?;
    println!("\nCloned file handle read: {} chars", content1.len());

    print_h3!("Reading specific ranges");
    let mut file: File = File::open(filename)?;
    file.seek(SeekFrom::Start(6))?;
    let mut range_buf: Vec<u8> = vec![0; 4];
    file.read_exact(&mut range_buf)?;
    println!("\nRange [6..10]: {}", String::from_utf8_lossy(&range_buf));

    print_h3!("Error handling patterns");
    match File::open("nonexistent.txt") {
        Ok(_) => println!("\nFile opened"),
        Err(e) => println!("Error opening file: {} (kind: {:?})", e, e.kind()),
    }

    print_h3!("Cleanup");
    std::fs::remove_file(filename)?;
    std::fs::remove_file("options.txt")?;
    std::fs::remove_file("buffered.txt")?;
    std::fs::remove_file("write_methods.txt")?;
    println!("\nCleaned up test files");

    return Ok(());
}
