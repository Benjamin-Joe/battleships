from random import randint


# Options for player to chose
Choices = ["ROCK", "PAPER", "SCISSORS"]

# Computer chosing random move between Rock, Paper or Scissors

while True:
    Computer = Choices[randint(0, 2)]
    Player = input("Pick Rock, Paper, Or Scissors Or Press X To Quit:  ").upper()
    if Player == "X":
        print("Game Ended")
        break
    elif Player == Computer:
        print("Draw!")
    elif Player == "ROCK":
        if Computer == "PAPER":
            print("You Lose HAHA", Computer, "Beats", Player)
        else:
            print("You Win YAY!!", Player, "Beats", Computer)
    elif Player == "PAPER":
        if Computer == "SCISSORS":
            print("HAHA you lose!", Computer, "Beats", Player)
        else:
            print("You Win YAY!!", Player, "Beats", Computer)
    elif Player == "SCISSORS":
        if Computer == "ROCK":
            print("You lose HAHA!!", Computer, "Beats", Player)
        else:
            print("Winner Woo Hoo!", Player, "Beats", Computer)
