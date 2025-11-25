<div align="center"><img src="https://github.com/ksyv/holbertonschool-web_front_end/blob/main/baniere_holberton.png"></div>

# Introduction

## Table of Contents :

  - [0. Basics of HTTP/HTTPS](#subparagraph0)
  - [1. Consume data from an API using command line tools (curl)](#subparagraph1)
  - [2. Consuming and processing data from an API using Python](#subparagraph2)
  - [3. Develop a simple API using Python with the `http.server` module](#subparagraph3)
  - [4. Develop a Simple API using Python with Flask](#subparagraph4)
  - [5. API Security and Authentication Techniques](#subparagraph5)

## Task
### 0. Basics of HTTP/HTTPS <a name='subparagraph0'></a>

The Hypertext Transfer Protocol (HTTP) is the foundation of data communication on the web. It allows web clients (like browsers) to communicate with web servers. HTTP has evolved over time and has a secure counterpart called HTTPS (HTTP Secure). HTTPS is just like HTTP but with an added layer of security using SSL/TLS encryption. This layer protects the data from eavesdroppers and tampering.

At the end of this exercise, students should be able to:

---

### 1. Consume data from an API using command line tools (curl) <a name='subparagraph1'></a>

<code>curl</code> (Client URL) is a command-line tool that allows users to transfer data to or from a network server, using one of the supported protocols (HTTP, HTTPS, FTP, and more). It’s widely used for debugging, testing, and interacting with RESTful web services and APIs. By mastering <code>curl</code>, one can quickly prototype API requests, diagnose server issues, and more, all from the command line.

At the end of this exercise, students should be able to:

---

### 2. Consuming and processing data from an API using Python <a name='subparagraph2'></a>

Python, due to its readability and a vast library ecosystem, is a popular choice for interacting with web services and APIs. The <code>requests</code> library simplifies HTTP communication and allows users to send HTTP requests using Python. Once the data is fetched, Python’s built-in libraries and tools enable effortless data manipulation and processing.

At the end of this exercise, students should be able to:

* <p>Create a function <code>fetch_and_print_posts()</code> that fetches all post from JSONPlaceholder.</p>

  * Print the status code of the response i.e. <code>Status Code: 200</code>
  * If the request was sucessfull, parse the fetched data into a JSON object using the <code>.json()</code> method of the response object.
  * Iterate through the parsed JSON data and print out the titles of all the posts.
* <p>Create a function <code>fetch_and_save_posts()</code> that fetches all post from JSONPlaceholder.</p>

  * If the request was sucessfull, instead of printing titles, structure the data into a list of dictionaries, where each dictionary represents a post with keys and values for <code>id</code>, <code>title</code>, and <code>body</code>.
  * Using Python’s <code>csv</code> module, write this data into a CSV file called <code>posts.csv</code> with columns corresponding to the dictionary keys.

```
$ cat main_02_requests.py
from task_02_requests import fetch_and_print_posts, fetch_and_save_posts

fetch_and_print_posts()
fetch_and_save_posts()

$ python3 main_02_requests.py 
Status Code: 200
sunt aut facere repellat provident occaecati excepturi optio reprehenderit
qui est esse
ea molestias quasi exercitationem repellat qui ipsa sit aut
eum et est occaecati
nesciunt quas odio
dolorem eum magni eos aperiam quia
...
```

---

### 3. Develop a simple API using Python with the `http.server` module <a name='subparagraph3'></a>

The <code>http.server</code> module in Python’s standard library provides basic classes for implementing web servers. While it’s not typically used for production applications, it’s a handy tool for building simple web servers and understanding the basics of web programming without relying on third-party libraries.

At the end of this exercise, students should be able to:

---

### 4. Develop a Simple API using Python with Flask <a name='subparagraph4'></a>

Flask is a lightweight web framework for Python, which is especially popular for creating small to medium web applications and RESTful APIs. Its minimalist and modular approach makes it a great choice for beginners to delve into web development without the overhead of more complex frameworks.

At the end of this exercise, students should be able to:
1. Set up a Flask application and run a development server.
2. Define and handle routes with Flask to respond to different endpoints.
3. Serve JSON data using Flask.
4. Understand the basics of request handling and response formation in Flask.
5. Handle POST requests to add new data to the API.

* <a href="/rltoken/lVatvIXp28JXebe-Qms1Gw" target="_blank" title="Flask Official Documentation">Flask Official Documentation</a>
Start with the Quickstart section: “A Minimal Application” to get an overall idea on how the framework works.

Test your application using the <code>flask</code> CLI to run the development server.

```
$ flask --app task_04_flask.py run
 * Serving Flask app 'task_04_flask.py'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

* Accessing <code>http://localhost:5000</code> should show the message: <code>"Welcome to the Flask API!"</code>.
* Visiting <code>http://localhost:5000/data</code> should return a JSON response with a list of all usernames stored in the API. For example, if the <code>users</code> dictionary contains <code>{"jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"}, "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}}</code>, the response should be:

```
["jane", "john"]
```

* The <code>/status</code> endpoint should return the string: <code>"OK"</code>.
* Accessing <code>/users/jane</code> should return the full object corresponding to the username “jane”. For example:

```
{
        "username": "jane", 
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"
}
```

* Similarly, accessing <code>/users/john</code> should return:

```
{
        "username": "john", 
        "name": "John",
        "age": 30,
        "city": "New York"
}
```

But if it doesn’t exist, return a <strong>404</strong> with:
<code>json
{"error": "User not found"}
</code>

* Posting a new user to <code>/add_user</code> should add the user to the <code>users</code> dictionary and return a <strong>201</strong> status code with a confirmation message with the user’s data. For example, posting:

```
{
        "username": "alice",
        "name": "Alice",
        "age": 25,
        "city": "San Francisco"
}
```

should return:

```
{
        "message": "User added",
        "user": {
                "username": "alice",
                "name": "Alice",
                "age": 25,
                "city": "San Francisco"
        }
}
```

* Posting a new user to <code>/add_user</code> without a <code>username</code> should return a <strong>400</strong> code error with the message:

```
{
        "error": "Username is required"
}
```

* Posting a new user to <code>/add_user</code> with a duplicate <code>username</code> (i.e., the username already exists) should return a <strong>409</strong> code error with the message:

```
{
        "error": "Username already exists"
}
```

* Posting a new user to <code>/add_user</code> with an invalid JSON body should return a <strong>400</strong> code error with the message:

```
{
        "error": "Invalid JSON"
}
```

---

### 5. API Security and Authentication Techniques <a name='subparagraph5'></a>

API security is of paramount importance, especially when the API is exposed to the wider internet. There are many risks, including unauthorized data access, data tampering, and denial-of-service attacks. One fundamental method of securing APIs is to use authentication and authorization mechanisms, ensuring only authorized users can access certain resources.

At the end of this exercise, students should be able to:

* For basic authentication, store passwords securely using <code>werkzeug.security.generate_password_hash</code> and verify them using <code>werkzeug.security.check_password_hash</code>.
* Embed user information, such as roles, within the JWT token payload.
* Use a strong secret key for JWT token generation and validation.
* Utilize <code>get_jwt_identity()</code> to retrieve user information from the current JWT token.

* Users should be stored in memory using a dictionary with the following structure:

```
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}
```

* <strong>Protected Route</strong>:


  * URL: <code>/basic-protected</code>
  * Method: <code>GET</code>
  * Description: Returns a message <code>"Basic Auth: Access Granted"</code> if the user provides valid basic authentication credentials.
  * Authentication: Basic

* <p><strong>Login</strong>:</p>

  * URL: <code>/login</code>
  * Method: <code>POST</code>
  * Description: Accepts JSON payload with <code>username</code> and <code>password</code>. Returns a JWT token if credentials are valid.
  * Example Request:


<pre><code class="json">   {
       "username": "user1",
       "password": "password"
   }
</code></pre>

  * Example Response:


<pre><code class="json">   {
       "access_token": "&lt;JWT_TOKEN&gt;"
   }
</code></pre>
* <p><strong>JWT Protected Route</strong>:</p>

  * URL: <code>/jwt-protected</code>
  * Method: <code>GET</code>
  * Description: Returns a message <code>"JWT Auth: Access Granted"</code> if the user provides a valid JWT token.
  * Authentication: JWT
* <p><strong>Role-based Protected Route</strong>:</p>

  * URL: <code>/admin-only</code>
  * Method: <code>GET</code>
  * Description: Returns a message <code>"Admin Access: Granted"</code> if the user is an admin.
  * Authentication: JWT with role check

When implementing authentication in your Flask API, ensure that all authentication errors return a <code>401 Unauthorized response</code>. This includes errors due to missing, invalid, expired, or malformed tokens. Returning a consistent <code>401</code> status code for authentication errors is crucial for passing the automated tests. Failure to return a <code>401</code> status code for these errors may result in failing tests.

* <strong>Custom Error Handlers</strong>: Use <code>Flask-JWT-Extended</code>‘s decorators to create custom error handlers for different types of JWT errors.

Here are some examples:

```
from flask_jwt_extended import JWTManager

  app = Flask(__name__)
  jwt = JWTManager(app)

  @jwt.unauthorized_loader
  def handle_unauthorized_error(err):
      return jsonify({"error": "Missing or invalid token"}), 401

  @jwt.invalid_token_loader
  def handle_invalid_token_error(err):
      return jsonify({"error": "Invalid token"}), 401

  @jwt.expired_token_loader
  def handle_expired_token_error(err):
      return jsonify({"error": "Token has expired"}), 401

  @jwt.revoked_token_loader
  def handle_revoked_token_error(err):
      return jsonify({"error": "Token has been revoked"}), 401

  @jwt.needs_fresh_token_loader
  def handle_needs_fresh_token_error(err):
      return jsonify({"error": "Fresh token required"}), 401
```

---


## Authors
loicleguen - [GitHub Profile](https://github.com/loicleguen)
