# A2_T2: Escape sequence and print parameters

# Make a Python program, which prompts user for a car brand and model. 
# After user inputs, do print the car brand and model sentence with two print commands using “step” and “end” parameters.

# Program starting.
print("Program starting.")
# Insert car brand: Toyota
CarBrand = input("Insert car brand: ")
# Insert car model: Corolla
CarModel = input("Insert car model: ")
# Car brand is "Toyota" and the model is 'Corolla'.
print("Car brand is", f"\"{CarBrand[0::]}\"", "and the model is", end=" ")
print(f"'{CarModel[::]}'", "", sep=".")
# Program ending.
print("Program ending.")


# Example program run:

# Program starting.
# Insert car brand: Toyota
# Insert car model: Corolla
# Car brand is "Toyota" and the model is 'Corolla'.
# Program ending.