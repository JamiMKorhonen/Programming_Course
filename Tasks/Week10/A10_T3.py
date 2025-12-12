########################################################
# Task A10_T3
# Developer Jami Korhonen
# Date 2025.12.10 (YYYY-MM-DD)
########################################################

# A10_T3 Bubble sort (TEST TASK)

# Visit wikipedia: Bubble sort and see the pseudocode implementation. 
# Use it or some other source as a guide to build the sorting algorithm. 
# Once done, ensure that the function is pure and has the interface as defined below(naming, parameters and return values). 
# The bot will extract the function based on the A10_T3.py implementation. 
# If you have used A10_TLib.py to store the algorithm, the bot should be able to extract it from there too.

# After the sorting algorithm is extracted successfully, it will test if the sorting algorithm works. 
# Then it compares the extracted bubble sort algorithm into another algorithm to determine if the speed aligns with the expectations (BigO notation).

# Interface to implement. Note parameter PAsc is set by default to True. This means that the algorithm should sort everything in ascending order by default if only one argument is passed.
    # def bubbleSort(PValues: list[int], PAsc: bool = True) -> None:
    #     # Sort PValues by implementing bubble sort algorithm.
    #     # Handle PValues list like it is a pointer to memory
    #     # Sort the list inplace e.g., PValues[CurrentIndex] = PValues[NextIndex]
    #     # Don't overwrite PValues identifier.
    #     # Tester expects that the PValues list is modified.
    #     # It doesn't catch a return value.
    #     return None

# For the main program, prompt filename if there are no CLI arguments to the program. 
# In case the len(sys.argv) is 2, then take the second argument (sys.argv[1]) and use it as a filename.
# Commands:
    # # Tab 1 - Insert dataset name 'A10_D10.txt' manually
    # python A10_T3.py 
    # # Tab 2 - CLI Argument (sys.argv[1])
    # python A10_T3.py A10_D10.txt
    # # Tab 3 - CLI Argument (sys.argv[1])
    # python A10_T3.py A10_D100.txt


import sys
from A10_TLib import readValues, displayValues, bubbleSort


def main() -> None:
    # Initialize
    Values: list[int] = []
    Filename = ""

    print("Program starting.")

    # TODO: Handle CLI argument or prompt for filename
    # If len(sys.argv) == 2, use sys.argv[1]
    # Otherwise, ask the user to input the filename
    if len(sys.argv) == 2:
        Filename = sys.argv[1]
    else:
        Filename = input("Insert filename: ")

    # TODO: Read values from file into Values list using readValues()
    readValues(Values, Filename)

    # TODO: Print raw values using displayValues()
    displayValues(Values, Filename)

    bubbleSort(Values, PAsc=True)

    # TODO: Sort values in ascending order using bubbleSort()
    # TODO: Print sorted ascending values
    print(f"Ascending '{Filename}' ->", end=" ")
    print(*Values, sep=", ")

    # TODO: Sort values in descending order using bubbleSort(PAsc=False)
    # TODO: Print sorted descending values
    print(f"Descending '{Filename}' ->", end=" ")
    print(*Values, sep=", ")

    Values.clear()


if __name__ == "__main__":
    main()
