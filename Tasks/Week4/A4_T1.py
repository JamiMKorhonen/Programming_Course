# A4_T1 For-loop 1

# Create a Python program which prompts user to insert two integers. 
# Use these integers together with the “for-loop” structure to create behaviour like in the example program example run below.


# Program starting.
print("Program starting.\n")

# Insert starting value: 1
start = int(input("Insert starting value: "))
start = start - 1
# Insert stopping value: 10
stop = int(input("Insert stopping value: "))

# Starting for-loop:
print("\nStarting for-loop:")
for i in range(start, stop):
    i += 1
    print(i)

# Program ending.
print("\nProgram ending.")
