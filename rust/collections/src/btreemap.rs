use shared::{print_h2, print_h3};
use std::collections::BTreeMap;

pub fn run() {
    print_h2!("BTreeMap");

    print_h3!("Creation");

    // BTreeMap<K, V>: sorted by key (unlike HashMap which is unordered)
    // Backed by a B-tree - O(log n) for insert/get/remove
    // Use when: iteration order matters, need range queries, keys impl Ord

    let mut map: BTreeMap<String, i32> = BTreeMap::new();

    let from_iter: BTreeMap<i32, &str> = BTreeMap::from([
        (3, "three"),
        (1, "one"),
        (2, "two"),
        (5, "five"),
        (4, "four"),
    ]);

    println!("from_iter (always sorted): {:?}", from_iter);
    // HashMap would print in arbitrary order; BTreeMap always prints in key order

    let collected: BTreeMap<i32, i32> = (0..5).map(|i| (i, i * i)).collect();
    println!("collected squares: {:?}", collected);

    print_h3!("Insert and Get");

    map.insert(String::from("banana"), 3);
    map.insert(String::from("apple"), 5);
    map.insert(String::from("cherry"), 1);
    map.insert(String::from("date"), 8);

    println!("map = {:?}", map); // alphabetical order

    let apples: Option<&i32> = map.get("apple");
    println!("get(\"apple\")   = {:?}", apples);
    println!("get(\"mango\")   = {:?}", map.get("mango"));

    // get_key_value returns (key, value) pair
    let kv: Option<(&String, &i32)> = map.get_key_value("banana");
    println!("get_key_value  = {:?}", kv);

    // Indexing panics if key absent
    println!("map[\"cherry\"]  = {}", map["cherry"]);
    // PANIC: map["mango"] - key not found

    print_h3!("Contains");

    println!("contains_key(\"apple\")  = {}", map.contains_key("apple"));
    println!("contains_key(\"mango\")  = {}", map.contains_key("mango"));

    print_h3!("Entry API");

    // or_insert: insert default if absent, return &mut V
    *map.entry(String::from("apple")).or_insert(0) += 10;
    println!("apple after +10: {}", map["apple"]);

    map.entry(String::from("elderberry")).or_insert(2);
    println!("elderberry (new): {}", map["elderberry"]);

    // or_insert_with: lazy default (only called if missing)
    map.entry(String::from("fig")).or_insert_with(|| 42 * 2);
    println!("fig: {}", map["fig"]);

    // or_default: inserts T::default() if missing
    map.entry(String::from("grape")).or_default();
    println!("grape (defaulted): {}", map["grape"]); // 0

    // and_modify: mutate existing value only
    map.entry(String::from("cherry")).and_modify(|v| *v *= 10);
    println!("cherry after *10: {}", map["cherry"]);

    print_h3!("Removal");

    let removed: Option<i32> = map.remove("grape");
    println!("remove(\"grape\") = {:?}", removed);
    println!("remove(\"mango\") = {:?}", map.remove("mango")); // None

    // remove_entry returns (K, V)
    let entry: Option<(String, i32)> = map.remove_entry("fig");
    println!("remove_entry(\"fig\") = {:?}", entry);

    print_h3!("Range Queries (BTreeMap-exclusive)");

    let scores: BTreeMap<i32, &str> = BTreeMap::from([
        (10, "ten"),
        (20, "twenty"),
        (30, "thirty"),
        (40, "forty"),
        (50, "fifty"),
    ]);

    // range returns an iterator over (K, V) pairs in the range
    println!("range(20..=40):");
    for (k, v) in scores.range(20..=40) {
        println!("  {} = {}", k, v);
    }

    println!("range(..30) (exclusive upper):");
    for (k, v) in scores.range(..30) {
        println!("  {} = {}", k, v);
    }

    println!("range(30..) (from 30 onwards):");
    for (k, v) in scores.range(30..) {
        println!("  {} = {}", k, v);
    }

    // range_mut for mutation
    let mut mutable: BTreeMap<i32, i32> = (1..=5).map(|i| (i, i * 10)).collect();
    for (_k, v) in mutable.range_mut(2..=4) {
        *v += 100;
    }
    println!("After range_mut(2..=4) += 100: {:?}", mutable);

    print_h3!("First and Last (min/max keys)");

    println!("first_key_value = {:?}", scores.first_key_value()); // (10, "ten")
    println!("last_key_value  = {:?}", scores.last_key_value()); // (50, "fifty")

    let mut m: BTreeMap<i32, i32> = BTreeMap::from([(1, 10), (2, 20), (3, 30)]);
    println!("pop_first = {:?}", m.pop_first()); // removes and returns (1, 10)
    println!("pop_last  = {:?}", m.pop_last()); // removes and returns (3, 30)
    println!("remaining: {:?}", m);

    print_h3!("Iteration (always sorted order)");

    let words: BTreeMap<&str, usize> =
        BTreeMap::from([("rust", 4), ("go", 2), ("python", 6), ("c", 1)]);

    println!("keys():   {:?}", words.keys().collect::<Vec<_>>());
    println!("values(): {:?}", words.values().collect::<Vec<_>>());

    for (word, len) in &words {
        println!("  {} (len {})", word, len);
    }

    // into_iter consumes the map
    let owned: Vec<(&str, usize)> = words.into_iter().collect();
    println!("into_iter: {:?}", owned);

    print_h3!("split_off");

    let mut left: BTreeMap<i32, i32> = (1..=10).map(|i| (i, i * 100)).collect();
    let right: BTreeMap<i32, i32> = left.split_off(&6); // key >= 6 goes to right
    println!("left  (< 6): {:?}", left);
    println!("right (>= 6): {:?}", right);

    print_h3!("retain");

    let mut evens: BTreeMap<i32, i32> = (1..=10).map(|i| (i, i)).collect();
    evens.retain(|k, _v| k % 2 == 0);
    println!("retain(even keys): {:?}", evens);

    print_h3!("HashMap vs BTreeMap");
    println!("HashMap:   O(1) avg insert/get,  unordered,  no range queries");
    println!("BTreeMap:  O(log n) insert/get,  sorted,     range() / first / last");
    println!("Use BTreeMap when: ordering matters, need min/max, range iteration");
    println!("Use HashMap when: just need fast lookup, order irrelevant");
}
