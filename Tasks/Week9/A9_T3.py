########################################################
# Task A9_T3
# Developer Jami Korhonen
# Date 2025.12.10 (YYYY-MM-DD)
########################################################

# A9_T3 File exists

# Write a small Python program which read a text file. 
# If the file doesn’t exist, the program must print error message to the user and the program must exit with code 1.
# Otherwise print the file content and continue program run normally.
# Test file
#     A9_T3_D1.txt


import sys


def readLines(Pfilepath: str, Plines: list[str]):
    try:
        FileHandle = open(Pfilepath, 'r', encoding="UTF-8")
        line = FileHandle.readline()
        while line != "":
            Plines.append(line)
            line = FileHandle.readline()
    except FileNotFoundError:
        print(f"Couldn't read file \"{Pfilepath}\".")
        sys.exit(1)
    # except Exception:
    #     print("Could not read file")
    #     sys.exit(1)
    return None


def main():
    Lines: list[str] = []
    print("Program starting.")

    filename = input("Insert filename:  ")
    # filename = "A9_T3_D1.txt"
    
    readLines(filename, Lines)

    print(f"## {filename} ##")
    for line in Lines:
        print(line)
    print(f"## {filename} ##")

    print("Program ending.")
    return None


if __name__ == "__main__":
    main()

