<div align="center"><img src="https://github.com/ksyv/holbertonschool-web_front_end/blob/main/baniere_holberton.png"></div>

# Background Context

## Table of Contents :

  - [0. Who am I?](#subparagraph0)
  - [1. Where are you?](#subparagraph1)
  - [2. Right count](#subparagraph2)
  - [3. Right count =](#subparagraph3)
  - [4. Right count =](#subparagraph4)
  - [5. Right count =+](#subparagraph5)
  - [6. Is equal](#subparagraph6)
  - [7. Is the same](#subparagraph7)
  - [8. Is really equal](#subparagraph8)
  - [9. Is really the same](#subparagraph9)
  - [10. And with a list, is it equal](#subparagraph10)
  - [11. And with a list, is it the same](#subparagraph11)
  - [12. And with a list, is it really equal](#subparagraph12)
  - [13. And with a list, is it really the same](#subparagraph13)
  - [14. List append](#subparagraph14)
  - [15. List add](#subparagraph15)
  - [16. Integer incrementation](#subparagraph16)
  - [17. List incrementation](#subparagraph17)
  - [18. List assignation](#subparagraph18)
  - [19. Copy a list object](#subparagraph19)
  - [20. Tuple or not?](#subparagraph20)
  - [21. Tuple or not?](#subparagraph21)
  - [22. Tuple or not?](#subparagraph22)
  - [23. Tuple or not?](#subparagraph23)
  - [24. Who I am?](#subparagraph24)
  - [25. Tuple or not](#subparagraph25)
  - [26. Empty is not empty](#subparagraph26)
  - [27. Still the same?](#subparagraph27)
  - [28. Same or not?](#subparagraph28)
  - [29. Python3: Mutable, Immutable... everything is object!](#subparagraph29)
  - [30. #pythonic](#subparagraph30)
  - [31. Low memory cost](#subparagraph31)
  - [32. int 1/3](#subparagraph32)
  - [33. int 2/3](#subparagraph33)
  - [34. int 3/3](#subparagraph34)
  - [35. Clear strings](#subparagraph35)

## Resources
### Read or watch:
* [9.10. Objects and values](/rltoken/vu0q2rKj3XKGyDoqvx72sA)
* [9.11. Aliasing](/rltoken/MOP1Saf_C2E_eHxKnZggHw)
* [Immutable vs mutable types](/rltoken/vvV3pDEliqja6aAI7XFNiA)
* [Mutation](/rltoken/Xy3ZTgiwzUL_pLlB2rZoJw)
* [9.12. Cloning lists](/rltoken/2tqD3FclxPgvlTC70KQApw)
* [Python tuples: immutable but potentially changing](/rltoken/cEGMM3oDORTvSOgUi7Qnhg)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
* What is an object
* What is the difference between a class and an object or instance
* What is the difference between immutable object and mutable object
* What is a reference
* What is an assignment
* What is an alias
* How to know if two variables are identical
* How to know if two variables are linked to the same object
* How to display the variable identifier (which is the memory address in the CPython implementation)
* What is mutable and immutable
* What are the built-in mutable types
* What are the built-in immutable types
* How does Python pass variables to functions

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
### 0. Who am I? <a name='subparagraph0'></a>

What function would you use to print the type of an object?

Write the name of the function in the file, without <code>()</code>.

---

### 1. Where are you? <a name='subparagraph1'></a>

How do you get the variable identifier (which is the memory address in the CPython implementation)?

Write the name of the function in the file, without <code>()</code>.

---

### 2. Right count <a name='subparagraph2'></a>

In the following code, do <code>a</code> and <code>b</code> point to the same object?
Answer with <code>Yes</code> or <code>No</code>.

```
>>> a = 89
>>> b = 100
```

---

### 3. Right count = <a name='subparagraph3'></a>

In the following code, do <code>a</code> and <code>b</code> point to the same object?
Answer with <code>Yes</code> or <code>No</code>.

```
>>> a = 89
>>> b = 89
```

---

### 4. Right count = <a name='subparagraph4'></a>

In the following code, do <code>a</code> and <code>b</code> point to the same object?
Answer with <code>Yes</code> or <code>No</code>.

```
>>> a = 89
>>> b = a
```

---

### 5. Right count =+ <a name='subparagraph5'></a>

In the following code, do <code>a</code> and <code>b</code> point to the same object?
Answer with <code>Yes</code> or <code>No</code>.

```
>>> a = 89
>>> b = a + 1
```

---

### 6. Is equal <a name='subparagraph6'></a>

What do these 3 lines print?

```
>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2)
```

---

### 7. Is the same <a name='subparagraph7'></a>

What do these 3 lines print?

```
>>> s1 = "Best"
>>> s2 = s1
>>> print(s1 is s2)
```

---

### 8. Is really equal <a name='subparagraph8'></a>

What do these 3 lines print?

```
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 == s2)
```

---

### 9. Is really the same <a name='subparagraph9'></a>

What do these 3 lines print?

```
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 is s2)
```

---

### 10. And with a list, is it equal <a name='subparagraph10'></a>

What do these 3 lines print?

```
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 == l2)
```

---

### 11. And with a list, is it the same <a name='subparagraph11'></a>

What do these 3 lines print?

```
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 is l2)
```

---

### 12. And with a list, is it really equal <a name='subparagraph12'></a>

What do these 3 lines print?

```
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)
```

---

### 13. And with a list, is it really the same <a name='subparagraph13'></a>

What do these 3 lines print?

```
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)
```

---

### 14. List append <a name='subparagraph14'></a>

What does this script print?

```
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)
```

---

### 15. List add <a name='subparagraph15'></a>

What does this script print?

```
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)
```

---

### 16. Integer incrementation <a name='subparagraph16'></a>

What does this script print?

```
def increment(n):
    n += 1

a = 1
increment(a)
print(a)
```

---

### 17. List incrementation <a name='subparagraph17'></a>

What does this script print?

```
def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)
```

---

### 18. List assignation <a name='subparagraph18'></a>

What does this script print?

```
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)
```

---

### 19. Copy a list object <a name='subparagraph19'></a>

Write a function <code>def copy_list(a_list):</code> that returns a <strong>copy</strong> of a list.

* The input list can contain any type of objects
* Your file should be maximum 3-line long (no documentation needed)
* You are not allowed to import any module

```
guillaume@ubuntu:~/$ cat 19-main.py
#!/usr/bin/python3
copy_list = __import__('19-copy_list').copy_list

my_list = [1, 2, 3]
print(my_list)

new_list = copy_list(my_list)

print(my_list)
print(new_list)

print(new_list == my_list)
print(new_list is my_list)

guillaume@ubuntu:~/$ ./19-main.py
[1, 2, 3]
[1, 2, 3]
[1, 2, 3]
True
False
guillaume@ubuntu:~/$ wc -l 19-copy_list.py 
3 19-copy_list.py
guillaume@ubuntu:~/$
```

<strong>No test cases needed</strong>

---

### 20. Tuple or not? <a name='subparagraph20'></a>

```
a = ()
```

Is <code>a</code> a tuple? Answer with <code>Yes</code> or <code>No</code>.

---

### 21. Tuple or not? <a name='subparagraph21'></a>

```
a = (1, 2)
```

Is <code>a</code> a tuple? Answer with <code>Yes</code> or <code>No</code>.

---

### 22. Tuple or not? <a name='subparagraph22'></a>

```
a = (1)
```

Is <code>a</code> a tuple? Answer with <code>Yes</code> or <code>No</code>.

---

### 23. Tuple or not? <a name='subparagraph23'></a>

```
a = (1, )
```

Is <code>a</code> a tuple? Answer with <code>Yes</code> or <code>No</code>.

---

### 24. Who I am? <a name='subparagraph24'></a>

What does this script print?

```
a = (1)
b = (1)
a is b
```

---

### 25. Tuple or not <a name='subparagraph25'></a>

What does this script print?

```
a = (1, 2)
b = (1, 2)
a is b
```

---

### 26. Empty is not empty <a name='subparagraph26'></a>

What does this script print?

```
a = ()
b = ()
a is b
```

---

### 27. Still the same? <a name='subparagraph27'></a>

```
>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)
```

Will the last line of this script print <code>139926795932424</code>? Answer with <code>Yes</code> or <code>No</code>.

---

### 28. Same or not? <a name='subparagraph28'></a>

```
>>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a)
```

Will the last line of this script print <code>139926795932424</code>? Answer with <code>Yes</code> or <code>No</code>.

---

### 29. Python3: Mutable, Immutable... everything is object! <a name='subparagraph29'></a>

Write a blog post about everything you just learned / this project is covering. Your blog post should be articulated this way (one paragraph per item):

* introduction
* id and type
* mutable objects
* immutable objects
* why does it matter and how differently does Python treat mutable and immutable objects
* how arguments are passed to functions and what does that imply for mutable and immutable objects

<em>If you worked on advanced tasks, please also include what you did learn in those tasks in the blog post.</em>

Your posts should have many code/output examples to illustrate what you are explaining, and at least one picture, at the top.
Publish your blog post on Medium or LinkedIn, and share it at least on LinkedIn.

When done, please add all urls below (blog post, LinkedIn post, etc.)

Please, remember that these blogs must be written in English to further your technical ability in a variety of settings.

---

### 30. #pythonic <a name='subparagraph30'></a>

Write a function <code>magic_string()</code> that returns a string “BestSchool” n times the number of the iteration (see code):

* Format: see example
* Your file should be maximum 4-line long (no documentation needed)
* You are not allowed to import any module

```
guillaume@ubuntu:~/$ cat 100-main.py
#!/usr/bin/python3
magic_string = __import__('100-magic_string').magic_string

for i in range(10):
    print(magic_string())

guillaume@ubuntu:~/$ ./100-main.py | cat -e
BestSchool$
BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
guillaume@ubuntu:~/$ wc -l 100-magic_string.py 
4 100-magic_string.py
guillaume@ubuntu:~/$
```

<strong>No test cases needed</strong>

---

### 31. Low memory cost <a name='subparagraph31'></a>

Write a class <code>LockedClass</code> with no class or object attribute, that prevents the user from dynamically creating new instance attributes, except if the new instance attribute is called <code>first_name</code>.

* You are not allowed to import any module

```
guillaume@ubuntu:~/$ cat 101-main.py
#!/usr/bin/python3
LockedClass = __import__('101-locked_class').LockedClass

lc = LockedClass()
lc.first_name = "John"
try:
    lc.last_name = "Snow"
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

guillaume@ubuntu:~/$ ./101-main.py
[AttributeError] 'LockedClass' object has no attribute 'last_name'
guillaume@ubuntu:~/$
```

<strong>No test cases needed</strong>

---

### 32. int 1/3 <a name='subparagraph32'></a>

```
julien@ubuntu:/python3$ cat int.py 
a = 1
b = 1
julien@ubuntu:/python3$
```

Assuming we are using a CPython implementation of Python3 with default options/configuration:

* How many int objects are created by the execution of the first line of the script? (<code>103-line1.txt</code>)
* How many int objects are created by the execution of the second line of the script (<code>103-line2.txt</code>)

---

### 33. int 2/3 <a name='subparagraph33'></a>

```
julien@ubuntu:/python3$ cat int.py 
a = 1024
b = 1024
del a
del b
c = 1024
julien@ubuntu:/python3$
```

Assuming we are using a CPython implementation of Python3 with default options/configuration:

* How many int objects are created by the execution of the first line of the script? (<code>104-line1.txt</code>)
* How many int objects are created by the execution of the second line of the script (<code>104-line2.txt</code>)
* After the execution of line 3, is the int object pointed by <code>a</code> deleted? Answer with <code>Yes</code> or <code>No</code> (<code>104-line3.txt</code>)
* After the execution of line 4, is the int object pointed by <code>b</code> deleted? Answer with <code>Yes</code> or <code>No</code> (<code>104-line4.txt</code>)
* How many int objects are created by the execution of the last line of the script (<code>104-line5.txt</code>)

---

### 34. int 3/3 <a name='subparagraph34'></a>

```
julien@twix:/tmp/so$ cat int.py 
print("I")
print("Love")
print("Python")
julien@ubuntu:/tmp/so$
```

Assuming we are using a CPython implementation of Python3 with default options/configuration:

* Before the execution of line 2 (<code>print("Love")</code>), how many int objects have been created and are still in memory? (<code>105-line1.txt</code>)
* Why? (optional blog post :))

Hint: <code>NSMALLPOSINTS</code>, <code>NSMALLNEGINTS</code>

<img alt="" loading="lazy" src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2020/9/70f9ea0e969dfcc407a7427aba4786d87a920494.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20251126%2Feu-west-3%2Fs3%2Faws4_request&amp;X-Amz-Date=20251126T071740Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=9d646846f28276b1b1cb94eb3092ee7281d72d2ebb68bde8439e788a0c815b0f" style=""/>

---

### 35. Clear strings <a name='subparagraph35'></a>

```
guillaume@ubuntu:/python3$ cat string.py 
a = "SCHL"
b = "SCHL"
del a
del b
c = "SCHL"
guillaume@ubuntu:/python3$
```

Assuming we are using a CPython implementation of Python3 with default options/configuration (For answers with numbers use integers, don’t spell out the word):

* How many string objects are created by the execution of the first line of the script? (<code>106-line1.txt</code>)
* How many string objects are created by the execution of the second line of the script (<code>106-line2.txt</code>)
* After the execution of line 3, is the string object pointed by <code>a</code> deleted? Answer with <code>Yes</code> or <code>No</code> (<code>106-line3.txt</code>)
* After the execution of line 4, is the string object pointed by <code>b</code> deleted? Answer with <code>Yes</code> or <code>No</code> (<code>106-line4.txt</code>)
* How many string objects are created by the execution of the last line of the script (<code>106-line5.txt</code>)

---


## Authors
loicleguen - [GitHub Profile](https://github.com/loicleguen)
