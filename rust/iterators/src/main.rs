#![allow(dead_code)]
use shared::print_h1;

mod adapters;
mod advanced;
mod basics;
mod consumers;
mod custom_iterators;
mod patterns;

fn main() {
    print_h1!("Iterators");

    basics::run();
    adapters::run();
    consumers::run();
    advanced::run();
    custom_iterators::run();
    patterns::run();
}
