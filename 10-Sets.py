#Sets in python
MySet = {"apple", "banana", "cherry"}
print(MySet)

#Set items are unordered, unchangeable, and do not allow duplicate values.
ThisSet = {"apple", "banana", "cherry", "apple"}
print(ThisSet)

#Get the lenght of the set
print(len(ThisSet))

#Set Items can be of any type
#A set can contain different data types
print(type(ThisSet))

#We can create set by using set() constructor
ThisSet = set(("apple", "banana", "cherry"))
print(ThisSet)

#You cannot access items in set by referring to an index or a key as set is unordered

#You can loop through the set items using for and you can us in keyword to search an item in set
for x in ThisSet:
    print(x)

#Once a set is created you can't change its items, but you can add new items using add()
ThisSet.add("orange")
print(ThisSet)

#To add items from another set into the current set, use the update() method
TropicalSet = {"pineapple", "mango", "papaya"}
ThisSet.update(TropicalSet)
print(ThisSet)

#The object in the update() method does not have to be a set, it can be any iterable object(tuples, lists, dictionaries, etc)
MyList = ["kiwi", "orange"]
ThisSet.update(MyList)
print(ThisSet)

#To remove an item in a set, use remove() or discard() method, if the item to remove does not exist, discard() method will NOT raise an error
ThisSet.remove("kiwi")
print(ThisSet)
ThisSet.discard("pineapple")
print(ThisSet)

#You cas use pop() method to remove the last item, remember that sets are unordered so you will not know what item is going to be removed
x = ThisSet.pop()
print(x)
print(ThisSet)

#We can use clear() method to clear the whole set and we can use delete() method to delte set completely
ThisSet.clear()
print(ThisSet)
del ThisSet

#You can loop through the set items by using for loop
ThisSet = {"apple", "banana", "cherry"}
for x in ThisSet:
    print(x)

#Join sets
"""
There are several ways to join two or more sets in Python.
You can use the union() method that returns a new set containing all items from both sets,
or the update() method that inserts all the items from one set into another
"""
Set1 = {"a", "b" , "c"}
Set2 = {1, 2, 3}
Set3 = Set1.union(Set2)
print(Set3)

#The update() method inserts the items in set2 into set1:
Set1 = {"a", "b" , "c"}
Set2 = {1, 2, 3}
Set1.update(Set2)
print(Set1)

#Both union() and update() will exclude any duplicate items.

#The intersection_update() method will keep only the items that are present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

#The intersection() method will return a new set, that only contains the items that are present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)

#The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

#The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)

#Python set methods
"""
Method 	                            Description
add()	                            Adds an element to the set
clear()	                            Removes all the elements from the set
copy()	                            Returns a copy of the set
difference()	                    Returns a set containing the difference between two or more sets
difference_update()	                Removes the items in this set that are also included in another, specified set
discard()	                        Remove the specified item
intersection()	                    Returns a set, that is the intersection of two other sets
intersection_update()	            Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	                    Returns whether two sets have a intersection or not
issubset()	                        Returns whether another set contains this set or not
issuperset()	                    Returns whether this set contains another set or not
pop()	                            Removes an element from the set
remove()	                        Removes the specified element
symmetric_difference()	            Returns a set with the symmetric differences of two sets
symmetric_difference_update()	    inserts the symmetric differences from this set and another
union()	                            Return a set containing the union of sets
update()	                        Update the set with the union of this set and others
"""