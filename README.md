# firepex
A minimal Python + [Fire](https://github.com/google/python-fire) + [PEX](https://github.com/pantsbuild/pex) app. As it sits, you could use it to help you build portable cli tools. All the compiled file needs is a Python environment.

## Getting Started
Clone this repo, cd to repo folder.

> Setup a venv here if you want

Install pex, fire (pip3 for me): `pip3 install pex fire`

##### Quick Test
From the `firepex`'s root, run `fireapp` 'normally': `python3 fireapp`... should print:
```
user@user-pc:~/firepex$ python fireapp
Type:        Example
String form: <__main__.Example object at 0x7f8c6acc94a8>
File:        ~/repos/firepex-github/fireapp/__main__.py
Docstring:   Example for firepex

Usage:       fireapp
             fireapp r-class
             fireapp r-string
```

## Build
run `rollpex`, a quick n' dirty bash script to create a wheel, build the pex file, and chmod +x the resulting pex file.

> run: `./firepex`; should print:

```
user@user-pc:~/firepex$ ./firepex
Type:        Example
String form: <__main__.Example object at 0x7fede8977f28>
Docstring:   Example for firepex

Usage:       firepex
             firepex r-class
             firepex r-string
```

Play around with the cli and check out Fire! It's great!

### More

`./firepex` runs likes a script..

```
user@user-pc:/firepex$ head -n1 firepex
#!/usr/bin/env python3.6
```

In this case, the shell looks for Python 3.6. This means I need Python 3.6 in the deployed environment to run this, but all my dependencies are included.

When you run `./rollpex`, the `#!` is determined from your current python environment OR it can be overridden with a flag in Pex.

Fin.
