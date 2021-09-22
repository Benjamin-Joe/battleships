import random

# orientation
# Across Vertical
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
        print("%d|%s"| % (row_number, "|".join(row)))
        row_number += 1

def place_ships(board):
    # loop through length of ships
    for ship_length in length_of_ships:
        # loop until ship fits on board
        while True:
            if board == computer_board:
                orientation, row,column = random.choice(["Across", "Vertical"]), random.randint(0,8), random.randint(0,8)
                if check_ship_fits(ship_length, row, column, orientation):


def check_ship_fits(ship_length, row, column, orientation):
    if orientation == "Across":
        if column + ship_length > 9:
            return False
        else:
            return True
    else:
        if row + ship_length > 9:
            return False
        else:
            return True
    

def check_overlap():
    pass

def user_input():
    pass

def count_hit_ships():
    pass

def turn(board):
    pass

while True:

