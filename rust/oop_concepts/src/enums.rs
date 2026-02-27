#![allow(dead_code)]
use shared::{print_h2, print_h3};

// Rust enums are algebraic data types (sum types): each variant can carry different data
#[derive(Debug)]
pub enum WebEvent {
    PageLoad,
    KeyPress(char),
    Click { x: i64, y: i64 }, // struct-like variant with named fields
}

#[derive(Debug)]
pub enum TrafficLight {
    Red,
    Yellow,
    Green,
}

impl TrafficLight {
    pub fn duration(&self) -> u8 {
        match self {
            TrafficLight::Red => 30,
            TrafficLight::Yellow => 5,
            TrafficLight::Green => 25,
        }
    }
}

pub fn run() {
    print_h2!("Enums");
    print_h3!("Data Enums");
    let event = WebEvent::Click { x: 10, y: 20 };
    println!("Event: {:?}", event);

    print_h3!("Enum Methods");
    let light = TrafficLight::Green;
    println!("Green light duration: {}s", light.duration());
}
