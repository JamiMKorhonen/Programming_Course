########################################################
# Task A10_T1
# Developer Jami Korhonen
# Date 2025.12.10 (YYYY-MM-DD)
########################################################


# A10_T1 Read and display data

# First download the datasets above. Then create a program which prompts user to insert a filename and then displays the file content in two different ways:
#     Vertically - Each value on its own row.
#     Horizontally - Values on the same row, separated by comma and space “, ”.
# While reading the file rows, strip the newline characters and ignore empty rows.


def main():
    print("Program starting.")

    filename = input("Insert filename: ")

    try:
        with open(filename, 'r') as file:
            lines = [line.strip() for line in file if line.strip()]

        print("# --- Vertically --- #")
        for line in lines:
            print(line)
        print("# --- Vertically --- #")

        print("# --- Horizontally --- #")
        print(", ".join(lines))
        print("# --- Horizontally --- #")
    except Exception as err:
        print(err)

    print("Program ending.")


if __name__ == "__main__":
    main()