# A4_T4 Repetitive prompt

# Make a program, which prompts user to insert words. 
# Program must stop prompting words if user inserts empty word. 
# After stopping the repetitive prompt, print the amount of words and characters that the user inserted.


print("Program starting.\n")

words = 0
chars = 0
LoopAgain = True
while LoopAgain == True:
    feed = input("Insert word (empty stops): ")
    if feed == "":
        print("\nYou inserted:")
        print(f"- {words} words")
        print(f"- {chars} characters")
        LoopAgain = False
    else:
        words += 1
        chars = chars + len(feed)

print("\nProgram ending.")


# Example program run 3:

# Insert word (empty stops): Five
# Insert word (empty stops): Four
# Insert word (empty stops): Three
# Insert word (empty stops): Two
# Insert word (empty stops): One
# Insert word (empty stops): 

# You inserted:
# - 5 words
# - 19 characters

# Program ending.
