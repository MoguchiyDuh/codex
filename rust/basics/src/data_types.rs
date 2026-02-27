use shared::{get_type, print_h2, print_h3};

pub fn run() {
    print_h2!("Data Types");

    print_h3!("Signed integers");
    let i8_val: i8 = 127;
    let i16_val: i16 = 32_767;
    let i32_val: i32 = 2_147_483_647;
    let i64_val: i64 = 9_223_372_036_854_775_807;
    let i128_val: i128 = 170_141_183_460_469_231_731_687_303_715_884_105_727;
    println!("i8: {} (min: {}, max: {})", i8_val, i8::MIN, i8::MAX);
    println!("i16: {} (min: {}, max: {})", i16_val, i16::MIN, i16::MAX);
    println!("i32: {} (min: {}, max: {})", i32_val, i32::MIN, i32::MAX);
    println!("i64: {} ({})", i64_val, get_type(&i64_val));
    println!("i128: {} ({})", i128_val, get_type(&i128_val));

    // isize/usize are pointer-sized: 32-bit on 32-bit platforms, 64-bit on 64-bit platforms
    let isize_val: isize = 100;
    println!(
        "isize: {} (ptr-sized, {} bits)",
        isize_val,
        std::mem::size_of::<isize>() * 8
    );

    print_h3!("Unsigned integers");
    let u8_val: u8 = 255;
    let u16_val: u16 = 65_535;
    let u32_val: u32 = 4_294_967_295;
    let u64_val: u64 = 18_446_744_073_709_551_615;
    let u128_val: u128 = 340_282_366_920_938_463_463_374_607_431_768_211_455;
    println!("u8: {} (min: {}, max: {})", u8_val, u8::MIN, u8::MAX);
    println!("u16: {} (min: {}, max: {})", u16_val, u16::MIN, u16::MAX);
    println!("u32: {} ({})", u32_val, get_type(&u32_val));
    println!("u64: {} ({})", u64_val, get_type(&u64_val));
    println!("u128: {} ({})", u128_val, get_type(&u128_val));

    let usize_val: usize = 200;
    println!(
        "usize: {} (ptr-sized, {} bits)",
        usize_val,
        std::mem::size_of::<usize>() * 8
    );

    print_h3!("Floats");
    let f32_val: f32 = 3.14159;
    let f64_val: f64 = 2.718281828459045;
    println!("f32: {} ({})", f32_val, get_type(&f32_val));
    println!("f64: {} ({})", f64_val, get_type(&f64_val));

    // NaN != NaN (IEEE 754): use .is_nan() to check; f32/f64 implement PartialEq, not Eq
    let nan: f64 = f64::NAN;
    let inf: f64 = f64::INFINITY;
    let neg_inf: f64 = f64::NEG_INFINITY;
    println!("NaN: {}, is_nan: {}", nan, nan.is_nan());
    println!("Infinity: {}, is_infinite: {}", inf, inf.is_infinite());
    println!("Neg Infinity: {}", neg_inf);

    print_h3!("Boolean");
    let bool_true: bool = true;
    let bool_false: bool = false;
    println!(
        "bool: {} {} ({})",
        bool_true,
        bool_false,
        get_type(&bool_true)
    );
    println!("Size: {} byte", std::mem::size_of::<bool>());

    print_h3!("Char (4 bytes, Unicode)");
    // char is a Unicode scalar value (U+0000..=U+10FFFF), always 4 bytes — not UTF-8 encoded
    let ch_ascii: char = 'A';
    let ch_unicode: char = '😀';
    let ch_escape: char = '\n';
    println!(
        "char: '{}' '{}' ({})",
        ch_ascii,
        ch_unicode,
        get_type(&ch_ascii)
    );
    println!(
        "Char size: {} bytes (Unicode scalar)",
        std::mem::size_of::<char>()
    );
    println!("Escape sequence '\\n': {:?}", ch_escape);

    print_h3!("Tuples");
    let tuple2: (i32, f64) = (42, 3.14);
    let tuple3: (i32, &str, bool) = (1, "hello", true);
    let unit: () = ();
    println!("Tuple (i32, f64): {:?}", tuple2);
    println!("Tuple access: .0={} .1={}", tuple2.0, tuple2.1);
    println!("Tuple3: {:?}", tuple3);
    println!("Unit type: {:?} ({})", unit, get_type(&unit));

    let (a, b, c) = tuple3; // Destructuring
    println!("Destructured: a={} b={} c={}", a, b, c);

    print_h3!("Arrays (fixed size)");
    let arr_i32: [i32; 5] = [1, 2, 3, 4, 5];
    let arr_repeat: [i32; 3] = [0; 3];
    println!("Array: {:?} ({})", arr_i32, get_type(&arr_i32));
    println!("Repeat array: {:?}", arr_repeat);
    println!("Array size: {} bytes", std::mem::size_of_val(&arr_i32));

    print_h3!("Numeric literals");
    let decimal: i32 = 98_222;
    let hex: i32 = 0xff;
    let octal: i32 = 0o77;
    let binary: i32 = 0b1111_0000;
    let byte: u8 = b'A'; // ASCII byte
    println!(
        "Literals: dec={} hex={:#x} oct={:#o} bin={:#b} byte={} (as char: '{}')",
        decimal, hex, octal, binary, byte, byte as char
    );

    print_h3!("Type inference");
    let inferred = 42; // Defaults to i32
    println!("Inferred: {} ({})", inferred, get_type(&inferred));

    let inferred_float = 3.14; // Defaults to f64
    println!(
        "Inferred float: {} ({})",
        inferred_float,
        get_type(&inferred_float)
    );

    print_h3!("Type aliases");
    type Kilometers = i32;
    let distance: Kilometers = 100;
    println!(
        "Type alias Kilometers: {} ({})",
        distance,
        get_type(&distance)
    );

    print_h3!("Overflow behavior");
    // The following would cause a COMPILE-TIME ERROR because it's a literal constant overflow:
    // let overflowed = 255_u8 + 1;
    // println!("Overflowed add 255+1: {}", overflowed);
    //
    // Note: Rust panics on overflow in debug mode at runtime, but wraps in release mode.
    // To handle overflow explicitly, use the following methods:

    let wrapping: u8 = 255_u8.wrapping_add(1);
    println!("Wrapping add 255+1: {}", wrapping);

    let checked: Option<u8> = 255_u8.checked_add(1);
    println!("Checked add 255+1: {:?}", checked);
    // PANIC: In debug mode, 255_u8 + 1 would panic (overflow check enabled)

    let saturating: u8 = 255_u8.saturating_add(1);
    println!("Saturating add 255+1: {}", saturating);

    let overflowing: (u8, bool) = 255_u8.overflowing_add(1);
    println!(
        "Overflowing add 255+1: value={} overflow={}",
        overflowing.0, overflowing.1
    );

    print_h3!("Type sizes");
    println!("Size of i8: {} bytes", std::mem::size_of::<i8>());
    println!("Size of i32: {} bytes", std::mem::size_of::<i32>());
    println!("Size of f64: {} bytes", std::mem::size_of::<f64>());
    println!("Size of char: {} bytes", std::mem::size_of::<char>());
    println!("Size of &str: {} bytes", std::mem::size_of::<&str>());
}
