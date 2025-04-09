#Tate Morgan Battle System


from small_functions import *
from guide import main as guide
from profile_management import main as manage_profiles
from battling import main as battle



def main():
    while True:
        
        choice = is_int(input("""
Welcome to battle simulator!
What would you like to do? Type:
1 to battle someone else
2 to manage/create/view profiles
3 to learn what you're doing
4 to exit
Your answer here: """))
        if choice == 1:
            battle()

        elif choice == 2:
            manage_profiles()

        elif choice == 3:
            guide()

        elif choice == 4:
            break


main()