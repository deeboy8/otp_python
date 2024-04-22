# notes

## 4/19

- my attempt to *consolidate* and *capture* our discussions, Lessons, notes, and LSes - relating to `otp`'s command line arguments/options - in a reviewable/usable format:

```shell
usage: otp [--version] [--help] [--verbose [VERBOSE]] [--log-level [LOG-LEVEL]] 
        keygen [--length LENGTH] [--seed [SEED]] [--key-file KEY-FILE] |
        encode [--in-file [PT-FILE] | --text PT-STRING] [--out-file CT-FILE] 
            --key-file KEY-FILE | --key KEY-STRING | [--length [LENGTH] --seed [SEED]]] [--algorithm [ALGORITHM]] |
        decode [--in-file [CT-FILE] | --text CT-STRING] [--out-file PT-FILE] 
            --key-file KEY-FILE | --key KEY-STRING | [--length [LENGTH] --seed [SEED]]] [--algorithm [ALGORITHM]]
```

|          | pri | short name | option/arg                | description                                   | type      | missing        | default   | possible values                  | notes |
| -------- | --- | ---------- | ------------------------- | --------------------------------------------- | --------- | -------------- | --------- | -------------------------------- | ----- |
| `otp`    |     |            |                           |                                               |           |                |           |                                  |       |
|          | 1   |            | `--version`               | Show program's version number                 | BOOL      | `false`        |           |                                  |       |
|          | 1   |            | `--help`                  | Show help message                             | BOOL      | `false`        |           |                                  |       |
|          | 1   | `-v`       | `--verbose[=VERBOSE]`     | Set verbosity level                           | COUNTER   | `0`            | `1`       |                                  |       |
|          | 2   |            | `--log-level[=LOG-LEVEL]` | Set log level                                 | LOG-LEVEL | `error`        | `info`    | `debug`, `info`, `warn`, `error` |       |
| `keygen` | 1   |            |                           |                                               |           |                |           |                                  |       |
|          | 1   | `-l`       | `--length=LENGTH`         | Specify length of the key                     | INTEGER   | `128`          |           | $\{0, 1, 2, \ldots, N\}$         |       |
|          | 1   | `-s`       | `--seed[=SEED]`           | Specify seed for key generation               | INTEGER   | `current time` | `0`       | $\{1, 2, 3, \ldots, N\}$         |       |
|          | 1   | `-k`       | `--key-file[=KEY-FILE]`   | Specify key file                              | FILENAME  | `stdout`       | `key.txt` |                                  |       |
| `encode` | 1   |            |                           |                                               |           |                |           |                                  |       |
|          | 1   | `-i`       | `--in-file[=PT-FILE]`     | Specify input file for encoding [^5]          | FILENAME  | `stdin`        | `pt.txt`  |                                  |       |
|          | 1   | `-t`       | `--text=PT-STRING`        | Specify input text directly for encoding [^6] | STRING    |                |           |                                  |       |
|          | 1   | `-o`       | `--out-file[=CT-FILE]`    | Specify output file                           | FILENAME  | `stdout`       | `ct.txt`  |                                  |       |
|          | 1   | `-k`       | `--key-file=KEY-FILE`     | Specify key file [^1]                         | FILENAME  | `key.txt`      |           |                                  |       |
|          | 2   | `-x`       | `--key=KEY-STRING`        | Specify key directly  [^2]                    | STRING    |                |           |                                  |       |
|          | 2   | `-l`       | `--length=LENGTH`         | Specify length of the key  [^3]               | INTEGER   | `128`          |           |                                  |       |
|          | 1   | `-s`       | `--seed=SEED`             | Specify seed for key generation  [^4]         | INTEGER   | `current time` | `0`       |                                  |       |
|          | 2   | `-a`       | `--algorithm[=ALGORITHM]` | Specify encryption/decryption algorithm       | ALGORITHM | `xor`          | `mod`     | `mod`, `xor`                     |       |
| `decode` | 1   |            |                           |                                               |           |                |           |                                  |       |
|          | 1   | `-i`       | `--in-file[=CT-FILE]`     | Specify input file for decoding [^5]          | FILENAME  | `stdin`        | `ct.txt`  |                                  |       |
|          | 1   | `-t`       | `--text=CT-STRING`        | Specify input text directly for decoding [^6] | STRING    |                |           |                                  |       |
|          | 1   | `-o`       | `--out-file[=PT-FILE]`    | Specify output file                           | FILENAME  | `stdout`       | `pt.txt`  |                                  |       |
|          | 1   | `-k`       | `--key-file=KEY-FILE`     | Specify key file [^1]                         | FILENAME  | `key.txt`      |           |                                  |       |
|          | 2   | `-x`       | `--key=KEY-STRING`        | Specify key directly  [^2]                    | STRING    |                |           |                                  |       |
|          | 2   | `-l`       | `--length=LENGTH`         | Specify length of the key  [^3]               | INTEGER   | `128`          |           |                                  |       |
|          | 1   | `-s`       | `--seed=SEED`             | Specify seed for key generation  [^4]         | INTEGER   | `current time` | `0`       |                                  |       |
|          | 2   | `-a`       | `--algorithm[=ALGORITHM]` | Specify encryption/decryption algorithm       | ALGORITHM | `xor`          | `mod`     | `mod`, `xor`                     |       |
| TODO     |     |            |                           |                                               |           |                |           |                                  |       |
|          | 4   |            |                           | ability to specify alphabet                   |           |                |           |                                  |       |
|          | 3   |            |                           | design/refactor for (network) C/S support     |           |                |           |                                  |       |

