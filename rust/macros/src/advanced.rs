use shared::{print_h2, print_h3};

pub fn run() {
    print_h2!("Advanced Macro Patterns");

    print_h3!("Internal rules (@keyword convention)");

    // @prefix is a convention (not enforced by the compiler) to mark arms as internal helpers
    // that should not be invoked directly by callers — part of the TT muncher pattern
    macro_rules! log {
        (info: $msg:expr)  => { log!(@print "INFO",  $msg) };
        (warn: $msg:expr)  => { log!(@print "WARN",  $msg) };
        (error: $msg:expr) => { log!(@print "ERROR", $msg) };
        // Internal helper - never called directly from outside
        (@print $level:expr, $msg:expr) => {
            println!("[{}] {}", $level, $msg);
        };
    }

    log!(info: "server started");
    log!(warn: "high memory usage");
    log!(error: "connection refused");

    print_h3!("Generating impl blocks");

    macro_rules! impl_display {
        ($type:ty, $fmt:expr) => {
            impl std::fmt::Display for $type {
                fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
                    return write!(f, $fmt, self.0);
                }
            }
        };
    }

    struct Meters(f64);
    struct Kilograms(f64);
    impl_display!(Meters, "{} m");
    impl_display!(Kilograms, "{} kg");

    println!("{}", Meters(1.5));
    println!("{}", Kilograms(70.0));

    print_h3!("Generating multiple items");

    macro_rules! make_errors {
        ($($name:ident => $msg:literal),+ $(,)?) => {
            $(
                #[derive(Debug)]
                struct $name;

                impl std::fmt::Display for $name {
                    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
                        return write!(f, $msg);
                    }
                }

                impl std::error::Error for $name {}
            )+
        };
    }

    make_errors!(
        ParseError   => "parse error",
        NetworkError => "network error",
        TimeoutError => "connection timed out",
    );

    let pe: ParseError = ParseError;
    let ne: NetworkError = NetworkError;
    println!("Error: {}", pe);
    println!("Error: {}", ne);

    print_h3!("Variadic over types");

    macro_rules! print_type_size {
        ($($t:ty),+ $(,)?) => {
            $(
                println!(
                    "size_of::<{}>() = {} bytes",
                    stringify!($t),
                    std::mem::size_of::<$t>()
                );
            )+
        };
    }

    print_type_size!(i8, i16, i32, i64, i128, f32, f64, bool, char, usize);

    print_h3!("Trailing comma normalization");

    // $(,)? at the end of a pattern allows an optional trailing comma
    // This lets users write: my_vec![1, 2, 3,] or my_vec![1, 2, 3]
    macro_rules! flexible_vec {
        ($($elem:expr),* $(,)?) => {
            vec![$($elem),*]
        };
    }

    let v1: Vec<i32> = flexible_vec![1, 2, 3];
    let v2: Vec<i32> = flexible_vec![1, 2, 3,]; // trailing comma OK
    println!("flexible_vec![1,2,3]  = {:?}", v1);
    println!("flexible_vec![1,2,3,] = {:?}", v2);

    print_h3!("cfg-conditional macros");

    macro_rules! platform_msg {
        () => {
            if cfg!(target_os = "linux") {
                "Linux"
            } else if cfg!(target_os = "windows") {
                "Windows"
            } else {
                "Other OS"
            }
        };
    }

    println!("Platform: {}", platform_msg!());

    print_h3!("Macro calling macro");

    macro_rules! add_one {
        ($x:expr) => {
            $x + 1
        };
    }

    macro_rules! double_then_add_one {
        ($x:expr) => {
            add_one!($x * 2)
        };
    }

    println!("double_then_add_one!(5) = {}", double_then_add_one!(5)); // (5*2)+1 = 11

    print_h3!("Macro export visibility");

    // #[macro_export] makes a macro available from the crate root
    // Without it, macros are only visible in the module they're defined in
    // shared crate uses #[macro_export] for print_h1!, print_h2!, print_h3!
    // Access: `use shared::{print_h1, print_h2, print_h3};`
    // Or legacy: `#[macro_use] extern crate shared;` (imports all exported macros)
    println!("See shared/src/lib.rs for #[macro_export] examples");

    print_h3!("Procedural macros (overview)");

    // Three kinds of proc macros:
    //   1. #[derive(Trait)]   - code generation for structs/enums
    //   2. #[my_attribute]    - transforms the annotated item
    //   3. my_macro!(...)     - function-like, full token control
    //
    // Minimal proc-macro crate Cargo.toml:
    //   [lib]
    //   proc-macro = true
    //   [dependencies]
    //   syn   = { version = "2", features = ["full"] }
    //   quote = "1"
    //   proc-macro2 = "1"
    //
    // Example usage: serde uses derive, tokio::main uses attribute, sqlx::query! is fn-like

    println!("proc macros: derive / attribute / function-like");
    println!("Real-world: serde (derive), tokio::main (attribute), sqlx::query! (fn-like)");

    print_h3!("? operator desugaring");

    fn try_parse(s: &str) -> Result<i32, std::num::ParseIntError> {
        // ? is syntax sugar: on Err it calls From::from(e) (Into::into) and early-returns
        // ? desugars to: match expr { Ok(v) => v, Err(e) => return Err(e.into()) }
        let n: i32 = s.trim().parse()?;
        return Ok(n * 2);
    }

    println!("try_parse(\"21\")  = {:?}", try_parse("21"));
    println!("try_parse(\"abc\") = {:?}", try_parse("abc"));
}
