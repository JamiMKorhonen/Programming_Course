# A2_T7 Fahrenheit to Celcius

# Create a Python program to convert Fahrenheit to Celcius. Round the Celsius to 1 decimal precision.
# Formula to calculate Celcius from Fahrenheit is (Fahrenheit - 32) / 1.8


# Program starting.
print("Program starting.")

# Insert fahrenheits: 50
feed = float(input("Insert fahrenheits: "))
celsius = (feed - 32) / 1.8
celsius = round(celsius, 1)

# 50.0°F is 10.0°C
print(f"{feed}°F is {celsius}°C")

# Program ending.
print("Program ending.")


# Example program run:

# Program starting.
# Insert fahrenheits: 50
# 50.0°F is 10.0°C
# Program ending.
