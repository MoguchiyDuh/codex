use shared::print_h3;
use std::borrow::Cow;

// Cow<'a, B> = Clone on Write
// Either borrows (&'a B) or owns an owned copy (B::Owned)
// The key: avoid allocating unless mutation is actually needed
//
// Common cases:
//   Cow<'_, str>   - either &str (borrowed) or String (owned)
//   Cow<'_, [T]>   - either &[T] (borrowed) or Vec<T> (owned)
//   Cow<'_, Path>  - either &Path or PathBuf

// ------------------- Basic usage -------------------

fn ensure_no_spaces(input: &str) -> Cow<'_, str> {
    if !input.contains(' ') {
        return Cow::Borrowed(input); // no allocation - return original
    }
    return Cow::Owned(input.replace(' ', "_")); // allocate only when needed
}

fn ensure_lowercase(input: &str) -> Cow<'_, str> {
    if input.chars().all(|c| !c.is_uppercase()) {
        return Cow::Borrowed(input); // already lowercase - no copy
    }
    return Cow::Owned(input.to_lowercase());
}

// ------------------- Cow<'_, [T]> -------------------

fn ensure_sorted(data: &[i32]) -> Cow<'_, [i32]> {
    if data.windows(2).all(|w| w[0] <= w[1]) {
        return Cow::Borrowed(data); // already sorted - borrow it
    }
    let mut owned: Vec<i32> = data.to_vec(); // clone only when needed
    owned.sort();
    return Cow::Owned(owned);
}

// ------------------- Function accepting both &str and String -------------------

// Cow lets a function accept &str, String, or anything that converts to Cow<str>
fn process_name(name: impl Into<Cow<'static, str>>) -> String {
    let cow: Cow<'static, str> = name.into();
    return format!("Hello, {}!", cow);
}

// ------------------- Cow in error messages -------------------

// Efficient error messages: static strings borrowed, dynamic ones owned
fn describe_error(code: u32) -> Cow<'static, str> {
    match code {
        404 => Cow::Borrowed("not found"),             // static, no alloc
        500 => Cow::Borrowed("internal server error"), // static, no alloc
        _ => Cow::Owned(format!("unknown error code {}", code)), // needs alloc
    }
}

pub fn run() {
    print_h3!("Cow<'a, T> - Clone on Write");

    print_h3!("Borrowed vs Owned");

    let no_spaces: &str = "hello_world";
    let has_spaces: &str = "hello world";

    let r1: Cow<str> = ensure_no_spaces(no_spaces);
    let r2: Cow<str> = ensure_no_spaces(has_spaces);

    println!(
        "ensure_no_spaces({:?}) -> {:?} (is_owned={})",
        no_spaces,
        r1,
        matches!(r1, Cow::Owned(_))
    );
    println!(
        "ensure_no_spaces({:?}) -> {:?} (is_owned={})",
        has_spaces,
        r2,
        matches!(r2, Cow::Owned(_))
    );

    let r3: Cow<str> = ensure_lowercase("already_lower");
    let r4: Cow<str> = ensure_lowercase("Has_Upper");
    println!(
        "ensure_lowercase(\"already_lower\") is_owned={}",
        matches!(r3, Cow::Owned(_))
    );
    println!(
        "ensure_lowercase(\"Has_Upper\")     is_owned={}",
        matches!(r4, Cow::Owned(_))
    );

    print_h3!("Deref: use like &str regardless");

    // Cow<str> derefs to str, so you can call all str methods on it
    let cow: Cow<str> = Cow::Borrowed("hello world");
    println!("cow.len()           = {}", cow.len()); // str method via Deref
    println!("cow.to_uppercase()  = {}", cow.to_uppercase());
    println!("cow.starts_with('h')= {}", cow.starts_with('h'));

    print_h3!("to_mut() - lazy clone");

    let original: &str = "hello";
    let mut cow: Cow<str> = Cow::Borrowed(original);
    println!(
        "Before to_mut: is_borrowed={}",
        matches!(cow, Cow::Borrowed(_))
    );

    cow.to_mut().push_str(" world"); // clones String on first mutation
    println!("After  to_mut: is_owned={}", matches!(cow, Cow::Owned(_)));
    println!("cow = {:?}", cow);

    // Repeated mutations don't re-clone
    cow.to_mut().push('!');
    println!("After 2nd mut: {:?}", cow);

    print_h3!("Cow<[T]>");

    let sorted_data: Vec<i32> = vec![1, 2, 3, 4, 5];
    let unsorted: Vec<i32> = vec![5, 3, 1, 4, 2];

    let r1: Cow<[i32]> = ensure_sorted(&sorted_data);
    let r2: Cow<[i32]> = ensure_sorted(&unsorted);

    println!(
        "sorted input:   is_owned={}, {:?}",
        matches!(r1, Cow::Owned(_)),
        r1
    );
    println!(
        "unsorted input: is_owned={}, {:?}",
        matches!(r2, Cow::Owned(_)),
        r2
    );

    print_h3!("Accepting Cow in API");

    println!("{}", process_name("Alice")); // &str - no allocation
    println!("{}", process_name(String::from("Bob"))); // String - moved in

    print_h3!("Error message pattern");

    for code in [404, 500, 418] {
        let msg: Cow<str> = describe_error(code);
        let is_owned: bool = matches!(msg, Cow::Owned(_));
        println!("describe_error({}) = {:?} (owned={})", code, msg, is_owned);
    }

    print_h3!("Size");
    println!(
        "size_of::<Cow<str>>()    = {}",
        std::mem::size_of::<Cow<str>>()
    );
    println!(
        "size_of::<String>()      = {}",
        std::mem::size_of::<String>()
    );
    println!("size_of::<&str>()        = {}", std::mem::size_of::<&str>());
    // Cow<str> is 3 words: variant tag + ptr + len (or ptr + len + cap for Owned)

    print_h3!("When to use");
    println!("Use Cow when: function sometimes needs to mutate, sometimes doesn't");
    println!("Use Cow when: function returns either a borrow or an owned value");
    println!("Use Cow when: avoiding unnecessary String::from() allocations in hot paths");
    println!("Don't use Cow when: always owned or always borrowed - use String or &str directly");
}
