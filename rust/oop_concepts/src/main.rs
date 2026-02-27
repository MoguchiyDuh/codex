#![allow(dead_code)]
use shared::print_h1;

mod enums;
mod generics;
mod std_traits;
mod structs;
mod traits;

fn main() {
    print_h1!("OOP & Type System");

    structs::run();
    enums::run();
    traits::run();
    generics::run();
    std_traits::run();
}
