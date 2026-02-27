use shared::{print_h2, print_h3};

pub fn run() {
    print_h2!("Raw Pointers");

    // ------------------- Creating raw pointers -------------------
    print_h3!("Creating Raw Pointers");

    let x: i32 = 42;
    let ptr_const: *const i32 = &x as *const i32; // immutable raw pointer
    let mut y: i32 = 100;
    let ptr_mut: *mut i32 = &mut y as *mut i32; // mutable raw pointer

    println!("ptr_const address = {:p}", ptr_const);
    println!("ptr_mut address   = {:p}", ptr_mut);

    // Creating a pointer to an arbitrary address is valid syntax (just can't deref it)
    let _dangling: *const i32 = 0x12345 as *const i32;
    // PANIC: unsafe { *_dangling } - undefined behavior (likely segfault)

    // ------------------- Dereferencing (requires unsafe) -------------------
    print_h3!("Dereferencing");

    let val: i32 = unsafe { *ptr_const };
    println!("*ptr_const = {}", val);

    unsafe {
        *ptr_mut = 200;
        println!("*ptr_mut after write = {}", *ptr_mut);
    }
    println!("y after ptr mutation = {}", y);

    // ------------------- Pointer arithmetic -------------------
    print_h3!("Pointer Arithmetic");

    let arr: [i32; 5] = [10, 20, 30, 40, 50];
    let base: *const i32 = arr.as_ptr();

    unsafe {
        for i in 0..5usize {
            // .add(n) advances by n * size_of::<T>() bytes; .offset(n) is the signed equivalent
            // Going out of bounds is immediate UB — the pointer must stay within the allocation
            let elem: *const i32 = base.add(i);
            println!("arr[{}] via ptr arithmetic = {}", i, *elem);
        }
    }

    unsafe {
        let third: *const i32 = base.offset(2); // signed variant of add
        println!("base.offset(2) = {}", *third);
    }

    // ------------------- Null pointers -------------------
    print_h3!("Null Pointers");

    let null_ptr: *const i32 = std::ptr::null();
    let null_mut: *mut i32 = std::ptr::null_mut();
    println!("null_ptr.is_null()  = {}", null_ptr.is_null());
    println!("null_mut.is_null()  = {}", null_mut.is_null());
    // PANIC: unsafe { *null_ptr } - null dereference = undefined behavior

    // ------------------- ptr::read / ptr::write -------------------
    print_h3!("ptr::read and ptr::write");

    let src: i32 = 999;
    // ptr::read copies the value (like dereferencing but explicit about Copy)
    let copied: i32 = unsafe { std::ptr::read(&src as *const i32) };
    println!("ptr::read(999) = {}", copied);

    let mut dst: i32 = 0;
    // ptr::write writes without reading/dropping the old value
    unsafe { std::ptr::write(&mut dst as *mut i32, 777) };
    println!("ptr::write -> dst = {}", dst);

    // ------------------- copy_nonoverlapping -------------------
    print_h3!("ptr::copy_nonoverlapping");

    let src_arr: [i32; 3] = [1, 2, 3];
    let mut dst_arr: [i32; 3] = [0; 3];
    unsafe {
        // Like C's memcpy: src and dst must not overlap
        std::ptr::copy_nonoverlapping(src_arr.as_ptr(), dst_arr.as_mut_ptr(), 3);
    }
    println!("copy_nonoverlapping([1,2,3]) -> {:?}", dst_arr);

    // ptr::copy allows overlapping regions (like C's memmove)
    unsafe {
        std::ptr::copy(dst_arr.as_ptr(), dst_arr.as_mut_ptr().add(0), 2);
    }
    println!("ptr::copy (memmove) result = {:?}", dst_arr);

    // ------------------- Thin vs fat pointers -------------------
    print_h3!("Pointer Sizes");

    // Thin pointer: just an address
    println!("size_of::<*const i32>()           = {} bytes", std::mem::size_of::<*const i32>());
    // Fat pointer: address + metadata (length or vtable)
    println!("size_of::<*const str>()            = {} bytes (ptr + len)", std::mem::size_of::<*const str>());
    println!(
        "size_of::<*const dyn std::fmt::Debug>() = {} bytes (ptr + vtable)",
        std::mem::size_of::<*const dyn std::fmt::Debug>()
    );

    // ------------------- What NOT to do: aliased mutable pointers -------------------
    print_h3!("UB: Aliased Mutable Pointers");
    // Two *mut pointing to same location and both written = undefined behavior
    // let mut z = 5;
    // let p1 = &mut z as *mut i32;
    // let p2 = &mut z as *mut i32;
    // unsafe { *p1 = 10; *p2 = 20; } // UNDEFINED BEHAVIOR - data race
    println!("Two *mut aliases to same data = undefined behavior (don't do this)");
}
