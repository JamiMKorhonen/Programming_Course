# A6_T7 Messages from the Four Emperors

# Each of the Four Emperors—Galba, Otho, Vitellius and Vespasian—has left a message in their own palaces. 
# Your task is to travel programmatically to each location and gather all their messages.
# You may travel only once per program run. Travel should begin by displaying the current location, followed by the process of traveling to the next location. 
# The first location is the “start” or “Home” location on the map below.

# Place names listed:
#     home
#     Galba's palace
#     Otho's palace
#     Vitellius' palace
#     Vespasian's palace

# Create a file “player_progress.txt” and initialize it with the following details.
#   current_location;next_location;passphrase
#   0;1;qvfpvcyvar

# Player progress file explained:
#     First row is the header row with the column names.
#     Data row 1
#         Current location id 0 refers to the starting point (Home).
#         Next location id 1 refers to the next objective (Galba's palace).
#         Passphrase ciphered (ROT13)
#     Next data row
#         Should be added after progress is made on it’s own new line in the same file.
# Once you have traveled to the destination, walk into the palace and shout the passphrase(print the plain version) to the guard as you enter. 
# After entering, locate the message (open file "{NextLocationId}_{PassPhrase}.gkg") and read the content.
# The “.gkg” file extension in this context means that the text file content is in ciphered form. 
# It can be deciphered back to plain text using the Ceasar Cipher (ROT13).
# Read the first line as ciphered text and append it to the player_progress.txt. 
# After the first line, save the plain version of the message into "{NextLocationId}-{PlainPassPhrase}.txt".

# Examples of message formats:
#     file1: Ciphered message "{NextLocationId}_{PassPhrase}.gkg"
# 0;1;qvfpvcyvar
# Cneg 0 - Lrne bs gur Sbhe Rzcrebef:
# Va NQ 68, nsgre Areb'f qrngu, Ebzr cyhatrq vagb punbf.
# Jvgu ab pyrne urve, gur rzcver fnj encvq cbjre fgehttyrf.
# Tnyon gbbx gur guebar svefg, sbyybjrq ol Bgub, Ivgryyvhf, naq svanyyl Irfcnfvna,
# rnpu onggyvat sbe pbageby va jung orpnzr gur Lrne bs gur Sbhe Rzcrebef.
#   file2: Plain version to save "{NextLocationId}-{PlainPassPhrase}.txt"
# Part 0 - Year of the Four Emperors:
# In AD 68, after Nero's death, Rome plunged into chaos.
# With no clear heir, the empire saw rapid power struggles.
# Galba took the throne first, followed by Otho, Vitellius, and finally Vespasian,
# each battling for control in what became the Year of the Four Emperors.

# After the progress and the Emperor’s message have been saved, the program closes with the final phrases. 
# The next time the program runs, it should be able to read the previous progress from player_progress.txt and continue the next turn.


import os

LOWER_ALPHABETS = "abcdefghijklmnopqrtsuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DELIMITER = ';'

def readFile(PFilename) -> str:
    Content = ''
    FileHandle = open(PFilename, 'r')
    Row = FileHandle.readline()
    while Row != '':
        Content += Row
        Row = FileHandle.readline()
    FileHandle.close()
    return Content


# With help from Sami Viljakainen (LAB)
def writeFile(PNextLocationId, PPassPhrase, PPlainPassPhrase):
    encrypted_filename = f"A6_T7_{PNextLocationId}_{PPassPhrase}.gkg"
    print(encrypted_filename)
    with open(encrypted_filename, "r", encoding="UTF-8") as f:
        encrypted_content = f.read()
    first_line_encrypted = encrypted_content.split('\n')[0]
    plain_content = rot(encrypted_content)
    plain_filename = f"A6_T7_{PNextLocationId}-{PPlainPassPhrase}.txt"
    with open(plain_filename, "w", encoding="UTF-8") as f:
        f.write(plain_content)
    return first_line_encrypted


