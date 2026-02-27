use shared::{print_h2, print_h3};

pub fn run() {
    print_h2!("Loops");

    print_h3!("loop (infinite)");
    let mut counter: i32 = 0;
    loop {
        print!("{} ", counter);
        counter += 1;
        if counter >= 5 {
            break;
        }
    }
    println!();

    print_h3!("loop with return value");
    // loop is an expression: `break value` makes the whole loop evaluate to that value
    let mut n: i32 = 0;
    let result: i32 = loop {
        n += 1;
        if n == 10 {
            break n * 2; // Returns value from loop
        }
    };
    println!("loop returned: {}", result);

    print_h3!("while");
    let mut i: i32 = 0;
    while i < 5 {
        print!("{} ", i);
        i += 1;
    }
    println!();

    print_h3!("while let");
    let mut stack: Vec<i32> = vec![1, 2, 3];
    while let Some(top) = stack.pop() {
        print!("{} ", top);
    }
    println!();

    print_h3!("for with range");
    for i in 0..5 {
        print!("{} ", i);
    }
    println!();

    // Inclusive range
    for i in 0..=5 {
        print!("{} ", i);
    }
    println!();

    print_h3!("Range variants");
    print!("rev: ");
    // .rev() reverses the iteration order
    for i in (0..5).rev() {
        print!("{} ", i);
    }
    println!();

    print!("step_by(2): ");
    // .step_by(n) jumps by n each iteration
    for i in (0..10).step_by(2) {
        print!("{} ", i);
    }
    println!();

    print_h3!("for with arrays");
    let arr: [i32; 3] = [10, 20, 30];
    for item in arr {
        print!("{} ", item);
    }
    println!();
    // ERROR: arr moved, can't use after loop
    // println!("{:?}", arr); // Would fail

    print_h3!("for with iter (borrow)");
    let arr2: [i32; 3] = [40, 50, 60];
    for item in arr2.iter() {
        print!("{} ", item);
    }
    println!();
    println!("arr2 still valid: {:?}", arr2);

    print_h3!("for with iter_mut");
    let mut arr3: [i32; 3] = [1, 2, 3];
    for item in arr3.iter_mut() {
        *item *= 10;
    }
    println!("mutated: {:?}", arr3);

    print_h3!("enumerate");
    let names: [&str; 3] = ["Alice", "Bob", "Carol"];
    for (idx, name) in names.iter().enumerate() {
        println!("[{}] = {}", idx, name);
    }

    print_h3!("break and continue");
    for i in 0..10 {
        if i == 3 {
            continue; // Skip 3
        }
        if i == 7 {
            break; // Stop at 7
        }
        print!("{} ", i);
    }
    println!();

    print_h3!("Nested loops with labels");
    // Loop labels ('name:) allow break/continue to target an outer loop specifically
    'outer: for x in 0..3 {
        for y in 0..3 {
            print!("({},{}) ", x, y);
            if x == 1 && y == 1 {
                break 'outer; // Break outer loop
            }
        }
    }
    println!();

    print_h3!("Labeled continue");
    'outer2: for x in 0..3 {
        for y in 0..3 {
            if y == 1 {
                continue 'outer2; // Continue outer loop
            }
            print!("({},{}) ", x, y);
        }
    }
    println!();

    print_h3!("Iterator methods in loops");
    print!("skip(2): ");
    // .skip(n) bypasses the first n elements
    for i in (0..10).skip(2) {
        print!("{} ", i);
    }
    println!();

    print!("take(3): ");
    // .take(n) limits the iteration to the first n elements
    for i in (0..10).take(3) {
        print!("{} ", i);
    }
    println!();

    print!("skip(2).take(3): ");
    // Adapters can be chained: skip 2, then take the next 3
    for i in (0..10).skip(2).take(3) {
        print!("{} ", i);
    }
    println!();

    print_h3!("Infinite iterator with take");
    print!("cycle().take(8): ");
    let pattern: [i32; 3] = [1, 2, 3];
    // .cycle() repeats the iterator infinitely; must use .take() to bound it
    for item in pattern.iter().cycle().take(8) {
        print!("{} ", item);
    }
    println!();

    print_h3!("Loop control patterns");
    let mut found: bool = false;
    for i in 0..100 {
        if i == 42 {
            found = true;
            break;
        }
    }
    println!("Found 42: {}", found);

    print_h3!("Loop with collect");
    let doubled: Vec<i32> = (1..6).map(|x: i32| x * 2).collect();
    println!("map+collect: {:?}", doubled);

    print_h3!("Loop with filter");
    let evens: Vec<i32> = (0..10).filter(|x: &i32| x % 2 == 0).collect();
    println!("filter evens: {:?}", evens);
}
