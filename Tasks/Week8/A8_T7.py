from A8_T7_drawLib import draw_hexagon, save_svg


def showOptions():
    print("Options:")
    print("1 - Draw square")
    print("2 - Draw circle")
    print("3 - Draw hexagon")
    print("4 - Save svg")
    print("0 - Exit")
    return None


def askChoice():
    return input("Your choice: ")


def main():
    print("Program starting.")

    while True:
        showOptions()
        choice = askChoice()

        if choice == "1":
            pass
        elif choice == "2":
            pass
        elif choice == "3":
            draw_hexagon()
        elif choice == "4":
            save_svg()
        elif choice == "0":
            print("Exiting program.\n")
            break

    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
