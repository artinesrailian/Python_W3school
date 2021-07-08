#A lambda function is a small anonymus function
#A lambda function can take any number of arguments, but can only have one expression
#Lambda syntax:
# lambda arguments : expression
x = lambda a : a + 10
print("Sum result is", x(5))



#Lambda function can take any number of arguments
multiply = lambda a, b : a * b
print("Multiplication result is", multiply(5, 6))



#The power of lambda is better shown when you use them as an anonymous function inside another function
#Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))