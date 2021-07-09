#Python has a built-in package called json, which can be used to work with JSON data
import json

#If you have a JSON string, you can parse it by using the json.loads() method

#Some JSON
x = '{ "name":"John", "age":30, "city":"New York" }'

#Parse x
#The result is a Python dictionary
y = json.loads(x)
print(y)
print(type(y))

#If you have a Python object, you can convert it into a JSON string by using the json.dumps() method

# a python object (dict)
x = {
    "name": "Rocky",
    "age": 20,
    "city": "Amsterdam"
}

#Convert into JSON
y = json.dumps(x)
print(y)
#The output is a JSON string
print(type(y))


#You can convert Python objects of the following types, into JSON strings
"""
dict
list
tuple
string
int
float
True
False
None
"""

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))


#When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent
"""
Python 	    JSON
dict 	    Object
list 	    Array
tuple 	    Array
str 	    String
int 	    Number
float 	    Number
True 	    true
False 	    false
None 	    null
"""

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))


#The example above prints a JSON string, but it is not very easy to read, with no indentations and line breaks
print(json.dumps(x, indent=4))

#You can also define the separators, default value is (", ", ": "),
#which means using a comma and a space to separate each object, and a colon and a space to separate keys from values
print(json.dumps(x, indent=4, separators=(". ", " = ")))

#The json.dumps() method has parameters to order the keys in the result
print(json.dumps(x, indent=4, sort_keys=True))