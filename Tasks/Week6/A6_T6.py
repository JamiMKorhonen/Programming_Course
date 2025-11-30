# A6_T6 Cipher messages (TEST TASK)

# In this exercise, get familiar with the Caesar cipher and specificly on the ROT13 implementation.
# https://en.wikipedia.org/wiki/Caesar_cipher
# https://en.wikipedia.org/wiki/ROT13


# Caesar Cipher explained (3 minutes): youtu.be/sMOZf4GN3oc

# Create a Python program which collects plain text rows from user till the user inserts an empty row. 
# Cipher all rows and then ask user to choose between showing the ciphered text or saving it.
# A 	B 	C 	D 	E 	F 	G 	H 	I 	J 	K 	L 	M 	N 	O 	P 	Q 	R 	S 	T 	U 	V 	W 	X 	Y 	Z
# N 	O 	P 	Q 	R 	S 	T 	U 	V 	W 	X 	Y 	Z 	A 	B 	C 	D 	E 	F 	G 	H 	I 	J 	K 	L 	M

# Program must be able to cipher following lowercase and uppercase alphabets. Other characters remains same during ciphering operation.
    # # English alphabets (2 x 26)
    # LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
    # UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


import os

# English alphabets (2 x 26)
LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

DELIMITER = "\n"


def collectWords():
    words = ""
    while True:
        word = input("Insert row(empty stops): ")
        if word == "":
            break
        if words:
            words += DELIMITER
        words += word
    return words


# With help from teacher Mira Vorne (LAB)
def shiftCharacter(Character: str, Alphabets: str, Shift: int = 13) -> str:
    #"""Shifts a character by 'Shift' positions in the given alphabet (ROT13 logic)."""
    NewCharacter = Character
    for i in range(len(Alphabets)):
        if (Character == Alphabets[i]):  # Find character in alphabet
            ShiftedIndex = i + Shift 
            if ShiftedIndex >= len(Alphabets):  # Go around the alphabets if necessary
                ShiftedIndex = ShiftedIndex - len(Alphabets)
            NewCharacter = Alphabets[ShiftedIndex]  # Get shifted character
    return NewCharacter


# With help from teacher Mira Vorne (LAB)
def rot13(PContent: str, PShift: int = 13) -> str:
    #"""Applies ROT13 to an entire string."""
    NewContent = ""
    for Character in PContent:
        if (Character in LOWER_ALPHABETS):  # Lowercase letter
            NewContent += shiftCharacter(Character, LOWER_ALPHABETS, PShift)
        elif (Character in UPPER_ALPHABETS):  # Uppercase letter
            NewContent += shiftCharacter(Character, UPPER_ALPHABETS, PShift)
        else:
            NewContent += Character  # Non-alphabet characters remain unchanged
    return NewContent


def writeFile(Pfilename, Pcontent):
    if Pfilename == "":
        print("File name not defined.")
        print("Aborting save operation.")
    else:
        with open(Pfilename, "w", encoding='UTF-8') as save:
            save.write(Pcontent)
        print("Ciphered text saved!")
        

def main():
    print("Program starting.\n")
    print("Collecting plain text rows for ciphering.")

    words = collectWords()
    #print(words)

    content = rot13(words)
    #print(cipheredWords)

    print("\n#### Ciphered text ####")
    print(content)


    print("\n#### Ciphered text ####")
    filename = input("Insert filename to save: ")
    writeFile(filename, content)

    print("Program ending.")
    return None


if __name__ == "__main__":
    main()


# Example program runs:

# Program starting.

# Collecting plain text rows for ciphering.
# Insert row(empty stops): Hello
# Insert row(empty stops): World
# Insert row(empty stops): 

# #### Ciphered text ####
# Uryyb
# Jbeyq

# #### Ciphered text ####
# Insert filename to save: A6_T6_F1.txt
# Ciphered text saved!
# Program ending.
