# A8_T4 Years, Months and Weekdays

# Create a menu-driven program which is able to read timestamps and count timestamps based on “year”, “month” or “weekday”. 
# Use both provided datasets: “A8_T1D1.txt” and “A8_T1D2.txt”.

# Datasets
#     A8_T4_D1.txt
#     A8_T4_D2.txt

# For handling the timestamps use the “datetime” library and look for the datetime library documentation aspects:
#     strptime and format directives %Y, %m, %d, %H and %M
#     year
#     month
#     day

# Recommended things to implement into the library file:
#     MONTHS: list[str] containing month names
#     WEEKDAYS: list[str] containing weekday names
#     def readTimestamps(PFilename: str, PTimestamps: list[datetime]) -> None:
#     def calculateYears(PYear: int, PTimestamps: list[datetime]) -> int:
#     def calculateMonths(PMonth: str, PTimestamps: list[datetime]) -> int:
#     def calculateWeekdays(PWeekday: str, PTimestamps: list[datetime]) -> int:

# Weekdays and months can be defined as constant variables in the program top-level. e.g.,


from A8_library import MONTHS, WEEKDAYS, readTimestamps, calculateYears, calculateMonths, calculateWeekdays


def showOptions():
    print("\nOptions:")
    print("1 - Calculate amount of timestamps during year")
    print("2 - Calculate amount of timestamps during month")
    print("3 - Calculate amount of timestamps during weekday")
    print("0 - Exit")
    return None


def askChoice():
    return int(input("Your choice: "))


def main():
    print("Program starting.")

    filename = input("Insert filename: ")
    timestamps = []
    readTimestamps(filename, timestamps)

    while True:
        showOptions()
        choice = askChoice()

        if choice == 0:
            print("Exiting program.\n")
            break

        elif choice == 1:
            year = int(input("Insert year: "))
            result = calculateYears(year, timestamps)
            print(f"Amount of timestamps during year '{year}' is {result}")

        elif choice == 2:
            month = input("Insert month: ")
            result = calculateMonths(month, timestamps)
            print(f"Amount of timestamps during month '{month}' is {result}")

        elif choice == 3:
            weekday = input("Insert weekday: ")
            result = calculateWeekdays(weekday, timestamps)
            print(f"Amount of timestamps during weekday '{weekday}' is {result}")

    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
