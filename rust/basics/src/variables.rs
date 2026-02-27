use shared::{print_h2, print_h3};

pub fn run() {
    print_h2!("Variables");

    print_h3!("let (immutable by default)");
    let x: i32 = 5;
    println!("x: {}", x);
    // ERROR: Cannot mutate immutable variable
    // x = 6; // Would fail: "cannot assign twice to immutable variable"

    print_h3!("let mut");
    let mut y: i32 = 10;
    println!("y: {}", y);
    y = 20; // OK: variable is mutable
    println!("y after mutation: {}", y);

    print_h3!("Shadowing");
    // Shadowing: redeclaring same name creates NEW variable
    let z: i32 = 5;
    println!("z: {}", z);

    let z: i32 = z + 1; // Shadows previous z
    println!("z shadowed: {}", z);

    {
        let z: i32 = z * 2; // Shadows again in inner scope
        println!("z in inner scope: {}", z);
    }
    println!("z after inner scope: {}", z); // Outer shadow still valid

    // Shadowing can change type — unlike mut, which locks the type
    let spaces: &str = "   ";
    let spaces: usize = spaces.len(); // Different type, same name — new binding entirely
    println!("spaces: {}", spaces);

    // ERROR: Can't change type with mut
    // let mut count = "123";
    // count = count.len(); // Would fail: type mismatch

    print_h3!("const (compile-time constant)");
    const MAX_POINTS: u32 = 100_000;
    const PI: f64 = 3.14159;
    println!("MAX_POINTS: {}", MAX_POINTS);
    println!("PI: {}", PI);
    // Must be type-annotated, must be compile-time evaluable
    // Can't use mut, must be SCREAMING_SNAKE_CASE by convention

    print_h3!("static (global variable)");
    static GLOBAL_COUNT: i32 = 42;
    println!("GLOBAL_COUNT: {}", GLOBAL_COUNT);
    // static has a fixed memory address and lives for the entire program ('static lifetime)
    // Unlike const, static is not inlined — it has one location in memory
    // Can be mutable with unsafe: static mut (dangerous — UB if accessed from multiple threads)

    print_h3!("Type inference");
    let inferred = 42; // Compiler infers i32
    let inferred_float = 3.14; // Compiler infers f64
    println!("Inferred types: {} {}", inferred, inferred_float);

    // Can help compiler with type annotation
    let vec_inferred: Vec<i32> = Vec::new();
    println!("Vec inferred: {:?}", vec_inferred);

    print_h3!("Destructuring tuples");
    let tuple: (i32, f64, char) = (500, 6.4, 'A');
    let (a, b, c): (i32, f64, char) = tuple;
    println!("Destructured: a={} b={} c={}", a, b, c);

    // Ignoring with _
    let (first, _, third): (i32, f64, char) = tuple;
    println!("Partial destructure: {} {}", first, third);

    print_h3!("Destructuring arrays");
    let arr: [i32; 3] = [1, 2, 3];
    let [x1, x2, x3]: [i32; 3] = arr;
    println!("Array destructure: {} {} {}", x1, x2, x3);

    print_h3!("Destructuring structs");
    struct Point {
        x: i32,
        y: i32,
    }
    let p: Point = Point { x: 10, y: 20 };
    let Point { x: px, y: py } = p;
    println!("Struct destructure: px={} py={}", px, py);

    // Shorthand when names match
    let Point { x, y } = Point { x: 5, y: 15 };
    println!("Struct shorthand: x={} y={}", x, y);

    print_h3!("Variable scope");
    {
        let inner: i32 = 100;
        println!("inner scope: {}", inner);
    } // inner dropped here
    // ERROR: inner not in scope
    // println!("{}", inner); // Would fail: "not found in this scope"

    print_h3!("Unused variables");
    let _unused: i32 = 42; // _ prefix suppresses warning
    // Without _, compiler warns about unused variable

    print_h3!("Multiple declarations");
    let (a, b, c): (i32, i32, i32) = (1, 2, 3);
    println!("Multiple: a={} b={} c={}", a, b, c);

    print_h3!("Patterns in let");
    let opt: Option<i32> = Some(42);
    if let Some(value) = opt {
        println!("Pattern match in let: {}", value);
    }

    print_h3!("Reference patterns");
    let ref_val: i32 = 50;
    let r: &i32 = &ref_val;
    // &deref_val in pattern position peels off one layer of reference:
    // r is &i32, matching &deref_val gives deref_val: i32 (copied, since i32: Copy)
    let &deref_val = r; // Pattern destructure reference
    println!("Deref pattern: {}", deref_val);

    print_h3!("Mutable references");
    let mut mutable: i32 = 10;
    let r_mut: &mut i32 = &mut mutable;
    *r_mut += 5;
    println!("After mut ref: {}", mutable);
}
