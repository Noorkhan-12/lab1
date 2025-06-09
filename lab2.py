# Boolean Comparison
a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")
 
# Boolean evaluation
x = "Hello"
y = 15
print(bool(x))
print(bool(y))
 
# Boolean evaluation of falsy values
print(bool(False))
print(bool(None))  # None is a data type that returns False in bool context
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
 
# Custom class with len method
class myclass:
    def len(self):
        return 0
 
myobj = myclass()
print(bool(myobj))
 
# Function returning boolean
def myFunction():
    return True
 
print(myFunction())
 
# Conditional based on function
if myFunction():
    print("YES!")
else:
    print("NO!")
 
# Type checking
x = 200
print(isinstance(x, int))
 
# Arithmetic
print((6 + 3) - (6 + 3))
 
# List operations
thislist = ["apple", "banana", "cherry"]
print(thislist)
 
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1)
print(list2)
print(list3)
 
# List indexing
mylist = ['apple', 'banana', 'cherry']
print(mylist[-1])
 
# List type checking
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
 
# List slicing
thislist = ["Wick", "mark", "John", "Noor", "Najib", "Habib", "mike"]
print(thislist[2:5])
print(thislist[:4])
print(thislist[-4:-1])
 
# List modification
thislist = ["blue", "Red", "Yellow"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
 
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
 
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
 
# List extension
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
 
# List removal
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
 
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
 
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
 
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
 
# List clearing
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
 
# List iteration
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)
 
for i in range(len(thislist)):
    print(thislist[i])
 
i = 0
while i < len(thislist):
    print(thislist[i])
    i += 1
 
[print(x) for x in thislist]
 
# List comprehension
newlist = [x for x in range(10) if x < 5]
print(newlist)
 
# List sorting
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
 
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
 
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
print(thislist)
 
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=True)
print(thislist)
 
# List reversal
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
 
# List copying
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
 
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)
 
# Tuple operations
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])
 
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")
 
# Tuple modification (via list conversion)
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)
 
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)
 
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)
 
# Tuple unpacking
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)
 
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)
 
# Python Sets: Basic Operations
myset = {"apple", "banana", "cherry"}
print(myset)
 
myset.add("orange")
print(myset)
 
myset.update(["mango", "grape"])
print(myset)
 
myset.remove("banana")
print(myset)
 
myset.discard("apple")
print(myset)
 
myset.pop()
print(myset)
 
myset.clear()
print(myset)
 
# Python Sets: Looping and Checking
myset = {"apple", "banana", "cherry"}
for x in myset:
    print(x)
 
if "banana" in myset:
    print("Yes, 'banana' is in the set")
 
# Python Dictionaries: Basic Operations
mydict = {"name": "John", "age": 30}
print(mydict["name"])
 
mydict["city"] = "New York"
print(mydict)
 
del mydict["age"]
print(mydict)
 
for key, value in mydict.items():
    print(key, value)
 
# Python if...Else
a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")
 
x = 100
if x > 200:
    print("x is greater than 200")
elif x == 100:
    print("x is 100")
else:
    print("x is less than 100")
 
# Python Match (Python 3.10+)
x = 2
match x:
    case 1:
        print("x is 1")
    case 2:
        print("x is 2")
    case _:
        print("x is something else")
 
# Python While Loops
i = 0
while i < 5:
    print(i)
    i += 1
 
i = 0
while i < 5:
    print(i)
    if i == 3:
        break
    i += 1
 
# Python For Loops
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)
 
for i in range(5):
    print(i)
 
for x in thislist:
    if x == "banana":
        break
    print(x)