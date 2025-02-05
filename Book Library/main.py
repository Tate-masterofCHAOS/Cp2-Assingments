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

def add(libarby):
    book = input("What book do you wish to add: ")
    author = input("What is the author of the book you wish to add: ")
    libarby.add(book)
    libarby.add(author)


def remove(libarby):
    book = input("What book do you wish to remove: ")
    author = input("What is the author of book you wish to remove: ")
    libarby.remove(book, "by", author)

def search(libarby,):
        book = input("What is the title of the book: ").lower()
        for i in libarby:
            if i == book:
                print(libarby)
            else:
                print("Sorry that is not in our library")


def main():
    libarby = set({""})
    while True:
        job = input("Would you like to add, remove, or search for a book: ")
        job.lower
        if job == "add":
            add(libarby)
        elif job == "remove":
            remove(libarby)
        elif job == "search" or "search for a book":
            search(libarby)
        else:
            print("I am sorry that is not a function please double check your spelling")
    
main()
