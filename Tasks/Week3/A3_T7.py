# A3_T7 Decision trees

# In this task the idea is to create a program where user can define an integer and choose the decision structure being applied to the inserted integer. Certain rules must be applied to specified value tresholds and the decision structure has partial role in the end results. Structure, order and operators matter, so do exactly as the task describes.
#     Prompt user to insert value as an integer.
#     Display menu
#         option 1 - In one multi-branched decision
#         option 2 - Independent if-statement decisions
#         option 0 - Exit
#     Prompt user to choose option
#     Apply following math operations in the options 1 & 2
#         One multi-branched decision structure:
#             Value is 400 or more => add 44 to the existing value
#             Value is 200 or more => add 22 to the existing value
#             Value is 100 or more => add 11 to the existing value
#         Independent if-statement decisions one after another:
#             Value is 400 or more => add 44 to the existing value
#             Value is 200 or more => add 22 to the existing value
#             Value is 100 or more => add 11 to the existing value
#         Exit: “Exiting…”
#     At the end of the options 1 & 2, show the results like in the example program runs.
# Other possible output variats:
#     “Unknown option.”


# Program starting.
print("Program starting.")

# Testing decision structures.
print("Testing decision structures.")
# Insert an integer: 
int1 = int(input("Insert an integer: "))
# Options:
print("Options:")
# 1 - In one multi-branched decision
print("1 - In one multi-branched decision")
# 2 - In multiple independent if-statements
print("2 - In multiple independent if-statements")
# 0 - Exit
print("0 - Exit")
# Your choice: 
choice = int(input("Your choice: "))


# Using one multi-branched decision structure.
if choice == 1:
    print("Using one multi-branched decision structure.")
# Result is 
    if int1 >= 400:
        int1 = int1 + 44
        print(f"Result is {int1}")
    elif int1 >= 200:
        int1 = int1 + 22
        print(f"Result is {int1}")
    elif int1 >= 100:
        int1 = int1 + 11
        print(f"Result is {int1}")

# Using multiple independent if-statements structure.
if choice == 2:
    print("Using multiple independent if-statements structure.")
# Result is 283
    if int1 >= 400:
        int1 = int1 + 44
    if int1 >= 200:
        int1 = int1 + 22
    if int1 >= 100:
        int1 = int1 + 11
    print(f"Result is {int1}")


# Exiting...
if choice == 0:
    print("Exiting...")

# Unknown option.
else:
    print("Unknown option.")

# Program ending.
print("\nProgram ending.")