[^1]: Can not be used w/ `key`, `length`, or `seed`
[^2]: Can not be used w/ `key-file`, `length`, or `seed`
[^3]: Can not be used w/ `key`or`key-|      file` and must be used w/ `seed`
[^4]: Can not be used w/ `key`or`key-file` and must be used w/ `length`
[^5]: Can not be used w/ `text`
[^6]: Can not be used w/ `in-file`

### 4/19 next

- complete `otp` (`pri-1`) command line per above

## 4/16

- in today’s Lesson – after catching up some personal going-ons, we had a lengthy, opinionated discussion about languages and tech:
  - imho, python’s too verbose, and seems to rely on a lot of *tribal myth* to be a true *pythonista*
  - I never liked that idiomatic `c` required `#define`-s be UPPERCASE, or that `go` uses the case of the first letter of an identifier to determine if it was *public* or *private*
  - again imho, python takes thing’s to the extreme, w/these types of conventions, *e.g.*:
    - [Single and Double Underscores in Python Names](https://realpython.com/python-double-underscore/#:~:text=Python%20developers%20let%20you%20know%20when%20an%20object,use%20within%20the%20containing%20module%2C%20class%2C%20or%20package)
  - once again, imho, I think python will remain relevant for years due to its current popularity and code base
    - I suspect it’ll be replaced for backend/infrastructure components w/a modern `c` replacement like `rust`
    - frontend (*i.e.*, some analysis, manipulation and visualization) development will be replaced by low-code/no-code tools
  - python’s rules for inheritance, *etc.* are not as bad as how `c++` has evolved, but, as we discussed:
    - [Inheritance and Composition: A Python OOP Guide](https://realpython.com/inheritance-composition-python/)
  - additionally, features feel like they’re being bolted-on:
    - [typing — Support for type hints](https://docs.python.org/3/library/typing.html)
- we then moved onto examining, discussing, and debugging to explain why your `encode | decode` pipeline was behaving as it was WRT the order that *debug prints* showed up on the screen:
  - this led to another discussion on standard handles and using `stderr` for error/debug data
  - consider the following pipeline:  
    > `demitri-otp> a | b | c`
    - conceptually, the shell starts `a`, `b`, and `c`, but before it allows them to run, it creates two pipes and attaches:
      - `stdout` of processes to the left of a pipe (*i.e.*, `a` and `b`), to the *write* end of the pipe
      - `stdin` of processes to the right of a pipe (*i.e.*, `b` and `c`),to the *read* end of the pipe
    - yielding the pipeline:
      > `a` → `stdout` → **pipe** → `stdin` → `b` → `stdout` → **pipe** → `stdin` → `c`
  - at this point, which process runs at any point in time is driven by the OS scheduler
  - it also (hopefully😎) shows why/how `demitri` and `demitri first` were printing in the order they were and which process was actually doing the printing
    - that is, your debug output was intermingling w/your (theoretical) cipher-text in your `encode | decode` pipeline
    - the pipes offer (buffering and) synchronization as `read` and `write` will block, if data is unavailable or the pipe is full, respectively
- we concluded w/a quick discussion on alternatives to *debug print*:
  - [Logging HOWTO](https://docs.python.org/3/howto/logging.html)
  - [Debugging in Visual Studio Code](https://code.visualstudio.com/Docs/editor/debugging#_logpoints)

### 4/16 – next

- take a break from `otp` and write a little test program (spike) to experiment w/pipelines
- complete the `otp` command line

good luck and have fun!

## 4/12

- reviewed standard handles (*i.e.*, `stdin`, `stdout`, and `stderr`) WRT to both *redirection* and *piping*, and the roles & resposibilities of:
  - application (process)
  - shell
  - OS
- peeked at `pytest` and discussed/demoed the much deeper UT integration, into VS Code,  compared to munit
  - test explorer
  - run/debug test codelens

### 4/12 next

- complete - production code and unit tests - `./otp` command line, based on discussions, using `argparse`

## 4/5

- discussed *classes* ('blueprints', 'templates', 'stencils') vs. *objects*, which are *instances* of a `class`
  - resources (*i.e.*, memory) are allocated to *objects*
  - discussed the very close relationship w/`C` `structs`
    - `structs` contain *public* data and lack any uniquely associated *behavior*
    - *classes* solve this via *encapsulation* and special functions - *methods*
    - data and functions that are part of a *class* are often referred to as *members* - *i.e.*, member data, member functions
- comparing `getopt` to `argparse` - the latter is *way* more verbose
  - part of the reason is it uses a *declarative* style
  - but mostly because it does *so* much more❗
- with that in mind, we dove a bit deeper into `argparse`, including a discussion (and some hinting 😎) WRT sub-parsers

Good luck and have fun!

### 4/5 next

- ensure repo, tooling, debugger, *etc.*, are completely setup
- complete argument parsing using `argparse`
