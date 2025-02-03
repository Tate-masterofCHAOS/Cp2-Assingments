#This is my morse code translator Tate Morgan Period 3





english = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
morse_code = ["._", "_...", "_._.", "_..", ".", ".._.", "__.", "....", "..", ".___", "_._", "._..", "__", "_.", "___", ".__.", "__._", "._.", "...", "_", ".._", "..._", ".__", "_.._", "_.__", "__..", " "]



def english_to_morse(words):
    for i in words:
        if i in english:
            x = english.index(i)
            print(morse_code[x], end="")


def morse_to_english(words):
    for i in words:
        if i in morse_code:
            x = morse_code.index(i)
            print(english[x], end="")





def main():
    type = input("Are you translating to english or to morse: ").lower()
    if type == "english":
        words = input("Please place your morse code here using . and _: ").lower()
        morse_to_english(words)
    if type == "morse":
        words = input("Please place your english here: ").lower()
        english_to_morse(words)


main()