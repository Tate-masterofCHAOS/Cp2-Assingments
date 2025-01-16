#Stores all items in a list
#Function to add a new item
#Function to search the items
#Function to remove an item
#Function that runs the code (displays the menu options inside and calls the functions inside of a while True loop)
#Project must include
#easy to understand variable and function names
#Pseudocode comments explaining what the code is doing
#Good use of white space to keep items separate and easy to read/find
#Have at least 2 people test your code before submission!
books = ["officical legend of zelda historia", "mythology", "the school for good and evil"]
author = ["nintendo", "edith hamilton", "soman chainani"]
def main():
    
    job = input("Would you like to add, remove, or search for a book: ")
    job.lower
    if job == "add":
        books.append(input("What book do you wish to add: "))
        author.append(input("What is the author of the book you wish to add: "))
    elif job == "remove":
        book_remove = input("What book do you wish to remove: ")
        author_remove = input("What is the author of book you wish to remove: ")
        books.remove(book_remove)
        author.remove(author_remove)
    else:
        print("I am sorry that is not a function please double check your spelling")
    return books, author

main()