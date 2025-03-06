#Tate Morgan Advanced Notes Help



#1. What is a helper function
    #A function written to be called by in another function
def is_int(user_input):
    try:
        int(user_input)
    except:
        #8. What is recursion
            #When you call a function within itself
        #9. How does recursion work
            #Calling a function within itself with new info
        print("Please give me a number.")
        user_input = is_int(input("How old are you?\n"))
    return user_input
    
def age():
    old = is_int(input("How old are you?\n"))

    print(f"Cool. You are {old} years")


#age()
#2. What is the purpose of a helper function
    #Makes it easier so read
#3. What is an inner function
    #A function that exists inside another function
#def add(a):
    #b = int(input("Give me a number\n"))

    #def addition():
        #print(a+b)

    #addition()

#add(3)

#import logging
#logging.basicConfig(level=logging.INFO)

#def logger(func):

    #def wrapper(*args, **kwargs):
        #logging.info(f"Exexuting {func.__name__} with {args}, {kwargs}")
        #return func(*args, **kwargs)
    #return wrapper

#@logger
#def adder(a,b):
    #return a+b
#print(adder(3,4))
#4. What is the scope of a function With an inner function
    #Access of anything within the local function but stuff in the inner function cant be used by the outer function

#5. Why do we use inner functions
    #To prevent us from needing to return values
#6. What is a closure function
    #This allows your function to remember information across multiple function

def add(a):

    def addition(b):
        return a+b

    return addition

base = add(10)

#print(base(5))
#7. Why do we write closure functions
    #Saves The information