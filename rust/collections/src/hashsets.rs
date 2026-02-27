use shared::{print_h2, print_h3};
use std::collections::HashSet;

pub fn run() {
    print_h2!("HashSet<T>");

    print_h3!("Creation");
    let mut set: HashSet<i32> = HashSet::new();
    set.insert(1);
    set.insert(2);
    set.insert(3);
    println!("Created with new(): {:?}", set);

    // From array
    let set2: HashSet<i32> = HashSet::from([1, 2, 3, 4, 5]);
    println!("From array: {:?}", set2);

    // From iterator
    let set3: HashSet<i32> = (0..5).collect();
    println!("From iterator: {:?}", set3);

    // With capacity
    let set4: HashSet<i32> = HashSet::with_capacity(10);
    println!("Capacity pre-allocated: {}", set4.capacity());

    print_h3!("Inserting");
    let mut set5: HashSet<&str> = HashSet::new();
    let inserted1: bool = set5.insert("hello"); // Returns true (new element)
    println!("Inserted 'hello': {}", inserted1);

    let inserted2: bool = set5.insert("hello"); // Returns false (duplicate)
    println!("Inserted 'hello' again: {}", inserted2);
    println!("Set: {:?}", set5);

    print_h3!("Checking membership");
    let set6: HashSet<i32> = HashSet::from([10, 20, 30, 40, 50]);

    let has_20: bool = set6.contains(&20);
    let has_99: bool = set6.contains(&99);
    println!("Contains 20: {}, Contains 99: {}", has_20, has_99);

    print_h3!("Removing");
    let mut set7: HashSet<i32> = HashSet::from([1, 2, 3, 4, 5]);

    let removed: bool = set7.remove(&3); // Returns true if element existed
    println!("Removed 3: {}", removed);
    println!("After removal: {:?}", set7);

    let not_found: bool = set7.remove(&99);
    println!("Remove 99 (not found): {}", not_found);

    // take: remove and return the element
    let taken: Option<i32> = set7.take(&2);
    println!("Taken: {:?}, set: {:?}", taken, set7);

    let not_taken: Option<i32> = set7.take(&99);
    println!("Take 99 (not found): {:?}", not_taken);

    print_h3!("Length and capacity");
    let mut set8: HashSet<i32> = HashSet::with_capacity(10);
    set8.insert(1);
    set8.insert(2);
    println!("Len: {}, Capacity: {}", set8.len(), set8.capacity());
    println!("Is empty: {}", set8.is_empty());

    set8.reserve(20); // Reserve space for 20 MORE elements
    println!("After reserve: capacity {}", set8.capacity());

    set8.shrink_to_fit(); // Reduce capacity to fit current len
    println!("After shrink: capacity {}", set8.capacity());

    print_h3!("Clearing");
    let mut set9: HashSet<i32> = HashSet::from([1, 2, 3, 4, 5]);
    set9.clear();
    println!("After clear: {:?}, is_empty: {}", set9, set9.is_empty());

    print_h3!("Iteration");
    let set10: HashSet<&str> = HashSet::from(["apple", "banana", "cherry"]);

    // Immutable iteration
    println!("Elements:");
    for element in &set10 {
        println!("  {}", element);
    }
    println!("set10 still valid: {:?}", set10);

    // Consuming iteration (moves set)
    let set11: HashSet<i32> = HashSet::from([10, 20, 30]);
    for element in set11 {
        println!("  Consumed: {}", element);
    }
    // ERROR: set11 is moved
    // println!("{:?}", set11); // Would fail

    print_h3!("Extending");
    let mut set12: HashSet<i32> = HashSet::from([1, 2, 3]);
    set12.extend([3, 4, 5]); // Duplicates ignored
    println!("After extend: {:?}", set12);

    let mut set13: HashSet<i32> = HashSet::from([1, 2]);
    let other: HashSet<i32> = HashSet::from([2, 3, 4]);
    set13.extend(other);
    println!("Extended with another set: {:?}", set13);

    print_h3!("Filtering with retain");
    let mut set14: HashSet<i32> = HashSet::from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
    set14.retain(|&x| x % 2 == 0); // Keep only evens
    println!("After retain evens: {:?}", set14);

    print_h3!("Set operations: union");
    let set_a: HashSet<i32> = HashSet::from([1, 2, 3, 4]);
    let set_b: HashSet<i32> = HashSet::from([3, 4, 5, 6]);

    // Union: all elements from both sets
    let union: HashSet<i32> = set_a.union(&set_b).copied().collect();
    println!("set_a: {:?}", set_a);
    println!("set_b: {:?}", set_b);
    println!("Union: {:?}", union);

    print_h3!("Set operations: intersection");
    // Intersection: elements in both sets
    let intersection: HashSet<i32> = set_a.intersection(&set_b).copied().collect();
    println!("Intersection: {:?}", intersection);

    print_h3!("Set operations: difference");
    // Difference: elements in set_a but not in set_b
    let difference: HashSet<i32> = set_a.difference(&set_b).copied().collect();
    println!("Difference (a - b): {:?}", difference);

    let reverse_diff: HashSet<i32> = set_b.difference(&set_a).copied().collect();
    println!("Difference (b - a): {:?}", reverse_diff);

    print_h3!("Set operations: symmetric difference");
    // Symmetric difference: elements in one set but not both
    let sym_diff: HashSet<i32> = set_a.symmetric_difference(&set_b).copied().collect();
    println!("Symmetric difference: {:?}", sym_diff);

    print_h3!("Set relations");
    let set_x: HashSet<i32> = HashSet::from([1, 2, 3]);
    let set_y: HashSet<i32> = HashSet::from([1, 2, 3, 4, 5]);
    let set_z: HashSet<i32> = HashSet::from([6, 7, 8]);

    // is_subset: all elements of set_x in set_y?
    let is_sub: bool = set_x.is_subset(&set_y);
    println!("set_x subset of set_y: {}", is_sub);

    // is_superset: set_y contains all elements of set_x?
    let is_super: bool = set_y.is_superset(&set_x);
    println!("set_y superset of set_x: {}", is_super);

    // is_disjoint: no common elements?
    let disjoint_xy: bool = set_x.is_disjoint(&set_y);
    let disjoint_xz: bool = set_x.is_disjoint(&set_z);
    println!("set_x disjoint with set_y: {}", disjoint_xy);
    println!("set_x disjoint with set_z: {}", disjoint_xz);

    print_h3!("Replacing elements");
    let mut set15: HashSet<i32> = HashSet::from([1, 2, 3]);
    // replace: if element exists, replace it and return old value
    let old: Option<i32> = set15.replace(2);
    println!("Replaced 2 (existed): {:?}", old);

    let new: Option<i32> = set15.replace(99);
    println!("Replaced 99 (new): {:?}", new);
    println!("Set after replace: {:?}", set15);

    print_h3!("Getting element reference");
    let set16: HashSet<String> = HashSet::from([String::from("hello"), String::from("world")]);

    // get: returns reference to element if exists
    let found: Option<&String> = set16.get("hello");
    println!("Get 'hello': {:?}", found);

    let not_found: Option<&String> = set16.get("rust");
    println!("Get 'rust': {:?}", not_found);

    print_h3!("Common patterns");
    // Pattern: Remove duplicates from vector
    let vec: Vec<i32> = vec![1, 2, 3, 2, 4, 3, 5, 1];
    let unique: HashSet<i32> = vec.into_iter().collect();
    println!("Unique elements: {:?}", unique);

    // Pattern: Find common elements
    let list1: Vec<i32> = vec![1, 2, 3, 4, 5];
    let list2: Vec<i32> = vec![4, 5, 6, 7, 8];
    let set1: HashSet<i32> = list1.into_iter().collect();
    let set2: HashSet<i32> = list2.into_iter().collect();
    let common: HashSet<i32> = set1.intersection(&set2).copied().collect();
    println!("Common elements: {:?}", common);

    // Pattern: Check if all elements are unique
    let numbers: Vec<i32> = vec![1, 2, 3, 4, 5];
    let unique_set: HashSet<i32> = numbers.iter().copied().collect();
    let all_unique: bool = numbers.len() == unique_set.len();
    println!("All unique: {}", all_unique);

    let duplicates: Vec<i32> = vec![1, 2, 3, 2, 4];
    let dup_set: HashSet<i32> = duplicates.iter().copied().collect();
    let has_dups: bool = duplicates.len() != dup_set.len();
    println!("Has duplicates: {}", has_dups);
}
