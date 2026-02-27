use shared::{print_h2, print_h3};
use std::cell::{Cell, RefCell};
use std::rc::Rc;

pub fn run() {
    print_h2!("RefCell<T> & Cell<T>");

    print_h3!("RefCell<T> basic usage");
    // RefCell provides interior mutability (runtime borrow checking)
    let data: RefCell<i32> = RefCell::new(5);
    println!("Initial: {}", data.borrow());

    *data.borrow_mut() += 10;
    println!("After mutation: {}", data.borrow());

    print_h3!("Borrow rules (runtime checked)");
    let value: RefCell<String> = RefCell::new(String::from("hello"));

    // Multiple immutable borrows OK
    let r1 = value.borrow();
    let r2 = value.borrow();
    println!("\nTwo immutable borrows: {} {}", r1, r2);
    drop(r1);
    drop(r2);

    // Mutable borrow
    let mut r_mut = value.borrow_mut();
    r_mut.push_str(" world");
    println!("After mut borrow: {}", r_mut);
    drop(r_mut);

    // PANIC: Can't borrow while mutably borrowed
    // let _r_mut = value.borrow_mut();
    // let _r = value.borrow(); // Would panic at runtime

    print_h3!("try_borrow");
    // Safe alternative that returns Result
    let cell: RefCell<i32> = RefCell::new(10);

    let borrow1 = cell.try_borrow();
    match borrow1 {
        Ok(val) => println!("\ntry_borrow succeeded: {}", val),
        Err(_) => println!("try_borrow failed"),
    }

    let mut_borrow = cell.borrow_mut();
    match cell.try_borrow() {
        Ok(val) => println!("try_borrow succeeded: {}", val),
        Err(_) => println!("try_borrow failed (already mutably borrowed)"),
    }
    drop(mut_borrow);

    print_h3!("Rc<RefCell<T>> pattern");
    // Shared ownership + interior mutability
    let shared: Rc<RefCell<Vec<i32>>> = Rc::new(RefCell::new(vec![1, 2, 3]));

    let clone1: Rc<RefCell<Vec<i32>>> = Rc::clone(&shared);
    let clone2: Rc<RefCell<Vec<i32>>> = Rc::clone(&shared);

    // Both can mutate
    clone1.borrow_mut().push(4);
    clone2.borrow_mut().push(5);
    shared.borrow_mut().push(6);

    println!("\nRc<RefCell> after mutations: {:?}", shared.borrow());

    print_h3!("into_inner");
    // Extract value (consumes RefCell)
    let cell2: RefCell<String> = RefCell::new(String::from("data"));
    let inner: String = cell2.into_inner();
    println!("\nExtracted: {}", inner);

    print_h3!("replace");
    // Replace value and return old one
    let cell3: RefCell<i32> = RefCell::new(10);
    let old: i32 = cell3.replace(20);
    println!("\nOld: {}, New: {}", old, cell3.borrow());

    print_h3!("swap");
    // Swap values between two RefCells
    let cell_a: RefCell<i32> = RefCell::new(1);
    let cell_b: RefCell<i32> = RefCell::new(2);
    cell_a.swap(&cell_b);
    println!("\nAfter swap: a={}, b={}", cell_a.borrow(), cell_b.borrow());

    print_h3!("Cell<T> for Copy types");
    // Cell is simpler than RefCell for Copy types (no borrowing)
    let cell: Cell<i32> = Cell::new(5);
    println!("\nCell value: {}", cell.get());

    cell.set(10);
    println!("After set: {}", cell.get());

    // Cell can be modified through shared reference
    fn increment(cell: &Cell<i32>) {
        cell.set(cell.get() + 1);
    }

    increment(&cell);
    println!("After increment: {}", cell.get());

    print_h3!("Cell::update");
    // Modify in place with closure
    let counter: Cell<i32> = Cell::new(0);
    counter.update(|x| x + 1);
    println!("\nCounter: {}", counter.get());

    print_h3!("Cell::take");
    // Take value, leaving Default
    let cell_take: Cell<String> = Cell::new(String::from("taken"));
    let taken: String = cell_take.take();
    println!("\nTaken: {}, Cell now: {:?}", taken, cell_take.take());

    print_h3!("Cell::replace");
    let cell_replace: Cell<i32> = Cell::new(100);
    let old_val: i32 = cell_replace.replace(200);
    println!("\nReplaced {} with {}", old_val, cell_replace.get());

    print_h3!("Cell vs RefCell comparison");
    // Cell: Copy types only, no borrow checking, get/set
    let cell_copy: Cell<i32> = Cell::new(1);
    cell_copy.set(2);
    println!("\nCell (Copy types): {}", cell_copy.get());

    // RefCell: Any type, runtime borrow checking, borrow/borrow_mut
    let refcell: RefCell<Vec<i32>> = RefCell::new(vec![1]);
    refcell.borrow_mut().push(2);
    println!("RefCell (non-Copy): {:?}", refcell.borrow());

    print_h3!("When to use RefCell");
    // Use when you need:
    // 1. Interior mutability with shared references
    // 2. Mock objects in tests
    // 3. Complex data structures (graphs, caches)
    // 4. Breaking borrow checker limitations

    // Example: Graph with back-references
    #[derive(Debug)]
    struct Node {
        value: i32,
        neighbors: RefCell<Vec<Rc<Node>>>,
    }

    let node1: Rc<Node> = Rc::new(Node {
        value: 1,
        neighbors: RefCell::new(vec![]),
    });

    let node2: Rc<Node> = Rc::new(Node {
        value: 2,
        neighbors: RefCell::new(vec![]),
    });

    // Add edges (mutual references)
    node1.neighbors.borrow_mut().push(Rc::clone(&node2));
    node2.neighbors.borrow_mut().push(Rc::clone(&node1));

    println!("\nNode 1 has {} neighbors", node1.neighbors.borrow().len());
    println!("Node 2 has {} neighbors", node2.neighbors.borrow().len());

    print_h3!("Performance notes");
    // RefCell has runtime overhead (borrow flags)
    // Cell has zero overhead for Copy types
    // Prefer compile-time checking when possible

    println!(
        "\nRefCell size: {} bytes",
        std::mem::size_of::<RefCell<i32>>()
    );
    println!("Cell size: {} bytes", std::mem::size_of::<Cell<i32>>());
    println!("i32 size: {} bytes", std::mem::size_of::<i32>());
}
