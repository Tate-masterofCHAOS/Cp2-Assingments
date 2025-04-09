#Tate Morgan Battle Simulator


import csv


import random


from small_functions import *



def assign_stats(level):

    skill_points= [1,2,3,4] 
    for i in range(level):
        skill_points.append(random.randint(1,4))

  
    strength = 0
    defense = 0
    health = 0
    speed = 0

    for point in skill_points:
        
        if point == 1:
            strength += 2

      
        elif point == 2:
            defense += 1

        
        elif point == 3:
            health += 5

        elif point == 4:
            speed += 1

    
    return strength, defense, health, speed



def count_points(strength, defense, health, speed):
    str_count = strength//2
    def_count = defense
    hlt_count = health//5
    spd_count = speed

    total = str_count + def_count + hlt_count + spd_count - 4 

    return total



def format_profiles(profiles):
    formatted_list = "\n"
    for i in range(len(profiles['name'])):
        formatted_list += f"{i+1}  Level {profiles['level'][i]} {profiles['name'][i]}\n"

    return formatted_list



def main():

    
    profiles = load_profiles()
    


    def new_profile():
        name = input("\nwhat is the name? (leave blank to be random) ")
        if name == "":
            name = rand_name()
            print(f"\nname is {name}\n")

        level = is_int(input("\nwhat is the character's level? "))
        strength, defense, health, speed = assign_stats(level)

        profiles['name'][len(profiles['name'])] = name
        profiles['strength'][len(profiles['strength'])] = strength
        profiles['defense'][len(profiles['defense'])] = defense
        profiles['health'][len(profiles['health'])] = health
        profiles['speed'][len(profiles['speed'])] = speed
        profiles['level'][len(profiles['level'])] = level
        


    
    def edit_profile(profile):
       
        if profiles["level"][profile] > count_points(profiles["strength"][profile], profiles["defense"][profile], profiles["health"][profile], profiles["speed"][profile]):
            
            print("\nwhat would you like to do? Type:\n1 to add 1 strength point (2 strength)\n2 to add 1 defense point (1 defense)\n3 to add 1 health point (10 health)\n4 to add 1 speed point (1 speed)\n5 to go back\nYour answer here: ")
            action = is_int(input())

      
            if action == 1:
                profiles["strength"][profile] += 2

  
            elif action == 2:
                profiles["defense"][profile] += 1

            
            elif action == 3:
                profiles["health"][profile] += 5

          
            elif action == 4:
                profiles["speed"][profile] += 1

         
            elif action == 5:
                pass
            
            return f"\nsuccessfully updated profile\n"

        else:
            return "\nyou've spent all your skill points\n"
        

  
    while True:
        print("\nwhat would you like to do? Type:\n1 to make a new profile\n2 to edit a profile\n3 to view profiles\n4 to view a specific profile's stats\n5 to view stats on all profiles\n6 to exit\nYour answer here:")
        user_input = is_int(input())

       
        if user_input == 1:
            cs()
            new_profile()

           
            save_profiles(profiles)

       
        elif user_input == 2:
            cs()
           
            editing_profile_name = input("\nwhat is the name of the profile you are editing?\n")
            if is_in_list(profiles["name"], editing_profile_name):
               
                edited_profile_index = is_in_list(profiles["name"], editing_profile_name)-1
                print(edit_profile(edited_profile_index))

            
            save_profiles(profiles)

      
        elif user_input == 3:
            cs()
            print(format_profiles(profiles))

       
        elif user_input == 4:
            profile_name = input("\nwhat is the name of the profile you are viewing? (type nothing to go back)\n")
        
            if profile_name == "":
                continue

            if is_in_list(profiles['name'], profile_name):
                pfp_index = is_in_list(profiles['name'], profile_name)
                
                print(f"""\n{profiles['name'][pfp_index-1]}'s stats:
Strength: {profiles['strength'][pfp_index-1]} ({profiles['strength'][pfp_index-1]//2-1} points)
Defense: {profiles['defense'][pfp_index-1]} ({profiles['defense'][pfp_index-1]-1} points)
Health: {profiles['health'][pfp_index-1]} ({profiles['health'][pfp_index-1]//5-1} points)
Speed: {profiles['speed'][pfp_index-1]} ({profiles['speed'][pfp_index-1]-1} points)
Level: {profiles['level'][pfp_index-1]}
""")
                graph([profiles['strength'][pfp_index-1]//2-1,profiles['defense'][pfp_index-1]-1,profiles['health'][pfp_index-1]//5-1,profiles['speed'][pfp_index-1]-1,profiles['level'][pfp_index-1]],['strength','defense','health','speed','level'])

            else:
                print("\nthat is not a profile")


        elif user_input == 5:
            cs()
            df = pd.DataFrame(profiles).describe()
            print(df)
            
            




       
        elif user_input == 6:
            cs()
          
            save_profiles(profiles)

            break
    

main()