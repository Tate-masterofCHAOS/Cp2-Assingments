#Main Menu for game
from pet_management import *
from time import sleep
import threading
import random




def main():
    temp = 0
    while True:
        print('Welcome to The Koro-Sensie pet lab where we biologically engineer each and every korosensei ready to be taken care of by you!\n')
        choice = input('Would you like to create a new pet or load an existing one? (1/2) ').lower()
        if choice == '1':
            current_koro = pet_creation()
        elif choice == '2':
            current_koro = pet_selection()
            print(current_koro)
        else:
            print('Invalid choice, please try again.')
            main()
        home(current_koro)
            
    
        


main()