# With help from Sami Viljakainen (LAB)
def appendToFile(current_id: int, next_id: int, passphrase: str, PlayerProgressFilename):
    new_line = f"{current_id}{DELIMITER}{next_id}{DELIMITER}{passphrase}"

    with open(PlayerProgressFilename, "a", encoding="UTF-8") as f:
        f.write(new_line + "\n")
        
    print("[Game] Progress autosaved!")
    return None


# With help from teacher Mira Vorne (LAB)
def shiftCharacter(Character: str, Alphabets: str, Shift: int = 13) -> str:
    #"""Shifts a character by 'Shift' positions in the given alphabet (ROT13 logic)."""
    NewCharacter = Character
    for i in range(len(Alphabets)):
        if (Character == Alphabets[i]):  # Find character in alphabet
            ShiftedIndex = i + Shift 
            if ShiftedIndex >= len(Alphabets):  # Go around the alphabets if necessary
                ShiftedIndex = ShiftedIndex - len(Alphabets)
            NewCharacter = Alphabets[ShiftedIndex]  # Get shifted character
    return NewCharacter


# With help from teacher Mira Vorne (LAB)
def rot(PContent: str, PShift: int = 13) -> str:
    #"""Applies ROT13 to an entire string."""
    NewContent = ""
    for Character in PContent:
        if (Character in LOWER_ALPHABETS):  # Lowercase letter
            NewContent += shiftCharacter(Character, LOWER_ALPHABETS, PShift)
        elif (Character in UPPER_ALPHABETS):  # Uppercase letter
            NewContent += shiftCharacter(Character, UPPER_ALPHABETS, PShift)
        else:
            NewContent += Character  # Non-alphabet characters remain unchanged
    return NewContent


def getLocation(locationId):
    Location = "unknown"
    if locationId == 0:
        Location = "Home"
    elif locationId == 1:
        Location = "Galba's palace "
    elif locationId == 2:
        Location = "Otho's palace "
    elif locationId == 3:
        Location = "Vitellius' palace "
    elif locationId == 4:
        Location = "Vespasian's palace "
    return Location


def main():
    print("Travel starting.")

    PlayerProgressFilename = "A6_T7_player_progress.txt"
    #print(PlayerProgressFilename)

    Progress = readFile(PlayerProgressFilename)
    LastProgress = Progress.strip().split('\n')[-1].split(DELIMITER)
    #print(Progress)
    #print(LastProgress)

    CurrentLocationId = int(LastProgress[0])
    CurrentLocation = getLocation(CurrentLocationId)
    #print(CurrentLocationId)
    #print(CurrentLocation)

    NextLocationId = int(LastProgress[1])
    NextLocation = getLocation(NextLocationId)
    #print(NextLocationId)
    #print(NextLocation)

    PassPhrase = LastProgress[2]
    PlainPassPhrase = rot(LastProgress[2])
    #print(PassPhrase)
    #print(PlainPassPhrase)


    print(f"Currently at {CurrentLocation}.")
    print(f"Travelling to {NextLocation}.")
    print(f"...Arriving to the {NextLocation}.")
    print("Passing the guard at the entrance.")
    print(f'"{PlainPassPhrase}!')
    print("Looking for the message in the palace...")
    print("Ah, there it is! Seems cryptic.")
    print("Deciphering Emperor's message...")

    next_progress = writeFile(NextLocationId, PassPhrase, PlainPassPhrase)
    #print(next_progress)
    new_current, new_next, new_passphrase = next_progress.split(DELIMITER)
    appendToFile(int(new_current), int(new_next), new_passphrase, PlayerProgressFilename)

    print("Looks like I've got now the plain version copy of the Emperor's message.")
    print("Time to leave...")
    print("Travel ending.")
    return None


if __name__ == "__main__":
    main()


#Example program run:
# Travel starting.
# Currently at home.
# Travelling to Galba's palace...
# ...Arriving to the Galba's palace.
# Passing the guard at the entrance.
# "Discipline!"
# Looking for the message in the palace...
# Ah, there it is! Seems cryptic.
# [Game] Progress autosaved!
# Deciphering Emperor's message...
# Looks like I've got now the plain version copy of the Emperor's message.
# Time to leave...
# Travel ending.
