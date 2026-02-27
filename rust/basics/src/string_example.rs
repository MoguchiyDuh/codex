use shared::{print_h2, print_h3};

pub fn run() {
    print_h2!("Strings");

    print_h3!("String vs &str");
    // String: heap-allocated, growable, owned
    let owned: String = String::from("owned");
    // &str: string slice, borrowed, can be static or borrowed from String
    let borrowed: &str = "borrowed"; // String literal (static)
    let slice: &str = &owned[0..3]; // Slice borrows from String
    println!(
        "String: '{}', &str: '{}', slice: '{}'",
        owned, borrowed, slice
    );

    print_h3!("Creation");
    let s1: String = String::from("from");
    let s2: String = "to_string".to_string();
    let s3: String = String::new(); // Empty
    let s4: String = "into".into();
    println!("Created: '{}' '{}' '{}' '{}'", s1, s2, s3, s4);

    print_h3!("Capacity vs length");
    let mut s: String = String::with_capacity(10);
    println!("capacity: {}, len: {}", s.capacity(), s.len());
    s.push_str("hello");
    println!("After push: capacity: {}, len: {}", s.capacity(), s.len());

    print_h3!("Appending");
    let mut text: String = String::from("Hello");
    text.push_str(", world"); // Append &str
    text.push('!'); // Append char
    println!("Appended: '{}'", text);

    print_h3!("Concatenation");
    let s1: String = String::from("Hello");
    let s2: String = String::from(" world");
    // + calls Add::add(self, &str): s1 is moved (fn takes ownership), s2 is borrowed via Deref
    let s3: String = s1 + &s2; // s1 moved, s2 borrowed
    // ERROR: s1 is moved
    // println!("{}", s1); // Would fail
    println!("Concat: '{}'", s3);

    let a: String = String::from("a");
    let b: String = String::from("b");
    let c: String = format!("{}{}", a, b); // Doesn't move, borrows both
    println!("format!: '{}', a still valid: '{}'", c, a);

    print_h3!("Slicing (UTF-8 boundaries)");
    let hello: String = String::from("hello");
    let slice1: &str = &hello[0..2];
    println!("Slice [0..2]: '{}'", slice1);
    // PANIC: Slicing must be on char boundaries
    // let bad = &hello[0..1]; // 'h' is 1 byte, OK
    // let emoji = String::from("😀");
    // let bad_slice = &emoji[0..1]; // PANIC: invalid UTF-8 boundary

    print_h3!("Querying");
    let text2: String = String::from("hello world");
    println!("len (bytes): {}", text2.len());
    println!("is_empty: {}", text2.is_empty());
    println!("contains('world'): {}", text2.contains("world"));
    println!("starts_with('hello'): {}", text2.starts_with("hello"));
    println!("ends_with('world'): {}", text2.ends_with("world"));

    print_h3!("Finding");
    let pos: Option<usize> = text2.find("world");
    println!("find('world'): {:?}", pos);

    let rpos: Option<usize> = text2.rfind('o');
    println!("rfind('o'): {:?}", rpos);

    print_h3!("Case transformations");
    println!("to_uppercase: '{}'", text2.to_uppercase());
    println!("to_lowercase: '{}'", text2.to_lowercase());

    print_h3!("Trimming");
    let padded: &str = "  spaces  ";
    println!("trim: '{}'", padded.trim());
    println!("trim_start: '{}'", padded.trim_start());
    println!("trim_end: '{}'", padded.trim_end());

    let custom: &str = "xxxdataxxx";
    println!("trim_matches('x'): '{}'", custom.trim_matches('x'));

    print_h3!("Splitting");
    let csv: &str = "a,b,c,d";
    let parts: Vec<&str> = csv.split(',').collect();
    println!("split(','): {:?}", parts);

    let whitespace: &str = "one two  three";
    let words: Vec<&str> = whitespace.split_whitespace().collect();
    println!("split_whitespace: {:?}", words);

    let lines: &str = "line1\nline2\nline3";
    let line_vec: Vec<&str> = lines.lines().collect();
    println!("lines: {:?}", line_vec);

    print_h3!("Replacing");
    let original: String = String::from("hello hello");
    let replaced: String = original.replace("hello", "hi");
    println!("replace: '{}'", replaced);

    let replaced_n: String = original.replacen("hello", "hi", 1);
    println!("replacen(n=1): '{}'", replaced_n);

    print_h3!("Iterating chars");
    let text3: String = String::from("Rust");
    print!("chars: ");
    for ch in text3.chars() {
        print!("'{}' ", ch);
    }
    println!();

    print_h3!("Iterating bytes");
    print!("bytes: ");
    for byte in text3.bytes() {
        print!("{} ", byte);
    }
    println!();

    print_h3!("Char indices");
    let emoji_text: String = String::from("a😀b");
    // char_indices yields (byte_offset, char) - byte offsets are not char indices
    for (i, ch) in emoji_text.char_indices() {
        println!("char_indices: [{}] = '{}'", i, ch);
    }
    println!("Byte length: {}", emoji_text.len()); // 7 bytes (a=1, emoji=4, b=1) — NOT char count

    print_h3!("Pattern matching");
    let text4: String = String::from("rust programming");
    if text4.contains("rust") {
        println!("Contains 'rust'");
    }

    match text4.as_str() {
        "rust programming" => println!("Match: exact"),
        _ => println!("Match: other"),
    }

    print_h3!("Mutation");
    let mut s_mut: String = String::from("mutable");
    s_mut.push_str(" text");
    println!("Mutated: '{}'", s_mut);

    s_mut.truncate(7); // Keep first 7 bytes
    println!("Truncated: '{}'", s_mut);

    s_mut.clear();
    println!("Cleared: '{}' (is_empty: {})", s_mut, s_mut.is_empty());

    print_h3!("Conversion to/from bytes");
    let text5: String = String::from("bytes");
    let byte_vec: Vec<u8> = text5.clone().into_bytes();
    println!("into_bytes: {:?}", byte_vec);

    let from_bytes: String = String::from_utf8(byte_vec).unwrap();
    println!("from_utf8: '{}'", from_bytes);

    let as_bytes_ref: &[u8] = text5.as_bytes();
    println!("as_bytes (ref): {:?}", as_bytes_ref);

    print_h3!("Formatting");
    let name: &str = "Alice";
    let age: i32 = 30;
    let formatted: String = format!("{} is {} years old", name, age);
    println!("format!: '{}'", formatted);

    let debug_fmt: String = format!("{:?}", vec![1, 2, 3]);
    println!("format debug: '{}'", debug_fmt);

    print_h3!("Repeat");
    let repeated: String = "ha".repeat(3);
    println!("repeat(3): '{}'", repeated);

    print_h3!("Comparison");
    let a_str: String = String::from("abc");
    let b_str: String = String::from("abd");
    println!("'abc' < 'abd': {}", a_str < b_str);
    println!("'abc' == 'abc': {}", a_str == "abc"); // Can compare with &str
}
