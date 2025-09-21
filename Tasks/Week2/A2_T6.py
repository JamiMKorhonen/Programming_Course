# A2_T6 Hex Colors (TEST TASK)

# Write a Python program which asks user to insert hex color. 
# In this case hex color is expected to be the 7 character representation starting with # and followed by 6 0-F characters to represent RGB colors. 
# More about hex colors at https://en.wikipedia.org/wiki/Web_colors

# Slice the amount of red, green and blue from that inserted color and display each color as shown below.


# Program starting.
print("Program starting.\n")

# Insert a hex color: #FFA500
hex = input("Insert a hex color: ")

# Colors
print("\nColors")
# - Red FF
Red = hex[1:3:]
print("- Red", Red)
# - Green A5
Green = hex[3:5:]
print("- Green", Green)
# - Blue 00
Blue = hex [5:7:]
print("- Blue", Blue)

# Program ending.
print("\nProgram ending.")


# Example program run:

# Program starting.

# Insert a hex color: #FFA500

# Colors
# - Red FF
# - Green A5
# - Blue 00

# Program ending.
