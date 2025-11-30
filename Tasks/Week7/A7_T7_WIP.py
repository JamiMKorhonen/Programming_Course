# T7 - Enigma machine

# How did the Enigma Machine work?: https://youtu.be/ybkkiGtJmkM
# Implement Enigma machine in Python.

# The program must handle:
#     3 x Rotors with 26 positions (A-Z)
#     1 x Reflector - Types A, B & C
#     0 x Plugboard. Prompt is required, but no need to implement.

# The order of machine operations described:
#     User presses letter on the keyboard
#         Keypress is passed via plugboard (skipped in this exercise)
#         Rotate the wheels (positions)
#         Scramble current letter using “Forward pass-through” process
#             Iterate through rotors in order 1-3
#                 Create offset using current rotor position and the letter
#                 Use the offset to shift the given letter in alphabets
#         Scramble current letter using using the reflector
#         Scramble current letter using “Reverse pass-through” process
#             Iterate through rotors in reverse order
#             Change current letter based on each wheel position offset

# In this program, user inserts row and the scrambling starts always from positions [0, 0, 0]. 
# So enter press means that the program must reset the positions before scrambling the inserted text. 
# The Enigma machine will shut down if the user enters an empty line.

# Recommended datastructures:
#     Rotors(characters): list[str]
#     Positions(rotor positions): list[int]
#     Reflector: str

# Initial configs
#     Tab 1: iconf1.txt
#     Tab 2: iconf2.txt
#     Tab 3: iconf3.txt


import os
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def config(filename):
    rotors = []
    reflector = ""

    with open(filename, "r") as fileHandle:
        for line in fileHandle:
            if line.startswith("Rotor"):
                rotors.append(line.split(":")[1].strip())
            elif line.startswith("Reflector"):
                reflector = line.split(":")[1].strip()
    return rotors, reflector


def encode(Prow, Protos, Preflector):
    

    return None


def main():
    # fileName = input("Insert config(filename): ")
    filename = "A7_T7_iconf1.txt"
    rotors, reflector = config(filename)

    plugs = input("Insert plugs (y/n)?: ")
    if plugs == "y":
        print("Skipped in this excercise")
    else:
        print("No extra plugs inserted.")

    print("Enigma initialized.\n")


    while True:
        row = input("Insert row (empty stops): ").upper()
        if not row: 
            print("\nEnigma closing.")
            break

        converted = encode(row, rotors, reflector)

    return None


if __name__ == "__main__":
    main()