# Tate Morgan, Writing to text notes
import csv

"""
r= read file
w = write on file
w+ = read and rite
a = append
x = create
a+ append and read
"""

#with open("Notes/test.txt", "a") as file:
    #file.write("undertale\n omori\n")

data = [
    {"username": "papyrus", "color": "red"},
    {"username": "sans", "color": "blue"},
    {"username": "alphys", "color": "yellow"},
    {"username": "undyne", "color": "blue"},
    {"username": "mettaton", "color": "purple"},
    {"username": "muffet", "color": "purple"}
]

with open("Notes\Class CSV sample - Sheet1 (1).csv", "a", newline="") as file:
    fieldnames = ["username", "color"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)



with open("Notes\Class CSV sample - Sheet1 (1).csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(f"user name: {row[0]}\n color: {row[1]}\n---------------------\n")