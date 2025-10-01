# A3_T2 String comparisons

# Make Python program which does the following steps:
#     Prompt user to insert
#         A word
#         A character
#     Find if the character exists in the word. Possible prints below.
#         Word "{WordFirst}" contains character "{Character}"
#         Word "{WordFirst}" doesn't contain character "{Character}"
#     Prompt user to insert one more word
#     Compare the first word to the second word. Examples below:
#         The first word "{WordFirst}" is before the second word "{WordSecond}" alphabetically.
#         The second word "{WordSecond}" is before the first word "{WordFirst}" alphabetically.
#         Both inserted words are the same alphabetically, "{WordFirst}"


# Program starting.
print("Program starting.")


# String comparisons
print("Starting comparisons")
# Insert first word: 
WordFirst = input("Insert first word: ")
# Insert a character: 
char = input("Insert a character: ")

# Word "{WordFirst}" contains character "{Character}"
if char in WordFirst:
    print(f"{WordFirst} contains character {char}")
# Word "{WordFirst}" doesn't contain character "{Character}"
if char not in WordFirst:
    print(f"{WordFirst} doesn't contain character {char}")

# Insert second word: 
WordSecond = input("Insert second word: ")
# Compare the first word to the second word. Examples below:
#  The first word "{WordFirst}" is before the second word "{WordSecond}" alphabetically.
if WordFirst < WordSecond:
    print(f"The first word {WordFirst} is before the second word {WordSecond} alphabetically")
#  The second word "{WordSecond}" is before the first word "{WordFirst}" alphabetically.
elif WordSecond > WordFirst:
    print(f"The first word {WordSecond} is before the second word {WordFirst} alphabetically")
#  Both inserted words are the same alphabetically, "{WordFirst}"
elif WordFirst == WordSecond:
    print(f"Both inserted words are the same alphabetically, {WordFirst}")

# Program ending.
print("Program ending.")