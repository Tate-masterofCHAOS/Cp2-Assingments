#Each item in the dictionary should have AT LEAST 4 different details about it
#You should be able to update the different items in your dictionary
#There should be the option to print a simple list (Names and authors/artists/director) OR print a detailed list (Contains all the information)



def add(anime_library):
    name = input("What is the name of the anime: ").lower()
    protagonist = input("What is the main character: ").lower()
    antagonist = input("What is the name of the Main Villain or villin group: ").lower()
    gimmick = input("What is the main gimmik: ").lower()
    anime_library.append({"Name": name,
                       "Main Character": protagonist,
                       "Main Villain(s)": antagonist,
                       "Main Gimmick": gimmick})


def remove(anime_library):
    name = input("What is the name of the anime: ")
    protagonist = input("What is the main character: ")
    antagonist = input("What is the name of the Main Villain or villin group: ")
    gimmick = input("What is the main gimmik: ")
    anime_library.remove({"Name": name,
                       "Main Character": protagonist,
                       "Main Villain(s)": antagonist,
                       "Main Gimmick": gimmick})


def search(anime_library):
    name = input("What is the name of the anime")
    for i in anime_library:
        if i == name:
            print({i,i[1],i[2],i[3]})


def main():
    anime_library = []
    while True:
        job = input("Would you like to add, remove, or search for a Anime, you could also say leave to leave: ").lower()
        if job == "add":
            add(anime_library)
        elif job == "remove":
            remove(anime_library)
        elif job == "search":
            search(anime_library)
        elif job == "leave":
            break
        else:
            print("I am sorry that is not a function please double check your spelling")


main()