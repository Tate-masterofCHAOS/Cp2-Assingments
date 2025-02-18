import csv
with open("Notes\Class CSV sample - Sheet1 (1).csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(f"user name: {row[0]} color: {row[1]}")