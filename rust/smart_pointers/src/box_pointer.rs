use shared::{print_h2, print_h3};

pub fn run() {
    print_h2!("Box<T>");

    print_h3!("Heap allocation");
    // Box allocates on heap instead of stack
    let boxed: Box<i32> = Box::new(5);
    println!("Boxed value: {}", boxed);

    // Automatically dereferenced
    let unboxed: i32 = *boxed;
    println!("Unboxed: {}", unboxed);

    print_h3!("Why use Box?");
    // 1. Large data that would overflow stack
    let large_array: Box<[i32; 1_000_000]> = Box::new([0; 1_000_000]);
    println!("Large array on heap, len: {}", large_array.len());

    // 2. Transfer ownership without copying
    let data: Box<Vec<i32>> = Box::new(vec![1, 2, 3, 4, 5]);
    let moved: Box<Vec<i32>> = data; // Ownership transferred, no data copy
    println!("Moved box: {:?}", moved);

    // 3. Trait objects (dynamic dispatch)
    trait Drawable {
        fn draw(&self);
    }

    struct Circle {
        radius: f64,
    }

    impl Drawable for Circle {
        fn draw(&self) {
            println!("  Drawing circle, radius: {}", self.radius);
        }
    }

    let shape: Box<dyn Drawable> = Box::new(Circle { radius: 5.0 });
    shape.draw();

    print_h3!("Recursive types");
    // Without Box, the compiler can't know List's size (it would be infinite).
    // Box breaks the recursion: the enum variant holds a pointer (known size) instead of the full type.
    #[derive(Debug)]
    enum List {
        Cons(i32, Box<List>),
        Nil,
    }

    let list: List = List::Cons(
        1,
        Box::new(List::Cons(2, Box::new(List::Cons(3, Box::new(List::Nil))))),
    );
    println!("\nRecursive list: {:?}", list);

    // Binary tree with Box
    #[derive(Debug)]
    struct TreeNode {
        value: i32,
        left: Option<Box<TreeNode>>,
        right: Option<Box<TreeNode>>,
    }

    let tree: TreeNode = TreeNode {
        value: 10,
        left: Some(Box::new(TreeNode {
            value: 5,
            left: None,
            right: None,
        })),
        right: Some(Box::new(TreeNode {
            value: 15,
            left: None,
            right: None,
        })),
    };
    println!("Tree: {:?}", tree);

    print_h3!("Deref coercion");
    // Box implements Deref, auto-converts to reference
    let boxed_string: Box<String> = Box::new(String::from("hello"));
    let len: usize = boxed_string.len(); // Auto-deref to &String
    println!("\nBoxed string len: {}", len);

    fn takes_str(s: &str) {
        println!("  Got: {}", s);
    }

    takes_str(&boxed_string); // Box<String> -> &String -> &str

    print_h3!("Drop trait");
    // Box implements Drop, frees heap memory when dropped
    {
        let _temp: Box<i32> = Box::new(42);
        println!("\nBox created in scope");
    } // Box dropped here, heap memory freed
    println!("Box dropped, memory freed");

    print_h3!("Box::leak");
    // Box::leak gives a &'static reference by intentionally forgetting the Box.
    // The memory is never freed. Use sparingly — mainly for initializing static data
    // from runtime values, or for passing heap data to a C library.
    let leaked: &'static mut i32 = Box::leak(Box::new(100));
    *leaked += 1;
    println!("\nLeaked value: {}", leaked);
    // Memory never freed (intentional leak)

    print_h3!("Box::from_raw");
    // Box::into_raw transfers ownership to a raw pointer (Box is forgotten, no drop).
    // Box::from_raw reconstructs the Box — the caller must ensure the pointer came from
    // Box::into_raw and is not aliased; calling from_raw twice = double-free (UB).
    let boxed2: Box<i32> = Box::new(50);
    let raw: *mut i32 = Box::into_raw(boxed2);
    println!("\nRaw pointer: {:?}", raw);

    unsafe {
        let reconstructed: Box<i32> = Box::from_raw(raw);
        println!("Reconstructed: {}", reconstructed);
        // Box dropped here, memory freed
    }

    print_h3!("Box with DST");
    // Box can hold slices
    let slice: Box<[i32]> = Box::new([1, 2, 3, 4, 5]);
    println!("\nBoxed slice: {:?}", slice);

    // Box with str
    let string_slice: Box<str> = String::from("boxed str").into_boxed_str();
    println!("Boxed str: {}", string_slice);

    print_h3!("Box::new vs Box::default");
    let box_new: Box<Vec<i32>> = Box::new(Vec::new());
    let box_default: Box<Vec<i32>> = Box::default();
    println!("\nBox::new: {:?}, Box::default: {:?}", box_new, box_default);

    print_h3!("Pattern matching");
    let maybe_boxed: Option<Box<i32>> = Some(Box::new(99));
    match maybe_boxed {
        Some(boxed_val) => println!("\nGot boxed: {}", boxed_val),
        None => println!("No value"),
    }

    print_h3!("Moving out of Box");
    let boxed3: Box<String> = Box::new(String::from("owned"));
    let owned: String = *boxed3; // Move out, Box is consumed
    println!("\nMoved out: {}", owned);
    // ERROR: boxed3 is moved
    // println!("{}", boxed3); // Would fail

    print_h3!("Box with custom types");
    struct LargeStruct {
        data: [u8; 1000],
    }

    impl LargeStruct {
        fn new() -> Box<LargeStruct> {
            return Box::new(LargeStruct { data: [0; 1000] });
        }
    }

    let large: Box<LargeStruct> = LargeStruct::new();
    println!(
        "\nLarge struct on heap, size: {}",
        std::mem::size_of_val(&*large)
    );

    print_h3!("Stack vs Heap comparison");
    // Stack: fast, fixed size, automatic cleanup
    let stack_val: i32 = 42;
    println!("\nStack value: {}", stack_val);

    // Heap: slower, dynamic size, manual control
    let heap_val: Box<i32> = Box::new(42);
    println!("Heap value: {}", heap_val);

    print_h3!("Box as function return");
    fn make_box(value: i32) -> Box<i32> {
        return Box::new(value * 2);
    }

    let result: Box<i32> = make_box(21);
    println!("\nFunction returned box: {}", result);

    print_h3!("Box with closures");
    let closure: Box<dyn Fn(i32) -> i32> = Box::new(|x| x * 2);
    let doubled: i32 = closure(5);
    println!("\nBoxed closure result: {}", doubled);
}
