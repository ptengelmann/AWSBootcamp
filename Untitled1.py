"""
Your module description
"""

#Exercise 1

myString = "This is a string"
print(myString)

print(type(myString))

print(myString + " is of the data type " + str(type(myString)))

#Exercise 2 

first_string = "water "
second_string = "fall"
third_String = first_string + second_string
print(third_String)

name = input("What is your name? ")
print(name)

#Exercise 4 

color = input( "What is your favourite colour? ")
animal = input("what is your favourite animal? ")
action = input("What does it do? ")

print("{} you like a {} {} that {}!".format(name,color,animal,action))