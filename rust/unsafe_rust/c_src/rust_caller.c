/* Declare Rust-exported functions - defined with #[unsafe(no_mangle)] in ffi_basics.rs */
extern int rust_add(int a, int b);
extern int rust_square(int x);

/* C wrapper that delegates straight to Rust */
int call_rust_add(int a, int b) {
    return rust_add(a, b);
}

/* Rust → C → Rust round trip: C uses rust_add internally */
int double_via_rust(int x) {
    return rust_add(x, x);
}

/* Chains two Rust functions: computes (a + b)^2 */
int sum_then_square(int a, int b) {
    int sum = rust_add(a, b);
    return rust_square(sum);
}
