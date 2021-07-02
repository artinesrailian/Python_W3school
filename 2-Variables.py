#This is another example of creating and using variables
x = 5           #x is of type int
y = "Artin"     #y is of type str
print(x)
print(y)

#To specify the data type we can use
x = str(3)      # x will be "3"
y = int(3)      # y will be "3"
z = float(3)    # z will be "3.0"

#To get the type of a variable we can use
x = 5
y = "Artin"
print(type(x))
print(type(y))

"""
Variables are case sensitive in Python
These two variables (a and A) have two separate values
"""
a = 4
A = "Artin"

#Camel case varibale
myVariableName = "Artin"

#Pascal case variable
MyVaribaleName = "Artin"

#Snake case varibale
my_varibale_name = "Artin"

#Assign multiple variables at a time
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#Assign a variable to multiple variable at once
x = y = z = "Orange"
print(x)
print(y)
print(z)

#Unpacking collections into separate variables
fruits = ["apple", "orange", "banana"]
x, y, z = fruits
print(x)
print(y)
print(z)
print(type(fruits))

#Combine strings example
language = "python"
print("My favorite programming language is " + language)

#Add two variables
state = "Awsome"
language = "Python"
text = state + language
print(text)

#Python uses + sign differently as the varibale type changes
x = 5
y = 10
print(x + y)

#Python can not combine int type with string

#All of the above variables are global variables

#Example of the global variable used in a function
x = "awsome"
def myfunc():
    # global x
    x = "fantastic"
    print("Python is " + x)

myfunc()

print("Python is " + x)

