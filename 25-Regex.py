#A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern
#RegEx can be used to check if a string contains the specified search pattern
#Python has a built-in package called re, which can be used to work with Regular Expressions
import re

#When you have imported the re module, you can start using regular expressions
#Search the string to see if it starts with "The" and ends with "Spain"
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)

#The re module offers a set of functions that allows us to search a string for a match
"""
Function 	Description
findall 	Returns a list containing all matches
search 	    Returns a Match object if there is a match anywhere in the string
split 	    Returns a list where the string has been split at each match
sub 	    Replaces one or many matches with a string
"""

#Metacharacters are characters with a specila meaning
"""
Character 	    Description 	                                                                Example
[] 	            A set of characters 	                                                        "[a-m]"
\ 	            Signals a special sequence (can also be used to escape special characters) 	    "\d"
. 	            Any character (except newline character) 	                                    "he..o"
^ 	            Starts with 	                                                                "^hello"
$ 	            Ends with 	                                                                    "world$"
* 	            Zero or more occurrences 	                                                    "aix*"
+ 	            One or more occurrences 	                                                    "aix+"
{} 	            Exactly the specified number of occurrences 	                                "al{2}"
| 	            Either or 	                                                                    "falls|stays"
() 	            Capture and group
"""

#Special sequence is a \ followed by one of the characters in the list below, and has special meaning
"""
Character 	Description 	                                            Example
\A 	        Returns a match if the specified characters                 "\AThe"
            are at the beginning of the string
\b 	        Returns a match where the specified characters              r"\bain"
            are at the beginning or at the end of a word                r"ain\b"
            (the "r" in the beginning is making sure that
            the string is being treated as a "raw string")
\B 	        Returns a match where the specified characters              r"\Bain"
            are present, but NOT at the beginning (or at the end)       r"ain\B"
            of a word (the "r" in the beginning is making sure that
            the string is being treated as a "raw string")
\d 	        Returns a match where the string contains digits            "\d"
            (numbers from 0-9)
\D 	        Returns a match where the string DOES NOT contain digits 	"\D"
\s 	        Returns a match where the string contains                   "\s"
            a white space character
\S 	        Returns a match where the string DOES NOT                   "\S"
            contain a white space character
\w 	        Returns a match where the string contains                   "\w"
            any word characters (characters from a to Z,
            digits from 0-9, and the underscore _ character)
\W 	        Returns a match where the string                            "\W"
            DOES NOT contain any word characters
\Z 	        Returns a match if the specified characters                 "Spain\Z"
            are at the end of the string
"""

#Set is a sef of characters inside a pair of square brackets [] with a special meaning
"""
Set 	            Description
[arn] 	            Returns a match where one of the specified characters (a, r, or n) are present
[a-n] 	            Returns a match for any lower case character, alphabetically between a and n
[^arn] 	            Returns a match for any character EXCEPT a, r, and n
[0123] 	            Returns a match where any of the specified digits (0, 1, 2, or 3) are present
[0-9] 	            Returns a match for any digit between 0 and 9
[0-5][0-9] 	        Returns a match for any two-digit numbers from 00 and 59
[a-zA-Z] 	        Returns a match for any character alphabetically between a and z, lower case OR upper case
[+] 	            In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string
"""

#The findall() function returns a list containing all matches
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

#The list contains the matches in the order they are found
#If no matches are found, an empty list is returned
x = re.findall("Portugal", txt)
print(x)

#The search() function searches the string for a match, and returns a Match object if there is a match
#If there is more than one match, only the first occurrence of the match will be returned
#Search for the first white-space character in the string
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start())

#If no mathces are found, the value None is returned
x = re.search("Portugal", txt)
print(x)

#The split() function return a list where the string has been split at each match
#Split at each white-space character
x = re.split("\s", txt)
print(x)

#You can control the number of occurrences by specifying the maxsplit parameter
x = re.split("\s", txt, 1)
print(x)

#The sub() function replaces the matches with the text of your choice
x = re.sub("\s", "5", txt)
print(x)

#You can control the number of replacements by specifying the count parameter
x = re.sub("\s", "5", txt, 2)
print(x)

#A math object is an object containing information about the search and the result
#If there is no match, the value None will be returned, instead of the Match object
x = re.search("ai", txt)
print(x)  #This will print an object

#The Match Object has properties and methods used to retrieve information about the search, and the result
"""
.span() returns a tuple containing the start-, and end positions of the match.
.string returns the string passed into the function
.group() returns the part of the string where there was a match
"""
x = re.search(r"\bS\w+", txt)
print(x.span())

#Print the string passed into the function
x = re.search(r"\bS\w+", txt)
print(x.string)

#Print the part of the string where there was a match
#The regular expression looks for any words that starts with an upper case "S"
x = re.search(r"\bS\w+", txt)
print(x.group())