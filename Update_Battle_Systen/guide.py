#Tate Morgan Battle Simulator


from small_functions import *


def stat_explain():
    print("""
Stats:
Strength: how much damage you do (with slight variation)
Defense: how much damage you block (with slight variation)
Health: how much damage you can take
Speed: increases chance of taking no damage
""")



def leveling_explain():
    print("""
You gain levels when you beat someone else.
You can spend skill points on characters depending on their level.
strength points increase strength by 2
defense points increase defense by 1
health points upgrade health by 5
speed points upgrade speed by 1
""")



def main():
    while True:
      
        print("""
Welcome to Battle Simulator!
This is a school project made by Alec
What would you like to learn about? Type:
1 to learn about stats and what they do
2 to learn about leveling and related mechanics
3 to exit the guide
Your answer here:""")
        choice = input()
        cs()
        if choice == "1":
            stat_explain()

        elif choice == "2":
            leveling_explain()

        elif choice == "3":
            break

        else:
            print("\ninvalid input")