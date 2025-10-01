# A3_T5 Temperature converter (TEST TASK)

# Create a temperature unit conversion program.

# Start the program by listing options for the user:
#     Celsius to Fahrenheit
#     Fahrenheit to Celsius
#     Exit Prompt user to insert choice. After the decision to convert, ask the amount of current temperature (use the floating point datatype). Lastly show the converted value to the user.
# For the unit conversions, use the formula Celsius = (Fahrenheit - 32) / 1.8
# Data representation examples:
#     50.0 °F
#     10.0 °C Use 1 decimal precision to round the converted value.
# If the user chooses option Exit, notify the user: Exiting...


# Program starting.
print("Program starting. \n")
# Options:
print("Options:")
# 1 - Celsius to Fahrenheit
print("1 - Celsius to Fahrenheit")
# 2 - Fahrenheit to Celsius
print("2 - Fahrenheit to Celsius")
# 0 - Exit
print("0 - Exit")
# Your choice: 1
feed = int(input("Your choice: "))

# 1 - Celsius to Fahrenheit
# Insert the amount of Celsius: 23
# 23.0 °C equals to 73.4 °F
if feed == 1:
    cel = float(input("Insert the amount of Celsius: "))
    fah = (cel * 1.8) + 32
    print(f"{cel} °C equals to {fah} °F")

# 2 - Fahrenheit to Celsius
# Insert the amount of Fahrenheit: 100
# 100.0 °F equals to 37.8 °C
elif feed == 2:
    fah = float(input("Insert the amount of Fahrenheit: "))
    cel = (fah - 32) / 1.8
    cel = round(cel, 1)
    print(f"{fah} °F equals to {cel} °C")

# 0 - Exit
elif feed == 0:
    print("Exiting...")

else:
    print("Unknown option.")

# Program ending.
print("\nProgram ending.")


# Example program runs

# # Run 1 - Celsius to Fahrenheit
# Program starting.

# Options:
# 1 - Celsius to Fahrenheit
# 2 - Fahrenheit to Celsius
# 0 - Exit
# Your choice: 1
# Insert the amount of Celsius: 23
# 23.0 °C equals to 73.4 °F


# # Run 2 - Fahrenheit to Celsius
# Program starting.

# Options:
# 1 - Celsius to Fahrenheit
# 2 - Fahrenheit to Celsius
# 0 - Exit
# Your choice: 2
# Insert the amount of Fahrenheit: 100
# 100.0 °F equals to 37.8 °C

# Program ending.
