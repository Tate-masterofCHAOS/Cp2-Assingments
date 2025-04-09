#Tate Morgan Battle Simulator


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from faker import Faker


def cs():
    print("\033c")



def is_int(value):
    try:
        int(value)

    except:
        value = is_int(input("\nPlease input an integer.\n"))
    return int(value)



def is_in_range(value, min, max):
    value = is_int(value)

    if value < min or value > max:
        value = is_in_range("\ninvalid input, try again.\n", min, max)
    return value


def is_unique(list, value):

    
    for item in list:
        if item == value:
            value = is_unique(list, input("\nThat item already exists. Choose something else.\n"))
            
    return value




def is_in_list(list, value):
    for index in range(len(list)):
        if list[index] == value:
            return index+1 
        
    return False



def load_profiles():

    profiles = pd.read_csv('battle_simulator/character_info.csv')
    return profiles.to_dict()



def save_profiles(profiles):
    profiles = pd.DataFrame(profiles)
    profiles.to_csv('battle_simulator/character_info.csv', index=False)



def graph(values, titles):
    plt.bar(titles, values)

    plt.show()


def rand_name():
    fake = Faker()

    return fake.name()