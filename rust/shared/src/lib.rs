// `pub use colored` re-exports the colored crate from this library.
// Downstream crates can do `use shared::colored::Colorize` instead of adding colored as a dep.
pub use colored;
use std::any::type_name;

pub fn center_string(s: &str, width: usize, fillchar: char) -> String {
    let total_padding = width.saturating_sub(s.len() + 2);
    if total_padding == 0 {
        return s.to_string();
    }
    let left_padding = total_padding / 2;
    let right_padding = total_padding - left_padding;
    format!(
        "{} {} {}",
        fillchar.to_string().repeat(left_padding),
        s,
        fillchar.to_string().repeat(right_padding)
    )
}

#[macro_export]
macro_rules! print_h1 {
    ($($arg:tt)*) => {{
        use $crate::colored::Colorize;
        let msg = format!($($arg)*).to_uppercase();
        println!("\n{}", $crate::center_string(&msg, 60, '=').bright_green().bold());
    }};
}

#[macro_export]
macro_rules! print_h2 {
    ($($arg:tt)*) => {{
        use $crate::colored::Colorize;
        let msg = format!($($arg)*);
        println!("{}", $crate::center_string(&msg, 50, '-').bright_magenta().bold());
    }};
}

#[macro_export]
macro_rules! print_h3 {
    ($($arg:tt)*) => {{
        use $crate::colored::Colorize;
        let msg = format!($($arg)*);
        println!("{}", $crate::center_string(&msg, 40, '.').bright_cyan());
    }};
}

// type_name::<T>() is a const fn that returns the Rust canonical name of T as a &'static str.
// The parameter `_: &T` is used only to infer T — the value itself is never touched.
pub fn get_type<T>(_: &T) -> &'static str {
    type_name::<T>()
}
