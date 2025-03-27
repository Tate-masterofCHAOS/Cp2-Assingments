#Tate Morgan Coin Change Problem
from converter import convert












def main():
    print("WELCOME TO MY SOLUTION TO THE COIN CHANGE PROBLEM")
    country = input("Press the number corresponding with the country are you translating from \n1. USA \n")
    target = float(input("How much money would you like to save for please write it in 5.25 form \n"))
    convert(country,target)


main()