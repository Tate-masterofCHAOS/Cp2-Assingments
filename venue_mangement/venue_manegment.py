#Tate Morgan venue management stuff


stages = set()
#This is my function to add a location
def add_stage():
    stages.add(input("What location would you like to add: ").lower)
    return


#this is my function to drop a location
def remove_stage():
    locations.remove( input("What location would you like to remove: ").lower())
    pass


#This is my function to check the equipment and stage name of who it owns it
def equipment():
    pass


#This is my main function
def venue_managementMAIN():
    while True:
        choice = input("Would you like to manage stages or equipment: ").lower()
        if choice == "location":
            location = input("Would you like to add, remove, or view stages: ").lower()
            if location == "add":
                add_stage()
            elif location == "remove":
                remove_stage()
            elif location == "view":
                print(locations)
        if choice == "stage names":
        pass


venue_managementMAIN()
#here after used it will go to ticket sales and admission