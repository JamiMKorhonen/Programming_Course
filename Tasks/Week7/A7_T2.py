# T2 - Analyse separated values

# Create a Python program that processes a list of comma-separated integers entered by the user.
# The program will perform the following operations:
#     Parse the input, validate that all entries are valid integers.
#     If an invalid value is detected, output an error message indicating the invalid value, but still process the valid integers.
#     Calculate the sum of the valid integers and determine if the sum is even or odd.
#     Display the total count of valid integers, the sum of the integers, and whether the sum is even or odd.
#     If no valid integers are provided, display an appropriate message.
# Requirements:
#     Input:
#         The user inputs a comma-separated list of values.
#         The program parses these the entered values and checks if they are valid.
#     Output:
#         If all values are valid, display the number of integers, their sum, and whether the sum is even or odd.
#         If invalid values have been entered, display an error message for the invalid value.
#         If no valid integers remain after parsing, inform the user that there are no values to analyze.
# Preferred datastructures: list[int]


def askInteger(Values):
    feed = input("Insert comma separated integers: ")

    for Value in feed.split(','):
        if Value.isnumeric():
            Values.append(int(Value))
        else:
            print(f"Invalid value '{Value}' detected.")
            continue
    #print(Values)
    return None


def analyze(Values):
    Sum = 0
    if len(Values) == 0:
        print("No values to analyze.")
    else:
        for Value in Values:
            Sum += Value
        print(f"There are {len(Values)} integers in the list.")
        Parity = 'even' if Sum % 2== 0 else 'odd'
        print(f"Sum of the integers is {Sum} and it's {Parity}")
    return None


def main():
    print("Program starting.")

    Values: list[int] = []
    askInteger(Values)
    analyze(Values)


    print("Program ending.")
    return None


if __name__ == "__main__":
    main()


# Example program runs
# Program starting.
# Insert comma separated integers: 2,2,1,3
# There are 4 integers in the list.
# Sum of the integers is 8 and it's even
# Program ending.