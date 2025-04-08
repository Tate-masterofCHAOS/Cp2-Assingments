import csv
from tempfile import NamedTemporaryFile
import shutil
from faker import Faker
import random
fake = Faker()

characters = [
    {"Name": "Dipper Pines", "Health": 30, "Strength": 5, "Defense": 5, "Speed": 5, "Level": 1, "Description": "A young boy who loves mystery"},
    {"Name": "Mable Pines", "Health": 30, "Strength": 5, "Defense": 5, "Speed": 5, "Level": 1, "Description": "A young girl who loves being weird"},
    {"Name": "Anne Boonchuy", "Health": 30, "Strength": 5, "Defense": 5, "Speed": 5, "Level": 1, "Description": "A teenage girl stuck in a world of frogs, newts, and toads"},
    {"Name": "Luz Noceda", "Health": 30, "Strength": 5, "Defense": 5, "Speed": 5, "Level": 1, "Description": "A teenage girl stuck in a world of demons and magic trying to become a witch"},
    {"Name": "Tate Morgan", "Health": 30, "Strength": 30, "Defense": 5, "Speed": 5, "Level": 1, "Description": "Dev character purposefully unbeatable"}
]


def chara_update(player,characters):
    filename = 'Battle_system/chara.csv'
    tempfile = NamedTemporaryFile(mode='w', delete=False)

    fields = ['Name', 'Health', 'Strength', 'Defense', 'Speed', 'Level', 'Description']

    with open(filename, 'r') as csvfile, tempfile:
        reader = csv.DictReader(csvfile, fieldnames=fields)
        writer = csv.DictWriter(tempfile, fieldnames=fields)
        for row in reader:
            if row['Name'] == player['Name']:
                row['Name'], row['Health'], row['Strength'], row['Defense'], row['Speed'], row['Level'], row['Description'] = player['Name'], player['Health'], player['Strength'], player['Defense'], player['Speed'], player['Level'], player['Description']
            row = {'Name': row['Name'], 'Health': row['Health'], 'Strength': row['Strength'], 'Defense': row['Defense'], 'Speed': row['Speed'], 'Level': row['Level'], 'Description': row['Description']}
            writer.writerow(row)

    shutil.move(tempfile.name, filename)

            
def chara_manage():
    profile = input("Press 1 to use load a character, press 2 to create one, press 3 to delete one, or 4 to leave game: ")
    if profile == "1":
        def chara_select():
            with open("Battle_system/chara.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    print(f"Name: {row[0]} Health: {row[1]} Strength: {row[2]} Defense: {row[3]} Speed: {row[4]} Level {row[5]}, Description {row[6]}\n---------------------\n")
            desision = input("Choose your character: ")
            with open("Battle_system/chara.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == desision:
                        player = {"Name": row[0], "Health": row[1], "Strength": row[2], "Defense": row[3], "Speed": row[4], "Level": row[5], 'Description': row[6]}
                        return player
                    else:
                        continue
        player = chara_select()
    elif profile == "2":
        def chara_create():
            create = input("Would you like to create a custom character or have one be generated randomly \npress 1 for custom or 2 for random\n")
            if create == "1":
                chara = input("What is the characters name: ")
                hp = input("What is the characters health: ")
                str = input("What is the characters strength: ")
                df = input("What is the characters defense: ")
                spd = input("What is the characters speed: ")
                description = input("Describe your character")
            elif create == "2":
                chara = fake.name()
                hp = random.randint(50,150)
                str = random.randint(50,150)
                df = random.randint(50,150)
                spd = random.randint(50,150)
                description = fake.text()
            characters.append({"Name": chara, "Health": hp, "Strength": str, "Defense": df, "Speed": spd, "Level": 1, "Description": description})
            with open("Battle_system\chara.csv", "w", newline="") as file:
                fieldnames = ["Name", "Health", "Strength", "Defense", "Speed", "Level", "Description"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(characters)
            chara_manage()
        chara_create()
    elif profile == "3":
        def chara_delete():
            chara = input("What is the name of the character you wish to delete: ")
            for i in characters:
                if i == chara:
                    characters.remove(i)
                else:
                    continue
            with open("Battle_system\chara.csv", "w", newline="") as file:
                fieldnames = ["Name", "Health", "Strength", "Defense", "Speed", "Level", "Description"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(characters)
            chara_manage()
        chara_delete()
    elif profile == "4":
        quit()
    return player





