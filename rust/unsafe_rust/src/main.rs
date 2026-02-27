#![allow(dead_code)]
use shared::print_h1;

mod ffi_basics;
mod raw_pointers;
mod unsafe_functions;

fn main() {
    print_h1!("Unsafe Rust");

    raw_pointers::run();

    println!();
    unsafe_functions::run();

    println!();
    ffi_basics::run();
}
