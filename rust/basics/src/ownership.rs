use shared::{print_h2, print_h3};

pub fn run() {
    print_h2!("Ownership & Borrowing");

    print_h3!("Move semantics (heap types)");
    // String owns heap memory; it cannot implement Copy because that would allow
    // two owners of the same heap allocation (double-free on drop)
    let s1: String = String::from("hello");
    let s2: String = s1; // Ownership transferred to s2 — s1 is now uninitialized
    println!("s2: {}", s2);
    // ERROR: s1 is now invalid (moved)
    // println!("{}", s1); // Would fail: "borrow of moved value"

    print_h3!("Copy trait (stack types)");
    // Primitive types implement Copy, so assignment copies the value
    let x: i32 = 42;
    let y: i32 = x; // x is copied, both remain valid
    println!("x: {}, y: {}", x, y); // Both accessible

    // Types that implement Copy: all integers, floats, bool, char, tuples of Copy types
    let tuple: (i32, bool) = (10, true);
    let tuple2: (i32, bool) = tuple; // Copied
    println!("Both tuples valid: {:?} {:?}", tuple, tuple2);

    print_h3!("Clone (explicit deep copy)");
    let s3: String = String::from("data");
    let s4: String = s3.clone(); // Explicit heap allocation copy
    println!("s3: {}, s4: {}", s3, s4); // Both valid, separate heap allocations

    print_h3!("Immutable borrowing");
    // & creates an immutable reference (borrow), doesn't transfer ownership
    let s5: String = String::from("borrowed");
    let r1: &String = &s5;
    let r2: &String = &s5;
    let r3: &String = &s5; // Multiple immutable borrows OK
    println!("r1: {}, r2: {}, r3: {}", r1, r2, r3);
    println!("s5 still valid: {}", s5); // Original still accessible

    print_h3!("Mutable borrowing");
    // &mut creates a mutable reference
    // RULE: Can have EITHER multiple immutable refs OR one mutable ref, never both
    let mut s6: String = String::from("mutable");
    let r_mut: &mut String = &mut s6;
    r_mut.push_str(" modified");
    println!("r_mut: {}", r_mut);
    // ERROR: Can't use s6 while mutable borrow exists
    // println!("{}", s6); // Would fail: "cannot borrow as immutable"

    // NLL (Non-Lexical Lifetimes): borrow ends at the last USE, not end of block
    // So r_mut's borrow ends after the println above, allowing s6 to be used again
    println!("s6 after r_mut last used: {}", s6); // Now accessible

    print_h3!("Borrow checker rules");
    let mut s7: String = String::from("test");
    let r_imm1: &String = &s7;
    let r_imm2: &String = &s7; // Multiple immutable OK
    println!("{} {}", r_imm1, r_imm2);
    // ERROR: Can't create mutable borrow while immutable borrows exist
    // let r_mut2 = &mut s7; // Would fail
    // println!("{}", r_imm1); // Would fail if r_mut2 existed

    // After immutable borrows are done, mutable is OK
    let r_mut3: &mut String = &mut s7;
    r_mut3.push_str("!");
    println!("Now mutable is OK: {}", r_mut3);

    print_h3!("Function ownership transfer");
    let s8: String = String::from("transferred");
    takes_ownership(s8); // s8 moved into function
    // ERROR: s8 no longer valid
    // println!("{}", s8); // Would fail: "borrow of moved value"

    let x2: i32 = 5;
    makes_copy(x2); // x2 is copied (implements Copy)
    println!("x2 still valid: {}", x2); // Still accessible

    print_h3!("Function borrowing");
    let s9: String = String::from("borrowed string");
    let len: usize = calculate_length(&s9); // Borrow, don't move
    println!("Length of '{}' is {}", s9, len); // s9 still valid

    let mut s10: String = String::from("mutable borrow");
    change(&mut s10); // Mutable borrow
    println!("After change: {}", s10);

    print_h3!("Return values transfer ownership");
    let s11: String = gives_ownership(); // Function returns ownership
    println!("Received ownership: {}", s11);

    let s12: String = String::from("yours");
    let s13: String = takes_and_gives_back(s12); // Takes and returns ownership
    // ERROR: s12 is moved
    // println!("{}", s12); // Would fail
    println!("Got back: {}", s13);

    print_h3!("Scope and dropping");
    {
        let s_scoped: String = String::from("scoped");
        println!("Inside scope: {}", s_scoped);
    } // s_scoped dropped here (memory freed)
    // ERROR: s_scoped no longer exists
    // println!("{}", s_scoped); // Would fail: "not found in this scope"

    print_h3!("Explicit drop()");
    // Manually drop owned value before end of scope
    let s_drop: String = String::from("will be dropped early");
    println!("Before drop: {}", s_drop);
    drop(s_drop); // Explicitly free memory NOW
    // ERROR: s_drop is now invalid
    // println!("{}", s_drop); // Would fail: "borrow of moved value"

    // Useful when holding large data or locks
    let large: Vec<i32> = vec![1; 1000];
    println!("Have large vec, len: {}", large.len());
    drop(large); // Free memory immediately
    println!("Large vec dropped, memory freed");

    print_h3!("Dangling reference prevention");
    // Rust prevents dangling references at compile time
    // ERROR: This function would not compile:
    // fn dangle() -> &String {
    //     let s = String::from("dangling");
    //     &s // ERROR: s dropped, would return reference to freed memory
    // }

    // Correct: return owned String
    let valid: String = no_dangle();
    println!("Valid string: {}", valid);

    print_h3!("Slices (special references)");
    let text: String = String::from("hello world");
    // &str is a fat pointer: (ptr, len) — it borrows a UTF-8 byte range of the String
    // Indexing must fall on valid UTF-8 character boundaries, or it panics at runtime
    let hello: &str = &text[0..5]; // Slice borrows part of String
    let world: &str = &text[6..11];
    println!("Slices: '{}' '{}'", hello, world);
    println!("Original still valid: {}", text);

    print_h3!("Copy vs Move examples");
    let arr: [i32; 3] = [1, 2, 3]; // Arrays of Copy types implement Copy
    let arr2: [i32; 3] = arr; // Copied
    println!("Both arrays valid: {:?} {:?}", arr, arr2);

    let vec: Vec<i32> = vec![1, 2, 3]; // Vec doesn't implement Copy
    let vec2: Vec<i32> = vec; // Moved
    // ERROR: vec is moved
    // println!("{:?}", vec); // Would fail
    println!("vec2: {:?}", vec2);

    print_h3!("Common patterns");
    // Pattern: Clone when you need independent copies
    let original: String = String::from("original");
    let backup: String = original.clone();
    do_something_with(original); // original moved
    println!("Still have backup: {}", backup);

    // Pattern: Borrow when you don't need ownership
    let data: String = String::from("data");
    process_ref(&data); // Borrow
    process_ref(&data); // Can borrow again
    println!("data still usable: {}", data);

    // Pattern: Return ownership from functions
    let mut result: String = String::new();
    result = build_string(result); // Take and return ownership
    println!("Built string: {}", result);
}

fn takes_ownership(s: String) {
    println!("  takes_ownership: {}", s);
    // s dropped here
}

fn makes_copy(x: i32) {
    println!("  makes_copy: {}", x);
}

fn calculate_length(s: &String) -> usize {
    return s.len();
    // s not dropped (borrowed, not owned)
}

fn change(s: &mut String) {
    s.push_str(" changed");
}

fn gives_ownership() -> String {
    let s: String = String::from("yours");
    return s; // Ownership transferred to caller
}

fn takes_and_gives_back(s: String) -> String {
    return s; // Takes ownership and gives it back
}

fn no_dangle() -> String {
    let s: String = String::from("hello");
    return s; // Return ownership, not reference
}

fn do_something_with(s: String) {
    println!("  Processing: {}", s);
}

fn process_ref(s: &String) {
    println!("  Processing ref: {}", s);
}

fn build_string(mut s: String) -> String {
    s.push_str(" built");
    return s;
}
