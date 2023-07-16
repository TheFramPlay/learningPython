# Learning to print
# print("Hello World")
# print("It's really good!")

# Learning Variables
# first_name = 'Harley'
# last_name = 'Garcia'
# full_name = first_name + ' ' + last_name
#
# print("Hello " + full_name)
# print(type(full_name))
# age = 26
# age += 1
#
# print("Your age is: " + str(age))
# print(type(age))

# height = 250.5
# print("Your height is: " + str(height) + "cm")
# print(type(height))

# human = True
# print("Are you a human: " + str(human))
# print(type(human))

# Multiple assignment = allows us to assign multiple variables at the same time in one line of code
# name = "Bro"
# age = 26
# attractive = True

# name, age, attractive = "Bro", 26, True
#
# print(name)
# print(age)
# print(attractive)

# name = "Harley"
# print(len(name))
# print(name.find("B"))
# print(name.capitalize())
# print(name.upper())
# print(name.lower())
# print(name.isdigit())
# print(name.isalpha())
# print(name.count('r'))
# print((name.replace("a","o")))
# print(name*3)

# type casting = convert the data type of a value to another data type
# x = 1    # int
# y = 2.0  # float
# z = "3"  # str
#
# print("X is " + str(x))
# print("X is " + str(y))
# print(z*3)

# print("Hello World")
# print(1+1)
# age = True
# print("Hi my name is, Harley, and I'm " + str(age) + " years old.")
# print(type(age))

# name = input(str("What is your name?"))
#
# if name == "Harley":
#     print("Hello, "+name +" I hope you had a great day today!")
# else:
#     print("Hope you had a terrible day!")
#

# First Lines Of Code From W3
"""
print("Hello World!")
if 5 > 2:
    print("Five is greater than two.")

if 5 > 2:
    print("Five is greater than two.")
"""
"""
I'm trying to be the best I can be!
"""

# x = 4.0
# print(type(x))
# print(str(x))

# x, y, z = "Orange", "Banana", "Cherry"
# print(x)
# print(y)
# print(z)

# harley = [26, "Harley", 'IT', 3]
# age, firstName, job, experience = harley
# print("Your age is " + str(age))
# print("Your name is " + firstName)
# print("You work in " + job)
# print("You have " + str(experience) + " years experience.")
#
# x = "Python"
# y = "is"
# z = "awesome"
# print(x, y, z)

# x = 26
# y = 24
# print(x-y)
#
# name = "You"
# age = 26
# print(name, age)
#
# print(name)
# def myfunc():
#     global name
#     name = "Harley"
#     print("My name is " + name)
#
# myfunc()
#
# print("My name is " + name)
#
# x = ("apple", "banana", "cherry")
# print(type(x))

# x = {"name" : "John", "age" : 36}
# print(type(x))
# vales = 2
# nomes = 3
# cn = complex(vales,nomes)
# print(cn)

# x = "Hello World"
# print(x[2:5])
#
# text = x.strip()
# print(text)

# x=b"Hello"
# print(x)
# print(type(x))

# x = 2.8
# a = int(x)
# print(a)

# import random
# print(random.randrange(1, 10))
#
# guess = int(input("Guess the number: "))

# age = '25'
# convertAge = int(age)
# print(age)
# print(type(age))
# print(convertAge)
# print(type(convertAge))

# import random
#
# randomNumber = random.randrange(1, 20)
# print(randomNumber)
# guess = int(input("Guess the number 1-20: "))
# if guess == randomNumber:
#     print("You Won!")
# elif not guess == randomNumber:
#     print("You Lost!")

# journey = """
# This is my programming journey.
# Thank you all for tuning in and supporting me.
# I know I will conquer my dreams!
# """
# print(journey)
# for x in "banana":
#     print(x)

# a = "Hello, World!"
# print(len(a))

# txt = "The best things in life are free!"
# print("love" in txt)

# txt = "I am loving python!"
# word = input("Word: ")
# if word in txt:
#     print("Yes, " + "'"+word + "'"+" is present.")
# elif word not in txt:
#     print("Sorry, " +"'"+ word + "'"+" is not present.")

# b = "Hello, World!"
# print(b[2:5])

