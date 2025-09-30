<div align="center"><img src="https://github.com/ksyv/holbertonschool-web_front_end/blob/main/baniere_holberton.png"></div>

# Resources

## Table of Contents :

  - [0. Read file](#subparagraph0)
  - [1. Write to a file](#subparagraph1)
  - [2. Append to a file](#subparagraph2)
  - [3. To JSON string](#subparagraph3)
  - [4. From JSON string to Object](#subparagraph4)
  - [5. Save Object to a file](#subparagraph5)
  - [6. Create object from a JSON file](#subparagraph6)
  - [7. Load, add, save](#subparagraph7)
  - [8. Class to JSON](#subparagraph8)
  - [9. Student to JSON](#subparagraph9)
  - [10. Student to JSON with filter](#subparagraph10)
  - [11. Student to disk and reload](#subparagraph11)
  - [12. Pascal's Triangle](#subparagraph12)
  - [13. Search and update](#subparagraph13)
  - [14. Log parsing](#subparagraph14)


## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
* Why Python programming is awesome
* How to open a file
* How to write text in a file
* How to read the full content of a file
* How to read a file line by line
* How to move the cursor in a file
* How to make sure a file is closed after using it
* What is and how to use thewithstatement
* What isJSON
* What is serialization
* What is deserialization
* How to convert a Python data structure to a JSON string
* How to convert a JSON string to a Python data structure
* How to access command line parameters in a Python script

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
### 0. Read file <a name='subparagraph0'></a>

Write a function that reads a text file (<code>UTF8</code>) and prints it to stdout:

* Prototype: <code>def read_file(filename=""):</code>
* You must use the <code>with</code> statement
* You don’t need to manage <code>file permission</code> or <code>file doesn't exist</code> exceptions.
* You are not allowed to import any module

```
guillaume@ubuntu:~/$ cat 0-main.py
#!/usr/bin/python3
read_file = __import__('0-read_file').read_file

read_file("my_file_0.txt")

guillaume@ubuntu:~/$ cat my_file_0.txt
We offer a truly innovative approach to education:
focus on building reliable applications and scalable systems, take on real-world challenges, collaborate with your peers. 

A school every software engineer would have dreamt of!
guillaume@ubuntu:~/$ ./0-main.py
We offer a truly innovative approach to education:
focus on building reliable applications and scalable systems, take on real-world challenges, collaborate with your peers. 

A school every software engineer would have dreamt of!
guillaume@ubuntu:~/$
```

<strong>No test cases needed</strong>

---

### 1. Write to a file <a name='subparagraph1'></a>

Write a function that writes a string to a text file (<code>UTF8</code>) and returns the number of characters written:

* Prototype: <code>def write_file(filename="", text=""):</code>
* You must use the <code>with</code> statement
* You don’t need to manage file permission exceptions.
* Your function should create the file if doesn’t exist.
* Your function should overwrite the content of the file if it already exists.
* You are not allowed to import any module

```
guillaume@ubuntu:~/$ cat 1-main.py
#!/usr/bin/python3
write_file = __import__('1-write_file').write_file

nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
print(nb_characters)

guillaume@ubuntu:~/$ ./1-main.py
24
guillaume@ubuntu:~/$ cat my_first_file.txt
This School is so cool!
guillaume@ubuntu:~/$
```

<strong>No test cases needed</strong>

---

### 2. Append to a file <a name='subparagraph2'></a>

Write a function that appends a string at the end of a text file (<code>UTF8</code>) and returns the number of characters added:

* Prototype: <code>def append_write(filename="", text=""):</code>
* If the file doesn’t exist, it should be created
* You must use the <code>with</code> statement
* You don’t need to manage <code>file permission</code> or <code>file doesn't exist</code> exceptions.
* You are not allowed to import any module

```
guillaume@ubuntu:~/$ cat 2-main.py
#!/usr/bin/python3
append_write = __import__('2-append_write').append_write

nb_characters_added = append_write("file_append.txt", "This School is so cool!\n")
print(nb_characters_added)

guillaume@ubuntu:~/$ cat file_append.txt
cat: file_append.txt: No such file or directory
guillaume@ubuntu:~/$ ./2-main.py
24
guillaume@ubuntu:~/$ cat file_append.txt
This School is so cool!
guillaume@ubuntu:~/$ ./2-main.py
24
guillaume@ubuntu:~/$ cat file_append.txt
This School is so cool!
This School is so cool!
guillaume@ubuntu:~/$
```

<strong>No test cases needed</strong>

---

### 3. To JSON string <a name='subparagraph3'></a>

Write a function that returns the JSON representation of an object (string):

* Prototype: <code>def to_json_string(my_obj):</code>
* You don’t need to manage exceptions if the object can’t be serialized.

```
guillaume@ubuntu:~/$ cat 3-main.py
#!/usr/bin/python3
to_json_string = __import__('3-to_json_string').to_json_string

my_list = [1, 2, 3]
s_my_list = to_json_string(my_list)
print(s_my_list)
print(type(s_my_list))

my_dict = { 
    'id': 12,
    'name': "John",
    'places': [ "San Francisco", "Tokyo" ],
    'is_active': True,
    'info': {
        'age': 36,
        'average': 3.14
    }
}
s_my_dict = to_json_string(my_dict)
print(s_my_dict)
print(type(s_my_dict))

try:
    my_set = { 132, 3 }
    s_my_set = to_json_string(my_set)
    print(s_my_set)
    print(type(s_my_set))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

guillaume@ubuntu:~/$ ./3-main.py
[1, 2, 3]
<class 'str'>
{"id": 12, "name": "John", "places": ["San Francisco", "Tokyo"], "is_active": true, "info": {"age": 36, "average": 3.14}}
<class 'str'>
[TypeError] Object of type set is not JSON serializable
guillaume@ubuntu:~/$
```

<strong>No test cases needed</strong>

---

### 4. From JSON string to Object <a name='subparagraph4'></a>

Write a function that returns an object (Python data structure) represented by a JSON string:

* Prototype: <code>def from_json_string(my_str):</code>
* You don’t need to manage exceptions if the JSON string doesn’t represent an object.

```
guillaume@ubuntu:~/$ cat 4-main.py
#!/usr/bin/python3
from_json_string = __import__('4-from_json_string').from_json_string

s_my_list = "[1, 2, 3]"
my_list = from_json_string(s_my_list)
print(my_list)
print(type(my_list))

s_my_dict = """
{"is_active": true, "info": {"age": 36, "average": 3.14}, 
"id": 12, "name": "John", "places": ["San Francisco", "Tokyo"]}
"""
my_dict = from_json_string(s_my_dict)
print(my_dict)
print(type(my_dict))

try:
    s_my_dict = """
    {"is_active": true, 12 }
    """
    my_dict = from_json_string(s_my_dict)
    print(my_dict)
    print(type(my_dict))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

guillaume@ubuntu:~/$ ./4-main.py
[1, 2, 3]
<class 'list'>
{'id': 12, 'is_active': True, 'name': 'John', 'info': {'age': 36, 'average': 3.14}, 'places': ['San Francisco', 'Tokyo']}
<class 'dict'>
[JSONDecodeError] Expecting property name enclosed in double quotes: line 2 column 25 (char 25)
guillaume@ubuntu:~/$
```

<strong>No test cases needed</strong>

---

### 5. Save Object to a file <a name='subparagraph5'></a>

Write a function that writes an Object to a text file, using a JSON representation:

* Prototype: <code>def save_to_json_file(my_obj, filename):</code>
* You must use the <code>with</code> statement
* You don’t need to manage exceptions if the object can’t be serialized.
* You don’t need to manage file permission exceptions.

```
guillaume@ubuntu:~/$ cat 5-main.py
#!/usr/bin/python3
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "my_list.json"
my_list = [1, 2, 3]
save_to_json_file(my_list, filename)

filename = "my_dict.json"
my_dict = { 
    'id': 12,
    'name': "John",
    'places': [ "San Francisco", "Tokyo" ],
    'is_active': True,
    'info': {
        'age': 36,
        'average': 3.14
    }
}
save_to_json_file(my_dict, filename)

try:
    filename = "my_set.json"
    my_set = { 132, 3 }
    save_to_json_file(my_set, filename)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

guillaume@ubuntu:~/$ ./5-main.py
[TypeError] Object of type set is not JSON serializable
guillaume@ubuntu:~/$ cat my_list.json ; echo ""
[1, 2, 3]
guillaume@ubuntu:~/$ cat my_dict.json ; echo ""
{"name": "John", "places": ["San Francisco", "Tokyo"], "id": 12, "info": {"average": 3.14, "age": 36}, "is_active": true}
guillaume@ubuntu:~/$ cat my_set.json ; echo ""

guillaume@ubuntu:~/$
```

<strong>No test cases needed</strong>

---

### 6. Create object from a JSON file <a name='subparagraph6'></a>

Write a function that creates an Object from a “JSON file”:

* Prototype: <code>def load_from_json_file(filename):</code>
* You must use the <code>with</code> statement
* You don’t need to manage exceptions if the JSON string doesn’t represent an object.
* You don’t need to manage file permissions / exceptions.

```
guillaume@ubuntu:~/$ cat my_fake.json
{"is_active": true, 12 }
guillaume@ubuntu:~/$ cat 6-main.py
#!/usr/bin/python3
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "my_list.json"
my_list = load_from_json_file(filename)
print(my_list)
print(type(my_list))

filename = "my_dict.json"
my_dict = load_from_json_file(filename)
print(my_dict)
print(type(my_dict))

try:
    filename = "my_set_doesnt_exist.json"
    my_set = load_from_json_file(filename)
    print(my_set)
    print(type(my_set))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    filename = "my_fake.json"
    my_fake = load_from_json_file(filename)
    print(my_fake)
    print(type(my_fake))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

guillaume@ubuntu:~/$ cat my_list.json ; echo ""
[1, 2, 3]
guillaume@ubuntu:~/$ cat my_dict.json ; echo ""
{"name": "John", "places": ["San Francisco", "Tokyo"], "id": 12, "info": {"average": 3.14, "age": 36}, "is_active": true}
guillaume@ubuntu:~/$ cat my_fake.json ; echo ""
{"is_active": true, 12 }
guillaume@ubuntu:~/$ ./6-main.py
[1, 2, 3]
<class 'list'>
{'name': 'John', 'info': {'age': 36, 'average': 3.14}, 'id': 12, 'places': ['San Francisco', 'Tokyo'], 'is_active': True}
<class 'dict'>
[FileNotFoundError] [Errno 2] No such file or directory: 'my_set_doesnt_exist.json'
[JSONDecodeError] Expecting property name enclosed in double quotes: line 1 column 21 (char 20)
guillaume@ubuntu:~/$
```

<strong>No test cases needed</strong>

---

### 7. Load, add, save <a name='subparagraph7'></a>

Write a script that adds all arguments to a Python list, and then save them to a file:

* You must use your function <code>save_to_json_file</code> from <code>5-save_to_json_file.py</code>
* You must use your function <code>load_from_json_file</code> from <code>6-load_from_json_file.py</code>
* The list must be saved as a JSON representation in a file named <code>add_item.json</code>
* If the file doesn’t exist, it should be created
* You don’t need to manage file permissions / exceptions.

```
guillaume@ubuntu:~/$ cat add_item.json
cat: add_item.json: No such file or directory
guillaume@ubuntu:~/$ ./7-add_item.py
guillaume@ubuntu:~/$ cat add_item.json ; echo ""
[]
guillaume@ubuntu:~/$ ./7-add_item.py Best School
guillaume@ubuntu:~/$ cat add_item.json ; echo ""
["Best", "School"]
guillaume@ubuntu:~/$ ./7-add_item.py 89 Python C
guillaume@ubuntu:~/$ cat add_item.json ; echo ""
["Best", "School", "89", "Python", "C"]
guillaume@ubuntu:~/$
```

<strong>No test cases needed</strong>

---

### 8. Class to JSON <a name='subparagraph8'></a>

Write a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object:

* Prototype: <code>def class_to_json(obj):</code>
* <code>obj</code> is an instance of a Class
* All attributes of the <code>obj</code> Class are serializable: list, dictionary, string, integer and boolean
* You are not allowed to import any module

```
guillaume@ubuntu:~/$ cat 8-my_class.py 
#!/usr/bin/python3
""" My class module
"""

class MyClass:
    """ My class
    """

    def __init__(self, name):
        self.name = name
        self.number = 0

    def __str__(self):
        return "[MyClass] {} - {:d}".format(self.name, self.number)

guillaume@ubuntu:~/$ cat 8-main.py 
#!/usr/bin/python3
MyClass = __import__('8-my_class').MyClass
class_to_json = __import__('8-class_to_json').class_to_json

m = MyClass("John")
m.number = 89
print(type(m))
print(m)

mj = class_to_json(m)
print(type(mj))
print(mj)

guillaume@ubuntu:~/$ ./8-main.py 
<class '8-my_class.MyClass'>
[MyClass] John - 89
<class 'dict'>
{'name': 'John', 'number': 89}
guillaume@ubuntu:~/$ 
guillaume@ubuntu:~/$ cat 8-my_class_2.py 
#!/usr/bin/python3
""" My class module
"""

class MyClass:
    """ My class
    """

    score = 0

    def __init__(self, name, number = 4):
        self.__name = name
        self.number = number
        self.is_team_red = (self.number % 2) == 0

    def win(self):
        self.score += 1

    def lose(self):
        self.score -= 1

    def __str__(self):
        return "[MyClass] {} - {:d} => {:d}".format(self.__name, self.number, self.score)

guillaume@ubuntu:~/$ cat 8-main_2.py 
#!/usr/bin/python3
MyClass = __import__('8-my_class_2').MyClass
class_to_json = __import__('8-class_to_json').class_to_json

m = MyClass("John")
m.win()
print(type(m))
print(m)

mj = class_to_json(m)
print(type(mj))
print(mj)

guillaume@ubuntu:~/$ ./8-main_2.py 
<class '8-my_class_2.MyClass'>
[MyClass] John - 4 => 1
<class 'dict'>
{'number': 4, '_MyClass__name': 'John', 'is_team_red': True, 'score': 1}
guillaume@ubuntu:~/$
```

<strong>No test cases needed</strong>

---

### 9. Student to JSON <a name='subparagraph9'></a>

Write a class <code>Student</code> that defines a student by:

* Public instance attributes: 


  * <code>first_name</code>
  * <code>last_name</code>
  * <code>age</code>
* Instantiation with <code>first_name</code>, <code>last_name</code> and <code>age</code>: <code>def __init__(self, first_name, last_name, age):</code>
* Public method <code>def to_json(self):</code> that retrieves a dictionary representation of a <code>Student</code> instance (same as <code>8-class_to_json.py</code>)
* You are not allowed to import any module

```
guillaume@ubuntu:~/$ cat 9-main.py 
#!/usr/bin/python3
Student = __import__('9-student').Student

students = [Student("John", "Doe", 23), Student("Bob", "Dylan", 27)]

for student in students:
    j_student = student.to_json()
    print(type(j_student))
    print(j_student['first_name'])
    print(type(j_student['first_name']))
    print(j_student['age'])
    print(type(j_student['age']))

guillaume@ubuntu:~/$ ./9-main.py 
<class 'dict'>
John
<class 'str'>
23
<class 'int'>
<class 'dict'>
Bob
<class 'str'>
27
<class 'int'>
guillaume@ubuntu:~/$
```

<strong>No test cases needed</strong>

---

### 10. Student to JSON with filter <a name='subparagraph10'></a>

Write a class <code>Student</code> that defines a student by: (based on <code>9-student.py</code>)

* Public instance attributes: 


  * <code>first_name</code>
  * <code>last_name</code>
  * <code>age</code>
* Instantiation with <code>first_name</code>, <code>last_name</code> and <code>age</code>: <code>def __init__(self, first_name, last_name, age):</code>
* Public method <code>def to_json(self, attrs=None):</code> that retrieves a dictionary representation of a <code>Student</code> instance (same as <code>8-class_to_json.py</code>):


  * If <code>attrs</code> is a list of strings, only attribute names contained in this list must be retrieved.
  * Otherwise, all attributes must be retrieved
* You are not allowed to import any module

```
guillaume@ubuntu:~/$ cat 10-main.py 
#!/usr/bin/python3
Student = __import__('10-student').Student

student_1 = Student("John", "Doe", 23)
student_2 = Student("Bob", "Dylan", 27)

j_student_1 = student_1.to_json()
j_student_2 = student_2.to_json(['first_name', 'age'])
j_student_3 = student_2.to_json(['middle_name', 'age'])

print(j_student_1)
print(j_student_2)
print(j_student_3)

guillaume@ubuntu:~/$ ./10-main.py 
{'age': 23, 'last_name': 'Doe', 'first_name': 'John'}
{'age': 27, 'first_name': 'Bob'}
{'age': 27}
guillaume@ubuntu:~/$
```

<strong>No test cases needed</strong>

---

### 11. Student to disk and reload <a name='subparagraph11'></a>

Write a class <code>Student</code> that defines a student by: (based on <code>10-student.py</code>)

* Public instance attributes: 


  * <code>first_name</code>
  * <code>last_name</code>
  * <code>age</code>
* Instantiation with <code>first_name</code>, <code>last_name</code> and <code>age</code>: <code>def __init__(self, first_name, last_name, age):</code>
* Public method <code>def to_json(self, attrs=None):</code> that retrieves a dictionary representation of a <code>Student</code> instance (same as <code>8-class_to_json.py</code>):


  * If <code>attrs</code> is a list of strings, only attributes name contain in this list must be retrieved.
  * Otherwise, all attributes must be retrieved
* Public method <code>def reload_from_json(self, json):</code> that replaces all attributes of the <code>Student</code> instance:


  * You can assume <code>json</code> will always be a dictionary
  * A dictionary key will be the public attribute name
  * A dictionary value will be the value of the public attribute
* You are not allowed to import any module

Now, you have a simple implementation of a serialization and deserialization mechanism (concept of representation of an object to another format, without losing any information and allow us to rebuild an object based on this representation)

```
guillaume@ubuntu:~/$ cat 11-main.py 
#!/usr/bin/python3
import os
import sys

Student = __import__('11-student').Student
read_file = __import__('0-read_file').read_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

path = sys.argv[1]

if os.path.exists(path):
    os.remove(path)

student_1 = Student("John", "Doe", 23)
j_student_1 = student_1.to_json()
print("Initial student:")
print(student_1)
print(type(student_1))
print(type(j_student_1))
print("{} {} {}".format(student_1.first_name, student_1.last_name, student_1.age))


save_to_json_file(j_student_1, path)
read_file(path)
print("\nSaved to disk")


print("Fake student:")
new_student_1 = Student("Fake", "Fake", 89)
print(new_student_1)
print(type(new_student_1))
print("{} {} {}".format(new_student_1.first_name, new_student_1.last_name, new_student_1.age))


print("Load dictionary from file:")
new_j_student_1 = load_from_json_file(path)

new_student_1.reload_from_json(j_student_1)
print(new_student_1)
print(type(new_student_1))
print("{} {} {}".format(new_student_1.first_name, new_student_1.last_name, new_student_1.age))

guillaume@ubuntu:~/$ ./11-main.py student.json
Initial student:
<11-student.Student object at 0x7f832826eda0>
<class '11-student.Student'>
<class 'dict'>
John Doe 23
{"last_name": "Doe", "first_name": "John", "age": 23}
Saved to disk
Fake student:
<11-student.Student object at 0x7f832826edd8>
<class '11-student.Student'>
Fake Fake 89
Load dictionary from file:
<11-student.Student object at 0x7f832826edd8>
<class '11-student.Student'>
John Doe 23
guillaume@ubuntu:~/$ cat student.json ; echo ""
{"last_name": "Doe", "first_name": "John", "age": 23}
guillaume@ubuntu:~/$
```

<strong>No test cases needed</strong>

---

### 12. Pascal's Triangle <a name='subparagraph12'></a>

<strong>Technical interview preparation</strong>:

* You are not allowed to google anything
* Whiteboard first

Create a function <code>def pascal_triangle(n):</code> that returns a list of lists of integers representing the Pascal’s triangle of <code>n</code>:

* Returns an empty list if <code>n &lt;= 0</code>
* You can assume <code>n</code> will be always an integer
* You are not allowed to import any module

```
guillaume@ubuntu:~/$ cat 12-main.py
#!/usr/bin/python3
"""
12-main
"""
pascal_triangle = __import__('12-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))

guillaume@ubuntu:~/$ 
guillaume@ubuntu:~/$ ./12-main.py
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
guillaume@ubuntu:~/$
```

---

### 13. Search and update <a name='subparagraph13'></a>

Write a function that inserts a line of text to a file, after each line containing a specific string (see example):

* Prototype: <code>def append_after(filename="", search_string="", new_string=""):</code>
* You must use the <code>with</code> statement
* You don’t need to manage <code>file permission</code> or <code>file doesn't exist</code> exceptions.
* You are not allowed to import any module

```
guillaume@ubuntu:~/$ cat 100-main.py
#!/usr/bin/python3
append_after = __import__('100-append_after').append_after

append_after("append_after_100.txt", "Python", "\"C is fun!\"\n")

guillaume@ubuntu:~/$ cat append_after_100.txt
At School,
Python is really important,
But it can be very hard if:
- You don't get all Pythonic tricks
- You don't have strong C knowledge.
guillaume@ubuntu:~/$ ./100-main.py
guillaume@ubuntu:~/$ cat append_after_100.txt
At School,
Python is really important,
"C is fun!"
But it can be very hard if:
- You don't get all Pythonic tricks
"C is fun!"
- You don't have strong C knowledge.
guillaume@ubuntu:~/$ ./100-main.py
guillaume@ubuntu:~/$ cat append_after_100.txt
At School,
Python is really important,
"C is fun!"
"C is fun!"
But it can be very hard if:
- You don't get all Pythonic tricks
"C is fun!"
"C is fun!"
- You don't have strong C knowledge.
guillaume@ubuntu:~/$
```

<strong>No test cases needed</strong>

---

### 14. Log parsing <a name='subparagraph14'></a>

Write a script that reads <code>stdin</code> line by line and computes metrics:

* Input format: <code>&lt;IP Address&gt; - [&lt;date&gt;] "GET /projects/260 HTTP/1.1" &lt;status code&gt; &lt;file size&gt;</code>
* Each 10 lines and after a keyboard interruption (<code>CTRL + C</code>), prints those statistics since the beginning:


  * Total file size: <code>File size: &lt;total size&gt;</code>
  * where <total size=""> is the sum of all previous <file size=""> (see input format above)</file></total>
  * Number of lines by status code: 


    * possible status code: <code>200</code>, <code>301</code>, <code>400</code>, <code>401</code>, <code>403</code>, <code>404</code>, <code>405</code> and <code>500</code>
    * if a status code doesn’t appear, don’t print anything for this status code
    * format: <code>&lt;status code&gt;: &lt;number&gt;</code>
    * status codes should be printed in ascending order

```
guillaume@ubuntu:~/$ cat 101-generator.py
#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

for i in range(10000):
    sleep(random.random())
    sys.stdout.write("{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
        random.randint(1, 255), random.randint(1, 255), random.randint(1, 255), random.randint(1, 255),
        datetime.datetime.now(),
        random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
        random.randint(1, 1024)
    ))
    sys.stdout.flush()

guillaume@ubuntu:~/$ ./101-generator.py | ./101-stats.py 
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
File size: 11320
200: 3
301: 2
400: 1
401: 2
403: 3
404: 4
405: 2
500: 3
File size: 16305
200: 3
301: 3
400: 4
401: 2
403: 5
404: 5
405: 4
500: 4
^CFile size: 17146
200: 4
301: 3
400: 4
401: 2
403: 6
404: 6
405: 4
500: 4
Traceback (most recent call last):
  File "./101-stats.py", line 15, in <module>
Traceback (most recent call last):
  File "./101-generator.py", line 8, in <module>
    for line in sys.stdin:
KeyboardInterrupt
    sleep(random.random())
KeyboardInterrupt
guillaume@ubuntu:~/$
```

<strong>No test cases needed</strong>

---


## Authors
loicleguen - [GitHub Profile](https://github.com/loicleguen)
