# A5_T4 Multiple parameter

# The following code should calculate the area of a rectangle based on the user inputs.
# Fix the example code below without altering defined function names or function parameters. 
# Fixed code must produce similar results as is in the expected program runs. 
# The code must also be fixed to match the requirements in the provided style guide.

# def askDimension(PPrompt: str) -> float:
#    Feed = input("Insert number: ")
#    return Feed

# Width = askNumber("width")
# Height = askNumber("height")

# def calcRectangleArea(PWidth: float, PHeight: float) -> float:
#    PWidth = Area * PHeight
#    return Sum

# Area = calculateArea()
# print("")
# print("Area is {Area}²")
# print("end")


print("Program starting.")

def askDimension(PPrompt: str) -> float:
   Feed = float(input(f"Insert {PPrompt}: "))
   return Feed

Width = askDimension("width")
Height = askDimension("height")

def calcRectangleArea(PWidth: float, PHeight: float) -> float:
   Area = PWidth * PHeight
   return Area

Area = calcRectangleArea(Width, Height)

print(f"\nArea is {Area}²")

print("Program ending.")