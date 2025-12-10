########################################################
# Task A9_T2
# Developer Jami Korhonen
# Date 2025.12.10 (YYYY-MM-DD)
########################################################

# A9_T2 Exit codes

# Prompt the user to insert exit code. 
# Exit the program with using sys.exit and the user defined exit code. 
# Remember to convert the value into an integer. sys.exit expects value between 0-255.


import sys


def main():
    print("Program starting.")

    feed = input("Insert exit code(0-255): ")
    exitCode = int(feed)
    
    if exitCode == 0:
        print("Clean exit")
    else:
        print("Error code")
        sys.exit(exitCode)

    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
