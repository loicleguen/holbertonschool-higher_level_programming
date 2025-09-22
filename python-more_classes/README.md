<div align="center"><img src="https://github.com/ksyv/holbertonschool-web_front_end/blob/main/baniere_holberton.png"></div>

# Resources

## Table of Contents :

  - [0. Simple rectangle](#subparagraph0)
  - [1. Real definition of a rectangle](#subparagraph1)
  - [2. Area and Perimeter](#subparagraph2)
  - [3. String representation](#subparagraph3)
  - [4. Eval is magic](#subparagraph4)
  - [5. Detect instance deletion](#subparagraph5)
  - [6. How many instances](#subparagraph6)
  - [7. Change representation](#subparagraph7)
  - [8. Compare rectangles](#subparagraph8)
  - [9. A square is a rectangle](#subparagraph9)
  - [10. Class and instance attributes](#subparagraph10)
  - [11. N queens](#subparagraph11)


## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
* Why Python programming is awesome
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
* What are the special__str__and__repr__methods and how to use them
* What is the difference between__str__and__repr__
* What is a class attribute
* What is the difference between a object attribute and a class attribute
* What is a class method
* What is a static method
* How to dynamically create arbitrary new attributes for existing instances of a class
* How to bind attributes to object and classes
* What is and what does contain__dict__of a class and of an instance of a class
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

## Task
### 0. Simple rectangle <a name='subparagraph0'></a>

Write an empty class <code>Rectangle</code> that defines a rectangle:

* You are not allowed to import any module

```
guillaume@ubuntu:~/$ cat 0-main.py
#!/usr/bin/python3
Rectangle = __import__('0-rectangle').Rectangle

my_rectangle = Rectangle()
print(type(my_rectangle))
print(my_rectangle.__dict__)

guillaume@ubuntu:~/$ ./0-main.py
<class '0-rectangle.Rectangle'>
{}
guillaume@ubuntu:~/$
```

<strong>No test cases needed</strong>

---

### 1. Real definition of a rectangle <a name='subparagraph1'></a>

Write a class <code>Rectangle</code> that defines a rectangle by: (based on <code>0-rectangle.py</code>)

* Private instance attribute: <code>width</code>:


  * property <code>def width(self):</code> to retrieve it
  * property setter <code>def width(self, value):</code> to set it:


    * <code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br/>
    * if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code>
* Private instance attribute: <code>height</code>:


  * property <code>def height(self):</code> to retrieve it
  * property setter <code>def height(self, value):</code> to set it:


    * <code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br/>
    * if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code>
* Instantiation with optional <code>width</code> and <code>height</code>: <code>def __init__(self, width=0, height=0):</code>
* You are not allowed to import any module

```
guillaume@ubuntu:~/$ cat 1-main.py
#!/usr/bin/python3
Rectangle = __import__('1-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(my_rectangle.__dict__)

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle.__dict__)

guillaume@ubuntu:~/$ ./1-main.py
{'_Rectangle__width': 2, '_Rectangle__height': 4}
{'_Rectangle__width': 10, '_Rectangle__height': 3}
guillaume@ubuntu:~/$
```

<strong>No test cases needed</strong>

---

### 2. Area and Perimeter <a name='subparagraph2'></a>

Write a class <code>Rectangle</code> that defines a rectangle by: (based on <code>1-rectangle.py</code>)

* Private instance attribute: <code>width</code>:


  * property <code>def width(self):</code> to retrieve it
  * property setter <code>def width(self, value):</code> to set it:


    * <code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br/>
    * if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code>
* Private instance attribute: <code>height</code>:


  * property <code>def height(self):</code> to retrieve it
  * property setter <code>def height(self, value):</code> to set it:


    * <code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br/>
    * if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code>
* Instantiation with optional <code>width</code> and <code>height</code>: <code>def __init__(self, width=0, height=0):</code>
* Public instance method: <code>def area(self):</code> that returns the rectangle area
* Public instance method: <code>def perimeter(self):</code> that returns the rectangle perimeter:


  * if <code>width</code> or <code>height</code> is equal to <code>0</code>, perimeter is equal to <code>0</code>
* You are not allowed to import any module

```
guillaume@ubuntu:~/$ cat 2-main.py
#!/usr/bin/python3
Rectangle = __import__('2-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

guillaume@ubuntu:~/$ ./2-main.py
Area: 8 - Perimeter: 12
--
Area: 30 - Perimeter: 26
guillaume@ubuntu:~/$
```

<strong>No test cases needed</strong>

---

### 3. String representation <a name='subparagraph3'></a>

Write a class <code>Rectangle</code> that defines a rectangle by: (based on <code>2-rectangle.py</code>)

* Private instance attribute: <code>width</code>:


  * property <code>def width(self):</code> to retrieve it
  * property setter <code>def width(self, value):</code> to set it:


    * <code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br/>
    * if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code>
* Private instance attribute: <code>height</code>:


  * property <code>def height(self):</code> to retrieve it
  * property setter <code>def height(self, value):</code> to set it:


    * <code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br/>
    * if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code>
* Instantiation with optional <code>width</code> and <code>height</code>: <code>def __init__(self, width=0, height=0):</code>
* Public instance method: <code>def area(self):</code> that returns the rectangle area
* Public instance method: <code>def perimeter(self):</code> that returns the rectangle perimeter:


  * if <code>width</code> or <code>height</code> is equal to <code>0</code>, perimeter has to be equal to <code>0</code>
* <code>print()</code> and <code>str()</code> should print the rectangle with the character <code>#</code>: (see example below)


  * if <code>width</code> or <code>height</code> is equal to 0, return an empty string
* You are not allowed to import any module

```
guillaume@ubuntu:~/$ cat 3-main.py
#!/usr/bin/python3
Rectangle = __import__('3-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print(str(my_rectangle))
print(repr(my_rectangle))

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle)
print(repr(my_rectangle))

guillaume@ubuntu:~/$ ./3-main.py
Area: 8 - Perimeter: 12
##
##
##
##
<3-rectangle.Rectangle object at 0x7f92a75a2eb8>
--
##########
##########
##########
<3-rectangle.Rectangle object at 0x7f92a75a2eb8>
guillaume@ubuntu:~/$
```

<strong>Object address can be different</strong>

<strong>No test cases needed</strong>

---

### 4. Eval is magic <a name='subparagraph4'></a>

Write a class <code>Rectangle</code> that defines a rectangle by: (based on <code>3-rectangle.py</code>)

* Private instance attribute: <code>width</code>:


  * property <code>def width(self):</code> to retrieve it
  * property setter <code>def width(self, value):</code> to set it:


    * <code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br/>
    * if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code>
* Private instance attribute: <code>height</code>:


  * property <code>def height(self):</code> to retrieve it
  * property setter <code>def height(self, value):</code> to set it:


    * <code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br/>
    * if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code>
* Instantiation with optional <code>width</code> and <code>height</code>: <code>def __init__(self, width=0, height=0):</code>
* Public instance method: <code>def area(self):</code> that returns the rectangle area
* Public instance method: <code>def perimeter(self):</code> that returns the rectangle perimeter:


  * if <code>width</code> or <code>height</code> is equal to <code>0</code>, perimeter has to be equal to <code>0</code>
* <code>print()</code> and <code>str()</code> should print the rectangle with the character <code>#</code>: (see example below)


  * if <code>width</code> or <code>height</code> is equal to 0, return an empty string
* <code>repr()</code> should return a string representation of the rectangle to be able to recreate a new instance by using <code>eval()</code> (see example below)
* You are not allowed to import any module

```
guillaume@ubuntu:~/$ cat 4-main.py
#!/usr/bin/python3
Rectangle = __import__('4-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(str(my_rectangle))
print("--")
print(my_rectangle)
print("--")
print(repr(my_rectangle))
print("--")
print(hex(id(my_rectangle)))
print("--")

# create new instance based on representation
new_rectangle = eval(repr(my_rectangle))
print(str(new_rectangle))
print("--")
print(new_rectangle)
print("--")
print(repr(new_rectangle))
print("--")
print(hex(id(new_rectangle)))
print("--")

print(new_rectangle is my_rectangle)
print(type(new_rectangle) is type(my_rectangle))

guillaume@ubuntu:~/$ ./4-main.py
##
##
##
##
--
##
##
##
##
--
Rectangle(2, 4)
--
0x7f09ebf7cc88
--
##
##
##
##
--
##
##
##
##
--
Rectangle(2, 4)
--
0x7f09ebf7ccc0
--
False
True
guillaume@ubuntu:~/$
```

<strong>No test cases needed</strong>

---

### 5. Detect instance deletion <a name='subparagraph5'></a>

Write a class <code>Rectangle</code> that defines a rectangle by: (based on <code>4-rectangle.py</code>)

* Private instance attribute: <code>width</code>:


  * property <code>def width(self):</code> to retrieve it
  * property setter <code>def width(self, value):</code> to set it:


    * <code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br/>
    * if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code>
* Private instance attribute: <code>height</code>:


  * property <code>def height(self):</code> to retrieve it
  * property setter <code>def height(self, value):</code> to set it:


    * <code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br/>
    * if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code>
* Instantiation with optional <code>width</code> and <code>height</code>: <code>def __init__(self, width=0, height=0):</code>
* Public instance method: <code>def area(self):</code> that returns the rectangle area
* Public instance method: <code>def perimeter(self):</code> that returns the rectangle perimeter:


  * if <code>width</code> or <code>height</code> is equal to <code>0</code>, perimeter has to be equal to <code>0</code>
* <code>print()</code> and <code>str()</code> should print the rectangle with the character <code>#</code>: 


  * if <code>width</code> or <code>height</code> is equal to 0, return an empty string
* <code>repr()</code> should return a string representation of the rectangle to be able to recreate a new instance by using <code>eval()</code>
* Print the message <code>Bye rectangle...</code> (<code>...</code> being 3 dots not ellipsis) when an instance of <code>Rectangle</code> is deleted
* You are not allowed to import any module

```
guillaume@ubuntu:~/$ cat 5-main.py
#!/usr/bin/python3
Rectangle = __import__('5-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

del my_rectangle

try:
    print(my_rectangle)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

guillaume@ubuntu:~/$ ./5-main.py
Area: 8 - Perimeter: 12
Bye rectangle...
[NameError] name 'my_rectangle' is not defined
guillaume@ubuntu:~/$
```

<strong>No test cases needed</strong>

---

### 6. How many instances <a name='subparagraph6'></a>

Write a class <code>Rectangle</code> that defines a rectangle by: (based on <code>5-rectangle.py</code>)

* Private instance attribute: <code>width</code>:


  * property <code>def width(self):</code> to retrieve it
  * property setter <code>def width(self, value):</code> to set it:


    * <code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br/>
    * if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code>
* Private instance attribute: <code>height</code>:


  * property <code>def height(self):</code> to retrieve it
  * property setter <code>def height(self, value):</code> to set it:


    * <code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br/>
    * if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code>
* Public class attribute <code>number_of_instances</code>:


  * Initialized to <code>0</code>
  * Incremented during each new instance instantiation
  * Decremented during each instance deletion
* Instantiation with optional <code>width</code> and <code>height</code>: <code>def __init__(self, width=0, height=0):</code>
* Public instance method: <code>def area(self):</code> that returns the rectangle area
* Public instance method: <code>def perimeter(self):</code> that returns the rectangle perimeter:


  * if <code>width</code> or <code>height</code> is equal to <code>0</code>, perimeter has to be equal to <code>0</code>
* <code>print()</code> and <code>str()</code> should print the rectangle with the character <code>#</code>: 


  * if <code>width</code> or <code>height</code> is equal to 0, return an empty string
* <code>repr()</code> should return a string representation of the rectangle to be able to recreate a new instance by using <code>eval()</code>
* Print the message <code>Bye rectangle...</code> (<code>...</code> being 3 dots not ellipsis) when an instance of <code>Rectangle</code> is deleted
* You are not allowed to import any module

```
guillaume@ubuntu:~/$ cat 6-main.py
#!/usr/bin/python3
Rectangle = __import__('6-rectangle').Rectangle

my_rectangle_1 = Rectangle(2, 4)
my_rectangle_2 = Rectangle(2, 4)
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
del my_rectangle_1
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
del my_rectangle_2
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))

guillaume@ubuntu:~/$ ./6-main.py
2 instances of Rectangle
Bye rectangle...
1 instances of Rectangle
Bye rectangle...
0 instances of Rectangle
guillaume@ubuntu:~/$
```

<strong>No test cases needed</strong>

---

### 7. Change representation <a name='subparagraph7'></a>

Write a class <code>Rectangle</code> that defines a rectangle by: (based on <code>6-rectangle.py</code>)

* Private instance attribute: <code>width</code>:


  * property <code>def width(self):</code> to retrieve it
  * property setter <code>def width(self, value):</code> to set it:


    * <code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br/>
    * if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code>
* Private instance attribute: <code>height</code>:


  * property <code>def height(self):</code> to retrieve it
  * property setter <code>def height(self, value):</code> to set it:


    * <code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br/>
    * if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code>
* Public class attribute <code>number_of_instances</code>:


  * Initialized to <code>0</code>
  * Incremented during each new instance instantiation
  * Decremented during each instance deletion
* Public class attribute <code>print_symbol</code>:


  * Initialized to <code>#</code>
  * Used as symbol for string representation
  * Can be any type
* Instantiation with optional <code>width</code> and <code>height</code>: <code>def __init__(self, width=0, height=0):</code>
* Public instance method: <code>def area(self):</code> that returns the rectangle area
* Public instance method: <code>def perimeter(self):</code> that returns the rectangle perimeter:


  * if <code>width</code> or <code>height</code> is equal to <code>0</code>, perimeter has to be equal to <code>0</code>
* <code>print()</code> and <code>str()</code> should print the rectangle with the character(s) stored in  <code>print_symbol</code>: 


  * if <code>width</code> or <code>height</code> is equal to 0, return an empty string
* <code>repr()</code> should return a string representation of the rectangle to be able to recreate a new instance by using <code>eval()</code>
* Print the message <code>Bye rectangle...</code> (<code>...</code> being 3 dots not ellipsis) when an instance of <code>Rectangle</code> is deleted
* You are not allowed to import any module

```
guillaume@ubuntu:~/$ cat 7-main.py
#!/usr/bin/python3
Rectangle = __import__('7-rectangle').Rectangle

my_rectangle_1 = Rectangle(8, 4)
print(my_rectangle_1)
print("--")
my_rectangle_1.print_symbol = "&"
print(my_rectangle_1)
print("--")

my_rectangle_2 = Rectangle(2, 1)
print(my_rectangle_2)
print("--")
Rectangle.print_symbol = "C"
print(my_rectangle_2)
print("--")

my_rectangle_3 = Rectangle(7, 3)
print(my_rectangle_3)

print("--")

my_rectangle_3.print_symbol = ["C", "is", "fun!"]
print(my_rectangle_3)

print("--")

guillaume@ubuntu:~/$ ./7-main.py
########
########
########
########
--
&&&&&&&&
&&&&&&&&
&&&&&&&&
&&&&&&&&
--
##
--
CC
--
CCCCCCC
CCCCCCC
CCCCCCC
--
['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']
['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']
['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']
--
Bye rectangle...
Bye rectangle...
Bye rectangle...
guillaume@ubuntu:~/$
```

<strong>No test cases needed</strong>

---

### 8. Compare rectangles <a name='subparagraph8'></a>

Write a class <code>Rectangle</code> that defines a rectangle by: (based on <code>7-rectangle.py</code>)

* Private instance attribute: <code>width</code>:


  * property <code>def width(self):</code> to retrieve it
  * property setter <code>def width(self, value):</code> to set it:


    * <code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br/>
    * if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code>
* Private instance attribute: <code>height</code>:


  * property <code>def height(self):</code> to retrieve it
  * property setter <code>def height(self, value):</code> to set it:


    * <code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br/>
    * if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code>
* Public class attribute <code>number_of_instances</code>:


  * Initialized to <code>0</code>
  * Incremented during each new instance instantiation
  * Decremented during each instance deletion
* Public class attribute <code>print_symbol</code>:


  * Initialized to <code>#</code>
  * Used as symbol for string representation
  * Can be any type
* Instantiation with optional <code>width</code> and <code>height</code>: <code>def __init__(self, width=0, height=0):</code>
* Public instance method: <code>def area(self):</code> that returns the rectangle area
* Public instance method: <code>def perimeter(self):</code> that returns the rectangle perimeter:


  * if <code>width</code> or <code>height</code> is equal to <code>0</code>, perimeter has to be equal to <code>0</code>
* <code>print()</code> and <code>str()</code> should print the rectangle with the character <code>#</code>: 


  * if <code>width</code> or <code>height</code> is equal to 0, return an empty string
* <code>repr()</code> should return a string representation of the rectangle to be able to recreate a new instance by using <code>eval()</code>
* Print the message <code>Bye rectangle...</code> (<code>...</code> being 3 dots not ellipsis) when an instance of <code>Rectangle</code> is deleted
* Static method <code>def bigger_or_equal(rect_1, rect_2):</code> that returns the biggest rectangle based on the area


  * <code>rect_1</code> must be an instance of <code>Rectangle</code>, otherwise raise a <code>TypeError</code> exception with the message <code>rect_1 must be an instance of Rectangle</code><br/>
  * <code>rect_2</code> must be an instance of <code>Rectangle</code>, otherwise raise a <code>TypeError</code> exception with the message <code>rect_2 must be an instance of Rectangle</code><br/>
  * Returns <code>rect_1</code> if both have the same area value
* You are not allowed to import any module

```
guillaume@ubuntu:~/$ cat 8-main.py
#!/usr/bin/python3
Rectangle = __import__('8-rectangle').Rectangle

my_rectangle_1 = Rectangle(8, 4)
my_rectangle_2 = Rectangle(2, 3)

if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
    print("my_rectangle_1 is bigger or equal to my_rectangle_2")
else:
    print("my_rectangle_2 is bigger than my_rectangle_1")


my_rectangle_2.width = 10
my_rectangle_2.height = 5
if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
    print("my_rectangle_1 is bigger or equal to my_rectangle_2")
else:
    print("my_rectangle_2 is bigger than my_rectangle_1")

guillaume@ubuntu:~/$ ./8-main.py
my_rectangle_1 is bigger or equal to my_rectangle_2
my_rectangle_2 is bigger than my_rectangle_1
Bye rectangle...
Bye rectangle...
guillaume@ubuntu:~/$
```

<strong>No test cases needed</strong>

---

### 9. A square is a rectangle <a name='subparagraph9'></a>

Write a class <code>Rectangle</code> that defines a rectangle by: (based on <code>8-rectangle.py</code>)

* Private instance attribute: <code>width</code>:


  * property <code>def width(self):</code> to retrieve it
  * property setter <code>def width(self, value):</code> to set it:


    * <code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br/>
    * if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code>
* Private instance attribute: <code>height</code>:


  * property <code>def height(self):</code> to retrieve it
  * property setter <code>def height(self, value):</code> to set it:


    * <code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br/>
    * if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code>
* Public class attribute <code>number_of_instances</code>:


  * Initialized to <code>0</code>
  * Incremented during each new instance instantiation
  * Decremented during each instance deletion
* Public class attribute <code>print_symbol</code>:


  * Initialized to <code>#</code>
  * Used as symbol for string representation
  * Can be any type
* Instantiation with optional <code>width</code> and <code>height</code>: <code>def __init__(self, width=0, height=0):</code>
* Public instance method: <code>def area(self):</code> that returns the rectangle area
* Public instance method: <code>def perimeter(self):</code> that returns the rectangle perimeter:


  * if <code>width</code> or <code>height</code> is equal to <code>0</code>, perimeter has to be equal to <code>0</code>
* <code>print()</code> and <code>str()</code> should print the rectangle with the character <code>#</code>: 


  * if <code>width</code> or <code>height</code> is equal to 0, return an empty string
* <code>repr()</code> should return a string representation of the rectangle to be able to recreate a new instance by using <code>eval()</code>
* Print the message <code>Bye rectangle...</code> (<code>...</code> being 3 dots not ellipsis) when an instance of <code>Rectangle</code> is deleted
* Static method <code>def bigger_or_equal(rect_1, rect_2):</code> that returns the biggest rectangle based on the area


  * <code>rect_1</code> must be an instance of <code>Rectangle</code>, otherwise raise a <code>TypeError</code> exception with the message <code>rect_1 must be an instance of Rectangle</code><br/>
  * <code>rect_2</code> must be an instance of <code>Rectangle</code>, otherwise raise a <code>TypeError</code> exception with the message <code>rect_2 must be an instance of Rectangle</code><br/>
  * Returns <code>rect_1</code> if both have the same area value
* Class method <code>def square(cls, size=0):</code> that returns a new Rectangle instance with <code>width == height == size</code>
* You are not allowed to import any module

```
guillaume@ubuntu:~/$ cat 9-main.py
#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

my_square = Rectangle.square(5)
print("Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter()))
print(my_square)

guillaume@ubuntu:~/$ ./9-main.py
Area: 25 - Perimeter: 20
#####
#####
#####
#####
#####
Bye rectangle...
guillaume@ubuntu:~/$
```

<strong>No test cases needed</strong>

---

### 10. Class and instance attributes <a name='subparagraph10'></a>

Write a blog post describing how object and class attributes work.

* What’s a class attribute
* What’s an instance attribute
* What are all the ways to create them and what is the Pythonic way of doing it
* What are the differences between class and instance attributes
* What are the advantages and drawbacks of each of them
* How does Python deal with the object and class attributes using the <code>__dict__</code>

Your posts should have examples and at least one picture, at the top. 
Publish your blog post on Medium or LinkedIn, and share it at least on LinkedIn.

When done, please add all urls below (blog post, LinkedIn post, etc.)

Please, remember that these blogs must be written in English to further your technical ability in a variety of settings.

<strong>It is your responsibility to request a review for your blog from a peer before the project’s deadline. If no peers have been reviewed, you should request a review from a TA or staff member.</strong>

---

### 11. N queens <a name='subparagraph11'></a>

<img src="http://www.crestbook.com/files/Judit-photo1_602x433.jpg"/>

The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard.
Write a program that solves the N queens problem.

* Usage: <code>nqueens N</code>

  * If the user called the program with the wrong number of arguments, print <code>Usage: nqueens N</code>, followed by a new line, and exit with the status <code>1</code>
* where N must be an integer greater or equal to <code>4</code>

  * If N is not an integer, print <code>N must be a number</code>, followed by a new line, and exit with the status <code>1</code>
  * If N is smaller than <code>4</code>, print <code>N must be at least 4</code>, followed by a new line, and exit with the status <code>1</code>
* The program should print every possible solution to the problem


  * One solution per line
  * Format: see example
  * You don’t have to print the solutions in a specific order
* You are only allowed to import the <code>sys</code> module

Read: <a href="/rltoken/dDicO6zMBxsIvGh5os96vw" target="_blank" title="Queen">Queen</a>, <a href="/rltoken/6Z2Yy69oesExpZ1-QVnvLw" target="_blank" title="Backtracking">Backtracking</a>

```
julien@ubuntu:~/N Queens$ ./101-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
julien@ubuntu:~/N Queens$ ./101-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
julien@ubuntu:~/N Queens$
```

---


## Authors
loicleguen - [GitHub Profile](https://github.com/loicleguen)
