########################################################
# Task A9_T1
# Developer Jami Korhonen
# Date 2025.12.10 (YYYY-MM-DD)
########################################################

# A9_T1 Faulty user input

# Create a Python program that prompts the user to insert floating-point values. 
# If the user inserts 0, stop the prompt and print the sum of the inserted values.

# If the user inserts an invalid value, such as “aaaaa” or “1.b2”, print an error message indicating that the inserted value couldn’t be converted to a floating-point number. 
# Skip the incorrect feed and continue prompting.

# During the prompts, use the raw values for the presentation ("{}".format(Value)).
# In the final sum presentation, use two decimal presentation format. 
# This can be achieved by using the float format specifier.


def main():
    Sum = 0
    Value = -1

    while Value != 0:
        feed = input("Insert a floating-point value (0 to stop): ")
        try:
            Value = float(feed)
            Sum += Value
        except ValueError as err:
            print(f"Error! {Value} couldn't be converted to float.")
        except Exception as err:
            print(f"Error: {err}")

    print(f"\nFinal sum is {Sum}")
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
