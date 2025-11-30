# Build “rock-paper-scissors” game in Python. In this game, there are two players, user and bot named “RPS-3PO”.

# Rules for the RPS game:

#     Rock beats scissors
#     Paper beats rock
#     Scissors beat paper

# In this exercise, place the following at the beginning of the code (right at the top). 
# Setting the seed value means we are setting an initial state for the random number generator. 
# After this, the generated numbers will follow exactly the same sequence. 
# The random number will then depend on the number of calls to the random function.

# import random
# random.seed(1234)

# Randomize the bot’s choice in each game by calling the random.randint(1, 3) function with the given arguments. 
# This function call returns a random integer between 1 and 3, inclusive. 
# Implementing randomness in another way may lead to varying test results and is therefore not recommended.

# The program start by asking for the player’s name. 
# Then, greet the player and announce the opponent. After that, inform that the game is starting.

# The menu contains 4 options, first three are game related options. 
# If user chooses rock, paper or scissors from the menu, a round will be played.

# Display text "Rock! Paper! Scissors! Shoot!\n". 
# Then, reveal the player’s choice first, followed by the bot’s choice. 
# Show a decorative line of 25 hash (#) symbols between and around the choices to visually separate the player’s and the bot’s selections.

# Then check the players’ choice according to the rules of the RPS game. 
# If both players have chosen the same option, the result is a draw ("Draw! Both players chose ____."). 
# Otherwise, declare the winner and the reason for the victory based on the condition.


import random
random.seed(1234)



rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""" 


def welcomePlayer():
    print("Welcome to the rock-paper-scissors game!")
    # playerName = input("Insert player name: ")
    playerName = "John"
    print(f"Welcome {playerName}!")
    print("Your opponent is RPS-3PO.")
    print("Game starts...")
    return playerName

def options():
    print("\nOptions:")
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Scissors")
    print("0 - Quit game")


def game(playerName):
    playerWins = 0
    botWins = 0
    Draws = 0

    while True:
        options()
        option = input("Your choice: ")

        if option == "0":
            print("Results:")
            print(f"{playerName} - wins ({playerWins}), losses ({botWins}), draws ({Draws})")
            print(f"RPS-3PO - wins ({botWins}), losses ({playerWins}), draws ({Draws})")
            break
        elif option == "1":
            print("\n#########################")
            print("Rock! Paper! Scissors! Shoot!")
            print(f"{playerName} chose rock.")
            print(rock)
        elif option == "2":
            print("\n#########################")
            print("Rock! Paper! Scissors! Shoot!")
            print(f"{playerName} chose paper.")
            print(paper)
        elif option == "3":
            print("\n#########################")
            print("Rock! Paper! Scissors! Shoot!")
            print(f"{playerName} chose scissors.")
            print(scissors)

        print("\n#########################")
        botChoice = random.randint(1,3)
        if botChoice == 1:
            print(f"RPS-3PO chose rock.")
            print(rock)
        elif botChoice == 2:
            print(f"RPS-3PO chose paper.")
            print(paper)
        elif botChoice == 3:
            print(f"RPS-3PO chose scissors.")
            print(scissors)


        print("\n#########################\n")

        if option == "1":
            if botChoice == 1:
                print("Draw! Both players chose rock.")
                Draws += 1
            if botChoice == 2:
                print(f"RPS-3PO paper beats {playerName} rock.")
                botWins += 1
            if botChoice == 3:
                print(f"{playerName} rock beats RPS-3PO scissors")
                playerWins += 1

        if option == "2":
            if botChoice == 1:
                print(f"{playerName} paper beats RPS-3PO rock")
                playerWins += 1
            if botChoice == 2:
                print("Draw! Both players chose paper.")
                Draws += 1
            if botChoice == 3:
                print(f"RPS-3PO scissors beats {playerName} paper.")
                botWins += 1
        
        if option == "3":
            if botChoice == 1:
                print(f"RPS-3PO rock beats {playerName} scissors.")
                botWins += 1
            if botChoice == 2:
                print(f"{playerName} scissors beats RPS-3PO paper")
                playerWins += 1
            if botChoice == 3:
                print("Draw! Both players chose scissorcs.")
                Draws += 1
    return None


def main():
    print("Program starting.")
    playerName = welcomePlayer()
    game(playerName)
    print("\nProgram ending.")
    return None


if __name__ == "__main__":
    main()



# Program starting.
# Welcome to the rock-paper-scissors game!
# Insert player name: John
# Welcome John!
# Your opponent is RPS-3PO.
# Game starts...

# Options:
# 1 - Rock
# 2 - Paper
# 3 - Scissors
# 0 - Quit game
# Your choice: 1
# Rock! Paper! Scissors! Shoot!