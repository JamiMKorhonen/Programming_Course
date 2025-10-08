# A4_T6 Collatz Conjecture (TEST TASK)

# This mathematical problem is described in the following video: youtu.be/094y1Z2wpJg
# Also at the wikipedia: en.wikipedia.org/wiki/Collatz_conjecture

# Create a program which prompts the user to insert an integer and then display the collatz conjecture as shown in the examples below.


# Program starting.
print("Program starting.")

# Insert a positive integer: 10
feed = int(input("Insert a positive integer: "))

# 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
i=0
sequence = f"{feed}"
LoopAgain = True

while LoopAgain == True:
    i += 1
    ChkEven = feed % 2
    if ChkEven == 0:
        feed = feed // 2
        sequence = sequence + f" -> {feed}"
    else:
        feed = feed * 3 + 1
        sequence = sequence + f" -> {feed}"
    if feed == 1:
        break
print(sequence)

# Sequence had 6 total steps.
print(f"Sequence had {i} total steps.\n")

# Program ending.
print("Program ending.")



#Example run 1

# Program starting.
# Insert a positive integer: 10
# 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# Sequence had 6 total steps.

# Program ending.
