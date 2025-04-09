#Tate Morgan Battle Simulator

from small_functions import *
import random

def format_profiles(profiles):
    formatted_list = "\n"
    for i in range(len(profiles['name'])):
        formatted_list += f"{i+1}  Level {profiles['level'][i]} {profiles['name'][i]}\n"

    return formatted_list
        


def assign_stats(index, df):
    stats = dict({})
    stats['strength']=df['strength'][index]
    stats['defense']=df['defense'][index]
    stats['health']=df['health'][index]
    stats['speed']=df['speed'][index]
    return stats
    

        



def combat(p1, p2):
    print(p1)
    print(p2)
    commentary = "" 
    if random.randint(1,2) == 1:
        commentary += "\nPlayer 1 starts"
        turn = 1

    else:
        commentary += "\nPlayer 2 starts"
        turn = 2

    while p1["health"] > 0 and p2["health"] > 0:
        if turn == 1:
            damage = p1["strength"] + random.randint(-p1["strength"]//4,p1["strength"]//4)
            defense = random.randint(p2["defense"]//2,p2["defense"])
            
            damage -= defense
            dodge = random.randint(0,p2["speed"])-p1["speed"]

          
            if damage < 0:
                damage = 0

         
            if dodge > 0:
                damage = 0
           
                commentary += "Player 2 dodged"

            else:
              
                commentary += f"\nPlayer 1 did {damage} damage, player 2 blocked {defense} damage."

       
            p2["health"] -= damage
            commentary += f" Player 2 is now at {p2['health']} health."


     
        elif turn == 2:
            damage = p2["strength"] + random.randint(-p2["strength"]//4,p2["strength"]//4)
            defense = random.randint(p1["defense"]//2,p1["defense"])
  
            damage -= defense
            dodge = random.randint(0,p1["speed"])-p2["speed"]

           
            if damage < 0:
                damage = 0

           
            if dodge > 0:
                damage = 0
           
                commentary += "Player 1 dodged"

            else:
           
                commentary += f"\nPlayer 2 did {damage} damage, player 1 blocked {defense} damage."

           
            p1["health"] -= damage
            commentary += f" Player 1 is now at {p1['health']} health."

        if turn == 1:
            turn += 1

        else:
            turn -= 1

    if p1["health"] < 0:
        commentary += '\nPlayer 2 wins'
        return 2, commentary
    
    else:
        commentary += '\nPlayer 1 wins'
        return 1, commentary





def select_profiles(profiles):
    print(f"\nprofiles:{format_profiles(profiles)}")


    index_1 = is_in_range(is_int(input("type the number of the profile ")), 0, len(profiles['name']))-1
    index_2 = is_in_range(is_int(input("type the number of the profile ")), 0, len(profiles['name']))-1
    profile_1 = assign_stats(index_1, profiles)
    profile_2 = assign_stats(index_2, profiles)


    return profile_1, profile_2, index_1, index_2




def main():
    profiles = load_profiles()
    if len(profiles['name']) < 2:
        cs()
        print("\nnot enough profiles\n")
        return

    profile_1, profile_2, index_1, index_2 = select_profiles(profiles)

    winner, commentary = combat(profile_1, profile_2)
    print(commentary)
    input("\ntype anything to move on")
    cs()
    
    if winner == 1:
        profiles['level'][index_1] += 1

    else:
        profiles["level"][index_2] += 1

    
    save_profiles(profiles)

main()