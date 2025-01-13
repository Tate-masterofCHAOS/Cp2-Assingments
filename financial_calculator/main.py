# Tate Morgan Financial calculator 
# This is my financial calculator

# My job is to build a prpgram that completes the following functions
# How long it will take to save for a goal based on a weekly or monthly deposit
# Compound Interest Calculator 
# Budget Allocator (use set percentages to divide an income into spending categories like savings, entertainment, and food)
# Sale Price Calculator (apply discounts to prices)
# Tip Calculator

# The Steps ill follow are as follows
# Create a main function that will run the user interface
# Using project decomposition to figure out what other functions you need and how they interact with each other
# Create your functions
# Have at least 2 people test your code to make sure it works
 
income = ""
interest_rate = ""
years = ""
def Save_time():
    pass

def CompoundInt_cal(income, interest_rate, years):
    runs = int(years)
    interest_rate = int(interest_rate) / 100
    for i in range(runs):
        Interest = int(income) * float(interest_rate)
        income = float(income) + float(Interest)
        print(f"{income:.2f} dollars")
    return income

def Budget_Allocator(income, spen_per, ent_per, sav_per):
    spen_per = int(spen_per) / 100
    Spen_mon = float(income) * float(spen_per)
    spen = Spen_mon
    print(f"Your spending money is {spen:.2f} dollars")
    ent_per = int(ent_per) / 100
    ent_mon = float(income) * float(ent_per)
    ent = ent_mon
    print(f"Your entertainment money is {ent:.2f} dollars")
    sav_per = int(sav_per) / 100
    sav_mon = float(income) * float(sav_per)
    sav = sav_mon
    print(f"Your entertainment money is {sav:.2f} dollars")
    pass

def price_cal(price, per_off):
    discount = int(per_off) / 100
    total_discount = float(price) * discount
    price = float(price) - total_discount
    print(f"Yout total is now {price:.2f} dollars")
    pass

def tip_cal(price, tip_per):
    tip = int(tip_per) / 100
    total_tip = float(price) * tip
    price = float(price) + total_tip
    print(f"Yout total is now {price:.2f} dollars")
    pass

def main():
    job = input("what would you like to use(Compound interest calculator, Budget allocator): ")
    if job == "Compound interest calculator":
        income = input("How much money do you have initially: ")
        interest_rate = input("What is the interest rate: ")
        years = input("How many years will you be acruing interest: ")
        CompoundInt_cal(income, interest_rate, years)
    elif job == "Budget allocator":
        income = input("How much money do you have: ")
        spen_per = input("What percent is spending money: ")
        ent_per = input("What percent is going into entertainment: ")
        sav_per = input("What percent is going into savings: ")
        Budget_Allocator(income, spen_per, ent_per, sav_per)
    elif job == "Price calculator":
        price = input("what is the price: ")
        per_off = input("How much percent off")
        price_cal(price, per_off)
    elif job == "Tip calculator":
        price = input("what is the price: ")
        tip_per = input("what percent tip: ")
        tip_cal(price, tip_per)
    else:
        print("Sorry thats not a function please check your spelling or try something else")
    pass
main()