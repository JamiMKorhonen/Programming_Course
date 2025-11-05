# A5_T6 Tally counter (TEST TASK)

# Make a menu-driven Python program which mimics Tally Counter.

# This menu-driven program must contain a maintainable program structure with the following requirements:

#     main function which represents the main program logic including menu cycle.
#     showOptions function which takes no arguments, shows the available options in the standard output and returns None.
#     askChoice function which takes no arguments, prompts user to insert choice and returns an integer regardless of the user feed.

# In case user incorrectly inserts text as a choice, the program must output "Unknown option!". For this, see the string method isnumeric() behaviour described in W3S or via Python documentation.

def askChoice():
    feed = input("Your choice: ")
    return feed

def showOptions():
    print("Options:")
    print("1 - Show count")
    print("2 - Increase count")
    print("3 - Reset count")
    print("0 - Exit")
    return None

def main():
    i = 0

    while True:
        showOptions()
        feed = askChoice()

        if feed.isnumeric():
            choice = int(feed)

            if choice == 1:
                print(f"Current count - {i}\n")
            
            elif choice == 2:
                i += 1
                print("Count increased!\n")

            elif choice == 3:
                i = 0
                print("Cleared count!\n")

            elif choice == 0:
                print("Exiting program.")
                break

            else:
                print("Unknown option!\n")

        else:
            print("Unknown option!\n")

print("Program starting.")
main()
print("\nProgram ending.")
