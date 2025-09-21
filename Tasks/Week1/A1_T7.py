# A1_T7 Fuel consumption

# Create a Python program that is able to calculate car’s fuel consumption (diesel or petrol) 
# and present the consumption in liters per 100km “x l per 100 km”

# Print info message “Calculate fuel consumtion.”
print("Calculate fuel consumption.")
# Ask “Enter travel distance(kilometers): ” and store the value to Feed variable
Feed = input("Enter travel distance(kilometers): ")
# Convert the Feed into an integer and assign it to Distance variable
Distance = int(Feed)
# Ask “Enter fuel usage(liters): ”
Feed = input("Enter fuel usage(liters):" )
# Convert the Feed into an integer and assign it to FuelUsage variable
FuelUsage = int(Feed)
# Calculate the Consumption for 100 km
Consumption = (FuelUsage/Distance) * 100
# Convert the Consumption back to an integer
Consumption = int(Consumption)
# Print “Fuel consumption is {Consumption} l per 100 km”
print("Consumption is", Consumption, "l per 100 km")

# Example program run:

# Calculate fuel consumption.
# Enter travel distance(kilometers): 200
# Enter fuel usage(liters): 20
# Fuel consumption is 10 l per 100 km