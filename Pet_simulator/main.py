#Main Menu for game
from pet_management import *
from time import sleep
from threading import Timer

class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.start()
    
    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)
    
    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True
    
    def stop(self):
        self._timer.cancel()
        self.is_running = False





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
        rt = RepeatedTimer(random.randint(30,120), stat_update(current_koro)) # it auto-starts, no need of rt.start()
        try:
            stat_update(current_koro)
        finally:
            rt.stop()
            choice = input('What would you like to do? \n1: Feed, \n2: Play, \n3: Sleep, \n4: Check Status, \n5. Change pet, \n6. Quit \n')
            if choice == 1:
                pass
            elif choice == 2:
                pass
            elif choice == 3:
                pass
            elif choice == 4:
                current_koro.stat_check()
            elif choice == 5:
                print('You have chosen to change your pet')
                current_koro = pet_selection()
                print(current_koro)
            elif choice == 6:
                print('Thanks for playing!')
                quit()
    
    
        


main()

