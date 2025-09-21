# A1_T4 Printing and math operations

# Make Python program and add following procedures to it:

# Assign value 47 to variable Num1
num1 = 47
# Assign value 102 to a variable Num2
num2 = 102
# Sum variables Num1 and Num2, and put the result into Sum variable
sum = num1 + num2
# Subtract Num1 from Num2, then store the result in the Diff variable.
diff = num2 - num1
# Multiply Sum and Diff, then place the resulting product in Product.
product = sum * diff
# Print the sum operation “{Num1} + {Num2} = {Sum}”
print(num1, "+", num2, "=", sum)
# Print the sub operation “{Num2} - {Num1} = {Diff}”
print(num2, "-", num1, "=", diff)
# Print the multiply operation “{Sum} * {Diff} = {Product}”
print(sum, "*", diff, "=", product)
# Print the sum, sub and multiply operations together. See “program run” below.
print( "(", num1, "+", num2, ")", "*", "(", num2, "-", num1, ")", "=", product )

# Example program run:

# 47 + 102 = 149
# 102 - 47 = 55
# 149 * 55 = 8195
# ( 47 + 102 ) * ( 102 - 47 ) = 8195