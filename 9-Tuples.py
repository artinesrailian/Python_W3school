#Tuple in python
from typing import FrozenSet


Tuple1 = ("apple", "banana", "cherry", "apple", "apple", "strawberry")
print(Tuple1)

#Tuple items are ordered, unchangeable, and allow duplicate values
print(len(Tuple1))

#To create a tuple with 1 item you have to add a comma after the item, otherwise python will not recognize it as a tuple
OneItemTuple = ("apple",)
print(type(OneItemTuple))
#Not a tuple, this is a string
OneItemTuple = ("apple")
print(type(OneItemTuple))

#Tuple items can be of any data type
Tuple1 = ("apple", "cherry", "banana")
Tuple2 = (1, 2, 3)
Tuple3 = (True, False, True, True)

#Tuple can contain different data types
Tuple1 = ("abc", 34, True, "male")

#To create tuple we can use tuple() constructor
ThisTuple = tuple(("apple", "banana", "cherry"))
print(ThisTuple)

#To access tuple items we can use the index number
print(Tuple1[1])

#All accessing methods for the Lists also apply to tuples, like reverse indexing, selecting index range and etc

#Change tuple value
"""
Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
"""
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
print(type(x))

#Append tuple
"""
Since tuples are immutable, they do not have a build-in append() method, but there are other ways to add items to a tuple.
1. Convert into a list: Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple.
"""
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
"""
2. Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:
"""
y = ("orange",)
thistuple += y
print(thistuple)

#Remove item from tuple
"""
Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items:
"""
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

#To delete tuple comletely we can use del
del thistuple

#Unpacking tuple
#When we create a tuple, we normally assign values to it, this is called "packing" a tuple
#In python we are also allowed to extract the values back into variables, this is called "unpacking"
Fruits = ("apple", "banana", "cherry")
(x, y, z) = Fruits
print(x)
print(y)
print(z)

#Using *
Fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = Fruits
print(green)
print(yellow)
print(red)

#If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.
Fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = Fruits
print(green)
print(tropic)
print(red)

#Loops are like the ones in the lists we can use for, while, using index numbers, using len(), range() and etc

#To join two or more tuples you can use the + operator
Tuple1 = ("a", "b", "c")
Tuple2 = (1, 2, 3)
Tuple3 = Tuple1 + Tuple2
print(Tuple3)

#Multiply tuples
MultiplyTuples = Tuple2 * 3
print(MultiplyTuples)

#Tuple methods, Python has two built-in methods that can use on tuples
"""
Method 	        Description
count()	        Returns the number of times a specified value occurs in a tuple
index()	        Searches the tuple for a specified value and returns the position of where it was found
"""