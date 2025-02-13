import csv




def print_require():
    length =""
    director = ""
    genre = ""
    while True:
        requirements = input("Press number according to what you want \n1: Length \n2: Director \n3: Genre \n4: move on \n")
        if requirements == "1":
            length = int(input("What is the length you want"))
        if requirements == "2":
            director = input("Who is the director you looking for")
        if requirements == "3":
            genre = input("What is the genre you looking for")
        if requirements == "4":
            break
    file = open("movie_rec\Movies list.csv","r").read()

    movies = {}

    with open("movie_rec\Movies list.csv") as file:
        reader = csv.reader(file)
        next(reader)
        if length != "":
            for i in reader:
                if int(i[4]) >= length:
                    movies.update({i[0]:i[1]})
                    print(i)
                    print("These movies match your length requirements")
        if director != "":
            for i in reader:
                if i[1] == director:
                    movies.update({i[0]:i[1]})
                    print(i)
                    print("These movies are made by your requested director")
        if i 
            
            
            



def main():
    require = input("Would you like to add search requirements or print all movies press 1 for search requirments and 2 for printing all: ")
    if require == "1":
        print_require()
         
    if require == "2":
        file = open("movie_rec\Movies list.csv","r").read()

        movies = {}

        with open("movie_rec\Movies list.csv") as file:
            reader = csv.reader(file)
            next(reader)
            for i in reader:
                movies.update({i[0]:i[1]})
                print(i)

main()