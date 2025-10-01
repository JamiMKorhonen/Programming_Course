# A3_T6 Submenu (TEST TASK)

# Create menu program with submenus. Mainly for unit conversions. Use the values from the following table for unit conversions https://www.isa.org/getmedia/192f7bda-c77c-480a-8925-1a39787ed098/CCST-Conversions-document.pdf
# Menu options:
#     Length
#         Meters to kilometers
#         Kilometers to meters
#     Weight
#         Grams to pounds
#         Pounds to grams
#     Exit
#         “Exiting...”
# Handle all the data in floating point datatype. Remember to round every value in 1 digit precision right before displaying.
# Other possible prints:
#     “Unknown option.”


# Program starting.
print("Program starting.")
# Welcome to the unit converter program!
print("Welcome to the unit converter program!")
# Follow the menu instructions below.
print("Follow the menu instructions below.")

# Options:
print("\nOptions")
# 1 - Length
print("1 - Length")
# 2 - Weight
print("2 - Weight")
# 0 - Exit
print("0 - Exit")
# Your choice:
main = int(input("Your choice: "))


# # main - Length
if main == 1:
    # Length options:
    print("\nLength options:")
    # 1 - Meters to kilometers
    print("1 - Meters to kilometers")
    # 2 - Kilometers to meters
    print("2 - Kilometers to meters")
    # 0 - Exit
    print("0 - Exit")
    # Your choice:
    length = int(input("Your choice: "))
    
    # length - Meters to kilometers
    if length == 1:
        # Insert meters: 1000
        meters = float(input("Insert meters: "))
        # 1000.0 m is 1.0 km
        km = meters / 1000
        km = round(km, 1)
        print(f"{meters} m is {km} km")

    # length - Kilometers to meters
    elif length == 2:
        # Insert kilometers: 20
        km = float(input("Insert kilometers: "))
        # 20.0 km is 20000.0 m
        meters = km * 1000
        meters = round(meters, 1)
        print(f"{km} km is {meters} m")

    #length - Exit
    elif length == 0:
        print("Exiting...")

    #length - Unknown option
    else:
        print("Unknown option.")


elif main == 2:
    # weight options:
    print("\nWeight options:")
    # 1 - Grams to pounds
    print("1 - Grams to pounds")
    # 2 - Pounds to grams
    print("2 - Pounds to grams")
    # 0 - Exit
    print("0 - Exit")
    # Your choice:
    weight = int(input("Your choice: "))

    # weight - Grams to pounds
    if weight == 1:
        # Insert grams: 100
        grams = float(input("Insert grams: "))
        # 100.0 g is 0.2205 lb
        lb = (grams * 0.002205)
        lb = round(lb, 1)
        print(f"{grams} g is {lb} lb")

    # weight - Pounds to grams
    elif weight == 2:
        # Insert pounds: 1
        pounds = float(input("Insert punds: "))
        # 1.0 lb is 453.6 g
        grams = (pounds * 453.59237)
        grams = round(grams, 1)
        print(f"{pounds} lb is {grams} g")

    # weight - Exit
    elif weight == 0:
        print("Exiting...")

    # weight - Unknown option.
    else:
        print("Unknown option.")


# main - Exit
elif main == 0:
    print("Exiting...")

# main - Unknown option
else:
    print("Unknown option.")


# Program ending.
print("\nProgram ending.")











# # Example run 1

# Program starting.
# Welcome to the unit converter program!
# Follow the menu instructions below.

# Options:
# 1 - Length
# 2 - Weight
# 0 - Exit
# Your choice: 1

# Length options:
# 1 - Meters to kilometers
# 2 - Kilometers to meters
# 0 - Exit
# Your choice: 1
# Insert meters: 1000
# 1000.0 m is 1.0 km

# Program ending.


# # Example run 2

# Program starting.
# Welcome to the unit converter program!
# Follow the menu instructions below.

# Options:
# 1 - Length
# 2 - Weight
# 0 - Exit
# Your choice: 1

# Length options:
# 1 - Meters to kilometers
# 2 - Kilometers to meters
# 0 - Exit
# Your choice: 2
# Insert kilometers: 20
# 20.0 km is 20000.0 m

# Program ending.


# # Example run 3

# Program starting.
# Welcome to the unit converter program!
# Follow the menu instructions below.

# Options:
# 1 - Length
# 2 - Weight
# 0 - Exit
# Your choice: 1

# Length options:
# 1 - Meters to kilometers
# 2 - Kilometers to meters
# 0 - Exit
# Your choice: 3
# Unknown option.

# Program ending.


# # Example run 4

# Program starting.
# Welcome to the unit converter program!
# Follow the menu instructions below.

# Options:
# 1 - Length
# 2 - Weight
# 0 - Exit
# Your choice: 1

# Length options:
# 1 - Meters to kilometers
# 2 - Kilometers to meters
# 0 - Exit
# Your choice: 0
# Exiting...

# Program ending.


# # Example run 5

# Program starting.
# Welcome to the unit converter program!
# Follow the menu instructions below.

# Options:
# 1 - Length
# 2 - Weight
# 0 - Exit
# Your choice: 2

# Weight options:
# 1 - Grams to pounds
# 2 - Pounds to grams
# 0 - Exit
# Your choice: 1
# Insert grams: 100
# 100.0 g is 0.2205 lb

# Program ending.


# # Example run 6

# Program starting.
# Welcome to the unit converter program!
# Follow the menu instructions below.

# Options:
# 1 - Length
# 2 - Weight
# 0 - Exit
# Your choice: 2

# Weight options:
# 1 - Grams to pounds
# 2 - Pounds to grams
# 0 - Exit
# Your choice: 2
# Insert pounds: 1
# 1.0 lb is 453.6 g

# Program ending.


# # Example run 7

# Program starting.
# Welcome to the unit converter program!
# Follow the menu instructions below.

# Options:
# 1 - Length
# 2 - Weight
# 0 - Exit
# Your choice: 2

# Weight options:
# 1 - Grams to pounds
# 2 - Pounds to grams
# 0 - Exit
# Your choice: 3
# Unknown option.

# Program ending.


# # Example run 8

# Program starting.
# Welcome to the unit converter program!
# Follow the menu instructions below.

# Options:
# 1 - Length
# 2 - Weight
# 0 - Exit
# Your choice: 2

# Weight options:
# 1 - Grams to pounds
# 2 - Pounds to grams
# 0 - Exit
# Your choice: 0
# Exiting...

# Program ending.


# # Example run 9

# Program starting.
# Welcome to the unit converter program!
# Follow the menu instructions below.

# Options:
# 1 - Length
# 2 - Weight
# 0 - Exit
# Your choice: 0

# Exiting...

# Program ending.
