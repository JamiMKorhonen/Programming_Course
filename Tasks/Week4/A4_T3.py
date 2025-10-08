# A4_T3 While-loop

# Make Python program which prompts user to insert two integers. 
# Use these integers together with the “while-loop” structure to create behaviour like in the example program run below.


# Program starting.
print("Program starting.\n")

# Insert starting value: 1
start = int(input("Insert starting value: "))
start = start - 1
# Insert stopping value: 10
stop = int(input("Insert stopping value: "))

# Starting while-loop:
print("\nStarting while-loop:")
LoopAgain = True
while LoopAgain == True:
    start += 1
    print(start, end=" ")

    if start >= stop:
        LoopAgain = False

# Program ending.
print("\n\nProgram ending.")
