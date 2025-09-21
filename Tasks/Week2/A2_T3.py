# A2_T3: String length and concatenation

# Make Python program, which prompts user to insert two words. 
# Print the length of each word and then compound them together. 
# Put single quotes around the compound word.

# Program starting.
print("Program starting.")
# Insert first word: fire
Feed = input("Insert first word: ")
First = (Feed)
# Insert second word: fighter
Feed = input("Insert second word: ")
Second = (Feed)
# 1st word is 4 characters long.
print("1st word is", len(First), "characters long.")
# 2nd word is 7 characters long.
print("2nd word is", len(Second), "characters long.")
# Words together makes one closed compound 'firefighter'.
print("Words together makes one closed compound", f"'{First+Second}'."   )
print(First+Second)
# Program ending.
print("Program ending.")


# Example program run:

# Program starting.
# Insert first word: fire
# Insert second word: fighter
# 1st word is 4 characters long.
# 2nd word is 7 characters long.
# Words together makes one closed compound 'firefighter'.
# Program ending.
