
# Python Fundamentals

## Table of Contents

1. [Introduction to Python](#introduction-to-python)
2. [Variables and Data Types](#variables-and-data-types)
3. [Control Flow](#control-flow)
4. [Functions and Modules](#functions-and-modules)
5. [File Handling](#file-handling)
6. [Exception Handling](#exception-handling)
7. [Data Structures](#data-structures)
8. [Object-Oriented Programming](#object-oriented-programming)
9. [Regular Expressions](#regular-expressions)
10. [Database Connectivity](#database-connectivity)
11. [Web Scraping](#web-scraping)
12. [GUI Programming](#gui-programming)
13. [Multithreading and Multiprocessing](#multithreading-and-multiprocessing)
14. [Networking](#networking)
15. [Testing and Debugging](#testing-and-debugging)
16. [Best Practices and Coding Style](#best-practices-and-coding-style)

---

## 1. Introduction to Python

**Description:**
Python is a versatile and widely-used programming language known for its simplicity and readability. This section introduces the basics of Python programming. <br>
>Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.


**Syntax:**
```python
# This is a comment
print("Hello, World!")
```

**Example:**
```python
# Example of a simple Python program
print("Hello, World!")
```

**Exercise:**
1. Write a program that prints "Welcome to Python!".
2. Add comments explaining each line of your code.

**Resources:**
- [Python Documentation: Getting Started](https://docs.python.org/3/tutorial/index.html)
- [Real Python: Introduction to Python](https://realpython.com/python-introduction/)

---

## 2. Variables and Data Types

**Description:**
Variables are used to store data, and data types specify the type of data a variable holds. Common data types include strings, integers, floats, and booleans. <br>
> In Python, variables are dynamically typed, meaning you don't need to declare their type. The type is inferred from the value assigned. Python supports various data types such as integers, floating-point numbers, strings, and booleans, which are used to represent different kinds of data in a program.


**Syntax:**
```python
# Variable assignment
name = "Alice"       # String
age = 30             # Integer
height = 5.5         # Float
is_student = True    # Boolean
```

**Example:**
```python
# Example of variable assignment
name = "Alice"
age = 30
height = 5.5
is_student = True

# Printing variables
print(name, age, height, is_student)
```

**Exercise:**
1. Create variables for your favorite book's title, author, number of pages, and whether you have read it or not.
2. Print these variables.

**Resources:**
- [Python Documentation: Data Types](https://docs.python.org/3/library/stdtypes.html)
- [Real Python: Variables and Data Types](https://realpython.com/python-data-types/)

---

## 3. Control Flow

### If-Else Statements

**Description:**
Control the flow of the program based on conditions using if-else statements. <br>
> Control flow statements are used to execute different blocks of code based on certain conditions. The `if` statement allows you to check a condition, and if it evaluates to True, a specific block of code is executed. The `else` statement can be used to execute a block of code if the condition is False.

**Syntax:**
```python
if condition:
    # Code to execute if condition is true
else:
    # Code to execute if condition is false
```

**Example:**
```python
age = 20
if age > 18:
    print("Adult")
else:
    print("Minor")
```

**Exercise:**
1. Write a program that checks if a number is positive, negative, or zero.

**Resources:**
- [Python Documentation: if Statements](https://docs.python.org/3/tutorial/controlflow.html#if-statements)
- [Real Python: Conditional Statements](https://realpython.com/python-conditional-statements/)

### Loops

**Description:**
Loops are used to execute a block of code multiple times. <br>
> Loops in Python are used to iterate over a sequence (like a list, tuple, or string) or execute a block of code repeatedly. The `for` loop is used for iterating over a sequence, while the `while` loop continues executing as long as a condition is true.


**Syntax:**
```python
# For loop
for variable in sequence:
    # Code to execute

# While loop
while condition:
    # Code to execute
```

**Example:**
```python
# For loop example
for i in range(5):
    print(i)

# While loop example
count = 0
while count < 5:
    print(count)
    count += 1
```

**Exercise:**
1. Write a program that prints the numbers from 1 to 10 using a for loop.
2. Write a program that prints the numbers from 10 to 1 using a while loop.

**Resources:**
- [Python Documentation: for Statements](https://docs.python.org/3/tutorial/controlflow.html#for-statements)
- [Python Documentation: while Statements](https://docs.python.org/3/tutorial/controlflow.html#the-while-statement)

---

## 4. Functions and Modules

**Description:**
Functions are reusable blocks of code, and modules are files containing Python code that can be imported.

### Functions 
> Functions in Python are defined using the `def` keyword. They allow you to encapsulate code into reusable blocks, making your programs more modular and easier to understand. Functions can take parameters and return values.


**Syntax:**
```python
def function_name(parameters):
    # Code to execute
    return value
```

**Example:**
```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
```

**Exercise:**
1. Write a function that takes a number as input and returns its square.

**Resources:**
- [Python Documentation: Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Real Python: Defining Your Own Python Function](https://realpython.com/defining-your-own-python-function/)

### Modules
> Modules in Python are files containing Python code. They allow you to organize your code into separate files for better manageability. You can import and use functions, classes, and variables defined in other modules using the `import` statement.

**Syntax:**
```python
import module_name
```

**Example:**
```python
import math
print(math.sqrt(16))
```

**Exercise:**
1. Use the `math` module to find the factorial of a number.

**Resources:**
- [Python Documentation: Modules](https://docs.python.org/3/tutorial/modules.html)
- [Real Python: Python Modules and Packages](https://realpython.com/python-modules-packages/)

---

## 5. File Handling

**Description:**
Read from and write to files using Python. <br>
> File handling in Python allows you to read from and write to files. The built-in `open()` function is used to open a file, and the `with` statement is used to ensure the file is properly closed after operations.

**Syntax:**
```python
with open('filename', 'mode') as file:
    # Code to read/write file
```

**Example:**
```python
# Writing to a file
with open('example.txt', 'w') as file:
    file.write("Hello, World!")

# Reading from a file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
```

**Exercise:**
1. Write a program that writes the numbers 1 to 10 to a file.
2. Write a program that reads and prints the content of a file.

**Resources:**
- [Python Documentation: File Objects](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [Real Python: Reading and Writing Files in Python](https://realpython.com/read-write-files-python/)

---

## 6. Exception Handling

**Description:**
Handle errors and exceptions gracefully using try-except blocks. <br>
> Exception handling in Python allows you to handle errors gracefully. The `try` block contains code that might raise an exception, and the `except` block contains code that runs if an exception occurs. You can also use `finally` to execute code regardless of whether an exception occurred.

**Syntax:**
```python
try:
    # Code that might raise an exception
except ExceptionType:
    # Code to execute if an exception occurs
finally:
    # Code to execute regardless of an exception
```

**Example:**
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")
finally:
    print("This will execute no matter what.")
```

**Exercise:**
1. Write a program that asks the user to input a number and prints its square root. Use exception handling to manage invalid inputs.
2. Create a function that reads from a file and handles any `FileNotFoundError` exceptions.

**Resources:**
- [Python Documentation: Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Real Python: Python Exception Handling](https://realpython.com/python-exceptions/)

---

## 7. Data Structures

### Lists

**Description:**
Lists are mutable sequences used to store collections of items. <br>
> Lists in Python are ordered, mutable collections of items that can be of mixed data types. Lists are created using square brackets and can be manipulated using various methods such as `append()`, `remove()`, and `sort()`.

**Syntax:**
```python
my_list = [1, 2, 3, 4, 5]
```

**Example:**
```python
# Example of list operations
my_list = [1, 2, 3, 4, 5]
my_list.append(6)
print(my_list)
my_list.remove(2)
print(my_list)
my_list.sort(reverse=True)
print(my_list)
```

**Exercise:**
1. Create a list of your favorite fruits and print it.
2. Add a new fruit to the list, remove one, and sort the list alphabetically.

**Resources:**
- [Python Documentation: Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
- [Real Python: Lists and Tuples](https://realpython.com/python-lists-tuples/)

### Tuples

**Description:**
Tuples are immutable sequences used to store collections of items. <br>
> Tuples in Python are ordered, immutable collections of items that can be of mixed data types. Tuples are created using parentheses and are often used to store related pieces of data.

**Syntax:**
```python
my_tuple = (1, 2, 3, 4, 5)
```

**Example:**
```python
# Example of tuple operations
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
print(my_tuple[1])
print(my_tuple[:3])
```

**Exercise:**
1. Create a tuple of your favorite movies and print it.
2. Access and print the first and last movies in the tuple.

**Resources:**
- [Python Documentation: Tuples](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)
- [Real Python: Lists and Tuples](https://realpython.com/python-lists-tuples/)

### Dictionaries

**Description:**
Dictionaries are mutable mappings used to store key-value pairs. <br>
> Dictionaries in Python are unordered collections of key-value pairs. Keys must be unique and immutable, while values can be of any type. Dictionaries are created using curly braces and can be accessed and modified using keys.

**Syntax:**
```python
my_dict = {'key1': 'value1', 'key2': 'value2'}
```

**Example:**
```python
# Example of dictionary operations
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
print(my_dict['name'])
my_dict['age'] = 31
print(my_dict)
my_dict['country'] = 'USA'
print(my_dict)
```

**Exercise:**
1. Create a dictionary to store information about a book (title, author, year).
2. Update the year of the book and add a new key-value pair for the genre.

**Resources:**
- [Python Documentation: Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [Real Python: Dictionaries in Python](https://realpython.com/python-dicts/)

---

## 8. Object-Oriented Programming

### Classes and Objects

**Description:**
Classes are blueprints for creating objects, and objects are instances of classes. <br>
> Object-oriented programming (OOP) is a programming paradigm based on the concept of objects. A class defines the properties and behaviors of objects. Objects are instances of classes and encapsulate data and functionality.

**Syntax:**
```python
class MyClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}!")

# Creating an object
obj = MyClass("Alice")
obj.greet()
```

**Example:**
```python
# Example of a class and object
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} is barking.")

# Creating objects
dog1 = Dog("Buddy", 3)
dog2 = Dog("Charlie", 5)

dog1.bark()
dog2.bark()
```

**Exercise:**
1. Create a class `Car` with attributes `make`, `model`, and `year`. Add a method `display_info` to print the car's information. Create two car objects and display their information.

**Resources:**
- [Python Documentation: Classes](https://docs.python.org/3/tutorial/classes.html)
- [Real Python: Object-Oriented Programming](https://realpython.com/python3-object-oriented-programming/)

### Inheritance

**Description:**
Inheritance allows a class to inherit attributes and methods from another class. <br>
> Inheritance is a fundamental concept in OOP that allows a class (child class) to inherit attributes and methods from another class (parent class). This promotes code reuse and establishes a hierarchical relationship between classes.

**Syntax:**
```python
class ParentClass:
    # Parent class code

class ChildClass(ParentClass):
    # Child class code
```

**Example:**
```python
# Example of inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} barks."

class Cat(Animal):
    def speak(self):
        return f"{self.name} meows."

dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak())
print(cat.speak())
```

**Exercise:**
1. Create a base class `Person` with attributes `name` and `age`. Create a derived class `Student` with an additional attribute `student_id`. Add a method to display student information.

**Resources:**
- [Python Documentation: Inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance)
- [Real Python: Inheritance and Composition](https://realpython.com/inheritance-composition-python/)

### Polymorphism

**Description:**
Polymorphism allows methods to do different things based on the object it is acting upon. <br>
> Polymorphism is a concept in OOP that allows methods to be used interchangeably between different classes, as long as those classes implement the same methods. It provides a way to perform a single action in different ways.

**Syntax:**
```python
def func(obj):
    obj.method()
```

**Example:**
```python
# Example of polymorphism
class Bird:
    def fly(self):
        print("Bird is flying.")

class Airplane:
    def fly(self):
        print("Airplane is flying.")

def take_off(flying_object):
    flying_object.fly()

bird = Bird()
airplane = Airplane()

take_off(bird)
take_off(airplane)
```

**Exercise:**
1. Create two classes `Rectangle` and `Circle`, each with a method `area`. Implement polymorphism to calculate the area of different shapes using the same method name.

**Resources:**
- [Python Documentation: Polymorphism](https://docs.python.org/3/tutorial/classes.html#tut-polymorphism)
- [Real Python: Polymorphism](https://realpython.com/polymorphism-in-python/)

---

## 9. Regular Expressions

**Description:**
Regular expressions (regex) are sequences of characters that define a search pattern, primarily for use in pattern matching with strings. <br>
> Regular expressions are powerful tools for pattern matching and string manipulation. The `re` module in Python provides functions to work with regular expressions, such as `search`, `match`, and `findall`.

**Syntax:**
```python
import re
pattern = r'\d+'
text = "There are 123 apples"
result = re.search(pattern, text)
```

**Example:**
```python
import re

# Example of regular expressions
pattern = r'\b\w{4}\b'
text = "This is a test sentence with four-letter words."

matches = re.findall(pattern, text)
print(matches)
```

**Exercise:**
1. Write a regular expression to find all email addresses in a given text.
2. Create a regular expression to validate phone numbers in the format (123) 456-7890.

**Resources:**
- [Python Documentation: re module](https://docs.python.org/3/library/re.html)
- [Real Python: Regular Expressions](https://realpython.com/regex-python/)

---

## 10. Database Connectivity

**Description:**
Connect to databases and execute SQL queries using Python. <br>
> Database connectivity in Python is commonly achieved using libraries like `sqlite3` for SQLite databases, `psycopg2` for PostgreSQL, and `MySQLdb` for MySQL. These libraries provide functions to connect to a database, execute SQL queries, and fetch results.

**Syntax:**
```python
import sqlite3

# Connecting to a database
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Creating a table
cursor.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

# Inserting data
cursor.execute('''INSERT INTO users (name, age) VALUES ('Alice', 30)''')

# Querying data
cursor.execute('''SELECT * FROM users''')
print(cursor.fetchall())

# Closing the connection
conn.close()
```

**Example:**
```python
import sqlite3

# Example of database operations
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Creating a table
cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

# Inserting data
cursor.execute('''INSERT INTO users (name, age) VALUES ('Alice', 30)''')
cursor.execute('''INSERT INTO users (name, age) VALUES ('Bob', 25)''')

# Querying data
cursor.execute('''SELECT * FROM users''')
print(cursor.fetchall())

# Closing the connection
conn.close()
```

**Exercise:**
1. Create a database for a library system with tables for books, authors, and loans. Insert sample data and write queries to fetch information about books and authors.

**Resources:**
- [Python Documentation: sqlite3 module](https://docs.python.org/3/library/sqlite3.html)
- [Real Python: SQLite Databases](https://realpython.com/python-sqlite-sqlalchemy/)

---

## 11. Web Scraping

**Description:**
Extract data from web pages using Python libraries like BeautifulSoup and requests. <br>
> Web scraping involves fetching a web page's content and extracting useful information from it. The `requests` library is used to send HTTP requests, and `BeautifulSoup` is used to parse HTML and XML documents.

**Syntax:**
```python
import requests
from bs4 import BeautifulSoup

# Fetching a web page
response = requests.get('https://example.com')
soup = BeautifulSoup(response.content, 'html.parser')

# Extracting data
title = soup.title.text
print(title)
```

**Example:**
```python
import requests
from bs4 import BeautifulSoup

# Example of web scraping
url = 'https://example.com'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Extracting data
title = soup.title.text
print(f"Title: {title}")

# Finding all links
links = soup.find_all('a')
for link in links:
    print(link.get('href'))
```

**Exercise:**
1. Write a web scraper that extracts and prints the headlines from a news website.
2. Create a script that scrapes product names and prices from an e-commerce site.

**Resources:**
- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Real Python: Web Scraping with BeautifulSoup](https://realpython.com/beautiful-soup-web-scraper-python/)

---

## 12. GUI Programming

**Description:**
Create graphical user interfaces using Python libraries like Tkinter. <br>
> GUI programming in Python can be done using libraries such as Tkinter, PyQt, and Kivy. Tkinter is included with Python and provides a simple way to create windows, dialogs, and other GUI elements.

**Syntax:**
```python
import tkinter as tk

# Creating a window
window = tk.Tk()
window.title("My GUI App")

# Adding a label
label = tk.Label(window, text="Hello, World!")
label.pack()

# Running the application
window.mainloop()
```

**Example:**
```python
import tkinter as tk

# Example of a simple GUI application
def on_button_click():
    label.config(text="Button clicked!")

# Creating a window
window = tk.Tk()
window.title("Simple GUI")

# Adding a label
label = tk.Label(window, text="Hello, World!")
label.pack()

# Adding a button
button = tk.Button(window, text="Click Me", command=on_button_click)
button.pack()

# Running the application
window.mainloop()
```

**Exercise:**
1. Create a GUI application with a text entry field, a button, and a label. When the button is clicked, display the text from the entry field in the label.
2. Create a simple calculator GUI with buttons for digits and basic arithmetic operations.

**Resources:**
- [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)
- [Real Python: Python GUI Programming with Tkinter](https://realpython.com/python-gui-tkinter/)

---

## 13. Multithreading and Multiprocessing

**Description:**
Perform concurrent execution of code using threading and multiprocessing. <br>
> Multithreading and multiprocessing allow you to execute code concurrently, making your programs more efficient. The `threading` module provides a way to create and manage threads, while the `multiprocessing` module allows you to create processes.

### Multithreading

**Syntax:**
```python
import threading

def print_numbers():
    for i in range(5):
        print(i)

# Creating a thread
thread = threading.Thread(target=print_numbers)
thread.start()
thread.join()
```

**Example:**
```python
import threading

# Example of multithreading
def print_numbers():
    for i in range(5):
        print(f"Thread 1: {i}")

def print_letters():
    for letter in 'abcde':
        print(f"Thread 2: {letter}")

thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
```

**Exercise:**
1. Write a program that creates two threads: one that prints even numbers and another that prints odd numbers up to 10.

**Resources:**
- [Python Documentation: threading module](https://docs.python.org/3/library/threading.html)
- [Real Python: Python Threading](https://realpython.com/intro-to-python-threading/)

### Multiprocessing

**Syntax:**
```python
import multiprocessing

def print_numbers():
    for i in range(5):
        print(i)

# Creating a process
process = multiprocessing.Process(target=print_numbers)
process.start()
process.join()
```

**Example:**
```python
import multiprocessing

# Example of multiprocessing
def print_numbers():
    for i in range(5):
        print(f"Process 1: {i}")

def print_letters():
    for letter in 'abcde':
        print(f"Process 2: {letter}")

process1 = multiprocessing.Process(target=print_numbers)
process2 = multiprocessing.Process(target=print_letters)

process1.start()
process2.start()

process1.join()
process2.join()
```

**Exercise:**
1. Write a program that creates two processes: one that prints the squares of numbers and another that prints the cubes of numbers up to 5.

**Resources:**
- [Python Documentation: multiprocessing module](https://docs.python.org/3/library/multiprocessing.html)
- [Real Python: Python Multiprocessing](https://realpython.com/python-multiprocessing/)

---

## 14. Networking

**Description:**
Perform network-related tasks like creating servers and clients using Python. <br>
> Networking in Python can be done using the `socket` module, which provides low-level networking interfaces. You can create servers and clients that communicate over TCP or UDP protocols.

**Syntax:**
```python
import socket

# Creating a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 8080))
s.listen()

# Accepting a connection
conn, addr = s.accept()
print(f"Connected by {addr}")

# Receiving data
data = conn.recv(1024)
print(f"Received: {data}")

# Closing the connection
conn.close()
```

**Example:**
```python
import socket

# Example of a simple server
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8080))
    server_socket.listen(1)
    print("Server is listening on port 8080...")

    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(f"Received: {data.decode()}")
        conn.sendall(data)

    conn.close()

# Example of a Simple Client

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 8080))
    
    message = "Hello, Server!"
    client_socket.sendall(message.encode())
    
    data = client_socket.recv(1024)
    print(f"Received: {data.decode()}")
    
    client_socket.close()

# Run the server in one script or terminal
# start_server()

# Run the client in another script or terminal
# start_client()
```

**Exercise:**
1. Create a server that accepts multiple clients and echoes back messages sent by the clients.
2. Implement a simple chat application where multiple clients can connect to a server and send messages to each other.

**Resources:**
- [Python Documentation: socket module](https://docs.python.org/3/library/socket.html)
- [Real Python: Python Socket Programming](https://realpython.com/python-sockets/)

---

## 15. Testing

**Description:**
Write and run tests to ensure your code works as expected using libraries like `unittest` and `pytest`. <br>
> Testing is crucial for ensuring the reliability and correctness of your code. The `unittest` module is built into Python and provides a framework for writing and running tests. `pytest` is a third-party testing framework that offers more features and better readability.

### unittest

**Syntax:**
```python
import unittest

class TestMathOperations(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(1 + 1, 2)

    def test_subtraction(self):
        self.assertEqual(2 - 1, 1)

if __name__ == '__main__':
    unittest.main()
```

**Example:**
```python
import unittest

# Example of unittest
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(2, 1), 1)
        self.assertEqual(subtract(1, 1), 0)

if __name__ == '__main__':
    unittest.main()
```

### pytest

**Syntax:**
```python
# test_math_operations.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(2, 1) == 1
    assert subtract(1, 1) == 0

# Run the tests with the command: pytest test_math_operations.py
```

**Example:**
```python
# Example of pytest
def multiply(a, b):
    return a * b

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 5) == -5
```

**Exercise:**
1. Write unit tests for a function that calculates the factorial of a number using both `unittest` and `pytest`.
2. Create a test suite for a simple calculator application that includes addition, subtraction, multiplication, and division functions.

**Resources:**
- [Python Documentation: unittest module](https://docs.python.org/3/library/unittest.html)
- [Real Python: Testing Your Code](https://realpython.com/python-testing/)
- [pytest Documentation](https://docs.pytest.org/en/stable/)

---

## 16. Best Practices and Coding Style

### Description

This guide outlines the best practices and coding style conventions for Python development. Adhering to these principles ensures code readability, maintainability, and consistency across projects.

### Contents

> 1. [PEP 8 – Style Guide for Python Code](#pep-8-style-guide-for-python-code)
> 2. [Naming Conventions](#naming-conventions)
> 3. [Code Layout](#code-layout)
> 4. [Comments](#comments)
> 5. [Docstrings](#docstrings)
> 6. [Imports](#imports)
> 7. [Whitespace in Expressions and Statements](#whitespace-in-expressions-and-statements)
> 8. [Programming Recommendations](#programming-recommendations)

### 1. PEP 8 – Style Guide for Python Code

PEP 8 is the de facto code style guide for Python. It provides guidelines on how to write clean and readable Python code.

### 2. Naming Conventions

#### Variables

- Use `snake_case` for variable names.
- Example:
  ```python
  user_name = "Alice"
  total_count = 42
  ```

#### Functions

- Use `snake_case` for function names.
- Example:
  ```python
  def calculate_total(price, tax):
      return price + tax
  ```

#### Classes

- Use `CamelCase` for class names.
- Example:
  ```python
  class DataProcessor:
      def __init__(self, data):
          self.data = data
  ```

#### Constants

- Use `UPPER_CASE` for constant names.
- Example:
  ```python
  MAX_CONNECTIONS = 100
  TIMEOUT_DURATION = 30
  ```

### 3. Code Layout

#### Indentation

- Use 4 spaces per indentation level.
- Example:
  ```python
  def process_data(data):
      for item in data:
          print(item)
  ```

#### Maximum Line Length

- Limit all lines to a maximum of 79 characters.
- Example:
  ```python
  def fetch_data_from_server(server_url, timeout=30):
      # Implementation goes here
      pass
  ```

#### Blank Lines

- Separate top-level function and class definitions with two blank lines.
- Method definitions inside a class are separated by a single blank line.
- Example:
  ```python
  class MyClass:
      
      def method_one(self):
          pass
      
      def method_two(self):
          pass
  ```

### 4. Comments

- Use comments to explain code.
- Use `#` for inline comments and block comments.
- Keep comments up-to-date with the code.
- Example:
  ```python
  # This function calculates the total price
  def calculate_total(price, tax):
      return price + tax  # Add tax to the price
  ```

### 5. Docstrings

- Use docstrings to describe all public modules, functions, classes, and methods.
- Use triple quotes for docstrings.
- Example:
  ```python
  def fetch_data(url):
      """
      Fetch data from the specified URL.
      
      Parameters:
          url (str): The URL to fetch data from.
          
      Returns:
          dict: The data fetched from the URL.
      """
      pass
  ```

### 6. Imports

- Import standard libraries first, then third-party libraries, and local modules last.
- Use absolute imports.
- Avoid wildcard imports.
- Example:
  ```python
  import os
  import sys
  
  import requests
  
  from my_module import my_function
  ```

### 7. Whitespace in Expressions and Statements

- Avoid extraneous whitespace.
- Example:
  ```python
  # Correct:
  spam(ham[1], {eggs: 2})
  
  # Wrong:
  spam( ham[ 1 ], { eggs: 2 } )
  ```

### 8. Programming Recommendations

- Use `is` for comparison to `None`.
- Example:
  ```python
  if variable is None:
      pass
  ```

- Use `startswith()` and `endswith()` for string comparisons.
- Example:
  ```python
  if filename.startswith('file_'):
      pass
  ```

- Use list comprehensions for simple loops.
- Example:
  ```python
  squares = [x**2 for x in range(10)]
  ```

- Handle exceptions properly.
- Example:
  ```python
  try:
      result = 10 / 0
  except ZeroDivisionError:
      result = None
  ```

## References

- [Python Official Documentation](https://docs.python.org/3/)
- [Real Python](https://realpython.com/)
- [Learn Python the Hard Way](https://learnpythonthehardway.org/)
- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)
- [PEP 8 – Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
- [The Zen of Python](https://www.python.org/dev/peps/pep-0020/)
