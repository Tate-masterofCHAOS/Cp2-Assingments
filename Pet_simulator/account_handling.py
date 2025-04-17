








def account_handling():
    while True:
        choice = input('Choose one: \n1. Log in \n2. Create account')
        if choice == '1':
            if user != {"": ""}:
                username = input('What is your username')
                with open('Pet_simulator/accounts.csv') as file:
                    reader = csv.reader(file)
                    for line in file:
                        if line[0] == username:
                            password = input('What is your password you may also type leave to go back to the username selection')
                            while True:
                                if line[1] == password:
                                    user = {'Username': username, 'Password': password}
                                    break
                                elif line[1] == 'leave':
                                    break
                                else:
                                    print("That is not the correct password")
                        else:
                            print('That account does not exist would you like to create one or go back \n1. Create account \n2. Go back')