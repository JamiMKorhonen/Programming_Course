# T3 - Timestamp analysis

# In this task, create a program that reads timestamps from a textfile. The file content is in “.csv” format and contains information related to electricity usage.

# Datasets
#     A7_T3_D1.csv
#     A7_T3_D2.csv
#     A7_T3_D3.csv

# CSV format:
#     Has header row
#     Columns
#         Weekday
#         Hour
#         Consumption(kWh)
#         Price(€/kWh)
#     Separator ;

# Download the datasets to your computer and set up the following steps in your program:
#     Prompt user to insert the filename
#     Read the specified file
#         Skip header row
#         Read line and remove newline character
#         If line is empty (contains only newline character), skip line
#     Analyse timestamps per weekday
#         Count each row that starts with weekday (Row.startswith(…))
#     Display results

# When analysing and creating results, the recommendation is to pass the data rows and the results list to the analyse function. 
# This analyse function then reads the datarows, does the calculations and fills the results list when needed.
# Displaying the results could be a function that simply iterates through the results and displays them. 

# Preferred datastructures:
#     WEEKDAYS: tuple[str]
#     Rows: list[str]
#     Results: list[str]

import os
WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday",)


def readFile(PFilename: str, PRows: list[str]) -> None:
    print('Reading file "{}".'.format(PFilename))
    # 0. Clear PRows list just in case
    PRows.clear()
    # 1. Open filehandle
    with open(PFilename, "r", encoding="UTF-8") as fileHandle:
    # 2. Read filehandle line-by-line
    # 2.1. Skip first line (header row)
        next(fileHandle)
    # 2.2. Check if line is empty '\n'
        for line in fileHandle:
            if line.strip():
    # 2.3. Add non empty datarow without newline at the end.
                PRows.append(line.strip())
    # 3. Close filehandle 
    return None


def analyseTimestamps(PRows: list[str], PResults: list[str]) -> None:
    print("Analysing timestamps.")
    # Append results to the PResults list
    # Initialise helper list 
    WeekdayTimestampAmount: list[int] = [0, 0, 0, 0, 0, 0, 0]
    # Iterate rows with i
    for PRow in PRows:
        for i,WEEKDAY in enumerate(WEEKDAYS):
    #   Iterate WEEKDAYS with j
    #      Check if the row starts with the weekday name
            if PRow.startswith(WEEKDAY):
    #          Count the day in proper place
                WeekdayTimestampAmount[i] += 1
    # Iterate WEEKDAYS with i and append the daily results
    PResults.append("### Timestamp analysis ###")
    for i,WEEKDAY in enumerate(WEEKDAYS):
        PResults.append(f" - {WEEKDAY} {WeekdayTimestampAmount[i]} stamps")
    PResults.append("### Timestamp analysis ###")
    # Clear the helper list
    WeekdayTimestampAmount.clear()
    return None


def displayResults(PResults: list[str]) -> None:
    print("Displaying results.")
    # Iterate results and print for the user
    for line in PResults:
        print(line)
    return None


def main() -> None:
    # 1. Initialise
    # 1.1. Initialise rows list
    Rows: list[str] = []
    # 1.2. Initialise results list
    Results: list[str] = []
    # 2. Operate
    print("Program starting.")
    # 2.1. Ask user to define filename
    Filename = input("Insert filename: ")
    #Filename = "A7_T3_D1.csv"
    # 2.2. Read file
    readFile(Filename, Rows)
    # 2.3. Analyse rows
    analyseTimestamps(Rows, Results)
    # 2.3. Display results
    displayResults(Results)
    # 3. Cleanup
    print("Program ending.")
    # 3.1. Clear lists
    return None


main()


if __name__ == "__main__":
    main()


# Remember to change terminal directory to Week7!
# cd Tasks/Week7

# You may run the program with single bash command:
#    echo -e "A7_T3_D1.csv\n" | python A7_T3.py