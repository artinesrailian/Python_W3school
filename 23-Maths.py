#The min() and max() functions can be used to find the lowest or highest value in an iterable
x = min(5, 10, 15)
y = max(5, 10, 15)
print("Min is ", x)
print("Max is ", y)

#The abs() function returns the absolute (positive) value of the specified number
x = abs(-7.25)
print(x)

#The pow(x, y) function returns the value of x to the power of y (xy)
x = pow(4, 3)
print("4 ^ 3 = ", x)

#Python has also a built-in module called math, which extends the list of mathematical functions
#To use it, you must import the math module
#The math.sqrt() method for example, returns the square root of a number
import math
x = math.sqrt(64)
print(x)

#The math.ceil() method rounds a number upwards to its nearest integer,
#and the math.floor() method rounds a number downwards to its nearest integer, and returns the result
x = math.ceil(1.4)
y = math.floor(1.4)
print(x)
print(y)

#The math.pi constant, returns the value of PI (3.14...)
x = math.pi
print(x)
print(math.pi)