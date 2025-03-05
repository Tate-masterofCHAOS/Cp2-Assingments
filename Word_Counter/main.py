


def count():    
    word_count = 0
    with open("Word_Counter/word_doc.txt", "w", newline="") as file:
            text = input("What would you like to check the word count of").lower()
            file.write(text)
        
    
    with open("Word_Counter/word_doc.txt", "r") as file:
        file.read(n)
        for n in file:
            if n == " ":
                word_count += 1
            else:
                continue
        word_count +=1

count()
        