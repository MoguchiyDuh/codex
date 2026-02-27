use shared::{print_h2, print_h3};
use std::fmt;
use std::ops::{Add, Deref, DerefMut, Index};

// ------------------- Clone -------------------

#[derive(Debug)]
struct Buffer {
    data: Vec<u8>,
    label: String,
}

impl Clone for Buffer {
    fn clone(&self) -> Self {
        println!("  Buffer::clone() called"); // side-effect to show it's deep copy
        return Buffer {
            data: self.data.clone(),
            label: self.label.clone(),
        };
    }
}

// ------------------- Copy -------------------

// Copy = bit-copy instead of move. Only for stack-only, trivially-copyable types.
// A type can't implement Copy if it contains heap data (String, Vec, etc.)
#[derive(Debug, Clone, Copy, PartialEq)]
struct Color {
    r: u8,
    g: u8,
    b: u8,
}

// ------------------- Default -------------------

#[derive(Debug)]
struct ServerConfig {
    host: String,
    port: u16,
    timeout_ms: u64,
    max_conn: u32,
    tls: bool,
}

impl Default for ServerConfig {
    fn default() -> Self {
        return ServerConfig {
            host: String::from("127.0.0.1"),
            port: 8080,
            timeout_ms: 5000,
            max_conn: 100,
            tls: false,
        };
    }
}

// ------------------- Display and Debug -------------------

struct Temperature {
    celsius: f64,
}

impl fmt::Display for Temperature {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        return write!(
            f,
            "{:.1}°C / {:.1}°F",
            self.celsius,
            self.celsius * 9.0 / 5.0 + 32.0
        );
    }
}

impl fmt::Debug for Temperature {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        return f
            .debug_struct("Temperature")
            .field("celsius", &self.celsius)
            .finish();
    }
}

// Custom binary/hex format specifiers
struct Flags(u32);

impl fmt::Binary for Flags {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        return write!(f, "{:08b}", self.0);
    }
}

impl fmt::LowerHex for Flags {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        return write!(f, "0x{:08x}", self.0);
    }
}

// ------------------- PartialEq and Eq -------------------

#[derive(Debug, Clone)]
struct Version {
    major: u32,
    minor: u32,
    patch: u32,
}

impl PartialEq for Version {
    fn eq(&self, other: &Self) -> bool {
        return self.major == other.major && self.minor == other.minor && self.patch == other.patch;
    }
}

// Eq is a marker trait: adds the guarantee that a == a is always true
// f64 implements PartialEq but NOT Eq because NaN != NaN
impl Eq for Version {}

// ------------------- PartialOrd and Ord -------------------

#[derive(Debug, Clone, PartialEq, Eq)]
struct SemVer {
    major: u32,
    minor: u32,
    patch: u32,
}

impl PartialOrd for SemVer {
    // The canonical pattern when you also implement Ord: delegate to cmp().
    // PartialOrd returns Option<Ordering> to handle types that may not be comparable (e.g. NaN).
    // For totally ordered types like SemVer, it's always Some(...)
    fn partial_cmp(&self, other: &Self) -> Option<std::cmp::Ordering> {
        return Some(self.cmp(other)); // delegate to Ord when Ord is implemented
    }
}

impl Ord for SemVer {
    fn cmp(&self, other: &Self) -> std::cmp::Ordering {
        return self
            .major
            .cmp(&other.major)
            .then(self.minor.cmp(&other.minor))
            .then(self.patch.cmp(&other.patch));
    }
}

// ------------------- From and Into -------------------

struct Km(f64);
struct Miles(f64);

impl From<Km> for Miles {
    fn from(km: Km) -> Self {
        return Miles(km.0 * 0.621371);
    }
}

// From<T> for U automatically provides Into<U> for T — never implement both manually

#[derive(Debug)]
struct CsvLine(Vec<String>);

impl From<&str> for CsvLine {
    fn from(s: &str) -> Self {
        return CsvLine(s.split(',').map(|f| f.trim().to_string()).collect());
    }
}

impl From<Vec<&str>> for CsvLine {
    fn from(v: Vec<&str>) -> Self {
        return CsvLine(v.into_iter().map(|s| s.to_string()).collect());
    }
}

// ------------------- Deref and DerefMut -------------------

// Deref: *val calls deref() and follows the reference
// DerefMut: *val on mutable allows mutation
// Deref coercion: &MyBox<String> -> &String -> &str automatically in function calls

