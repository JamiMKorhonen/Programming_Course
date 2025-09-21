# A2_T1: Basic program structure

# Make a Python program, which prompts the user name and two floating numbers. 
# Multiply the inserted numbers to get product. Round the product in two decimal precision. 
# Complete the program output as shown below.

# Program starting.
print("Program starting.")
# What is your name: John
Name = input("What is your name: ")
# Enter a floating point number: 3.1
Feed = input("Enter a floating point number: ")
Number1 = float(Feed)
# Enter second floating point number: 5.3
Feed = input("Enter second floating point number: ")
Number2 = float(Feed)
# John you gave numbers 3.1 and 5.3
print(Name, "you gave numbers", Number1, "and", Number2)
Product = Number1 * Number2
# Multiplying first and second number will result in product 16.43
print("Multiplying first and second number will result in product", round(Product, 2) )
# Program ending.
print("Program ending.")


# Example program run:

# Program starting.
# What is your name: John
# Enter a floating point number: 3.1
# Enter second floating point number: 5.3
# John you gave numbers 3.1 and 5.3
# Multiplying first and second number will result in product 16.43
# Program ending.
