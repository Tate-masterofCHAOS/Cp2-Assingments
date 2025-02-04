# Define the Morse code dictionary.
morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
    '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', ' ': '/'
}

# Convert a message to Morse code.
def english_to_morse(words):
    
    morse_code = ''
    for char in words.upper():
        if char in morse_dict:
            morse_code += morse_dict[char] + ' '
    return morse_code

# Convert a Morse code sequence to a message.
def morse_to_english(morse_code):
        
    words = ''
    morse_code = morse_code.split(' ')
    for code in morse_code:
        for char, morse in morse_dict.items():
            if morse == code:
                words += char
    return words

# User interface
def main():
    while True:
        choice = input("Choose an option:\nSay Morse to translate english into morse code\nSay English to translate morse code to english text\nSay quit to quit\n").lower()
        if choice == 'morse':
            words = input("Enter a message to convert to Morse code: ")
            morse_code = english_to_morse(words)
            print(morse_code)
        
        elif choice == 'english':
            morse_code = input("Enter a Morse code sequence to convert to text: ")
            words = morse_to_english(morse_code)
            print(words)
        
        elif choice == 'quit':
            print("Quitted successfully")
            break
            
        else:
            print("Invalid choice, please choose from the available options.")

main()