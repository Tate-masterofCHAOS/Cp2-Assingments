import random

player = ""

enemies = [
    {"Name": "Soos", "Health": "30", "Strength": "5", "Defense": "5", "Speed": "5"},
    {"Name": "Grunkle Stan", "Health": "30", "Strength": "5", "Defense": "5", "Speed": "5"},
    {"Name": "Sprig", "Health": "30", "Strength": "5", "Defense": "5", "Speed": "5"},
    {"Name": "King", "Health": "30", "Strength": "5", "Defense": "5", "Speed": "5"},
]


def battle(player):
    enemy = dict(random.choice(enemies))
    print(f"You have encountered {enemy['Name']}")
    player_turn = input(print("Press numbers corresponding to the action you wish to use \n1: Attack \n2: Act \n 3: Item \n4: Run"))
    if player_turn == "1":
        enemy["Health"] - player["Strength"]
        print(f"{enemy['Name']} is at {enemy['Health']}")
    if player_turn == "2":
        pass
    if player_turn == "3":
        pass
    if player_turn == "4":
        pass

