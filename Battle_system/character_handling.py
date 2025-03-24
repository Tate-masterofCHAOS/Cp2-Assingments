import csv

characters = [
    {"Name": "Dipper Pines", "Health": 5, "Strength": 5, "Defense": 5, "Speed": 5},
    {"Name": "Mable Pines", "Health": 5, "Strength": 5, "Defense": 5, "Speed": 5},
    {"Name": "Anne Boonchuy", "Health": 5, "Strength": 5, "Defense": 5, "Speed": 5},
    {"Name": "Luz Noceda", "Health": 5, "Strength": 5, "Defense": 5, "Speed": 5},
]


def chara_create():
    chara = input("What is the characters name: ")
    hp = input("What is the characters health: ")
    str = input("What is the characters strength: ")
    df = input("What is the characters defense: ")
    spd = input("What is the characters speed: ")
    characters.append({"Name": chara, "Health": hp, "Strength": str, "Defense": df, "Speed": spd})
    with open("Battle_system\chara.csv", "w", newline="") as file:
        fieldnames = ["Name", "Health", "Strength", "Defense", "Speed"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(characters)
    with open("Battle_system\chara.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"Name: {row[0]} Health: {row[1]} Strength: {row[2]} Defense: {row[3]} Speed: {row[4]}\n---------------------\n")


def chara_delete():
    chara = input("What is the name of the character you wish to delete: ")
    for i in characters:
        if i == chara:
            characters.remove(i)
        else:
            continue
    with open("Battle_system\chara.csv", "w", newline="") as file:
        fieldnames = ["Name", "Health", "Strength", "Defense", "Speed"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(characters)

def chara_select():
    with open("Battle_system/chara.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"Name: {row[0]} Health: {row[1]} Strength: {row[2]} Defense: {row[3]} Speed: {row[4]}\n---------------------\n")
    desision = input("Choose your character: ")
    with open("Battle_system/chara.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == desision:
                player = {"Name": row[0], "Health": row[1], "Strength": row[2], "Defense": row[3], "Speed": row[4]}
                return player
            else:
                continue