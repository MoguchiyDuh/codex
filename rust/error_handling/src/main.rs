#![allow(dead_code)]
use shared::print_h1;

mod anyhow_example;
mod custom_errors;
mod error_conversion;
mod error_trait;
mod propagation;
mod thiserror_example;

fn main() {
    print_h1!("Error Handling");

    custom_errors::run();
    error_trait::run();
    error_conversion::run();
    propagation::run();
    thiserror_example::run();
    anyhow_example::run();
}