# b = "Hello, World"
# print(b)

# a = " Hello, World! "
# print(a.strip())

# a = "Hello, World"
# print(a.replace("Hello", "Hola"))

# a = "Hello, World"
# print(a.split(","))

# a = "Hello"
# b = "World"
# c = a + " " + b
# print(c)

# age = 26
# txt = "My name is Yelrah, and I am {}"
# print(txt.format(age))

# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want {} pieces of item {} for {} dollars."
# print(myorder.format(quantity, itemno, price))
#
# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
# print(myorder.format(quantity, itemno, price))

# txt = "We are on an \"Amazing\" Python journey!"
# print(txt)

# txt = 'How was your day?'
# ending = txt.endswith(('?'))
# print(ending)
# print(txt.index('d'))

# print(bool("abc"))

# print(10 > 9) #true
# print(10 == 9) #false
# print(10 < 9) #false

# a = 200
# b = 33
#
# if b > a:
#   print("b is greater than a")
# else:
#   print("b is not greater than a")

# x = 33
# y = 27
#
# print(x <=27)

# x = (6/2 + 6*3)
# print(x)
# print(type(x))

# friends = ["Mr.Solver", "Alex the Wizard", "MightyD"]
# print(friends[0])
# print(len(friends))

# myCar = ["Kia", "Forte", 2013, 170000, True]
# print(myCar)
# myCar2 = list(("Nissan", "Sentra XE", 1994, 170000, True))
# print((myCar2))
# myCar[1] = "Sportage"
# print((myCar))

# print("Our first commit")

"""
Tuples used to store multiple items in a single variable.
Tuple is also an ordered collection that is immutable.
Tuples are written with ()
Allow duplicate values
Tuples can have any data type
type() is <class 'tuple'>
"""
# To create a tuple with a single item
# thistuple = ("apple",)

# Tuple constructor tuple()
# thistuple = tuple(()) #must use double parenthesis to construct

"""Indexing is the same as indexing through a list"""

# Check if item exists
# thistuple = ("apple", "pear", "orange", "banana")
# if "apple" in thistuple:
#     print("apple is in the tuple")

"""
Since tuples are immutable, there is a workaround
You can change a tuple to a list,
make the change to the list, 
then change it back to a tuple.
"""

# x = ("apple", "pear", "orange", "banana")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)
# print(x)

"""
To add items to a tuple, you will do the same thing
change tuple to list
use the append() method on the list
then convert it back to a tuple
"""

"""
You can add a tuple to a tuple
"""
# thistuple = ("apple", "banana", "cherry")
# y = ("orange",)
# thistuple += y
#
# print(thistuple)

"""
since you can't remove items from tuples
you must use the same method of converting to list
then remove the item and convert it back to 
a tuple

You can fully delete a tuple by using
the del keyword.
"""
# thistuple = ("apple", "banana", "cherry")
# del thistuple
# print(thistuple) #this will raise an error because the tuple no longer exists

"""
Unpacking - allows us to unpack the tuple and assign it to a new
variable name, respectively.
"""
# x = (1, 2, 3, 4)
# (green, yellow, red, blue) = x
#
# print(green)
# print(yellow)
# print(red)
# print(blue)

#Asterisk
"""
If the number of variables is less than the number of values,
you can add an * to the variable name and the values will be 
assigned to the variable as a list:
"""


# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
#
# (green, yellow, *red) = fruits
#
# print(green) #output apple
# print(yellow) #output banana
# print(red) #output ["cherry", "strawberry", "raspberry"]


"""
If the asterisk is added to another variable name than the 
last, Python will assign values to the variable until the 
number of values left matches the number of variables left.
"""

# fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
#
# (green, *tropic, red) = fruits
#
# print(green)
# print(tropic)
# print(red)

# for loop

# thistuple = ("apple", "banana", "cherry")
# for x in thistuple:
#     print(x)

# loop through index
# thistuple = ("apple", "banana", "cherry")
# for i in range(len(thistuple)):
#     print(thistuple[i])

# thistuple = ("apple", "banana", "cherry")
# i = 0
# while i < len(thistuple):
#     print(thistuple[i])
#     i += 1