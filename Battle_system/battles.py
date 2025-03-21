import random
import time

player = ""

enemy_dialogue = ["kicks you", "punches you", "stomps on you", "Does a silly dance and somehow hurts you"]
enemies = [
    {"Name": "Soos", "Health": 30, "Strength": 5, "Defense": 5, "Speed": 5},
    {"Name": "Grunkle Stan", "Health": 30, "Strength": 5, "Defense": 5, "Speed": 5},
    {"Name": "Sprig", "Health": 30, "Strength": 5, "Defense": 5, "Speed": 5},
    {"Name": "King", "Health": 30, "Strength": 5, "Defense": 5, "Speed": 5},
]

def heroes_turn(player, enemy):
    player_turn = input(print("Press numbers corresponding to the action you wish to use \n1: Attack \n2: Act \n3: Item \n4: Run \n"))
    if player_turn == "1":
        enemy['Health'] = enemy['Health'] - int(player['Strength'])
        print(f"{enemy['Name']} is at {enemy['Health']}")
        return enemy
    elif player_turn == "2":
        player_action = input(print("Press numbers corresponding to the action you wish to use \n1: Check \n2: Talk \n3: Back \n"))
        if player_action == "1":
            print(f"{enemy['Name']}    ATK: {enemy['Strength']}    DEF {enemy['Defense']}")
        elif player_action == "2":
            pass
        elif player_action == "3":
            heroes_turn(player, enemy)
    elif player_turn == "3":
        pass
    elif player_turn == "4":
        pass

def enemies_turn(player, enemy):
    print(f"{enemy['Name']} uses {random.choice(enemy_dialogue)}")
    player['Health'] = int(player['Health']) - enemy['Strength']
    print(f"{player['Name']} is at {player['Health']}")
    return player

def battle(player):
    enemy = dict(random.choice(enemies))
    print(f"You have encountered {enemy['Name']}")
    while True:
        heroes_turn(player, enemy)
        time.sleep(3)
        enemies_turn(player, enemy)
        time.sleep(3)
         
    

