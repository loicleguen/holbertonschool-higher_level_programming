<div align="center"><img src="https://github.com/ksyv/holbertonschool-web_front_end/blob/main/baniere_holberton.png"></div>

# Resources

## Table of Contents :

  - [0. Safe list printing](#subparagraph0)
  - [1. Safe printing of an integers list](#subparagraph1)
  - [2. Print and count integers](#subparagraph2)
  - [3. Integers division with debug](#subparagraph3)
  - [4. Divide a list](#subparagraph4)
  - [5. Raise exception](#subparagraph5)
  - [6. Raise a message](#subparagraph6)

## Resources
### Read or watch:
* [Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
* [Learn to Program 11 Static & Exception Handling](https://www.youtube.com/watch?v=7vbgD-3s-w4)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
* Why Python programming is awesome
* What’s the difference between errors and exceptions
* What are exceptions and how to use them
* When do we need to use exceptions
* How to correctly handle an exception
* What’s the purpose of catching exceptions
* How to raise a builtin exception
* When do we need to implement a clean-up action after an exception

## Requirements
### General
* Allowed editors:vi,vim,emacs
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All your files should end with a new line
* The first line of all your files should be exactly#!/usr/bin/python3
* AREADME.mdfile, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version 2.7.*)
* All your files must be executable
* The length of your files will be tested usingwc

## Task
### 0. Safe list printing <a name='subparagraph0'></a>

Write a function that prints <code>x</code> elements of a list.

* Prototype: <code>def safe_print_list(my_list=[], x=0):</code>
* <code>my_list</code> can contain any type (integer, string, etc.)
* All elements must be printed on the same line followed by a new line.
* <code>x</code> represents the number of elements to print
* <code>x</code> can be bigger than the length of <code>my_list</code>
* Returns the real number of elements printed
* You have to use <code>try: / except:</code>
* You are not allowed to import any module
* You are not allowed to use <code>len()</code>

```
guillaume@ubuntu:~/$ cat 0-main.py
#!/usr/bin/python3
safe_print_list = __import__('0-safe_print_list').safe_print_list

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))

guillaume@ubuntu:~/$ ./0-main.py
12
nb_print: 2
12345
nb_print: 5
12345
nb_print: 5
guillaume@ubuntu:~/$
```

---

### 1. Safe printing of an integers list <a name='subparagraph1'></a>

Write a function that prints an integer with <code>"{:d}".format()</code>.

* Prototype: <code>def safe_print_integer(value):</code>
* <code>value</code> can be any type (integer, string, etc.)
* The integer should be printed followed by a new line
* Returns <code>True</code> if <code>value</code> has been correctly printed (it means the <code>value</code> is an integer)
* Otherwise, returns <code>False</code>
* You have to use <code>try: / except:</code>
* You have to use <code>"{:d}".format()</code> to print as integer
* You are not allowed to import any module
* You are not allowed to use <code>type()</code>

```
guillaume@ubuntu:~/$ cat 1-main.py
#!/usr/bin/python3
safe_print_integer = __import__('1-safe_print_integer').safe_print_integer

value = 89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = -89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = "School"
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

guillaume@ubuntu:~/$ ./1-main.py
89
-89
School is not an integer
guillaume@ubuntu:~/$
```

---

### 2. Print and count integers <a name='subparagraph2'></a>

Write a function that prints the first <code>x</code> elements of a list and only integers.

* Prototype: <code>def safe_print_list_integers(my_list=[], x=0):</code>
* <code>my_list</code> can contain any type (integer, string, etc.)
* All integers have to be printed on the same line followed by a new line - other type of value in the list must be skipped (in silence).
* <code>x</code> represents the number of elements to access in <code>my_list</code>
* <code>x</code> can be bigger than the length of <code>my_list</code> - if it’s the case, an exception is expected to occur
* Returns the real number of integers printed
* You have to use <code>try: / except:</code>
* You have to use <code>"{:d}".format()</code> to print an integer
* You are not allowed to import any module
* You are not allowed to use <code>len()</code>

```
guillaume@ubuntu:~/$ cat 2-main.py
#!/usr/bin/python3
safe_print_list_integers = \
    __import__('2-safe_print_list_integers').safe_print_list_integers

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list_integers(my_list, 2)
print("nb_print: {:d}".format(nb_print))

my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
nb_print = safe_print_list_integers(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))

guillaume@ubuntu:~/$ ./2-main.py
12
nb_print: 2
12345
nb_print: 5
12345Traceback (most recent call last):
  File "./2-main.py", line 14, in <module>
    nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
  File "//2-safe_print_list_integers.py", line 7, in safe_print_list_integers
    print("{:d}".format(my_list[i]), end="")
IndexError: list index out of range
guillaume@ubuntu:~/$
```

---

### 3. Integers division with debug <a name='subparagraph3'></a>

Write a function that divides 2 integers and prints the result.

* Prototype: <code>def safe_print_division(a, b):</code>
* You can assume that <code>a</code> and <code>b</code> are integers
* The result of the division should print on the <code>finally:</code> section preceded by <code>Inside result:</code>
* Returns the value of the division, otherwise: <code>None</code>
* You have to use <code>try: / except: / finally:</code>
* You have to use <code>"{}".format()</code> to print the result
* You are not allowed to import any module

```
guillaume@ubuntu:~/$ cat 3-main.py
#!/usr/bin/python3
safe_print_division = __import__('3-safe_print_division').safe_print_division

a = 12
b = 2
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

a = 12
b = 0
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

guillaume@ubuntu:~/$ ./3-main.py
Inside result: 6.0
12 / 2 = 6.0
Inside result: None
12 / 0 = None
guillaume@ubuntu:~/$
```

---

### 4. Divide a list <a name='subparagraph4'></a>

Write a function that divides element by element 2 lists.

* Prototype: <code>def list_division(my_list_1, my_list_2, list_length):</code>
* <code>my_list_1</code> and <code>my_list_2</code> can contain any type (integer, string, etc.)
* <code>list_length</code> can be bigger than the length of both lists
* Returns a new list (length = <code>list_length</code>) with all divisions
* If 2 elements can’t be divided, the division result should be equal to <code>0</code>
* If an element is not an integer or float:


  * print: <code>wrong type</code>
* If the division can’t be done (<code>/0</code>):


  * print: <code>division by 0</code>
* If <code>my_list_1</code> or <code>my_list_2</code> is too short


  * print: <code>out of range</code>
* You have to use <code>try: / except: / finally:</code>
* You are not allowed to import any module

```
guillaume@ubuntu:~/$ cat 4-main.py
#!/usr/bin/python3
list_division = __import__('4-list_division').list_division

my_l_1 = [10, 8, 4]
my_l_2 = [2, 4, 4]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)

print("--")

my_l_1 = [10, 8, 4, 4]
my_l_2 = [2, 0, "H", 2, 7]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)

guillaume@ubuntu:~/$ ./4-main.py
[5.0, 2.0, 1.0]
--
division by 0
wrong type
out of range
[5.0, 0, 0, 2.0, 0]
guillaume@ubuntu:~/$
```

---

### 5. Raise exception <a name='subparagraph5'></a>

Write a function that raises a type exception.

* Prototype: <code>def raise_exception():</code>
* You are not allowed to import any module

```
guillaume@ubuntu:~/$ cat 5-main.py
#!/usr/bin/python3
raise_exception = __import__('5-raise_exception').raise_exception

try:
    raise_exception()
except TypeError as te:
    print("Exception raised")

guillaume@ubuntu:~/$ ./5-main.py
Exception raised
guillaume@ubuntu:~/$
```

---

### 6. Raise a message <a name='subparagraph6'></a>

Write a function that raises a name exception with a message.

* Prototype: <code>def raise_exception_msg(message=""):</code>
* You are not allowed to import any module

```
guillaume@ubuntu:~/$ cat 6-main.py
#!/usr/bin/python3
raise_exception_msg = __import__('6-raise_exception_msg').raise_exception_msg

try:
    raise_exception_msg("C is fun")
except NameError as ne:
    print(ne)

guillaume@ubuntu:~/$ ./6-main.py
C is fun
guillaume@ubuntu:~/$
```

---


## Authors
loicleguen - [GitHub Profile](https://github.com/loicleguen)
