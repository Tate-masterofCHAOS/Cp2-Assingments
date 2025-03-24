import csv

characters = [
    {"Name": "Dipper Pines", "Health": 30, "Strength": 5, "Defense": 5, "Speed": 5, "Level": 1},
    {"Name": "Mable Pines", "Health": 30, "Strength": 5, "Defense": 5, "Speed": 5, "Level": 1},
    {"Name": "Anne Boonchuy", "Health": 30, "Strength": 5, "Defense": 5, "Speed": 5, "Level": 1},
    {"Name": "Luz Noceda", "Health": 30, "Strength": 5, "Defense": 5, "Speed": 5, "Level": 1},
    {"Name": "Tate Morgan", "Health": 30, "Strength": 30, "Defense": 5, "Speed": 5, "Level": 1}
]



def chara_update(player,characters):
    with open("Battle_system/chara.csv", "w+", newline="") as file:
        fieldnames = ["Name", "Health", "Strength", "Defense", "Speed", "Level"]
        reader = csv.reader(file)
        for row in reader:
            if row[0] == player[0]:
                row[1,2,3,4,5] = player[1,2,3,4,5]
                file.write(row)
            else:
                file.write(row)
    with open("Battle_system/chara.csv", "r") as file:
        reader = csv.reader(file)
        for row in file:
            if row == 1:
                pass
            elif row == 2:
                characters = [{"Name": row[0], "Health": row[1], "Strength": row[2], "Defense": row[3], "Speed": row[4], "Level": 1}]
            else:
                characters.insert(player = {"Name": row[0], "Health": row[1], "Strength": row[2], "Defense": row[3], "Speed": row[4], "Level": 1})
            

def chara_create():
    chara = input("What is the characters name: ")
    hp = input("What is the characters health: ")
    str = input("What is the characters strength: ")
    df = input("What is the characters defense: ")
    spd = input("What is the characters speed: ")
    characters.append({"Name": chara, "Health": hp, "Strength": str, "Defense": df, "Speed": spd, "Level": 1})
    with open("Battle_system\chara.csv", "w", newline="") as file:
        fieldnames = ["Name", "Health", "Strength", "Defense", "Speed", "Level"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(characters)


def chara_delete():
    chara = input("What is the name of the character you wish to delete: ")
    for i in characters:
        if i == chara:
            characters.remove(i)
        else:
            continue
    with open("Battle_system\chara.csv", "w", newline="") as file:
        fieldnames = ["Name", "Health", "Strength", "Defense", "Speed", "Level"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(characters)

def chara_select():
    with open("Battle_system/chara.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"Name: {row[0]} Health: {row[1]} Strength: {row[2]} Defense: {row[3]} Speed: {row[4]} Level {row[5]}\n---------------------\n")
    desision = input("Choose your character: ")
    with open("Battle_system/chara.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == desision:
                player = {"Name": row[0], "Health": row[1], "Strength": row[2], "Defense": row[3], "Speed": row[4], "Level": 1}
                return player
            else:
                continue