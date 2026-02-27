use shared::{print_h2, print_h3};
use std::fmt;
use std::marker::PhantomData;

// ------------------- Generic function, single bound -------------------

fn largest<T: PartialOrd>(list: &[T]) -> &T {
    let mut largest: &T = &list[0];
    for item in list.iter() {
        if item > largest {
            largest = item;
        }
    }
    return largest;
}

// ------------------- Multiple bounds with + -------------------

fn display_and_debug<T: fmt::Display + fmt::Debug + Clone>(val: T) {
    let cloned: T = val.clone();
    println!("Display={:<15} Debug={:?}", format!("{}", val), cloned);
}

// ------------------- Where clause -------------------
// Cleaner than T: A + B when bounds get long or complex

fn complex_bounds<T, U>(t: T, u: U) -> String
where
    T: fmt::Display + Clone,
    U: fmt::Debug + PartialOrd,
{
    return format!("t={}, u={:?}", t, u);
}

// ------------------- Generic struct with constrained impl blocks -------------------

#[derive(Debug, Clone)]
struct Pair<T> {
    first: T,
    second: T,
}

// This impl only exists for T: PartialOrd + Display - other T's still get the struct
impl<T: fmt::Display + PartialOrd> Pair<T> {
    fn new(first: T, second: T) -> Self {
        return Pair { first, second };
    }

    fn max(&self) -> &T {
        if self.first >= self.second {
            return &self.first;
        }
        return &self.second;
    }

    fn display(&self) {
        println!("({}, {})", self.first, self.second);
    }
}

// ------------------- Multiple type parameters -------------------

#[derive(Debug)]
struct KeyValue<K, V> {
    key: K,
    value: V,
}

impl<K: fmt::Display, V: fmt::Display> KeyValue<K, V> {
    fn show(&self) {
        println!("{} -> {}", self.key, self.value);
    }
}

// ------------------- Generic enum -------------------

#[derive(Debug)]
enum Tree<T> {
    Leaf(T),
    Node(Box<Tree<T>>, Box<Tree<T>>),
}

impl<T: fmt::Display> Tree<T> {
    fn depth(&self) -> usize {
        match self {
            Tree::Leaf(_) => return 1,
            Tree::Node(left, right) => return 1 + left.depth().max(right.depth()),
        }
    }

    fn count_leaves(&self) -> usize {
        match self {
            Tree::Leaf(_) => return 1,
            Tree::Node(left, right) => return left.count_leaves() + right.count_leaves(),
        }
    }
}

// ------------------- Associated types -------------------

// Associated types fix the type per impl — implementor decides, not the caller.
// Contrast: trait Container<T> {} means the *caller* picks T for each impl,
// allowing multiple impls like Container<i32> and Container<String> for the same struct.
// With associated types you get at most one impl per struct — much cleaner for single-type collections.

trait Container {
    type Item; // one Item type per Container implementation

    fn get(&self, index: usize) -> Option<&Self::Item>;
    fn len(&self) -> usize;
    fn is_empty(&self) -> bool {
        return self.len() == 0;
    }
}

struct Stack<T> {
    items: Vec<T>,
}

impl<T> Stack<T> {
    fn new() -> Self {
        return Stack { items: Vec::new() };
    }

    fn push(&mut self, item: T) {
        self.items.push(item);
    }

    fn pop(&mut self) -> Option<T> {
        return self.items.pop();
    }
}

impl<T> Container for Stack<T> {
    type Item = T; // fix the associated type

    fn get(&self, index: usize) -> Option<&T> {
        return self.items.get(index);
    }

    fn len(&self) -> usize {
        return self.items.len();
    }
}

// Associated type in bound: C::Item: Debug
fn print_first<C: Container>(c: &C)
where
    C::Item: fmt::Debug,
{
    println!("first = {:?}", c.get(0));
}

// ------------------- Const generics -------------------

// const N: usize - a compile-time constant as a type parameter
#[derive(Debug)]
struct FixedVec<T, const N: usize> {
    data: [Option<T>; N],
    len: usize,
}

impl<T: Copy + Default + fmt::Debug, const N: usize> FixedVec<T, N> {
    fn new() -> Self {
        return FixedVec {
            data: [None; N],
            len: 0,
        };
    }

    fn push(&mut self, val: T) -> bool {
        if self.len >= N {
            return false; // full
        }
        self.data[self.len] = Some(val);
        self.len += 1;
        return true;
    }

    fn get(&self, i: usize) -> Option<&T> {
        if i >= self.len {
            return None;
        }
        return self.data[i].as_ref();
    }

    fn capacity() -> usize {
        return N; // N is a compile-time constant
    }
}

// Const generic function: array identity function (size is compile-time)
fn identity_array<T: Copy, const N: usize>(arr: [T; N]) -> [T; N] {
    return arr;
}

// ------------------- PhantomData (zero-cost type marker) -------------------

// PhantomData<T> marks that the struct is "logically associated" with T
// but doesn't actually store a T. Zero runtime cost.
// Use: enforce type-level distinctions, express variance, satisfy the borrow checker.

struct Meters;
struct Seconds;
struct Kilograms;

#[derive(Debug, Clone, Copy)]
struct Quantity<T, Unit> {
    value: T,
    _unit: PhantomData<Unit>, // zero-size marker
}

impl<T: Copy + fmt::Display> Quantity<T, Meters> {
    fn meters(val: T) -> Self {
        return Quantity {
            value: val,
            _unit: PhantomData,
        };
    }
}

