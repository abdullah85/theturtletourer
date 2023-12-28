# About

Explore python's `turtle` library with `tkinter`.

# Installation

You need to install `python3` and `tkinter`. 
Check the [Tk docs](https://tkdocs.com/tutorial/index.html) to check and verify if the latest version is installed.
Then, execute the following

```
  $ cd src
  $ python3 tourtheturtle.py
```

## Issues

If you get an error for `tkinter`

```
$ python3 tourtheturtle.py
     .....
	File "/usr/lib/python3.10/turtle.py", line 107, in <module>
     import tkinter as TK
ModuleNotFoundError: No module named 'tkinter'

```

* https://blog.finxter.com/easy-fix-for-module-not-found-error-tkinter/

### What did not work (on Ubuntu jammy - 22.04)

```
$ pip install tkinter
Defaulting to user installation because normal site-packages is not writeable
ERROR: Could not find a version that satisfies the requirement tkinter (from versions: none)
ERROR: No matching distribution found for tkinter
```

### Solution (that worked for me)

`$ sudo apt-get install python3-tk`

# References

* https://docs.python.org/3/library/turtle.html
  * https://docs.python.org/3/library/turtle.html#turtle-graphics-reference
* https://openbookproject.net/thinkcs/python/english3e/hello_little_turtles.html
* https://en.wikipedia.org/wiki/Turtle_graphics

