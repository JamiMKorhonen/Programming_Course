########################################################
# Task A9_T6
# Developer Jami Korhonen
# Date 2025.12.10 (YYYY-MM-DD)
########################################################

# A9_T6 Save before exit (TEST TASK)

# In some scenarios, programs contain unsaved user data, and the user may accidentally do something that typically causes the program to close. 
# In CLI programs, this occurs if the user sends a keyboard interrupt (CTRL + C). 
# Handle the KeyboardInterrupt in a menu-driven program, which collects user-inserted lines.

# If the user has inserted 0 lines during a program run, there is nothing to save. 
# Handle the keyboard interrupt (CTRL + C) smoothly by informing the user that the program is closing suddenly.

# If the user has inserted 1 or more lines and then presses CTRL + C, prompt the user to confirm if they would like to save the lines to a file. 
# If the user confirms with yes, ask for the filename to write. Otherwise close the program gracefully.

# In the example program runs below, keypair ^C indicates user initiated KeyboardInterrupt. 
# Text after ^C on the same line represents program output after keyboard interrupt (color glitch).


def showOptions() -> None:
    print("Options:")
    print("1 - Insert line")
    print("2 - Save lines")
    print("0 - Exit")
    return None


def askChoice() -> int:
    try:
        return int(input("Your choice: "))
    except Exception as err:
        print(err)
        return -1


def saveLines(PLines: list[str]) -> None:
    try:
        filename = input("Insert filename: ")
        with open(filename, "w", encoding="UTF-8") as fileHandle:
            fileHandle.writelines(PLines)
    except Exception as err:
        print(err)
    return None


def insertLine(PLines: list[str]) -> None:
    try:
        text = input("Insert text: ")
        PLines.append(text)
    except Exception as err:
        print(err)
    return None


def onInterrupt(PLines: list[str]) -> None:
    if len(PLines) == 0:
        print("\nClosing suddenly.")
        return

    print("\nKeyboard interrupt and unsaved progress!")
    try:
        save = input("Save before quit(y/n)?: ").strip().lower()
        if save == "y":
            saveLines(PLines)
    except Exception as err:
        print(err)
    return None


def main() -> None:
    Lines: list[str] = []
    Choice = -1
    print("Program starting.")

    # Wrap the main loop in a try-except block to catch KeyboardInterrupt
    try:
        while Choice != 0:
                showOptions()
                Choice = askChoice()
                if Choice == 1:
                    insertLine(Lines)
                elif Choice == 2:
                    saveLines(Lines)
                elif Choice == 0:
                    print("Exiting program.")
                else:
                    print("Unknown option!")
                print("")
    except KeyboardInterrupt:
        onInterrupt(Lines)
    
    Lines.clear()
    print("Program ending.")

if __name__ == "__main__":
    main()
