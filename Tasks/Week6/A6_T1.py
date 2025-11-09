# A6_T1 Read text file

# Datasets
#     A6_T1_D1.txt
#     A6_T1_D2.txt
#     A6_T1_D3.txt

# Create a program that can read a text file and then print the file content. User must be able to specify the file name. Decorate the beginning and the end of the file with a decorative line.

# Decorative lines

#     #### START "{filename}" ####
#     #### END "{filename}" ####


def main():
    print("Program starting.")
    print("This program can read a file.")
    filename = input("Insert filename: ")
    print(f"#### START {filename} ####")


    # See A6_T3 readFile() if file content needs to be saved into variable
    file = open(filename, "r")
    while True:
        line = file.readline()
        if len(line) == 0:
            break
        print(line, end="")
    file.close()

    print(f"\n#### END {filename} ####")
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()


# Remember to change terminal directory to Week6!
# cd Tasks/Week6