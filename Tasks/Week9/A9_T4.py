########################################################
# Task A9_T4
# Developer Jami Korhonen
# Date 2025.12.10 (YYYY-MM-DD)
########################################################


# A9_T4 Reasonable celsius

# Create a program, which collects reasonable Celsius. Range listed below:
#       TEMP_MIN = -273.15
#       TEMP_MAX = 10000

# For this exercise, define collectCelsius function which returns collected celsius or raises following error:
#       ValueError: "could not convert string to float: '{Feed}'"
#       Exception: "{Celsius} temperature out of range."


TEMP_MIN = -273.15
TEMP_MAX = 10000

def collectCelsius():

    try:
        celsius = input("Insert Celsius: ")
    except ValueError:
        print(f"could not convert string to float: \'{celsius}\'")
    celsius = float(celsius)
    if (celsius < TEMP_MIN) or (celsius > TEMP_MAX):
        raise Exception(f"{celsius} temperature out of range.")

    return celsius


def main():
    print("Program starting.")

    celsius = collectCelsius()
    print(f"You inserted {celsius}℃")

    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
