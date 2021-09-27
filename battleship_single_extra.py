import random

# gameboard


class gameboard:
    def __init__(self, board):
        self.board = board

    def get_letters_to_numbers():
        letters_to_numbers = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8}
        return letters_to_numbers

    def print_board(self):
        print("   A B C D E F G H I")
        print("   __________________")
        row_number = 1
        for row in self.board:
            print("%d|%s|" % (row_number, "|".join(row)))
            row_number += 1


class Battleship:
    def __init__(self, board):
        self.board = board

    def create_ships(self):
        for i in range(5):
            self.x_row, self.y_column = random.randint(0, 8), random.randint(0, 8)
            while self.board[self.x_row][self.y_column] == "X":
                self.x_row, self.y_column = random.randint(0, 8), random.randint(0, 8)
            self.board[self.x_row][self.y_column] = "X"
        return self.board

    def get_user_input(self):
        try:
            x_row = input("Enter the for of the ship:  ")
            while x_row not in '123456789':
                print('Not a valid number, please select a VALID row ')
                x_row = input("Enter the row of ship:  ")

            y_column = input("Enter the column letter of the ship:  ").upper()
            while y_column not in "ABCDEFGHI":
                print('Not an appropriate choice, Pick VALID letter')
                y_column = input("Enter the column letter of the ship:  ").upper()
            return int(x_row) -1, gameboard.get_letters_to_numbers()[y_column]
        except ValueError and KeyError:
            print("Not VALID input !!")
            return self.get_user_input()


def count_hit_ships(self):
    hit_ships = 0
    for row in self.board:
        for column in row:
            if column == "X":
                hit_ships += 1
    return hit_ships


def PlayGame():
    computer_board = gameboard([[" "] * 9 for i in range(9)])
    user_guess = gameboard([[" "] * 9 for i in range(9)])
    Battleship.create_ships(computer_board)
    turns = 50
    while turns > 0:
        gameboard.print_board(user_guess)
        user_x_row, user_y_column = Battleship.get_user_input(object)

        while user_guess.board[user_x_row][user_y_column] == "-" or user_guess.board[user_x_row][user_y_column] =="X":
            print("You already guessed there")
            user_x_row, user_y_column = Battleship.get_user_input(object)

        if computer_board.board[user_x_row][user_y_column] == "X":
            print("You sunk one of my ships!!")
            user_guess.board[user_x_row][user_y_column] = "X":
        else:
            print("Ha, You Mised Me!!")
            user_guess.board[user_x_row][user_y_column] = "-"


          
