########################################################
# Task A9_T7
# Developer Jami Korhonen
# Date 2025.12.10 (YYYY-MM-DD)
########################################################


# A9_T7 CLI Copy tool with error handling

# Create a CLI tool for copying text files (similar to A6_T3). This time around, parse CLI arguments and write error handling to the program.
# A9_T7 Datasets
#     A9_T7_D1.txt
#     A9_T7_D2.txt
#     A9_T7_D3.txt

# CLI Arguments is a new topic, and we will dive into them later in the course (extras). 
# Python provides access to the CLI arguments via sys.argv, which is a list of strings.

# Example below illustrates how to access all CLI arguments:
    # import sys
    # def main() -> None:
    #     print("Program starting.")
    #     for i in range(len(sys.argv)):
    #         print("arg_{}: {}".format(i, sys.argv[i]))
    #     print("Program ending.")
    #     return None
    # main()

# Provide the arguments via CLI for example:
    # user@host:~/projects/ohj
    # $ python A9_T7.py src_file.txt dst_file.txt
    # Program starting.
    # arg_0: A9_T7.py
    # arg_1: src_file.txt
    # arg_2: dst_file.txt
    # Program ending.
    # user@host:~/projects/ohj
    # $ 

# To check if a file exists, one could use os.path.exists-function.
    # import os
    # Filename = input("Insert filename: ")
    # if (os.path.exists(Filename)):
    #     print('File "{}" exists.'.format(Filename))
    # else:
    #     print('File "{}" doesn\'t exists.'.format(Filename))

# In this exercise, write the program to handle following cases(see order):
#     1. Argument amount must be 3 (python_filename, src_file, dst_file) - if there are more or less arguments, inform user that there is invalid amount of arguments followed by the synopsis (CLI tool usage).
#     2. Test if destination file exists (prompt user to overwrite)
#     3. Try to open and copy files. If the operation fails, inform the user and exit program with exit code -1. Possible failure could occur if the source file doesn’t exist.


import sys
import os


def showHelp() -> None:
    print("[USAGE] python {} <source_file> <destination_file>".format(sys.argv[0]))
    return None


def copyFile(srcFile: str, dstFile: str) -> None:
    proceed = True

    if os.path.exists(dstFile):
        answer = input(f'Destination file "{dstFile}" already exists.\nDo you want to overwrite it? (y/n): ').strip().lower()
        if answer != 'y':
            proceed = False

    if proceed:
        try:
            with open(srcFile, 'r', encoding='UTF-8') as fileSource:
                content = fileSource.read()
            with open(dstFile, 'w', encoding='UTF-8') as fileDestination:
                fileDestination.write(content)
        except Exception:
            print(f'Couldn\'t copy "{srcFile}" to "{dstFile}".')
            print("Exiting program.")
            sys.exit(-1)

    return None


def main() -> None:
    print("Program starting.")

    if len(sys.argv) != 3:
        print("Error: Invalid number of arguments.")
        showHelp()
        sys.exit(-1)

    srcFile = sys.argv[1]
    dstFile = sys.argv[2]

    print(f'Source file "{srcFile}"')
    print(f'Destination file "{dstFile}"')

    copyFile(srcFile, dstFile)

    print("Program ending.")
    return None

if __name__ == "__main__":
    main()


# Run in terminal:
# python A9_T7.py A9_T7_D1.txt A9_T7_F1.txt
# python A9_T7.py A9_T7_D2.txt A9_T7_F1.txt
# python A9_T7.py A9_T7_D3.txt A9_T7_F1.txt
# python A9_T7.py A9_T7_D3.txt A9_T7_F1.txt A9_T7_F2.txt
# python A9_T7.py A9_T7_D5.txt A9_T7_F5.txt
