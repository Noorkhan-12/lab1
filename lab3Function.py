def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if 2 * chickens + 4 * rabbits == numlegs:
            return chickens, rabbits
    return None, None


chickens, rabbits = solve(35, 94)
if chickens is not None:
    print(f"Chickens: {chickens}, Rabbits: {rabbits}")
else:
    print("No solution found.")

def converter(Farh):
    result = (Farh-32)*(5/9)
    print(result)


number = float(input("please insert your desired number? "))
converter(number)

def converter(numbeer):
    result = number/28.3494
    print(result)


number = float(input("please insert a number? "))

converter(number)

import random
name = input("Hello, what is your name? ")
number = random.randint(1, 20)
print(f"well {name} Im thinking a name between 1 and 20 \n Take a guess")

counter = 0
numberPlayer = -1
while numberPlayer != number:
    numberPlayer = int(input("Your guess: "))

    if numberPlayer == number:
        print('You Win')
    elif abs(numberPlayer - number) <= 5:
        print('You are so close')
    else:
        print('Not close')
    counter += 1


my_list = []
num = int(input("write a number? "))

for i in range(num):
    num2 = int(input("insert another number? "))
    my_list.append(num2)

for i in range(len(my_list)):
    print(my_list[i]*"*")

import sys
import random
print("Hello, World!")

print(sys.version)

if 5 > 2:
    print("Five is greater than two!")
if 5 > 2:
    print("Five is greater than  two!")

x = 5
y = "Hello, world!"

# This is a comment.
print("Hello, World!")
print("Hello, World!")  # This a comment.
# print("Hello, World!")
print("Hello, World!")

x = 5
y = "John"
print(x)
print(y)
x = 4  # x is type int
x = "sally"  # x is now of type str
print(x)

x = str(3)  # x will be '3'
y = int(3)  # y will be 3
z = float(3)  # z will be 3.0

x = 5
y = "John"
print(type(x))
print(type(y))

x = 'John'
# is the same as
x = 'John'

a = 4
A = "Sally"
# A will not overwrite a

# Legal names in python
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# illegal names in python
2myvar = "John"
my-var = "John"
my var = "John"

# ways to declear a variable with more than one word
myVariableName = "John"  # Camel Case
MyVariableName = "John"  # Pascal Case
my_variable_name = "John"  # Snake case

# Many Values to Mutiple Variables
x,  y, z = "orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# one value to mutiple Variables
x = y = z = "ornage"
print(x)
print(y)
print(z)

# Unpacking a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Output Variables
x = "Python is awesome"
print(x)

# print mutiple variable seprated by a comma
x = "python"
y = "is"
z = "awesome"
# You can also use the + operator to output mutiple variable
x = "python"
y = "is "
z = "awesome"
print(x + y + z)

# For the numbers, the + character works as a mathematical operator
x = 5
y = 10
print(x + y)

x = 5
y = "John"
print(x, y)

# Global Variable; vavriable outside of a function
x = "awesome"


def myfunction():
    print("python is " + x)


myfunction()

# create a variable inside a function, with the same name as the global variable

x = "aswesome"


def myfunction():
    x = "fantastic"
    print("Python is " + x)


myfunction()

print("python is " + x)

# gloabal keyword


def myfunction():
    global x
    x = "fantastic"


myfunction()

print("Python id " + x)

# you can use global keyword to change the value of a variable inside the a function
x = "awesome"


def myfunction():
    global x
    x = "fantastic"


myfunction()

print("python is " + x)

# printing the type of a vriable
x = 5
print(type(x))

x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(type(x))
print(type(y))
print(type(z))
# int is a full number without a fraction

x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

# float is a number, positive or negative, containing one or more decimal

x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

# complex also be scintific number with an "e" to indicate the power of 10
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

# complex number are wrriten with a "j" as the imaginary
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

# Type Coversion

x = 1    # int
y = 2.8  # float
z = 1j   # complex

# convert from int to float:
a = float(x)

# convert from float to int:
b = int(y)

# convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# Random Number
print(random.randrange(1, 10))

# casting
# specify the vriable type
x = int(1)  # x will be 1
y = int(2.8)  # y will be 2
z = int("3")  # z will be 3
# float
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2")  # w will be 4.2
# string
x = str("s1")  # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

