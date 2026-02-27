use shared::{print_h2, print_h3};
use std::ffi::{CStr, CString, c_char, c_double, c_int, c_longlong};

// ------------------- External C functions: libc -------------------

unsafe extern "C" {
    fn strlen(s: *const c_char) -> usize;
    fn abs(x: c_int) -> c_int;
    fn atoi(s: *const c_char) -> c_int;
}

// ------------------- External C functions: our c_src/ -------------------

unsafe extern "C" {
    // math_utils.c
    fn c_add(a: c_int, b: c_int) -> c_int;
    fn c_multiply(a: c_int, b: c_int) -> c_int;
    fn c_factorial(n: c_int) -> c_longlong;
    fn c_point_magnitude(p: CPoint) -> c_double;
    fn c_apply(value: c_int, f: extern "C" fn(c_int) -> c_int) -> c_int;
    fn c_repeat_char(c: c_char, n: c_int, buf: *mut c_char, buf_len: c_int) -> c_int;

    // rust_caller.c — C functions that call back into Rust
    fn call_rust_add(a: c_int, b: c_int) -> c_int;
    fn double_via_rust(x: c_int) -> c_int;
    fn sum_then_square(a: c_int, b: c_int) -> c_int;
}

// ------------------- C-compatible struct (shared with C side) -------------------
// Must match `typedef struct { double x; double y; } CPoint;` in math_utils.c

// #[repr(C)] makes field layout match C's struct ABI: sequential, with C alignment rules.
// Without it, Rust may reorder or add padding differently from what C expects.
// Clone + Copy allow the struct to be passed by value across the FFI boundary.
#[repr(C)]
#[derive(Debug, Clone, Copy)]
struct CPoint {
    x: c_double,
    y: c_double,
}

// ------------------- Rust functions exported to C -------------------
// rust_caller.c declares `extern int rust_add(int a, int b)` and calls these

// #[unsafe(no_mangle)]: keeps the symbol name as-is in the binary (no Rust name mangling).
// extern "C": uses the C calling convention so C code can call this function.
// Together these two attributes make a Rust function callable from C.
#[unsafe(no_mangle)]
pub extern "C" fn rust_add(a: c_int, b: c_int) -> c_int {
    return a + b;
}

#[unsafe(no_mangle)]
pub extern "C" fn rust_square(x: c_int) -> c_int {
    return x * x;
}

// ------------------- Callbacks: Rust fn with C calling convention -------------------
// Passed as function pointers to c_apply() in math_utils.c

extern "C" fn double_it(x: c_int) -> c_int {
    return x * 2;
}

extern "C" fn negate(x: c_int) -> c_int {
    return -x;
}

