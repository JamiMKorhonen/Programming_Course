# T1 - Positive Integer Collector

# Create a program that collects positive integers from the user until user enters a negative integer. 
# After this, the program should then display the collected integers along with their indices and ordinals. 
# If no integers are entered, the program should gracefully handle the situation by displaying an appropriate message.
#     Input: The program repeatedly prompt the user to enter positive integers. If the user enters a negative integer, the input process stops.
#     Validation: Only positive integers should be collected. A negative integer stops the input collection.
#     Output:
#         After input is stopped, the program will display the collected integers.
#         For each integer, show the following:
#             Index (starting from 0).
#             Ordinal (index + 1).
#         If there are no integers, inform the user that there are no integers to display.
#     Program Flow:
#         The program starts with the message: “Program starting.”
#         Collect positive integers from the user.
#         Stop collecting on a negative number.
#         After stopping input, display the results.
#         The program ends with the message: “Program ending.”
# Preferred datastructures:
#     list[int]


def askPositiveInteger():
    PositiveInt = -1
    feed = input("Insert positive integer(negative stops): ")
    if feed.isnumeric():
        PositiveInt = int(feed)
    return PositiveInt


def displayIntegers(Numbers):
    if len(Numbers) == 0:
        print("No integers to display")
    else:
        print(f"Displaying {len(Numbers)} integers:")
        for i in range(len(Numbers)):
            print(f"- Index {i} => Ordinal {i+1} => Integer {Numbers[i]}")
    return None


def main():
    print("Program starting.")
    print("Collect positive integers.")

    PositiveIntegers: list[int] = []
    CurrentInteger = askPositiveInteger()
    while CurrentInteger >= 0:
        PositiveIntegers.append(CurrentInteger)
        CurrentInteger = askPositiveInteger()
    #print(PositiveIntegers)
    print("Stopped collecting positive integers.")

    displayIntegers(PositiveIntegers)

    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
