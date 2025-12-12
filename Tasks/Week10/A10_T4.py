########################################################
# Task A10_T4
# Developer Jami Korhonen
# Date 2025.12.10 (YYYY-MM-DD)
########################################################

# A10_T4 Merge sort (TEST TASK)

# Merge sort is a divine-and-conquer sorting algorithm that splits an array into smaller subarrays, recursively sorts them, and then merges them back to gether in sorted order. 
# It is very efficient sorting algorithm in terms of time and space complexity. It is also stable.
# One down side is that it is not sorting in-place, which means that it requires additional memory for merging.

# The merge sort pseudocode example below describes important aspects on how to implement it.
    # function merge(left, right):
    #     result = empty array
    #     while left and right are not empty:
    #         if left[0] ≤ right[0]:  # Change to ≥ for descending order
    #             append left[0] to result
    #             remove left[0] from left
    #         else:
    #             append right[0] to result
    #             remove right[0] from right
    #     append remaining elements of left and right to result
    #     return result
    # function mergeSort(array):
    #     if size of array ≤ 1:
    #         return array
    #     mid = size of array // 2
    #     left = mergeSort(array[0:mid])
    #     right = mergeSort(array[mid:])
    #     return merge(left, right)

# Expected interface for the algorithm:
    # def merge(PLeft: list[int], PRight: list[int], PMerge: list[int], PAsc: bool = True) -> None:
    #     return None
    # def mergeSort(PValues: list[int], PAsc: bool = True) -> None:
    #     # Sort PValues.
    #     # PAsc: in ascending order by default. False will sort in descending order.
    #     return None

# Commands:
    # # Tab 1 - Insert dataset name 'A10_D10.txt' manually
    # python A10_T4.py 
    # # Tab 2 - CLI Argument (sys.argv[1])
    # python A10_T4.py A10_D10.txt
    # # Tab 3 - CLI Argument (sys.argv[1])
    # python A10_T4.py A10_D100.txt


import copy
import time
import sys
from typing import Callable


def readValues(PValues: list[int | float]) -> str:
    """Reads integers from a file and returns the filename."""
    PValues.clear()

    if len(sys.argv) > 1:
        filename = sys.argv[1]
        print(f"The filename '{filename}' was passed via CLI.")
    else:
        filename = input("Insert filename: ")

    try:
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    PValues.append(int(line))
    except FileNotFoundError:
        print(f"ERROR: File '{filename}' not found.")
        return ""

    return filename


def merge(PLeft: list[int], PRight: list[int], PMerge: list[int], PAsc: bool = True) -> None:
    i = j = k = 0

    if PAsc:
        comp = lambda a, b: a <= b
    else:
        comp = lambda a, b: a >= b

    while i < len(PLeft) and j < len(PRight):
        if comp(PLeft[i], PRight[j]):
            PMerge[k] = PLeft[i]
            i += 1
        else:
            PMerge[k] = PRight[j]
            j += 1
        k += 1

    while i < len(PLeft):
        PMerge[k] = PLeft[i]
        i += 1
        k += 1

    while j < len(PRight):
        PMerge[k] = PRight[j]
        j += 1
        k += 1


def mergeSort(PValues: list[int], PAsc: bool = True) -> None:
    if len(PValues) <= 1:
        return

    mid = len(PValues) // 2
    left = PValues[:mid]
    right = PValues[mid:]

    mergeSort(left, PAsc)
    mergeSort(right, PAsc)

    merge(left, right, PValues, PAsc)


def formatList(values: list[int]) -> str:
    return ", ".join(str(v) for v in values)


def main() -> None:
    print("Program starting.")

    Values: list[int] = []
    filename = readValues(Values)

    if filename == "" or not Values:
        print("No data loaded. Program ending.")
        return

    print(f"Raw '{filename}' -> {formatList(Values)}")

    ascValues = copy.deepcopy(Values)
    mergeSort(ascValues, True)
    print(f"Ascending '{filename}' -> {formatList(ascValues)}")

    descValues = copy.deepcopy(Values)
    mergeSort(descValues, False)
    print(f"Descending '{filename}' -> {formatList(descValues)}")

    print("\nProgram ending.")
    return


if __name__ == "__main__":
    main()
