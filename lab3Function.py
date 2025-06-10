# A basic function
def my_function():
    print("Hello from a function")

# Function called after being defined (note: previous definition is overwritten)
def my_function():
    print("Hello from a function")
my_function()

# Function with one argument
def my_function(fname):
    print(fname + " Refsnes")
my_function("Emil")
my_function("Tobias")
my_function("Linus")

# Function with two arguments
def my_function(fname, lname):
    print(fname + " " + lname)
my_function("Emil", "Refsnes")

# Function call with missing argument (this will raise an error)
def my_function(fname, lname):
    print(fname + " " + lname)
my_function("Emil")

# Function with arbitrary number of arguments (*args)
def my_function(*kids):
    print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")

# Function with named arguments
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# Function with arbitrary keyword arguments (**kwargs)
def my_function(**kid):
    print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")

# Function with default parameter value
def my_function(country = "Norway"):
    print("I am from " + country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# Function that accepts a list
def my_function(food):
    for x in food:
        print(x)
fruits = ["apple", "banana", "cherry"]
my_function(fruits)

# Function with return statement
def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))

# Empty function with pass
def myfunction():
    pass

# Function with positional-only argument
def my_function(x, /):
    print(x)
my_function(3)

# Function with keyword argument
def my_function(x):
    print(x)
my_function(x = 3)

# Function with positional-only argument (will raise error with keyword)
def my_function(x, /):
    print(x)
my_function(x = 3)

# Function with keyword-only argument
def my_function(*, x):
    print(x)
my_function(x = 3)

# Normal function call
def my_function(x):
    print(x)
my_function(3)

# Keyword-only argument (will raise error if passed positionally)
def my_function(*, x):
    print(x)
my_function(3)

# Combination of positional-only and keyword-only arguments
def my_function(a, b, /, *, c, d):
    print(a + b + c + d)
my_function(5, 6, c = 7, d = 8)

# Recursive function
def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result
print("Recursion Example Results:")
tri_recursion(6)

# Simple lambda with one argument
x = lambda a : a + 10
print(x(5))

# Lambda with two arguments
x = lambda a, b : a * b
print(x(5, 6))

# Lambda with three arguments
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

# Lambda returning function (closure)
def myfunc(n):
    return lambda a : a * n

# Using a lambda doubler
def myfunc(n):
    return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))

# Using a lambda tripler
def myfunc(n):
    return lambda a : a * n
mytripler = myfunc(3)
print(mytripler(11))

# Using both doubler and tripler
def myfunc(n):
    return lambda a : a * n
mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11))
print(mytripler(11))

# Simple class with one property
class MyClass:
    x = 5

p1 = MyClass()
print(p1.x)

# Class with _init_ constructor
class Person:
    def _init_(self, name, age):
        self.name = name
        self.age = age
p1 = Person("John", 36)
print(p1.name)
print(p1.age)

# Printing an object without _str_ method
class Person:
    def _init_(self, name, age):
        self.name = name
        self.age = age
p1 = Person("John", 36)
print(p1)

# Printing with _str_ method
class Person:
    def _init_(self, name, age):
        self.name = name
        self.age = age
    def _str_(self):
        return f"{self.name}({self.age})"
p1 = Person("John", 36)
print(p1)

# Method inside class
class Person:
    def _init_(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello my name is " + self.name)
p1 = Person("John", 36)
p1.myfunc()

# Custom names for self
class Person:
    def _init_(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

# Modifying object properties
p1.age = 40

# Deleting object properties and object
del p1.age
del p1

# Empty class
class Person:
    pass

# Inheriting from Person (using base class constructor directly)
class Student(Person):
    def _init_(self, fname, lname):
        Person._init_(self, fname, lname)

# Inheriting using super()
class Student(Person):
    def _init_(self, fname, lname):
        super()._init_(fname, lname)

# Adding extra attribute
class Student(Person):
    def _init_(self, fname, lname):
        super()._init_(fname, lname)
        self.graduationyear = 2019

# Constructor with additional parameter
class Student(Person):
    def _init_(self, fname, lname, year):
        super()._init_(fname, lname)
        self.graduationyear = year
x = Student("Mike", "Olsen", 2019)

# Child class with custom method
class Student(Person):
    def _init_(self, fname, lname, year):
        super()._init_(fname, lname)
        self.graduationyear = year
    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)