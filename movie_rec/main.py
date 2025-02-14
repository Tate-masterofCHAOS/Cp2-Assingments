import csv



#This function uses the variables in order to print specific movies
def print_require(length, director, genre, title):
    
    file = open("movie_rec\Movies list.csv","r").read()

    movies = {}
    #This is what reads your requirements and prints them
    with open("movie_rec\Movies list.csv") as file:
        reader = csv.reader(file)
        next(reader)
        for i in reader:
            if int(i[4]) >= length and  director in i[1].lower() and genre in i[2].lower() and title in i[0].lower():
                movies.update({i[0]:i[1]})
                print(i)
        print("These movies match your requirements")
            
            
            



def main():
    while True:
        require = input("Would you like to add search requirements or print all movies press 1 for search requirments and 2 for printing all: ")
        if require == "1":
            #This is what I use to gather information
            length = 1
            director = ""
            genre = ""
            title = ""
            while True:
                requirements = input("Press number according to what you want \n1: Length \n2: Director \n3: Genre \n4: Title \n5: Move on \n6: Leave ")
                if requirements == "1":
                    length = int(input("What is the length you want: "))
                if requirements == "2":
                    director = input("Who is the director you looking for: ").lower()
                if requirements == "3":
                    genre = input("What is the genre you looking for: ").lower()
                if requirements == "4":
                    title = input("What is the Title you looking for: ").lower()
                if requirements == "5":
                    print_require(length, director, genre, title)
                    break
                if requirements == "6":
                    return
            
        #This Prints all things
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