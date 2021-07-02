#This shows the type of variable used
x = 6                                           #int
print(type(x))
x = "Hello World"                               #str
x = 6.5                                         #float
x = 5j                                          #complex
x = ["apple", "banana", "cherry"]               #list
x = ("apple", "banana", "cherry")               #tuple
x = {"apple", "banana", "cherry"}               #set
x = {"name": "Artin", "age": 36}                #dictionary
x = frozenset({"apple", "banana", "cherry"})    #frozenset
x = True                                        #bool
x = b"Hello"                                    #bytes
x = bytearray(5)                                #bytearray
x = memoryview(bytes(5))                        #memoryview

#Setting the specific datatype
x = str("Hello, World!")
x = int(10)
x = float(10.2)
x = complex(1j)
x = list(("Apple", "Banana", "Cherry"))
x = tuple (("Apple", "Banana", "Cherry"))
x = range(6)
x = dict(name="Artin", age=30)
x = set(("Apple", "Banana", "Cherry"))
x = frozenset(("Apple", "Banana", "Cherry"))
x = bool(5)
x = bytes(5)
x = bytearray(5)
x = memoryview(bytes(5))