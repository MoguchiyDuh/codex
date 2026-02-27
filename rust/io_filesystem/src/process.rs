use shared::{print_h2, print_h3};
use std::io::{self, Write};
use std::process::{Command, ExitStatus, Output, Stdio};

pub fn run() -> io::Result<()> {
    print_h2!("Process & Command");

    print_h3!("Basic execution");

    let status: ExitStatus = Command::new("echo").arg("hello from Command").status()?;
    println!("echo exit status: success={}", status.success());
    println!("echo exit code:   {:?}", status.code()); // Some(0)

    print_h3!("Capture output");

    let output: Output = Command::new("echo").args(["line 1", "line 2"]).output()?;

    println!(
        "stdout: {:?}",
        String::from_utf8_lossy(&output.stdout).trim()
    );
    println!("stderr: {:?}", String::from_utf8_lossy(&output.stderr));
    println!("exit:   {}", output.status.success());

    print_h3!("Commands with arguments");

    let ls_output: Output = Command::new("ls").args(["-la", "/tmp"]).output()?;

    let ls_str: String = String::from_utf8_lossy(&ls_output.stdout).to_string();
    let line_count: usize = ls_str.lines().count();
    println!("ls -la /tmp: {} lines", line_count);

    print_h3!("Environment variables");

    let with_env: Output = Command::new("sh")
        .arg("-c")
        .arg("echo $GREETING")
        .env("GREETING", "hello from rust")
        .output()?;
    println!(
        "with env var: {:?}",
        String::from_utf8_lossy(&with_env.stdout).trim()
    );

    let multi_env: Output = Command::new("sh")
        .arg("-c")
        .arg("echo $A $B")
        .envs([("A", "foo"), ("B", "bar")])
        .output()?;
    println!(
        "with envs: {:?}",
        String::from_utf8_lossy(&multi_env.stdout).trim()
    );

    let clean: Output = Command::new("env")
        .env_clear()
        .env("ONLY_THIS", "1")
        .output()?;
    let clean_vars: usize = String::from_utf8_lossy(&clean.stdout).lines().count();
    println!(
        "env_clear + one var: {} lines (vs {} without clear)",
        clean_vars,
        std::env::vars().count()
    );

    print_h3!("Working directory");

    let cwd_output: Output = Command::new("pwd").current_dir("/tmp").output()?;
    println!(
        "pwd with current_dir(/tmp): {:?}",
        String::from_utf8_lossy(&cwd_output.stdout).trim()
    );

    print_h3!("Stdin piping");

    // Stdio::piped() creates an OS pipe. child.stdin is Option<ChildStdin> — Some when piped.
    // We must write to stdin BEFORE calling wait_with_output(), or we risk deadlock
    // if the child blocks waiting for input while we block waiting for it to finish.
    let mut child = Command::new("cat")
        .stdin(Stdio::piped())
        .stdout(Stdio::piped())
        .spawn()?;

    if let Some(stdin) = child.stdin.as_mut() {
        stdin.write_all(b"hello from stdin\nline two\n")?;
    }

    // wait_with_output() closes stdin (signals EOF to child), then waits for it to exit
    let piped_output: Output = child.wait_with_output()?;
    println!(
        "cat (from stdin): {:?}",
        String::from_utf8_lossy(&piped_output.stdout).trim()
    );

    print_h3!("Piping commands together");

    // echo "a\nb\nc" | sort -r
    let mut echo_child = Command::new("sh")
        .arg("-c")
        .arg("printf 'c\\nb\\na\\n'")
        .stdout(Stdio::piped())
        .spawn()?;

    // .take() extracts the ChildStdout from the Option, leaving None.
    // Stdio::from() converts the ChildStdout into a Stdio that can be given to the next process.
    let echo_stdout: Stdio = Stdio::from(echo_child.stdout.take().unwrap());

    let sort_output: Output = Command::new("sort").arg("-r").stdin(echo_stdout).output()?;

    echo_child.wait()?;
    println!(
        "printf | sort -r: {:?}",
        String::from_utf8_lossy(&sort_output.stdout).trim()
    );

    print_h3!("Suppress output");

    let quiet: ExitStatus = Command::new("ls")
        .arg("/tmp")
        .stdout(Stdio::null())
        .stderr(Stdio::null())
        .status()?;
    println!("ls /tmp (silent): exit={}", quiet.success());

    print_h3!("Exit codes");

    let fail: ExitStatus = Command::new("sh").args(["-c", "exit 42"]).status()?;
    println!(
        "exit 42: code={:?}, success={}",
        fail.code(),
        fail.success()
    );

    let ok: ExitStatus = Command::new("sh").args(["-c", "exit 0"]).status()?;
    println!("exit 0:  code={:?}, success={}", ok.code(), ok.success());

    print_h3!("Spawn and wait");

    let mut handle = Command::new("sleep")
        .arg("0.01") // 10ms
        .spawn()?;

    println!("subprocess id = {}", handle.id());

    let not_done: Option<ExitStatus> = handle.try_wait()?;
    println!("try_wait (before done): {:?}", not_done);

    let final_status: ExitStatus = handle.wait()?;
    println!("wait() (after done): success={}", final_status.success());

    print_h3!("Kill");

    let mut long_process = Command::new("sleep").arg("100").spawn()?;
    println!("spawned sleep 100, pid={}", long_process.id());
    long_process.kill()?;
    let killed: ExitStatus = long_process.wait()?;
    println!("after kill: success={}", killed.success());

    return Ok(());
}
