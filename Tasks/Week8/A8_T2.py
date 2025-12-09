# A8_T2 Calculator

# Create a menu-driven program which can perform basic arithmetic operations. 
# All the math operations should be performed with floating datatype and without rounding. 
# Separate the functionality into the appropriate files.


from A8_library import add, subtract, multiply, divide


def showOptions() -> None:
    print("\nOptions:")
    print("1 - Add")
    print("2 - Subtract")
    print("3 - Multiply")
    print("4 - Divide")
    print("0 - Exit")


def askChoice() -> int:
    return int(input("Your choice: "))


def askValue(PPrompt: str) -> float:
    return float(input(PPrompt))


def main() -> None:
    print("Program starting.")

    while True:
        showOptions()
        choice = askChoice()

        if choice == 0:
            print("Exiting program.")
            break

        if choice == 1:
            value1 = askValue("Insert first addend value: ")
            value2 = askValue("Insert second addend value: ")
            result = add(value1, value2)
            print(f"{value1} + {value2} = {result}")

        elif choice == 2:
            value1 = askValue("Insert minuend value: ")
            value2 = askValue("Insert subtrahend value: ")
            result = subtract(value1, value2)
            print(f"{value1} - {value2} = {result}")

        elif choice == 3:
            value1 = askValue("Insert multiplicand value: ")
            value2 = askValue("Insert multiplier value: ")
            result = multiply(value1, value2)
            print(f"{value1} * {value2} = {result}")

        elif choice == 4:
            value1 = askValue("Insert dividend value: ")
            value2 = askValue("Insert divisor value: ")
            result = divide(value1, value2)
            print(f"{value1} / {value2} = {result}")

    print("\nProgram ending.")
    return None

if __name__ == "__main__":
    main()
