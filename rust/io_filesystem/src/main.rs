#![allow(dead_code)]
use shared::print_h1;
use std::io;

mod advanced;
mod directories;
mod file_io;
mod paths;
mod process;
mod stdio;

fn main() -> io::Result<()> {
    print_h1!("I/O & Filesystem");

    file_io::run()?;
    directories::run()?;
    paths::run()?;
    stdio::run()?;
    advanced::run()?;
    process::run()?;

    return Ok(());
}
