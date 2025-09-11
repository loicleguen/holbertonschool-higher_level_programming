<div align="center"><img src="https://github.com/ksyv/holbertonschool-web_front_end/blob/main/baniere_holberton.png"></div>

# Author’s disclaimer

## Table of Contents :

  - [0. Hello, print](#subparagraph0)
  - [1. Print integer](#subparagraph1)
  - [2. Print float](#subparagraph2)
  - [3. Print string](#subparagraph3)
  - [4. Play with strings](#subparagraph4)
  - [5. Copy - Cut - Paste](#subparagraph5)
  - [6. Create a new sentence](#subparagraph6)
  - [7. Easter Egg](#subparagraph7)

## Resources
### Read or watch:
* [Learn to Program](https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt)
* [Whetting Your Appetite](https://docs.python.org/3/tutorial/appetite.html)
* [Using the Python Interpreter](https://docs.python.org/3/tutorial/interpreter.html)
* [An Informal Introduction to Python](https://docs.python.org/3/tutorial/introduction.html)
* [How To Use String Formatters in Python 3](https://docs.python.org/3/tutorial/introduction.html)
* [Pycodestyle – Style Guide for Python Code](https://pypi.org/project/pycodestyle/)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
* How to use the Python interpreter
* How to print text and variables usingprint
* How to use strings
* What are indexing and slicing in Python
* What is the official Python coding style and how to check your code withpycodestyle

## Requirements
### General
* Allowed editors:vi,vim,emacs
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.*)
* All your files should end with a new line
* The first line of all your files should be exactly#!/usr/bin/python3
* AREADME.mdfile at the root of the repo, containing a description of the repository
* AREADME.mdfile, at the root of the folder ofthisproject, is mandatory
* Your code should use the pycodestyle (version 2.7.*)
* All your files must be executable
* The length of your files will be tested usingwc

## Task
### 0. Hello, print <a name='subparagraph0'></a>

Write a Python script that prints exactly <code>"Programming is like building a multilingual puzzle</code>, followed by a new line.

* Use the function <code>print</code>

```
guillaume@ubuntu:~/py/$ ./2-print.py 
"Programming is like building a multilingual puzzle
guillaume@ubuntu:~/py/$
```

---

### 1. Print integer <a name='subparagraph1'></a>

Complete this <a href="https://github.com/hs-hq/0x00.py/blob/master/3-print_number.py" target="_blank" title="source code">source code</a> in order to print the integer stored in the variable <code>number</code>, followed by <code>Battery street</code>, followed by a new line.

* You can find the source code <a href="https://github.com/hs-hq/0x00.py/blob/master/3-print_number.py" target="_blank" title="here">here</a>
* The output of the script should be:


  * the number, followed by <code>Battery street</code>,
  * followed by a new line
* You are not allowed to cast the variable <code>number</code> into a string
* Your code must be 3 lines long
* You have to use f-strings <a href="/rltoken/dd7bIKsC3_0wb3Np_8URUA" target="_blank" title="tips">tips</a>

```
guillaume@ubuntu:~/py/0x00$ ./3-print_number.py
98 Battery street
guillaume@ubuntu:~/py/0x00$
```

---

### 2. Print float <a name='subparagraph2'></a>

Complete the source code in order to print the float stored in the variable <code>number</code> with a precision of 2 digits.

* You can find the source code <a href="https://github.com/hs-hq/0x00.py/blob/master/4-print_float.py" target="_blank" title="here">here</a>
* The output of the program should be:


  * <code>Float:</code>, followed by the float with only 2 digits
  * followed by a new line
* You are not allowed to cast <code>number</code> to string
* You have to use f-strings

```
guillaume@ubuntu:~/py/0x00$ ./4-print_float.py
Float: 3.14
guillaume@ubuntu:~/py/0x00$
```

---

### 3. Print string <a name='subparagraph3'></a>

Complete this <a href="https://github.com/hs-hq/0x00.py/blob/master/5-print_string.py" target="_blank" title="source code">source code</a> in order to print 3 times a string stored in the variable <code>str</code>, followed by its first 9 characters.

* You can find the source code <a href="https://github.com/hs-hq/0x00.py/blob/master/5-print_string.py" target="_blank" title="here">here</a>
* The output of the program should be:


  * 3 times the value of <code>str</code>
  * followed by a new line
  * followed by the 9 first characters of <code>str</code>
  * followed by a new line
* You are not allowed to use any loops or conditional statement
* Your program should be maximum 5 lines long

```
guillaume@ubuntu:~/py/$ ./5-print_string.py 
Holberton SchoolHolberton SchoolHolberton School
Holberton
guillaume@ubuntu:~/py/$
```

---

### 4. Play with strings <a name='subparagraph4'></a>

Complete this <a href="https://github.com/hs-hq/0x00.py/blob/master/6-concat.py" target="_blank" title="source code">source code</a> to print <code>Welcome to Holberton School!</code>

* You can find the source code <a href="https://github.com/hs-hq/0x00.py/blob/master/6-concat.py" target="_blank" title="here">here</a>
* You are not allowed to use any loops or conditional statements.
* You have to use the variables <code>str1</code> and <code>str2</code> in your new line of code
* Your program should be exactly 5 lines long

```
guillaume@ubuntu:~/py/$ ./6-concat.py
Welcome to Holberton School!
guillaume@ubuntu:~/py/$ wc -l 6-concat.py
5 6-concat.py
guillaume@ubuntu:~/py/$
```

---

### 5. Copy - Cut - Paste <a name='subparagraph5'></a>

Complete this <a href="https://github.com/hs-hq/0x00.py/blob/master/7-edges.py" target="_blank" title="source code">source code</a>

* You can find the source code <a href="https://github.com/hs-hq/0x00.py/blob/master/7-edges.py" target="_blank" title="here">here</a>
* You are not allowed to use any loops or conditional statements
* Your program should be exactly 8 lines long
* <code>word_first_3</code> should contain the first 3 letters of the variable <code>word</code>
* <code>word_last_2</code> should contain the last 2 letters of the variable <code>word</code>
* <code>middle_word</code> should contain the value of the variable <code>word</code> without the first and last letters

```
guillaume@ubuntu:~/py/$ ./7-edges.py
First 3 letters: Hol
Last 2 letters: on
Middle word: olberto
guillaume@ubuntu:~/py/$ wc -l 7-edges.py
8 7-edges.py
guillaume@ubuntu:~/py/$
```

---

### 6. Create a new sentence <a name='subparagraph6'></a>

Complete this <a href="https://github.com/hs-hq/0x00.py/blob/master/8-concat_edges.py" target="_blank" title="source code">source code</a> to print <code>object-oriented programming with Python</code>, followed by a new line.

* You can find the source code <a href="https://github.com/hs-hq/0x00.py/blob/master/8-concat_edges.py" target="_blank" title="here">here</a>
* You are not allowed to use any loops or conditional statements
* Your program should be exactly 5 lines long
* You are not allowed to create new variables
* You are not allowed to use string literals

```
guillaume@ubuntu:~/py/$ ./8-concat_edges.py
object-oriented programming with Python
guillaume@ubuntu:~/py/$ wc -l 8-concat_edges.py
5 8-concat_edges.py
guillaume@ubuntu:~/py/$
```

---

### 7. Easter Egg <a name='subparagraph7'></a>

Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.

* Your script should be maximum 98 characters long (please check with <code>wc -m 9-easter_egg.py</code>)

```
guillaume@ubuntu:~/py/$ ./9-easter_egg.py
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
guillaume@ubuntu:~/py/$
```

---


## Authors
loicleguen - [GitHub Profile](https://github.com/loicleguen)
