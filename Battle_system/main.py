#Tate Morgan Battle Simulator

import csv
from character_handling import chara_manage
from battles import battle







def main():
    player = chara_manage()
    begin = input("Will you continue. \npress 1 for yes or 2 for no: ")
    if begin == "1":
        battle(player)
    elif begin == "2":
        main()
    main()



main()