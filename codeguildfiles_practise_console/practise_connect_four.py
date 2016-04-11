# -*- coding: utf-8 -*-
"""
Python Coding Bootcamp (pdxcodeguild)
Program exercise file input/output in Python
By Lab Partners: Andrew Theis, Matthew James K
Date: 4/4/2016
LAB/STEP requirements:

Practice: Connect Four
Connect Four is a board game. Players take turns placing tokens of their color into a vertical grid. They drop to the bottom,
and if anyone has four of their color in a straight line, they've won!

Create a program that simulates the moves of an existing Connect Four game.

It will read a file that contains a history of the moves in a game. Assume the playing board is made of columns numbered 1 through 7.
The file will have one line for each move (players alternate). The number in that line is the column the current player placed a token in.

Your board should be represented as a class. Think about how to concisely store the tokens that have been dropped in the board.

Use the following example move file. Save it in something like 4-moves.txt

4
3
5
6
4
4
5
3
6
2
7
7
3
7
4
5
6
5
This moves file recreates this game.

After each move, print out a representation of the board. You can use R and Y to represent the pieces.

Advanced

Once all moves are done, also print out what player, if any, won.
"""

class Token:
    def __init__(self, color):
        self.color = color
    def __str__(self):
        return 'Token({})'.format(self.color)
# end class Token:

class Board:
    def __init__(self, coordinates):
        self.coordinates = coordinates
        
    def check_if_cell_filled(self, move, token):
        row = 6
        while row > 0:
            target = str(move) + str(row) # '16'
            if self.coordinates[target] == ' ':
                self.coordinates[target] = token
                break
            else:
                row -= 1
                
    def __str__(self):
        d = self.coordinates
        return """
        {} | {} | {} | {} | {} | {} | {}
        -------------------------
        {} | {} | {} | {} | {} | {} | {}
        -------------------------
        {} | {} | {} | {} | {} | {} | {}
        -------------------------
        {} | {} | {} | {} | {} | {} | {}
        -------------------------
        {} | {} | {} | {} | {} | {} | {}
        -------------------------
        {} | {} | {} | {} | {} | {} | {}
        -------------------------
        """.format(d['11'], d['21'], d['31'], d['41'], d['51'], d['61'], d['71'],
        d['12'], d['22'], d['32'], d['42'], d['52'], d['62'], d['72'],
        d['13'], d['23'], d['33'], d['43'], d['53'], d['63'], d['73'],
        d['14'], d['24'], d['34'], d['44'], d['54'], d['64'], d['74'],
        d['15'], d['25'], d['35'], d['45'], d['55'], d['65'], d['75'],
        d['16'], d['26'], d['36'], d['46'], d['56'], d['66'], d['76'],)
# end class Board:

def read_game_moves_file():
    """
    This helper function reads in the game moves input file 4-moves.txt
    :returns: the games moves input as a list()-->[]
    """
    move_list = []
    with open('4-moves.txt') as moves_file:
        moves = moves_file.readlines()
        [ move_list.append(move.strip()) for move in moves ]
    return move_list
# end def read_game_moves_file():

def initialize_tokens():
    return [Token('R'), Token('Y')]
# end ​def initialize_tokens():

def initialize_board():
    board_coordinates = {}
    for column in columns:
        for row in rows:
            board_coordinates[str(column) + str(row)] = ' '
    board = Board(board_coordinates)
    return board
# end def initialize_board():

def execute_move_input(move_list_inputfile, token_object_users, connect_four_game_board):
    move_index = 0
    while move_index < len(move_list_inputfile):
        for token in token_object_users:
            move = move_list_inputfile[move_index]
            connect_four_game_board.check_if_cell_filled(move, token.color)
            move_index += 1
            print(connect_four_game_board)
            input('')
# end def execute_move_input(move_list, token_objects, board):

def main():
    board = initialize_board()
    token_objects = initialize_tokens()
    move_list = read_game_moves_file()
    execute_move_input(move_list, token_objects, board)
# end main():

columns = [1, 2, 3, 4, 5, 6, 7]
rows = [1, 2, 3, 4, 5, 6]

main()