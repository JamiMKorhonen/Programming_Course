# A3_T1 If-statements

# Make Python program and implement if-statements in proper places.

#     Ask user to insert two integers
#     Compare the integers and then announce the greater number
#     Create sum of the two integers
#     Check the parity of the sum (see modulo-operator ‘%’)

# Other possible output variants:

#     Integer comparison
#         Integers are the same.
#         First integer is greater.
#     Parity check
#         Sum is even.


# Program starting.
print("Program starting.")
# Insert two integers.
print("Insert two integers.")
# Insert first integer: 
int1 = int(input("Insert first integer: "))
# Insert second integer: 
int2 = int(input("Insert second integer: "))
# Comparing inserted integers.
print("Comparing inserted integers.")
# First integer is greater.
if int1 > int2:
    print("First integer is greater.")
elif int2 > int1:
    print("Second integer is greater.")
elif int1 == int2:
    print("Integers are the same")

# Adding integers together
print("\nAdding integers together")
# 2 + 3 = 5
sum = (int1 + int2)
print(f"{int1} + {int2} = {sum}")

# Checking the parity of the sum...
parity = sum % 2
# Sum is odd/even
if parity == 0:
    print("Sum is even")
else:
    print("Sum id odd")
# Program ending.
print("Program ending.")