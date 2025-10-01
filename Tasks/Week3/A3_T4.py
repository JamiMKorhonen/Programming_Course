# A3_T4 More menu options

# Extend the previous menu program by adding three more options to the menu.
# Options:
#     Print the name backwards
#         Your name backwards is "{NameBackwards}"
#     Print the first character
#         The first character in name "{Name}" is "{FirstChar}"
#     Show the amount of characters in the name
#         There are {NameLength} characters in the name "{Name}"


# Program starting.
print("Program starting.")
# This is a program with simple menu, where you can choose which operation the program performs.
print("# This is a program with simple menu, where you can choose which operation the program performs.")
# Before the menu, please insert your name: 
name = input("Before the menu, please insert your name: ")

# Options:
print("Options: ")
# 1 - Print welcome message
print("1 - Print welcome message")
# 2 - Print the name backwards
print("2 - Print the name backwards")
# 3 - Print the first character
print("3 - Print the first character")
# 4 - Show the amount of characters in the name
print("4 - Show the amount of characters in the name")
# 0 - Exit
print("0 - Exit")
# Your choice: 
choice = int(input("Your choice: "))


# 1 - Print welcome message
if choice == 1:
    print(f"Welcome, {name}")

# 2 - Print the name backwards
elif choice == 2:
    print(f"Your name backwards is {name[::-1]}")

# 3 - Print the first character
elif choice == 3:
    FirstChar = name[:1:]
    print(f"The first character in name {name} is {FirstChar}")

# 4 - Show the amount of characters in the name
elif choice == 4:
    NameLength = len(name)
    print(f"There are {NameLength} characters in the name {name}")

# 0 - Exit
elif choice == 0:
    print("Exiting...")

# ???
else:
    print("Unknown option.")

# Program ending.
print("\nProgram ending.")
