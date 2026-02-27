use shared::{print_h2, print_h3};
use std::fs::{self, DirEntry, Metadata};
use std::io;
use std::path::Path;

pub fn run() -> io::Result<()> {
    print_h2!("Directories");

    print_h3!("Creating directories");
    let dir: &str = "test_dir";
    fs::create_dir(dir)?;
    println!("Created directory: {}", dir);

    let nested: &str = "test_dir/nested/deep";
    fs::create_dir_all(nested)?;
    println!("Created nested: {}", nested);

    print_h3!("Checking directory existence");
    let exists: bool = Path::new(dir).exists();
    let is_dir: bool = Path::new(dir).is_dir();
    println!("\n{} exists: {}, is_dir: {}", dir, exists, is_dir);

    print_h3!("Reading directory contents");
    // Create some files for testing
    fs::write("test_dir/file1.txt", b"content1")?;
    fs::write("test_dir/file2.txt", b"content2")?;
    fs::write("test_dir/nested/file3.txt", b"content3")?;

    println!("\nDirectory contents:");
    let entries: fs::ReadDir = fs::read_dir(dir)?;
    for entry in entries {
        let entry: DirEntry = entry?;
        let path = entry.path();
        let metadata: Metadata = entry.metadata()?;

        println!(
            "  {} ({})",
            path.display(),
            if metadata.is_dir() { "dir" } else { "file" }
        );
    }

    print_h3!("Walking directory tree");
    fn walk_dir(path: &Path, depth: usize) -> io::Result<()> {
        if path.is_dir() {
            let indent: String = "  ".repeat(depth);
            println!("{}{}/", indent, path.file_name().unwrap().to_string_lossy());

            let entries: fs::ReadDir = fs::read_dir(path)?;
            for entry in entries {
                let entry: DirEntry = entry?;
                walk_dir(&entry.path(), depth + 1)?;
            }
        } else {
            let indent: String = "  ".repeat(depth);
            println!("{}{}", indent, path.file_name().unwrap().to_string_lossy());
        }
        return Ok(());
    }

    println!("\nDirectory tree:");
    walk_dir(Path::new(dir), 0)?;

    print_h3!("Directory metadata");
    let metadata: Metadata = fs::metadata(dir)?;
    println!("\nDirectory metadata:");
    println!("  Is directory: {}", metadata.is_dir());
    println!("  Is file: {}", metadata.is_file());
    println!("  Read-only: {}", metadata.permissions().readonly());

    // Modified time
    if let Ok(modified) = metadata.modified() {
        println!("  Modified: {:?}", modified);
    }

    print_h3!("Listing with filtering");
    println!("\nFiltering .txt files:");
    let entries: fs::ReadDir = fs::read_dir(dir)?;
    for entry in entries {
        let entry: DirEntry = entry?;
        if entry.path().extension().and_then(|s| s.to_str()) == Some("txt") {
            println!("  {}", entry.path().display());
        }
    }

    print_h3!("Recursive file collection");
    fn collect_files(path: &Path, files: &mut Vec<std::path::PathBuf>) -> io::Result<()> {
        if path.is_dir() {
            let entries: fs::ReadDir = fs::read_dir(path)?;
            for entry in entries {
                let entry: DirEntry = entry?;
                collect_files(&entry.path(), files)?;
            }
        } else {
            files.push(path.to_path_buf());
        }
        return Ok(());
    }

    let mut all_files: Vec<std::path::PathBuf> = Vec::new();
    collect_files(Path::new(dir), &mut all_files)?;
    println!("\nAll files recursively: {} files", all_files.len());
    for file in &all_files {
        println!("  {}", file.display());
    }

    print_h3!("Counting files and directories");
    fn count_entries(path: &Path) -> io::Result<(usize, usize)> {
        let mut files: usize = 0;
        let mut dirs: usize = 0;

        if path.is_dir() {
            dirs += 1;
            let entries: fs::ReadDir = fs::read_dir(path)?;
            for entry in entries {
                let entry: DirEntry = entry?;
                let (f, d) = count_entries(&entry.path())?;
                files += f;
                dirs += d;
            }
        } else {
            files += 1;
        }

        return Ok((files, dirs));
    }

    let (file_count, dir_count) = count_entries(Path::new(dir))?;
    println!("\nTotal: {} files, {} directories", file_count, dir_count);

    print_h3!("Directory size");
    fn dir_size(path: &Path) -> io::Result<u64> {
        let mut total: u64 = 0;

        if path.is_dir() {
            let entries: fs::ReadDir = fs::read_dir(path)?;
            for entry in entries {
                let entry: DirEntry = entry?;
                total += dir_size(&entry.path())?;
            }
        } else {
            total += fs::metadata(path)?.len();
        }

        return Ok(total);
    }

    let size: u64 = dir_size(Path::new(dir))?;
    println!("\nTotal directory size: {} bytes", size);

    print_h3!("Finding files by name");
    fn find_files(
        path: &Path,
        name: &str,
        results: &mut Vec<std::path::PathBuf>,
    ) -> io::Result<()> {
        if path.is_dir() {
            let entries: fs::ReadDir = fs::read_dir(path)?;
            for entry in entries {
                let entry: DirEntry = entry?;
                find_files(&entry.path(), name, results)?;
            }
        } else if path.file_name().and_then(|s| s.to_str()) == Some(name) {
            results.push(path.to_path_buf());
        }
        return Ok(());
    }

    let mut found: Vec<std::path::PathBuf> = Vec::new();
    find_files(Path::new(dir), "file1.txt", &mut found)?;
    println!("\nFound 'file1.txt': {:?}", found);

    print_h3!("Empty directory check");
    fn is_empty_dir(path: &Path) -> io::Result<bool> {
        let entries: fs::ReadDir = fs::read_dir(path)?;
        return Ok(entries.count() == 0);
    }

    let empty: bool = is_empty_dir(Path::new(nested))?;
    println!("\nIs {} empty? {}", nested, empty);

    print_h3!("Removing directories");
    // remove_dir - only if empty
    fs::remove_dir(nested)?;
    println!("\nRemoved empty directory: {}", nested);

    // remove_dir_all - removes recursively
    fs::remove_dir_all(dir)?;
    println!("Removed directory tree: {}", dir);

    return Ok(());
}
