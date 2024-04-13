# notes

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
