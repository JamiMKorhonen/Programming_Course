# A4_T2 For-loop 2

# Copy the previous program and modify the behaviour to match the example program run below. 
# This program must use “for-loop” structure.
# It is recommended to replace the print-command end character with space, so that all the iterations can be printed on the same row. 
# Last iteration might require additional logic to get rid of the extra space at the end.


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
    print(i, end=" ")

# Program ending.
print("\n\nProgram ending.")
