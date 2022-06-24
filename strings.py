

#clear terminal
import os
os.system('clear')

greetings = 'My Boss Yelled "GET BACK TO WORK!"'

print(greetings)

#or
greetings1 = "My Boss Yelled 'GET BACK TO WORK!'"

print(greetings1)

#or use escape character \ to ignore the next "

greetings2 = "My Boss Yelled \"GET BACK TO WORK!\""

print(greetings2)

#or use escape character and new line \n

greetings3 = "My Boss Yelled \n\"GET BACK TO WORK!\""

print(greetings3)

# concatenating strings and variables using the + character, note, only strings can be concatenated

name = "Robert"

greetings4 = "Hello my name is " + name

print(greetings4)

# python is an object oriented language, you can perform task against strings object example below

greetings5 = "Hello my name is Robert Joyner"

# upper() function, lower(), capitalize(), title(), swapcase() len() split()

print(greetings5.upper())

#or

print(greetings5.lower())

#or capitalize the first letter in the string object

print(greetings5.capitalize())

#or capitalize the first letter in each word of the string object

print(greetings5.title())

#or swapcase() will change the case of each character in the string object

print(greetings5.swapcase())

#or retrieve the length of your string object 

print(len(greetings5))

#or return specific characterfs in a string object

print(greetings5[24:30])

# split allow you to separate your string object by specific character

print(greetings5.split(" "))

#or print only a specific index in your object split

print(greetings5.split(" ")[5])

print(greetings5.split(" ")[4:6])