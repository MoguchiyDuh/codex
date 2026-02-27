use rand::prelude::*;
use shared::{print_h2, print_h3};

pub fn run() {
    print_h2!("Random Numbers");
    print_h3!("rand crate basics");
    let mut rng = rand::rng();

    let n: i32 = rng.random();
    println!("Random i32: {}", n);

    let roll = rng.random_range(1..=6);
    println!("D6 Roll: {}", roll);

    let prob = rng.random_bool(0.5);
    println!("Coin flip: {}", if prob { "Heads" } else { "Tails" });
}