# string
# you can declear a python string in both double or single quote
print("Hello")
print('Hello')
# are the same
# Quote inside Quote
# yo can use ase long quote inside the string that it did not match the quote srrounded
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

# assinig a strig to a variable
x = "hello"
print(x)
# multiple string
# you can assign a multiple string to a string varriable bt using three quottes """ """
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
# or thee single quotes
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
# like many other programming langauge strings are arrays
# square braket is used to access to the elemnet of the of the string
a = "Hello, World!"
print(a[1])

# since strings are arrays you can for loop inside the string
for x in "banana":
    print(x)

# to get the length of a string we use from len()
a = "Hello, World!"
print(len(a))
# to check if a certain text or chracter exist in string we use form in
txt = "The best things in life are free!"
print("free" in txt)

# with f statment
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")

# Check if not
# check if text or string is not in a string
txt = "The best things in life are free!"
print("expensive" not in txt)

# with f statment
txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")
# you can return a range of chracters by using slicing
b = "Hello, World!"
print(b[2:5])
# slicing from the first
b = "Hello, World!"
print(b[:5])
# slice to the end
b = "Hello, World!"
print(b[2:])

# Negative Index
b = "Hello, World!"
print(b[-5:-2])

# upper case
a = "Hello, World!"
print(a.upper())

# lower case
a = "Hello, World!"
print(a.lower())
# strip removes white spaces in python
a = " Hello, World! "
print(a.strip())  # returns "Hello, World!"

# replace
a = "Hello, World!"
print(a.replace("H", "J"))
# The split() method returns a list where the text between the specified separator becomes the list items.

a = "Hello, World!"
print(a.split(","))  # returns ['Hello', ' World!']

# String Concatenation
# To concatenate, or combine, two strings you can use the + operator.
a = "Hello"
b = "World"
c = a + b
print(c)

# To add a space between them, add a " ":
a = "Hello"
b = "World"
c = a + " " + b
print(c)

# F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.
age = 36
txt = f"My name is John, I am {age}"
print(txt)
# Add a placeholder for the price variable:
price = 59
txt = f"The price is {price} dollars"
print(txt)

# Display the price with 2 decimals:
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

# Perform a math operation in the placeholder, and return the result:
txt = f"The price is {20 * 59} dollars"
print(txt)
# to fix problem the problem of sytanx erro in python we use from esape chracter
txt = "We are the so-called \"Vikings\" from the north."

def List():
    n = int(input("Please input how many numbers you want to enter: "))
    numbers = []
    for i in range(n):
        num = int(input(f"Please input number {i+1}: "))
        numbers.append(num)
    for i in range(len(numbers)):
        if numbers[i] == 0 and numbers[i+1] == 0 and numbers[i+2] == 7:
            print("found")
            break


List()

def List():
    n = int(input("Please input how many numbers you want to enter: "))
    numbers = []
    for i in range(n):
        num = int(input(f"Please input number {i+1}: "))
        numbers.append(num)
    for i in range(len(numbers)):
        if numbers[i] == 3 and numbers[i+1] == 3:
            print("found")
            break


List()


name = input("write a string? ")
reversed_string = name[::-1]
if name == reversed_string:
    print("YES")
else:
    print("NO")


from itertools import permutations


def recursive():
    name = input("please insert a string? ")
    perm_set = set(permutations(name))
    print(f"\n permuation of '{name}': ")
    for p in sorted(perm_set):
        print(''.join(p))


recursive()



def is_prime(number):
    check = False

    for i in range(2, number-1):
        if number % i == 0:
            check = True
            break

        if check == False:
            print(number)


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

for i in list:
    is_prime(i)



def Sentence():
    sentence = input("Enter a sentence")
    words = sentence.split()
    reversed_sentence = ' ' .join(words[::-1])
    return reversed_sentence


print(Sentence())


def uniq(my_new):
    my_new = []
    for item in my_list:
        if item not in my_new:
            my_new.append(item)
    print(my_new)


num = int(input('Please insert a number'))
my_list = []

for i in range(num):
    num2 = int(input("please insert your numbers? "))
    my_list.append(num2)

uniq(my_list)

