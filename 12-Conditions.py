#Python conditions
"""
Equals:                     a == b
Not Equals:                 a != b
Less than:                  a < b
Less than or equal to:      a <= b
Greater than:               a > b
Greater than or equal to:   a >= b
"""

#An if statement is writeen by using if keyword
#Python relies on indentation
a, b = 33, 200
if b > a:
    print("b is greater than a")

#The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition"
a, b = 33, 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

#The else keyword catches anything which isn't caught by the preceding conditions
a, b = 200, 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

#If you have only one statement to execute, you can put it on the same line as the if statement
if a > b: print("a is greater than b")

#If you have only one statement to execute, one for if, and one for else, you can put it all on the same line
a, b = 2, 200
print("A") if a > b else print("B")
#This technique is known as Ternary Operators, or Conditional Expressions

#You can also have multiple else statements on the same line
a = b = 330
print("A") if a > b else print ("=") if a == b else print("B")

#The and keyword is a logical operator, and is used to combine conditional statements
a, b, c = 200, 33, 500
if a > b and c > a:
    print("Both conditions are True")

#The or keyword is a logical operator, and is used to combine conditional statements
if a > b or a >c:
    print("At lest one of the conditions is True")

# Nested if: you can have if statements inside if statements, this is called nested if statements
x = 41
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

#Pass statement: if statement cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error
a, b = 33, 200
if b > a:
    pass