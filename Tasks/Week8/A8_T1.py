# A8_T1 Pause

# Create a menu-driven program which has three options:
#     Set pause duration
#     Activate pause
#     Exit

# Utilize time-library’s sleep-function to implement the pause in the program.
# Create a single program file “A8_T1.py”. Use this exercise to build the “template.py” mentioned earlier.


from A8_library import activatePause


def askUser() -> int:
    return int(input("Your choice: "))


def showOption() -> None:
    print("Options:")
    print("1 - Set pause duration")
    print("2 - Activate pause")
    print("0 - Exit")
    return None


def chooseActivity() -> None:
    while True:
        showOption()
        choice = askUser()
        print(choice)
        match choice:
            case 1:
                duration = int(input("Insert pause duration (s): "))
            case 2:
                activatePause(duration)
            case 0:
                print("Exiting program.")
                break
    return None


def main() -> None:
    print("Program starting.")
    chooseActivity()
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
