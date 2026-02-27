#![allow(dead_code)]
use shared::print_h1;

mod array_example;
mod casting;
mod conditions;
mod data_types;
mod environment;
mod functions;
mod input;
mod lifetimes;
mod loops;
mod matching;
mod option_result;
mod ownership;
mod panic;
mod printing;
mod random;
mod string_example;
mod time;
mod variables;

fn main() {
    print_h1!("Rust Basics");

    variables::run();
    data_types::run();
    casting::run();
    functions::run();
    conditions::run();
    loops::run();
    matching::run();
    ownership::run();
    lifetimes::run();
    string_example::run();
    array_example::run();
    option_result::run();
    panic::run();
    printing::run();
    input::run();
    random::run();
    environment::run();
    time::run();
}
