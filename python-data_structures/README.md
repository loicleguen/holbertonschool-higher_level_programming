<div align="center"><img src="https://github.com/ksyv/holbertonschool-web_front_end/blob/main/baniere_holberton.png"></div>

# Resources

## Table of Contents :

  - [0. Print a list of integers](#subparagraph0)
  - [1. Secure access to an element in a list](#subparagraph1)
  - [2. Replace element](#subparagraph2)
  - [3. Print a list of integers... in reverse!](#subparagraph3)
  - [4. Replace in a copy](#subparagraph4)
  - [5. Can you C me now?](#subparagraph5)
  - [6. Lists of lists = Matrix](#subparagraph6)
  - [7. Tuples addition](#subparagraph7)
  - [8. More returns!](#subparagraph8)
  - [9. Find the max](#subparagraph9)
  - [10. Only by 2](#subparagraph10)
  - [11. Delete at](#subparagraph11)
  - [12. Switch](#subparagraph12)

## Resources
### Read or watch:
* [3.1.3. Lists](https://docs.python.org/3/tutorial/introduction.html#lists)
* [Data structures](https://docs.python.org/3/tutorial/datastructures.html)
* [Learn to Program 6 : Lists](https://www.youtube.com/watch?v=A1HUzrvS-Pw)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
* What are lists and how to use them
* What are the differences and similarities between strings and lists
* What are the most common methods of lists and how to use them
* How to use lists as stacks and queues
* What are list comprehensions and how to use them
* What are tuples and how to use them
* When to use tuples versus lists
* What is a sequence
* What is tuple packing
* What is sequence unpacking
* What is thedelstatement and how to use it

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
### 0. Print a list of integers <a name='subparagraph0'></a>

Write a function that prints all integers of a list.

* Prototype: <code>def print_list_integer(my_list=[]):</code>
* Format: one integer per line. See example
* You are not allowed to import any module
* You can assume that the list only contains integers
* You are not allowed to cast integers into strings
* You have to use <code>str.format()</code> to print integers

```
guillaume@ubuntu:~/$ cat 0-main.py
#!/usr/bin/python3
print_list_integer = __import__('0-print_list_integer').print_list_integer

my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)

guillaume@ubuntu:~/$ ./0-main.py
1
2
3
4
5
guillaume@ubuntu:~/$
```

---

### 1. Secure access to an element in a list <a name='subparagraph1'></a>

Write a function that retrieves an element from a list.

* Prototype: <code>def element_at(my_list, idx):</code>
* If <code>idx</code> is negative, the function should return <code>None</code>
* If <code>idx</code> is out of range (> of number of element in <code>my_list</code>), the function should return <code>None</code>
* You are not allowed to import any module
* You are not allowed to use <code>try/except</code>

```
guillaume@ubuntu:~/$ cat 1-main.py
#!/usr/bin/python3
element_at = __import__('1-element_at').element_at

my_list = [1, 2, 3, 4, 5]
idx = 3
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))

guillaume@ubuntu:~/$ ./1-main.py
Element at index 3 is 4
guillaume@ubuntu:~/$
```

---

### 2. Replace element <a name='subparagraph2'></a>

Write a function that replaces an element of a list at a specific position.

* Prototype: <code>def replace_in_list(my_list, idx, element):</code>
* If <code>idx</code> is negative, the function should not modify anything, and returns the original list
* If <code>idx</code> is out of range (> of number of element in <code>my_list</code>), the function should not modify anything, and returns the original list
* You are not allowed to import any module
* You are not allowed to use <code>try/except</code>

```
guillaume@ubuntu:~/$ cat 2-main.py
#!/usr/bin/python3
replace_in_list = __import__('2-replace_in_list').replace_in_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = replace_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)

guillaume@ubuntu:~/$ ./2-main.py
[1, 2, 3, 9, 5]
[1, 2, 3, 9, 5]
guillaume@ubuntu:~/$
```

---

### 3. Print a list of integers... in reverse! <a name='subparagraph3'></a>

Write a function that prints all integers of a list, in reverse order.

* Prototype: <code>def print_reversed_list_integer(my_list=[]):</code>
* Format: one integer per line. See example
* You are not allowed to import any module
* You can assume that the list only contains integers
* You are not allowed to cast integers into strings
* You have to use <code>str.format()</code> to print integers

```
guillaume@ubuntu:~/$ cat 3-main.py
#!/usr/bin/python3
print_reversed_list_integer = __import__('3-print_reversed_list_integer').print_reversed_list_integer

my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)

guillaume@ubuntu:~/$ ./3-main.py
5
4
3
2
1
guillaume@ubuntu:~/$
```

---

### 4. Replace in a copy <a name='subparagraph4'></a>

Write a function that replaces an element in a list at a specific position without modifying the original list.

* Prototype: <code>def new_in_list(my_list, idx, element):</code>
* If <code>idx</code> is negative, the function should return a copy of the original <code>list</code>
* If <code>idx</code> is out of range (> of number of element in <code>my_list</code>), the function should return a copy of the original <code>list</code>
* You are not allowed to import any module
* You are not allowed to use <code>try/except</code>

```
guillaume@ubuntu:~/$ cat 4-main.py
#!/usr/bin/python3
new_in_list = __import__('4-new_in_list').new_in_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = new_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)

guillaume@ubuntu:~/$ ./4-main.py
[1, 2, 3, 9, 5]
[1, 2, 3, 4, 5]
guillaume@ubuntu:~/$
```

---

### 5. Can you C me now? <a name='subparagraph5'></a>

Write a function that removes all characters <code>c</code> and <code>C</code> from a string.

* Prototype: <code>def no_c(my_string):</code>
* The function should return the new string
* You are not allowed to import any module
* You are not allowed to use <code>str.replace()</code>

```
guillaume@ubuntu:~/$ cat 5-main.py
#!/usr/bin/python3
no_c = __import__('5-no_c').no_c

print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))

guillaume@ubuntu:~/$ ./5-main.py
Best Shool
hiago
 is fun!
guillaume@ubuntu:~/$
```

---

### 6. Lists of lists = Matrix <a name='subparagraph6'></a>

Write a function that prints a matrix of integers.

* Prototype: <code>def print_matrix_integer(matrix=[[]]):</code>
* Format: see example
* You are not allowed to import any module
* You can assume that the list only contains integers
* You are not allowed to cast integers into strings
* You have to use <code>str.format()</code> to print integers

```
guillaume@ubuntu:~/$ cat 6-main.py
#!/usr/bin/python3
print_matrix_integer = __import__('6-print_matrix_integer').print_matrix_integer

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()

guillaume@ubuntu:~/$ ./6-main.py | cat -e
1 2 3$
4 5 6$
7 8 9$
--$
$
guillaume@ubuntu:~/$
```

---

### 7. Tuples addition <a name='subparagraph7'></a>

Write a function that adds 2 tuples.

* Prototype: <code>def add_tuple(tuple_a=(), tuple_b=()):</code>
* Returns a tuple with 2 integers:


  * The first element should be the addition of the first element of each argument
  * The second element should be the addition of the second element of each argument
* You are not allowed to import any module
* You can assume that the two tuples will only contain integers
* If a tuple is smaller than 2, use the value <code>0</code> for each missing integer
* If a tuple is bigger than 2, use only the first 2 integers

```
guillaume@ubuntu:~/$ cat 7-main.py
#!/usr/bin/python3
add_tuple = __import__('7-add_tuple').add_tuple

tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))

guillaume@ubuntu:~/$ ./7-main.py
(89, 100)
(2, 89)
(1, 89)
guillaume@ubuntu:~/$
```

---

### 8. More returns! <a name='subparagraph8'></a>

Write a function that returns a tuple with the length of a string and its first character.

* Prototype: <code>def multiple_returns(sentence):</code>
* If the sentence is empty, the first character should be equal to <code>None</code>
* You are not allowed to import any module

```
guillaume@ubuntu:~/$ cat 8-main.py
#!/usr/bin/python3
multiple_returns = __import__('8-multiple_returns').multiple_returns

sentence = "At school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))

guillaume@ubuntu:~/$ ./8-main.py
Length: 22 - First character: A
guillaume@ubuntu:~/$
```

---

### 9. Find the max <a name='subparagraph9'></a>

Write a function that finds the biggest integer of a list.

* Prototype: <code>def max_integer(my_list=[]):</code>
* If the list is empty, return <code>None</code>
* You can assume that the list only contains integers
* You are not allowed to import any module
* You are not allowed to use the builtin <code>max()</code>

```
guillaume@ubuntu:~/$ cat 9-main.py
#!/usr/bin/python3
max_integer = __import__('9-max_integer').max_integer

my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))

guillaume@ubuntu:~/$ ./9-main.py
Max: 90
guillaume@ubuntu:~/$
```

---

### 10. Only by 2 <a name='subparagraph10'></a>

Write a function that finds all multiples of 2 in a list.

* Prototype: <code>def divisible_by_2(my_list=[]):</code>
* Return a new list with <code>True</code> or <code>False</code>, depending on whether the integer at the same position in the original list is a multiple of 2
* The new list should have the same size as the original list
* You are not allowed to import any module

```
guillaume@ubuntu:~/$ cat 10-main.py
#!/usr/bin/python3
divisible_by_2 = __import__('10-divisible_by_2').divisible_by_2

my_list = [0, 1, 2, 3, 4, 5, 6]
list_result = divisible_by_2(my_list)

i = 0
while i < len(list_result):
    print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
    i += 1

guillaume@ubuntu:~/$ ./10-main.py
0 is divisible by 2
1 is not divisible by 2
2 is divisible by 2
3 is not divisible by 2
4 is divisible by 2
5 is not divisible by 2
6 is divisible by 2
guillaume@ubuntu:~/$
```

---

### 11. Delete at <a name='subparagraph11'></a>

Write a function that deletes the item at a specific position in a list.

* Prototype: <code>def delete_at(my_list=[], idx=0):</code>
* If <code>idx</code> is negative or out of range, nothing change (returns the same list)
* You are not allowed to use <code>pop()</code>
* You are not allowed to import any module

```
guillaume@ubuntu:~/$ cat 11-main.py
#!/usr/bin/python3
delete_at = __import__('11-delete_at').delete_at

my_list = [1, 2, 3, 4, 5]
idx = 3
new_list = delete_at(my_list, idx)
print(new_list)
print(my_list)

guillaume@ubuntu:~/$ ./11-main.py
[1, 2, 3, 5]
[1, 2, 3, 5]
guillaume@ubuntu:~/$
```

---

### 12. Switch <a name='subparagraph12'></a>

Complete the source code in order to switch value of <code>a</code> and <code>b</code>

* You can find the source code <a href="/rltoken/9viUCbnIwdfsOPV_UrvIRA" target="_blank" title="here">here</a>
* Your code should be inserted where the comment is (line 4)
* Your program should be exactly 5 lines long

```
guillaume@ubuntu:~/py/$ ./12-switch.py
a=10 - b=89
guillaume@ubuntu:~/py/$ wc -l 12-switch.py
5 12-switch.py
guillaume@ubuntu:~/py/$
```

---


## Authors
loicleguen - [GitHub Profile](https://github.com/loicleguen)
