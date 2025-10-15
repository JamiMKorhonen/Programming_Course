# A5_T2 Pass argument

# Create Python program which is able to print user input with a decorative frame.
# Program must consist of two functions:
#     main-function
#         Print starting and ending statements.
#         Print any empty row (see example program run)
#         Prompt user to insert a word.
#         Pass the inserted word into the frameWord-function.
#         Returns None
#     frameWord
#         Takes PWord as a parameter.
#         Prints the framing and the PWord
#             Hint: Multiply the asterisk '*'-character.
#         Returns None

# Note! Tests for this task relies on properly defined functions and may fail if the program is not written according to the instructions.



def frameWord(PWord):
    chars = len(PWord) + 4
    print("*" * chars)
    print(f"* {PWord} *")
    print("*" * chars)
    return None

def main():
    print("Program starting.")
    PWord = input("Insert word: ")
    print("")
    frameWord(PWord)
    print("\nProgram ending.")
    return None

main()
