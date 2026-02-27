use shared::{print_h2, print_h3};

pub fn run() {
    print_h2!("Lifetimes");

    print_h3!("Basic lifetime annotations");
    let string1: String = String::from("long string");
    let string2: String = String::from("short");
    let result: &str = longest(&string1, &string2);
    println!("longest('{}', '{}') = '{}'", string1, string2, result);

    print_h3!("Multiple lifetimes");
    let text: String = String::from("hello world");
    let prefix: &str = "hello";
    let has: bool = starts_with(&text, prefix);
    println!("'{}' starts_with('{}')? {}", text, prefix, has);

    print_h3!("Lifetime in structs");
    let novel: String = String::from("Call me Ishmael. Some years ago...");
    let first_sentence: &str = novel.split('.').next().unwrap();
    let excerpt: Excerpt = Excerpt {
        part: first_sentence,
    };
    println!("Excerpt: '{}'", excerpt.part);
    println!("Novel still valid: {}", novel.len());
    // ERROR: Can't drop `novel` here while `excerpt` still holds reference to it
    // drop(novel); // Would fail to compile

    print_h3!("Methods with lifetimes");
    let announce: &str = "Breaking news!";
    let level: i32 = excerpt.announce_and_return_part(announce);
    println!("Announce level: {}", level);

    print_h3!("'static lifetime");
    // String literals are stored in the program's binary (rodata section),
    // so they live for the entire program — hence &'static str
    let static_str: &'static str = "I live forever"; // String literal
    println!("Static lifetime: '{}'", static_str);

    const CONSTANT: &str = "Also static";
    println!("Constant: '{}'", CONSTANT);

    // Box::leak intentionally leaks a heap allocation, giving it a 'static lifetime.
    // Useful when you need a &'static str at runtime (e.g. for error messages).
    // The memory is never freed — use sparingly.
    let leaked: &'static str = Box::leak(Box::new(String::from("leaked")));
    println!("Leaked to static: '{}'", leaked);

    print_h3!("Lifetime elision");
    // Lifetime elision rules allow omitting annotations in common patterns.
    // first_word's signature is really fn first_word<'a>(s: &'a str) -> &'a str
    // Rule: single input ref → output lifetime matches input lifetime
    let data: String = String::from("elision example");
    let first: &str = first_word(&data); // Compiler infers lifetimes
    println!("first_word('{}') = '{}'", data, first);

    print_h3!("Lifetime bounds");
    let ref_wrapper: RefWrapper<i32> = RefWrapper { value: &42 };
    ref_wrapper.print();

    print_h3!("Generic lifetime with trait");
    let s1: String = String::from("abc");
    let s2: String = String::from("xyz");
    println!(
        "longest_with_announcement: '{}'",
        longest_with_announcement(&s1, &s2, "Now")
    );

    print_h3!("Multiple struct references");
    let name: String = String::from("Alice");
    let age: i32 = 30;
    let person: Person = Person {
        name: &name,
        age: &age,
    };
    println!("Person: name='{}' age={}", person.name, person.age);

    print_h3!("Lifetime subtyping");
    let outer: String = String::from("outer");
    {
        let inner: String = String::from("inner");
        let longer: &str = longest(&outer, &inner);
        println!("Within scope: '{}'", longer);
    }
    // inner dropped, but outer still valid

    print_h3!("Lifetime elision in impl");
    let simple: SimpleRef = SimpleRef { data: &100 };
    simple.display(); // Method uses elided lifetime

    print_h3!("Common lifetime errors (commented)");
    // ERROR: Returning reference to local variable
    // fn dangling() -> &str {
    //     let s = String::from("hello");
    //     &s // ERROR: `s` does not live long enough - dropped at end of function
    // }

    // ERROR: "borrowed value does not live long enough"
    // let r: &str;
    // {
    //     let s = String::from("temp");
    //     r = &s; // ERROR: `s` does not live long enough
    // } // `s` dropped here while still borrowed
    // println!("{}", r); // ERROR: borrow later used here

    // ERROR: Storing reference that outlives data
    // struct Holder<'a> {
    //     data: &'a str,
    // }
    // let holder: Holder;
    // {
    //     let temp = String::from("temporary");
    //     holder = Holder { data: &temp }; // ERROR: `temp` does not live long enough
    // } // `temp` dropped here
    // println!("{}", holder.data); // Would access freed memory
}

// 'a is a lifetime parameter: it means "the return value lives at least as long as
// the shorter of x and y". The compiler uses this to prevent dangling references.
// Without 'a, the compiler can't tell which input the returned reference comes from.
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() {
        return x;
    }
    return y;
}

fn starts_with<'a, 'b>(text: &'a str, prefix: &'b str) -> bool {
    return text.starts_with(prefix);
}

fn first_word(s: &str) -> &str {
    return s.split_whitespace().next().unwrap_or("");
}

fn longest_with_announcement<'a, T: std::fmt::Display>(x: &'a str, y: &'a str, ann: T) -> &'a str {
    println!("Announcement: {}", ann);
    if x.len() > y.len() {
        return x;
    }
    return y;
}

// The lifetime 'a on the struct means: Excerpt cannot outlive the &str it holds.
// The compiler enforces this — you can't store Excerpt if the source string is dropped.
struct Excerpt<'a> {
    part: &'a str,
}

impl<'a> Excerpt<'a> {
    fn announce_and_return_part(&self, announcement: &str) -> i32 {
        println!("Attention: {}", announcement);
        return self.part.len() as i32;
    }
}

struct RefWrapper<'a, T> {
    value: &'a T,
}

impl<'a, T: std::fmt::Display> RefWrapper<'a, T> {
    fn print(&self) {
        println!("RefWrapper value: {}", self.value);
    }
}

struct Person<'a> {
    name: &'a str,
    age: &'a i32,
}

struct SimpleRef<'a> {
    data: &'a i32,
}

impl<'a> SimpleRef<'a> {
    fn display(&self) {
        println!("SimpleRef display: {}", self.data);
    }
}
