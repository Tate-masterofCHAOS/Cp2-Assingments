#Main Menu for game
from pet_management import *


    









def main():
    print('Welcome to The Koro-Sensie pet lab where we biologically engineer each and every korosensei ready to be taken care of by you!\n')
    choice = input('Would you like to create a new pet or load an existing one? (1/2) ').lower()
    if choice == '1':
        current_koro = pet_selection()
        print(current_koro)
    elif choice == '2':
        current_koro = pet_creation()
    if current_koro.shade == 'normal':
        print(pet_sprites['pet_idle_normal'])
    elif current_koro.shade == 'X faced':
        print(pet_sprites['pet_idle_x'])
    elif current_koro.shade == 'O faced':
        print(pet_sprites['pet_idle_o'])
    print(f'\n{current_koro.name} comes running over at your call')
    while True:
        decrease_time = random.randint(30, 120)
        choice = input('What would you like to do? (1: Feed, \n2: Play, \n3: Sleep, \n4: Check Status, \n5. Change pet, \n6. Quit) \n')
    
    
        


main()