struct Newtype<T>(T);

impl<T> Deref for Newtype<T> {
    type Target = T;
    fn deref(&self) -> &T {
        return &self.0;
    }
}

impl<T> DerefMut for Newtype<T> {
    fn deref_mut(&mut self) -> &mut T {
        return &mut self.0;
    }
}

// ------------------- Index and IndexMut -------------------

struct Matrix {
    data: [[f64; 3]; 3],
}

impl Index<(usize, usize)> for Matrix {
    type Output = f64;
    fn index(&self, (row, col): (usize, usize)) -> &f64 {
        return &self.data[row][col];
    }
}

// ------------------- Add (operator overloading) -------------------

#[derive(Debug, Clone, Copy, PartialEq)]
struct Vec2 {
    x: f64,
    y: f64,
}

impl Add for Vec2 {
    type Output = Vec2;
    fn add(self, rhs: Vec2) -> Vec2 {
        return Vec2 {
            x: self.x + rhs.x,
            y: self.y + rhs.y,
        };
    }
}

impl fmt::Display for Vec2 {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        return write!(f, "({:.2}, {:.2})", self.x, self.y);
    }
}

pub fn run() {
    print_h2!("Standard Traits");
    print_h3!("Clone");

    let original: Buffer = Buffer {
        data: vec![1, 2, 3, 4, 5],
        label: String::from("original"),
    };
    let cloned: Buffer = original.clone(); // deep copy - independent data
    println!("original: {:?}", original);
    println!("cloned:   {:?}", cloned);

    // Derive Clone generates: self.field.clone() for each field
    let v1: Vec<i32> = vec![1, 2, 3];
    let v2: Vec<i32> = v1.clone();
    println!("v1 (still valid): {:?}", v1);
    println!("v2 (deep copy):   {:?}", v2);

    print_h3!("Copy");

    let c1: Color = Color {
        r: 255,
        g: 128,
        b: 0,
    };
    let c2: Color = c1; // bit-copy, c1 is STILL valid
    println!("c1 = {:?} (still valid after assignment)", c1);
    println!("c2 = {:?}", c2);

    // Primitives are all Copy: i32, f64, bool, char, &T, etc.
    let x: i32 = 5;
    let y: i32 = x; // copy
    println!("x={}, y={} (both valid)", x, y);

    // String is NOT Copy (heap data):
    // let s1 = String::from("hello");
    // let s2 = s1;  // s1 moved - ERROR: s1 used after move

    print_h3!("Default");

    let cfg: ServerConfig = ServerConfig::default();
    println!("ServerConfig::default() = {:?}", cfg);

    // Struct update syntax: override some fields, default the rest
    let prod: ServerConfig = ServerConfig {
        host: String::from("0.0.0.0"),
        port: 443,
        tls: true,
        ..ServerConfig::default()
    };
    println!("prod config = {:?}", prod);

    // Default for std types
    println!("i32::default()          = {}", i32::default()); // 0
    println!("f64::default()          = {}", f64::default()); // 0.0
    println!("bool::default()         = {}", bool::default()); // false
    println!("String::default()       = {:?}", String::default()); // ""
    println!("Vec::<i32>::default()   = {:?}", Vec::<i32>::default()); // []
    println!("Option::<i32>::default()= {:?}", Option::<i32>::default()); // None

    print_h3!("Display and Debug");

    let t: Temperature = Temperature { celsius: 37.5 };
    println!("Display: {}", t); // human-readable
    println!("Debug:   {:?}", t); // developer-readable
    println!("Pretty:  {:#?}", t); // multi-line debug

    let f: Flags = Flags(0b1010_1100_1111_0000);
    println!("Binary: {:b}", f); // uses fmt::Binary impl
    println!("Hex:    {:x}", f); // uses fmt::LowerHex impl

    // Format width / padding work with Display
    let val: i32 = 42;
    println!("padded: {:>10}", val); // right-aligned in 10 chars
    println!("zero:   {:010}", val); // zero-padded

    print_h3!("PartialEq / Eq");

    let v1: Version = Version {
        major: 1,
        minor: 2,
        patch: 3,
    };
    let v2: Version = Version {
        major: 1,
        minor: 2,
        patch: 3,
    };
    let v3: Version = Version {
        major: 2,
        minor: 0,
        patch: 0,
    };

    println!("v1 == v2: {}", v1 == v2); // true
    println!("v1 == v3: {}", v1 == v3); // false
    println!("v1 != v3: {}", v1 != v3); // true

    // NaN is the classic PartialEq-but-not-Eq case
    let nan: f64 = f64::NAN;
    println!(
        "NaN == NaN: {} (PartialEq - NaN violates reflexivity)",
        nan == nan
    );

    print_h3!("PartialOrd / Ord");

    let mut versions: Vec<SemVer> = vec![
        SemVer {
            major: 2,
            minor: 0,
            patch: 0,
        },
        SemVer {
            major: 1,
            minor: 10,
            patch: 3,
        },
        SemVer {
            major: 1,
            minor: 2,
            patch: 0,
        },
        SemVer {
            major: 1,
            minor: 10,
            patch: 1,
        },
    ];

    versions.sort(); // uses Ord
    println!("Sorted versions:");
    for v in &versions {
        println!("  {}.{}.{}", v.major, v.minor, v.patch);
    }

    let a: SemVer = SemVer {
        major: 1,
        minor: 0,
        patch: 0,
    };
    let b: SemVer = SemVer {
        major: 2,
        minor: 0,
        patch: 0,
    };
    println!("1.0.0 < 2.0.0: {}", a < b);
    println!("min(1.0.0, 2.0.0) = {:?}", a.clone().min(b.clone()));
    println!("max(1.0.0, 2.0.0) = {:?}", a.max(b));

    // f64 implements PartialOrd but NOT Ord - can't use sort(), use sort_by() instead
    let mut floats: Vec<f64> = vec![3.1, 1.4, 1.5, 9.2];
    floats.sort_by(|a, b| a.partial_cmp(b).unwrap());
    println!("f64 sorted via partial_cmp: {:?}", floats);

    print_h3!("From / Into");

    let km: Km = Km(100.0);
    let miles: Miles = Miles::from(Km(100.0));
    println!("100 km = {:.3} miles", miles.0);

    let also_miles: Miles = km.into(); // Into<Miles> auto-derived from From<Km> for Miles
    println!("into() miles = {:.3}", also_miles.0);

    // CsvLine conversions
    let line: CsvLine = CsvLine::from("alice, 30, engineer");
    println!("CsvLine from &str: {:?}", line);

    let from_vec: CsvLine = vec!["bob", "25", "designer"].into(); // Into via From impl
    println!("CsvLine from vec: {:?}", from_vec);

    // Numeric From (lossless widening)
    let n: i32 = 42;
    let wide: i64 = i64::from(n);
    println!("i32({}) -> i64({})", n, wide);

    // String conversions use From/Into
    let s: String = String::from("hello");
    let s2: String = "world".into();
    println!("{} {}", s, s2);

    print_h3!("Deref / DerefMut");

    let mut boxed: Newtype<String> = Newtype(String::from("hello"));
    println!("*boxed = {}", *boxed); // Deref: calls deref() -> &String
    println!("len via coercion = {}", boxed.len()); // Deref coercion: Newtype<String> -> String -> str

    *boxed = String::from("world"); // DerefMut: calls deref_mut() -> &mut String
    println!("after DerefMut: {}", *boxed);

    boxed.push_str("!"); // DerefMut coercion to call String method
    println!("after push_str: {}", *boxed);

    // Deref coercion chain: Box<String> -> String -> str
    let b: Box<String> = Box::new(String::from("deref chain"));
    let as_str: &str = &b; // Box -> String -> str coercion
    println!("Box -> &str coercion: {}", as_str);

    print_h3!("Index");

    let mat: Matrix = Matrix {
        data: [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]],
    };
    println!("mat[(0, 0)] = {}", mat[(0, 0)]);
    println!("mat[(1, 2)] = {}", mat[(1, 2)]);
    println!("mat[(2, 1)] = {}", mat[(2, 1)]);

    print_h3!("Add operator");

    let a: Vec2 = Vec2 { x: 1.0, y: 2.0 };
    let b: Vec2 = Vec2 { x: 3.0, y: 4.0 };
    let sum: Vec2 = a + b; // calls Add::add
    println!("{} + {} = {}", a, b, sum);

    // std::ops: Add Sub Mul Div Rem Neg Not BitAnd BitOr BitXor Shl Shr
    // std::ops: Index IndexMut  ([] operator)
    // std::ops: Fn FnMut FnOnce (() operator - closures)
    println!("std::ops covers all arithmetic and logical operators");
}
