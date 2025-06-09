<i>The Quick Python Book. Naomi Ceder. Summary</i>

# 3 The Quick Python overview

# 3.2 Built-in data types</h1>
## 3.2.1 Numbers</h2>

Python's four number types are integers, floats, complex numbers, and Booleans:

- Integers — 1, –3, 42, 355, 888888888888888, –7777777777 (integers aren't limited in size except by available memory)
- Floats — 3.0, 31e12, –6e-4
- Complex numbers — 3 + 2j, –4- 2j, 4.2 + 6.3j
- Booleans — True, False

You can manipulate them by using the arithmetics operators: `+` (addition), `-` (subtraction), `*` (multiplication), `/` (division), `**` (exponentiation), and `%` (modulus).

The following examples use integers:

```python
x = 5 + 2 - 3 * 2
x
1
```
```python
5 / 2
2.5
```
```python
5 // 2
2
```
```python
5 % 2
1
```
```python
2 ** 8
256
```
```python
1000000001 ** 3
1000000003000000003000000001
```

These examples work with floats, which are based on the doubles in C:

```python
x = 4.2 ** 2.4
x
31.318308439069273
```
```python
3.5e30 * 2.77e45
9.695e+75
```
```python
1000000001.0 ** 3
1.000000003e+27
```

These examples use complex numbers:

```python
(3+2j) ** (2+3j)
(0.6817665190890336-2.1207457766159625j)
```
```python
x = (3+2j) * (4+9j)
x
(-6+35j)
```
```python
x.real
-6.0
```
```python
x.imag
35.0
```

Several built-in functions can operate on numbers. There are also the library module `cmath` (whitch contains functions for complex numbers) and the library module `math` (whitch contains functions for the other three types):
```python
round(3.49)
3
```
```python
import math
math.ceil(3.49)
4
```
The following examples use Booleans:
```python
x = False
x
False
```
```python
not x
True
```
```python
y = True * 2
y
2
```

## 3.2.2 Lists

Python has a powerful built-in list type:

```python
[]
[1]
[1, 2, 3, 4, 5, 6, 7, 8, 12]
[1, "two", 3, 4.0, ["a", "b"], (5,6)]
```

A list can be indexed from its front or back. You can also refer to a subsegment, or slice, of a list by using slice notation:

```python
x = ['first', 'second', 'third', 'fourth']
x[0]
'first'
```
```python
x[2]
'third'
```
```python
x[-1]
'fourth'
```
```python
x[-2]
'third'
```
```python
x[1:-1]
['second', 'third']
```
```python
x[0:3]
['first', 'second', 'third']
```
```python
x[-2:-1]
['third']
```
```python
x[:3]
['first', 'second', 'third']
```
```python
x[-2:]
['third', 'fourth']
```
```python
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x[8:9] = []
x
[1, 'two', 3, 4, 5, 6, 7, 8]
```
```python
x[5:7] = [6.0, 6.5, 7.0]
x
[1, 'two', 3, 4, 5, 6.0, 6.5, 7.0, 8]
```
```python
x[5:]
[6.0, 6.5, 7.0, 8]
```

Some built-in functions (`len`, `max`, and `min`), some operators (`in`, `+`, and `*`), the `del` statement, and the list methods (`append`, `count`, `extend`, `index`, `insert`, `pop`, `remove`, `reverse`, and `sort`) operate on lists:

```python
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
len(x)
9
```
```python
[-1, 0] + x
[-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```
```python
x.reverse()
x
[9, 8, 7, 6, 5, 4, 3, 2, 1]
```

## 3.2.3 Tuples

```python
()
(1,)
(1, 2, 3, 4, 5, 6, 7, 8, 12)
(1, "two", 3L, 4.0, ["a", "b"], (5, 6))
```

A list can be converted to a tuple by using the built-in function `tuple()`:

```python
x = [1, 2, 3, 4]
tuple(x)
(1, 2, 3, 4)
```

Conversely, a tuple can be converted to a list by using the built-in function `list()`:

```python
x = (1, 2, 3 , 4)
list(x)
[1, 2, 3, 4]
```
## 3.2.4 Strings

String processing is one of Python's strength. They are many options for delimiting strings:

```python
"A string in double quotes can contain 'single quote' characters."
'A string in single quotes can contain "double quote" characters.'
'''\tA string which starts with a tab; ends with a newline character.\n'''
"""This is a triple double quoted string - triple quoted strings (single
   or double quoted) are only kind that can contain real newlines."""
   
'This is a triple double quoted string - triple quoted strings (single\n   or double quoted) are only kind that can contain real newlines.'
```

Strongs have several methods to work with their contents...
```python
x = "live and     let \t   \tlive"
x.split()
['live', 'and', 'let', 'live']
```
```python
x.replace("    let \t   \tlive", "enjoy life")
'live and enjoy life'
```
The `re` library module also contains functions for working with string:
```python
import re
regexp = re.compile(r"[\t ]+")
'live and let live'
```
The print function outputs strings. Other Python data types can be easily converted to string and formatted:
```python
e = 2.718
x = [1, "two", 3, 4.0, ["a", "b"], (5, 6)]
The constant e is: 2.718 and the list x is: [1, 'two', 3, 4.0, ['a', 'b'], (5, 6)]
```
Objects are automatically converted to string representations for printing #1.
Placing an `f` in front of a string #2 inserts the values of variables or expressions in `{}` into the string.
```python
>>> print(f"the value of e is: {e}")
the value of e is: 2.718
```
## 3.2.5 Dictionaries

Keys must me of immutable type #1, including numbers, string and tuples. Values can be any kind of object, including mutable types such as lists and dictionaries.

```python
>>> x = {1: "one", 2: "two"}
>>> x["first"] = "one"
>>> x[("Delorme", "Ryan", 1995)] = (1, 2, 3)
>>> list(x.key())
[1, 2, 'first', ('Delorme', 'Ryan', 1995)]
```
If you try to access the value of a key thet isn't in the dictionary, a `KeyError` exception is raised. To avoid this error, the dictionary method `get` #2 optionally returns a user-definable value when a key isn't in a dictionary.

```python
x.get(1, "not available")
'one'
x.get(4, "not available")
'not available'
```

## 3.2.6 Sets, frozensets

A set in Python is an unordered collection of objects, used in situations where membership and uniqueness in the set are important. Frozensets are similar to sets, but once created are immutable.

```python
>>> x = set([1, 2, 3, 1, 3, 5])
>>> x
[1, 2, 3, 1, 3, 5]
```
```python
>>> 1 in x
True
```
```python
>>> 4 in x
False
```

## 3.2.7 File objects

A file is accessed through a Python file object:

```python
>>> f = open("myfile", "w")
>>> f.write("First line with necessary newline file\n")
46
>>> f.write("Second line to write to the file\n")
33
>>> f.close()
>>> f = open("myfile", "r")
>>> line1 = f.readline()
>>> line2 = f.readline()
>>> f.close()
>>> print(line1, line2)
First line with necessesary newline character
 Second line to write to the file
```
```python
>>> import os
>>> directory = os.getcwd()
>>> print(directory)
/content
```
```python
>>> filename = os.path.join(directory, "myfile")
>>> print(filename)
First line with necessesary newline character

>>> f.close()
```
