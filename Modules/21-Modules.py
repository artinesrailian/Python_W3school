#Consider a module to be the same as a code library
#A file containing a set of functions you want to include in your application
#To create a module just save the code you want in a file with the file extension .py
import MyModule
MyModule.greeting("John")

#When using a function from a module, use the syntax: module_name.function_name
#The module can contain functions, as already described, but also variables of all types (arrays, dictionaries, objects etc)
import MySecondModule
a = MySecondModule.person1["age"]
print(a)

#You can name the module file whatever you like, but it must have the file extension .py
#You can create an alias when you import a module, by using the as keyword
import MySecondModule as mx

a = mx.person1["name"]
print(a)

#There are several built-in modules in Python, which you can import whenver you like
import platform
x = platform.system()
print(x)

#There is a built-in function to list all the function names (or variable names) in a module. The dir() function
import platform

x = dir(platform)
print(x)
#The dir() function can be used on all modules, also the ones you create yourself
#You can choose to import only parts from a module, by using the from keyword

from MyModule import person1
print (person1["age"])

#When importing using the from keyword, do not use the module name when referring to elements in the module.
#Example: person1["age"], not mymodule.person1["age"]