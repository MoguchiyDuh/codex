#![allow(dead_code)]
use shared::print_h1;

mod binary_heap;
mod btreemap;
mod btreeset;
mod deques;
mod hashmaps;
mod hashsets;
mod vectors;

fn main() {
    print_h1!("Rust Collections");

    vectors::run();
    hashmaps::run();
    hashsets::run();
    deques::run();
    btreemap::run();
    btreeset::run();
    binary_heap::run();
}
