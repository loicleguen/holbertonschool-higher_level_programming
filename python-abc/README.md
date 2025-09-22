<div align="center"><img src="https://github.com/ksyv/holbertonschool-web_front_end/blob/main/baniere_holberton.png"></div>

# Python OOP - Abtract Class, Interface, Subclassing

## Table of Contents :

  - [0. Abstract Animal Class and its Subclasses](#subparagraph0)
  - [1. Shapes, Interfaces, and Duck Typing](#subparagraph1)
  - [2. Extending the Python List with Notifications](#subparagraph2)
  - [3. CountedIterator - Keeping Track of Iteration](#subparagraph3)
  - [4. The Enigmatic FlyingFish - Exploring Multiple Inheritance](#subparagraph4)
  - [5. The Mystical Dragon - Mastering Mixins](#subparagraph5)

## Task
### 0. Abstract Animal Class and its Subclasses <a name='subparagraph0'></a>

In object-oriented programming, Abstract Base Classes (ABCs) ensure that derived classes implement specific methods from the base class. This provides a blueprint for creating and structuring derived classes. Python’s <code>ABC</code> package facilitates the creation of abstract base classes.

* Python <code>ABC</code> documentation: <a href="/rltoken/_0PgSum1lebIia7sFQmIbA" target="_blank" title="https://docs.python.org/3/library/abc.html">https://docs.python.org/3/library/abc.html</a>

<strong>Hints</strong>:

* The abstract method in the base class doesn’t have a body. You need to provide the implementation in the subclasses.
* If you try to instantiate a class that hasn’t implemented all of its abstract methods, Python will raise a <code>TypeError</code>.

```
$ cat main_00_abc.py 
#!/usr/bin/env python3
from task_00_abc import Animal, Dog, Cat

bobby = Dog()
garfield = Cat()

print(bobby.sound())
print(garfield.sound())

animal = Animal()
print(animal.sound())

$ ./main_00_abc.py 
Bark
Meow
Traceback (most recent call last):
  File "main_00_abc.py", line 10, in <module>
    animal = Animal()
TypeError: Can't instantiate abstract class Animal with abstract method sound
```

---

### 1. Shapes, Interfaces, and Duck Typing <a name='subparagraph1'></a>

Python employs a concept called “duck typing,” which is concerned with the semantics of objects rather than their inheritance hierarchy. If an object behaves like a duck (i.e., has all the methods and properties of a duck), then it’s considered a duck, regardless of its actual class. This concept allows for flexible and dynamic polymorphism.

In this exercise, we’ll use abstract base classes to design a blueprint for shapes and use duck typing to handle objects of different shapes uniformly.

* Python <code>ABC</code> documentation: <a href="/rltoken/_0PgSum1lebIia7sFQmIbA" target="_blank" title="https://docs.python.org/3/library/abc.html">https://docs.python.org/3/library/abc.html</a>
* Concept of Duck Typing: <a href="/rltoken/i3FBxu-VBtDf3LuXcT_82g" target="_blank" title="https://realpython.com/lessons/duck-typing/">https://realpython.com/lessons/duck-typing/</a>

<strong>Hints</strong>:

* While Python doesn’t enforce interfaces in the same way as statically-typed languages, abstract base classes provide a mechanism to ensure certain methods are implemented in subclasses.
* Duck typing in the <code>shape_info</code> function implies that you shouldn’t use <code>isinstance</code> checks. Instead, trust that the passed object adheres to the <code>Shape</code> interface.

```
$ cat main_01_duck_typing.py 
#!/usr/bin/env python3
from task_01_duck_typing import Circle, Rectangle, shape_info

circle = Circle(radius=5)
rectangle = Rectangle(width=4, height=7)

shape_info(circle)
shape_info(rectangle)

$ ./main_01_duck_typing.py 
Area: 78.53981633974483
Perimeter: 31.41592653589793
Area: 28
Perimeter: 22
```

---

### 2. Extending the Python List with Notifications <a name='subparagraph2'></a>

In Python, you can extend built-in classes to add or modify behavior. The <code>list</code> class provides a collection of methods and functionalities that handle list operations. By extending the <code>list</code> class, you can provide custom behaviors while retaining the original functionalities.

Create a class named <code>VerboseList</code> that extends the Python <code>list</code> class. This custom class should print a notification message every time an item is added (using the <code>append</code> or <code>extend</code> methods) or removed (using the <code>remove</code> or <code>pop</code> methods).

<strong>Hints</strong>:

* Remember to call the original method of the <code>list</code> class using the <code>super()</code> function to ensure that the original functionality is retained. For example, for <code>append</code>: <code>super().append(item)</code>.
* Think about edge cases, such as trying to remove an item that doesn’t exist in the list.

```
$ cat main_02_verboselist.py 
#!/usr/bin/env python3
from task_02_verboselist import VerboseList

vl = VerboseList([1, 2, 3])
vl.append(4)
vl.extend([5, 6])
vl.remove(2)
vl.pop()
vl.pop(0)

$ ./main_02_verboselist.py 
Added [4] to the list.
Extended the list with [2] items.
Removed [2] from the list.
Popped [6] from the list.
Popped [1] from the list.
```

---

### 3. CountedIterator - Keeping Track of Iteration <a name='subparagraph3'></a>

Subclassing allows a new class to inherit properties and methods from an existing class. In Python, many built-in classes can be extended to customize or enhance their behavior. The <code>iter</code> function, which returns an iterator object, provides the <code>__next__</code> method to fetch the next item in the sequence. This exercise focuses on extending the functionality of this iterator object.

Create a class named <code>CountedIterator</code> that extends the built-in iterator obtained from the <code>iter</code> function. The <code>CountedIterator</code> should keep track of the number of items that have been iterated over. Specifically, you will need to override the <code>__next__</code> method to increment a counter each time an item is fetched.

<strong>Hints</strong>:

* Remember that the <code>__next__</code> method should raise a <code>StopIteration</code> exception when there are no more items to iterate, so ensure this behavior is retained in your overridden method.
* You can initialize the iterator object in the <code>CountedIterator</code> constructor using: <code>self.iterator = iter(some_iterable)</code>.

```
$ cat main_03_countediterator.py 
#!/usr/bin/env python3
from task_03_countediterator import CountedIterator

data = [1, 2, 3, 4]
counted_iter = CountedIterator(data)

try:
    while True:
        item = next(counted_iter)
        print(f"Got {item}, total {counted_iter.get_count()} items iterated.")
except StopIteration:
    print("No more items.")

$ ./main_03_countediterator.py 
Got 1, total 1 items iterated.
Got 2, total 2 items iterated.
Got 3, total 3 items iterated.
Got 4, total 4 items iterated.
No more items.
```

---

### 4. The Enigmatic FlyingFish - Exploring Multiple Inheritance <a name='subparagraph4'></a>

In some object-oriented languages, a class can inherit attributes and behaviors from more than one parent class. This is known as multiple inheritance. Python is one of the languages that supports multiple inheritance, which can be a powerful tool, but it also comes with complexities, particularly regarding method resolution order (MRO).

Construct a <code>FlyingFish</code> class that inherits from both a <code>Fish</code> class and a <code>Bird</code> class. Within <code>FlyingFish</code>, override methods from both parents. The goal is to comprehend multiple inheritance and how Python determines method resolution order.

<strong>Hints</strong>:

* Consider the order in which you list the parent classes when defining <code>FlyingFish</code>. It affects the method resolution order.
* While multiple inheritance can be a powerful tool, it should be used judiciously, as it can make the code more complex and harder to read.

```
$ cat main_04_flyingfish.py 
#!/usr/bin/env python3
from task_04_flyingfish import Fish, FlyingFish

flying_fish = FlyingFish()
flying_fish.swim()
flying_fish.fly()
flying_fish.habitat()

$ ./main_04_flyingfish.py 
The flying fish is swimming!
The flying fish is soaring!
The flying fish lives both in water and the sky!
```

---

### 5. The Mystical Dragon - Mastering Mixins <a name='subparagraph5'></a>

Mixins are a way to add functionality to classes in a modular fashion. They’re not meant to stand alone but are meant to be combined with other classes to add behaviors. By using mixins, you can compose behaviors in classes without the need for deep or rigid inheritance hierarchies.

Design two mixin classes, <code>SwimMixin</code> and <code>FlyMixin</code>, each equipped with methods <code>swim</code> and <code>fly</code> respectively. Next, construct a class <code>Dragon</code> that inherits from both these mixins. Your aim is to show that a <code>Dragon</code> instance can both swim and fly.

<strong>Hints</strong>:

* While designing mixins, remember that they should be focused, providing a single piece of functionality. They shouldn’t be overly broad or try to manage too much behavior.
* Mixins allow for code reusability and can be combined in various ways to give objects different capabilities without setting up complex inheritance hierarchies.

```
$ cat main_05_dragon.py 
#!/usr/bin/env python3
from task_05_dragon import Dragon

dragon = Dragon()
dragon.swim()  # Outputs: The creature swims!
dragon.fly()   # Outputs: The creature flies!
dragon.roar()  # Outputs: The dragon roars!

$ ./main_05_dragon.py 
The creature swims!
The creature flies!
The dragon roars!
```

---


## Authors
loicleguen - [GitHub Profile](https://github.com/loicleguen)
