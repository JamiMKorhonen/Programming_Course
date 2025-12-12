########################################################
# Task A10_T6
# Developer Jami Korhonen
# Date 2025.12.12 (YYYY-MM-DD)
########################################################

# A10_T6 Sorting algorithm speed tests

# Create a menu-driven program which is able to measure nano seconds spent on sorting. 
# In this exercise, use datasets A10_D10.txt, A10_D100.txt and A10_1000.txt.

# Implement and/or use three sorting algorithm:
#     Built-in sorted
#     Bubble sort
#     Quick sort
# Build menu-driven program with 4 options
#     1 - Read dataset values
#     2 - Measure speeds
#     3 - Save results
#     0 - Exit

# Measure the sorting time on ascending order using the “time.perf_counter_ns()” function. 
# Sorting time can be calculated by subtracting starting time from the stopping time.

# Functions can also be passed as an argument to other functions. 
# Just omit the parentheses () when doing so. 
# The datatype is Callable which can be imported from the typing library.

# Also copy the original dataset using for example copy.deepcopy function so that the next sorting algorithm doesn’t receive already sorted array.
# Import the copy module first.

# Note! the speed results may vary.
#  Measuring speeds using “A10_D100.txt” or “A10_D1000.txt”, 
# the built-in sorted should be the quickest, followed by quick sort and slowest sorting algorithm should be bubble sort..


import copy
import time
from typing import Callable


def showOptions() -> None:
    print("\nOptions:")
    print("1 - Read dataset values")
    print("2 - Measure speeds")
    print("3 - Save results")
    print("0 - Exit")
    return None


def readValues(PValues: list[int|float]) -> str:
    # clear values list to ensure no duplicate data (reading twice)
    PValues.clear()
    # open filehandle
    Filename = input("Insert dataset filename: ")
    with open(Filename, 'r') as File:
        # read line-by-line
        for Line in File:
            # parse value(int) from line(str + '\n')
            Line = Line.strip()
            if not Line:
                continue
            Value = int(Line)
            # append value into the values list
            PValues.append(Value)
    # close filehandle
    return Filename


def quickSort(PNums: list[int]) -> list[int]:
    # https://en.wikipedia.org/wiki/Bubble_sort
    if len(PNums) <= 1:
        return PNums
    Pivot = PNums[0]
    Left = [x for x in PNums[1:] if x <= Pivot]
    Right = [x for x in PNums[1:] if x > Pivot]
    return quickSort(Left) + [Pivot] + quickSort(Right)


def bubbleSort(PNums: list[int]) -> list[int]:
    # https://en.wikipedia.org/wiki/Quicksort
    n = len(PNums)
    for i in range(n):
        for j in range(0, n-i-1):
            if PNums[j] > PNums[j+1]:
                PNums[j], PNums[j+1] = PNums[j+1], PNums[j]
    return PNums


def measureSortingTime(PSortingAlgorithm: Callable, PArr: list[int]) -> int:
    StartTime = time.perf_counter_ns()
    PSortingAlgorithm(PArr) # param is function
    EndTime = time.perf_counter_ns()
    ElapsedTime = EndTime - StartTime
    return ElapsedTime


def main() -> None:
    # 1. Initialize
    Values: list[int] = []
    Results: list[str] = []
    print("Program starting.")

    DatasetFilename = ""
    while True:
        showOptions()
        Choice = input("Your choice: ")

        if Choice == "1":
            DatasetFilename = readValues(Values)
        elif Choice == "2":
            # pass algorithm into the measureSortingTime function # import copy
            BuiltinSortedTimeNs = measureSortingTime(sorted, copy.deepcopy(Values))
            BubbleSortTimeNs = measureSortingTime(bubbleSort, copy.deepcopy(Values))
            QuickSortTimeNs = measureSortingTime(quickSort, copy.deepcopy(Values))
            print(f"Measured speeds for dataset '{DatasetFilename}':")
            print(f" - Built-in sorted {BuiltinSortedTimeNs} ns")
            print(f" - Buble sort {BubbleSortTimeNs} ns")
            print(f" - Quick sort {QuickSortTimeNs} ns")

            Results = [
                f"Measured speeds for dataset '{DatasetFilename}':",
                f" - Built-in sorted {BuiltinSortedTimeNs} ns",
                f" - Buble sort {BubbleSortTimeNs} ns",
                f" - Quick sort {QuickSortTimeNs} ns"
            ]
        elif Choice == "3":
            if not Results:
                continue
            ResultsFilename = input("Insert results filename: ")
            with open(ResultsFilename, "w") as f:
                f.write("\n".join(Results))
        elif Choice == "0":
            print("Exiting program.")
            break

    # 3. Cleanup
    Values.clear()
    Results.clear()
    print("\nProgram ending.")
    return None


if __name__ == "__main__":
    main()
