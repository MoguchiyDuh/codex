use shared::{print_h2, print_h3};
use std::collections::BTreeSet;

pub fn run() {
    print_h2!("BTreeSet");

    print_h3!("Creation");

    // BTreeSet<T>: sorted unique values (unlike HashSet which is unordered)
    // Backed by BTreeMap<T, ()> - O(log n) operations
    // Use when: need sorted iteration, range queries, min/max

    let mut set: BTreeSet<i32> = BTreeSet::new();

    let from_iter: BTreeSet<i32> = BTreeSet::from([5, 3, 1, 4, 2, 3, 1]); // deduped + sorted
    println!("from_iter (sorted, deduped): {:?}", from_iter);

    let collected: BTreeSet<i32> = vec![9, 7, 5, 3, 1, 3, 7].into_iter().collect();
    println!("collected: {:?}", collected);

    print_h3!("Insert and Contains");

    let inserted_new: bool = set.insert(3);
    let inserted_dup: bool = set.insert(3); // false - already present
    set.insert(1);
    set.insert(5);
    set.insert(2);
    set.insert(4);

    println!("insert(3) first time  = {}", inserted_new); // true
    println!("insert(3) second time = {}", inserted_dup); // false
    println!("set = {:?}", set);

    println!("contains(3) = {}", set.contains(&3));
    println!("contains(9) = {}", set.contains(&9));

    print_h3!("get and take");

    let found: Option<&i32> = set.get(&3);
    println!("get(3) = {:?}", found);

    let mut s2: BTreeSet<String> = BTreeSet::from([
        String::from("rust"),
        String::from("go"),
        String::from("zig"),
    ]);
    // take removes and returns the value (useful to get ownership)
    let taken: Option<String> = s2.take("go");
    println!("take(\"go\") = {:?}", taken);
    println!("set after take: {:?}", s2);

    print_h3!("Remove");

    let removed: bool = set.remove(&3);
    let absent: bool = set.remove(&99);
    println!("remove(3)  = {}", removed); // true
    println!("remove(99) = {}", absent); // false
    println!("set after remove: {:?}", set);

    print_h3!("First, Last, Pop");

    let nums: BTreeSet<i32> = BTreeSet::from([10, 30, 50, 20, 40]);

    println!("first() = {:?}", nums.first()); // Some(10) - minimum
    println!("last()  = {:?}", nums.last()); // Some(50) - maximum

    let mut m: BTreeSet<i32> = nums.clone();
    println!("pop_first() = {:?}", m.pop_first()); // removes and returns 10
    println!("pop_last()  = {:?}", m.pop_last()); // removes and returns 50
    println!("remaining: {:?}", m);

    print_h3!("Range Queries");

    println!(
        "range(20..=40): {:?}",
        nums.range(20..=40).collect::<Vec<_>>()
    );
    println!("range(..30):    {:?}", nums.range(..30).collect::<Vec<_>>());
    println!("range(30..):    {:?}", nums.range(30..).collect::<Vec<_>>());

    print_h3!("Set Operations (always sorted output)");

    let a: BTreeSet<i32> = BTreeSet::from([1, 2, 3, 4, 5]);
    let b: BTreeSet<i32> = BTreeSet::from([3, 4, 5, 6, 7]);

    let union: BTreeSet<i32> = a.union(&b).copied().collect();
    let inter: BTreeSet<i32> = a.intersection(&b).copied().collect();
    let diff: BTreeSet<i32> = a.difference(&b).copied().collect();
    let sym_diff: BTreeSet<i32> = a.symmetric_difference(&b).copied().collect();

    println!("a = {:?}", a);
    println!("b = {:?}", b);
    println!("union              = {:?}", union); // {1,2,3,4,5,6,7}
    println!("intersection       = {:?}", inter); // {3,4,5}
    println!("difference (a-b)   = {:?}", diff); // {1,2}
    println!("symmetric_diff     = {:?}", sym_diff); // {1,2,6,7}

    print_h3!("Set Relations");

    let small: BTreeSet<i32> = BTreeSet::from([3, 4]);
    println!("small is_subset of a:    {}", small.is_subset(&a));
    println!("a is_superset of small:  {}", a.is_superset(&small));
    println!("a is_disjoint from b:    {}", a.is_disjoint(&b)); // false - they share 3,4,5

    let disjoint: BTreeSet<i32> = BTreeSet::from([10, 20]);
    println!("a is_disjoint from [10,20]: {}", a.is_disjoint(&disjoint)); // true

    print_h3!("retain");

    let mut evens: BTreeSet<i32> = (1..=10).collect();
    evens.retain(|x| x % 2 == 0);
    println!("retain(even): {:?}", evens);

    print_h3!("Iteration");

    let words: BTreeSet<&str> = BTreeSet::from(["rust", "go", "python", "c", "zig"]);
    println!("iter (sorted): {:?}", words.iter().collect::<Vec<_>>());

    for w in &words {
        print!("{} ", w);
    }
    println!();

    print_h3!("HashSet vs BTreeSet");
    println!("HashSet:   O(1) avg,  unordered,    no range queries");
    println!("BTreeSet:  O(log n),  sorted,        range() / first / last");
    println!("Use BTreeSet when: iteration order matters, need min/max/range");
}
