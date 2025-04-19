#Main Menu for game
from pet_management import *
from time import sleep
import threading
import random
from rick import rick



def main():
    temp = 0
    print('Welcome to The Koro-Sensie pet lab where we biologically engineer each and every korosensei ready to be taken care of by you!\n')
    choice = input('Would you like to create a new pet or load an existing one? (1/2) ').lower()
    if choice == '1':
        current_koro = pet_creation()
    elif choice == '2':
        current_koro = pet_selection()
        print(current_koro)
    Event_timer = threading.Timer(random.randint(60,180), random_events, args=(current_koro,))
    Event_timer.start()
    Stat_timer = threading.Timer(random.randint(60,120), stat_update, args=(current_koro,))
    Stat_timer.start()
    while True:
        if Event_timer.is_alive() == True and Stat_timer.is_alive() == True:
            if current_koro.shade == 'normal':
                print(pet_sprites['pet_idle_normal'])
            elif current_koro.shade == 'X faced':
                print(pet_sprites['pet_idle_X'])
            elif current_koro.shade == 'O faced':
                print(pet_sprites['pet_idle_O'])
            elif current_koro.shade == 'Rick':
                print('Hello Mrs. Larose you have made a grave error choosing this pet, this will last around 3-5 seconds when it stops I recommend you choose another pet')
                time.sleep(5)
                rick()
            print(f'\n{current_koro.name} comes running over at your call')
            choice = int(input('What would you like to do? \n1: Feed, \n2: Play, \n3: Sleep, \n4: Check Status, \n5. Change pet, \n6. Fly(Requires level 2) \n7. Melt(Requires level 5) \n8. Quit \n'))
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
                if current_koro.level >= 2:
                    fly()
                else:
                    print('Your pet is not leveled up enough to fly')
                    time.sleep(2)
            elif choice == 7:
                if current_koro.level >= 5:
                    melt()
                else:
                    print('Your pet is not leveled up enough to melt')
                    time.sleep(2)
            elif choice == 8:
                print('Thanks for playing!')
                save_pet(current_koro)
                quit()
        elif Event_timer.is_alive() == False and Stat_timer.is_alive() == False:
            Event_timer = threading.timer(random.randint(60,180), random_events, args=(current_koro,)).start()
            Stat_timer = threading.timer(random.randint(60,120), stat_update, args=(current_koro,)).start()
        elif Event_timer.is_alive(Event_timer) == False:
            Event_timer = threading.timer(random.randint(60,180), random_events, args=(current_koro,)).start()
        elif Stat_timer.is_alive() == False:
            Stat_timer = threading.timer(random.randint(60,120), stat_update, args=(current_koro,)).start()
        while current_koro.time_alive >= 3:
            print('Your pet has leveled up!')
            current_koro.level += 1
            temp += current_koro.time_alive
            current_koro.time_alive -= 3
            
    
        


main()