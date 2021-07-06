#List example
from typing import List


MyList = ["apple", "banana", "cherry"]
print(MyList)

"""
List items are ordere, changeable, and allow duplicate values.
List items are indexed, the first item has index [0], the second item has index [1] etc.

When you add new items to a list, the new items will be placed at the end of the list.
"""
MyList = ["apple", "banana", "cherry", "apple", "cherry"]
print(MyList)

#List lenght, to determine how many items a list have
print(len(MyList))

#List items can be of any data type
list1 = ["apple", "banana", "cherry"]
list2 = [1, 2, 3, 4, 5]
list3 = [True, False, False]

#List can contain different data types
MixList = ["abc", 123, True, True, 40, "Banana"]
print(type(MixList))

#We can create lists by using lists()
NewList = list(("apple", "banana", "cherry"))
print(NewList)

#There are 4 collection data types in the python programming language
"""
List            is a collection which is ordered and changeable. Allows duplicate members.
Tuple           is a collection which is ordered and unchangeable. Allows duplicate members.
Set             is a collection which is unordered and unindexed. No duplicate members.
Dictionary      is a collection which is ordered* and changeable. No duplicate members.
"""

#Access items in the list
MyNewList = ["Chris", "Joy", "Jesse"]
print(MyNewList[1])

#Print the last item of the list
print(MyNewList[-1])

#Range of indexes (The search will start at index 2 (included) and end at index 5 (not included))
IndexRange = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(IndexRange[2:5])
print(IndexRange[:5])
print(IndexRange[2:])
#This example returns the items from "orange" (-4) to, but NOT including "mango" (-1)
print(IndexRange[-4:-1])
#Check if item exists
if "apple" in IndexRange:
    print("Yes, 'apple' is in the fruits list")

#Change the second item
ThisList = ["apple", "banana", "cherry"]
ThisList[1] = "blackberry"
print(ThisList)

#Change a range of item values
ThisList = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
ThisList[1:3] = ["blackcurrant", "watermelon"]
print(ThisList)
#If you insert more items than you replace, the new items will be inserted where specified, and the remining items will move accordingly
#The lenght of the list will change when the number of items inserted does not match the number of items replaced
ThisList[1:2] = ["cherry", "strawberry"]
print(ThisList) 
#If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly
ThisList[1:3] = ["coconut"]
print(ThisList)

#To insert net list item, we can use insert()
FruitsList = ["apple", "banana", "cherry"]
print(FruitsList)
FruitsList.insert(2, "watermelon")
print(FruitsList)

#To add an item to the end of the list we use append()
FruitsList.append("orange")
print(FruitsList)

#To insert a list item at a specified index
FruitsList.insert(1, "pineapple")
print(FruitsList)

#Extend list, use extend(), the elements will be added to the end of the list
#The extend method does not have to append lists, you can add any iterable object (tuple, sets, dictionaries etc)
list1 = ["apple", "orange", "banana"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)

#To remove specified item from list use remove()
list1.remove(2)
print(list1)

#To remove specified index use pop(), if you dont specify the index pop() will remove the last item from the list
list1.pop(1)
print(list1)

#the del keyword also removes the specified index
del list1[1]
print(list1)

#To delete all the indexes we can use clear() method
list1.clear()
print(list1)

#To have a loop in python we can use "for"
list1 = ["apple", "orange", "banana"]
list2 = ["strawberry", "coconut", "cranberries"]
list1.extend(list2)
for x in list1:
    print(x)

#You can also loop through the list items by reffering to their index number
#User the range() and len() functinos to create a suitable iterable
for i in range(len(list1)):
    print(list1[i])

#While loop
i = 0
while i < len(list1):
    print(list1[i])
    i += 1

"""
The Syntax
newlist = [expression for item in iterable if condition == True]
"""

#Looping using list comprehension, this is the shortest way for looping intems in a list
[print(x) for x in list1]
ListWithA = [x for x in list1 if "a" in x]
print(ListWithA)
ListWithoutApple = [x for x in list1 if x != "apple"]
print(ListWithoutApple)

#The iterable can be any iterable object, like a list, tuple, set etc.
#You can use the range() function to create an iterable
List10 = [x for x in range(10)]
print(List10)

#Exact same example above but with condition
ListCondition = [x for x in range(10) if x < 5]
print(ListCondition)

#The expression can be manipulated before it end up like a list item
ListManipulate = [x.upper() for x in ListWithoutApple]
print(ListManipulate)
ListHello = ["Hello" for x in ListWithoutApple]
print(ListHello)

#The expressions can also contain conditions, not like a filter, but as a way to manipulate the outcome
#Return the item if it is not banana, if it is banana return orange
ListIf = [x if x != "banana" else "orange" for x in ListWithoutApple]
print(ListIf)

#Sort list alphanumerically
list1.sort()
print(list1)

#Sort descending
list1.sort(reverse = True)
print(list1)

#By default sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters.
#Here is the example of case insensitive sort
ListCase = ["banana", "Orange", "Kiwi", "cherry"]
ListCase.sort()
print(ListCase)
ListCase.sort(key = str.lower)
print(ListCase)

#Copy lists using builtin copy() method
"""
You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1,
and changes made in list1 will automatically also be made in list2.
There are ways to make a copy, one way is to use the built-in List method copy().
"""
CopyList = list1.copy()
print(CopyList)

#Copy list using list() method
CopyOfCopy = list(CopyList)
print(CopyOfCopy)

#Join lists using + operator
List1 = ["a", "b", "c"]
List2 = [1, 2, 3]
List3 = List1 + List2
print(List3)

#Joint lists by appending all the items from List2 to List1 one by one
for x in List2:
    List1.append(x)
print(List1)

#Joint lists by using extend() method to add List2 at the end of List1
List1.extend(List2)
print(List1)

# List Methods
"""
Method 	        Description
append()	    Adds an element at the end of the list
clear()	        Removes all the elements from the list
copy()	        Returns a copy of the list
count()	        Returns the number of elements with the specified value
extend()	    Add the elements of a list (or any iterable), to the end of the current list
index()	        Returns the index of the first element with the specified value
insert()	    Adds an element at the specified position
pop()	        Removes the element at the specified position
remove()	    Removes the item with the specified value
reverse()	    Reverses the order of the list
sort()	        Sorts the list
"""

