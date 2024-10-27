#How to Code Battleship in Python (https://www.youtube.com/watch?v=tF1WRCrd_HQ)
from random import randint
import os

#Board for the ship locations
HIDDEN_BOARD = [[" "] * 8 for x in range(8)]
# Board for tracking hits/misses
GUESS_BOARD = [[" "] * 8 for i in range(8)]

def welcome():
    os.system('clear')
    print("Welcome to Battleships!")
    print("Your goal is to sink the enemy ship,")
    print("This is done by typing a row and a column letter.")
    print("If a ship is hit, an 'x' will be shown.")
    print("If you miss, a '-' will be shown.")

def print_board(board):
    print("  A B C D E F G H")
    print("  +-+-+-+-+-+-+-+")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1

letters_to_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7
}

#Creates the ships
def create_ships(board):
    for ship in range(5):
        ship_row, ship_column = randint(0,7), randint(0,7)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = get_ship_location()
        board[ship_row][ship_column] = "X"

#Gets the ship location
def get_ship_location():
    row = input("Enter the row of the ship: ").upper()
    while row not in "12345678":
        print('Please select a valid row')
        row = input("Enter the row of the ship: ").upper()
    column = input("Enter the column of the ship: ").upper()
    while column not in "ABCDEFGH":
        print('Please select a valid column')
        column = input("Enter the column of the ship: ").upper()
    return int(row) - 1, letters_to_numbers[column]

#Checks if ships are hit
def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count

if __name__ == "__main__":
    create_ships(HIDDEN_BOARD)
    turns = 10
    while turns > 0:
        print('Guess a battleship location.')
        print_board(GUESS_BOARD)
        row, column = get_ship_location()
        if GUESS_BOARD[row][column] == "-":
            print("This spot has been checked already.")
        elif HIDDEN_BOARD[row][column] == "X":
            print("Hit")
            GUESS_BOARD[row][column] = "X" 
            turns -= 1  
        else:
            print("MISS!")
            GUESS_BOARD[row][column] = "-"   
            turns -= 1     
        if count_hit_ships(GUESS_BOARD) == 5:
            print("You win!")
            break
        print("You have " + str(turns) + " turns left")
        if turns == 0:
            print("You ran out of turns")