import datetime

def count():    
    word_count = 0
    with open(r'Word_Counter/word_doc.txt','r') as file:
        data = file.read()
        lines = data.split()
        for word in lines:
            if not word.isnumeric():          
                word_count += 1
        print(f"Your document is {word_count} long")

def main():
    while True
        task = input("Press 1 to edit file, 2 to check word count, or 3 to check timestamps\n")
        if task == "1":
            with open(r'Word_Counter/word_doc.txt','a') as file:
                file.write(input("What would you like to add: \n"))
                current_time = datetime.datetime.now()
                print(current_time)
            with open(r'Word_Counter/Timestamps.txt','a') as file:
                timestamp = str(current_time)
                file.write(timestamp)
                file.write("\n")
        if task == "2":
            count()
        if task == "3":
            with open(r'Word_Counter/Timestamps.txt','r') as file:
                file.read()

main()