impl<T: Copy + fmt::Display> Quantity<T, Seconds> {
    fn seconds(val: T) -> Self {
        return Quantity {
            value: val,
            _unit: PhantomData,
        };
    }
}

impl<T: Copy + fmt::Display> Quantity<T, Kilograms> {
    fn kilograms(val: T) -> Self {
        return Quantity {
            value: val,
            _unit: PhantomData,
        };
    }
}

// Can only compute speed from correct units - type system enforces this
fn speed(dist: Quantity<f64, Meters>, time: Quantity<f64, Seconds>) -> f64 {
    return dist.value / time.value;
}

// ------------------- Generic with lifetime -------------------

// T: 'a means "T must live at least as long as 'a". Needed because if T contained
// a reference shorter than 'a, storing it behind a &'a T would be unsound.
struct Ref<'a, T: 'a> {
    value: &'a T,
}

impl<'a, T: fmt::Display> Ref<'a, T> {
    fn new(val: &'a T) -> Self {
        return Ref { value: val };
    }

    fn show(&self) {
        println!("Ref holds: {}", self.value);
    }
}

pub fn run() {
    print_h2!("Generics");
    print_h3!("Generic functions");

    let nums: Vec<i32> = vec![34, 50, 25, 100, 65];
    println!("largest([34,50,25,100,65]) = {}", largest(&nums));

    let chars: Vec<char> = vec!['y', 'm', 'a', 'q'];
    println!("largest(['y','m','a','q']) = {}", largest(&chars));

    let strs: Vec<&str> = vec!["banana", "apple", "cherry"];
    println!(
        "largest([\"banana\",\"apple\",\"cherry\"]) = {}",
        largest(&strs)
    );

    print_h3!("Multiple bounds");

    display_and_debug(42_u32);
    display_and_debug("ferris");
    display_and_debug(3.14_f64);

    print_h3!("Where clauses");

    let result: String = complex_bounds("hello", vec![1, 2, 3]);
    println!("complex_bounds = {}", result);

    print_h3!("Generic structs");

    let pair_i32: Pair<i32> = Pair::new(5, 10);
    let pair_f64: Pair<f64> = Pair::new(3.14, 2.71);
    let pair_str: Pair<&str> = Pair::new("zebra", "apple");

    pair_i32.display();
    println!("max of i32 pair = {}", pair_i32.max());
    pair_f64.display();
    println!("max of f64 pair = {}", pair_f64.max());
    pair_str.display();
    println!("max of str pair = {}", pair_str.max());

    print_h3!("Multiple type parameters");

    let kv1: KeyValue<&str, i32> = KeyValue {
        key: "score",
        value: 42,
    };
    let kv2: KeyValue<i32, bool> = KeyValue {
        key: 404,
        value: false,
    };
    kv1.show();
    kv2.show();

    print_h3!("Generic enums");

    let tree: Tree<i32> = Tree::Node(
        Box::new(Tree::Leaf(1)),
        Box::new(Tree::Node(Box::new(Tree::Leaf(2)), Box::new(Tree::Leaf(3)))),
    );
    println!("Tree depth   = {}", tree.depth());
    println!("Tree leaves  = {}", tree.count_leaves());

    print_h3!("Associated types");

    let mut stack: Stack<i32> = Stack::new();
    stack.push(10);
    stack.push(20);
    stack.push(30);

    println!("len = {}", stack.len());
    println!("get(0) = {:?}", stack.get(0));
    println!("is_empty = {}", stack.is_empty());
    print_first(&stack);

    println!("pop = {:?}", stack.pop());
    println!("len after pop = {}", stack.len());

    print_h3!("Const generics");

    let mut fv: FixedVec<i32, 4> = FixedVec::new(); // capacity fixed at compile time
    println!("FixedVec capacity = {}", FixedVec::<i32, 4>::capacity());

    let pushed: bool = fv.push(10);
    fv.push(20);
    fv.push(30);
    fv.push(40);
    let overflow: bool = fv.push(50); // returns false - full

    println!("push(10) ok = {}", pushed);
    println!("push(50) ok = {}", overflow); // false
    println!("get(2) = {:?}", fv.get(2));

    let arr: [i32; 3] = identity_array([1, 2, 3]);
    println!("identity_array([1,2,3]) = {:?}", arr);

    // std uses const generics: [T; N], SIMD types, fixed-size buffers

    print_h3!("PhantomData");

    let dist: Quantity<f64, Meters> = Quantity::meters(100.0);
    let time: Quantity<f64, Seconds> = Quantity::seconds(9.58);
    let mass: Quantity<f64, Kilograms> = Quantity::kilograms(75.0);

    println!("distance = {} m", dist.value);
    println!("time     = {} s", time.value);
    println!("mass     = {} kg", mass.value);
    println!("speed    = {:.3} m/s", speed(dist, time));

    // size_of PhantomData is always 0
    println!(
        "size_of::<Quantity<f64, Meters>>()    = {}",
        std::mem::size_of::<Quantity<f64, Meters>>()
    );
    println!(
        "size_of::<PhantomData<Meters>>()      = {}",
        std::mem::size_of::<PhantomData<Meters>>()
    );
    // ERROR: speed(dist, mass)  - mismatched units, compile-time error

    print_h3!("Generics + lifetimes");

    let value: String = String::from("owned string");
    let r: Ref<String> = Ref::new(&value);
    r.show();

    let num: i32 = 42;
    let r2: Ref<i32> = Ref::new(&num);
    r2.show();
}
