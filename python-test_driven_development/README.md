<div align="center"><img src="https://github.com/ksyv/holbertonschool-web_front_end/blob/main/baniere_holberton.png"></div>

# Background Context

## Table of Contents :

  - [0. Integers addition](#subparagraph0)
  - [1. Divide a matrix](#subparagraph1)
  - [2. Say my name](#subparagraph2)
  - [3. Print square](#subparagraph3)
  - [4. Text indentation](#subparagraph4)
  - [5. Max integer - Unittest](#subparagraph5)

## Resources
### Read or watch:
* [doctest — Test interactive Python examples](/rltoken/Hmd_LI8NZ-F2ymDxue5HCg)
* [doctest – Testing through documentation](/rltoken/fbFfGNFU07L2yD0D1uc-Xg)
* [Unit Tests in Python](/rltoken/LhbdUZYzqiP7cjxjE3rG3w)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
* Why Python programming is awesome
* What’s an interactive test
* Why tests are important
* How to write Docstrings to create tests
* How to write documentation for each module and function
* What are the basic option flags to create tests
* How to find edge cases

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
### 0. Integers addition <a name='subparagraph0'></a>

Write a function that adds 2 integers.

* Prototype: <code>def add_integer(a, b=98):</code>
* <code>a</code> and <code>b</code> must be integers or floats, otherwise raise a <code>TypeError</code> exception with the message <code>a must be an integer</code> or <code>b must be an integer</code>
* <code>a</code> and <code>b</code> must be first casted to integers if they are float
* Returns an integer: the addition of <code>a</code> and <code>b</code>
* You are not allowed to import any module

```
guillaume@ubuntu:~/$ cat 0-main.py
#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer

print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer(100.3, -2))
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)

guillaume@ubuntu:~/$ ./0-main.py
3
98
100
98
b must be an integer
a must be an integer
guillaume@ubuntu:~/$ python3 -m doctest -v ./tests/0-add_integer.txt | tail -2
9 passed and 0 failed.
Test passed.
guillaume@ubuntu:~/$ python3 -c 'print(__import__("0-add_integer").__doc__)' | wc -l
5
guillaume@ubuntu:~/$ python3 -c 'print(__import__("0-add_integer").add_integer.__doc__)' | wc -l
3
guillaume@ubuntu:~/$
```

---

### 1. Divide a matrix <a name='subparagraph1'></a>

Write a function that divides all elements of a matrix.

* Prototype: <code>def matrix_divided(matrix, div):</code>
* <code>matrix</code> must be a list of lists of integers or floats, otherwise raise a <code>TypeError</code> exception with the message <code>matrix must be a matrix (list of lists) of integers/floats</code>
* Each row of the <code>matrix</code> must be of the same size, otherwise raise a <code>TypeError</code> exception with the message <code>Each row of the matrix must have the same size</code>
* <code>div</code> must be a number (integer or float), otherwise raise a <code>TypeError</code> exception with the message <code>div must be a number</code>
* <code>div</code> can’t be equal to <code>0</code>, otherwise raise a <code>ZeroDivisionError</code> exception with the message <code>division by zero</code>
* All elements of the matrix should be divided by <code>div</code>, rounded to 2 decimal places
* Returns a new matrix
* You are not allowed to import any module

```
guillaume@ubuntu:~/$ cat 2-main.py
#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
print(matrix)

guillaume@ubuntu:~/$ ./2-main.py
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
[[1, 2, 3], [4, 5, 6]]
guillaume@ubuntu:~/$ python3 -m doctest -v ./tests/2-matrix_divided.txt | tail -2
5 passed and 0 failed.
Test passed.
guillaume@ubuntu:~/$
```

Note: you might have a different number of tests than in the above example. As usual, your tests should cover all possible cases.

---

### 2. Say my name <a name='subparagraph2'></a>

Write a function that prints <code>My name is &lt;first name&gt; &lt;last name&gt;</code>

* Prototype: <code>def say_my_name(first_name, last_name=""):</code>
* <code>first_name</code> and <code>last_name</code> must be strings otherwise, raise a <code>TypeError</code> exception with the message <code>first_name must be a string</code> or <code>last_name must be a string</code>
* You are not allowed to import any module

```
guillaume@ubuntu:~/$ cat 3-main.py
#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name

say_my_name("John", "Smith")
say_my_name("Walter", "White")
say_my_name("Bob")
try:
    say_my_name(12, "White")
except Exception as e:
    print(e)

guillaume@ubuntu:~/$ ./3-main.py | cat -e
My name is John Smith$
My name is Walter White$
My name is Bob $
first_name must be a string$
guillaume@ubuntu:~/$ python3 -m doctest -v ./tests/3-say_my_name.txt | tail -2
5 passed and 0 failed.
Test passed.
guillaume@ubuntu:~/$
```

Note: you might have a different number of tests than in the above example. As usual, your tests should cover all possible cases.

---

### 3. Print square <a name='subparagraph3'></a>

Write a function that prints a square with the character <code>#</code>.

* Prototype: <code>def print_square(size):</code>
* <code>size</code> is the size length of the square
* <code>size</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>size must be an integer</code>
* if <code>size</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>size must be &gt;= 0</code>
* if <code>size</code> is a float and is less than 0, raise a <code>TypeError</code> exception with the message <code>size must be an integer</code>
* You are not allowed to import any module

```
guillaume@ubuntu:~/$ cat 4-main.py
#!/usr/bin/python3
print_square = __import__('4-print_square').print_square

print_square(4)
print("")
print_square(10)
print("")
print_square(0)
print("")
print_square(1)
print("")
try:
    print_square(-1)
except Exception as e:
    print(e)
print("")

guillaume@ubuntu:~/$ ./4-main.py
####
####
####
####

##########
##########
##########
##########
##########
##########
##########
##########
##########
##########


#

size must be >= 0

guillaume@ubuntu:~/$ python3 -m doctest -v ./tests/4-print_square.txt
guillaume@ubuntu:~/$
```

---

### 4. Text indentation <a name='subparagraph4'></a>

Write a function that prints a text with 2 new lines after each of these characters: <code>.</code>, <code>?</code> and <code>:</code>

* Prototype: <code>def text_indentation(text):</code>
* <code>text</code> must be a string, otherwise raise a <code>TypeError</code> exception with the message <code>text must be a string</code>
* There should be no space at the beginning or at the end of each printed line
* You are not allowed to import any module

```
guillaume@ubuntu:~/$ cat 5-main.py
#!/usr/bin/python3
text_indentation = __import__('5-text_indentation').text_indentation

text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
beatiorem! Iam ruinas videres""")

guillaume@ubuntu:~/$ ./5-main.py | cat -e
Lorem ipsum dolor sit amet, consectetur adipiscing elit.$
$
Quonam modo?$
$
Utrum igitur tibi litteram videor an totas paginas commovere?$
$
Non autem hoc:$
$
igitur ne illud quidem.$
$
Fortasse id optimum, sed ubi illud:$
$
Plus semper voluptatis?$
$
Teneo, inquit, finem illi videri nihil dolere.$
$
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum rationi oboediens.$
$
Si id dicis, vicimus.$
$
Inde sermone vario sex illa a Dipylo stadia confecimus.$
$
Sin aliud quid voles, postea.$
$
Quae animi affectio suum cuique tribuens atque hanc, quam dico.$
$
Utinam quidem dicerent alium alio beatiorem! Iam ruinas videresguillaume@ubuntu:~/$
guillaume@ubuntu:~/$ python3 -m doctest -v ./tests/5-text_indentation.txt
guillaume@ubuntu:~/$
```

---

### 5. Max integer - Unittest <a name='subparagraph5'></a>

Since the beginning you have been creating “Interactive tests”. For this exercise, you will add Unittests.

In this task, you will write unittests for the function <code>def max_integer(list=[]):</code>.

* Your test file should be inside a folder <code>tests</code>
* You have to use the <a href="/rltoken/0a3DSCMIMni_V7pgq1myLQ" target="_blank" title="unittest module">unittest module</a>
* Your test file should be python files (extension: <code>.py</code>)
* Your test file should be executed by using this command: <code>python3 -m unittest tests.6-max_integer_test</code>
* All tests you make must be passable by the function below
* We strongly encourage you to work together on test cases, so that you don’t miss any edge case

```
guillaume@ubuntu:~/$ cat 6-max_integer.py
#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result

guillaume@ubuntu:~/$ 
guillaume@ubuntu:~/$ cat 6-main.py
#!/usr/bin/python3
max_integer = __import__('6-max_integer').max_integer

print(max_integer([1, 2, 3, 4]))
print(max_integer([1, 3, 4, 2]))
guillaume@ubuntu:~/$
guillaume@ubuntu:~/$ ./6-main.py
4
4
guillaume@ubuntu:~/$
guillaume@ubuntu:~/$ python3 -m unittest tests.6-max_integer_test 2>&1 | tail -1
OK
guillaume@ubuntu:~/$
guillaume@ubuntu:~/$ head -7 tests/6-max_integer_test.py 
#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
guillaume@ubuntu:~/$
```

---


## Authors
Ksyv - [GitHub Profile](https://github.com/ksyv)
