#Function is a block of code which only runs when it is called
#You can pass data, known as parameters, into a function
#A function can return data as a result

#In python a fuction is defined using the def keyword
def my_function():
    print("Hello from a function")

my_function()



#Information can be passed into functions as arguments
#Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma
def name_function(fname):
    print(fname + " is my name")

name_function("Emil")
name_function("Tobias")
name_function("Artin")

#The terms parameter and argument can be used for the same thing: information that are passed into a function
"""
From a function's perspective:
A parameter is the variable listed inside the parentheses in the function definition.
An argument is the value that is sent to the function when it is called.
"""

#By default, a function must be called with the correct number of arguments.
#Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less
def full_name(fname, lname):
    print(fname + " " + lname)

full_name("Walter", "White")
#If you try to call the function with 1 or 3 arguments, you will get an error


#Arbitrary arguments
#Arbitrary Arguments are often shortened to *args in Python documentations
"""
If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
This way the function will receive a tuple of arguments, and can access the items accordingly
"""
def kids(*kids):
    print("The second kid is " + kids[1])

kids("Emil", "Linus", "Walter", "Jesse")



#Keyword arguments, you can also send arguments with the key = value syntax.
#This way the order of the arguments does not matter.
#The phrase Keyword Arguments are often shortened to kwargs in Python documentations.
def children(child3, child1, child2):
    print("The youngest child is " + child3)

children(child1 = "Emil", child2 = "Linus", child3 = "Walter")



#Arbitrary keyword arguments, **kwargs
#Arbitrary Kword Arguments are often shortened to **kwargs in Python documentations
"""
If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
This way the function will receive a dictionary of arguments, and can access the items accordingly:
"""
def kid(**kid):
    print("His last name is " + kid["lname"])

kid(fname = "Walter", lname = "White")





#Default parameter, if we call the function without argument, it uses the default value
def country(country = "Armenia"):
    print("I am from " + country)

country("Sweden")
country("Iran")
country("Brazil")
country()
country("India")



#Passing a list as an argument
def food_function(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]

food_function(fruits)




#Return values, to let a function return a value, use the return statement
def return_function(x):
    return 5 * x

print(return_function(3))
print(return_function(2))
print(return_function(12))



#Pass statement, function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting error.
def empty_function():
    pass



#Recursion, Python also accepts function recursion, which means a defined function can call itself.
"""
Recursion is a common mathematical and programming concept.
It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.
The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates,
or one that uses excess amounts of memory or processor power.
However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.
"""
def tri_recursion(k):
    if (k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion Example Results")
tri_recursion(6)