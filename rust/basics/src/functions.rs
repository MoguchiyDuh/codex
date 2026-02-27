use shared::{print_h2, print_h3};

pub fn run() {
    print_h2!("Functions");

    print_h3!("Basic functions");
    hello_world();
    greet("Kirill");

    let sum: i32 = add(10, 5);
    println!("add(10, 5) = {}", sum);

    let product: i32 = multiply(10, 5);
    println!("multiply(10, 5) = {}", product);

    print_h3!("Multiple return values");
    let (x, y): (i32, i32) = swap(1, 2);
    println!("swap(1, 2) = ({}, {})", x, y);

    let (quot, rem): (i32, i32) = div_mod(17, 5);
    println!("div_mod(17, 5) = ({}, {})", quot, rem);

    print_h3!("Early returns");
    println!("classify(-5) = {}", classify(-5));
    println!("classify(0) = {}", classify(0));
    println!("classify(10) = {}", classify(10));

    print_h3!("Optional parameters (via Option)");
    println!(
        "greet_opt(Some('Mr.'), 'John') = {}",
        greet_opt(Some("Mr."), "John")
    );
    println!("greet_opt(None, 'Jane') = {}", greet_opt(None, "Jane"));

    print_h3!("Variadic-like (via slice)");
    println!("sum_all([1, 2, 3, 4, 5]) = {}", sum_all(&[1, 2, 3, 4, 5]));
    println!("sum_all([]) = {}", sum_all(&[]));

    print_h3!("const fn (compile-time eval)");
    // const fn can be evaluated at compile time when used in a const context.
    // The result is embedded directly into the binary — zero runtime cost.
    const FACTORIAL_5: u32 = factorial(5);
    println!("const factorial(5) = {}", FACTORIAL_5);

    print_h3!("Methods (impl blocks)");
    let mut rect: Rectangle = Rectangle::new(10, 20);
    println!("Rectangle::new(10, 20) area={}", rect.area());
    println!(
        "Rectangle can_hold(5x5)? {}",
        rect.can_hold(&Rectangle::new(5, 5))
    );
    rect.scale(2);
    println!("After scale(2): {}x{}", rect.width, rect.height);

    print_h3!("Associated functions");
    let square: Rectangle = Rectangle::square(10);
    println!("Rectangle::square(10) = {}x{}", square.width, square.height);

    print_h3!("Generic functions");
    println!("max_generic(10, 20) = {}", max_generic(10, 20));
    println!("max_generic(3.14, 2.71) = {}", max_generic(3.14, 2.71));

    print_debug(42);
    print_debug("hello");
    print_debug(vec![1, 2, 3]);

    print_h3!("Higher-order functions");
    let result: i32 = operation(10, 5, add);
    println!("operation(10, 5, add) = {}", result);

    let result2: i32 = apply(|x: i32| x * 2, 10);
    println!("apply(|x| x*2, 10) = {}", result2);

    print_h3!("Closures: Fn, FnMut, FnOnce");
    let add_five = |x: i32| -> i32 {
        return x + 5;
    };
    println!("Closure add_five(10) = {}", add_five(10));

    let nums: [i32; 5] = [1, 2, 3, 4, 5];
    let squared: Vec<i32> = nums.iter().map(|&x: &i32| x * x).collect();
    println!("map squared: {:?}", squared);

    // FnMut: closure borrows captured variable mutably — can only call when you have &mut closure
    // The closure type hierarchy: FnOnce ⊇ FnMut ⊇ Fn (every Fn is also FnMut and FnOnce)
    let mut counter: i32 = 0;
    let mut increment = || {
        counter += 1;
        return counter;
    };
    println!("FnMut increment: {}", increment());
    println!("FnMut increment: {}", increment());

    // FnOnce: closure moves (consumes) a captured value — can only be called once
    // 'move' keyword forces capture by move even if the closure only borrows
    let text: String = String::from("consumed");
    let consume = move || {
        println!("FnOnce consumed: {}", text); // text moved into closure
    };
    consume(); // text is dropped at end of consume()

    // Fn: borrows captured variable immutably — can be called any number of times
    let value: i32 = 100;
    let borrow = || {
        println!("Fn borrowed: {}", value);
    };
    borrow();
    println!("Value still accessible: {}", value); // value not consumed

    print_h3!("Diverging functions (never type !)");
    let choice: i32 = 1;
    // The never type `!` coerces to any type, so panic_example() (returning !)
    // can appear in a branch expecting i32. The compiler knows it never produces a value.
    let result: i32 = if choice == 0 {
        panic_example() // PANIC: Would panic if choice == 0
    } else {
        42
    };
    println!("Diverging function result: {}", result);
}

fn hello_world() {
    println!("Hello, world!");
}

fn greet(name: &str) {
    println!("Hello, {}!", name);
}

fn add(a: i32, b: i32) -> i32 {
    return a + b;
}

fn multiply(a: i32, b: i32) -> i32 {
    return a * b;
}

fn swap(a: i32, b: i32) -> (i32, i32) {
    return (b, a);
}

fn div_mod(a: i32, b: i32) -> (i32, i32) {
    return (a / b, a % b);
}

fn classify(n: i32) -> &'static str {
    if n < 0 {
        return "negative";
    }
    if n == 0 {
        return "zero";
    }
    return "positive";
}

fn greet_opt(title: Option<&str>, name: &str) -> String {
    if let Some(t) = title {
        return format!("{} {}", t, name);
    }
    return format!("{}", name);
}

fn sum_all(numbers: &[i32]) -> i32 {
    let mut total: i32 = 0;
    for &num in numbers {
        total += num;
    }
    return total;
}

const fn factorial(n: u32) -> u32 {
    if n == 0 {
        return 1;
    }
    return n * factorial(n - 1);
}

struct Rectangle {
    width: u32,
    height: u32,
}

impl Rectangle {
    fn new(width: u32, height: u32) -> Self {
        return Self { width, height };
    }

    fn square(size: u32) -> Self {
        return Self::new(size, size);
    }

    fn area(&self) -> u32 {
        return self.width * self.height;
    }

    fn can_hold(&self, other: &Rectangle) -> bool {
        return self.width > other.width && self.height > other.height;
    }

    fn scale(&mut self, factor: u32) {
        self.width *= factor;
        self.height *= factor;
    }
}

fn max_generic<T: PartialOrd>(a: T, b: T) -> T {
    if a > b {
        return a;
    }
    return b;
}

fn print_debug<T: std::fmt::Debug>(value: T) {
    println!("Debug: {:?}", value);
}

// fn(i32, i32) -> i32 is a function pointer type — a plain address, no captured state
// Unlike closures (Fn/FnMut/FnOnce), function pointers are always Copy and have no environment
fn operation(a: i32, b: i32, op: fn(i32, i32) -> i32) -> i32 {
    return op(a, b);
}

fn apply<F>(f: F, value: i32) -> i32
where
    F: Fn(i32) -> i32,
{
    return f(value);
}

fn panic_example() -> ! {
    panic!("This function never returns!");
}
