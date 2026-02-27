use shared::{print_h2, print_h3};
use std::time::{SystemTime, UNIX_EPOCH};

#[derive(Debug)]
pub struct Person {
    pub name: String,
    pub age: u8,
    pub job: String,
}

impl Person {
    // Returning Self (not Person) means substructs can reuse this without hardcoding the type name
    pub fn new(name: &str, job: &str) -> Self {
        let duration = SystemTime::now().duration_since(UNIX_EPOCH).unwrap();
        let year = 1970 + (duration.as_secs() / 31_557_600);
        Self {
            name: name.to_string(),
            age: (year - 2006) as u8,
            job: job.to_string(),
        }
    }

    pub fn introduce(&self) {
        println!(
            "I'm {}, {} years old, working as a {}",
            self.name, self.age, self.job
        );
    }
}

pub struct Counter {
    count: i32,
}

impl Counter {
    pub fn new() -> Self {
        Self { count: 0 }
    }

    pub fn increment(&mut self) {
        self.count += 1;
    }

    pub fn get(&self) -> i32 {
        self.count
    }
}

pub fn run() {
    print_h2!("Structs");
    print_h3!("Basic Structs & Impl");
    let kirill = Person::new("Kirill", "Programmer");
    kirill.introduce();

    print_h3!("Mutable Struct Methods");
    let mut c = Counter::new();
    c.increment();
    c.increment();
    println!("Counter value: {}", c.get());
}
