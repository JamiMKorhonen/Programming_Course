########################################################
# Task A10_T2
# Developer Jami Korhonen
# Date 2025.12.10 (YYYY-MM-DD)
########################################################

# A10_T2 Aggregate data

# Create a program that can analyse integers in a text file. 
# Filter empty rows and strip the newline characters so that each row can be converted into an integer datatype.

# Analysis:
#     Calculate the sum of the numbers
#     Calculate the product of the numbers

# Consider implementing the following aspects in the code:
    # import sys # for possible exit on errors
    # def readValues(PFilename: str, PValues: list[int]) -> None:
    #     # ...
    #     return None
    # def sumOfValues(PValues: list[int]) -> int:
    #     # ...
    #     return Sum
    # def productOfValues(PValues: list[int]) -> int:
    #     # ...
    #     return Product
    # def main() -> None:
    #     # 1. Initialize
    #     Values: list[int] = []
    #     # 2. Operate
    #     print("Program starting.")
    #     # 2.1 ask filename
    #     # 2.2 read values
    #     # 2.3 calculate sum of values
    #     # 2.4 calculate product of values
    #     # 2.5 display results
    #     # 3. Cleanup
    #     Values.clear()
    #     print("Program ending.")
    #     return None


import sys


def readValues(PFilename: str, PValues: list[int]) -> None:
    try:
        with open(PFilename, 'r') as fileHandle:
            for line in fileHandle:
                line = line.strip()
                if line:
                    try:
                        PValues.append(int(line))
                    except ValueError as err:
                        print(err)
    except FileNotFoundError as err:
        print(err)
        sys.exit(1)
    except Exception as err:
        print(err)
        sys.exit(1)
    return None


def sumOfValues(PValues: list[int]) -> int:
    Sum = sum(PValues)
    return Sum


def productOfValues(PValues: list[int]) -> int:
    Product = 1
    for value in PValues:
        Product *= value
    return Product


def main() -> None:
    # 1. Initialize
    Values: list[int] = []

    # 2. Operate
    print("Program starting.")
    
    # 2.1 ask filename
    filename = input("Insert filename: ")

    # 2.2 read values
    readValues(filename, Values)

    # 2.3 calculate sum of values
    total = sumOfValues(Values)
    
    # 2.4 calculate product of values
    product = productOfValues(Values)

    # 2.5 display results
    print("# --- Sum of numbers --- #")
    print(total)
    print("# --- Sum of numbers --- #")
    print("# --- Product of numbers --- #")
    print(product)
    print("# --- Product of numbers --- #")

    # 3. Cleanup
    Values.clear()
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
