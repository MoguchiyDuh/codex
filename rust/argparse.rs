#!/usr/bin/env rust-script
//! ```cargo
//! [dependencies]
//! clap = { version = "4.5", features = ["derive"] }
//! ```
// ~/.cargo/bin/rust-script argparse.rs -- inp.txt --verbose -p 8080 --email example@gmail.com -e dev -o out.txt

use clap::{Parser, ValueEnum};

#[derive(Parser, Debug)]
#[command(name = "myapp")]
#[command(about = "Does stuff", long_about = None)]
struct Args {
    // Required positional argument
    input: String,

    // Optional flag with short and long form
    // --verbose, -v
    #[arg(short, long)]
    verbose: bool,

    // Option with default value
    #[arg(short, long, default_value_t = 10)]
    max_cons: u32,

    // Custom port validator
    #[arg(short, long, value_parser = port_validator)]
    port: u16,

    // Validation by range [0-120]
    #[arg(short, long, value_parser = clap::value_parser!(u8).range(0..=120), default_value_t = 10)]
    timeout: u8,

    // Custom email validator
    #[arg(long, value_parser = email_validator)]
    email: String,

    // Like Literal["dev", "prod", "test"]
    #[arg(short, long, value_parser = ["dev", "prod", "test"])]
    evironment: String,

    // Using enum in args
    #[arg(short, long, value_enum, default_value_t=LogLevel::Info)]
    log_level: LogLevel,

    // Optional value
    #[arg(short, long)]
    output: Option<String>,
}

#[derive(Debug, Clone, ValueEnum)]
enum LogLevel {
    #[value(name = "debug")]
    Debug,
    #[value(name = "info")]
    Info,
    #[value(name = "warn")]
    Warn,
    #[value(name = "error")]
    Error,
}

fn port_validator(s: &str) -> Result<u16, String> {
    let port: u16 = s
        .parse()
        .map_err(|_| format!("'{}' is not a valid port", s))?;

    if port < 1024 {
        Err(format!("Port must be >= 1024"))
    } else {
        Ok(port)
    }
}

fn email_validator(s: &str) -> Result<String, String> {
    if s.contains('@') && s.contains('.') {
        Ok(s.to_string())
    } else {
        Err(format!("'{}' is not a valid email", s))
    }
}

fn main() {
    let args = Args::parse();

    println!("Input: {:#?}", args);
}
