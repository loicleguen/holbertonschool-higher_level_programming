<div align="center"><img src="https://github.com/ksyv/holbertonschool-web_front_end/blob/main/baniere_holberton.png"></div>

# Resources

## Table of Contents :

  - [0. My privileges!](#subparagraph0)
  - [1. Root user](#subparagraph1)
  - [2. Read user](#subparagraph2)
  - [3. Always a name](#subparagraph3)
  - [4. ID can't be null](#subparagraph4)
  - [5. Unique ID](#subparagraph5)
  - [6. States table](#subparagraph6)
  - [7. Cities table](#subparagraph7)
  - [8. Cities of California](#subparagraph8)
  - [9. Cities by States](#subparagraph9)
  - [10. Genre ID by show](#subparagraph10)
  - [11. Genre ID for all shows](#subparagraph11)
  - [12. No genre](#subparagraph12)
  - [13. Number of shows by genre](#subparagraph13)
  - [14. My genres](#subparagraph14)
  - [15. Only Comedy](#subparagraph15)
  - [16. List shows and genres](#subparagraph16)

## Resources
### Read or watch:
* [How To Create a New User and Grant Permissions in MySQL](/rltoken/1tuxYhEv__bmrwkAicbjpA)
* [How To Use MySQL GRANT Statement To Grant Privileges To a User](/rltoken/km4VxJIBhjKVfiWEBETk-w)
* [MySQL constraints](/rltoken/AHI2a6vFyr8h4LeI6xK96w)
* [Basic query operation: the join](/rltoken/iwZZ9bwumE2xjRjvK-yCxQ)
* [SQL technique: multiple joins and the distinct keyword](/rltoken/Hy6OBC0V9kzCRA5Xl0L7gw)
* [SQL technique: join types](/rltoken/MQFjsE5PICdbya6ef9fglw)
* [SQL technique: subqueries](/rltoken/L7aZyitKEI69svRrvEt9Ag)
* [SQL technique: union and minus](/rltoken/jidXwpyYDU7yhJspxvx0kw)
* [MySQL Cheat Sheet](/rltoken/g8QlxhHt2_WHdIXE-2oYYw)
* [The Seven Types of SQL Joins](/rltoken/o6faV44f8S34zW3FiO5Mgg)
* [MySQL Tutorial](/rltoken/T3VjE1yBfwJcd1hDD4tItw)
* [SQL Style Guide](/rltoken/0NaQZjOUvQuWy0xGPhTkVw)
* [MySQL 8.0 SQL Statement Syntax](/rltoken/R5KAnzO4iwYo2LgD3eKL8A)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
* How to create a new MySQL user
* How to manage privileges for a user to a database or table
* What’s aPRIMARY KEY
* What’s aFOREIGN KEY
* How to useNOT NULLandUNIQUEconstraints
* How to retrieve datas from multiple tables in one request
* What are subqueries
* What areJOINandUNION

## Requirements
### General
* Allowed editors:vi,vim,emacs
* All your files will be executed on Ubuntu 20.04 LTS usingMySQL 8.0(version 8.0.25)
* All your files should end with a new line
* All your SQL queries should have a comment just before (i.e. syntax above)
* All your files should start by a comment describing the task
* All SQL keywords should be in uppercase (SELECT,WHERE…)
* AREADME.mdfile, at the root of the folder of the project, is mandatory
* The length of your files will be tested usingwc

## Task
### 0. My privileges! <a name='subparagraph0'></a>

Write a script that lists all privileges of the MySQL users <code>user_0d_1</code> and <code>user_0d_2</code> on your server (in <code>localhost</code>).

```
guillaume@ubuntu:~/$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p
Enter password: 
ERROR 1141 (42000) at line 3: There is no such grant defined for user 'user_0d_1' on host 'localhost'
guillaume@ubuntu:~/$ 
guillaume@ubuntu:~/$ echo "CREATE USER 'user_0d_1'@'localhost';" |  mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ echo "GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';" |  mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p
Enter password: 
Grants for user_0d_1@localhost                                                                                                
GRANT SELECT, INSERT, UPDA..., DROP ROLE ON *.* TO `user_0d_1`@`localhost`                                                                                                                             
GRANT APPLICATION_PASSWORD_ADMIN,AUDIT...,XA_RECOVER_ADMIN ON *.* TO `user_0d_1`@`localhost`                                        
ERROR 1141 (42000) at line 4: There is no such grant defined for user 'user_0d_2' on host 'localhost'              
guillaume@ubuntu:~/$
```

---

### 1. Root user <a name='subparagraph1'></a>

Write a script that creates the MySQL server user <code>user_0d_1</code>.

* <code>user_0d_1</code> should have all privileges on your MySQL server
* The <code>user_0d_1</code> password should be set to <code>user_0d_1_pwd</code>
* If the user <code>user_0d_1</code> already exists, your script should not fail

```
guillaume@ubuntu:~/$ cat 1-create_user.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p
Enter password: 
Grants for user_0d_1@localhost                                                                                                
GRANT SELECT, INSERT..., DROP ROLE ON *.* TO `user_0d_1`@`localhost`                                                                                                                             
GRANT APPLICATION_PASSWORD_ADMIN,...,XA_RECOVER_ADMIN ON *.* TO `user_0d_1`@`localhost`                                        
ERROR 1141 (42000) at line 4: There is no such grant defined for user 'user_0d_2' on host 'localhost'
guillaume@ubuntu:~/$
```

---

### 2. Read user <a name='subparagraph2'></a>

Write a script that creates the database <code>hbtn_0d_2</code> and the user <code>user_0d_2</code>.

* <code>user_0d_2</code> should have only SELECT privilege in the database <code>hbtn_0d_2</code>
* The <code>user_0d_2</code> password should be set to <code>user_0d_2_pwd</code>
* If the database <code>hbtn_0d_2</code> already exists, your script should not fail
* If the user <code>user_0d_2</code> already exists, your script should not fail

```
guillaume@ubuntu:~/$ cat 2-create_read_user.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p
Enter password: 
Grants for user_0d_1@localhost                                                                                                
GRANT SELECT, ..., DROP ROLE ON *.* TO `user_0d_1`@`localhost`                                                                                                                             
GRANT APPLICATION_PASSWORD_ADMIN,...,XA_RECOVER_ADMIN ON *.* TO `user_0d_1`@`localhost`                                        
Grants for user_0d_2@localhost                                                                                                
GRANT USAGE ON *.* TO `user_0d_2`@`localhost`                                                                                 
GRANT SELECT ON `hbtn_0d_2`.* TO `user_0d_2`@`localhost`  
guillaume@ubuntu:~/$
```

---

### 3. Always a name <a name='subparagraph3'></a>

Write a script that creates the table <code>force_name</code> on your MySQL server.

* <code>force_name</code> description:


  * <code>id</code> INT
  * <code>name</code> VARCHAR(256) can’t be null
* The database name will be passed as an argument of the <code>mysql</code> command
* If the table <code>force_name</code> already exists, your script should not fail

```
guillaume@ubuntu:~/$ cat 3-force_name.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
guillaume@ubuntu:~/$ echo 'INSERT INTO force_name (id, name) VALUES (89, "Best School");' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
guillaume@ubuntu:~/$ echo 'SELECT * FROM force_name;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
id  name
89  Best School
guillaume@ubuntu:~/$ echo 'INSERT INTO force_name (id) VALUES (333);' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
ERROR 1364 (HY000) at line 1: Field 'name' doesn't have a default value
guillaume@ubuntu:~/$ echo 'SELECT * FROM force_name;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
id  name
89  Best School
guillaume@ubuntu:~/$
```

---

### 4. ID can't be null <a name='subparagraph4'></a>

Write a script that creates the table <code>id_not_null</code> on your MySQL server.

* <code>id_not_null</code> description:


  * <code>id</code> INT with the default value <code>1</code>
  * <code>name</code> VARCHAR(256)
* The database name will be passed as an argument of the <code>mysql</code> command
* If the table <code>id_not_null</code> already exists, your script should not fail

```
guillaume@ubuntu:~/$ cat 4-never_empty.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
guillaume@ubuntu:~/$ echo 'INSERT INTO id_not_null (id, name) VALUES (89, "Best School");' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
guillaume@ubuntu:~/$ echo 'SELECT * FROM id_not_null;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
id  name
89  Best School
guillaume@ubuntu:~/$ echo 'INSERT INTO id_not_null (name) VALUES ("Best");' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
guillaume@ubuntu:~/$ echo 'SELECT * FROM id_not_null;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
id  name
89  Best School
1   Best
guillaume@ubuntu:~/$
```

---

### 5. Unique ID <a name='subparagraph5'></a>

Write a script that creates the table <code>unique_id</code> on your MySQL server.

* <code>unique_id</code> description:


  * <code>id</code> INT with the default value <code>1</code> and must be unique
  * <code>name</code> VARCHAR(256)
* The database name will be passed as an argument of the <code>mysql</code> command
* If the table <code>unique_id</code> already exists, your script should not fail

```
guillaume@ubuntu:~/$ cat 5-unique_id.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
guillaume@ubuntu:~/$ echo 'INSERT INTO unique_id (id, name) VALUES (89, "Best School");' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
guillaume@ubuntu:~/$ echo 'SELECT * FROM unique_id;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
id  name
89  Best School
guillaume@ubuntu:~/$ echo 'INSERT INTO unique_id (id, name) VALUES (89, "Best");' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
ERROR 1062 (23000) at line 1: Duplicate entry '89' for key 'unique_id.id'
guillaume@ubuntu:~/$ echo 'SELECT * FROM unique_id;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
id  name
89  Best School
guillaume@ubuntu:~/$
```

---

### 6. States table <a name='subparagraph6'></a>

Write a script that creates the database <code>hbtn_0d_usa</code> and the table <code>states</code> (in the database <code>hbtn_0d_usa</code>) on your MySQL server.

* <code>states</code> description:


  * <code>id</code> INT unique, auto generated, can’t be null and is a primary key
  * <code>name</code> VARCHAR(256) can’t be null
* If the database <code>hbtn_0d_usa</code> already exists, your script should not fail
* If the table <code>states</code> already exists, your script should not fail

```
guillaume@ubuntu:~/$ cat 6-states.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ echo 'INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas");' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
guillaume@ubuntu:~/$ echo 'SELECT * FROM states;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id  name
1   California
2   Arizona
3   Texas
guillaume@ubuntu:~/$
```

---

### 7. Cities table <a name='subparagraph7'></a>

Write a script that creates the database <code>hbtn_0d_usa</code> and the table <code>cities</code> (in the database <code>hbtn_0d_usa</code>) on your MySQL server.

* <code>cities</code> description:


  * <code>id</code> INT unique, auto generated, can’t be null and is a primary key
  * <code>state_id</code> INT, can’t be null and must be a <code>FOREIGN KEY</code> that references to <code>id</code> of the <code>states</code> table
  * <code>name</code> VARCHAR(256) can’t be null
* If the database <code>hbtn_0d_usa</code> already exists, your script should not fail
* If the table <code>cities</code> already exists, your script should not fail

```
guillaume@ubuntu:~/$ cat 7-cities.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ echo 'INSERT INTO cities (state_id, name) VALUES (1, "San Francisco");' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
guillaume@ubuntu:~/$ echo 'SELECT * FROM cities;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id  state_id    name
1   1   San Francisco
guillaume@ubuntu:~/$ echo 'INSERT INTO cities (state_id, name) VALUES (10, "Paris");' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
ERROR 1452 (23000) at line 1: Cannot add or update a child row: a foreign key constraint fails (`hbtn_0d_usa`.`cities`, CONSTRAINT `cities_ibfk_1` FOREIGN KEY (`state_id`) REFERENCES `states` (`id`))
guillaume@ubuntu:~/$ echo 'SELECT * FROM cities;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id  state_id    name
1   1   San Francisco
guillaume@ubuntu:~/$
```

---

### 8. Cities of California <a name='subparagraph8'></a>

Write a script that lists all the cities of California that can be found in the database <code>hbtn_0d_usa</code>.

* The <code>states</code> table contains only one record where <code>name</code> = <code>California</code> (but the <code>id</code> can be different, as per the example)
* Results must be sorted in ascending order by <code>cities.id</code>
* You are not allowed to use the <code>JOIN</code> keyword
* The database name will be passed as an argument of the <code>mysql</code> command

```
guillaume@ubuntu:~/$ echo 'SELECT * FROM states;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id  name
1   California
2   Arizona
3   Texas
4   Utah
guillaume@ubuntu:~/$ echo 'SELECT * FROM cities;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id  state_id    name
1   1   San Francisco
2   1   San Jose
4   2   Page
6   3   Paris
7   3   Houston
8   3   Dallas
guillaume@ubuntu:~/$ cat 8-cities_of_california_subquery.sql | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id  name
1   San Francisco
2   San Jose
guillaume@ubuntu:~/$
```

---

### 9. Cities by States <a name='subparagraph9'></a>

Write a script that lists all cities contained in the database <code>hbtn_0d_usa</code>.

* Each record should display: <code>cities.id</code> - <code>cities.name</code> - <code>states.name</code>
* Results must be sorted in ascending order by <code>cities.id</code>
* You can use only one <code>SELECT</code> statement
* The database name will be passed as an argument of the <code>mysql</code> command

```
guillaume@ubuntu:~/$ echo 'SELECT * FROM states;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id  name
1   California
2   Arizona
3   Texas
4   Utah
guillaume@ubuntu:~/$ echo 'SELECT * FROM cities;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id  state_id    name
1   1   San Francisco
2   1   San Jose
4   2   Page
6   3   Paris
7   3   Houston
8   3   Dallas
guillaume@ubuntu:~/$ cat 9-cities_by_state_join.sql | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id  name    name
1   San Francisco   California
2   San Jose    California
4   Page    Arizona
6   Paris   Texas
7   Houston Texas
8   Dallas  Texas
guillaume@ubuntu:~/$
```

---

### 10. Genre ID by show <a name='subparagraph10'></a>

Import the database dump from <code>hbtn_0d_tvshows</code> to your MySQL server: <a href="https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" target="_blank" title="download">download</a>

Write a script that lists all shows contained in <code>hbtn_0d_tvshows</code> that have at least one genre linked.

* Each record should display: <code>tv_shows.title</code> - <code>tv_show_genres.genre_id</code>
* Results must be sorted in ascending order  by <code>tv_shows.title</code> and <code>tv_show_genres.genre_id</code>
* You can use only one <code>SELECT</code> statement
* The database name will be passed as an argument of the <code>mysql</code> command

```
guillaume@ubuntu:~/$ cat 10-genre_id_by_show.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password: 
title   genre_id
Breaking Bad    1
Breaking Bad    6
Breaking Bad    7
Breaking Bad    8
Dexter  1
Dexter  2
Dexter  6
Dexter  7
Dexter  8
Game of Thrones 1
Game of Thrones 3
Game of Thrones 4
House   1
House   2
New Girl    5
Silicon Valley  5
The Big Bang Theory 5
The Last Man on Earth   1
The Last Man on Earth   5
guillaume@ubuntu:~/$
```

---

### 11. Genre ID for all shows <a name='subparagraph11'></a>

Import the database dump of <code>hbtn_0d_tvshows</code> to your MySQL server: <a href="https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" target="_blank" title="download">download</a> (same as <code>10-genre_id_by_show.sql</code>)

Write a script that lists all shows contained in the database <code>hbtn_0d_tvshows</code>.

* Each record should display: <code>tv_shows.title</code> - <code>tv_show_genres.genre_id</code>
* Results must be sorted in ascending order by <code>tv_shows.title</code> and <code>tv_show_genres.genre_id</code>
* If a show doesn’t have a genre, display <code>NULL</code>
* You can use only one <code>SELECT</code> statement
* The database name will be passed as an argument of the <code>mysql</code> command

```
guillaume@ubuntu:~/$ cat 11-genre_id_all_shows.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password: 
title   genre_id
Better Call Saul    NULL
Breaking Bad    1
Breaking Bad    6
Breaking Bad    7
Breaking Bad    8
Dexter  1
Dexter  2
Dexter  6
Dexter  7
Dexter  8
Game of Thrones 1
Game of Thrones 3
Game of Thrones 4
Homeland    NULL
House   1
House   2
New Girl    5
Silicon Valley  5
The Big Bang Theory 5
The Last Man on Earth   1
The Last Man on Earth   5
guillaume@ubuntu:~/$
```

---

### 12. No genre <a name='subparagraph12'></a>

Import the database dump from <code>hbtn_0d_tvshows</code> to your MySQL server: <a href="https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" target="_blank" title="download">download</a> (same as <code>11-genre_id_all_shows.sql</code>)

Write a script that lists all shows contained in <code>hbtn_0d_tvshows</code> without a genre linked.

* Each record should display: <code>tv_shows.title</code> - <code>tv_show_genres.genre_id</code>
* Results must be sorted in ascending order by <code>tv_shows.title</code> and <code>tv_show_genres.genre_id</code>
* You can use only one <code>SELECT</code> statement
* The database name will be passed as an argument of the <code>mysql</code> command

```
guillaume@ubuntu:~/$ cat 12-no_genre.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password: 
title   genre_id
Better Call Saul    NULL
Homeland    NULL
guillaume@ubuntu:~/$
```

---

### 13. Number of shows by genre <a name='subparagraph13'></a>

Import the database dump from <code>hbtn_0d_tvshows</code> to your MySQL server: <a href="https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" target="_blank" title="download">download</a> (same as <code>12-no_genre.sql</code>)

Write a script that lists all genres from <code>hbtn_0d_tvshows</code> and displays the number of shows linked to each.

* Each record should display: <code>&lt;TV Show genre&gt;</code> - <code>&lt;Number of shows linked to this genre&gt;</code>
* First column must be called <code>genre</code>
* Second column must be called <code>number_of_shows</code>
* Don’t display a genre that doesn’t have any shows linked
* Results must be sorted in descending order by the number of shows linked
* You can use only one <code>SELECT</code> statement
* The database name will be passed as an argument of the <code>mysql</code> command

```
guillaume@ubuntu:~/$ cat 13-count_shows_by_genre.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password: 
genre   number_of_shows
Drama   5
Comedy  4
Mystery 2
Crime   2
Suspense    2
Thriller    2
Adventure   1
Fantasy 1
guillaume@ubuntu:~/$
```

---

### 14. My genres <a name='subparagraph14'></a>

Import the database dump from <code>hbtn_0d_tvshows</code> to your MySQL server: <a href="https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" target="_blank" title="download">download</a> (same as <code>13-count_shows_by_genre.sql</code>)

Write a script that uses the <code>hbtn_0d_tvshows</code> database to lists all genres of the show <code>Dexter</code>.

* The <code>tv_shows</code> table contains only one record where <code>title</code> = <code>Dexter</code> (but the <code>id</code> can be different)
* Each record should display: <code>tv_genres.name</code>
* Results must be sorted in ascending order by the genre name
* You can use only one <code>SELECT</code> statement
* The database name will be passed as an argument of the <code>mysql</code> command

```
guillaume@ubuntu:~/$ cat 14-my_genres.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password: 
name
Crime
Drama
Mystery
Suspense
Thriller
guillaume@ubuntu:~/$
```

---

### 15. Only Comedy <a name='subparagraph15'></a>

Import the database dump from <code>hbtn_0d_tvshows</code> to your MySQL server: <a href="https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" target="_blank" title="download">download</a> (same as <code>14-my_genres.sql</code>)

Write a script that lists all Comedy shows in the database <code>hbtn_0d_tvshows</code>.

* The <code>tv_genres</code> table contains only one record where <code>name</code> = <code>Comedy</code> (but the <code>id</code> can be different)
* Each record should display: <code>tv_shows.title</code>
* Results must be sorted in ascending order by the show title
* You can use only one <code>SELECT</code> statement
* The database name will be passed as an argument of the <code>mysql</code> command

```
guillaume@ubuntu:~/$ cat 15-comedy_only.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password: 
title
New Girl
Silicon Valley
The Big Bang Theory
The Last Man on Earth
guillaume@ubuntu:~/$
```

---

### 16. List shows and genres <a name='subparagraph16'></a>

Import the database dump from <code>hbtn_0d_tvshows</code> to your MySQL server: <a href="https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" target="_blank" title="download">download</a> (same as <code>15-comedy_only.sql</code>)

Write a script that lists all shows, and all genres linked to that show, from the database <code>hbtn_0d_tvshows</code>.

* If a show doesn’t have a genre, display <code>NULL</code> in the genre column
* Each record should display: <code>tv_shows.title</code> - <code>tv_genres.name</code>
* Results must be sorted in ascending order by the show title and genre name
* You can use only one <code>SELECT</code> statement
* The database name will be passed as an argument of the <code>mysql</code> command

```
guillaume@ubuntu:~/$ cat 16-shows_by_genre.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password: 
title   name
Better Call Saul    NULL
Breaking Bad    Crime
Breaking Bad    Drama
Breaking Bad    Suspense
Breaking Bad    Thriller
Dexter  Crime
Dexter  Drama
Dexter  Mystery
Dexter  Suspense
Dexter  Thriller
Game of Thrones Adventure
Game of Thrones Drama
Game of Thrones Fantasy
Homeland    NULL
House   Drama
House   Mystery
New Girl    Comedy
Silicon Valley  Comedy
The Big Bang Theory Comedy
The Last Man on Earth   Comedy
The Last Man on Earth   Drama
guillaume@ubuntu:~/$
```

---


## Authors
loicleguen - [GitHub Profile](https://github.com/loicleguen)
