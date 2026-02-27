use shared::{print_h2, print_h3};

pub fn run() {
    print_h2!("Unsafe Functions and Blocks");

    // ------------------- unsafe fn -------------------
    print_h3!("unsafe fn");

    // Marking a fn unsafe means the caller must uphold invariants not checked by the compiler
    unsafe fn add_via_ptrs(a: *const i32, b: *const i32) -> i32 {
        // Rust 2024: unsafe fn body is safe-by-default, still needs explicit unsafe block
        return unsafe { *a + *b };
    }

    let x: i32 = 10;
    let y: i32 = 20;
    let result: i32 = unsafe { add_via_ptrs(&x, &y) };
    println!("add_via_ptrs(10, 20) = {}", result);

    // ------------------- Safe abstraction over unsafe -------------------
    print_h3!("Safe Abstraction over Unsafe");

    // The goal: expose a safe API with unsafe internals, documented invariants
    fn split_at_mid(slice: &[i32], mid: usize) -> (&[i32], &[i32]) {
        assert!(mid <= slice.len(), "mid {} out of bounds for len {}", mid, slice.len());
        let ptr: *const i32 = slice.as_ptr();
        // SAFETY: mid verified <= len, both slices are within the original allocation,
        //         lifetimes are tied to 'slice', no aliasing (non-overlapping halves)
        unsafe {
            let left: &[i32] = std::slice::from_raw_parts(ptr, mid);
            let right: &[i32] = std::slice::from_raw_parts(ptr.add(mid), slice.len() - mid);
            return (left, right);
        }
    }

    let arr: [i32; 6] = [1, 2, 3, 4, 5, 6];
    let (left, right) = split_at_mid(&arr, 3);
    println!("split_at_mid([1..6], 3) = {:?} | {:?}", left, right);

    // ------------------- slice::from_raw_parts -------------------
    print_h3!("slice::from_raw_parts");

    let data: Vec<i32> = vec![10, 20, 30, 40, 50];
    let ptr: *const i32 = data.as_ptr();
    let len: usize = data.len();
    // SAFETY: ptr is valid, aligned, initialized, data outlives the slice
    let reconstructed: &[i32] = unsafe { std::slice::from_raw_parts(ptr, len) };
    println!("Reconstructed slice = {:?}", reconstructed);

    // ------------------- transmute -------------------
    print_h3!("std::mem::transmute");

    // transmute is the most dangerous unsafe operation: it blindly reinterprets raw bytes.
    // Both types must have the same size (compiler checks this), but alignment and validity
    // are NOT checked. Transmuting to an invalid bit pattern is immediate UB.
    // Prefer type-specific methods (to_bits, from_bits, bytemuck) when possible.
    let f: f32 = 1.0_f32;
    #[allow(unnecessary_transmutes)]
    let bits: u32 = unsafe { std::mem::transmute::<f32, u32>(f) };
    println!("transmute f32(1.0) -> u32 = 0x{:08X}", bits); // IEEE 754: 0x3F800000

    // Same as the safe: f.to_bits()
    println!("f32::to_bits(1.0) = 0x{:08X}", f.to_bits());

    // Transmuting slices: reinterpret &[u8] as &[u32] (needs correct alignment+length)
    // DANGEROUS: only safe if alignment, size, and validity are guaranteed
    // Usually prefer bytemuck crate for this instead

    // ------------------- mem::forget -------------------
    print_h3!("std::mem::forget");

    // Prevents the destructor from running - valid but leaks resources
    let v: Vec<i32> = vec![1, 2, 3];
    std::mem::forget(v); // heap memory is leaked, no drop called
    println!("mem::forget(v) - destructor skipped, memory leaked intentionally");

    // Use case: transferring ownership to C code that will free the memory
    let s: String = String::from("transferred to C");
    let ptr: *mut u8 = s.as_ptr() as *mut u8;
    let _len: usize = s.len();
    std::mem::forget(s); // C side will free ptr
    println!("mem::forget - ptr {:p} transferred to C (not freed by Rust)", ptr);

    // ------------------- ManuallyDrop -------------------
    print_h3!("ManuallyDrop");

    use std::mem::ManuallyDrop;

    let mut md: ManuallyDrop<String> = ManuallyDrop::new(String::from("manual"));
    println!("ManuallyDrop<String> = {:?}", *md);
    md.push_str(" drop");
    println!("After push_str = {:?}", *md);
    // We are responsible for calling drop
    unsafe { ManuallyDrop::drop(&mut md) };
    // PANIC: Using *md after drop = use-after-free undefined behavior

    // ------------------- union -------------------
    print_h3!("union (C-style)");

    union IntOrFloat {
        i: i32,
        f: f32,
    }

    let u: IntOrFloat = IntOrFloat { i: 0x3F800000_i32 }; // IEEE 754 bits for 1.0
    let as_float: f32 = unsafe { u.f };
    let as_int: i32 = unsafe { u.i };
    println!("union {{ i: 0x3F800000 }}");
    println!("  interpreted as f32 = {}", as_float); // 1.0
    println!("  interpreted as i32 = {}", as_int);
    // Only one field is valid at a time - reading wrong field = undefined behavior

    // ------------------- Global mutable static -------------------
    print_h3!("Global Mutable static");

    static mut COUNTER: u32 = 0;
    unsafe {
        COUNTER += 1;
        COUNTER += 1;
        // Rust 2024: can't form &COUNTER (shared ref to mutable static = UB risk)
        // Use addr_of! / &raw const to get a raw pointer, then read through it
        let val: u32 = std::ptr::read(&raw const COUNTER);
        println!("COUNTER = {}", val);
    }
    // RACE CONDITION: static mut accessed from multiple threads = undefined behavior
    // Use AtomicU32 or Mutex<u32> for thread-safe global state instead

    // ------------------- Unsafe trait implementations -------------------
    print_h3!("Unsafe Traits: Send and Sync");

    // Send: type can be transferred across thread boundaries
    // Sync: type can be shared between threads (&T is Send)
    // Most types are automatically Send + Sync
    // Raw pointers are neither Send nor Sync (compiler won't auto-impl)

    struct MyWrapper(*mut i32);
    // SAFETY: we guarantee exclusive access through external synchronization
    unsafe impl Send for MyWrapper {}
    unsafe impl Sync for MyWrapper {}

    let mut val: i32 = 42;
    let w: MyWrapper = MyWrapper(&mut val as *mut i32);
    // Now MyWrapper can cross thread boundaries (user must uphold the safety guarantee)
    println!("MyWrapper implements Send + Sync via unsafe impl");
    drop(w);
}
