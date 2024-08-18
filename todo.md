# notes

## 8/16

## 8/13

## 8/9

- Discussed how, after some reading/review/navel gazing😎, you had better understanding of, and even wrote some initial `typer` code❗
- High level chat about `pytest`, and how most (all?) UT frameworks tend to offer these four services:
  - Organization (_e.g._, suites, fixtures, UT function-signatures, _etc._)
  - Assertion framework
  - Runner
  - Reporter
- Reviewed my latest find, [futurecoder](https://futurecoder.io/course/#toc)
, and it’s friends:
  
  - [Online Python Tutor - visualize, debug, get AI help for Python, Java, C, C++, and JavaScript](https://pythontutor.com/)
  - [alexmojaki/snoop: A powerful set of Python debugging tools, based on PySnooper](https://github.com/alexmojaki/snoop)
  - [birdseye — birdseye documentation](https://birdseye.readthedocs.io/en/latest/)
  - [alexmojaki (Alex Hall)](https://github.com/alexmojaki)
- Discussed project status/progress as it felt, at least to me, that we’d stalled:
  - Already refocused on writing code, using `typer`, starting w/`otp`'s five _commands_ and their associated `arguments` and `options`
    - we agreed to call `otp` -  `app` - and use `commands` for (my temp names, pick your own or use these): `keygen`, `encode`, `decode`, `encode_d`, and `decode_d`
  - See [otp_discussion.py - Replit](https://replit.com/@DemitrusBooker/otpdiscussionpy#main.py)
- Continued review of typer
  - Turns out that it may have been:
    > "_...going in one ear and out the other..._" 😎
  - We agreed to surface these issues sooner so that we continue to make good use of our time together
- Touched on generic type (_e.g._, `List[int]`)
- Peeked at some of `typer`’s features such as `help`, `version`, `panels`, and the general use of [`rich`](https://rich.readthedocs.io/en/stable/) for UI

### 8/16 next

- Complete command line design and `typer` functions to support

## 8/6

## 8/2

In our most recent meetings, we…

- Caught up on the status of your DS cohort (vacation?) and _taking your time_ w/the **DC Course**
- Discussed Olympics/politics
- Continued review of **RP’s Socket article**:
  - _Selectors_, and the entire _multi-connect client/server_ is still a bit _muddy_
    - Put on back-burner for now
    - Jump directly into code when we pull it back onto the front-burner
    - Further discussed _sockets_ as a mechanism for binding an _address_ (_e.g._, computer) and _port_ (_i.e._, specific app)
    - Discussed how the **echo C/S** has an _implied protocol_ – assumptions made about its format, _etc_.
- Took a bit of a detour to discuss `regex` – very important topic…you should **definitely** continue to learn
- Began to review `typer` docs/code and discussed why I chose it vs. `fire` vs. `click` vs. …
- Walked through `typer` code on replit

### 8/6 next

- Continue review of `typer` – in context of `otp`
- **Offline**: continue to review RP Sockets article, and research sockets/hosts(addresses) and ports, to gain a better understanding before our return

Good luck and have fun!

## 7/26

## 7/29

- Discussed:
  - Future planning and Sept. milestone (moving)
  - How DS cohort seems to be on vacation 😎
  - How you’re a big DataCamp fan❗
    - I’ll review their article on sockets
- Reviewed _Multi-Connection Client and Server_ (MC) from RP article
- _Selectors_ wrap and monitor sockets for either _read_, _write_ or _both_ events
  - The _mask_, related to events, requires a bit of bit-twiddling – _i.e._, use a **bit** (😎) of bit level operators, _e.g._,  `AND` (`&`), `OR` (`|`), `NOT` (`~`) …
    - _Selectors_ can wrap any `fileobj`, _e.g._, socket, file, keyboard, pipe …
- Functions are used to manage the _listen_ and _connection_ sockets
  - A sentinel, `data=None`, is used to differentiate between the two
  - The data parameter can hold anything you want, _e.g._, `SimpleNamespace`
- Decided not to move onto _Application and Client Server_ (ACS) until:
  - You gain a better understanding of the MC version
  - We’ll study the ACS code together
- Detailed review of the MC version, w/much discussion on trying to find an analogy, that we both liked, for; socket, port, and host/address
  - Best I stumbled upon is that an address is a room (or apartment building) and the port is a specific seat (or apartment/unit)
  - see if any of these help:
    - [networks - What would be a good analogy for IP addresses and ports? - Computer Science Educators Stack Exchange](https://cseducators.stackexchange.com/questions/1331/what-would-be-a-good-analogy-for-ip-addresses-and-ports)
    - [Socket vs Port - Detailed Explanation and Difference - IP With Ease](https://ipwithease.com/ports-and-socket-explanation/)
    - [Difference between IP Address and Port Number - IP With Ease](https://ipwithease.com/difference-between-ip-address-and-port-number/)
    - [The Difference Between a Port and a Socket | Baeldung on Computer Science](https://www.baeldung.com/cs/port-vs-socket)
    - [Port Numbers and Sockets Explained: Key Networking Concepts](https://www.itms-us.com/Articles/Port-Numbers-And-Sockets-Explained)
    - [TCP/IP Ports and Sockets Explained](http://www.steves-internet-guide.com/tcpip-ports-sockets/)
    - [Understanding sockets concepts - IBM Documentation](https://www.ibm.com/docs/en/zos/3.1.0?topic=concepts-understanding-sockets)
    - [Difference between Socket and Port? - GeeksforGeeks](https://www.geeksforgeeks.org/difference-between-socket-and-port/#)
    - [The OSI Model – The 7 Layers of Networking Explained in Plain English](https://www.freecodecamp.org/news/osi-model-networking-layers-explained-in-plain-english/)
    - [A Complete Guide to Socket Programming in Python | DataCamp](https://www.datacamp.com/tutorial/a-complete-guide-to-socket-programming-in-python)

### 7/29 next

- Continue deep dive into RP code
  - MC C/S - running each, simultaneously, under debugger control
  - Begin review of ACS

Good luck and have fun!

## 7/22

## 7/19

In this week’s lessons, we:

- Discussed job opportunity – very exciting❗
- Reviewed and agreed to our go-forward plan – `C`, `Python`…
- Decided to pair-program socket implementation of `otp` from scratch
  - new repo?
- Introduced [typing](https://docs.python.org/3/library/typing.html),
[fire](https://google.github.io/python-fire/guide/),
[click](https://click.palletsprojects.com/en/8.1.x/), and
[typer](https://typer.tiangolo.com/)  
  - First and last are most relevant to `otp`
  - Need to review dev. env. – extensions, `mypy`, etc.
- Got the Real Python echo client/sever running in your dev. env.
- Began review of Real Python’s Multi-Connection Client and Server

### 7/22 next

- Complete review of Real Python’s [Multi-Connection Client and Server](https://realpython.com/python-sockets/#multi-connection-client-and-server)
  - Understand selectors
- Review dev. env.
- Discuss implementation of `otp` command line using typer

Good luck and have fun!

## 7/15

- In today’s Lesson we laid out a go-forward plan:
  - **Python**:
    - Continue working w/cohort on data structures/algorithm problems
      - Objectives:
        - Continue gaining experience
        - Interview prep
    - Use a structured – order, milestones, deliverables - course for broad exposure
      - Objectives:
        - A recognizable, upload-able certificate
        - A publishable portfolio of projects
    - Complete `otp-python`
      - Objectives:
        - pair-program
          - _let's discuss_
        - client/server
        - publishable
  - **C**:
    - Put review of old e.g., `my_zsh` projects on back-burner
    - Post `otp-python`, new project: `otp`, virus simulation, other?
      - Objectives:
        - _let's discuss_

### 7/15 next

- Use Friday to review status of Python efforts
- Download, configure, build, run, test Real Python’s echo server
- Be prepared to discuss [Real Python’s article up to Multiple… Socket Programming in Python (Guide) – Real Python](https://realpython.com/python-sockets/#multi-connection-client-and-server)
- Refine on go forward plan for `otp-python` before switching to C

Good luck and have fun!

## 6/26

- In the last couple of meetings, we discussed a few _administrivia_ items:
  - Moving apartments👎
  - Splitting our time between `python` and `C`
    - Complete `pyotp`
      - Continuing work w/study group
    - Cleanup `C` projects/repos
  - Post vacation: **Mon.** will be `C` day, **Fri.** will be `python` day
    > Subject to review…will meeting right before and after weekend work?
- Reviewed `my_zsh` usage of [`fork`](https://linux.die.net/man/3/fork), [`exec`](https://linux.die.net/man/3/exec) and [`#pragma`](https://en.cppreference.com/w/c/preprocessor/impl)
- Mentioned:
  - Extension for adding to [`.gitignore`](https://marketplace.visualstudio.com/items?itemName=maciejdems.add-to-gitignore)
  - `getopt`/`C` sample: [getopt-parsing](https://github.com/davegi/getopt-parsing/blob/main/gop.c)
- Given our chat – a few articles on distributed systems:
  - [What is a Distributed System? - GeeksforGeeks](https://www.geeksforgeeks.org/what-is-a-distributed-system/)
  - [Fundamentals of Distributed Systems | Baeldung on Computer Science](https://www.baeldung.com/cs/distributed-systems-guide)
  - [Directory of Azure Cloud Services | Microsoft Azure](https://azure.microsoft.com/en-us/products/)
  - [AWS services by category - Overview of Amazon Web Services](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/amazon-web-services-cloud-platform.html)

## 6/26 next

- Review latter part of: [Socket Programming in Python (Guide) – Real Python](https://realpython.com/python-sockets/)
  - Design protocol for `py_otp`
- Review `my_zsh` - me first and then together

## 6/11

- Discussed job opportunities, _devops_ vs. _development_, scripting, tooling, test, and production code
- Reviewed `dsh` - more specifically `fork()` and `exec()`
- Discussed the challenges, and uncommon sightings in production code, of recursive algorithms:

    > [Understanding Recursion With Examples | Better Programming](https://betterprogramming.pub/understanding-recursion-with-examples-f74606fd6be0)  
    > [Recursion Visualizer](https://www.recursionvisualizer.com/)

- Discussed sockets, the RP article and how we can use this as a base to start from

    > need to define protocol

- Ensure that `pyotp` is done - likely requires one more scrubbing – structure (internal and external), naming, style, dead code, commented out code, _etc._

  > in prep for C/S or other enhancements

## 6/11 next

- Complete review of RP sockets article

## 5/24

- reviewed client/server (c/s) architecture for a networked enabled (over _sockets_) `otp`
- defined _daemons_ as system processes, started when the system starts, run in the background, and have no direct UI
  - UI is often a seperate _client_ application
  - this is the architecture we'll use for `otp`
- `otp` now runs as five seperate applications:
  - `keygen` - client only key generator
  - `encode`/`decode` - client side apps, responsible for command line args, validation, packaging, communication w/transport (_sockets_, files, memory...), I/O...
  - `encode_d`/`decode_d` - server side apps that _listen_ on a supplied port/socket and use a child process to handle requests, over a _communication_ socket
    > how will processes be managed (_e.g._, max 5) - pool, queue, _etc._?
- discussed organizing code along different axis:
  - 6 files: main, keygen, encode, decode, encode_d, decode_d
  - 4 files:  main, keygen, clients, servers (c/s axis)
  - 4 files:  main, keygen, encode, decode (encode/decode axis)
  - _etc._

### 5/24 next

- continue with '5/15 next'

## 5/21

- reviewed the _tri-state_ possibilities of multiple CLAs, _e.g._

  ``` python
  switch(input_file_flag) {
    # flag not specified
    case missing:
      input_file = stdin
    # flag missing value
    case no value:
      input_file = open("default-file.txt")
    # use supplied file name
    default:
      input_file = open(supplied_file_name)
  } 

  ```

### 5/21 next

- see below…

## 5/15

- started by debugging the debugger, _i.e._, passing individual strings (`args`) via `launch.json` vs. a single string:
  - `"a", "b", "c"`  
    vs.
  - `"a b  c"`
- discussed different _types_ of breakpoints (_logpoints_) in `vs code`
  > [logpoints, _etc._](https://code.visualstudio.com/docs/python/python-tutorial#:~:text=Tip%3A%20Use%20Logpoints,Code%20debugging%20article.)
- learned about the _truthiness_ of strings, via interactive `python`:
  > tl;dr...let me know what you think:  
    > [Python's bool() Function: The Safe and Straightforward Way to Convert Strings to Booleans](https://python-code.dev/articles/2565231)

### 5/15 next

- cleanup, refactor, comment, _etc._ `v.current` of `otp` in prep for `v.next`
- decided that `v.next` will be `sockets` based and follow the architecture as documented in the `otp.pdf` doc
- pre-reqs for `v.next` beyond reviewing the `pdf`:
  - [**socket** — Low-level networking interface — Python 3.12.3 documentation](https://docs.python.org/3/library/socket.html)
  - [**logging** — Logging facility for Python — Python 3.12.3 documentation](https://docs.python.org/3/library/logging.html)

    > don't forget to look for other resources, especially those on [**Real Python**](https://realpython.com/)
- let's review `vs code`/`extension`/`python` environments  

good luck and have fun!

## 5/10

- quick discussion on interview/job opportunities
- discussed refactoring _data structures_ (vs. _code_ and _text_), specifically `C` `structs`
  - assuming _good names_ for both _types_ and _fields_, aids in:
    - code structure/maintenance (DRY - Don't Repeat Yourself); reuse existing DS, _e.g._, `typedef struct Coordinate`
    - abstraction; ability to write/read code at different levels/layers/depth of understanding
- reviewed/debugged `argparse` issues:
  - different behavior when run from the _debugger_ vs. _terminal_
    > need to double-check this, and create a simple, repeatable, test-case
  - need better way of displaying `python` DS:
    - there are other ways, but start here and see what you can _figure out_
      - [pprint — Data pretty printer — Python 3.12.3 documentation](https://docs.python.org/3/library/pprint.html)
      - [Prettify Your Data Structures With Pretty Print in Python – Real Python](https://realpython.com/python-pretty-print/)
      - [Welcome! — Pygments](https://pygments.org/)
      - [Syntax Highlighting in python using pygments - Deepan Seeralan](https://www.deepanseeralan.com/tech/syntax-highlighting-code-in-python-using-pygments/)
  - need better understanding of `argparse` _side-effects_, _e.g._, any assumptions made by `argparse`, that would impact _behavior_, such as `--flag` vs. `-f`

### 5/10 next

- debug (`argparse` issues) and complete argument parsing
- good luck and have fun❗

## 5/3

- _embedded struct_ example **was** for you - see below (end of `4/23` notes)
- decided to _pair-program_ next project, in contrast to the _top-down_ approach we've historically used
- independently came to the same conclusion wrt _frustration_:
  - mismatch between the path you were on and the _spec_ (table)
  - good learning experience as this type of mismatched objectives happens all the time in industry between product development teams and:
    - product management
    - quality assurance
    - product support
  > - asking lots of questions - w/people who you've established trust in the past - iteratively/incrementally is, imho, a good way to avoid these snafus
- discussed bug wrt order that parsers are declared which led to..._the grand (parser) refactoring_ based on the idea of multiple parsers, and common args/opts:
  1. declare common args/opts (_e.g._, `-i`, `-o`, _etc._)
     1. parameterized over command specific values (_e.g._, file names - `ct.txt` vs `pt.txt`, name of arg/opt - `in-file`, _etc._)
  2. declare parser for (i.)
  3. declare/execute command (`keygen`, `encode`, `decode`) parser
  4. declare/execute one of three _command specific_ parsers:
     1. based on (inherited?) from (ii.)
     2. declare and add command specific args/opts
  5. execute one command specific parser

> I think that's what we discussed, hypothesized, and agreed to, yes😎?

### 5/3 next

- review the _the grand (parser) refactoring_

## 4/23

- Discussed job interviews, which led to a discussion on possibly working on some sort of scientific software, _e.g._, for inspiration:
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
- I committed to an initial survey of **networking** in Python, and so discussed w/Python devs w/_way_ more Python experience than me or you😎, did a _miniscule_ amount of research, and ended up with:
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

- Implement p1 items from _table_
- Restructure notes as MD or NB and continue to use going forwards

> Thx for keeping current on Venmo  
>
> Good luck and have fun!

## 4/19

- my attempt to _consolidate_ and _capture_ our discussions, Lessons, notes, and LSes - relating to `otp`'s command line arguments/options - in a reviewable/usable format:

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
  - imho, python’s too verbose, and seems to rely on a lot of _tribal myth_ to be a true _pythonista_
  - I never liked that idiomatic `c` required `#define`-s be UPPERCASE, or that `go` uses the case of the first letter of an identifier to determine if it was _public_ or _private_
  - again imho, python takes thing’s to the extreme, w/these types of conventions, _e.g._:
    - [Single and Double Underscores in Python Names](https://realpython.com/python-double-underscore/#:~:text=Python%20developers%20let%20you%20know%20when%20an%20object,use%20within%20the%20containing%20module%2C%20class%2C%20or%20package)
  - once again, imho, I think python will remain relevant for years due to its current popularity and code base
    - I suspect it’ll be replaced for backend/infrastructure components w/a modern `c` replacement like `rust`
    - frontend (_i.e._, some analysis, manipulation and visualization) development will be replaced by low-code/no-code tools
  - python’s rules for inheritance, _etc._ are not as bad as how `c++` has evolved, but, as we discussed:
    - [Inheritance and Composition: A Python OOP Guide](https://realpython.com/inheritance-composition-python/)
  - additionally, features feel like they’re being bolted-on:
    - [typing — Support for type hints](https://docs.python.org/3/library/typing.html)
- we then moved onto examining, discussing, and debugging to explain why your `encode | decode` pipeline was behaving as it was WRT the order that _debug prints_ showed up on the screen:
  - this led to another discussion on standard handles and using `stderr` for error/debug data
  - consider the following pipeline:  
    > `demitri-otp> a | b | c`
    - conceptually, the shell starts `a`, `b`, and `c`, but before it allows them to run, it creates two pipes and attaches:
      - `stdout` of processes to the left of a pipe (_i.e._, `a` and `b`), to the _write_ end of the pipe
      - `stdin` of processes to the right of a pipe (_i.e._, `b` and `c`),to the _read_ end of the pipe
    - yielding the pipeline:
      > `a` → `stdout` → **pipe** → `stdin` → `b` → `stdout` → **pipe** → `stdin` → `c`
  - at this point, which process runs at any point in time is driven by the OS scheduler
  - it also (hopefully😎) shows why/how `demitri` and `demitri first` were printing in the order they were and which process was actually doing the printing
    - that is, your debug output was intermingling w/your (theoretical) cipher-text in your `encode | decode` pipeline
    - the pipes offer (buffering and) synchronization as `read` and `write` will block, if data is unavailable or the pipe is full, respectively
- we concluded w/a quick discussion on alternatives to _debug print_:
  - [Logging HOWTO](https://docs.python.org/3/howto/logging.html)
  - [Debugging in Visual Studio Code](https://code.visualstudio.com/Docs/editor/debugging#_logpoints)

### 4/16 – next

- take a break from `otp` and write a little test program (spike) to experiment w/pipelines
- complete the `otp` command line

good luck and have fun!

## 4/12

- reviewed standard handles (_i.e._, `stdin`, `stdout`, and `stderr`) WRT to both _redirection_ and _piping_, and the roles & resposibilities of:
  - application (process)
  - shell
  - OS
- peeked at `pytest` and discussed/demoed the much deeper UT integration, into VS Code,  compared to munit
  - test explorer
  - run/debug test codelens

### 4/12 next

- complete - production code and unit tests - `./otp` command line, based on discussions, using `argparse`

## 4/5

- discussed _classes_ ('blueprints', 'templates', 'stencils') vs. _objects_, which are _instances_ of a `class`
  - resources (_i.e._, memory) are allocated to _objects_
  - discussed the very close relationship w/`C` `structs`
    - `structs` contain _public_ data and lack any uniquely associated _behavior_
    - _classes_ solve this via _encapsulation_ and special functions - _methods_
    - data and functions that are part of a _class_ are often referred to as _members_ - _i.e._, member data, member functions
- comparing `getopt` to `argparse` - the latter is _way_ more verbose
  - part of the reason is it uses a _declarative_ style
  - but mostly because it does _so_ much more❗
- with that in mind, we dove a bit deeper into `argparse`, including a discussion (and some hinting 😎) WRT sub-parsers

Good luck and have fun!

### 4/5 next

- ensure repo, tooling, debugger, _etc._, are completely setup
- complete argument parsing using `argparse`
