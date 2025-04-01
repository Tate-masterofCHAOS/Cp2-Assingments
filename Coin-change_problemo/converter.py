import csv

coins = []


def calculate(target, coin_amount1, coin_amount2, coin_amount3, coin_amount4):
    coin1 = 0
    coin2 = 0
    coin3 = 0
    coin4 = 0
    while True:
        if target >= float(coin_amount1):
            coin1 += 1
        elif target >= float(coin_amount2):
            coin2 += 1
        elif target >= float(coin_amount3):
            coin3 += 1
        elif target >= float(coin_amount4):
            coin4 += 1
        else:
            break
    print(f"To reach your goal you need \n{coin1} {coins[3[0]]} \n{coin2} {coins[2[0]]} \n{coin3} {coins[1[0]]} \n{coin4} {coins[0[0]]}")
         




def convert(country,target):
    coin_amount1 = 0
    coin_amount2 = 0
    coin_amount3 = 0
    coin_amount4 = 0
    if country == "1":
        country = 'America'
        def denom_get(country,target,coins, coin_amount1, coin_amount2, coin_amount3, coin_amount4):
            coins.clear
            with open("Coin-change_problemo\money.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[2] == country:
                        coins.append({"Name": row[0], "Worth": row[1]})
                        if coin_amount1 == 0:
                            coin_amount1 = row[1]
                        elif coin_amount2 == "":
                            coin_amount2 = row[1]
                        elif coin_amount3 == "":
                            coin_amount3 = row[1]
                        elif coin_amount4 == "":
                            coin_amount4 = row[1]
                    else:
                          continue
            return coins, coin_amount1, coin_amount2, coin_amount3, coin_amount4
        denom_get(country, target,coins, coin_amount1, coin_amount2, coin_amount3, coin_amount4)
        calculate(target, coin_amount1, coin_amount2, coin_amount3, coin_amount4)
        
