fn main() {
    cc::Build::new()
        .file("c_src/math_utils.c")
        .file("c_src/rust_caller.c")
        .compile("c_ffi_examples");

    // math_utils.c uses sqrt() from libm
    println!("cargo:rustc-link-lib=m");

    println!("cargo:rerun-if-changed=c_src/math_utils.c");
    println!("cargo:rerun-if-changed=c_src/rust_caller.c");
}
