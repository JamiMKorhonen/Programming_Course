# A8_T3 Number files

# Create a menu-driven program for analysing number files.
# Datasets
#     A8_T3_D1.txt
#     A8_T3_D2.txt

# Menu options:
#     Read values
#     Amount of values
#     Calculate sum of values
#     Calculate average of values

# The recommendation during the “readValues” operation is to skip the empty rows “\n” and convert the rows into floating point values. 
# Values can be stored into a list[float] data structure.

# The amount of values can be calculated directly by using the “len”- function for the values list. 
# For analysing (options 3 and 4), pass the list of values as an argument to some specific function. 
# After calculating the sum or the average, round the results to one decimal precision. E.g. “1.234” => “1.2”


from A8_library import addValues


def showOptions():
    print("\nOptions:")
    print("1 - Read values")
    print("2 - Amount of values")
    print("3 - Calculate sum of values")
    print("4 - Calculate average of values")
    print("0 - Exit")
    return None


def askChoice():
    return int(input("Your choice: "))


def readValues(filename):
    values = []
    with open(filename, "r") as fileHandle:
        for line in fileHandle:
            stripped = line.strip()
            if stripped != "":
                values.append(float(stripped))
    return values


def averageValues(values):
    return round(addValues(values) / len(values), 1)


def main():
    print("Program starting.")
    values = []

    while True:
        showOptions()
        choice = askChoice()

        if choice == 0:
            print("Exiting program.\n")
            break

        elif choice == 1: 
            filename = input("Insert filename: ")
            values = readValues(filename)

        elif choice == 2:
            print(f"Amount of values {len(values)}")

        elif choice == 3:
            print(f"Sum of values: {addValues(values)}")

        elif choice == 4:
            print(f"Average of values: {averageValues(values)}")

    print("Program ending.")
    return None

if __name__ == "__main__":
    main()
