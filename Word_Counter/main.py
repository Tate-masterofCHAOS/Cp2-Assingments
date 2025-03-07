#Tate Morgan, Word Counter
import os


from time_handling import time_set #Imports the function that returns the time

from file_handling import count_words, add_file, remove_file, reset_file, display_file #Imports all the functions that handle the files

def main():
    
    print("""
    Choices
    1. Add to File
    2. Remove From File
    3. Reset File
    4. Display File
    5. Exit
    """)

    choice = input("\nChoose a Number: ")

    if choice == "1":
        add_file(user_file)
        print("\n",count_words(user_file))#Prints out the amount of words in the file
        print(time_set())#Prints out the time that the amount of words was checked
    elif choice == "2":
        remove_file(user_file)
        print("\n",count_words(user_file))
        print(time_set())
    elif choice == "3":
        reset_file(user_file)
        print("\n",count_words(user_file))
        print(time_set())
    elif choice == "4":
        display_file(user_file)
        print("\n",count_words(user_file))
        print(time_set())
    elif choice == "5":
        exit()
    else:
        print("Not an Option\n")


user_file = input("Input a relative path for a text file: ")

file_good = False

while file_good == False: #This part checks if a user's input is an existing file path and makes them input an exising file path
    exists = os.path.isfile(user_file)

    if exists == False:
        print("Not a File Path... Try Again")
        user_file = input("Input a relative path for a text file: ")#Asks the user for a File Path Again
    else:
        file_good = True


while True:
    main()