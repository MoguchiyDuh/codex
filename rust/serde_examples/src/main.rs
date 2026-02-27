#![allow(dead_code)]
use shared::print_h1;

mod custom_serde;
mod derive_macros;
mod json_basics;
mod toml_basics;

fn main() {
    print_h1!("Serde / Serialization");

    json_basics::run();
    derive_macros::run();
    custom_serde::run();
    toml_basics::run();
}
