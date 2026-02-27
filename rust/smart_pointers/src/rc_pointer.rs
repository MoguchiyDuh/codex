use shared::{print_h2, print_h3};
use std::rc::{Rc, Weak};

pub fn run() {
    print_h2!("Rc<T> & Weak<T>");

    print_h3!("Basic Rc usage");
    // Rc enables multiple ownership (single-threaded only)
    let data: Rc<String> = Rc::new(String::from("shared data"));
    println!("Created Rc, strong count: {}", Rc::strong_count(&data));

    let ref1: Rc<String> = Rc::clone(&data);
    let ref2: Rc<String> = Rc::clone(&data);
    println!("After 2 clones, strong count: {}", Rc::strong_count(&data));

    println!("All refs can read: {}, {}, {}", data, ref1, ref2);

    print_h3!("Reference counting");
    {
        let ref3: Rc<String> = Rc::clone(&data);
        println!("\nIn scope, strong count: {}", Rc::strong_count(&ref3));
    } // ref3 dropped, count decremented
    println!("After scope, strong count: {}", Rc::strong_count(&data));

    drop(ref1);
    println!(
        "After drop(ref1), strong count: {}",
        Rc::strong_count(&data)
    );

    print_h3!("Rc is immutable by default");
    let numbers: Rc<Vec<i32>> = Rc::new(vec![1, 2, 3]);
    // ERROR: Can't mutate through Rc
    // numbers.push(4); // Would fail: Rc is immutable

    // Can read from all references
    println!("\nShared vec: {:?}", numbers);

    print_h3!("Sharing across data structures");
    #[derive(Debug)]
    struct Node {
        value: i32,
        parent: Option<Rc<Node>>,
    }

    let parent: Rc<Node> = Rc::new(Node {
        value: 10,
        parent: None,
    });

    let child1: Node = Node {
        value: 20,
        parent: Some(Rc::clone(&parent)),
    };

    let child2: Node = Node {
        value: 30,
        parent: Some(Rc::clone(&parent)),
    };

    println!("\nParent strong count: {}", Rc::strong_count(&parent));
    println!("Child1 parent: {:?}", child1.parent.as_ref().unwrap().value);
    println!("Child2 parent: {:?}", child2.parent.as_ref().unwrap().value);

    print_h3!("Weak references");
    // Weak<T> holds a non-owning reference — does NOT increment the strong count.
    // The allocation is freed when strong count hits 0, regardless of weak count.
    // Use Weak to break reference cycles (e.g. parent-child trees where both hold Rc).
    let strong: Rc<i32> = Rc::new(42);
    let weak: Weak<i32> = Rc::downgrade(&strong);

    println!(
        "\nStrong count: {}, Weak count: {}",
        Rc::strong_count(&strong),
        Rc::weak_count(&strong)
    );

    // Upgrade Weak to Rc (returns Option)
    match weak.upgrade() {
        Some(rc) => println!("Weak upgraded: {}", rc),
        None => println!("Value was dropped"),
    }

    drop(strong);

    // After dropping strong ref, weak can't upgrade
    match weak.upgrade() {
        Some(rc) => println!("Weak upgraded: {}", rc),
        None => println!("Value was dropped (strong refs gone)"),
    }

    print_h3!("Preventing reference cycles");
    #[derive(Debug)]
    struct TreeNode {
        value: i32,
        parent: Option<Weak<TreeNode>>, // Weak to prevent cycle
        children: Vec<Rc<TreeNode>>,
    }

    let leaf: Rc<TreeNode> = Rc::new(TreeNode {
        value: 3,
        parent: None,
        children: vec![],
    });

    println!(
        "\nLeaf strong: {}, weak: {}",
        Rc::strong_count(&leaf),
        Rc::weak_count(&leaf)
    );

    // Parent holds strong refs to children, children hold weak refs to parent
    // This prevents memory leak from circular references

    print_h3!("try_unwrap");
    // Extract value if only one strong reference exists
    let single: Rc<String> = Rc::new(String::from("unique"));
    match Rc::try_unwrap(single) {
        Ok(value) => println!("\nUnwrapped: {}", value),
        Err(rc) => println!("Still has {} refs", Rc::strong_count(&rc)),
    }

    let shared: Rc<String> = Rc::new(String::from("shared"));
    let _clone: Rc<String> = Rc::clone(&shared);
    match Rc::try_unwrap(shared) {
        Ok(value) => println!("Unwrapped: {}", value),
        Err(rc) => println!("Can't unwrap, {} refs remain", Rc::strong_count(&rc)),
    }

    print_h3!("get_mut");
    // Rc::get_mut succeeds only when strong_count == 1 (no other owners).
    // This is the safe way to mutate Rc data without RefCell — no runtime borrow checks.
    let mut unique: Rc<String> = Rc::new(String::from("mutable"));
    if let Some(value) = Rc::get_mut(&mut unique) {
        value.push_str(" modified");
        println!("\nModified via get_mut: {}", value);
    }

    let shared2: Rc<String> = Rc::new(String::from("shared"));
    let mut shared2_mut: Rc<String> = Rc::clone(&shared2);
    if let Some(value) = Rc::get_mut(&mut shared2_mut) {
        value.push_str(" modified");
    } else {
        println!("Can't get_mut, multiple refs exist");
    }

    print_h3!("Rc::ptr_eq");
    // Check if two Rc point to same allocation
    let rc1: Rc<i32> = Rc::new(10);
    let rc2: Rc<i32> = Rc::clone(&rc1);
    let rc3: Rc<i32> = Rc::new(10);

    println!("\nrc1 and rc2 same? {}", Rc::ptr_eq(&rc1, &rc2)); // true
    println!("rc1 and rc3 same? {}", Rc::ptr_eq(&rc1, &rc3)); // false

    print_h3!("Rc with methods");
    let rc_vec: Rc<Vec<i32>> = Rc::new(vec![1, 2, 3, 4, 5]);
    let sum: i32 = rc_vec.iter().sum();
    println!("\nRc<Vec> sum: {}", sum);

    print_h3!("Weak counts");
    let strong2: Rc<i32> = Rc::new(100);
    let weak2: Weak<i32> = Rc::downgrade(&strong2);
    let weak3: Weak<i32> = Rc::downgrade(&strong2);

    println!("\nStrong count via Weak: {}", weak2.strong_count());
    println!("Weak count via Weak: {}", weak2.weak_count());

    drop(strong2);
    println!("After drop, strong count: {}", weak3.strong_count());

    print_h3!("Performance notes");
    // Rc has overhead: pointer + reference count
    // Clone is cheap (just increments counter)
    // Drop is cheap (just decrements counter)
    println!("\nRc size: {} bytes", std::mem::size_of::<Rc<i32>>());
    println!("&i32 size: {} bytes", std::mem::size_of::<&i32>());
}
