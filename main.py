#Tate K. Morgan, Coin change problem

\
from coin_change_manager import coin_change_main as coin_change

def main():
    start = input("Would you like to convert currency(1) or exit(2): ")
    if start == "1":
        coin_change()
    elif start == "2":
        exit()
    else:
        print("Invalid input!")

while True:
    main()