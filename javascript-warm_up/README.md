<div align="center"><img src="https://github.com/ksyv/holbertonschool-web_front_end/blob/main/baniere_holberton.png"></div>

# Background Context

## Table of Contents :

  - [0. First constant, first print](#subparagraph0)
  - [1. languages](#subparagraph1)
  - [2. Arguments](#subparagraph2)
  - [3. Value of my argument](#subparagraph3)
  - [4. Create a sentence](#subparagraph4)
  - [5. An Integer](#subparagraph5)
  - [6. Loop to languages](#subparagraph6)
  - [7. I love C](#subparagraph7)
  - [8. Square](#subparagraph8)
  - [9. Add](#subparagraph9)
  - [10. Factorial](#subparagraph10)
  - [11. Second biggest!](#subparagraph11)
  - [12. Object](#subparagraph12)
  - [13. Add file](#subparagraph13)

## Resources
### Read or watch:
* [Writing JavaScript Code](/rltoken/fQUkQNjfE1Dw47vcgps6Ig)
* [Variables](/rltoken/FX6qEtLyELhXUg7u23eMDg)
* [Data Types](/rltoken/R5-aJ7W7ypXbTAcI54Ut-g)
* [Operators](/rltoken/fQUkQNjfE1Dw47vcgps6Ig)
* [Operator Precedence](/rltoken/4PdyDQJJuDXEZmbALqttug)
* [Controlling Program Flow](/rltoken/N0Np7QFZVwSnRopkHsN4ow)
* [Functions](/rltoken/21XrxDV4cjQfW8v7r2FNMw)
* [Objects and Arrays](/rltoken/LSNtL9tP1DBU0bnBLdF2uA)
* [Intrinsic Objects](/rltoken/LSNtL9tP1DBU0bnBLdF2uA)
* [Module patterns](/rltoken/OOAH-N9qs-oT4Y32ErUELQ)
* [var, let and const](/rltoken/5dIWvs6Zn5XjcsP18Ti9Uw)
* [JavaScript Tutorial](/rltoken/PzZBOx5Ms7RL0FX1fihHKw)
* [Modern JS](/rltoken/toueHB-cJAYoXNscJtr3Jw)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
* Why JavaScript programming is amazing
* How to run a JavaScript script
* How to create variables and constants
* What are differences betweenvar,constandlet
* What are all the data types available in JavaScript
* How to use theif,if ... elsestatements
* How to use comments
* How to affect values to variables
* How to usewhileandforloops
* How to usebreakandcontinuestatements
* What is a function and how do you use functions
* What does a function that does not use anyreturnstatement return
* Scope of variables
* What are the arithmetic operators and how to use them
* How to manipulate dictionary
* How to import a file

## Requirements
### General
* Allowed editors:vi,vim,emacs
* All your files will be interpreted on Ubuntu 20.04 LTS usingnode(version 14.x)
* All your files should end with a new line
* The first line of all your files should be exactly#!/usr/bin/node
* AREADME.mdfile, at the root of the folder of the project, is mandatory
* Your code should besemistandardcompliant (version 16.x.x).Rules of Standard+semicolons on top. Also as reference:AirBnB style
* All your files must be executable
* The length of your files will be tested usingwc

## Task
### 0. First constant, first print <a name='subparagraph0'></a>

Write a script that prints “JavaScript is amazing”:

* You must create a constant variable called <code>myVar</code> with the value “JavaScript is amazing”
* You must use <code>console.log(...)</code> to print all output
* You are not allowed to use <code>var</code>

```
guillaume@ubuntu:~/$ ./0-javascript_is_amazing.js 
JavaScript is amazing
guillaume@ubuntu:~/$ 
guillaume@ubuntu:~/$ semistandard ./0-javascript_is_amazing.js 
guillaume@ubuntu:~/$
```

---

### 1. languages <a name='subparagraph1'></a>

Write a script that prints 3 lines:

* The first line: “C is fun”
* The second line: “Python is cool”
* The third line: “JavaScript is amazing”
* You must use <code>console.log(...)</code> to print all output
* You are not allowed to use <code>var</code>

```
guillaume@ubuntu:~/$ ./1-multi_languages.js 
C is fun
Python is cool
JavaScript is amazing
guillaume@ubuntu:~/$
```

---

### 2. Arguments <a name='subparagraph2'></a>

Write a script that prints a message depending of the number of arguments passed:

* If no arguments are passed to the script, print “No argument”
* If only one argument is passed to the script, print “Argument found”
* Otherwise, print “Arguments found”
* You must use <code>console.log(...)</code> to print all output
* You are not allowed to use <code>var</code>

Reference: <a href="/rltoken/vCoaeNm6cQ46Ns3YLGBxAw" target="_blank" title="process.argv">process.argv</a>

```
guillaume@ubuntu:~/$ ./2-arguments.js 
No argument
guillaume@ubuntu:~/$ ./2-arguments.js Best
Argument found
guillaume@ubuntu:~/$ ./2-arguments.js Best School
Arguments found
guillaume@ubuntu:~/$
```

---

### 3. Value of my argument <a name='subparagraph3'></a>

Write a script that prints the first argument passed to it:

* If no arguments are passed to the script, print “No argument”
* You must use <code>console.log(...)</code> to print all output
* You are not allowed to use <code>var</code>
* You are not allowed to use <code>length</code>

```
guillaume@ubuntu:~/$ ./3-value_argument.js 
No argument
guillaume@ubuntu:~/$ ./3-value_argument.js School
School
guillaume@ubuntu:~/$
```

---

### 4. Create a sentence <a name='subparagraph4'></a>

Write a script that prints two arguments passed to it, in the following format: “<first argument=""> is <second argument="">”</second></first>

* You must use <code>console.log(...)</code> to print all output
* You are not allowed to use <code>var</code>

```
guillaume@ubuntu:~/$ ./4-concat.js c cool
c is cool
guillaume@ubuntu:~/$ ./4-concat.js c 
c is undefined
guillaume@ubuntu:~/$ ./4-concat.js
undefined is undefined
guillaume@ubuntu:~/$
```

---

### 5. An Integer <a name='subparagraph5'></a>

Write a script that prints <code>My number: &lt;first argument converted in integer&gt;</code> if the first argument can be converted to an integer:

* If the argument can’t be converted to an integer, print “Not a number”
* You must use <code>console.log(...)</code> to print all output
* You are not allowed to use <code>var</code>
* You are not allowed to use <code>try/catch</code>

```
guillaume@ubuntu:~/$ ./5-to_integer.js 
Not a number
guillaume@ubuntu:~/$ ./5-to_integer.js 89
My number: 89
guillaume@ubuntu:~/$ ./5-to_integer.js "89"
My number: 89
guillaume@ubuntu:~/$ ./5-to_integer.js 89.89
My number: 89
guillaume@ubuntu:~/$ ./5-to_integer.js School
Not a number
guillaume@ubuntu:~/$
```

---

### 6. Loop to languages <a name='subparagraph6'></a>

Write a script that prints 3 lines: (like <code>1-multi_languages.js</code>) but by using an array of string and a loop

* The first line: “C is fun”
* The second line: “Python is cool”
* The third line: “JavaScript is amazing”
* You must use <code>console.log(...)</code> to print all output
* You are not allowed to use <code>var</code>
* You are not allowed to use any <code>if/else</code> statement
* You can use only one <code>console.log</code>
* You must use a loop (<code>while</code>, <code>for</code>, etc.)

```
guillaume@ubuntu:~/$ ./6-multi_languages_loop.js 
C is fun
Python is cool
JavaScript is amazing
guillaume@ubuntu:~/$
```

---

### 7. I love C <a name='subparagraph7'></a>

Write a script that prints <code>x</code> times “C is fun”

* Where <code>x</code> is the first argument of the script
* If the first argument can’t be converted to an integer, print “Missing number of occurrences”
* You must use <code>console.log(...)</code> to print all output
* You are not allowed to use <code>var</code>
* You can use only two <code>console.log</code>
* You must use a loop (<code>while</code>, <code>for</code>, etc.)

```
guillaume@ubuntu:~/$ ./7-multi_c.js 2
C is fun
C is fun
guillaume@ubuntu:~/$ ./7-multi_c.js 5
C is fun
C is fun
C is fun
C is fun
C is fun
guillaume@ubuntu:~/$ ./7-multi_c.js 
Missing number of occurrences
guillaume@ubuntu:~/$ ./7-multi_c.js -3
guillaume@ubuntu:~/$
```

---

### 8. Square <a name='subparagraph8'></a>

Write a script that prints a square

* The first argument is the size of the square
* If the first argument can’t be converted to an integer, print “Missing size”
* You must use the character <code>X</code> to print the square
* You must use <code>console.log(...)</code> to print all output
* You are not allowed to use <code>var</code>
* You must use a loop (<code>while</code>, <code>for</code>, etc.)

```
guillaume@ubuntu:~/$ ./8-square.js
Missing size
guillaume@ubuntu:~/$ ./8-square.js School
Missing size
guillaume@ubuntu:~/$ ./8-square.js 2
XX
XX
guillaume@ubuntu:~/$ ./8-square.js 6
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
guillaume@ubuntu:~/$ ./8-square.js -3
guillaume@ubuntu:~/$
```

---

### 9. Add <a name='subparagraph9'></a>

Write a script that prints the addition of 2 integers

* The first argument is the first integer
* The second argument is the second integer
* You have to define a function with this prototype: <code>function add(a, b)</code>
* You must use <code>console.log(...)</code> to print all output
* You are not allowed to use <code>var</code>

```
guillaume@ubuntu:~/$ ./9-add.js 
NaN
guillaume@ubuntu:~/$ ./9-add.js 1
NaN
guillaume@ubuntu:~/$ ./9-add.js 1 7
8
guillaume@ubuntu:~/$ ./9-add.js 13 89
102
guillaume@ubuntu:~/$
```

---

### 10. Factorial <a name='subparagraph10'></a>

Write a script that computes and prints a factorial

* The first argument is integer (argument can be cast as integer) used for computing the factorial
* Factorial of <code>NaN</code> is <code>1</code>
* You must do it recursively
* You must use a function
* You must use <code>console.log(...)</code> to print all output
* You are not allowed to use <code>var</code>

```
guillaume@ubuntu:~/$ ./10-factorial.js 
1
guillaume@ubuntu:~/$ ./10-factorial.js 3
6
guillaume@ubuntu:~/$ ./10-factorial.js 89
1.6507955160908452e+136
guillaume@ubuntu:~/$ ./10-factorial.js 333
Infinity
guillaume@ubuntu:~/$
```

---

### 11. Second biggest! <a name='subparagraph11'></a>

Write a script that searches the second biggest integer in the list of arguments.

* You can assume all arguments can be converted to integer
* If no argument passed, print <code>0</code>
* If the number of arguments is 1, print <code>0</code>
* You must use <code>console.log(...)</code> to print all output
* You are not allowed to use <code>var</code>

```
guillaume@ubuntu:~/$ ./11-second_biggest.js 
0
guillaume@ubuntu:~/$ ./11-second_biggest.js 1
0
guillaume@ubuntu:~/$ ./11-second_biggest.js 4 2 5 3 0 -3
4
guillaume@ubuntu:~/$
```

---

### 12. Object <a name='subparagraph12'></a>

Update this script to replace the value <code>12</code> with <code>89</code>:

* You are not allowed to use <code>var</code>

```
guillaume@ubuntu:~/$ cat 12-object.js
#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
console.log(myObject);

guillaume@ubuntu:~/$ ./12-object.js
{ type: 'object', value: 12 }
{ type: 'object', value: 89 }
guillaume@ubuntu:~/$
```

---

### 13. Add file <a name='subparagraph13'></a>

Write a function that returns the addition of 2 integers.

* The function must be visible from outside
* The name of the function must be <code>add</code>
* You are not allowed to use <code>var</code>

<a href="/rltoken/RJ9f5jTEwwzvgfbqijdiig" target="_blank" title="Tip">Tip</a>

```
guillaume@ubuntu:~/$ cat 13-main.js
#!/usr/bin/node
const add = require('./13-add').add;
console.log(add(3, 5));
guillaume@ubuntu:~/$ ./13-main.js
8
guillaume@ubuntu:~/$
```

---


## Authors
loicleguen - [GitHub Profile](https://github.com/loicleguen)
