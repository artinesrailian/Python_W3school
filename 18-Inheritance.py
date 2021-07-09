#Inheritance allows us to define a class that inherits all the methods and properties from another class
#Parent class is the class being inherited from, also called base class
#Child class is the class that inherits from another class, also called derived class

#Create a parent class
#Any class can be a parent class, so the syntax is the same as creating any other class
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

#Use the person class to create an object, and then execute the printname method
x = Person("John", "Doe")
x.printname()

#To create a class that inherits the functionality from another class,
#send the parent class as a parameter when creating the child class
class Student(Person):
    pass

#Now the Student class has the same properties and methods as the Person class
x = Student("Mike", "Olsen")
x.printname()

#So far we have created a child class that inherits the properties and methods from its parent
#We want to add the __init__() function to the child class (instead of the pass keyword)
#Python also has a super() function that will make the child class inherit all the methods and properties from its parent
#By using the super() function, you do not have to use the name of the parent element,
#it will automatically inherit the methods and properties from its parent.
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

#When you add the __init__() function, the child class will no longer inherit the parent's __init__() function
#The child's __init__() function overrides the inheritance of the parent's __init__() function


#To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function
class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(fname, lname)
#Now we have successfully added the __init__() function, and kept the inheritance of the parent class,
#and we are ready to add functionality in the __init__() function

#Add properties
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationyear = 2020

#In the above example the year 2020 must be replaced with a variable
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.greaduationyear = year

x = Student("Mike", "Olsen", 2020)


#Add method, Add a method called welcome to the Student class
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)