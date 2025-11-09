# A6_T2 Write text file

# Create a program that can write a text file. 
# Prompt the user to insert first name and last name. 
# Then prompt the file name for the write operation. 
# Finally write a text file with first name on the first row and last name on the second row. 
# Ensure that the text file ends in a empty row. Finally exit the program cleanly.


def writeFile(Pfilename, Pcontent):
    Filehandle = open(Pfilename, "w")
    Filehandle.write(Pcontent)
    Filehandle.close()
    return None


def main():
    print("Program starting.")
    firstname = input("Insert first name: ")
    lastname = input("Insert last name: ")
    filename = input("Insert filename: ")

    content = "{}\n{}\n".format(firstname, lastname)
    writeFile(filename, content)

    print("Program ending.")
    return None


if __name__ == "__main__":
    main()


# Remember to change terminal directory to Week6!
# cd Tasks/Week6