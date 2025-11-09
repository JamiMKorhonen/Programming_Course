# A6_T4 String analytics

# Datasets
#     A6_T4_D1.txt
#     A6_T4_D2.txt
#     A6_T4_D3.txt

# Create a Python program which is able to analyse names listed in a text file (See dataset files):
# Analyse and specify following aspects from the file:
#     The amount of names
#     Shortest name
#     Longest name
#     Average name length.

# Let the user specify the filename for the analysis. 
# Program reads the file and prints the results from the analysis. 
# Values must be presented like shown in the example program runs. 
# Average name length must be presented in 2 decimal precision. 
# Use Format Specification Mini-Language to achieving the required precision for the data presentation.

# Note! Given text files may contain empty rows and the program must be able to skip them if present.
# Other tips:
#     Read text file line-by-line.
#     Pay attention to the reading process (newline characters).
#     Names can be stored into a single string variable.
#         Consider separating names with a semicolon ;
#             John;Doe;Jane
#     Report can be stored into one string variable.
#     Format Specification Mini-Language.
#         E.g., "Value in 2 decimal precision {:.2f}".format(3.555)


def analyzeNames(Psourcefile):
    print(f"Reading names from \"{Psourcefile}\".")

    sourcecontent = ""
    Filehandle = open(Psourcefile, "r")
    for line in Filehandle:
        name = line.strip()
        if not name:
            continue
        if sourcecontent:
            sourcecontent += ";"
        sourcecontent += name
    Filehandle.close()

    return sourcecontent


def createReport(Psourcecontent):
    print("Analysing names...")

    names = Psourcecontent.split(';')
    count = len(names)

    shortest_name = min(names, key=len)
    shortest_length = len(shortest_name)
    longest_name = max(names, key=len)
    longest_length = len(longest_name)

    semicolons = Psourcecontent.count(";")
    wordcount = semicolons + 1
    totalchars = len(Psourcecontent)
    wordchars = totalchars - semicolons
    avg = wordchars / wordcount

    print("#### REPORT BEGIN ####")
    print(f"Name count - {count}")
    print(f"Shortest name - {shortest_length} chars")
    print(f"Longest name - {longest_length} chars")
    print("Average name - {:.2f} chars".format(avg))
    print("#### REPORT END ####") 

    print("Analysis complete!")
    return None


def main():
    print("Program starting.")
    print("This program analyses a list of names from a file.")

    sourcefile = input("Insert filename to read: ")

    sourcecontent = analyzeNames(sourcefile)
    createReport(sourcecontent)
 
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()


# Remember to change terminal directory to Week6!
# cd Tasks/Week6
