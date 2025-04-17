# Classes and objects in python

class subject:
    def __init__(self, content, period, teacher):
        self.content = content
        self.period = period
        self.teacher = teacher

    def __str__(self):
        return f'Name: {self.content} \nPeriod: {self.period} \nTeacher: {self.teacher}'

first = subject("Math", 1, "Miller")
second = subject("World Civ", 2, "Macinanti")

#print(first.content)
#print(second.content)



class pokemon:
    def __init__(self, name, type, hp, dmg):
        self.name = name
        self.type = type
        self.hp = hp
        self.dmg = dmg
    
    def __str__(self):
        return f'{self.name} is a {self.type} they have a max health of {self.hp} and does {self.dmg} damage in battle'
    
    def battle(self, opponent):
        while self.hp > 0 and opponent.hp > 0:
            opponent.hp -= self.dmg
            print(f'{self.name} attacked {opponent.name} for {self.dmg} and {opponent.name} is at {opponent.hp}')

            if opponent.hp <= 0:
                print(f'{opponent.name} is knocked out. {self.name} wins!')
            else:
                self.hp -= opponent.dmg
                print(f'{opponent.name} attacked {self.name} for {opponent.dmg} and {self.name} is at {self.hp}')

                if self.hp <= 0:
                    print(f'{self.name} is knocked out. {opponent.name} wins!')


fluffy = pokemon("Fluffy", "Arcananine", 280, 110)
slimy = pokemon("Slimy", "Ditto", 100, 70)
spiky = pokemon("Slimy", "joltean", 150, 100)


fluffy.battle(spiky)
            

#What is a class in python
    #A blueprint for an object
#What is an object in python
    #An instance of a class
#How do python classes relate to python objects
    #classes are blueprints for objects
#How do you create a python class
    #class:
#What are methods
    #Functions made for that specific class
#How do you create a python object
    #everything in python
#How do you call a method for an object
    #object.method
#Why do we use python classes
    #We can use these to make multiple that are slightly different
