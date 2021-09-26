from random import randint

# Legend
# X for placing ship and hitting ship
# ' ' for availiable space
# '-' for missed

hidden_board = [[' '] *9 for x in range(9)]
guess_board = [[' '] *9 for x in range(9)]

letters_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8}

def print_board(board):
    print('  A B C D E F G H I')
    print('  -----------------')
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1

def create_ships(board):
    for ship in range(5):
        ship_row, ship_column = randint(0,8), randint(0,8)
        while board[ship_row][ship_column] == 'X':
            ship_row, ship_column = randint(0,8), randint(0,8)
        board[ship_row][ship_column] = 'X'

def get_ship_location():
    row = input('Please Enter A Ship Row 1-9:  ')
    while row not in '123456789':
        print('Please Enter A VALID ROW:  ')
        row = input('Please Enter A Ship Row 1-9:  ')
    column = input('Please ENter A Letter A To I:  ').upper()
    while column not in 'ABCDEFGHI':
        print('Please Enter A VALID Letter:  ')
        column = input('Please Enter A Letter A To I_  ').upper()
except ValueError and KeyError:
    print("Not VALID input !!")
    return self.get_user_input()
    return int(row) - 1, letters_to_numbers[column]

def count_hit_ship(board):
    count = 0
    for row in board:
        for column in row:
            if column == 'X':
                count += 1
    return count

create_ships(hidden_board)
turns = 50
while turns > 0:
    print('Welcome To Battleships')
    print_board(guess_board)
    row, column = get_ship_location()
    if guess_board[row][column] == '-':
        print('You Guessed There Already')
    elif hidden_board[row][column] == 'X':
        print('Yay You Hit!!')
        guess_board[row][column] = 'X'
        turns -= 1
    else:
        print('Ha You Missed!!')
        guess_board[row][column] = '-'
        turns -= 1
    if count_hit_ship(guess_board) == 5:
        print('Yay You Won!!')
        break
    print('You Have ' + str(turns) + ' Turns Remaining')
    if turns == 0:
        print('You Lost!!')
        break

