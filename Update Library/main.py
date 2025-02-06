#Each item in the dictionary should have AT LEAST 4 different details about it
#You should be able to update the different items in your dictionary
#There should be the option to print a simple list (Names and authors/artists/director) OR print a detailed list (Contains all the information)



def add(anime_library):
    name = input("What is the name of the anime: ")
    protagonist = input("What is the main character: ")
    antagonist = input("What is the name of the Main Villain or villin group:n")
    anime_library.append({"Name": name,
                       "Main Character": protagonist,
                       "Main Villain(s)": antagonist,})


def remove(anime_library):
    book = input("What book do you wish to remove: ")
    author = input("What is the author of book you wish to remove: ")
    anime_library.remove(book)
    anime_library.remove(author)




def main():
    anime_library = []
    while True:
        job = input("Would you like to add, remove, or search for a Anime: ").lower()
        if job == "add":
            add(anime_library)
        elif job == "search":
            print(anime_library)
        
        else:
            print("I am sorry that is not a function please double check your spelling")


main()