#Main Menu for game
from pet_management import *


    









def main():
    print('Welcome to The Koro-Sensie pet lab where we biologically engineer each and every korosensei ready to be taken care of by you!\n')
    choice = input('Would you like to create a new pet or load an existing one? (1/2) ').lower()
    if choice == '1':
        current_koro = pet_selection(pet_choice())
        print(current_koro)
    elif choice == '2':
        current_koro = pet_creation()
    if current_koro.shade == '1':
        print(pet_sprites['pet_idle_normal'])
    print(f'\n{current_koro.name} comes running over at your call')
    
    
        


main()

