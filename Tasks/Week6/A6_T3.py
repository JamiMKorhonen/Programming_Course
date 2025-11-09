# A6_T3 Copy text file

# Datasets
#     A6_T3_D1.txt
#     A6_T3_D2.txt
#     A6_T3_D3.txt

# Create a program that copies a text file by reading from a source file and writing the content to a destination file. 
# Allow the user to specify the source and destination file names.


def readFile(Psourcefile):
    print(f"Reading file {Psourcefile} content.")

    sourcecontent = ""
    Filehandle = open(Psourcefile, "r")
    line = Filehandle.readline()
    while line != "":
        sourcecontent += line
        line = Filehandle.readline()
    Filehandle.close()
    
    print("File content ready in memory.")
    return sourcecontent


def writeFile(Pdestinationfile, Psourcecontent):
    print(f"Writing content into file {Pdestinationfile}.")

    Filehandle = open(Pdestinationfile, "w")
    Filehandle.write(Psourcecontent)
    Filehandle.close()

    print("Copying operation complete.")
    return None


def main():
    print("Program starting.")
    print("This program can copy a file.")

    sourcefile = input("Insert source filename: ")
    destinationfile = input("Insert destination filename: ")

    sourcecontent = readFile(sourcefile)

    writeFile(destinationfile, sourcecontent)

    print("Program ending.")
    return None


if __name__ == "__main__":
    main()


# Remember to change terminal directory to Week6!
# cd Tasks/Week6
