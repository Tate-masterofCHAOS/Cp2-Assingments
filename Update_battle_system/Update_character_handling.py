import csv
from tempfile import NamedTemporaryFile
import shutil

characters = [
    {"Name": "Dipper Pines", "Health": 60, "Strength": 25, "Defense": 65, "Speed": 80, "Level": 1},
    {"Name": "Mable Pines", "Health": 100, "Strength": 15, "Defense": 60, "Speed": 120, "Level": 1},
    {"Name": "Anne Boonchuy", "Health": 110, "Strength": 102, "Defense": 55, "Speed": 85, "Level": 1},
    {"Name": "Luz Noceda", "Health": 150, "Strength": 30, "Defense": 120, "Speed": 15, "Level": 1},
    {"Name": "Tate Morgan", "Health": 1500, "Strength": 1500, "Defense": 1500, "Speed": 1500, "Level": 1}
]



def chara_update(player,characters):
    filename = 'Update_battle_system/Update_chara.csv'
    tempfile = NamedTemporaryFile(mode='w', delete=False)

    fields = ['Name', 'Health', 'Strength', 'Defense', 'Speed', 'Level']

    with open(filename, 'r') as csvfile, tempfile:
        reader = csv.DictReader(csvfile, fieldnames=fields)
        writer = csv.DictWriter(tempfile, fieldnames=fields)
        for row in reader:
            if row['Name'] == player['Name']:
                row['Name'], row['Health'], row['Strength'], row['Defense'], row['Speed'], row['Level'] = player['Name'], player['Health'], player['Strength'], player['Defense'], player['Speed'], player['Level']
            row = {'Name': row['Name'], 'Health': row['Health'], 'Strength': row['Strength'], 'Defense': row['Defense'], 'Speed': row['Speed'], 'Level': row['Level']}
            writer.writerow(row)

    shutil.move(tempfile.name, filename)

            

def chara_create():
    chara = input("What is the characters name: ")
    hp = input("What is the characters health: ")
    str = input("What is the characters strength: ")
    df = input("What is the characters defense: ")
    spd = input("What is the characters speed: ")
    characters.append({"Name": chara, "Health": hp, "Strength": str, "Defense": df, "Speed": spd, "Level": 1})
    with open("Update_battle_system/Update_chara.csv", "w", newline="") as file:
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
    with open("Update_battle_system/Update_chara.csv", "w", newline="") as file:
        fieldnames = ["Name", "Health", "Strength", "Defense", "Speed", "Level"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(characters)

def chara_select():
    with open("Update_battle_system/Update_chara.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"Name: {row[0]} Health: {row[1]} Strength: {row[2]} Defense: {row[3]} Speed: {row[4]} Level {row[5]}\n---------------------\n")
    desision = input("Choose your character: ")
    with open("Update_battle_system/Update_chara.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == desision:
                player = {"Name": row[0], "Health": row[1], "Strength": row[2], "Defense": row[3], "Speed": row[4], "Level": 1}
                return player
            else:
                continue