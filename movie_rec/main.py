import csv




def open(length, director, genre):
    file = open("movie_rec\Movies list.csv","r").read()

    movies = {}

    with open("movie_rec\Movies list.csv") as file:
        reader = csv.reader(file)
        next(reader)
        for i in reader:
            if i[4] >= length:
                movies.update({i[0]:i[1]})
                print(i)



def main():
    require = input("Would you like to add search requirements or print all movies press 1 for search requirments and 2 for printing all: ")
    if require == "1":
        while True:
            requirements = input("Press number according to what you want \n1: Length \n2: Director \n3: Genre \n4: move on \n")
            if requirements == 1:
                length = input(int("What is the length you want"))
            if requirements == 2:
                director = input("Who is the director you looking for")
            if requirements == 3:
                genre = input("What is the genre you looking for")
            if requirements == 4:
                open(length, director, genre)
        
        
            
        
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