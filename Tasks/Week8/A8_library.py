from time import sleep
from datetime import datetime


MONTHS = ( "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December" )
WEEKDAYS = ( "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday" )


def activatePause(duration) -> None:
    print(f"Pausing for {duration} seconds.")
    sleep(duration)
    print("Unpaused")
    return None


def add(PAddend1: float, PAddend2: float) -> float:
    return PAddend1 + PAddend2
def subtract(PMinuend: float, PSubtrahend: float) -> float:
    return PMinuend - PSubtrahend
def multiply(PMultiplicant: float, PMultiplier: float) -> float:
    return PMultiplicant * PMultiplier
def divide(PDividend: float, PDivisor: float) -> float:
    return PDividend / PDivisor


def addValues(values):
    added = 0
    for value in values:
        added += value
    return added


def readTimestamps(PFilename, PTimestamps):
    PTimestamps.clear()
    with open(PFilename, "r") as file:
        for line in file:
            stripped = line.strip()
            if stripped != "":
                ts = datetime.strptime(stripped, "%Y-%m-%dT%H:%M")
                PTimestamps.append(ts)
    return None


def calculateYears(PYear, PTimestamps):
    count = 0
    for ts in PTimestamps:
        if ts.year == PYear:
            count += 1
    return count


def calculateMonths(PMonth, PTimestamps):
    if PMonth not in MONTHS:
        return 0

    month_index = MONTHS.index(PMonth) + 1
    count = 0
    for ts in PTimestamps:
        if ts.month == month_index:
            count += 1
    return count


def calculateWeekdays(PWeekday, PTimestamps):
    if PWeekday not in WEEKDAYS:
        return 0

    weekday_index = WEEKDAYS.index(PWeekday)
    count = 0
    for ts in PTimestamps:
        if ts.weekday() == weekday_index:
            count += 1
    return count


