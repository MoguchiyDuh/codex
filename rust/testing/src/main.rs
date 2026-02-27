#![allow(dead_code)]
use shared::print_h1;

mod assertions;
mod organizing;
mod unit_tests;

fn main() {
    print_h1!("Testing");

    unit_tests::run();
    assertions::run();
    organizing::run();

    println!("cargo test -p testing                  - run all tests");
    println!("cargo test -p testing -- --nocapture   - show println! output");
    println!("cargo test -p testing test_deposit     - filter by name");
    println!("cargo test -p testing -- --include-ignored  - include #[ignore] tests");
}
