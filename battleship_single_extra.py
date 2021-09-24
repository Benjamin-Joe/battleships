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
"""

    def get_user_input(self):
        try:
            x_row = input("Enter the for of the ship:  ")
            while x_row not in '123456789':
                print('Not a valid number, please select a VALID row ')
                x_row = input("Enter the row of ship:  ")

"""             
