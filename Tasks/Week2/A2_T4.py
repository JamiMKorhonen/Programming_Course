# A2_T4: Average and rounding

# Prompt the user to insert the minutes spent on each previous topic task. 
# Calculate the sum and the average. Display those in the example program run format (Note! precision). 
# Make sure to calculate the required average for two decimal digits and later integer as rounded integer (precision 0 + type conversion).


# Program starting.
print("Program starting.")
# Estimate how many minutes you spent on programming...
print("Estimate how many minutes you spent on programming...")

# A1_T1: 3
T1 = input("A1_T1: ")
T1 = int(T1)
# A1_T2: 7
T2 = input("A1_T2: ")
T2 = int(T2)
# A1_T3: 9
T3 = input("A1_T3: ")
T3 = int(T3)
# A1_T4: 8
T4 = input("A1_T4: ")
T4 = int(T4)
# A1_T5: 13
T5 = input("A1_T5: ")
T5 = int(T5)
# A1_T6: 14
T6 = input("A1_T6: ")
T6 = int(T6)
# A1_T7: 21
T7 = input("A1_71: ")
T7 = int(T7)

# In total you spent 75 minutes on programming.
Total = T1+T2+T3+T4+T5+T6+T7
print("In total you spent", Total, "minutes on programming.")
# Average per task was 10.71 min and same rounded to the nearest integer 11 min.
Average = float(Total/7)
Rounded = round(Total)
print("Average per task was", round(Average, 2), "min and same rounded to the nearest integer", Rounded, "min.")

# Program ending.
print("Program ending.")


# Example program run:

# Program starting.
# Estimate how many minutes you spent on programming...

# A1_T1: 3
# A1_T2: 7
# A1_T3: 9
# A1_T4: 8
# A1_T5: 13
# A1_T6: 14
# A1_T7: 21

# In total you spent 75 minutes on programming.
# Average per task was 10.71 min and same rounded to the nearest integer 11 min.

# Program ending.

