#Main Menu for game
from pet_management import pet, pet_sprites, pet_selection


    









def main():
    print('Welcome to The Koro-Sensie pet lab where we biologically engineer each and every korosensei ready to be taken care of')
    current_koro = pet_selection()
    if current_koro.shade == '1':
        print(pet_sprites['pet_idle_normal'])
    
    
        


main()

