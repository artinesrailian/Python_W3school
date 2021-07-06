#Every comparison in python return a boolean value of True or False
print(10 > 9)
print( 10 == 9)
print(10 < 9)

#When you run a condition in an if statement, Python return True or False
a, b = 200, 33
if b > a:
    print("b is greater than a")
else:
    print("a is greater than b")

#The bool() function allows you to evaluate any value, and give you True or False in return
print(bool("Hello"))
print(bool(15))
x = "Hello"
y = 15
print(bool(x))
print(bool(y))

"""
Almost any value is evaluated to True if it has some sort of content
Any string is True, except empty strings.
Any number is Trye, except 0.
Any list, tuple, set and dictionary are True, except empty ones.
"""
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

"""
In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, '', the
number 0, and the value None. And of course the value Flase evaluates to False.
"""
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({}) 

"""
One more value, or object in this case, evaluates to False, and that is if you have an object
that is made from a class with a __len__ function that returns 0 or False
"""
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#Function can return a boolean
def myFunction():
    return True
print(myFunction())

#Execute code based on the Boolean answer of a function
def newFunction():
    return True
if newFunction():
    print("YES!")
else:
    print("NO!")

#isinstance() function can be used to determine if an object is of a certain data type
x = 200
print(isinstance(x, int))