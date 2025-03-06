#Tate Morgan, Multiple page notes

#1. How do you make multiple files in python?
    #Make a new file ending in .py
    #snake case names
    #Descriptive file name (short)

#2. How do you get a function from another file
    #from file import * to import all
    #from file import function to import a specific function
    #use as to change the name of function
    #you can import variables though shamed upon
from calc import addition as add, subtraction as sub
print(add())
#3. How do you get variables from another file?
    #just add it to the list
from calc import num
print(sub(num,8))
#4. How do you have a function with multiple returns?
    #
def get_user_info():
    name = input("What is your name\n")
    age = input("How old are you\n")
    social_security = input("What is your social security number\n")
    return name, age, social_security

name, age, social_security = get_user_info()

print(social_security)
#5. Why would you use multiple pages for a python project?
    #easier to merge github pages
    #modularity - break the program into easier more managable peices
    #main should only include the introduction and user interface
    #funcionality
    



