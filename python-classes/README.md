<div align="center"><img src="https://github.com/ksyv/holbertonschool-web_front_end/blob/main/baniere_holberton.png"></div>

# Background Context

## Table of Contents :

  - [0. My first square](#subparagraph0)
  - [1. Square with size](#subparagraph1)
  - [2. Size validation](#subparagraph2)
  - [3. Area of a square](#subparagraph3)
  - [4. Access and update private attribute](#subparagraph4)
  - [5. Printing a square](#subparagraph5)
  - [6. Coordinates of a square](#subparagraph6)
  - [7. Singly linked list](#subparagraph7)
  - [8. Print Square instance](#subparagraph8)
  - [9. Compare 2 squares](#subparagraph9)


## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
* What is OOP
* “first-class everything”
* What is a class
* What is an object and an instance
* What is the difference between a class and an object or instance
* What is an attribute
* What are and how to use public, protected and private attributes
* What isself
* What is a method
* What is the special__init__method and how to use it
* What is Data Abstraction, Data Encapsulation, and Information Hiding
* What is a property
* What is the difference between an attribute and a property in Python
* What is the Pythonic way to write getters and setters in Python
* How to dynamically create arbitrary new attributes for existing instances of a class
* How to bind attributes to object and classes
* What is the__dict__of a class and/or instance of a class and what does it contain
* How does Python find the attributes of an object or class
* How to use thegetattrfunction

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
* All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
* All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
* All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)'andpython3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

## Task
### 0. My first square <a name='subparagraph0'></a>

Write an empty class <code>Square</code> that defines a square:

* You are not allowed to import any module

```
guillaume@ubuntu:~/$ cat 0-main.py
#!/usr/bin/python3
Square = __import__('0-square').Square

my_square = Square()
print(type(my_square))
print(my_square.__dict__)

guillaume@ubuntu:~/$ ./0-main.py
<class '0-square.Square'>
{}
guillaume@ubuntu:~/$
```

---

### 1. Square with size <a name='subparagraph1'></a>

Write a class <code>Square</code> that defines a square by: (based on <code>0-square.py</code>)

* Private instance attribute: <code>size</code>
* Instantiation with <code>size</code> (no type/value verification)
* You are not allowed to import any module

<strong>Why?</strong>

<em>Why <code>size</code> is private attribute?</em>

The size of a square is crucial for a square, many things depend of it (area computation, etc.), so you, as class builder, must control the type and value of this attribute. 
One way to have the control is to keep it privately. 
You will see in next tasks how to get, update and validate the size value.

```
guillaume@ubuntu:~/$ cat 1-main.py
#!/usr/bin/python3
Square = __import__('1-square').Square

my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(my_square.__size)
except Exception as e:
    print(e)

guillaume@ubuntu:~/$ ./1-main.py
<class '1-square.Square'>
{'_Square__size': 3}
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
guillaume@ubuntu:~/$
```

---

### 2. Size validation <a name='subparagraph2'></a>

Write a class <code>Square</code> that defines a square by: (based on <code>1-square.py</code>)

* Private instance attribute: <code>size</code>
* Instantiation with optional <code>size</code>: <code>def __init__(self, size=0):</code>

  * <code>size</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>size must be an integer</code><br/>
  * if <code>size</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>size must be &gt;= 0</code>
* You are not allowed to import any module

```
guillaume@ubuntu:~/$ cat 2-main.py
#!/usr/bin/python3
Square = __import__('2-square').Square

my_square_1 = Square(3)
print(type(my_square_1))
print(my_square_1.__dict__)

my_square_2 = Square()
print(type(my_square_2))
print(my_square_2.__dict__)

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

try:
    my_square_3 = Square("3")
    print(type(my_square_3))
    print(my_square_3.__dict__)
except Exception as e:
    print(e)

try:
    my_square_4 = Square(-89)
    print(type(my_square_4))
    print(my_square_4.__dict__)
except Exception as e:
    print(e)

guillaume@ubuntu:~/$ ./2-main.py
<class '2-square.Square'>
{'_Square__size': 3}
<class '2-square.Square'>
{'_Square__size': 0}
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
size must be an integer
size must be >= 0
guillaume@ubuntu:~/$
```

---

### 3. Area of a square <a name='subparagraph3'></a>

Write a class <code>Square</code> that defines a square by: (based on <code>2-square.py</code>)

* Private instance attribute: <code>size</code>
* Instantiation with optional <code>size</code>: <code>def __init__(self, size=0):</code>

  * <code>size</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>size must be an integer</code><br/>
  * if <code>size</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>size must be &gt;= 0</code>
* Public instance method: <code>def area(self):</code> that returns the current square area
* You are not allowed to import any module

```
guillaume@ubuntu:~/$ cat 3-main.py
#!/usr/bin/python3
Square = __import__('3-square').Square

my_square_1 = Square(3)
print("Area: {}".format(my_square_1.area()))

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

my_square_2 = Square(5)
print("Area: {}".format(my_square_2.area()))

guillaume@ubuntu:~/$ ./3-main.py
Area: 9
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
Area: 25
guillaume@ubuntu:~/$
```

---

### 4. Access and update private attribute <a name='subparagraph4'></a>

Write a class <code>Square</code> that defines a square by: (based on <code>3-square.py</code>)

* Private instance attribute: <code>size</code>:


  * property <code>def size(self):</code> to retrieve it
  * property setter <code>def size(self, value):</code> to set it:


    * <code>size</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>size must be an integer</code><br/>
    * if <code>size</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>size must be &gt;= 0</code>
* Instantiation with optional <code>size</code>: <code>def __init__(self, size=0):</code>
* Public instance method: <code>def area(self):</code> that returns the current square area
* You are not allowed to import any module

<strong>Why?</strong>

<em>Why a getter and setter?</em>

Reminder: <code>size</code> is a private attribute. We did that to make sure we control the type and value. 
Getter and setter methods are not 100% Python, but more OOP. 
With them, you will be able to validate the assignment of a private attribute and also define how getting the attribute value will be available from outside - by copy? by assignment? etc.
Also, adding type/value validation in the setter will centralize the logic, since you will do it in only one place.

```
guillaume@ubuntu:~/$ cat 4-main.py
#!/usr/bin/python3
Square = __import__('4-square').Square

my_square = Square(89)
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

my_square.size = 3
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

try:
    my_square.size = "5 feet"
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))
except Exception as e:
    print(e)

guillaume@ubuntu:~/$ ./4-main.py
Area: 7921 for size: 89
Area: 9 for size: 3
size must be an integer
guillaume@ubuntu:~/$
```

---

### 5. Printing a square <a name='subparagraph5'></a>

Write a class <code>Square</code> that defines a square by: (based on <code>4-square.py</code>)

* Private instance attribute: <code>size</code>:


  * property <code>def size(self):</code> to retrieve it
  * property setter <code>def size(self, value):</code> to set it:


    * <code>size</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>size must be an integer</code><br/>
    * if <code>size</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>size must be &gt;= 0</code>
* Instantiation with optional <code>size</code>: <code>def __init__(self, size=0):</code>
* Public instance method: <code>def area(self):</code> that returns the current square area
* Public instance method: <code>def my_print(self):</code> that prints in stdout the square with the character <code>#</code>:


  * if <code>size</code> is equal to 0, print an empty line
* You are not allowed to import any module

```
guillaume@ubuntu:~/$ cat 5-main.py
#!/usr/bin/python3
Square = __import__('5-square').Square

my_square = Square(3)
my_square.my_print()

print("--")

my_square.size = 10
my_square.my_print()

print("--")

my_square.size = 0
my_square.my_print()

print("--")

guillaume@ubuntu:~/$ ./5-main.py
###
###
###
--
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
--

--
guillaume@ubuntu:~/$
```

---

### 6. Coordinates of a square <a name='subparagraph6'></a>

Write a class <code>Square</code> that defines a square by: (based on <code>5-square.py</code>)

* Private instance attribute: <code>size</code>:


  * property <code>def size(self):</code> to retrieve it
  * property setter <code>def size(self, value):</code> to set it:


    * <code>size</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>size must be an integer</code><br/>
    * if <code>size</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>size must be &gt;= 0</code>
* Private instance attribute: <code>position</code>:


  * property <code>def position(self):</code> to retrieve it
  * property setter <code>def position(self, value):</code> to set it:


    * <code>position</code> must be a tuple of 2 positive integers, otherwise raise a <code>TypeError</code> exception with the message <code>position must be a tuple of 2 positive integers</code><br/>
* Instantiation with optional <code>size</code> and optional <code>position</code>: <code>def __init__(self, size=0, position=(0, 0)):</code>
* Public instance method: <code>def area(self):</code> that returns the current square area
* Public instance method: <code>def my_print(self):</code> that prints in stdout the square with the character <code>#</code>:


  * if <code>size</code> is equal to 0, print an empty line
  * <code>position</code> should be set using space - <strong>Don’t fill lines by spaces</strong> when <code>position[1] &gt; 0</code>
* You are not allowed to import any module

```
guillaume@ubuntu:~/$ cat 6-main.py
#!/usr/bin/python3
Square = __import__('6-square').Square

my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")

guillaume@ubuntu:~/$ ./6-main.py | tr " " "_" | cat -e
###$
###$
###$
--$
$
_###$
_###$
_###$
--$
___###$
___###$
___###$
--$
guillaume@ubuntu:~/$
```

---

### 7. Singly linked list <a name='subparagraph7'></a>

Write a class <code>Node</code> that defines a node of a  <a href="/rltoken/5N2lVauyxCootCs5r_Efbw" target="_blank" title="singly linked list">singly linked list</a>  by:

* Private instance attribute: <code>data</code>:


  * property <code>def data(self):</code> to retrieve it
  * property setter <code>def data(self, value):</code> to set it:


    * <code>data</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>data must be an integer</code><br/>
* Private instance attribute: <code>next_node</code>:


  * property <code>def next_node(self):</code> to retrieve it
  * property setter <code>def next_node(self, value):</code> to set it:


    * <code>next_node</code> can be <code>None</code> or must be a <code>Node</code>, otherwise raise a <code>TypeError</code> exception with the message <code>next_node must be a Node object</code><br/>
* Instantiation with <code>data</code> and <code>next_node</code>: <code>def __init__(self, data, next_node=None):</code>

And, write a class <code>SinglyLinkedList</code> that defines a singly linked list by:

* Private instance attribute: <code>head</code> (no setter or getter)
* Simple instantiation: <code>def __init__(self):</code>
* Should be printable:


  * print the entire list in stdout
  * one node number by line
* Public instance method: <code>def sorted_insert(self, value):</code> that inserts a new <code>Node</code> into the correct sorted position in the list (increasing order)
* You are not allowed to import any module

```
guillaume@ubuntu:~/$ cat 100-main.py
#!/usr/bin/python3
SinglyLinkedList = __import__('100-singly_linked_list').SinglyLinkedList

sll = SinglyLinkedList()
sll.sorted_insert(2)
sll.sorted_insert(5)
sll.sorted_insert(3)
sll.sorted_insert(10)
sll.sorted_insert(1)
sll.sorted_insert(-4)
sll.sorted_insert(-3)
sll.sorted_insert(4)
sll.sorted_insert(5)
sll.sorted_insert(12)
sll.sorted_insert(3)
print(sll)

guillaume@ubuntu:~/$ ./100-main.py
-4
-3
1
2
3
3
4
5
5
10
12
guillaume@ubuntu:~/$
```

---

### 8. Print Square instance <a name='subparagraph8'></a>

Write a class <code>Square</code> that defines a square by: (based on <code>6-square.py</code>)

* Private instance attribute: <code>size</code>:


  * property <code>def size(self):</code> to retrieve it
  * property setter <code>def size(self, value):</code> to set it:


    * <code>size</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>size must be an integer</code><br/>
    * if <code>size</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>size must be &gt;= 0</code>
* Private instance attribute: <code>position</code>:


  * property <code>def position(self):</code> to retrieve it
  * property setter <code>def position(self, value):</code> to set it:


    * <code>position</code> must be a tuple of 2 positive integers, otherwise raise a <code>TypeError</code> exception with the message <code>position must be a tuple of 2 positive integer</code><br/>
* Instantiation with optional <code>size</code> and optional <code>position</code>: <code>def __init__(self, size=0, position=(0, 0)):</code>
* Public instance method: <code>def area(self):</code> that returns the current square area
* Public instance method: <code>def my_print(self):</code> that prints in stdout the square with the character <code>#</code>:


  * if <code>size</code> is equal to 0, print an empty line
  * <code>position</code> should be use by using space
* Printing a <code>Square</code> instance should have the same behavior as <code>my_print()</code>
* You are not allowed to import any module

```
guillaume@ubuntu:~/$ cat 101-main.py
#!/usr/bin/python3
Square = __import__('101-square').Square

my_square = Square(5, (0, 0))
print(my_square)

print("--")

my_square = Square(5, (4, 1))
print(my_square)

guillaume@ubuntu:~/$ ./101-main.py | tr " " "_" | cat -e
#####$
#####$
#####$
#####$
#####$
--$
$
____#####$
____#####$
____#####$
____#####$
____#####$
guillaume@ubuntu:~/$
```

---

### 9. Compare 2 squares <a name='subparagraph9'></a>

Write a class <code>Square</code> that defines a square by: (based on <code>4-square.py</code>)

* Private instance attribute: <code>size</code>:


  * property <code>def size(self):</code> to retrieve it
  * property setter <code>def size(self, value):</code> to set it:


    * <code>size</code> must be a number (float or integer), otherwise raise a <code>TypeError</code> exception with the message <code>size must be a number</code><br/>
    * if <code>size</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>size must be &gt;= 0</code>
* Instantiation with <code>size</code>: <code>def __init__(self, size=0):</code>
* Public instance method: <code>def area(self):</code> that returns the current square area
* <code>Square</code> instance can answer to comparators: <code>==</code>, <code>!=</code>, <code>&gt;</code>, <code>&gt;=</code>, <code>&lt;</code> and <code>&lt;=</code> based on the square area
* You are not allowed to import any module

```
guillaume@ubuntu:~/$ cat 102-main.py
#!/usr/bin/python3
Square = __import__('102-square').Square

s_5 = Square(5)
s_6 = Square(6)

if s_5 < s_6:
    print("Square 5 < Square 6")
if s_5 <= s_6:
    print("Square 5 <= Square 6")
if s_5 == s_6:
    print("Square 5 == Square 6")
if s_5 != s_6:
    print("Square 5 != Square 6")
if s_5 > s_6:
    print("Square 5 > Square 6")
if s_5 >= s_6:
    print("Square 5 >= Square 6")

guillaume@ubuntu:~/$ ./102-main.py
Square 5 < Square 6
Square 5 <= Square 6
Square 5 != Square 6
guillaume@ubuntu:~/$
```

---


## Authors
loicleguen - [GitHub Profile](https://github.com/loicleguen)
