# About

To use python turtle library to give clear explanations of various concepts.

# References

* https://docs.python.org/3/library/turtle.html
* https://openbookproject.net/thinkcs/python/english3e/hello_little_turtles.html
* https://en.wikipedia.org/wiki/Turtle_graphics

# Issues

```
$ python3 docTour.py
Traceback (most recent call last):
  File "/home/abdullah/Desktop/tinyturtletours/summation/docTour.py", line 3, in <module>
    import turtle
  File "/usr/lib/python3.10/turtle.py", line 107, in <module>
    import tkinter as TK
ModuleNotFoundError: No module named 'tkinter'

```

* https://blog.finxter.com/easy-fix-for-module-not-found-error-tkinter/

## What did not work (on Ubuntu jammy - 22.04)

```
$ pip install tkinter
Defaulting to user installation because normal site-packages is not writeable
ERROR: Could not find a version that satisfies the requirement tkinter (from versions: none)
ERROR: No matching distribution found for tkinter
```

## Solution (that worked for me)

`$ sudo apt-get install python3-tk`
