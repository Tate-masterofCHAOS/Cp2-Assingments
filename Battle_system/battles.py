import random
import time

player = ""

enemy_dialogue = ["kicks you", "punches you", "stomps on you", "Does a silly dance and somehow hurts you"]
enemies = [
    {"Name": "Soos", "Health": 30, "Strength": 5, "Defense": 5, "Speed": 5, "Description": "A middle aged handyman who is often confused for a hairless gopher"},
    {"Name": "Grunkle Stan", "Health": 30, "Strength": 5, "Defense": 5, "Speed": 5, "Description": "A totally trustable business man who puts the fun in no refunds"},
    {"Name": "Sprig", "Health": 30, "Strength": 5, "Defense": 5, "Speed": 5, "Description": "A small bipedal pink frog with a sense for adventure"},
    {"Name": "Apothacary Gary", "Health": 30, "Strength": 5, "Defense": 5, "Speed": 5, "Description": "A parisitic mushroom in a world of frogs, newts, and toads"},
    {"Name": "King", "Health": 30, "Strength": 5, "Defense": 5, "Speed": 5, "Description": "A small demon who says 'Weh' a lot"},
    {"Name": "Hooty", "Health": 30, "Strength": 5, "Defense": 5, "Speed": 5, "Description": "A giant tube-like owl with no care for others privacy"}
]

def heroes_turn(player, enemy):
    player_turn = input(print("Press numbers corresponding to the action you wish to use \n1: Attack \n2: Act \n3: Item \n4: Run \n"))
    if player_turn == "1":
        enemy['Health'] = enemy['Health'] - int(player['Strength'])
        if enemy['Health'] > 0:
            print(f"{enemy['Name']} is at {enemy['Health']}")
        elif enemy['Health'] <= 0:
            print(f"You beat {enemy['Name']}")
            encounter = False
        return enemy
    
    elif player_turn == "2":
        player_action = input(print("Press numbers corresponding to the action you wish to use \n1: Check \n2: Talk \n3: Back \n"))
        if player_action == "1":
            print(f"{enemy['Name']}    ATK: {enemy['Strength']}    DEF {enemy['Defense']}    {enemy['Description']}")
        elif player_action == "2":
            print(f"You try talking to {enemy['Name']} but they do not listen")
        elif player_action == "3":
            heroes_turn(player, enemy)

    elif player_turn == "3":
        player_use = input(print("Press numbers corresponding to the action you wish to use \n1: Cookie \n2: Snack \n3: Cake \n 4: Return"))
        if player_use == "1":
            if int(player['Health']) <= 25:
                int(player['Health']) + 5
                print("5 HP restored")
            elif int(player['Health']) >= 25:
                int(player['Health']) = 30
                print("HP fully restored")
        if player_use == "2":
            if int(player['Health']) <= 20:
                int(player['Health']) + 10
                print("5 HP restored")
            elif int(player['Health']) >= 20:
                int(player['Health']) = 30
                print("HP fully restored")
        if player_use == "3":
            int(player['Health']) = 30
            print("HP fully restored")
        if player_use == "4":
            heroes_turn(player, enemy)
            
    elif player_turn == "4":
        run = random.int(1,10)
        if run == 1:
            encounter = False
            print("You succesfully got away")
        elif run != 1:
            print("You could not get away")

def enemies_turn(player, enemy):
    print(f"{enemy['Name']} {random.choice(enemy_dialogue)}")
    player['Health'] = int(player['Health']) - enemy['Strength']
    print(f"{player['Name']} is at {player['Health']}")
    return player

def battle(player):
    encounter = True
    enemy = dict(random.choice(enemies))
    print(f"You have encountered {enemy['Name']}")
    while True:
        if encounter == True:
            heroes_turn(player, enemy)
            time.sleep(3)
            enemies_turn(player, enemy)
            time.sleep(3)
        elif encounter == False:
            break
         
    

