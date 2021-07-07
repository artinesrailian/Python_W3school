#Python has two primitive loop commands, while and for loops
i = 1
while i < 6:
    print(i)
    i += 1

#The while loop requires relevant variables to be ready, in this example we need to define an indexing variable, i, which we set to 1

#With the break statement we can stop the loop even if the while condition is true
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

#With the continue statement we can stop the current iteration and continue with the next
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

#With the else statement we can run a block of code once when the condition no longer is true
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

"""
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string)
This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages
With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc
"""
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

#The for loop does not require an indexing variable to set beforehand
#Even strings are iterabel objects, they contain a sequence of characters
for x in "banana":
    print(x)

#With the break statement we can stop the loop before it has looped thourgh all the items
for x in fruits:
    print(x)
    if x == "banana":
        break

#Exit the loop when x is "banana", but this time the break comes before the print
for x in fruits:
    if x == "banana":
        break
    print(x)

#With the continue statement we can stop the current iteration of the loop, and continue with the next
for x in fruits:
    if x == "banana":
        continue
    print(x)

#Range() function
"""
To loop through a set of code a specified number of times, we can use the range() function,
The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number
"""
for x in range(6):
    print(x)

#The range() function defaults to 0 as a starting value,
#however it is possible to specify the starting value by adding a parameter:
#range(2, 6), which means values from 2 to 6 (but not including 6):
for x in range(2, 6):
    print(x)

#The range() function defaults to increment the sequence by 1,
#however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3)
for x in range(2, 30, 5):
    print(x)

#The else keyword in a for loop specifies a block of code to be executed when the loop is finished
for x in range(6):
    print(x)
else:
    print("Finally finished!")

#The else block will NOT be executed if the loop is stopped by a break statement
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

#Nested loop is a loop inside a loop, the "inner loop" will be executed one time for each iteration of the "outer loop"
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x, y)

#for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error
for x in [0, 1, 2]:
    pass