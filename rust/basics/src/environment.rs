use shared::{print_h2, print_h3};
use std::env;
use std::path::PathBuf;

pub fn run() {
    print_h2!("Environment");

    print_h3!("Command-line arguments");

    // env::args() returns an iterator of strings (program name + args)
    // env::args_os() returns OsString (handles non-UTF8 paths on some platforms)
    let args: Vec<String> = env::args().collect();
    println!("args count = {}", args.len());
    println!("args[0] (program) = {:?}", args[0]); // path to the binary

    // Skip the program name
    let user_args: Vec<String> = env::args().skip(1).collect();
    println!("user args = {:?}", user_args); // empty when running via cargo run

    // Typical pattern: parse args manually
    fn parse_args() -> Option<String> {
        return env::args().nth(1); // first user arg, or None
    }
    println!("first user arg = {:?}", parse_args());

    print_h3!("Environment variables");

    // env::var() - read single var, returns Err if not set or invalid UTF-8
    let path: Result<String, env::VarError> = env::var("PATH");
    match &path {
        Ok(p) => println!("PATH (first 60 chars) = {}...", &p[..p.len().min(60)]),
        Err(e) => println!("PATH not set: {}", e),
    }

    // env::var_os() - returns OsString, doesn't fail on non-UTF8
    let home: Option<std::ffi::OsString> = env::var_os("HOME");
    println!("HOME = {:?}", home);

    // Common pattern: env var with fallback
    let log_level: String = env::var("LOG_LEVEL").unwrap_or_else(|_| String::from("info"));
    println!("LOG_LEVEL (with default) = {}", log_level);

    let port: u16 = env::var("PORT")
        .unwrap_or_else(|_| String::from("8080"))
        .parse()
        .unwrap_or(8080);
    println!("PORT (parsed u16) = {}", port);

    // Presence check pattern
    let debug_mode: bool = env::var("DEBUG").is_ok();
    println!("DEBUG mode = {}", debug_mode);

    print_h3!("Set and remove");

    // env::set_var() / env::remove_var() - unsafe in multithreaded contexts
    // In Rust 2024, these are marked unsafe due to POSIX thread-safety rules
    // Safe to use in single-threaded programs or before spawning threads
    unsafe {
        env::set_var("MY_APP_TOKEN", "secret123");
    }
    println!("MY_APP_TOKEN = {:?}", env::var("MY_APP_TOKEN").unwrap());

    unsafe {
        env::remove_var("MY_APP_TOKEN");
    }
    println!("MY_APP_TOKEN after remove = {:?}", env::var("MY_APP_TOKEN"));

    print_h3!("Iterate all vars");

    let count: usize = env::vars().count();
    println!("Total env vars = {}", count);

    // Print vars starting with "CARGO_" (common when running under cargo)
    let cargo_vars: Vec<(String, String)> = env::vars()
        .filter(|(k, _)| k.starts_with("CARGO_PKG"))
        .collect();
    println!("CARGO_PKG_* vars:");
    for (k, v) in &cargo_vars {
        println!("  {} = {}", k, v);
    }

    // env::vars_os() for non-UTF8-safe iteration
    let os_count: usize = env::vars_os().count();
    println!("vars_os count = {} (same count, OsString keys)", os_count);

    print_h3!("Paths");

    // Current working directory
    let cwd: PathBuf = env::current_dir().unwrap();
    println!("current_dir = {:?}", cwd);

    // Change working directory (affects the whole process)
    // env::set_current_dir("/tmp").unwrap();

    // Executable path
    let exe: Result<PathBuf, _> = env::current_exe();
    println!(
        "current_exe = {:?}",
        exe.ok().map(|p| p.display().to_string())
    );

    // Temp directory
    let tmp: PathBuf = env::temp_dir();
    println!("temp_dir = {:?}", tmp);

    print_h3!("Config loading pattern");

    #[derive(Debug)]
    struct AppConfig {
        host: String,
        port: u16,
        debug: bool,
        workers: usize,
    }

    impl AppConfig {
        fn from_env() -> Self {
            return AppConfig {
                host: env::var("APP_HOST").unwrap_or_else(|_| String::from("127.0.0.1")),
                port: env::var("APP_PORT")
                    .ok()
                    .and_then(|s| s.parse().ok())
                    .unwrap_or(3000),
                debug: env::var("APP_DEBUG")
                    .map(|v| v == "1" || v == "true")
                    .unwrap_or(false),
                workers: env::var("APP_WORKERS")
                    .ok()
                    .and_then(|s| s.parse().ok())
                    .unwrap_or(4),
            };
        }
    }

    let config: AppConfig = AppConfig::from_env();
    println!("AppConfig::from_env() = {:?}", config);
}
