<div align="center"><img src="https://github.com/ksyv/holbertonschool-web_front_end/blob/main/baniere_holberton.png"></div>

# Resources

## Table of Contents :

  - [0. Import a simple function from a simple file](#subparagraph0)
  - [1. My first toolbox!](#subparagraph1)
  - [2. How to make a script dynamic!](#subparagraph2)
  - [3. Infinite addition](#subparagraph3)
  - [4. Who are you?](#subparagraph4)
  - [5. Everything can be imported](#subparagraph5)
  - [6. Build my own calculator!](#subparagraph6)
  - [7. Easy print](#subparagraph7)
  - [8. ByteCode -> Python #3](#subparagraph8)
  - [9. Fast alphabet](#subparagraph9)

## Resources
### Read or watch:
* [Modules](https://docs.python.org/3/tutorial/modules.html)
* [Command line arguments](https://docs.python.org/3/tutorial/stdlib.html#command-line-arguments)
* [Pycodestyle – Style Guide for Python Code](https://pypi.org/project/pycodestyle/)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
* Why Python programming is awesome
* How to import functions from another file
* How to use imported functions
* How to create a module
* How to use the built-in functiondir()
* How to prevent code in your script from being executed when imported
* How to use command line arguments with your Python programs

## Requirements
### General
* Allowed editors:vi,vim,emacs
* All your files will be interpreted/compiled on Ubuntu 22.04 LTS using python3 (version 3.10.*)
* All your files should end with a new line
* The first line of all your files should be exactly#!/usr/bin/python3
* AREADME.mdfile, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version 2.7.*)
* All your files must be executable
* The length of your files will be tested usingwc

## Task
### 0. Import a simple function from a simple file <a name='subparagraph0'></a>

Write a program that imports the function <code>def add(a, b):</code> from the file <code>add_0.py</code> and prints the result of the addition <code>1 + 2 = 3</code>

* You have to use <code>print</code> function with string format to display integers
* You have to assign:


  * the value <code>1</code> to a variable called <code>a</code>
  * the value <code>2</code> to a variable called <code>b</code>
  * and use those two variables as arguments when calling the functions <code>add</code> and <code>print</code>
* <code>a</code> and <code>b</code> must be defined in 2 different lines: <code>a = 1</code> and another <code>b = 2</code>
* Your program should print: <code>&lt;a value&gt; + &lt;b value&gt; = &lt;add(a, b) value&gt;</code> followed with a new line
* You can only use the word <code>add_0</code> once in your code
* You are not allowed to use <code>*</code> for importing or <code>__import__</code>
* Your code should not be executed when imported - by using <code>__import__</code>, like the example below

```
guillaume@ubuntu:~/$ cat add_0.py
#!/usr/bin/python3
def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return (a + b)

guillaume@ubuntu:~/$ ./0-add.py
1 + 2 = 3
guillaume@ubuntu:~/$ cat 0-import_add.py
__import__("0-add")
guillaume@ubuntu:~/$ python3 0-import_add.py 
guillaume@ubuntu:~/$
```

---

### 1. My first toolbox! <a name='subparagraph1'></a>

Write a program that imports functions from the file <code>calculator_1.py</code>, does some Maths, and prints the result.

* Do not use the function <code>print</code> (with string format to display integers) more than 4 times
* You have to define:


  * the value <code>10</code> to a variable <code>a</code>
  * the value <code>5</code> to a variable <code>b</code>
  * and use those two variables only, as arguments when calling functions (including <code>print</code>)
* <code>a</code> and <code>b</code> must be defined in 2 different lines: <code>a = 10</code> and another <code>b = 5</code>
* Your program should call each of the imported functions. See example below for format
* the word <code>calculator_1</code> should be used only once in your file
* You are not allowed to use <code>*</code> for importing or <code>__import__</code>
* Your code should not be executed when imported

```
guillaume@ubuntu:~/$ cat calculator_1.py
#!/usr/bin/python3
def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return (a + b)


def sub(a, b):
    """My subtraction function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a - b
    """
    return (a - b)


def mul(a, b):
    """My multiplication function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a * b
    """
    return (a * b)


def div(a, b):
    """My division function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a / b
    """
    return int(a / b)

guillaume@ubuntu:~/$ ./1-calculation.py
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2
guillaume@ubuntu:~/$
```

---

### 2. How to make a script dynamic! <a name='subparagraph2'></a>

Write a program that prints the number of and the list of its arguments.

* The output should be:


  * Number of argument(s) followed by <code>argument</code> (if number is one) or <code>arguments</code> (otherwise), followed by
  * <code>:</code> (or <code>.</code> if no arguments were passed) followed by
  * a new line, followed by (if at least one argument),
  * one line per argument:


    * the position of the argument (starting at <code>1</code>) followed by <code>:</code>, followed by the argument value and a new line
* Your code should not be executed when imported
* The number of elements of <code>argv</code> can be retrieved by using: <code>len(argv)</code>
* You do not have to fully understand lists yet, but imagine that <code>argv</code> can be used just like a C array: you can use an index to walk through it. There are other ways (which will be preferred for future project tasks), if you know them you can use them.

```
guillaume@ubuntu:~/$ ./2-args.py 
0 arguments.
guillaume@ubuntu:~/$ ./2-args.py Hello
1 argument:
1: Hello
guillaume@ubuntu:~/$ ./2-args.py Hello Welcome To The Best School
6 arguments:
1: Hello
2: Welcome
3: To
4: The
5: Best
6: School
guillaume@ubuntu:~/$
```

---

### 3. Infinite addition <a name='subparagraph3'></a>

Write a program that prints the result of the addition of all arguments

* The output should be the result of the addition of all arguments, followed by a new line
* You can cast arguments into integers by using <code>int()</code> (you can assume that all arguments can be casted into integers)
* Your code should not be executed when imported

```
guillaume@ubuntu:~/$ ./3-infinite_add.py
0
guillaume@ubuntu:~/$ ./3-infinite_add.py 79 10
89
guillaume@ubuntu:~/$ ./3-infinite_add.py 79 10 -40 -300 89 
-162
guillaume@ubuntu:~/$
```

Last but not least, your program should also handle big numbers. And the good news is: if your program works for the above example, it will work for the following example:

```
guillaume@ubuntu:~/$ ./3-infinite_add.py 1111111111111111111111111111111111111111111111111111111111112222222222222222222222222222222222223435467866765443534434222222254444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555666666666666666666666666666666777777777777777777777777777777888888888888888888888888888888899999999999999999999999990000000000000000000 11111111111111111111111111111111111111111111111111222222222222222222222222222333333333333333333334567788888899999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
11111111111111111111111111111111111111111111111111222222222222222222222222222333333333333333333334568900000011111111111111111111111111111111111111111111111111112222222222222222222222222222222222223435467866765443534434222222254444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555666666666666666666666666666666777777777777777777777777777777888888888888888888888888888888899999999999999999999999989999999999999999999
guillaume@ubuntu:~/$
```

---

### 4. Who are you? <a name='subparagraph4'></a>

Write a program that prints all the names defined by the compiled module <strong>hidden_4.pyc</strong> (please download it locally in your sandbox using <em>curl</em>).

* This task must be done on the sandbox only
* File 4-hidden_discovery.py must be located on the folder /tmp/
* You should print one name per line, in alpha order
* You should print only names that do <strong>not</strong> start with <code>__</code>
* Your code should not be executed when imported

```
guillaume@ubuntu:/tmp$ curl -Lso "hidden_4.pyc" "https://github.com/hs-hq/0x02.py/raw/main/hidden_4.pyc"
guillaume@ubuntu:/tmp$ ./4-hidden_discovery.py | sort
my_secret_santa
print_hidden
print_school
guillaume@ubuntu:/tmp$
```

---

### 5. Everything can be imported <a name='subparagraph5'></a>

Write a program that imports the variable <code>a</code> from the file <code>variable_load_5.py</code> and prints its value.

* You are not allowed to use <code>*</code> for importing or <code>__import__</code>
* Your code should not be executed when imported

```
guillaume@ubuntu:~/$ cat variable_load_5.py
#!/usr/bin/python3
a = 98
"""Simple variable
"""

guillaume@ubuntu:~/$ ./5-variable_load.py
98
guillaume@ubuntu:~/$
```

---

### 6. Build my own calculator! <a name='subparagraph6'></a>

Write a program that imports all functions from the file <code>calculator_1.py</code> and handles basic operations.

* Usage: <code>./100-my_calculator.py a operator b</code>

  * If the number of arguments is not 3, your program has to:


    * print <code>Usage: ./100-my_calculator.py &lt;a&gt; &lt;operator&gt; &lt;b&gt;</code> followed with a new line
    * exit with the value <code>1</code>
  * <code>operator</code> can be: 


    * <code>+</code> for addition
    * <code>-</code> for subtraction
    * <code>*</code> for multiplication
    * <code>/</code> for division
  * If the operator is not one of the above:


    * print <code>Unknown operator. Available operators: +, -, * and /</code> followed with a new line
    * exit with the value <code>1</code>
  * You can cast <code>a</code> and <code>b</code> into integers by using <code>int()</code> (you can assume that all arguments will be castable into integers)
  * The result should be printed like this: <code>&lt;a&gt; &lt;operator&gt; &lt;b&gt; = &lt;result&gt;</code>, followed by a new line
* You are not allowed to use <code>*</code> for importing or <code>__import__</code>
* Your code should not be executed when imported

```
guillaume@ubuntu:~/$ cat calculator_1.py
#!/usr/bin/python3
def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return (a + b)


def sub(a, b):
    """My subtraction function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a - b
    """
    return (a - b)


def mul(a, b):
    """My multiplication function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a * b
    """
    return (a * b)


def div(a, b):
    """My division function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a / b
    """
    return int(a / b)

guillaume@ubuntu:~/$ ./100-my_calculator.py ; echo $?
Usage: ./100-my_calculator.py <a> <operator> <b>
1
guillaume@ubuntu:~/$ ./100-my_calculator.py 3 + 5 ; echo $?
3 + 5 = 8
0
guillaume@ubuntu:~/$ ./100-my_calculator.py 3 H 5 ; echo $?
Unknown operator. Available operators: +, -, * and /
1
guillaume@ubuntu:~/$
```

---

### 7. Easy print <a name='subparagraph7'></a>

Write a program that prints <code>#pythoniscool</code>, followed by a new line, in the standard output.

* Your program should be maximum 2 lines long
* You are not allowed to use <code>print</code> or <code>eval</code> or <code>open</code> or <code>import sys</code> in your file <code>101-easy_print.py</code>

```
guillaume@ubuntu:~/$ ./101-easy_print.py
#pythoniscool
guillaume@ubuntu:~/$
```

---

### 8. ByteCode -> Python #3 <a name='subparagraph8'></a>

Write the Python function <code>def magic_calculation(a, b):</code> that does exactly the same as the following Python bytecode:

```
3           0 LOAD_CONST               1 (0)
              3 LOAD_CONST               2 (('add', 'sub'))
              6 IMPORT_NAME              0 (magic_calculation_102)
              9 IMPORT_FROM              1 (add)
             12 STORE_FAST               2 (add)
             15 IMPORT_FROM              2 (sub)
             18 STORE_FAST               3 (sub)
             21 POP_TOP

  4          22 LOAD_FAST                0 (a)
             25 LOAD_FAST                1 (b)
             28 COMPARE_OP               0 (<)
             31 POP_JUMP_IF_FALSE       94

  5          34 LOAD_FAST                2 (add)
             37 LOAD_FAST                0 (a)
             40 LOAD_FAST                1 (b)
             43 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             46 STORE_FAST               4 (c)

  6          49 SETUP_LOOP              38 (to 90)
             52 LOAD_GLOBAL              3 (range)
             55 LOAD_CONST               3 (4)
             58 LOAD_CONST               4 (6)
             61 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             64 GET_ITER
        >>   65 FOR_ITER                21 (to 89)
             68 STORE_FAST               5 (i)

  7          71 LOAD_FAST                2 (add)
             74 LOAD_FAST                4 (c)
             77 LOAD_FAST                5 (i)
             80 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             83 STORE_FAST               4 (c)
             86 JUMP_ABSOLUTE           65
        >>   89 POP_BLOCK

  8     >>   90 LOAD_FAST                4 (c)
             93 RETURN_VALUE

 10     >>   94 LOAD_FAST                3 (sub)
             97 LOAD_FAST                0 (a)
            100 LOAD_FAST                1 (b)
            103 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
            106 RETURN_VALUE
            107 LOAD_CONST               0 (None)
            110 RETURN_VALUE
```

* Tip: <a href="/rltoken/qSJl9TV1pNZtDtRGJLsiBw" target="_blank" title="Python bytecode">Python bytecode</a>

---

### 9. Fast alphabet <a name='subparagraph9'></a>

Write a program that prints the alphabet in uppercase, followed by a new line.

* Your program should be maximum 3 lines long
* You are not allowed to use:


  * any loops
  * any conditional statements
  * <code>str.join()</code>
  * any string literal
  * any system calls

```
guillaume@ubuntu:~/$ ./103-fast_alphabet.py
ABCDEFGHIJKLMNOPQRSTUVWXYZ
guillaume@ubuntu:~/$ wc -l 103-fast_alphabet.py
3 103-fast_alphabet.py
guillaume@ubuntu:~/$
```

---


## Authors
loicleguen - [GitHub Profile](https://github.com/loicleguen)
