import string
import random
 
def main():
    length = int(input("Enter password length: "))
    print('''Choose character set for password from these : 
         1. Digits
         2. Letters
         3. Special characters
         4. Exit''')
 
    CharaList = ""
 
    # Getting character set for password
    while(True):
        requirement = int(input("Pick a number "))
        if(requirement == 1):
         
            # Adding letters to possible characters
            characterList += string.ascii_letters
        elif(requirement == 2):
            
            # Adding digits to possible characters
            characterList += string.digits
        elif(requirement == 3):
         
            # Adding special characters to possible
            # characters
            characterList += string.punctuation
        elif(requirement == 4):
            break
        else:
            print("Please pick a valid option!")
 
    password = []
 
    for i in range(length):
   
        # Picking a random character from our 
        # character list
        randomchar = random.choice(characterList)
     
        # appending a random character to password
        password.append(randomchar)
 
    # printing password as a string
    print("The random password is " + "".join(password))


main()
