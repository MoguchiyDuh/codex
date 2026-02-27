#![allow(dead_code)]
use shared::print_h1;

mod advanced;
mod built_in;
mod declarative;

fn main() {
    print_h1!("Macros");

    declarative::run();
    built_in::run();
    advanced::run();
}
