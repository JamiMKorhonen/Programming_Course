# W7_5

# Analyse provided CSV data and create a summary of daily power usage and cost. Use the data from the provided csv-files A7_T5_D1.csv, A7_T5_D2.csv and A7_T5_D3.csv.

# For the summary, calculate the daily power usage and the cost.

#     Daily usage: Sum the consumption for each timestamp at the daily level. Use gatherer variable.
#     Daily cost: Multiply the consumption by the daily timestamp’s corresponding price. Then sum the results into an gatherer-type variable.

# Preferred datastructures:

#     Timestamps: list[TIMESTAMP]
#     Analysis helper: list[DAY_USAGE]
#     Results: list[str]


import os
DELIMITER = ";"
WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday",)


class TIMESTAMP:
    weekday: str = ""
    hour: str = ""
    consumption: float = 0.0
    price: float = 0.0

class DAY_USAGE:
    weekday: str = ""
    totalconsumption: float = 0.0
    totalcost: float = 0.0


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


def analyzeTimestamps(timestamps):
    print("Analysing timestamps.")

    Analysis: list[DAY_USAGE] = []
    for WEEKDAY in WEEKDAYS:
        day = DAY_USAGE()
        day.weekday = WEEKDAY
        Analysis.append(day)

    for timestamp in timestamps:
        for day in Analysis:
            if timestamp.weekday == day.weekday:
                day.totalconsumption += timestamp.consumption
                day.totalcost += timestamp.consumption * timestamp.price
                break

    print("Displaying results.")
    print("### Electricity consumption summary ###")
    for day in Analysis:
        print(f" - {day.weekday} usage {day.totalconsumption:.2f} kWh, cost {day.totalcost:.2f} €")
    print("### Electricity consumption summary ###")
    return None


def main():
    print("Program starting.")
    filepath = input("Insert filename: ")
    # filepath = "A7_T5_D1.csv"

    timestamps: list[TIMESTAMP] = []
    readTimestamps(filepath, timestamps)
    analyzeTimestamps(timestamps)

    print("Program ending.")
    return None


if __name__ == "__main__":
    main()