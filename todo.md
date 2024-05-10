# notes

## 5/10

- quick discussion on interview/job opportunities
- discussed refactoring *data structures* (vs. *code* and *text*), specifically `C` `structs`
  - assuming *good names* for both *types* and *fields*, aids in:
    - code structure/maintenance (DRY - Don't Repeat Yourself); reuse existing DS, *e.g.*, `typedef struct Coordinate`
    - abstraction; ability to write/read code at different levels/layers/depth of understanding
- reviewed/debugged `argparse` issues:
  - different behavior when run from the *debugger* vs. *terminal*
    > need to double-check this, and create a simple, repeatable, test-case
  - need better way of displaying `python` DS:
    - there are other ways, but start here and see what you can *figure out*
      - [pprint — Data pretty printer — Python 3.12.3 documentation](https://docs.python.org/3/library/pprint.html)
      - [Prettify Your Data Structures With Pretty Print in Python – Real Python](https://realpython.com/python-pretty-print/)
      - [Welcome! — Pygments](https://pygments.org/)
      - [Syntax Highlighting in python using pygments - Deepan Seeralan](https://www.deepanseeralan.com/tech/syntax-highlighting-code-in-python-using-pygments/)
  - need better understanding of `argparse` *side-effects*, *e.g.*, any assumptions made by `argparse`, that would impact *behavior*, such as `--flag` vs. `-f`

### 5/10 next

- debug (`argparse` issues) and complete argument parsing
- good luck and have fun❗

## 5/3

- *embedded struct* example **was** for you - see below (end of `4/23` notes)
- decided to *pair-program* next project, in contrast to the *top-down* approach we've historically used
- independently came to the same conclusion wrt *frustration*:
  - mismatch between the path you were on and the *spec* (table)
  - good learning experience as this type of mismatched objectives happens all the time in industry between product development teams and:
    - product management
    - quality assurance
    - product support
  > - asking lots of questions - w/people who you've established trust in the past - iteratively/incrementally is, imho, a good way to avoid these snafus
- discussed bug wrt order that parsers are declared which led to...*the grand (parser) refactoring* based on the idea of multiple parsers, and common args/opts:
  1. declare common args/opts (*e.g.*, `-i`, `-o`, *etc.*)
     1. parameterized over command specific values (*e.g.*, file names - `ct.txt` vs `pt.txt`, name of arg/opt - `in-file`, *etc.*)
  2. declare parser for (i.)
  3. declare/execute command (`keygen`, `encode`, `decode`) parser
  4. declare/execute one of three *command specific* parsers:
     1. based on (inherited?) from (ii.)
     2. declare and add command specific args/opts
  5. execute one command specific parser

> I think that's what we discussed, hypothesized, and agreed to, yes😎?

### 5/3 next

- review the *the grand (parser) refactoring*

## 4/23

- Discussed job interviews, which led to a discussion on possibly working on some sort of scientific software, *e.g.*, for inspiration:
  - **Proteins** may be of interest:
    - [RCSB PDB: Homepage](https://www.rcsb.org/)
    - [PDB-101: Browse: Visualizing Molecules](https://pdb101.rcsb.org/browse/visualizing-molecules)
    - [fogleman/ribbon: Ribbon diagrams of proteins in #golang.](https://github.com/fogleman/ribbon)
      - Pretty pictures – I’ve used other PKGs from GG – high quality in my experience
      - ![protein visualization](https://camo.githubusercontent.com/38781afa7fc29e23bc77335b4032ca3b1533b91f5b79362131622390c67c4972/687474703a2f2f692e696d6775722e636f6d2f554670724247742e706e67)
  - How about **biology/botany** and describing plants (and other natural phenomena I suspect) - **L-Systems**:
    - [An Introduction to Lindenmayer Systems](https://www-archiv.fdm.uni-hamburg.de/b-online/e28_3/lsys.html)
    - [Algorithmic Botany: Home](http://algorithmicbotany.org/)
  - **One of my favorite** books on modelling **natural systems** – implementation is J5 – but implementing this book – or a subset – could be a lot of fun and yield an interesting portfolio:
    - [Nature of Code](https://natureofcode.com/)
- I committed to an initial survey of **networking** in Python, and so discussed w/Python devs w/*way* more Python experience than me or you😎, did a *miniscule* amount of research, and ended up with:
  - sockets
    - [socket — Low-level networking interface — Python 3.12.3 documentation](https://docs.python.org/3/library/socket.html)
    - [Socket Programming HOWTO — Python 3.12.3 documentation](https://docs.python.org/3/howto/sockets.html)
  - http
    - [Requests: HTTP for Humans™ — Requests 2.31.0 documentation](https://docs.python-requests.org/en/latest/index.html)
  - packet sniffer
    - [Scapy](https://scapy.net/)
  - protocols
    - [Twisted](https://twisted.org/)
  - web frameworks
    - [Welcome to Flask — Flask Documentation (3.0.x)](https://flask.palletsprojects.com/en/3.0.x/)
    - [CherryPy — A Minimalist Python Web Framework](https://cherrypy.dev/)
    - [The web framework for perfectionists with deadlines | Django](https://www.djangoproject.com/)
    - [The Web Framework that scales with you. — TurboGears2 Website 3.0 documentation](https://turbogears.org/)
- We also discussed maintaining project/meeting notes in:
  - Markdown
  - Jupyter NBs?
- A flash from the past - in the form of `bsq` came next
  - Tried to determine why we used a `0`/`1` vs `o`/`.` for internal representation of the map
    - Maybe for a simper, validated, common structure?
    - Maybe a constraint from the original assignment?
      > Decided that in this case it wasn’t obvious
    - Discussed refactoring common fields into an embedded `struct`:

      ``` C
      typedef struct A {
        int x;
        int y;
        int z;
      };
      typedef struct B {
        A a;
        int z;
      };
      typedef struct C {
        A a
        B b;
        int z;
      };
      // ...
      C c;
      c.z = 1;
      c.b.z = 1;
      c.b.a.z = 1;
      c.a.z = 1;
      // ...
      ```

- Reviewed table (CLAs) from LS 4/19

### 4/23 next

- Implement p1 items from *table*
- Restructure notes as MD or NB and continue to use going forwards

> Thx for keeping current on Venmo  
>
> Good luck and have fun!

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
