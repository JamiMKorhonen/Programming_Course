# T4 - Timestamp dataclass (TEST TASK)

# Structure timestamp data in program.
# This task is continuation to the A7_T3 task. You may start this task by copying the previous datasets. Rename datasets to match this task e.g., “A7_T3_D1.csv” => “A7_T4_D1.csv”.

# The dataset had four different values separated by a semicolon ;:
#     Weekday
#     Hour
#     Consumption(kWh)
#     Price(€/kWh)

# The goal is to print each timestamp from a file and also calculate the total of consumption and price. 
# Below is the output format for a single record.
    # Electiricity usages:
    # - Monday 12:00, price 0.20 €, consumption 15.00 kWh, total 3.00 €
    # - ...

# To keep the code maintainable, define a named datastructure for the different values. Once defined, specify a way to read the timestamps into a list. 
# This can be done by reading a file line by line, skipping empty lines, trimming line endings, and then splitting each line by the delimiter.

# Preferred datastructures:
#     Timestamps: list[TIMESTAMP]


# # Constants
# DELIMITER = ";"
#   # iterate over lines
#     ...
#     Row = Line.rstrip()               # Remove newline
#     Columns = Row.split(DELIMITER)      # Splits the row into a list
#     Timestamp = TIMESTAMP()           # Create object
#     Timestamp.weekday = Columns[0]      # Collect the first column
#     ...                               # Collect rest of the columns...
#     Timestamp.price = float(Columns[3]) # Collect the fourth column and convert datatype
#     Columns.clear()


import os
DELIMITER = ";"


class TIMESTAMP:
    weekday: str = ""
    hour: str = ""
    consumption: float = 0.0
    price: float = 0.0


def readTimestamps(Pfilepath, timestamps):
    print('Reading file "{}".'.format(Pfilepath))

    with open(Pfilepath, "r", encoding="UTF-8") as fileHandle:
        for line in fileHandle:
            Row = line.rstrip()

            if Row == "":
                continue
            if "Weekday" in Row:
                continue

            Columns = Row.split(DELIMITER)
            timestamp = TIMESTAMP()
            timestamp.weekday = Columns[0]
            timestamp.hour = Columns[1]
            timestamp.hour = f"{timestamp.hour}:00"
            timestamp.consumption = float(Columns[2])
            timestamp.price = float(Columns[3])

            timestamps.append(timestamp)
    return None


def displayTimestamps(timestamps):
    print("Electricity usage:")
    for timestamp in timestamps:
        total = timestamp.consumption * timestamp.price
        print(f" - {timestamp.weekday} {timestamp.hour}, price {timestamp.price:.2f}, consumption {timestamp.consumption:.2f} kWh, total {total:.2f} €")
    return None


def main():
    print("Program starting.")
    filepath = input("Insert filename: ")
    # filepath = "A7_T4_D1.csv"
    timestamps: list[TIMESTAMP] = []
    readTimestamps(filepath, timestamps)
    displayTimestamps(timestamps)

    print("Program ending.")
    return None


if __name__ == "__main__":
    main()