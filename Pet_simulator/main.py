#Main Menu for game
from pet_management import *
from time import sleep
from threading import Timer
import random
from rick import rick



def main():
    print('Welcome to The Koro-Sensie pet lab where we biologically engineer each and every korosensei ready to be taken care of by you!\n')
    choice = input('Would you like to create a new pet or load an existing one? (1/2) ').lower()
    if choice == '1':
        current_koro = pet_creation()
    elif choice == '2':
        current_koro = pet_selection()
        print(current_koro)
    Timer(random.randint(60,180), random_events, args=(current_koro,)).start()
    Timer(random.randint(60,120), stat_update, args=(current_koro,)).start()
    while True:
        if current_koro.shade == 'normal':
            print(pet_sprites['pet_idle_normal'])
        elif current_koro.shade == 'X faced':
            print(pet_sprites['pet_idle_X'])
        elif current_koro.shade == 'O faced':
            print(pet_sprites['pet_idle_O'])
        elif current_koro.shade == 'Rick':
            print('Hello Mrs. Larose you have made a grave error choosing this pet, to exit what shall open just hold X and when it stops I recommend you choose another pet')
            time.sleep(5)
            rick()
        print(f'\n{current_koro.name} comes running over at your call')
        choice = int(input('What would you like to do? \n1: Feed, \n2: Play, \n3: Sleep, \n4: Check Status, \n5. Change pet, \n6. Quit \n'))
        if choice == 1:
            current_koro.feed()
        elif choice == 2:
            current_koro.play()
        elif choice == 3:
            current_koro.sleep()
        elif choice == 4:
            print(current_koro.stat_check())
        elif choice == 5:
            print('You have chosen to change your pet')
            current_koro = pet_selection()
            print(current_koro)
        elif choice == 6:
            print('Thanks for playing!')
            save_pet(current_koro)
            quit()
    
    
        


main()