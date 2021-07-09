#A variable is only available from inside the region it is created. This is called scope
#A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.
def MyFunc():
    x = 200
    print(x)
MyFunc()

#As explained the variable x is not available outside the function, but it is available for any function inside the function
#The local variable can be accessed from a function within the function
def MyFunc():
    x = 300
    def MyInnerFunc():
        print(x)
    MyInnerFunc()
MyFunc()

#A variable created in the main body of the Python code is a global variable and belongs to the global scope
#Global variables are available from within any scope, global and local
x = 400
def MyFunc():
    print(x)
MyFunc()

#If you operate with the same variable name inside and outside of a function, Python will treat them as two separate variable,
#One available in the global scope (outsied the function) and one available in the local scope (inside the function)

x = 500
def MyFunc():
    x = 600
    print("This is function variable = ", x)
MyFunc()
print("This is the global variable =", x)

#The global keyword makes the variable global
def MyFunc():
    global x
    x = 800
MyFunc()
print(x)

#Also, use the global keyword if you want to make a change to a global variable inside a function
x = 300
def MyFunc():
    global x
    x = 400
    print("This is changed global variable in the function call = ", x)
print("This is before chaning the variable = ", x)
MyFunc()
print("This is after chaning the variable = ", x)