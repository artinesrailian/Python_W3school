#To make sure a string will display as expected, we can format the result with the format() method
#Sometimes there are parts of a text that you do not control, maybe they come from a database, or user input
#To control such values, add placeholders (curly brackets {}) in the text, and run the values through the format() method
price = 49
txt = "The prise is {} dollars"
print(txt.format(price))

#You can add parameters inside the curly brackets to specify how to convert the value
#Format the price to be displayed as a number with two decimals
txt = "The price is {:.2f} dollars"
print(txt.format(price))

#Formatting types
"""
:< 	Left aligns the result (within the available space)
:> 	Right aligns the result (within the available space)
:^ 	Center aligns the result (within the available space)
:= 	Places the sign to the left most position
:+ 	Use a plus sign to indicate if the result is positive or negative
:- 	Use a minus sign for negative values only
:  	Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers)
:, 	Use a comma as a thousand separator
:_ 	Use a underscore as a thousand separator
:b 	Binary format
:c 	Converts the value into the corresponding unicode character
:d 	Decimal format
:e 	Scientific format, with a lower case e
:E 	Scientific format, with an upper case E
:f 	Fix point number format
:F 	Fix point number format, in uppercase format (show inf and nan as INF and NAN)
:g 	General format
:G 	General format (using a upper case E for scientific notations)
:o 	Octal format
:x 	Hex format, lower case
:X 	Hex format, upper case
:n 	Number format
:% 	Percentage format
"""

#If you want to use more values, just add more values to the format() method
quantity = 3
itemno = 567
MyOrder = "I want {} pieces of item number {} for {:.2f} dollars."
print(MyOrder.format(quantity, itemno, price))

#You can use index numbers (a number inside the curly brackets {0}) to be sure the values are placed in the correct placeholders
MyOrder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(MyOrder.format(quantity, itemno, price))

#Also, if you want to refer to the same value more than once, use the index number
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

#You can also use named indexes by entering a name inside the curly brackets {carname},
#but then you must use names when you pass the parameter values txt.format(carname = "Ford")
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))