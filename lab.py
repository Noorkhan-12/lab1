print("Hello, World!")
import sys
 
print(sys.version)
 
# here we learned identation.
if 5 > 2:
    print("five is greater than two!")
if 5 > 2:
  print("five is greater than two")
 
# now variables
x = 5
y = "Hello , world"
 
 
#print("Hello, World!")  this is a comment
print("Cheers, Mate!")
 
#we can do multiple line with triple qoutation
 
 
""" This i a comment,
and we use this for multiple lines of comment"""
 
# now variables
 
x = 5
y = "Najib"
print(x)
print(y)
 
#changing the type of the variable
 
x = 4
x = "najib"
print(x)
 
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
 
#type
 
x = 5
y = "John"
print(type(x))
print(type(y))
 
x = "John"
# is the same as
x = 'John'
 
# multiple values in one line
 
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
 
x = y = z = "Orange"
print(x)
print(y)
print(z)
 
# unpacking
 
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
 
#outputing multiple variables
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
 
# the + character work as mathematical operator
x = 5
y = 10
print(x + y)
 
#global variables
# we can use them both inside and outside of the fuc
x = "awesome"
 
def myfunc():
  print("Python is " + x)
 
myfunc()
 
#2
x = "awesome"
 
def myfunc():
  x = "fantastic"
  print("Python is " + x)
 
myfunc()
 
print("Python is " + x)
 
# to create a global inside a func use keyword global and change as well
x = "fantastic"
def myfunc():
  global x
  x = "fantastic"
 
myfunc()
 
print("Python is " + x)
 
# In Python, the data type is set when you assign a value to a variable:
 
 
x = "Hello World" #str  
x = 20  #int  
x = 20.5  #float  
x = 1j  #complex  
x = ["apple", "banana", "cherry"] #list
x = ("apple", "banana", "cherry") #tuple  
x = range(6)  #range  
x = {"name" : "John", "age" : 36} #dict
x = {"apple", "banana", "cherry"} #set  
x = frozenset({"apple", "banana", "cherry"})  #frozenset  
x = True  #bool
x = b"Hello"  #bytes  
x = bytearray(5)  #bytearray  
x = memoryview(bytes(5))  #memoryview
x = None      #   NoneType  
 
# we can specify as well
x = str("Hello World")
 
# To verify the type of any object in Python, use the type() function:
 
print(type(x))
print(type(y))
print(type(z))
 
# Type Conversion
# int to float
a = float(x)
#float to int
b = int(y)
# int to complex
c = complex(x)
 
# import a radom number
import random
print(random.randrange(1, 10))
 
#Casting
# specifying variable type
 
x = int(1)   # x will be 1
x = float(1)     # x will be 1.0
x = str("s1") # x will be 's1'
 
#strings
# both single and double qoutation are the same
print("Hello")
print('Hello')
 
a = "Hello"
print(a)
 
#  we can write multiple lines of string in triple qoutation
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
 
# or triple single qoutation
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
 
#gettiin a character in string
 
a = "Hello, World!"
print(a[1])
 
# Loop through the letters in the word "banana":
 
for x in "banana":
  print(x)
 
# length
a = "Hello, World!"
print(len(a))
 
# Check if "free" is present in the following text:
txt = "The best things in life are free!"
print("free" in txt)
 
# we can use if as well
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
 
# slicing
 
# Get the characters from position 2 to position 5 (not included):
 
b = "Hello, World!"
print(b[2:5])
# slice from the start
b = "Hello, World!"
print(b[:5])
# slice to the end
b = "Hello, World!"
print(b[2:])
 
# start the slice from the end
#Get the characters:
#From: "o" in "World!" (position -5)
#To, but not included: "d" in "World!" (position -2):
b = "Hello, World!"
print(b[-5:-2])
 
# The upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper())
#lower()
a = "Hello, World!"
print(a.lower())
 
#Remove Whitespace
#The strip() method removes any whitespace from the beginning or the end:
 
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
# replacing a string with another
#replace()
a = "Hello, World!"
print(a.replace('H', 'j'))
 
# The split() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
 
# String Concatenation
# Merge variable a with variable b into variable c:
a = "Hello"
b = "World"
c = a + b
print(c)
#to add space between them
a = "Hello"
b = "World"
c = a + " " + b
print(c)
 
#Create an f-string:
# for merging num and string
age = 36
txt = f"My name is John, I am {age}"
print(txt)
 
price = 59
txt = f"The price is {price} dollars"
print(txt)
 
#Perform a math operation in the placeholder, and return the result:
txt = f"The price is {20 * 59} dollars"
print(txt)
 
# The escape character allows you to use double quotes when you normally would not be allowed:
 
txt = "We are the so-called \"Vikings\" from the north."
 
 