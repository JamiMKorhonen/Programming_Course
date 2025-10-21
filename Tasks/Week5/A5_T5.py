# A5_T5 Menu-driven program

# Create a menu-driven Python program with following options:

#     Insert a word
#         Which stores user inserted word into memory.
#     Show current word
#         Prints the word from the memory
#     Show current word in reverse
#         Prints the word from the memory in reverse.
#     Exit
#         Stops the program gracefully
#     Unknown option

# Initialize the Word with an empty string.


def main():
    print("\nOptions:")
    print("1 - Insert word")
    print("2 - Show current word")
    print("3 - Show current word in reverse")
    print("0 - Exit")
    choice = int(input("Your choice: "))
    Word = ""


    while choice != 0:
        if choice == 1:
            Word = input("Insert word: ")

            print("\nOptions:")
            print("1 - Insert word")
            print("2 - Show current word")
            print("3 - Show current word in reverse")
            print("0 - Exit")
            choice = int(input("Your choice: "))
        
        elif choice == 2:
            print(f"Current word - \"{Word}\"")

            print("\nOptions:")
            print("1 - Insert word")
            print("2 - Show current word")
            print("3 - Show current word in reverse")
            print("0 - Exit")
            choice = int(input("Your choice: "))
        
        elif choice == 3:
            Reverseword = Word[::-1]
            print(f"Word reversed - \"{Reverseword}\"")

            print("\nOptions:")
            print("1 - Insert word")
            print("2 - Show current word")
            print("3 - Show current word in reverse")
            print("0 - Exit")
            choice = int(input("Your choice: "))
        
        else:
            print("Unknown option! try again.")

            print("\nOptions:")
            print("1 - Insert word")
            print("2 - Show current word")
            print("3 - Show current word in reverse")
            print("0 - Exit")
            choice = int(input("Your choice: "))


print("Program starting.")
main()
print("Exiting Program.")
print("\nProgram ending.")



# Example program runs

# Program starting.
# Options:
# 1 - Insert word
# 2 - Show current word
# 3 - Show current word in reverse
# 0 - Exit
# Your choice: 1
# Insert word: Banana

# Options:
# 1 - Insert word
# 2 - Show current word
# 3 - Show current word in reverse
# 0 - Exit
# Your choice: 2
# Current word - "Banana"

# Options:
# 1 - Insert word
# 2 - Show current word
# 3 - Show current word in reverse
# 0 - Exit
# Your choice: 3
# Word reversed - "ananaB"

# Options:
# 1 - Insert word
# 2 - Show current word
# 3 - Show current word in reverse
# 0 - Exit
# Your choice: 0
# Exiting program.

# Program ending.


