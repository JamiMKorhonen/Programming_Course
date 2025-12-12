# ########################################################
# # Task A10_T6
# # Developer Jami Korhonen
# # Date 2025.12.12 (YYYY-MM-DD)
# ########################################################

# A10_T7 Minesweeper field

# Minesweeper is a classic puzzle game where player uncovers tiles on a grid while avoiding hidden mines. 
# The goal is to clear the board by revealing all non-mine tiles or flagging all mines without triggering one.

# The entire Minesweeper game can be implemented in approximately 500 lines of Python or JavaScript code, depending on the approach and complexity. 
# This exercise aims to guide you on this journey by introducing the first step of game development, which is the board creation (~150 lines of code).

# Design three Python functions to create a minefield for the Minesweeper game
# You can add additional helper functions if needed, but the specified functions must remain in place with the provided interface and adhere to the described behaviour in the documentation. 
# Functions layMines, calculateNearbys and generateMinefield will be extracted from the code and tested to ensure proper functionality and validation.
# Note! in this exercise, avoid using multiple program files. Create one python file A10_T7.py.


import random
random.seed(1234)


def showOptions() -> None:
    print("\nOptions:")
    print("1 - Generate minesweeper board")
    print("2 - Show generated board")
    print("3 - Save generated board")
    print("0 - Exit")
    return None


def layMines(PMineField: list[list[int]], PMines: int):
    rows = len(PMineField)
    cols = len(PMineField[0])
    placed = 0
    while placed < PMines:
        r = random.randint(0, rows - 1)
        c = random.randint(0, cols - 1)
        if PMineField[r][c] != 9:
            PMineField[r][c] = 9
            placed += 1


def calculateNearbys(PMineField: list[list[int]]) -> None:
    rows = len(PMineField)
    cols = len(PMineField[0])
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    for r in range(rows):
        for c in range(cols):
            if PMineField[r][c] == 9:
                continue
            count = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if PMineField[nr][nc] == 9:
                        count += 1
            PMineField[r][c] = count


def generateMinefield(
        PMineField: list[list[int]],
        PRows: int,
        PCols: int,
        PMines: int) -> None:
    PMineField.clear()
    for _ in range(PRows):
        PMineField.append([0]*PCols)
    layMines(PMineField, PMines)
    calculateNearbys(PMineField)


def main() -> None:
    PMineField = []
    while True:
        showOptions()
        choice = input("Your choice: ")
        if choice == "1":
            rows = int(input("Insert rows: "))
            cols = int(input("Insert columns: "))
            mines = int(input("Insert mines: "))
            generateMinefield(PMineField, rows, cols, mines)
        elif choice == "2":
            if PMineField:
                for row in PMineField:
                    print(row)
            else:
                print("No board generated yet.")
        elif choice == "3":
            if PMineField:
                filename = input("Insert filename: ")
                with open(filename, "w") as f:
                    for row in PMineField:
                        f.write(",".join(map(str,row)) + "\n")
            else:
                print("No board to save.")
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Invalid choice, try again.")
    print("\nProgram ending.")
    return None


if __name__ == "__main__":
    main()
