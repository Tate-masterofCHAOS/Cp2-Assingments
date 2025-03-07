#Tate Morgan, Word Counter

def count_words(user_file):
    with open(user_file, "r",) as file:
        words = 0
        file = file.read()

        rows = file.split()
        words += len(rows)#Adds to the variable the amount of words in the file
    if words > 1 or words < 1:  
        return"There are " + str(words) + " words" #Returns the amount of words in a string
    else:
        return"There is " + str(words) + " word"


def add_file(user_file):
    adding = input("What do you want to add to the file: ")
            
    with open(user_file, "a") as file:
        file.write(adding + "\n")#Adds to the file


def remove_file(user_file):
    with open(user_file, "r+",) as file:
        removing = input("What do you want to remove from the file: ")

                
        for item in file: 
            if removing in item:# Checks every row in the file to see if it contains what is being removed
                with open(user_file, "r") as f:
                    lines = f.readlines()
                with open(user_file, "w") as f:
                    for line in lines:
                        if line.strip("") != item:
                            f.write(line)#Rewrites the file without the thing that is being removed
                
            print("\nRemoved Item")


def reset_file(user_file):
    open(user_file, "w").close()#Erases all the content on the file


def display_file(user_file):
    with open(user_file, "r",) as file:# Prints out the contents of the file nicely
        file = file.read()
        print("\nFile:")
        print(file)