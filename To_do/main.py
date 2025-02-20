#Tate Morgan's To Do list
#Create a to do list (Kept on a txt file)
#Add items to the to do list
#Mark item as complete
#Delete item from to do list
import csv


def add():
    with open("To_do\To_Do.txt", "a", newline="") as file:
        writer = csv.writer(file)
        chore = input("What would you like to add to your to do list")
        writer.writerow(chore)
    
    with open("To_do\To_Do.txt", "r") as file:
        reader = csv.reader(file)
        print("Your updated To-Do list is as follow\n")
        for row in reader:
            print(f"{row}\n------------------------------")

def mark():
    pass


def delete():
    task = input("Would you like to delete entire list or specific tasks. \nPress 1 for entire list \nPress 2 for")
    if task == "1":
        with open("To_do\To_Do.txt", "w") as file:
            writer = csv.writer(file)
            writer.writerow("")


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
            pass
        if job == "5":
            break


main()