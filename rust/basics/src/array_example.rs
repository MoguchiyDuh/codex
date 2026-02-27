use shared::{get_type, print_h2, print_h3};

pub fn run() {
    print_h2!("Arrays & Slices");

    print_h3!("Creation");
    let _arr1: [i32; 5] = [1, 2, 3, 4, 5];
    let _arr2: [i32; 10] = [0; 10]; // Repeat syntax
    // from_fn initializes each element via closure receiving its index; size inferred from type
    let _arr3: [i32; 4] = std::array::from_fn(|i: usize| (i * 2) as i32);
    let mut arr: [i32; 6] = [5, 2, 8, 1, 9, 3];
    println!("Initial: {:?}", arr);

    print_h3!("Indexing");
    println!("Direct indexing arr[0]: {}", arr[0]); // Panics if out of bounds
    arr[0] = 10;
    println!("After arr[0] = 10: {:?}", arr);

    // .get() provides safe access
    let safe_access: Option<&i32> = arr.get(2);
    let out_of_bounds: Option<&i32> = arr.get(99);
    println!("get(2): {:?}, get(99): {:?}", safe_access, out_of_bounds);

    print_h3!("Properties");
    println!("len: {}, is_empty: {}", arr.len(), arr.is_empty());
    println!("first: {:?}, last: {:?}", arr.first(), arr.last());
    println!("contains(&8): {}", arr.contains(&8));

    print_h3!("Slicing");
    let slice: &[i32] = &arr[1..4];
    println!("Slice [1..4]: {:?}", slice);

    let (left, right): (&[i32], &[i32]) = arr.split_at(3);
    println!("split_at(3): {:?} | {:?}", left, right);

    print_h3!("Iteration");
    print!("iter: ");
    for item in arr.iter() {
        print!("{} ", item);
    }
    println!();

    print!("enumerate: ");
    for (idx, val) in arr.iter().enumerate() {
        print!("[{}]={} ", idx, val);
    }
    println!();

    print!("windows(3): ");
    for window in arr.windows(3) {
        print!("{:?} ", window);
    }
    println!();

    print!("chunks(2): ");
    for chunk in arr.chunks(2) {
        print!("{:?} ", chunk);
    }
    println!();

    print_h3!("Mutation");
    let mut test: [i32; 5] = [1, 2, 3, 4, 5];
    test.reverse();
    println!("reverse: {:?}", test);

    test.rotate_left(2);
    println!("rotate_left(2): {:?}", test);

    test.fill(7);
    println!("fill(7): {:?}", test);

    print_h3!("Sorting & Searching");
    arr.sort();
    println!("sort: {:?}", arr);

    arr.sort_unstable();
    println!("sort_unstable: {:?}", arr);

    let target: i32 = 8;
    match arr.binary_search(&target) {
        Ok(idx) => println!("binary_search(8): found at {}", idx),
        Err(idx) => println!("binary_search(8): would insert at {}", idx),
    }
    // NOTE: binary_search requires sorted array, otherwise results undefined

    print_h3!("Mutation iter");
    let mut modify: [i32; 4] = [1, 2, 3, 4];
    for item in modify.iter_mut() {
        *item *= 2;
    }
    println!("iter_mut (doubled): {:?}", modify);

    print_h3!("Swap");
    let mut swap_test: [i32; 3] = [10, 20, 30];
    swap_test.swap(0, 2);
    println!("swap(0, 2): {:?}", swap_test);

    print_h3!("Copy operations");
    let mut dest: [i32; 3] = [0; 3];
    let src: [i32; 3] = [7, 8, 9];
    dest.copy_from_slice(&src);
    println!("copy_from_slice: {:?}", dest);

    print_h3!("Conversion");
    let as_vec: Vec<i32> = arr.to_vec();
    println!("to_vec: {:?} (Type: {})", as_vec, get_type(&as_vec));

    let as_slice: &[i32] = arr.as_slice();
    println!("as_slice type: {}", get_type(&as_slice));
}
