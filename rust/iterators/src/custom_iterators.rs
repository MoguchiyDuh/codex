use shared::{print_h2, print_h3};

pub fn run() {
    print_h2!("Custom Iterators");

    print_h3!("Implementing Iterator trait");
    struct Counter {
        current: u32,
        max: u32,
    }

    impl Counter {
        fn new(max: u32) -> Counter {
            return Counter { current: 0, max };
        }
    }

    impl Iterator for Counter {
        type Item = u32; // associated type: only one impl per struct, not a generic parameter

        fn next(&mut self) -> Option<Self::Item> {
            if self.current < self.max {
                self.current += 1;
                return Some(self.current);
            }
            return None;
        }
    }

    println!("Counter iterator:");
    for num in Counter::new(5) {
        println!("  {}", num);
    }

    // Can use all iterator methods
    let sum: u32 = Counter::new(10).sum();
    println!("Counter sum(1..=10): {}", sum);

    print_h3!("Iterator with state");
    struct Fibonacci {
        a: u64,
        b: u64,
    }

    impl Fibonacci {
        fn new() -> Fibonacci {
            return Fibonacci { a: 0, b: 1 };
        }
    }

    impl Iterator for Fibonacci {
        type Item = u64;

        fn next(&mut self) -> Option<Self::Item> {
            let current: u64 = self.a;
            self.a = self.b;
            self.b = current + self.b;
            // Always returns Some — infinite iterator; pair with .take(n) to bound it
            return Some(current);
        }
    }

    let fib: Vec<u64> = Fibonacci::new().take(10).collect();
    println!("\nFibonacci (first 10): {:?}", fib);

    print_h3!("DoubleEndedIterator");
    // Allows iteration from both ends
    struct Range {
        start: i32,
        end: i32,
    }

    impl Range {
        fn new(start: i32, end: i32) -> Range {
            return Range { start, end };
        }
    }

    impl Iterator for Range {
        type Item = i32;

        fn next(&mut self) -> Option<Self::Item> {
            if self.start < self.end {
                let current: i32 = self.start;
                self.start += 1;
                return Some(current);
            }
            return None;
        }
    }

    impl DoubleEndedIterator for Range {
        fn next_back(&mut self) -> Option<Self::Item> {
            if self.start < self.end {
                self.end -= 1;
                return Some(self.end);
            }
            return None;
        }
    }

    let mut range = Range::new(1, 6);
    println!("\nDoubleEndedIterator:");
    println!("  next: {:?}", range.next()); // 1
    println!("  next_back: {:?}", range.next_back()); // 5
    println!("  next: {:?}", range.next()); // 2
    println!("  next_back: {:?}", range.next_back()); // 4

    // Can use rev()
    let reversed: Vec<i32> = Range::new(1, 6).rev().collect();
    println!("  reversed: {:?}", reversed);

    print_h3!("ExactSizeIterator");
    // Knows exact remaining length
    struct ExactCounter {
        count: usize,
        max: usize,
    }

    impl ExactCounter {
        fn new(max: usize) -> ExactCounter {
            return ExactCounter { count: 0, max };
        }
    }

    impl Iterator for ExactCounter {
        type Item = usize;

        fn next(&mut self) -> Option<Self::Item> {
            if self.count < self.max {
                let current: usize = self.count;
                self.count += 1;
                return Some(current);
            }
            return None;
        }

        fn size_hint(&self) -> (usize, Option<usize>) {
            let remaining: usize = self.max - self.count;
            return (remaining, Some(remaining));
        }
    }

    // ExactSizeIterator requires size_hint() to return (n, Some(n)) — checked in debug builds
    impl ExactSizeIterator for ExactCounter {
        fn len(&self) -> usize {
            return self.max - self.count;
        }
    }

    let mut exact = ExactCounter::new(5);
    println!("\nExactSizeIterator:");
    println!("  initial len: {}", exact.len());
    exact.next();
    exact.next();
    println!("  after 2 next(): {}", exact.len());

    print_h3!("FusedIterator");
    // Guarantees None after first None (no need to check repeatedly)
    struct FusedCounter {
        count: u32,
        max: u32,
        done: bool,
    }

    impl FusedCounter {
        fn new(max: u32) -> FusedCounter {
            return FusedCounter {
                count: 0,
                max,
                done: false,
            };
        }
    }

    impl Iterator for FusedCounter {
        type Item = u32;

        fn next(&mut self) -> Option<Self::Item> {
            if self.done {
                return None;
            }
            if self.count < self.max {
                self.count += 1;
                return Some(self.count);
            }
            self.done = true;
            return None;
        }
    }

    impl std::iter::FusedIterator for FusedCounter {}

    let mut fused = FusedCounter::new(3);
    println!("\nFusedIterator:");
    println!("  {:?}", fused.next()); // Some(1)
    println!("  {:?}", fused.next()); // Some(2)
    println!("  {:?}", fused.next()); // Some(3)
    println!("  {:?}", fused.next()); // None
    println!("  {:?}", fused.next()); // Still None

    print_h3!("Custom iterator with method");
    struct PowersOfTwo {
        current: u64,
    }

    impl PowersOfTwo {
        fn new() -> PowersOfTwo {
            return PowersOfTwo { current: 1 };
        }

        fn starting_from(start: u64) -> PowersOfTwo {
            return PowersOfTwo { current: start };
        }
    }

    impl Iterator for PowersOfTwo {
        type Item = u64;

        fn next(&mut self) -> Option<Self::Item> {
            let result: u64 = self.current;
            // checked_mul returns None on overflow; ? propagates None, ending the iterator
            self.current = self.current.checked_mul(2)?;
            return Some(result);
        }
    }

    let powers: Vec<u64> = PowersOfTwo::new().take(10).collect();
    println!("\nPowers of 2: {:?}", powers);

    let powers_from_4: Vec<u64> = PowersOfTwo::starting_from(4).take(6).collect();
    println!("Powers from 4: {:?}", powers_from_4);

    print_h3!("Iterator wrapper");
    struct SkipOdd<I> {
        iter: I,
    }

    impl<I> Iterator for SkipOdd<I>
    where
        I: Iterator<Item = i32>,
    {
        type Item = i32;

        fn next(&mut self) -> Option<Self::Item> {
            loop {
                match self.iter.next() {
                    Some(n) if n % 2 == 0 => return Some(n),
                    Some(_) => continue, // Skip odd
                    None => return None,
                }
            }
        }
    }

    let nums: Vec<i32> = vec![1, 2, 3, 4, 5, 6, 7, 8];
    let skip_odd = SkipOdd {
        iter: nums.into_iter(),
    };
    let evens_only: Vec<i32> = skip_odd.collect();
    println!("\nSkipOdd wrapper: {:?}", evens_only);

    print_h3!("Infinite iterator");
    struct Infinite;

    impl Iterator for Infinite {
        type Item = i32;

        fn next(&mut self) -> Option<Self::Item> {
            return Some(42); // Always returns Some
        }
    }

    let first_10: Vec<i32> = Infinite.take(10).collect();
    println!("\nInfinite iterator (take 10): {:?}", first_10);

    print_h3!("Iterator from function");
    fn make_counter(max: u32) -> impl Iterator<Item = u32> {
        return (1..=max).into_iter();
    }

    let counter_fn: Vec<u32> = make_counter(5).collect();
    println!("\nIterator from fn: {:?}", counter_fn);
}
