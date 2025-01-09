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
 
initial_amount = ""
interest_rate = ""
years = ""
def CompoundInt_cal(initial_amount, interest_rate, years):
    int(years)
    while years > 0
    interest_rate = int(interest_rate) / 100
    Interest = int(initial_amount) * float(interest_rate)
    initial_amount = int(initial_amount) + int(Interest)
    years - 0
    print(initial_amount)
    return initial_amount 

def Budget_Allocator():
    pass

def price_cal():
    pass
def tip_cal():
    pass

def main():
    job = input("what would you like to use(Compound interest calculator, ): ")
    if job == "Compound interest calculator":
        initial_amount = input("How much money do you have initially: ")
        interest_rate = input("What is the interest rate: ")
        years = input("How many years will you be acruing interes")
        CompoundInt_cal(initial_amount, interest_rate, years)
    else:
        print("Sorry thats not a function please check your spelling or try something else")
    pass
main()