# A5_T3 Ask name

# Create a Python program with two functions:

#     main-function
#         Does the routines ("Program starting." and "Program ending.")
#         Utilizes askName-function.
#         Utilizes greetUser-function.
#         Returns None
#     askName-function
#         Prompts the user to insert name
#         Returns name
#     greetUser-function
#         Which takes PName as an argument
#         Greets the user "Hello {PName}!"
#         Returns None

# Note! Tests for this task relies on properly defined functions and may fail if the program is not written according to the instructions.


#     askName-function
def askName():
#         Prompts the user to insert name
    Pname = input("Insert name: ")
#         Returns name
    return Pname


#     greetUser-function
#         Which takes PName as an argument
def greetUser(Pname):
#         Greets the user "Hello {PName}!"
    print(f"Hello {Pname}!")
#         Returns None
    return None


#     main-function
def main():
#         Does the routines ("Program starting." and "Program ending.")
    print("Program starting.")
#         Utilizes askName-function.
    name = askName()
#         Utilizes greetUser-function.
    greetUser(name)
#         Returns None
    print("Program ending.")
    return None

main()