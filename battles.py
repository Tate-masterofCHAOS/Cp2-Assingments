import random

player = ""

enemies = [
    {"Name": "Soos", "Health": "5", "Strength": "5", "Defense": "5", "Speed": "5"},
    {"Name": "Grunkle Stan", "Health": "5", "Strength": "5", "Defense": "5", "Speed": "5"},
    {"Name": "Sprig", "Health": "5", "Strength": "5", "Defense": "5", "Speed": "5"},
    {"Name": "King", "Health": "5", "Strength": "5", "Defense": "5", "Speed": "5"},
]


def battle(player):
    enemy = random.choice(enemies)
    print(enemy)

battle(player)