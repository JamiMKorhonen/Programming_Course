########################################################
# Task A9_T5
# Developer Jami Korhonen
# Date 2025.12.10 (YYYY-MM-DD)
########################################################

# A9_T5 RGB (TEST TASK)

# Collect red, green and blue integer values, each on range 0-255 inclusively. 
# This range is often described as “byte” or 8-bit. 
# These 3 bytes (R, G and B) can be used to describe one color using hex notation “#rrggbb”, where the “rr” represents the amount of color red. 
# The hex notation is created using the byte information.
#   28 = 162 = 255

# Above notation:
#     28 - 0-1 * 8 - 8-bits (base2)
#     162 - 0-f * 2 - Hexadecimals (base16)
#     255 - 0-9 0-255 - Integer representation (base10)

# So for example value 127(base-10) converts to 01111111(base-2) in 8-bit format or 7F(base-16) in hexadecimal format.

# While prompting values, ensure that:
#     Values are numeric
#     Values are actually integers
#     Value is inclusively within the 0-255 range

# If any of these conditions aren’t met, then print the error message "Couldn't perform the designed task due to the invalid input values.". 
# Continue the program execution to the end normally skipping the RGB displaying part. 
# One way to achieve this is to use “try-except” for the whole process and then any incorrect value being collected raises exception. 
# See Python Doc: Raising Exceptions

# If the RGB was ok, then show the details like in the example program run. 
# String format specified {:02x} converts integer into 2-digit hex format. 
# More details in the Python Documentation page Format Specification Mini-Language.

# Hex conversion example in Python REPL:
#   >>> "#{:02x}{:02x}{:02x}".format(255, 127, 0)
#   '#ff7f00'


def askIntByte(PPrompt: str) -> int:
    # Ask for input
    Feed = input(PPrompt)

    try:
        value_float = float(Feed)
    except:
        print(f"\"{Feed}\" is non-numeric value.")
        raise Exception

    if not value_float.is_integer():
        print(f"\"{Feed}\" is non-numeric value.")
        raise Exception

    value_int = int(value_float)

    if (value_int < 0) or (value_int > 255):
        print(f"Value \"{Feed}\" is out of the range 0-255.")
        raise Exception

    return value_int


def createHex(red: int, green: int, blue: int) -> str:
    return "#{:02x}{:02x}{:02x}".format(red, green, blue)


def main():
    print("Program starting.")

    try:
        red = askIntByte("Insert red: ")
        green = askIntByte("Insert green: ")
        blue = askIntByte("Insert blue: ")
        hex = createHex(red, green, blue)

        print("RGB Details:")
        print(f"- Red {red} (binary {red:08b})")
        print(f"- Green {green} (binary {green:08b})")
        print(f"- Blue {blue} (binary {blue:08b})")
        print(f"- Hex {hex}")

    except:
        print("Couldn't perform the designed task due to the invalid input values.")

    print("Program ending.")


if __name__ == "__main__":
    main()