pub fn run() {
    print_h2!("FFI Basics");

    // ------------------- Calling libc functions -------------------
    print_h3!("Calling libc Functions");

    let neg: c_int = -42;
    let pos: c_int = unsafe { abs(neg) };
    println!("libc abs(-42) = {}", pos);

    let rust_str: &str = "hello from Rust";
    let c_string: CString = CString::new(rust_str).expect("CString::new failed");
    let len: usize = unsafe { strlen(c_string.as_ptr()) };
    println!("libc strlen(\"{}\") = {}", rust_str, len);

    let num_str: CString = CString::new("1234").unwrap();
    let parsed: c_int = unsafe { atoi(num_str.as_ptr()) };
    println!("libc atoi(\"1234\") = {}", parsed);

    // ------------------- Custom C functions -------------------
    print_h3!("Custom C Functions (c_src/math_utils.c)");

    let sum: c_int = unsafe { c_add(10, 32) };
    println!("c_add(10, 32)       = {}", sum);

    let product: c_int = unsafe { c_multiply(6, 7) };
    println!("c_multiply(6, 7)    = {}", product);

    let fact: c_longlong = unsafe { c_factorial(10) };
    println!("c_factorial(10)     = {}", fact); // 3628800

    // ------------------- Passing #[repr(C)] structs to C -------------------
    print_h3!("Passing #[repr(C)] Structs to C");

    // CPoint layout matches `typedef struct { double x; double y; } CPoint;` in C
    let p: CPoint = CPoint { x: 3.0, y: 4.0 };
    let mag: c_double = unsafe { c_point_magnitude(p) };
    println!("c_point_magnitude({{3.0, 4.0}}) = {} (expected 5.0)", mag);

    let p2: CPoint = CPoint { x: 1.0, y: 1.0 };
    println!("c_point_magnitude({{1.0, 1.0}}) = {:.4}", unsafe { c_point_magnitude(p2) });

    // ------------------- Callbacks: Rust fn pointer passed to C -------------------
    print_h3!("Callbacks: Rust fn → C → calls back");

    // c_apply(value, fn) calls fn(value) in C — we pass Rust-defined function pointers
    let doubled: c_int = unsafe { c_apply(21, double_it) };
    println!("c_apply(21, double_it) = {}", doubled); // 42

    let negated: c_int = unsafe { c_apply(99, negate) };
    println!("c_apply(99, negate)    = {}", negated); // -99

    // Closure-like: Rust closure can't cross FFI boundary, but fn pointers can
    // extern "C" fn is required — not |x| x * 2 (closures have hidden state)

    // ------------------- Passing buffers to C -------------------
    print_h3!("Passing Buffers (Rust allocates, C fills)");

    // Rust allocates the buffer, C writes into it
    let mut buf: Vec<u8> = vec![0u8; 32];
    let written: c_int = unsafe {
        c_repeat_char(b'*' as c_char, 8, buf.as_mut_ptr() as *mut c_char, 32)
    };
    // SAFETY: C null-terminated within buf_len, buf still valid
    let filled: &CStr = unsafe { CStr::from_ptr(buf.as_ptr() as *const c_char) };
    println!("c_repeat_char('*', 8)  = {:?} ({} chars)", filled.to_str().unwrap(), written);

    let mut buf2: Vec<u8> = vec![0u8; 16];
    unsafe { c_repeat_char(b'-' as c_char, 5, buf2.as_mut_ptr() as *mut c_char, 16) };
    let filled2: &CStr = unsafe { CStr::from_ptr(buf2.as_ptr() as *const c_char) };
    println!("c_repeat_char('-', 5)  = {:?}", filled2.to_str().unwrap());

    // ------------------- Round trip: Rust → C → Rust -------------------
    print_h3!("Round Trip: Rust → C → Rust");

    // call_rust_add(a, b): defined in rust_caller.c, calls rust_add() back into Rust
    let via_c: c_int = unsafe { call_rust_add(15, 27) };
    println!("call_rust_add(15, 27)    = {} (Rust → C → rust_add)", via_c);

    // double_via_rust(x): C calls rust_add(x, x)
    let doubled: c_int = unsafe { double_via_rust(21) };
    println!("double_via_rust(21)      = {} (C calls rust_add(21,21))", doubled);

    // sum_then_square(a, b): C calls rust_add then rust_square
    let sq: c_int = unsafe { sum_then_square(3, 4) }; // (3+4)^2 = 49
    println!("sum_then_square(3, 4)    = {} ((3+4)^2, chains rust_add+rust_square)", sq);

    // ------------------- CString and CStr -------------------
    print_h3!("CString (owned) and CStr (borrowed)");

    // CString: heap-allocated, null-terminated — for passing to C
    let owned: CString = CString::new("owned C string").unwrap();
    println!("CString = {:?}", owned);

    // Fails if the &str contains interior null bytes
    let bad: Result<CString, _> = CString::new("has\0null");
    println!("CString::new(\"has\\0null\") = {:?}", bad); // Err(NulError)

    // into_raw / from_raw: transfer ownership to/from C
    let raw: *mut c_char = CString::new("transfer to C").unwrap().into_raw();
    let reclaimed: CString = unsafe { CString::from_raw(raw) };
    println!("Reclaimed from raw       = {:?}", reclaimed);

    // CStr: borrowed reference to a null-terminated byte sequence
    let cstr: &CStr = unsafe { CStr::from_bytes_with_nul_unchecked(b"static C string\0") };
    println!("CStr = {:?}", cstr);
    println!("CStr -> &str = \"{}\"", cstr.to_str().unwrap());

    // ------------------- C-compatible primitive types -------------------
    print_h3!("C-compatible Primitive Types");

    println!("c_char     = {} byte(s)", std::mem::size_of::<c_char>());
    println!("c_int      = {} bytes", std::mem::size_of::<c_int>());
    println!("c_double   = {} bytes", std::mem::size_of::<c_double>());
    println!("c_longlong = {} bytes", std::mem::size_of::<c_longlong>());
    println!("usize      = {} bytes  (≈ C size_t)", std::mem::size_of::<usize>());
    println!("isize      = {} bytes  (≈ C ptrdiff_t)", std::mem::size_of::<isize>());

    // ------------------- #[repr(C)] enum -------------------
    print_h3!("#[repr(C)] Enum");

    #[repr(C)]
    #[derive(Debug)]
    enum Status {
        Ok = 0,
        Error = 1,
        Timeout = 2,
    }
    let s: Status = Status::Ok;
    println!("Status::Ok as i32 = {}", s as i32);

    // ------------------- Linking and safe wrapper (overview) -------------------
    print_h3!("Linking and Safe Wrapper Pattern");

    // Linking options:
    //   build.rs: println!("cargo:rustc-link-lib=m")       dynamic
    //   build.rs: println!("cargo:rustc-link-lib=static=m") static
    //   attribute: #[link(name = "m")] on the extern block
    //   cc crate in build.rs: compiles .c files into a static lib

    // Best practice: expose a safe public fn, keep unsafe internal
    fn safe_factorial(n: u32) -> i64 {
        return unsafe { c_factorial(n as c_int) };
    }

    println!("safe_factorial(12) = {}", safe_factorial(12)); // 479001600
    println!("safe_factorial(0)  = {}", safe_factorial(0));  // 1
}
