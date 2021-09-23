import random

# orientation
# V = Vertical
# H = Horizontal
# length > 9 both ways 
#  Add random for picking number  
length_of_ships = [1, 2, 3, 4, 5]
player_board = [[" "] * 9 for i in range(9)]
computer_board = [[" "] * 9 for i in range(9)]
player_guess_board = [[" "] * 9 for i in range(9)]
computer_guess_board = [[" "] * 9 for i in range(9)]
letters_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8}

def print_board(board):
    print("  A B C D E F G H I")
    print("  +-+-+-+-+-+-+-+-+")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1

def place_ships(board):
    # loop through length of ships
    for ship_length in length_of_ships:
        # loop until ship fits on board
        while True:
            if board == computer_board:
                orientation, row, column = random.choice(["H", "V"]), random.randint(0,8), random.randint(0,8)
                if check_ship_fits(ship_length, row, column, orientation):
                    if check_overlap(board, row, column, orientation, ship_length)==False:
                        if orientation == "H":
                            for i in range(column, column + ship_length):
                                board [row][i] = "X"
                        else:
                            for i in range(row, row + ship_length):
                                board[i][column] = "X"
                        break
            else:
                place_ships = True
                print('place the ship with a length of' + str(ship_length))
                row, column, orientation = user_input(place_ships)
                if check_ship_fits(ship_length, row, column, orientation):
                    if check_overlap(board, row, column, orientation, ship_length) == False:
                        if orientation == "H":
                            for i in range(column, column + ship_length):
                                board[row][i] = "X"
                        else:
                            for i in range(row, row + ship_length):
                                board[i][column] = "X"
                        print_board(player_board)
                        break


def check_ship_fits(ship_length, row, column, orientation):
    if orientation == "H":
        if column + ship_length > 9:
            return False
        else:
            return True
    else:
        if row + ship_length > 9:
            return False
        else:
            return True
    

def check_overlap(board, row, column, orientation, ship_length):
    if orientation == "H":
        for i in range(column, column + ship_length):
            if board[row][i] == "X":
                return True
    else:
        for i in range(row, row + ship_length):
            if board[1][column] == "X":
                return True
    return False

def user_input(place_ships):
    if place_ships == True:
        while True:
            try:
                orientation = input("Enter orientation H(orizontal) or V(ertical):").upper()
                if orientation == "H" or orientation == "V":
                    break
            except TypeError:
                print('Enter a VALID orientation H or V')
        while True:
            try:
                row = input("Enter the row 1-9 of the ship: ")
                if row in '123456789':
                    row = int(row) - 1
                    break
            except ValueError:
                print('Enter a VALID number between 1 and 9')
        while True:
            try:
                column = input("Enter the column of the ship: ").upper()
                if column in 'ABCDEFGHI':
                    column = letters_to_numbers[column]
                    break
            except KeyError:
                print('Enter a VALID letter bewteen A and I')
        return row, column, orientation
    else:
        while True:
            try:
                row = input("Enter the row 1-9 of the ship:")
                if row in '123456789':
                    row = int(row) -1
                    break
            except ValueError:
                print('Enter a VALID number between 1-9')
        while True:
            try:
                column = input("Enter the column of the ship: ").upper()
                if column in 'ABCDEFGHI':
                    column = letters_to_numbers[column]
                    break
            except KeyError:
                print('Enter a VALID letter between A-I')
        return row, column

        


def count_hit_ships():
    pass

def turn(board):
    pass

while True:

