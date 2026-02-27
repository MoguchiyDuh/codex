use shared::{print_h2, print_h3};

// ------------------- Trait definition -------------------

trait Greet {
    fn hello(&self) -> String; // required method - must be implemented
    fn goodbye(&self) -> String {
        // default implementation - can be overridden
        return format!("Goodbye from: {}", self.hello());
    }
}

struct English;
struct Spanish;

impl Greet for English {
    fn hello(&self) -> String {
        return String::from("Hello!");
    }
}

impl Greet for Spanish {
    fn hello(&self) -> String {
        return String::from("¡Hola!");
    }
    fn goodbye(&self) -> String {
        // override default
        return String::from("¡Adiós!");
    }
}

// ------------------- impl Trait (static dispatch) -------------------

// Sugar for: fn greet_once<T: Greet>(item: &T)
// Monomorphized: compiler generates one copy per concrete type
fn greet_once(item: &impl Greet) {
    println!("{}", item.hello());
}

// Return-position impl Trait (RPIT) - hides concrete type from caller
fn make_greeter() -> impl Greet {
    return English;
}

// ------------------- dyn Trait (dynamic dispatch) -------------------

// Fat pointer: (data ptr, vtable ptr) - 2 words
// Vtable has pointers to the concrete type's method implementations
fn greet_dynamic(item: &dyn Greet) {
    println!("{}", item.hello());
}

fn make_greeter_dynamic(use_english: bool) -> Box<dyn Greet> {
    if use_english {
        return Box::new(English);
    }
    return Box::new(Spanish); // return type must be the same -> Box<dyn Greet>
}

// ------------------- Trait objects in collections -------------------

trait Shape {
    fn area(&self) -> f64;
    fn perimeter(&self) -> f64;
    fn name(&self) -> &str;
}

struct Circle {
    radius: f64,
}
struct Rectangle {
    width: f64,
    height: f64,
}
struct Triangle {
    a: f64,
    b: f64,
    c: f64,
}

impl Shape for Circle {
    fn area(&self) -> f64 {
        return std::f64::consts::PI * self.radius * self.radius;
    }
    fn perimeter(&self) -> f64 {
        return 2.0 * std::f64::consts::PI * self.radius;
    }
    fn name(&self) -> &str {
        return "circle";
    }
}

impl Shape for Rectangle {
    fn area(&self) -> f64 {
        return self.width * self.height;
    }
    fn perimeter(&self) -> f64 {
        return 2.0 * (self.width + self.height);
    }
    fn name(&self) -> &str {
        return "rectangle";
    }
}

impl Shape for Triangle {
    fn area(&self) -> f64 {
        let s: f64 = (self.a + self.b + self.c) / 2.0; // Heron's formula
        return (s * (s - self.a) * (s - self.b) * (s - self.c)).sqrt();
    }
    fn perimeter(&self) -> f64 {
        return self.a + self.b + self.c;
    }
    fn name(&self) -> &str {
        return "triangle";
    }
}

// ------------------- Multiple trait bounds -------------------

fn print_info<T: std::fmt::Display + std::fmt::Debug>(item: T) {
    println!("Display={:<15}  Debug={:?}", format!("{}", item), item);
}

// ------------------- Supertraits -------------------

// Printable can only be implemented by types that also implement Display
trait Printable: std::fmt::Display {
    fn pretty_print(&self) {
        println!("[[ {} ]]", self);
    }
}

// ------------------- Blanket implementation -------------------

// Implement Printable for ALL types that already implement Display
// This is how std does: impl<T: Iterator> IntoIterator for T
impl<T: std::fmt::Display> Printable for T {}

// ------------------- Trait with associated constants -------------------

trait Describable {
    const KIND: &'static str;

    fn describe(&self) -> String;

    // where Self: Sized means this method is excluded from the vtable
    // (can't be called via dyn Describable, but works on concrete types)
    fn kind() -> &'static str
    where
        Self: Sized,
    {
        return Self::KIND;
    }
}

struct Car {
    brand: String,
}
struct Bike {
    gears: u32,
}

impl Describable for Car {
    const KIND: &'static str = "vehicle";
    fn describe(&self) -> String {
        return format!("Car({})", self.brand);
    }
}

impl Describable for Bike {
    const KIND: &'static str = "vehicle";
    fn describe(&self) -> String {
        return format!("Bike({} gears)", self.gears);
    }
}

// ------------------- Object safety -------------------

// A trait is object-safe if it can be used as dyn Trait
// Requirements: no generic methods, no Self in return types, no associated consts (usually)
// The `where Self: Sized` guard excludes a method from the vtable

