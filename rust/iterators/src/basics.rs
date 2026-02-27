use shared::{print_h2, print_h3};

pub fn run() {
    print_h2!("Iterator Basics");

    print_h3!("Three iteration methods");
    // iter() - immutable borrow (&T)
    // iter_mut() - mutable borrow (&mut T)
    // into_iter() - takes ownership (T)

    let vec: Vec<i32> = vec![1, 2, 3, 4, 5];

    // iter() - borrows elements
    println!("iter() - immutable borrow:");
    for item in vec.iter() {
        println!("  &{}", item);
    }
    println!("vec still valid: {:?}", vec);

    // iter_mut() - mutable borrow
    let mut vec_mut: Vec<i32> = vec![1, 2, 3, 4, 5];
    println!("\niter_mut() - mutable borrow:");
    for item in vec_mut.iter_mut() {
        *item *= 2;
    }
    println!("After doubling: {:?}", vec_mut);

    // into_iter() - takes ownership
    let vec2: Vec<i32> = vec![10, 20, 30];
    println!("\ninto_iter() - takes ownership:");
    for item in vec2.into_iter() {
        println!("  {}", item);
    }
    // ERROR: vec2 is moved
    // println!("{:?}", vec2); // Would fail

    print_h3!("For loop desugaring");
    // A for loop calls IntoIterator::into_iter() on the expression, then repeatedly calls next().
    // `for x in &arr` desugars to: let mut iter = arr.iter(); while let Some(x) = iter.next() { ... }
    let arr: [i32; 3] = [1, 2, 3];

    // These are equivalent:
    println!("\nFor loop:");
    for x in &arr {
        print!("{} ", x);
    }
    println!();

    println!("Explicit iterator:");
    let mut iter = arr.iter();
    while let Some(x) = iter.next() {
        print!("{} ", x);
    }
    println!();

    print_h3!("Iterator trait");
    // All iterators implement Iterator trait with next() method
    let vec3: Vec<i32> = vec![1, 2, 3];
    let mut iter: std::slice::Iter<i32> = vec3.iter();

    let first: Option<&i32> = iter.next();
    let second: Option<&i32> = iter.next();
    let third: Option<&i32> = iter.next();
    let fourth: Option<&i32> = iter.next();

    println!("\nManual next() calls:");
    println!("1st: {:?}", first);
    println!("2nd: {:?}", second);
    println!("3rd: {:?}", third);
    println!("4th: {:?}", fourth); // None - exhausted

    print_h3!("Iterating over different types");
    // Vec
    let v: Vec<i32> = vec![1, 2, 3];
    let sum: i32 = v.iter().sum();
    println!("\nVec sum: {}", sum);

    // Array
    let a: [i32; 4] = [1, 2, 3, 4];
    let product: i32 = a.iter().product();
    println!("Array product: {}", product);

    // Slice
    let slice: &[i32] = &[5, 6, 7];
    let count: usize = slice.iter().count();
    println!("Slice count: {}", count);

    // String chars
    let s: String = String::from("hello");
    let char_count: usize = s.chars().count();
    println!("String chars: {}", char_count);

    // Range
    let range_sum: i32 = (1..=10).sum();
    println!("Range 1..=10 sum: {}", range_sum);

    // HashMap
    use std::collections::HashMap;
    let mut map: HashMap<&str, i32> = HashMap::new();
    map.insert("a", 1);
    map.insert("b", 2);
    println!("\nHashMap iteration:");
    for (key, value) in &map {
        println!("  {} = {}", key, value);
    }

    // HashSet
    use std::collections::HashSet;
    let set: HashSet<i32> = HashSet::from([1, 2, 3]);
    println!("\nHashSet iteration:");
    for item in &set {
        println!("  {}", item);
    }

    print_h3!("Consuming vs non-consuming");
    let vec4: Vec<i32> = vec![1, 2, 3];

    // Non-consuming: borrows
    let _first: Option<&i32> = vec4.iter().next();
    let _last: Option<&i32> = vec4.iter().last();
    println!("vec4 still valid: {:?}", vec4);

    // Consuming: takes ownership
    let vec5: Vec<i32> = vec![4, 5, 6];
    let collected: Vec<i32> = vec5.into_iter().collect();
    println!("Consumed and collected: {:?}", collected);
    // ERROR: vec5 is moved

    print_h3!("Lazy evaluation");
    // Iterators are lazy - nothing happens until consumed
    let vec6: Vec<i32> = vec![1, 2, 3, 4, 5];

    let _lazy = vec6.iter().map(|x| {
        println!("  This won't print!");
        return x * 2;
    });
    println!("Created lazy iterator, but nothing printed");

    // Consuming triggers evaluation
    let _result: Vec<i32> = vec6
        .iter()
        .map(|x| {
            println!("  Processing {}", x);
            return x * 2;
        })
        .collect();
    println!("After collect(), processing happened");

    print_h3!("Cloned and copied");
    let vec7: Vec<i32> = vec![1, 2, 3];

    // iter() gives &i32, use copied() to get i32
    let doubled: Vec<i32> = vec7.iter().copied().map(|x| x * 2).collect();
    println!("\nCopied and doubled: {:?}", doubled);

    // For non-Copy types, use cloned()
    let strings: Vec<String> = vec![String::from("a"), String::from("b")];
    let cloned: Vec<String> = strings.iter().cloned().collect();
    println!("Cloned strings: {:?}", cloned);
    println!("Original still valid: {:?}", strings);

    print_h3!("Iterator size hints");
    let vec8: Vec<i32> = vec![1, 2, 3, 4, 5];
    let iter = vec8.iter();
    let (lower, upper): (usize, Option<usize>) = iter.size_hint();
    println!("\nSize hint: lower={}, upper={:?}", lower, upper);

    print_h3!("Infinite iterators");
    // Some iterators are infinite (use take() to limit)
    let infinite = std::iter::repeat(42);
    let first_5: Vec<i32> = infinite.take(5).collect();
    println!("\nFirst 5 from infinite repeat: {:?}", first_5);

    // Range without end is infinite
    let counting = (1..).take(10).collect::<Vec<i32>>();
    println!("First 10 counting: {:?}", counting);
}
