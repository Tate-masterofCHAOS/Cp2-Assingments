#Tate Morgan's To Do list
#Create a to do list (Kept on a txt file)
#Add items to the to do list
#Mark item as complete
#Delete item from to do list
import csv


def add():
    with open("To_do\To_Do.txt", "a", newline="") as file:
        chore = input("What would you like to add to your to do list: ").lower()
        file.write(chore)
        file.write("\n")
    
    with open("To_do\To_Do.txt", "r") as file:
        print("Your updated To-Do list is as follow\n")
        print(file.read())

def mark():
    pass

def delete():
    task = input("Would you like to delete entire list or specific tasks. \nPress 1 for entire list \nPress 2 for a specific item \n")
    if task == "1":
        with open("To_do\To_Do.txt", "w") as file:
            file.write("")
            
    elif task == "2":
        with open("To_do\To_Do.txt", "w+") as file:
            chore = input("what is the task you desire to remove: ")
            file_list = file.read().split("\n")
            file_list.remove(chore)
            file.write(str(file_list))

            
        

def view():
    with open("To_do\To_Do.txt", "r") as file:
        print("Your updated To-Do list is as follow\n")
        print(file.read())


def main():
    while True:
        job = input("What would you like to do. \nPress 1 for adding chores. \nPress 2 for Marking off completed items. \nPress 3 to delete items. \nPress 4 to view list. \nPress 5 to exit\n")
        if job == "1":
            add()
        if job == "2":
            pass
        if job == "3":
            delete()
        if job == "4":
            view()
        if job == "5":
            break


main()