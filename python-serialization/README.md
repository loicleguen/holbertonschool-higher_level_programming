<div align="center"><img src="https://github.com/ksyv/holbertonschool-web_front_end/blob/main/baniere_holberton.png"></div>

# Python - Serialization

## Table of Contents :

  - [0. Basic Serialization](#subparagraph0)
  - [1. Pickling Custom Classes](#subparagraph1)
  - [2. Converting CSV Data to JSON Format](#subparagraph2)
  - [3. Serializing and Deserializing with XML](#subparagraph3)

## Task
### 0. Basic Serialization <a name='subparagraph0'></a>

Create a basic serialization module that adds the functionality to serialize a Python dictionary to a JSON file and deserialize the JSON file to recreate the Python Dictionary.

Write a Python module named <code>task_00_basic_serialization.py</code> with the following functions:

```
def serialize_and_save_to_file(data, filename):
    # Your code here to serialize and save data to the specified file
    pass

def load_and_deserialize(filename):
    # Your code here to load and deserialize data from the specified file
    pass
```

The function <code>serialize_and_save_to_file</code> take 2 parameters:

* <code>data</code>: A Python Dictionary with data
* <code>filename</code>: The filename of the output JSON file.
If the output file already exists it should be replaced.

The function <code>load_and_deserialize</code> take 1 <code>parameters</code>:

* <code>filename</code>: The filename of the input JSON file
This function returns a Python Dictionary with the deseialized JSON data from the file.

```
#!/usr/bin/env python3
from task_00_basic_serialization import load_and_deserialize, serialize_and_save_to_file

# Sample data to be serialized
data_to_serialize = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

# Serialize the data to JSON and save it to a file
serialize_and_save_to_file(data_to_serialize, 'data.json')

# Output: The data has been serialized and saved to 'data.json'
print("Data serialized and saved to 'data.json'.")

# Load and deserialize data from 'data.json'
deserialized_data = load_and_deserialize('data.json')

# Output: The deserialized data
print("Deserialized Data:")
print(deserialized_data)
```

```
Data serialized and saved to 'data.json'.
Deserialized Data:
{'name': 'John Doe', 'age': 30, 'city': 'New York'}
```

---

### 1. Pickling Custom Classes <a name='subparagraph1'></a>

Learn how to serialize and deserialize custom Python objects using the <code>pickle</code> module.

1 - Create a custom Python class named <code>CustomObject</code>. This class should have the following attributes:

* <code>name</code> (a string)
* <code>age</code> (an integer)
* <code>is_student</code> (a boolean)

Additionally, the class should have a method <code>display</code> method to print out the object’s attributes with the following format:

```
Name: John
Age: 25
Is Student: True
```

2 - Implement two methods within this class:

* <code>serialize(self, filename)</code>: This method will take a filename as its parameter. Using the <code>pickle</code> module, it will serialize the current instance of the object and save it to the provided filename.
* <code>@classmethod</code>
<code>deserialize(cls, filename)</code>: This class method will take a filename as its parameter. Using the <code>pickle</code> module, it will load and return an instance of the <code>CustomObject</code> from the provided filename.

3 - Save your code in a file named <code>task_01_pickle.py</code>.

```
#!/usr/bin/env python3
from task_01_pickle import CustomObject

# Create an instance of CustomObject
obj = CustomObject(name="John", age=25, is_student=True)
print("Original Object:")
obj.display()

# Serialize the object
obj.serialize("object.pkl")

# Deserialize the object into a new instance
new_obj = CustomObject.deserialize("object.pkl")
print("\nDeserialized Object:")
new_obj.display()
```

Output:

```
Original Object:
Name: John
Age: 25
Is Student: True

Deserialized Object:
Name: John
Age: 25
Is Student: True
```

---

### 2. Converting CSV Data to JSON Format <a name='subparagraph2'></a>

The objective of this exercise is to gain experience in reading data from one format (CSV) and converting it into another format (JSON) using serialization techniques.

```
#!/usr/bin/env python3
from task_02_csv import convert_csv_to_json

csv_file = "data.csv"
convert_csv_to_json(csv_file)
print(f"Data from {csv_file} has been converted to data.json")
```

```
$ python3 main_02_csv.py 
Data from data.csv has been converted to data.json
```

```
name,age,city
John,28,New York
Alice,24,Los Angeles
Bob,22,Chicago
Eve,30,San Francisco
```

After the conversion, the resulting <code>data.json</code> file should contain:

```
[
    {"name": "John", "age": "28", "city": "New York"},
    {"name": "Alice", "age": "24", "city": "Los Angeles"},
    {"name": "Bob", "age": "22", "city": "Chicago"},
    {"name": "Eve", "age": "30", "city": "San Francisco"}
]
```

---

### 3. Serializing and Deserializing with XML <a name='subparagraph3'></a>

In this exercise we’ll explore serialization and deserialization using XML as an alternative format to JSON.

```
import xml.etree.ElementTree as ET
```

* <p><code>serialize_to_xml(dictionary, filename)</code>: This will take a Python dictionary and a filename as parameters. It should serialize the dictionary into XML and save it to the given filename.</p>
* <p><code>deserialize_from_xml(filename)</code>: This will take a filename as its parameter, read the XML data from that file, and return a deserialized Python dictionary.</p>

* Create a root element, e.g., <code>&lt;data&gt;</code>.
* Iterate through the dictionary items and add them as child elements to the root.
* Write the XML tree to the provided filename using the <code>ET.ElementTree</code> class.

* Parse the XML file using <code>ET.parse</code>.
* Navigate through the XML elements to reconstruct the dictionary.
* Return the constructed dictionary.

```
#!/usr/bin/env python3
from task_03_xml import serialize_to_xml, deserialize_from_xml

def main():
    sample_dict = {
        'name': 'John',
        'age': '28',
        'city': 'New York'
    }

    xml_file = "data.xml"
    serialize_to_xml(sample_dict, xml_file)
    print(f"Dictionary serialized to {xml_file}")

    deserialized_data = deserialize_from_xml(xml_file)
    print("\nDeserialized Data:")
    print(deserialized_data)

if __name__ == "__main__":
    main()
```

```
Dictionary serialized to data.xml

Deserialized Data:
{'name': 'John', 'age': '28', 'city': 'New York'}
```

data.xml

```
<data>
    <name>John</name>
    <age>28</age>
    <city>New York</city>
</data>
```

---


## Authors
loicleguen - [GitHub Profile](https://github.com/loicleguen)
