use shared::{print_h2, print_h3};
use std::fs::{self, File, Permissions};
use std::io::{self, Write};
use std::path::Path;

pub fn run() -> io::Result<()> {
    print_h2!("Advanced Operations");

    print_h3!("Copying files");
    let src: &str = "source.txt";
    let dst: &str = "destination.txt";

    fs::write(src, b"Content to copy")?;
    fs::copy(src, dst)?;
    println!("Copied {} to {}", src, dst);

    let copied_content: String = fs::read_to_string(dst)?;
    println!("Copied content: {}", copied_content);

    print_h3!("Moving/renaming files");
    let old_name: &str = "old.txt";
    let new_name: &str = "new.txt";

    fs::write(old_name, b"Moving this file")?;
    fs::rename(old_name, new_name)?;
    println!("\nRenamed {} to {}", old_name, new_name);
    println!("Old name exists: {}", Path::new(old_name).exists());
    println!("New name exists: {}", Path::new(new_name).exists());

    print_h3!("Hard links");
    let original: &str = "original.txt";
    let hardlink: &str = "hardlink.txt";

    fs::write(original, b"Original content")?;
    fs::hard_link(original, hardlink)?;
    println!("\nCreated hard link: {}", hardlink);

    let metadata1 = fs::metadata(original)?;
    let metadata2 = fs::metadata(hardlink)?;
    println!(
        "Same inode (file size match): {} == {}",
        metadata1.len(),
        metadata2.len()
    );

    print_h3!("Symbolic links");
    #[cfg(unix)]
    {
        let target: &str = "target.txt";
        let symlink: &str = "symlink.txt";

        fs::write(target, b"Target content")?;
        std::os::unix::fs::symlink(target, symlink)?;
        println!("\nCreated symlink: {} -> {}", symlink, target);

        let is_symlink: bool = fs::symlink_metadata(symlink)?.is_symlink();
        println!("Is symlink: {}", is_symlink);

        let link_target = fs::read_link(symlink)?;
        println!("Link points to: {}", link_target.display());

        fs::remove_file(symlink)?;
        fs::remove_file(target)?;
    }

    print_h3!("File permissions");
    let perm_file: &str = "permissions.txt";
    fs::write(perm_file, b"Test permissions")?;

    let metadata = fs::metadata(perm_file)?;
    let perms: Permissions = metadata.permissions();
    println!("\nRead-only: {}", perms.readonly());

    let mut new_perms: Permissions = perms.clone();
    new_perms.set_readonly(true);
    fs::set_permissions(perm_file, new_perms)?;
    println!("Set to read-only");

    let updated_perms = fs::metadata(perm_file)?.permissions();
    println!("Now read-only: {}", updated_perms.readonly());

    let mut writable_perms: Permissions = updated_perms;
    writable_perms.set_readonly(false);
    fs::set_permissions(perm_file, writable_perms)?;
    println!("Set back to writable");

    print_h3!("Unix-specific permissions");
    #[cfg(unix)]
    {
        use std::os::unix::fs::PermissionsExt;

        let metadata = fs::metadata(perm_file)?;
        let mode: u32 = metadata.permissions().mode();
        println!("\nUnix mode: {:o}", mode);

        // Set specific mode (e.g., 0o644 = rw-r--r--)
        let new_perms = Permissions::from_mode(0o644);
        fs::set_permissions(perm_file, new_perms)?;
        println!("Set mode to 0o644");
    }

    print_h3!("Temporary files");
    use std::env;

    let temp_dir: std::path::PathBuf = env::temp_dir();
    println!("\nSystem temp dir: {}", temp_dir.display());

    let temp_file: std::path::PathBuf = temp_dir.join("my_temp_file.txt");
    fs::write(&temp_file, b"Temporary data")?;
    println!("Created temp file: {}", temp_file.display());

    fs::remove_file(&temp_file)?;
    println!("Removed temp file");

    print_h3!("File timestamps");
    let timestamp_file: &str = "timestamps.txt";
    fs::write(timestamp_file, b"Check timestamps")?;

    let metadata = fs::metadata(timestamp_file)?;

    if let Ok(created) = metadata.created() {
        println!("\nCreated: {:?}", created);
    }

    if let Ok(modified) = metadata.modified() {
        println!("Modified: {:?}", modified);
    }

    if let Ok(accessed) = metadata.accessed() {
        println!("Accessed: {:?}", accessed);
    }

    print_h3!("File size");
    let size_file: &str = "size_test.txt";
    fs::write(size_file, b"Testing file size")?;

    let size: u64 = fs::metadata(size_file)?.len();
    println!("\nFile size: {} bytes", size);

    print_h3!("Atomic writes (write to temp, then rename)");
    // Write-then-rename is atomic on POSIX filesystems: readers see either the old file
    // or the complete new file — never a partial write. This is the standard pattern
    // for safe file updates (used by editors, package managers, databases, etc.).
    let final_path: &str = "atomic.txt";
    let temp_path: &str = "atomic.txt.tmp";

    // Write to temp file
    let mut temp_file: File = File::create(temp_path)?;
    temp_file.write_all(b"Atomic write content")?;
    temp_file.sync_all()?; // Flush kernel buffers to disk before rename

    fs::rename(temp_path, final_path)?;
    println!("\nAtomic write completed: {}", final_path);

    print_h3!("Syncing to disk");
    let sync_file: &str = "sync_test.txt";
    let mut file: File = File::create(sync_file)?;
    file.write_all(b"Important data")?;

    file.sync_all()?;
    println!("\nSynced all to disk");

    file.sync_data()?;
    println!("Synced data to disk");

    print_h3!("File locking (platform-specific)");
    #[cfg(unix)]
    {
        println!("\nFile locking available on Unix");
        // Would use flock or fcntl (requires external crate for safe API)
    }

    print_h3!("Checking disk space");
    // Requires external crate like `fs2` or `sys-info`
    println!("\nDisk space check requires external crate");

    print_h3!("Cleaning up test files");
    fs::remove_file(src)?;
    fs::remove_file(dst)?;
    fs::remove_file(new_name)?;
    fs::remove_file(original)?;
    fs::remove_file(hardlink)?;
    fs::remove_file(perm_file)?;
    fs::remove_file(timestamp_file)?;
    fs::remove_file(size_file)?;
    fs::remove_file(final_path)?;
    fs::remove_file(sync_file)?;
    println!("\nCleaned up all test files");

    return Ok(());
}
