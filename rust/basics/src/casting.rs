use shared::{get_type, print_h2, print_h3};
use std::convert::TryInto;

pub fn run() {
    print_h2!("Casting");

    print_h3!("Numeric as-casting");
    let i8_val: i8 = 42;
    let i16_val: i16 = i8_val as i16;
    let i32_val: i32 = i8_val as i32;
    let i64_val: i64 = i8_val as i64;
    let i128_val: i128 = i8_val as i128;
    println!(
        "i8 {} -> i16:{} i32:{} i64:{} i128:{}",
        i8_val, i16_val, i32_val, i64_val, i128_val
    );

    let u8_val: u8 = 100;
    let u16_val: u16 = u8_val as u16;
    let u32_val: u32 = u8_val as u32;
    let u64_val: u64 = u8_val as u64;
    let u128_val: u128 = u8_val as u128;
    println!(
        "u8 {} -> u16:{} u32:{} u64:{} u128:{}",
        u8_val, u16_val, u32_val, u64_val, u128_val
    );

    let f32_val: f32 = i32_val as f32;
    let f64_val: f64 = i32_val as f64;
    println!("i32 {} -> f32:{} f64:{}", i32_val, f32_val, f64_val);

    let isize_val: isize = i32_val as isize;
    let usize_val: usize = u32_val as usize;
    println!(
        "isize:{} usize:{} ({})",
        isize_val,
        usize_val,
        get_type(&usize_val)
    );

    print_h3!("Lossy conversions");
    let float: f64 = 3.9999;
    let truncated: i32 = float as i32;
    println!("f64 {} as i32 (truncate): {}", float, truncated);

    // as-casting between signed/unsigned reinterprets the bits; -1i8 is 0xFF => 255u8
    let signed: i8 = -1;
    let as_unsigned: u8 = signed as u8;
    println!("i8 {} as u8 (bit reinterpret): {}", signed, as_unsigned);

    let large_unsigned: u16 = 256;
    let small: u8 = large_unsigned as u8; // Wraps
    println!("u16 {} as u8 (wrap): {}", large_unsigned, small);

    print_h3!("Checked conversions (TryInto)");
    let big: i32 = 300;
    let checked: Result<i8, _> = big.try_into();
    println!("i32 {} try_into i8: {:?}", big, checked);

    let ok_val: i32 = 100;
    let checked_ok: Result<i8, _> = ok_val.try_into();
    println!("i32 {} try_into i8: {:?}", ok_val, checked_ok);

    print_h3!("From/Into traits");
    // Implementing From<T> auto-implements Into<U>; these are infallible by contract
    let from_u8: u32 = u32::from(u8_val);
    println!("u32::from(u8 {}): {}", u8_val, from_u8);

    let into_u64: u64 = u8_val.into();
    println!("u8 {}.into() u64: {}", u8_val, into_u64);

    print_h3!("String parsing");
    let str_num: &str = "12345";
    let parsed_i32: i32 = str_num.parse().expect("parse i32");
    let parsed_f64: f64 = str_num.parse().expect("parse f64");
    println!("'{}' -> i32:{} f64:{}", str_num, parsed_i32, parsed_f64);

    let bad_str: &str = "abc";
    let parse_fail: Result<i32, _> = bad_str.parse();
    println!("'{}' -> {:?}", bad_str, parse_fail);

    print_h3!("To string");
    let num: i32 = 9876;
    let as_string: String = num.to_string();
    println!(
        "i32 {} -> String '{}' ({})",
        num,
        as_string,
        get_type(&as_string)
    );

    let formatted: String = format!("{:#x}", num); // Hex format
    println!("Formatted hex: {}", formatted);

    print_h3!("Char/byte conversions");
    let ch: char = 'A';
    let byte: u8 = ch as u8;
    println!("char '{}' as u8: {}", ch, byte);

    let back_to_char: char = byte as char;
    println!("u8 {} as char: '{}'", byte, back_to_char);

    let unicode: char = '😀';
    let unicode_val: u32 = unicode as u32;
    println!("char '{}' as u32: {}", unicode, unicode_val);

    print_h3!("Bool conversions");
    let truthy: bool = true;
    let falsy: bool = false;
    let true_int: i32 = truthy as i32;
    let false_int: i32 = falsy as i32;
    println!(
        "bool true as i32: {}, false as i32: {}",
        true_int, false_int
    );

    print_h3!("Safe bitwise conversions");
    let float_bits: f32 = 1.5;
    let bits: u32 = float_bits.to_bits();
    println!("f32 {} to bits: {:#x}", float_bits, bits);

    let back: f32 = f32::from_bits(bits);
    println!("u32 {:#x} back to f32: {}", bits, back);

    print_h3!("Array conversions");
    let arr: [u8; 4] = [1, 2, 3, 4];
    let as_u32_le: u32 = u32::from_le_bytes(arr);
    let as_u32_be: u32 = u32::from_be_bytes(arr);
    println!("bytes {:?} -> u32 LE:{} BE:{}", arr, as_u32_le, as_u32_be);

    let back_le: [u8; 4] = as_u32_le.to_le_bytes();
    let back_be: [u8; 4] = as_u32_le.to_be_bytes();
    println!("u32 {} -> LE:{:?} BE:{:?}", as_u32_le, back_le, back_be);

    print_h3!("String <-> bytes");
    let text: &str = "Hello";
    let bytes: &[u8] = text.as_bytes();
    println!("str '{}' -> bytes: {:?}", text, bytes);

    let from_bytes: &str = std::str::from_utf8(bytes).expect("valid utf8");
    println!("bytes {:?} -> str: '{}'", bytes, from_bytes);

    let invalid_utf8: Vec<u8> = vec![0xFF, 0xFE, 0xFD];
    let lossy: std::borrow::Cow<str> = String::from_utf8_lossy(&invalid_utf8); // Cow = Clone on Write: borrows if valid, clones if needs replacement
    println!("invalid bytes {:?} -> lossy: '{}'", invalid_utf8, lossy);
    // PANIC: std::str::from_utf8(&invalid_utf8).unwrap() would panic on invalid UTF-8

    let owned_string: String = String::from("owned");
    let into_bytes: Vec<u8> = owned_string.clone().into_bytes();
    println!("String '{}' -> Vec<u8>: {:?}", owned_string, into_bytes);

    let back_string: String = String::from_utf8(into_bytes).expect("valid utf8");
    println!("Vec<u8> -> String: '{}'", back_string);

    // from_utf8_unchecked skips the UTF-8 validity check; UB if bytes are not valid UTF-8
    let unchecked_bytes: Vec<u8> = vec![72, 101, 108, 108, 111];
    let unsafe_string: String = unsafe { String::from_utf8_unchecked(unchecked_bytes.clone()) };
    println!("unsafe from_utf8_unchecked: '{}'", unsafe_string);

    print_h3!("OsString conversions");
    use std::ffi::{OsStr, OsString};
    let os_string: OsString = OsString::from("path/to/file");
    let as_str_opt: Option<&str> = os_string.to_str();
    println!("OsString -> Option<&str>: {:?}", as_str_opt);

    let os_str: &OsStr = OsStr::new("another/path");
    let os_owned: OsString = os_str.to_os_string();
    println!("OsStr -> OsString: {:?}", os_owned);

    print_h3!("CString/CStr (FFI)");
    // CString is an owned, null-terminated byte string; CStr is its borrowed counterpart
    use std::ffi::{CStr, CString};
    let c_string: CString = CString::new("hello C").expect("CString::new");
    let c_str: &CStr = c_string.as_c_str();
    println!("CString: {:?}, as_c_str: {:?}", c_string, c_str);

    let rust_str: &str = c_str.to_str().expect("valid utf8");
    println!("CStr -> &str: '{}'", rust_str);

    let raw_ptr: *const i8 = c_string.as_ptr();
    let from_ptr: &CStr = unsafe { CStr::from_ptr(raw_ptr) };
    println!("CStr from raw ptr: {:?}", from_ptr);

    print_h3!("Ref casting");
    let value: i32 = 42;
    let ref_cast: &i32 = &value;
    let ptr: *const i32 = ref_cast as *const i32;
    let back_ref: &i32 = unsafe { &*ptr };
    println!("&i32 -> *const i32 -> &i32: {}", back_ref);

    let mut mut_val: i32 = 100;
    let mut_ptr: *mut i32 = &mut mut_val as *mut i32;
    unsafe { *mut_ptr += 10 };
    println!("Mutated via raw pointer: {}", mut_val);
}
