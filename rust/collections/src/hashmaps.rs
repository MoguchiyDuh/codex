use shared::{print_h2, print_h3};
use std::collections::HashMap;

pub fn run() {
    print_h2!("HashMap<K, V>");

    print_h3!("Creation");
    let mut map: HashMap<String, i32> = HashMap::new();
    map.insert(String::from("apple"), 10);
    map.insert(String::from("banana"), 20);
    println!("Created with new(): {:?}", map);

    // From array
    let map2: HashMap<&str, i32> = HashMap::from([("red", 1), ("blue", 2), ("green", 3)]);
    println!("From array: {:?}", map2);

    // From iterator: zip pairs two iterators; collect() uses HashMap's FromIterator impl
    let keys: Vec<&str> = vec!["a", "b", "c"];
    let values: Vec<i32> = vec![1, 2, 3];
    let map3: HashMap<&str, i32> = keys.into_iter().zip(values.into_iter()).collect();
    println!("From iterator: {:?}", map3);

    // With capacity
    let map4: HashMap<i32, i32> = HashMap::with_capacity(10);
    println!("Capacity pre-allocated: {}", map4.capacity());

    print_h3!("Inserting");
    let mut map5: HashMap<&str, i32> = HashMap::new();
    let old1: Option<i32> = map5.insert("key1", 100); // Returns None (new key)
    println!("Inserted key1, old value: {:?}", old1);

    let old2: Option<i32> = map5.insert("key1", 200); // Returns Some(100) (replaced)
    println!("Updated key1, old value: {:?}", old2);
    println!("Map: {:?}", map5);

    print_h3!("Accessing values");
    let map6: HashMap<&str, i32> = HashMap::from([("x", 10), ("y", 20), ("z", 30)]);

    // get returns Option<&V>
    let value: Option<&i32> = map6.get("x");
    match value {
        Some(v) => println!("x = {}", v),
        None => println!("x not found"),
    }

    let missing: Option<&i32> = map6.get("w");
    println!("w = {:?}", missing);

    // Direct indexing (panics if key missing)
    let direct: &i32 = &map6["x"];
    println!("Direct access: {}", direct);
    // PANIC: &map6["nonexistent"] would panic (key not found)

    // get_key_value returns Option<(&K, &V)>
    let pair: Option<(&&str, &i32)> = map6.get_key_value(&"x");
    println!("Key-value pair: {:?}", pair);

    print_h3!("Updating values");
    let mut map7: HashMap<&str, i32> = HashMap::from([("a", 1), ("b", 2)]);

    // Get mutable reference
    if let Some(val) = map7.get_mut("a") {
        *val += 10;
    }
    println!("After incrementing 'a': {:?}", map7);

    print_h3!("Entry API");
    // entry() returns an Entry enum that allows insert-or-modify without a double lookup
    let mut map8: HashMap<&str, i32> = HashMap::new();

    // or_insert: insert if key doesn't exist
    let v1: &mut i32 = map8.entry("key1").or_insert(50);
    println!("Inserted or got: {}", v1);
    *v1 += 1; // Can modify returned reference
    println!("After modify: {:?}", map8);

    // or_insert on existing key returns existing value
    let v2: &mut i32 = map8.entry("key1").or_insert(999);
    println!("Existing value: {}", v2);

    // or_insert_with: lazy initialization
    let v3: &mut i32 = map8.entry("key2").or_insert_with(|| {
        println!("  Computing default for key2");
        return 100;
    });
    println!("Lazy insert: {}", v3);

    // Pattern: counting word occurrences
    let text: &str = "hello world hello rust world";
    let mut word_count: HashMap<&str, i32> = HashMap::new();
    for word in text.split_whitespace() {
        let count: &mut i32 = word_count.entry(word).or_insert(0);
        *count += 1;
    }
    println!("Word count: {:?}", word_count);

    // and_modify: modify if exists, then or_insert
    let mut map9: HashMap<&str, i32> = HashMap::from([("a", 5)]);
    map9.entry("a").and_modify(|v| *v += 1).or_insert(0);
    map9.entry("b").and_modify(|v| *v += 1).or_insert(0);
    println!("After and_modify: {:?}", map9);

    print_h3!("Removing");
    let mut map10: HashMap<&str, i32> = HashMap::from([("x", 1), ("y", 2), ("z", 3)]);

    let removed: Option<i32> = map10.remove("y"); // Returns removed value
    println!("Removed: {:?}, map: {:?}", removed, map10);

    let missing: Option<i32> = map10.remove("w");
    println!("Remove missing key: {:?}", missing);

    // remove_entry returns (K, V)
    let removed_pair: Option<(&str, i32)> = map10.remove_entry("x");
    println!("Removed entry: {:?}", removed_pair);

    print_h3!("Checking membership");
    let map11: HashMap<&str, i32> = HashMap::from([("a", 1), ("b", 2)]);

    let has_a: bool = map11.contains_key("a");
    let has_z: bool = map11.contains_key("z");
    println!("Has 'a': {}, Has 'z': {}", has_a, has_z);

    print_h3!("Length and capacity");
    let mut map12: HashMap<i32, i32> = HashMap::with_capacity(10);
    map12.insert(1, 10);
    map12.insert(2, 20);
    println!("Len: {}, Capacity: {}", map12.len(), map12.capacity());
    println!("Is empty: {}", map12.is_empty());

    map12.reserve(20); // Reserve space for 20 MORE entries
    println!("After reserve: capacity {}", map12.capacity());

    map12.shrink_to_fit(); // Reduce capacity to fit current len
    println!("After shrink: capacity {}", map12.capacity());

    print_h3!("Clearing");
    let mut map13: HashMap<&str, i32> = HashMap::from([("a", 1), ("b", 2), ("c", 3)]);
    map13.clear();
    println!("After clear: {:?}, is_empty: {}", map13, map13.is_empty());

    print_h3!("Iteration");
    let map14: HashMap<&str, i32> = HashMap::from([("one", 1), ("two", 2), ("three", 3)]);

    // Iterate over key-value pairs
    println!("Key-value pairs:");
    for (key, value) in &map14 {
        println!("  {} = {}", key, value);
    }

    // Iterate over keys only
    println!("Keys:");
    for key in map14.keys() {
        println!("  {}", key);
    }

    // Iterate over values only
    println!("Values:");
    for value in map14.values() {
        println!("  {}", value);
    }

    // Mutable iteration over values
    let mut map15: HashMap<&str, i32> = HashMap::from([("a", 1), ("b", 2)]);
    for value in map15.values_mut() {
        *value *= 10;
    }
    println!("After multiplying values: {:?}", map15);

    // Consuming iteration (moves map)
    let map16: HashMap<&str, i32> = HashMap::from([("x", 1), ("y", 2)]);
    for (key, value) in map16 {
        println!("  Consumed: {} = {}", key, value);
    }
    // ERROR: map16 is moved
    // println!("{:?}", map16); // Would fail

    print_h3!("Filtering with retain");
    let mut map17: HashMap<&str, i32> = HashMap::from([("a", 5), ("b", 15), ("c", 25), ("d", 35)]);
    map17.retain(|_key, &mut value| value > 20); // Keep only values > 20
    println!("After retain: {:?}", map17);

    print_h3!("Merging maps");
    let mut map18: HashMap<&str, i32> = HashMap::from([("a", 1), ("b", 2)]);
    let map19: HashMap<&str, i32> = HashMap::from([("b", 20), ("c", 3)]);

    for (key, value) in map19 {
        map18.insert(key, value); // Overwrites if key exists
    }
    println!("Merged (overwrite): {:?}", map18);

    // Merge without overwriting
    let mut map20: HashMap<&str, i32> = HashMap::from([("a", 1), ("b", 2)]);
    let map21: HashMap<&str, i32> = HashMap::from([("b", 20), ("c", 3)]);
    for (key, value) in map21 {
        map20.entry(key).or_insert(value); // Only insert if key doesn't exist
    }
    println!("Merged (no overwrite): {:?}", map20);

    print_h3!("Common patterns");
    // Pattern: Grouping values by key
    let items: Vec<(&str, i32)> = vec![("a", 1), ("b", 2), ("a", 3), ("b", 4), ("c", 5)];
    let mut grouped: HashMap<&str, Vec<i32>> = HashMap::new();
    for (key, val) in items {
        grouped.entry(key).or_insert_with(Vec::new).push(val);
    }
    println!("Grouped: {:?}", grouped);

    // Pattern: Swap keys and values
    let original: HashMap<&str, i32> = HashMap::from([("a", 1), ("b", 2), ("c", 3)]);
    let swapped: HashMap<i32, &str> = original.iter().map(|(k, v)| (*v, *k)).collect();
    println!("Swapped: {:?}", swapped);
}
