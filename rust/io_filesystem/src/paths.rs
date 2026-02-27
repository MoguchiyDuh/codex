use shared::{print_h2, print_h3};
use std::io;
use std::path::{Component, Path, PathBuf};

pub fn run() -> io::Result<()> {
    print_h2!("Paths");

    let borrowed: &Path = Path::new("/usr/local/bin");
    let owned: PathBuf = PathBuf::from("/usr/local/bin");
    println!("Path: {}", borrowed.display());
    println!("PathBuf: {}", owned.display());

    print_h3!("Creating paths");
    let path1: PathBuf = PathBuf::from("file.txt");
    let path2: PathBuf = PathBuf::from("/home/user/file.txt");
    println!("\nCreated paths: {}, {}", path1.display(), path2.display());

    print_h3!("Joining paths");
    let mut base: PathBuf = PathBuf::from("/home/user");
    base.push("documents");
    base.push("file.txt");
    println!("\nJoined path: {}", base.display());

    let base2: &Path = Path::new("/home/user");
    let full: PathBuf = base2.join("documents").join("file.txt");
    println!("Join method: {}", full.display());

    print_h3!("Path components");
    let path: &Path = Path::new("/home/user/documents/file.txt");

    if let Some(parent) = path.parent() {
        println!("\nParent: {}", parent.display());
    }

    if let Some(name) = path.file_name() {
        println!("File name: {}", name.to_string_lossy());
    }

    if let Some(stem) = path.file_stem() {
        println!("File stem: {}", stem.to_string_lossy());
    }

    if let Some(ext) = path.extension() {
        println!("Extension: {}", ext.to_string_lossy());
    }

    print_h3!("Checking path types");
    let path_checks: &Path = Path::new(".");
    println!("\nCurrent directory checks:");
    println!("  exists: {}", path_checks.exists());
    println!("  is_file: {}", path_checks.is_file());
    println!("  is_dir: {}", path_checks.is_dir());
    println!("  is_absolute: {}", path_checks.is_absolute());
    println!("  is_relative: {}", path_checks.is_relative());

    print_h3!("Changing extension");
    let mut path_ext: PathBuf = PathBuf::from("document.txt");
    path_ext.set_extension("md");
    println!("\nChanged extension: {}", path_ext.display());

    println!("Removed extension: {}", path_ext.display());

    print_h3!("Changing file name");
    let mut path_name: PathBuf = PathBuf::from("/home/user/old.txt");
    path_name.set_file_name("new.txt");
    println!("\nChanged file name: {}", path_name.display());

    print_h3!("Pop (remove last component)");
    let mut path_pop: PathBuf = PathBuf::from("/home/user/documents/file.txt");
    path_pop.pop(); // Remove "file.txt"
    println!("\nAfter pop: {}", path_pop.display());
    path_pop.pop(); // Remove "documents"
    println!("After another pop: {}", path_pop.display());

    print_h3!("Iterating components");
    let path_iter: &Path = Path::new("/home/user/documents/file.txt");
    println!("\nPath components:");
    for component in path_iter.components() {
        match component {
            Component::RootDir => println!("  Root"),
            Component::Normal(name) => println!("  Normal: {}", name.to_string_lossy()),
            _ => println!("  Other: {:?}", component),
        }
    }

    print_h3!("Ancestors (parent chain)");
    let path_anc: &Path = Path::new("/home/user/documents/file.txt");
    println!("\nAncestors:");
    for ancestor in path_anc.ancestors() {
        println!("  {}", ancestor.display());
    }

    print_h3!("Canonical path (absolute, resolved)");

    let current_dir: PathBuf = std::env::current_dir()?;
    let canonical: PathBuf = current_dir.canonicalize()?;
    println!("\nCanonical path: {}", canonical.display());

    print_h3!("Relative paths");
    let base_path: &Path = Path::new("/home/user");
    let full_path: &Path = Path::new("/home/user/documents/file.txt");

    if let Ok(relative) = full_path.strip_prefix(base_path) {
        println!("\nRelative path: {}", relative.display());
    }

    print_h3!("Starts/ends with");
    let path_test: &Path = Path::new("/home/user/file.txt");
    println!("\nStarts with /home: {}", path_test.starts_with("/home"));
    println!("Ends with file.txt: {}", path_test.ends_with("file.txt"));

    print_h3!("to_string_lossy vs to_str");
    let path_str: &Path = Path::new("/home/user/file.txt");

    // to_string_lossy returns Cow<str>: borrows as &str if the path is valid UTF-8,
    // or allocates a new String with U+FFFD replacement chars for invalid bytes.
    let lossy: std::borrow::Cow<str> = path_str.to_string_lossy();
    println!("\nto_string_lossy: {}", lossy);

    // to_str returns None if the path contains non-UTF-8 bytes (common on Linux with bad filenames)
    if let Some(s) = path_str.to_str() {
        println!("to_str: {}", s);
    }

    print_h3!("Platform-specific separators");
    println!("\nPath separator: {:?}", std::path::MAIN_SEPARATOR);

    print_h3!("Collecting path parts");
    let parts: Vec<&Path> = path_iter.ancestors().collect();
    println!("\nPath parts: {} items", parts.len());

    print_h3!("Path comparison");
    let path_a: &Path = Path::new("/home/user/file.txt");
    let path_b: &Path = Path::new("/home/user/file.txt");
    let path_c: &Path = Path::new("/home/user/other.txt");

    println!("\nPath comparison:");
    println!("  a == b: {}", path_a == path_b);
    println!("  a == c: {}", path_a == path_c);

    print_h3!("Converting between Path and PathBuf");
    let path_ref: &Path = Path::new("file.txt");
    let path_owned: PathBuf = path_ref.to_path_buf();
    let path_borrowed: &Path = path_owned.as_path();
    println!(
        "\nConversions: {} -> {}",
        path_ref.display(),
        path_borrowed.display()
    );

    print_h3!("Common patterns");
    // Pattern: Check if file has specific extension
    fn has_extension(path: &Path, ext: &str) -> bool {
        return path.extension().and_then(|s| s.to_str()) == Some(ext);
    }

    let test_path: &Path = Path::new("document.txt");
    println!("\nHas .txt extension: {}", has_extension(test_path, "txt"));

    // Pattern: Get file name without extension
    fn name_without_ext(path: &Path) -> Option<String> {
        return path
            .file_stem()
            .and_then(|s| s.to_str())
            .map(|s| s.to_string());
    }

    if let Some(name) = name_without_ext(test_path) {
        println!("Name without ext: {}", name);
    }

    // Pattern: Build path from parts
    let parts: Vec<&str> = vec!["home", "user", "documents", "file.txt"];
    // PathBuf implements FromIterator<&str> — collect joins path components with the OS separator
    let built_path: PathBuf = parts.iter().collect();
    println!("\nBuilt from parts: {}", built_path.display());

    return Ok(());
}
