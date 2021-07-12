#The key function for working with files in Python is the open() function
#The open() function takes two parameters, filename, and mode
#There are four different modes
"""
r - Read - Default value. Opens a file for reading, error if the file does not exist
a - Append - Opens a file for appending, creates the file if it does not exist
w - Write - Opens a file for writing, creates the file if it does not exist
x - Create - Creates the specified file, returns an error if the file exists
"""

#In addition you can specify if the file should be handled as binary or text mode
"""
t - Text - Default value. Text mode
b - Binary - Binary mode (e.g. images)
"""

#The following two codes are the same as the read and text are the default values
f = open("demofile.txt", "rt")
f = open("demofile.txt")

#The read() method for reading the content of the file is the built-in method for open()
print(f.read())
"""
If the file is located in a different location, you will have to specify the file path, like this:
Example
f = open("D:\\myfiles\welcome.txt", "r")
"""

#By default the read() method returns the whole text, but you can also specify how many characters you want to return
f = open("demofile.txt")
print(f.read(10))

#You can return one line by using the readline() method
f = open("demofile.txt")
print(f.readline())

#By looping through the lines of the file, you can read the whole file, line by line
f = open("demofile.txt")
for x in f:
    print(x)

#It is a good practice to always close the file when you are done with it
f = open("demofile.txt")
print(f.readline())
f.close()

#You should always close your files, in some cases, due to buffering, changes made to a file may not show until you close the file

f = open("demofile.txt", "a")
f.write("Now the file has more lines!")
f.close()
f = open("demofile.txt")
print(f.readlines())
f.close()

f = open("demofile2.txt", "w")
f.write("This is the demofile2.txt")
f.close()
print(open("demofile2.txt").readline())

#The "w" method will overwrite the entire file

#To delete a file, you must import the OS module, and run its os.remove() function
import os
os.remove("demofile2.txt")

#To avoid getting an error, you might want to check if the file exists before you try to delete it
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist!")

#To delete an entire folderm, use the os.rmdir() method
#os.rmdir("myfolder")
#You can only remove empty folders