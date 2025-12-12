########################################################
# Task A10_T5
# Developer Jami Korhonen
# Date 2025.12.12 (YYYY-MM-DD)
########################################################

# A10_T5 Recursive factorial

# Create a CLI program which can calculate factorial recursively. 
# Collect factorial from the user input.

# Factorial definition (recursive):
# n! = n × (n − 1)!

# Note! This exercise is designed so you can practice how the recursion works. 
# However, it is often recommended to avoid using recursive calls in programs. 
# Recursive calls can lead to a stack overflow if the recursion depth exceeds the system’s maximum stack size. 
# In Python, the interpreter raises a RecursionError in such cases.


def factorial(number):
    if number <= 1:
        return 1
    return number * factorial(number - 1)


def main():
    print("Program starting.")
    
    number = int(input("Insert factorial: "))
    
    print(f"Factorial {number}!")
    
    chain = "*".join(str(i) for i in range(1, number + 1))

    result = factorial(number)

    print(f"{chain} = {result}")
    print("Program ending.")


if __name__ == "__main__":
    main()
