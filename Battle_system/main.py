#Tate Morgan Battle Simulator
import csv
from character_handling import chara_create, chara_delete, chara_select
from battles import battle







def main():
    while True:
        profile = input("Press 1 to use load a character, press 2 to create one, press 3 to delete one, or 4 to leave game: ")
        if profile == "1":
            player = chara_select()
            break
        elif profile == "2":
            chara_create()
        elif profile == "3":
            chara_delete()
        elif profile == "4":
            break
    print(f"You Have selected {player['Name']} Health {player['Health']}, Strength {player['Strength']}, Defense {player['Defense']}, Speed {player['Speed']}")
    begin = input("Will you continue. \npress 1 for yes or 2 for no: ")
    if begin == "1":
        battle(player)
    elif begin == "2":
        main()



main()