import random 
#This is my password generator assingments 
#A main function that runs the code Functions for the different password requirements A function that assembles that password once it is the correct length Users should be able to specify length and if they want to include uppercase letters, lowercase letters, numbers, special characters

charas = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "{", "}", "[", "]", "?", "/", ",", ".", "<", ">", "=", "+", "-", "_"]
def F_length():    
    length = int(input("what is the desired length: "))
    return length


def F_big_letter():
    pass


def F_small_letter():
    pass


def F_Nums():
    pass


def F_Special_Chara():
    pass

def password(length):
    print(random.choice(charas))
    pass


def main():
    V_requirement1 = input("Would you like to specify a length: ").lower
    V_requirement2 = input("would you like to require uppercase letters: ").lower
    V_requirement3 = input("would you like to require lowercase letters: ").lower
    V_requirement4 = input("would you like to require numbers: ").lower
    V_requirement5 = input("would you like to require special characters: ").lower
    L_requirments = [V_requirement1, V_requirement2, V_requirement3, V_requirement4, V_requirement5]







main()