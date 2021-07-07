#Create dictionary
ThisDict = {
    "brand": "Ford",
    "model": "Raptor",
    "year": 2013
}
print(ThisDict)
#A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
#As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

#Print a specific value
print(ThisDict["brand"])

#Dictionaries cannot have two items with the same key, duplicate values will overwrite existing values
NewDict = {
    "brand": "Ford",
    "model": "Raptor",
    "year": 2013,
    "year": 2021
}
print(NewDict)

#To determine how many items a dictionary has, use the len() function
print(len(NewDict))

#The values in dictionary items can be of any data type
NewDict = {
    "brand": "Ford",
    "model": "Raptor",
    "year": 2013,
    "colors": ["Red", "White", "Black", "Blue"]
}

#To access a dictionary item there are two ways, one is to call the key name, and the second one is to use get() method
x = NewDict["model"]
y = NewDict.get("brand")
print(x)
print(y)

#The key() method will return a list of all the keys in the dictionary
#The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list
keys = NewDict.keys()
print(keys)

#The values() method will return a list of all values in the dictionary
#The list of the values is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the values list
values = NewDict.values()
print(values)

#The items() method will return each item in a dictionary, as tuples in a list
#The returned list is a view of the items of the dictionary, meaning that any changes done to the dictionary will be reflected in the items list
items = NewDict.items()
print(items)

#To determine if a specified key is present in a dictionary use the in keyword
if "model" in NewDict:
    print("Yes, 'model', is one of the keys in the NewDict dictionary")

#Change values, you can change the value of a specific item by referring to its key name
NewDict["year"] = 2021
print(NewDict)

#The update() method will update the dictionary with the items from the given argument,
#the argument must be a dictionary or an iterable object with key:value pairs
NewDict.update({"model": "Mustang"})
print(NewDict)

#Adding an item to the dictionary is done by using a new index key and assigning a value to it
NewDict["engine"] = "V8"
print(NewDict)

#There are several method to remove items from a dictionary, the pop() method removes the item with the specified key name
NewDict.pop("engine")
print(NewDict)

#The popitem() method removes the last inserted item
NewDict.popitem()
print(NewDict)

#The del keyword removes the item with the specified key name
del NewDict["year"]
print(NewDict)

#The clear() method empties the dictionary
NewDict.clear()
print(NewDict)

#The del keyword can also delete the dictionary completely
del NewDict

#You can loop through a dictionary by using a for loop, when looping through a dictionary it only return the keys of the dictionary
NewDict = {
    "brand": "Ford",
    "model": "Raptor",
    "year": 2013,
    "colors": ["Red", "White", "Black", "Blue"]
}
for x in NewDict:
    print(x)

#Print all values in the dictionary one by one
for x in NewDict:
    print(NewDict[x])

#Copy dictionary
"""
You cannot copy a dictionary simply by typing dict2 = dict1,
because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2
"""
#Make a copy of a dictionary with the copy() method
CopyDict = NewDict
print(CopyDict)

#Another way to make a copy is to use the built-in fuction dict()
MyDict = dict(NewDict)
print(MyDict)

#A dictionary can contain dictionaries, this is called nested dictionaries
MyFamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}
print(MyFamily)

#If you want to add three dictionaries into a new dictionary
child1 = {
    "name": "Emil",
    "year": 2004
}
child2 = {
    "name": "Tobias",
    "year": 2007
}
child3 = {
    "name": "Linus",
    "year": 2011
}
NewFamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}
print(NewFamily)

#Dictionary Methods
"""
Method 	            Description
clear()	            Removes all the elements from the dictionary
copy()	            Returns a copy of the dictionary
fromkeys()	        Returns a dictionary with the specified keys and value
get()	            Returns the value of the specified key
items()	            Returns a list containing a tuple for each key value pair
keys()	            Returns a list containing the dictionary's keys
pop()	            Removes the element with the specified key
popitem()	        Removes the last inserted key-value pair
setdefault()	    Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	        Updates the dictionary with the specified key-value pairs
values()	        Returns a list of all the values in the dictionary
"""