// NOT object-safe (Clone returns Self):
// ERROR: Box<dyn Clone>  - Clone is not object-safe
// fn takes_clone(x: &dyn Clone) {}

// Object-safe wrapper trait:
trait CloneBox: Shape {
    fn clone_box(&self) -> Box<dyn Shape>;
}

pub fn run() {
    print_h2!("Traits");
    print_h3!("Basic traits");

    let en: English = English;
    let es: Spanish = Spanish;
    println!("English: {} | {}", en.hello(), en.goodbye()); // goodbye uses default
    println!("Spanish: {} | {}", es.hello(), es.goodbye()); // goodbye is overridden

    print_h3!("impl Trait (static dispatch)");

    // Zero runtime cost - compiler generates specialized code per type
    greet_once(&en);
    greet_once(&es);

    let greeter = make_greeter(); // concrete type is hidden (impl Trait in let is unstable)
    println!("make_greeter() says: {}", greeter.hello());

    print_h3!("dyn Trait (dynamic dispatch)");

    // &dyn Trait is a fat pointer: 16 bytes on 64-bit (ptr + vtable)
    greet_dynamic(&en);
    greet_dynamic(&es);

    let boxed: Box<dyn Greet> = make_greeter_dynamic(true);
    println!("Box<dyn Greet>: {}", boxed.hello());

    // impl Trait vs dyn Trait:
    //   impl Trait - compile-time dispatch, monomorphized, faster, but no heterogeneous collections
    //   dyn Trait  - runtime dispatch via vtable, slight overhead, allows Vec<Box<dyn Trait>>
    println!(
        "size_of::<&dyn Greet>()  = {} bytes (fat pointer)",
        std::mem::size_of::<&dyn Greet>()
    );
    println!(
        "size_of::<&English>()    = {} bytes (thin pointer)",
        std::mem::size_of::<&English>()
    );

    print_h3!("Heterogeneous collections");

    let shapes: Vec<Box<dyn Shape>> = vec![
        Box::new(Circle { radius: 3.0 }),
        Box::new(Rectangle {
            width: 4.0,
            height: 5.0,
        }),
        Box::new(Triangle {
            a: 3.0,
            b: 4.0,
            c: 5.0,
        }),
        Box::new(Circle { radius: 1.0 }),
    ];

    for s in &shapes {
        println!(
            "{}: area={:.3}  perimeter={:.3}",
            s.name(),
            s.area(),
            s.perimeter()
        );
    }

    let total_area: f64 = shapes.iter().map(|s| s.area()).sum();
    let largest: &Box<dyn Shape> = shapes
        .iter()
        .max_by(|a, b| a.area().partial_cmp(&b.area()).unwrap())
        .unwrap();
    println!("Total area = {:.3}", total_area);
    println!("Largest shape = {}", largest.name());

    print_h3!("Multiple bounds");

    print_info(42_u32);
    print_info("ferris");
    print_info(3.14_f64); // Vec doesn't impl Display - only types with both bounds work

    print_h3!("Supertraits");

    // i32, &str, f64 all impl Display -> blanket impl gives them Printable
    42_i32.pretty_print();
    "hello".pretty_print();
    3.14_f64.pretty_print();

    print_h3!("Blanket implementation");

    // impl<T: Display> Printable for T covers everything with Display
    // std uses this pattern: impl<T: Error> From<T> for Box<dyn Error>
    println!("true.pretty_print():");
    true.pretty_print();
    println!("'Z'.pretty_print():");
    'Z'.pretty_print();

    print_h3!("Associated constants + where Self: Sized");

    let car: Car = Car {
        brand: String::from("Ferris Motors"),
    };
    let bike: Bike = Bike { gears: 21 };

    println!("{}", car.describe());
    println!("{}", bike.describe());
    println!("Car::KIND  = {}", Car::kind());
    println!("Bike::KIND = {}", Bike::kind());

    print_h3!("Object safety");

    // Object-safe: methods take &self or &mut self, don't use generic params, don't return Self
    // Not object-safe: Clone (returns Self), any method with type params
    // `where Self: Sized` on a method excludes it from the vtable, making the trait object-safe
    println!("Clone is not object-safe (returns Self)");
    println!("Iterator is object-safe (next() returns Option<Self::Item>, not Self)");

    let v: Vec<Box<dyn std::fmt::Debug>> =
        vec![Box::new(1i32), Box::new("hello"), Box::new(3.14f64)];
    for item in &v {
        println!("{:?}", item); // Debug is object-safe
    }
}
