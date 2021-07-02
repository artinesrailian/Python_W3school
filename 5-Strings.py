#Strings can be in single or double quotation
from typing import Text


print("Hello")
print('Hello')

#Strings can be assigned to a variable
a = "Artin"
print(a)

#Example of multiline string
multi_line = """This is the example for multiline string.
As you see we can have multiline strings using triple double/single quotation mark.
Lines between opening and closing of these quotation marks are all in the multiline string"""
print(multi_line)

#Strings are array in python programming language
a = "Artin"
print("Second character of " + a + " is '" + a[1] + "'")

#We can loop in the strings as they are arrays
for item in "Artin":
    # a += 1
    print(item)

#String lenght
a = "Artin"
print("The lenght of the string " + a + " is " + str(len(a)))

#To check the existense of a character or phrase in a string we can use "in"
txt = "The best things in life are free!"
print("free" in txt)

#Usecase in the if statement
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")
elif "expensive" not in txt:
    print("expensive is not present in text.")

#Slicing string
b = "Hello, World!"
print(b[2:5]) # Example of the slice from index 2 to index number 4 as the index number 5 is not included when slicing
print(b[:5]) #Example of the slice from the start to the index number 5 not inclusive
print(b[5:]) #Example of the slice from the 5th index to the last index
print(b[-5:-2]) #Negative indexing to start from index number 5 from the last character and goes to 2 character

#To convert the string to uppercase
a = "Hello, World!"
print(a.upper())

#To convert the string to lowercase
a = "Hello, World!"
print(a.lower())

#Remove whitespaces, it only removes the whitespaces in the beginning or at the end
a = "    Hello,      World!         "
print(a.strip())

#Replace string with another string, in this case the letter "H" is replaced with the letter "J"
a = "Hello, World!"
print(a.replace("H", "J"))

#Split the string, this example will split the string from "," to two strings in the list
a = "Hello, World!"
print(a.split(","))

#Concat two or more strings
a = "Hello, "
b = "World!"
c = a + b
print(c)

#Format method takes the argument and put it in the string where the {} is located
age = 30
address = 100
phone = 374111111
text = "My name is Artin, and I am {} years old. My Phone number is {} and my home address is No.{}"
print(text.format(age, phone, address))

#The same example above with the use of index number
age = 30
address = 100
phone = 374111111
text = "My name is Artin, and I am {1} years old. My Phone number is {2} and my home address is No.{0}"
print(text.format(address, age, phone ))

#Escape character is \ like in Linux followed by the illegal or the character that we want to scape
text = "We are the so-called \"Vigings\" from the north"
print(text)

#Builtin string methods with their description
"""
Method 	                Description
capitalize()	        Converts the first character to upper case
casefold()	            Converts string into lower case
center()	            Returns a centered string
count()	                Returns the number of times a specified value occurs in a string
encode()	            Returns an encoded version of the string
endswith()	            Returns true if the string ends with the specified value
expandtabs()	        Sets the tab size of the string
find()	                Searches the string for a specified value and returns the position of where it was found
format()	            Formats specified values in a string
format_map()	        Formats specified values in a string
index()	                Searches the string for a specified value and returns the position of where it was found
isalnum()	            Returns True if all characters in the string are alphanumeric
isalpha()	            Returns True if all characters in the string are in the alphabet
isdecimal()	            Returns True if all characters in the string are decimals
isdigit()	            Returns True if all characters in the string are digits
isidentifier()	        Returns True if the string is an identifier
islower()	            Returns True if all characters in the string are lower case
isnumeric()	            Returns True if all characters in the string are numeric
isprintable()	        Returns True if all characters in the string are printable
isspace()	            Returns True if all characters in the string are whitespaces
istitle() 	            Returns True if the string follows the rules of a title
isupper()	            Returns True if all characters in the string are upper case
join()	                Joins the elements of an iterable to the end of the string
ljust()	                Returns a left justified version of the string
lower()	                Converts a string into lower case
lstrip()	            Returns a left trim version of the string
maketrans()	            Returns a translation table to be used in translations
partition()	            Returns a tuple where the string is parted into three parts
replace()	            Returns a string where a specified value is replaced with a specified value
rfind()	                Searches the string for a specified value and returns the last position of where it was found
rindex()	            Searches the string for a specified value and returns the last position of where it was found
rjust()	                Returns a right justified version of the string
rpartition()	        Returns a tuple where the string is parted into three parts
rsplit()	            Splits the string at the specified separator, and returns a list
rstrip()	            Returns a right trim version of the string
split()	                Splits the string at the specified separator, and returns a list
splitlines()	        Splits the string at line breaks and returns a list
startswith()	        Returns true if the string starts with the specified value
strip()	                Returns a trimmed version of the string
swapcase()	            Swaps cases, lower case becomes upper case and vice versa
title()	                Converts the first character of each word to upper case
translate()	            Returns a translated string
upper()	                Converts a string into upper case
zfill()	                Fills the string with a specified number of 0 values at the beginning
"""