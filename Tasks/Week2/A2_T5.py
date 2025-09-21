# A2_T5 String length and slicing (TEST TASK)

# Make a Python program, which prompts for a compound word.

# Get following aspects from the word
# Length
# First character
# Reversed version e.g. “Suitcase” is reversed “esactiuS”
# Display the aspects using print commands.
# Prompt the user to take substring from the existing compound word.
# Finally print the user specified substring.


# Program starting.
print("Program starting.")

# Insert a closed compound word: Moonbanana
compound = input("Insert a closed compound word: ")
# The word you inserted is 'Moonbanana' and in reverse it is 'ananabnooM'.
print("The word you inserted is", f"'{compound}'", "and in reverse it is", f"'{compound[::-1]}'." )
# The inserted word length is 10
print("The inserted word length is", (len(compound)) )
# Last character is 'a'
print("Last character is", f"'{compound[-1::]}'")
print("")

# Take substring from the inserted word by inserting...
print("Take substring from the inserted word by inserting...")
# 1) Starting point: 0
starting = input(f"1) Starting point: ")
starting = int(starting)
# 2) Ending point: 4
ending = input(f"2) Ending point: ")
ending = int(ending)
# 3) Step size: 1
step = input(f"3) Step size: ")
step = int(step)
print("")

# The word 'Moonbanana' sliced to the defined substring is 'Moon'.
print("The word", f"'{compound}'", "sliced to the defined substring is", f"'{compound[starting:ending:step]}'." )
# Program ending.
print("Program ending.")


# Example program run:

# Program starting.

# Insert a closed compound word: Moonbanana
# The word you inserted is 'Moonbanana' and in reverse it is 'ananabnooM'.
# The inserted word length is 10
# Last character is 'a'

# Take substring from the inserted word by inserting...
# 1) Starting point: 0
# 2) Ending point: 4
# 3) Step size: 1

# The word 'Moonbanana' sliced to the defined substring is 'Moon'.
# Program ending.
