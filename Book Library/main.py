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



def add(books, authors):
    book = input("What book do you wish to add: ").lower()
    author = input("What is the author of the book you wish to add: ").lower()
    books.append(book)
    authors.append(author)
    return books, author

def remove(books, authors):
    book = input("What book do you wish to remove: ").lower()
    author = input("What is the author of book you wish to remove: ").lower()
    books.remove(book)
    authors.remove(author)



def main():
    books = []
    authors = []
    while True:
        job = input("Would you like to add, remove, or search for a book: ").lower()
        if job == "add":
            add(books, authors)
        elif job == "remove":
            remove(books,authors)
        elif job == "search" or "search for a book":
            path = input("would you like to search by book or author").lower
            if path == "book":
                book = input("What is the title of the book").lower()
                print(books)
                pass
        else:
            print("I am sorry that is not a function please double check your spelling")
    
main()
