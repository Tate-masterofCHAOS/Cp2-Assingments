#Tate Morgan, Word Counter
import datetime
import pytz


def time_set():
    current_time = datetime.datetime.now(pytz.timezone('US/Mountain'))#Gets the time in Utah

    year = str(current_time.year) #Gets the current year

    month = str(current_time.month) #Gets the current month

    day = str(current_time.day) #Gets the current day

    hour = str(current_time.hour) #Gets the current hour

    minute = str(current_time.minute) #Gets the current minute
   
    if int(minute) < 10:
        minute = "0"+ minute #Adds a 0 in front of the minute if it is a single digit number so it is printed out nicely
    else:
        pass


    time = (hour + ":" + minute + ", " + month + "/" + day + "/" + year) #Combines the time into a nice string
    
    return "Time: " + time #Returns the time in a nice string to be printed out