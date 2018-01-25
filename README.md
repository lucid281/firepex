# firepex
A minimal Python 3 + Fire + PEX app template. Helps bootstrap building Python code into a single, portable, executable binary by providing an app template and a starter script.

> setup a venv if you want, I'm not here to babysit.


## 1: Dependencies
Install Python 3. Tested on 3.6.2

Install pex, fire: `pip3 install pex fire`


## 2: Clone + Notes
Clone this repo; works good as a template.

`setup.py`'s `package` entry must reflect the folder name of your app, in this case: `fireapp/`

`rollpex` must also contain your app and all imports in `fireapp/*`, in this case: `fire` and `fireapp`

##### Quick Test
Run fireapp 'normally': `python3 fireapp`; should print:
```
user@user-pc:~/firepex$ python fireapp
Type:        Maths
String form: <__main__.Maths object at 0x7f98af1186a0>
File:        ~/firepex/fireapp/__main__.py
Docstring:   Example for firepex

Usage:       fireapp
             fireapp add
             fireapp div
```


## 3: Build
run `rollpex`: quick n' dirty bash script to create a wheel, build the pex file, and chmod +x the pex file.
> Creates a ~533kb `firepex` file that you can run: `./firepex`; should print:

```
user@user-pc:~/firepex$ ./firepex
Type:        Maths
String form: <__main__.Maths object at 0x7f89aa3e7ef0>
Docstring:   Example for firepex

Usage:       firepex
             firepex add
             firepex div

```

## 4: Profit
