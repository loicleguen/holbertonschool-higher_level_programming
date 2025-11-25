<div align="center"><img src="https://github.com/ksyv/holbertonschool-web_front_end/blob/main/baniere_holberton.png"></div>

# Before you start…

## Table of Contents :

  - [0. Get all states](#subparagraph0)
  - [1. Filter states](#subparagraph1)
  - [2. Filter states by user input](#subparagraph2)
  - [3. SQL Injection...](#subparagraph3)
  - [4. Cities by states](#subparagraph4)
  - [5. All cities by state](#subparagraph5)
  - [6. First state model](#subparagraph6)
  - [7. All states via SQLAlchemy](#subparagraph7)
  - [8. First state](#subparagraph8)
  - [9. Contains `a`](#subparagraph9)
  - [10. Get a state](#subparagraph10)
  - [11. Add a new state](#subparagraph11)
  - [12. Update a state](#subparagraph12)
  - [13. Delete states](#subparagraph13)
  - [14. Cities in state](#subparagraph14)

## Resources
### Read or watch:
* [Object-relational mappers](/rltoken/tCytNeWUzuWhAn9APwtp9A)
* [mysqlclient/MySQLdb documentation](/rltoken/V8KJv3QCReECPZ0V-kXRwg)
* [MySQLdb tutorial](/rltoken/j_7jU3C9Jsa0o53pgfwxOQ)
* [SQLAlchemy tutorial](/rltoken/7y1s8FDE_0S-uhBtCgt5-A)
* [SQLAlchemy](/rltoken/j6kxlUETdjiFwiu0k_JI6Q)
* [mysqlclient/MySQLdb](/rltoken/vzsiR8tCdY3_OWsMH33jUA)
* [Introduction to SQLAlchemy](/rltoken/7m6F57mBASM7A2r_GcIeMA)
* [Flask SQLAlchemy](/rltoken/riV6WcWo1MGRpF3WSmv4Zw)
* [10 common stumbling blocks for SQLAlchemy newbies](/rltoken/uRrjdEkHmjrVenCqjwJRWQ)
* [Python SQLAlchemy Cheatsheet](/rltoken/B2luGwQGH5WjiAMglCu1pg)
* [SQLAlchemy ORM Tutorial for Python Developers](/rltoken/2BoGpuT2vAaoeuC3SN_wPA)
* [SQLAlchemy Tutorial](/rltoken/DrwY56jSHCOADKEbSOBa0A)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
* How to connect to a MySQL database from a Python script
* How toSELECTrows in a MySQL table from a Python script
* How toINSERTrows in a MySQL table from a Python script
* What ORM means
* How to map a Python Class to a MySQL table

## Requirements
### General
* Allowed editors:vi,vim,emacs
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS usingpython3(version 3.8.5)
* Your files will be executed withMySQLdbversion2.0.x
* Your files will be executed withSQLAlchemyversion1.4.x
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
* You are not allowed to useexecutewith sqlalchemy

## Task
### 0. Get all states <a name='subparagraph0'></a>

Write a script that lists all <code>states</code> from the database <code>hbtn_0e_0_usa</code>:

* Your script should take 3 arguments: <code>mysql username</code>, <code>mysql password</code> and <code>database name</code> (no argument validation needed)
* You must use the module <code>MySQLdb</code> (<code>import MySQLdb</code>)
* Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code>
* Results must be sorted in ascending order by <code>states.id</code>
* Results must be displayed as they are in the example below
* Your code should not be executed when imported

```
guillaume@ubuntu:~/$ cat 0-select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

guillaume@ubuntu:~/$ cat 0-select_states.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/$ ./0-select_states.py root root hbtn_0e_0_usa
(1, 'California')
(2, 'Arizona')
(3, 'Texas')
(4, 'New York')
(5, 'Nevada')
guillaume@ubuntu:~/$
```

<strong>No test cases needed</strong>

---

### 1. Filter states <a name='subparagraph1'></a>

Write a script that lists all <code>states</code> with a <code>name</code> starting with <code>N</code> (upper N) from the database <code>hbtn_0e_0_usa</code>:

* Your script should take 3 arguments: <code>mysql username</code>, <code>mysql password</code> and <code>database name</code> (no argument validation needed)
* You must use the module <code>MySQLdb</code> (<code>import MySQLdb</code>)
* Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code>
* Results must be sorted in ascending order by <code>states.id</code>
* Results must be displayed as they are in the example below
* Your code should not be executed when imported

```
guillaume@ubuntu:~/$ cat 0-select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

guillaume@ubuntu:~/$ cat 0-select_states.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/$ ./1-filter_states.py root root hbtn_0e_0_usa
(4, 'New York')
(5, 'Nevada')
guillaume@ubuntu:~/$
```

<strong>No test cases needed</strong>

---

### 2. Filter states by user input <a name='subparagraph2'></a>

Write a script that takes in an argument and displays all values in the <code>states</code> table of <code>hbtn_0e_0_usa</code> where <code>name</code> matches the argument.

* Your script should take 4 arguments: <code>mysql username</code>, <code>mysql password</code>, <code>database name</code> and <code>state name searched</code> (no argument validation needed)
* You must use the module <code>MySQLdb</code> (<code>import MySQLdb</code>)
* Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code>
* You must use <code>format</code> to create the SQL query with the user input
* Results must be sorted in ascending order by <code>states.id</code>
* Results must be displayed as they are in the example below
* Your code should not be executed when imported

```
guillaume@ubuntu:~/$ cat 0-select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

guillaume@ubuntu:~/$ cat 0-select_states.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/$ ./2-my_filter_states.py root root hbtn_0e_0_usa 'Arizona'
(2, 'Arizona')
guillaume@ubuntu:~/$
```

<strong>No test cases needed</strong>

---

### 3. SQL Injection... <a name='subparagraph3'></a>

Wait, do you remember the previous task? Did you test <code>"Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '"</code> as an input?

```
guillaume@ubuntu:~/$ ./2-my_filter_states.py root root hbtn_0e_0_usa "Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '"
(2, 'Arizona')
guillaume@ubuntu:~/$ ./0-select_states.py root root hbtn_0e_0_usa
guillaume@ubuntu:~/$
```

What? Empty?

Yes, it’s an <a href="/rltoken/d0bQ5pmhaRPHtf0OJI9-Vg" target="_blank" title="SQL injection">SQL injection</a> to delete all records of a table…

Once again, write a script that takes in arguments and displays all values in the <code>states</code> table of <code>hbtn_0e_0_usa</code> where <code>name</code> matches the argument. But this time, write one that is safe from MySQL injections!

* Your script should take 4 arguments: <code>mysql username</code>, <code>mysql password</code>, <code>database name</code> and <code>state name searched</code> (safe from MySQL injection)
* You must use the module <code>MySQLdb</code> (<code>import MySQLdb</code>)
* Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code>
* Results must be sorted in ascending order by <code>states.id</code>
* Results must be displayed as they are in the example below
* Your code should not be executed when imported

```
guillaume@ubuntu:~/$ cat 0-select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

guillaume@ubuntu:~/$ cat 0-select_states.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/$ ./3-my_safe_filter_states.py root root hbtn_0e_0_usa 'Arizona'
(2, 'Arizona')
guillaume@ubuntu:~/$
```

<strong>No test cases needed</strong>

---

### 4. Cities by states <a name='subparagraph4'></a>

Write a script that lists all <code>cities</code> from the database <code>hbtn_0e_4_usa</code>

* Your script should take 3 arguments: <code>mysql username</code>, <code>mysql password</code> and <code>database name</code>
* You must use the module <code>MySQLdb</code> (<code>import MySQLdb</code>)
* Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code>
* Results must be sorted in ascending order by <code>cities.id</code>
* You can use only <code>execute()</code> once
* Results must be displayed as they are in the example below
* Your code should not be executed when imported

```
guillaume@ubuntu:~/$ cat 4-cities_by_state.sql
-- Create states table in hbtn_0e_4_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_4_usa;
USE hbtn_0e_4_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

CREATE TABLE IF NOT EXISTS cities ( 
    id INT NOT NULL AUTO_INCREMENT, 
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY(state_id) REFERENCES states(id)
);
INSERT INTO cities (state_id, name) VALUES (1, "San Francisco"), (1, "San Jose"), (1, "Los Angeles"), (1, "Fremont"), (1, "Livermore");
INSERT INTO cities (state_id, name) VALUES (2, "Page"), (2, "Phoenix");
INSERT INTO cities (state_id, name) VALUES (3, "Dallas"), (3, "Houston"), (3, "Austin");
INSERT INTO cities (state_id, name) VALUES (4, "New York");
INSERT INTO cities (state_id, name) VALUES (5, "Las Vegas"), (5, "Reno"), (5, "Henderson"), (5, "Carson City");

guillaume@ubuntu:~/$ cat 4-cities_by_state.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/$ ./4-cities_by_state.py root root hbtn_0e_4_usa
(1, 'San Francisco', 'California')
(2, 'San Jose', 'California')
(3, 'Los Angeles', 'California')
(4, 'Fremont', 'California')
(5, 'Livermore', 'California')
(6, 'Page', 'Arizona')
(7, 'Phoenix', 'Arizona')
(8, 'Dallas', 'Texas')
(9, 'Houston', 'Texas')
(10, 'Austin', 'Texas')
(11, 'New York', 'New York')
(12, 'Las Vegas', 'Nevada')
(13, 'Reno', 'Nevada')
(14, 'Henderson', 'Nevada')
(15, 'Carson City', 'Nevada')
guillaume@ubuntu:~/$
```

<strong>No test cases needed</strong>

---

### 5. All cities by state <a name='subparagraph5'></a>

Write a script that takes in the name of a state as an argument and lists all <code>cities</code> of that state, using the database <code>hbtn_0e_4_usa</code>

* Your script should take 4 arguments: <code>mysql username</code>, <code>mysql password</code>, <code>database name</code> and <code>state name</code> (SQL injection free!)
* You must use the module <code>MySQLdb</code> (<code>import MySQLdb</code>)
* Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code>
* Results must be sorted in ascending order by <code>cities.id</code>
* You can use only <code>execute()</code> once
* The results must be displayed as they are in the example below
* Your code should not be executed when imported

```
guillaume@ubuntu:~/$ cat 4-cities_by_state.sql
-- Create states table in hbtn_0e_4_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_4_usa;
USE hbtn_0e_4_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

CREATE TABLE IF NOT EXISTS cities ( 
    id INT NOT NULL AUTO_INCREMENT, 
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY(state_id) REFERENCES states(id)
);
INSERT INTO cities (state_id, name) VALUES (1, "San Francisco"), (1, "San Jose"), (1, "Los Angeles"), (1, "Fremont"), (1, "Livermore");
INSERT INTO cities (state_id, name) VALUES (2, "Page"), (2, "Phoenix");
INSERT INTO cities (state_id, name) VALUES (3, "Dallas"), (3, "Houston"), (3, "Austin");
INSERT INTO cities (state_id, name) VALUES (4, "New York");
INSERT INTO cities (state_id, name) VALUES (5, "Las Vegas"), (5, "Reno"), (5, "Henderson"), (5, "Carson City");

guillaume@ubuntu:~/$ ./5-filter_cities.py root root hbtn_0e_4_usa Texas

guillaume@ubuntu:~/$ cat 4-cities_by_state.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/$ ./5-filter_cities.py root root hbtn_0e_4_usa Texas
Dallas, Houston, Austin
guillaume@ubuntu:~/$ ./5-filter_cities.py root root hbtn_0e_4_usa Hawaii

guillaume@ubuntu:~/$
```

<strong>No test cases needed</strong>

---

### 6. First state model <a name='subparagraph6'></a>

<img alt="" loading="lazy" src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2020/9/f84fe6edb9436c8560996c6d72e17ea51dab28e1.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20251125%2Feu-west-3%2Fs3%2Faws4_request&amp;X-Amz-Date=20251125T151313Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=556376a767e66c9055f7efd891b8b7abefff86776297d666b45f4be4228797fd" style=""/>

Write a python file that contains the class definition of a <code>State</code> and an instance <code>Base = declarative_base()</code>:

* <code>State</code> class:


  * inherits from <code>Base</code> <a href="/rltoken/62tIVCmGm735_tJWLxtJrQ" target="_blank" title="Tips">Tips</a>
  * links to the MySQL table <code>states</code>
  * class attribute <code>id</code> that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
  * class attribute <code>name</code> that represents a column of a string with maximum 128 characters and can’t be null
* You must use the module <code>SQLAlchemy</code>
* Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code>
* <strong>WARNING:</strong> all classes who inherit from <code>Base</code> <strong>must</strong> be imported before calling <code>Base.metadata.create_all(engine)</code>

```
guillaume@ubuntu:~/$ cat 6-model_state.sql
-- Create database hbtn_0e_6_usa
CREATE DATABASE IF NOT EXISTS hbtn_0e_6_usa;
USE hbtn_0e_6_usa;
SHOW CREATE TABLE states;

guillaume@ubuntu:~/$ cat 6-model_state.sql | mysql -uroot -p
Enter password: 
ERROR 1146 (42S02) at line 4: Table 'hbtn_0e_6_usa.states' doesn't exist
guillaume@ubuntu:~/$ cat 6-model_state.py
#!/usr/bin/python3
"""Start link class to table in database 
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

guillaume@ubuntu:~/$ ./6-model_state.py root root hbtn_0e_6_usa
guillaume@ubuntu:~/$ cat 6-model_state.sql | mysql -uroot -p
Enter password: 
Table   Create Table
states  CREATE TABLE `states` (\n  `id` int(11) NOT NULL AUTO_INCREMENT,\n  `name` varchar(128) NOT NULL,\n  PRIMARY KEY (`id`)\n) ENGINE=InnoDB DEFAULT CHARSET=latin1
guillaume@ubuntu:~/$
```

<strong>No test cases needed</strong>

---

### 7. All states via SQLAlchemy <a name='subparagraph7'></a>

Write a script that lists all <code>State</code> objects from the database <code>hbtn_0e_6_usa</code>

* Your script should take 3 arguments: <code>mysql username</code>, <code>mysql password</code> and <code>database name</code>
* You must use the module <code>SQLAlchemy</code>
* You must import <code>State</code> and <code>Base</code> from <code>model_state</code> - <code>from model_state import Base, State</code>
* Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code>
* Results must be sorted in ascending order by <code>states.id</code>
* The results must be displayed as they are in the example below
* Your code should not be executed when imported

```
guillaume@ubuntu:~/$ cat 7-model_state_fetch_all.sql
-- Insert states
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

guillaume@ubuntu:~/$ cat 7-model_state_fetch_all.sql | mysql -uroot -p hbtn_0e_6_usa
Enter password: 
guillaume@ubuntu:~/$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa
1: California
2: Arizona
3: Texas
4: New York
5: Nevada
guillaume@ubuntu:~/$
```

<strong>No test cases needed</strong>

---

### 8. First state <a name='subparagraph8'></a>

Write a script that prints the first <code>State</code> object from the database <code>hbtn_0e_6_usa</code>

* Your script should take 3 arguments: <code>mysql username</code>, <code>mysql password</code> and <code>database name</code>
* You must use the module <code>SQLAlchemy</code>
* You must import <code>State</code> and <code>Base</code> from <code>model_state</code> - <code>from model_state import Base, State</code>
* Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code>
* The state you display must be the first in <code>states.id</code>
* You are not allowed to fetch all states from the database before displaying the result
* The results must be displayed as they are in the example below
* If the table <code>states</code> is empty, print <code>Nothing</code> followed by a new line
* Your code should not be executed when imported

```
guillaume@ubuntu:~/$ ./8-model_state_fetch_first.py root root hbtn_0e_6_usa
1: California
guillaume@ubuntu:~/$
```

<strong>No test cases needed</strong>

---

### 9. Contains `a` <a name='subparagraph9'></a>

Write a script that lists all <code>State</code> objects that contain the letter <code>a</code> from the database <code>hbtn_0e_6_usa</code>

* Your script should take 3 arguments: <code>mysql username</code>, <code>mysql password</code> and <code>database name</code>
* You must use the module <code>SQLAlchemy</code>
* You must import <code>State</code> and <code>Base</code> from <code>model_state</code> - <code>from model_state import Base, State</code>
* Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code>
* Results must be sorted in ascending order by <code>states.id</code>
* The results must be displayed as they are in the example below
* Your code should not be executed when imported

```
guillaume@ubuntu:~/$ ./9-model_state_filter_a.py root root hbtn_0e_6_usa
1: California
2: Arizona
3: Texas
5: Nevada
guillaume@ubuntu:~/$
```

<strong>No test cases needed</strong>

---

### 10. Get a state <a name='subparagraph10'></a>

Write a script that prints the <code>State</code> object with the <code>name</code> passed as argument from the database <code>hbtn_0e_6_usa</code>

* Your script should take 4 arguments: <code>mysql username</code>, <code>mysql password</code>, <code>database name</code> and <code>state name to search</code> (SQL injection free)
* You must use the module <code>SQLAlchemy</code>
* You must import <code>State</code> and <code>Base</code> from <code>model_state</code> - <code>from model_state import Base, State</code>
* Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code>
* You can assume you have one record with the state name to search
* Results must display the <code>states.id</code>
* If no state has the name you searched for, display <code>Not found</code>
* Your code should not be executed when imported

```
guillaume@ubuntu:~/$ ./10-model_state_my_get.py root root hbtn_0e_6_usa Texas
3
guillaume@ubuntu:~/$ ./10-model_state_my_get.py root root hbtn_0e_6_usa Illinois
Not found
guillaume@ubuntu:~/$
```

<strong>No test cases needed</strong>

---

### 11. Add a new state <a name='subparagraph11'></a>

Write a script that adds the <code>State</code> object “Louisiana” to the database <code>hbtn_0e_6_usa</code>

* Your script should take 3 arguments: <code>mysql username</code>, <code>mysql password</code> and <code>database name</code>
* You must use the module <code>SQLAlchemy</code>
* You must import <code>State</code> and <code>Base</code> from <code>model_state</code> - <code>from model_state import Base, State</code>
* Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code>
* Print the new <code>states.id</code> after creation
* Your code should not be executed when imported

```
guillaume@ubuntu:~/$ ./11-model_state_insert.py root root hbtn_0e_6_usa 
6
guillaume@ubuntu:~/$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa 
1: California
2: Arizona
3: Texas
4: New York
5: Nevada
6: Louisiana
guillaume@ubuntu:~/$
```

<strong>No test cases needed</strong>

---

### 12. Update a state <a name='subparagraph12'></a>

Write a script that changes the name of a <code>State</code> object from the database <code>hbtn_0e_6_usa</code>

* Your script should take 3 arguments: <code>mysql username</code>, <code>mysql password</code> and <code>database name</code>
* You must use the module <code>SQLAlchemy</code>
* You must import <code>State</code> and <code>Base</code> from <code>model_state</code> - <code>from model_state import Base, State</code>
* Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code>
* Change the name of the <code>State</code> where <code>id = 2</code> to <code>New Mexico</code>
* Your code should not be executed when imported

```
guillaume@ubuntu:~/$ ./12-model_state_update_id_2.py root root hbtn_0e_6_usa 
guillaume@ubuntu:~/$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa 
1: California
2: New Mexico
3: Texas
4: New York
5: Nevada
6: Louisiana
guillaume@ubuntu:~/$
```

<strong>No test cases needed</strong>

---

### 13. Delete states <a name='subparagraph13'></a>

Write a script that deletes all <code>State</code> objects with a name containing the letter <code>a</code> from the database <code>hbtn_0e_6_usa</code>

* Your script should take 3 arguments: <code>mysql username</code>, <code>mysql password</code> and <code>database name</code>
* You must use the module <code>SQLAlchemy</code>
* You must import <code>State</code> and <code>Base</code> from <code>model_state</code> - <code>from model_state import Base, State</code>
* Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code>
* Your code should not be executed when imported

```
guillaume@ubuntu:~/$ ./13-model_state_delete_a.py root root hbtn_0e_6_usa 
guillaume@ubuntu:~/$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa 
2: New Mexico
4: New York
guillaume@ubuntu:~/$
```

<strong>No test cases needed</strong>

---

### 14. Cities in state <a name='subparagraph14'></a>

Write a Python file similar to <code>model_state.py</code> named <code>model_city.py</code> that contains the class definition of a <code>City</code>.

* <code>City</code> class:


  * inherits from <code>Base</code> (imported from <code>model_state</code>)
  * links to the MySQL table <code>cities</code>
  * class attribute <code>id</code> that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
  * class attribute <code>name</code> that represents a column of a string of 128 characters and can’t be null
  * class attribute <code>state_id</code> that represents a column of an integer, can’t be null and is a foreign key to <code>states.id</code>
* You must use the module <code>SQLAlchemy</code>

Next, write a script <code>14-model_city_fetch_by_state.py</code> that prints all <code>City</code> objects from the database <code>hbtn_0e_14_usa</code>:

* Your script should take 3 arguments: <code>mysql username</code>, <code>mysql password</code> and <code>database name</code>
* You must use the module <code>SQLAlchemy</code>
* You must import <code>State</code> and <code>Base</code> from <code>model_state</code> - <code>from model_state import Base, State</code>
* Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code>
* Results must be sorted in ascending order by <code>cities.id</code>
* Results must be display as they are in the example below (<code>&lt;state name&gt;: (&lt;city id&gt;) &lt;city name&gt;</code>)
* Your code should not be executed when imported

```
guillaume@ubuntu:~/$ cat 14-model_city_fetch_by_state.sql
-- Create database hbtn_0e_14_usa, tables states and cities + some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_14_usa;
USE hbtn_0e_14_usa;

CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

CREATE TABLE IF NOT EXISTS cities ( 
    id INT NOT NULL AUTO_INCREMENT, 
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY(state_id) REFERENCES states(id)
);
INSERT INTO cities (state_id, name) VALUES (1, "San Francisco"), (1, "San Jose"), (1, "Los Angeles"), (1, "Fremont"), (1, "Livermore");
INSERT INTO cities (state_id, name) VALUES (2, "Page"), (2, "Phoenix");
INSERT INTO cities (state_id, name) VALUES (3, "Dallas"), (3, "Houston"), (3, "Austin");
INSERT INTO cities (state_id, name) VALUES (4, "New York");
INSERT INTO cities (state_id, name) VALUES (5, "Las Vegas"), (5, "Reno"), (5, "Henderson"), (5, "Carson City");

guillaume@ubuntu:~/$ cat 14-model_city_fetch_by_state.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/$ ./14-model_city_fetch_by_state.py root root hbtn_0e_14_usa
California: (1) San Francisco
California: (2) San Jose
California: (3) Los Angeles
California: (4) Fremont
California: (5) Livermore
Arizona: (6) Page
Arizona: (7) Phoenix
Texas: (8) Dallas
Texas: (9) Houston
Texas: (10) Austin
New York: (11) New York
Nevada: (12) Las Vegas
Nevada: (13) Reno
Nevada: (14) Henderson
Nevada: (15) Carson City
guillaume@ubuntu:~/$
```

<strong>No test cases needed</strong>

---


## Authors
loicleguen - [GitHub Profile](https://github.com/loicleguen)
