# Piping & Redirection Cheat Sheet

In GNU/Linux, commands communicate via standard data streams. Redirection and piping allow you to intercept, route, and chain these streams to build powerful command-line pipelines.

---

## 1. Theory

### Standard Streams

Every process is initialized with three default data streams represented by integer file descriptors:

| Descriptor | Stream     | Name            | Default Device    |
| :--------- | :--------- | :-------------- | :---------------- |
| `0`        | **stdin**  | Standard Input  | Keyboard          |
| `1`        | **stdout** | Standard Output | Screen / Terminal |
| `2`        | **stderr** | Standard Error  | Screen / Terminal |

### Redirection Operators

- **Output Redirection (`>`, `>>`)**
  - `command > file`: Directs stdout to `file` (overwrites existing content).
  - `command >> file`: Appends stdout to the end of `file`.
  - `command 2> file`: Directs stderr to `file` (overwrites).
  - `command 2>> file`: Appends stderr to the end of `file`.
  - `command &> file` (or `command > file 2>&1`): Directs both stdout and stderr to `file`.
- **Input Redirection (`<`, `<<`, `<<<`)**
  - `command < file`: Feeds the contents of `file` into command's stdin.
  - `command << DELIMITER`: Feeds multi-line input (Here-Doc) into stdin until `DELIMITER` is met.
  - `command <<< "string"`: Feeds a single string (Here-String) into stdin.
- **Pipes (`|`, `|&`)**
  - `cmd1 | cmd2`: Routes the stdout of `cmd1` to the stdin of `cmd2`.
  - `cmd1 |& cmd2` (or `cmd1 2>&1 | cmd2`): Routes both stdout and stderr of `cmd1` to the stdin of `cmd2`.

---

## 2. Tasks & Concrete Examples

### Stream Separation & Silencing

#### Redirect stdout and stderr separately

```bash
ls /exists /doesntexist > stdout.txt 2> stderr.txt
```

#### Silence stdout only (errors still print)

```bash
ls /exists /doesntexist > /dev/null
```

#### Silence stderr only (output still prints)

```bash
ls /exists /doesntexist 2> /dev/null
```

#### Silence all output completely

```bash
ls /exists /doesntexist &> /dev/null
# Or POSIX-compliant:
ls /exists /doesntexist > /dev/null 2>&1
```

---

### Input Redirection

#### Feed file contents to command stdin

```bash
sort < unsorted.txt
```

#### Feed multi-line block directly to a command (Here-Document)

```bash
cat << EOF > story.txt
Once upon a time,
there was a shell user.
EOF
```

#### Feed a single string directly to stdin (Here-String)

```bash
grep "search" <<< "this is a search string"
```

---

### Pipes & Pipelines

#### Count files in a directory

```bash
ls /usr/bin | wc -l
```

#### Filter processes by keyword

```bash
ps aux | grep bash
```

#### Pipeline with sorting and deduplication

```bash
cat names.txt | sort | uniq
```

#### Pipe stdout and stderr together

```bash
ls /exists /doesntexist 2>&1 | wc -l
# Or using Bash shorthand:
ls /exists /doesntexist |& wc -l
```

#### Split output to a file and screen concurrently

```bash
command | tee output.txt
```

---

## 3. Key Redirection Pitfalls

### The Left-to-Right Evaluation Pitfall

The shell processes redirections from left to right. Order matters.

- **Incorrect Attempt to Silence Both Streams:**
  ```bash
  command 2>&1 > /dev/null
  ```

  - _Result:_ `stderr` (2) is redirected to where `stdout` (1) currently points (the terminal). Then `stdout` (1) is redirected to `/dev/null`. Stderr still prints to the terminal.
- **Correct Syntax:**
  ```bash
  command > /dev/null 2>&1
  ```

  - _Result:_ `stdout` (1) is redirected to `/dev/null`. Then `stderr` (2) is redirected to point to the current location of `stdout` (which is now `/dev/null`). Both streams are correctly silenced.

### Direct File Argument vs. Stdin Redirection

- **Reading via file argument:**
  ```bash
  wc -l file.txt
  # Output: 15 file.txt (includes filename)
  ```
- **Reading via stdin redirection:**
  ```bash
  wc -l < file.txt
  # Output: 15 (only the count, command does not know the filename)
  ```
