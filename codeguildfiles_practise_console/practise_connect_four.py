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

class Token(object):
    """
    A Token is one of two player instantiated instances
    """
    def __init__(self, color=''):
        """
        One argument constructor for a token that only has a color
        """
        self.color = color

    def __eq__():
        return

    def __repr__():
        return

class Board(object):
    """
    A Board is the x, y coordinate grid of empty cells at start of game
    """
    def __init__(self, board_coordinates={}):
        """
        Single arguement constructor to build the board grid as 'xy':'R or Y ' ' space as an empty cell coordinate:token foreach
        dictionary element represents the grid. Remember the physical grid is 7 columns for x 6 rows for y
        """
        self.board_coordinates = board_coordinates

    def __eq__():
        return

    def __repr__():
        return

    def get_board_cell_contents(self, grid_cell_location):
        """
        This class funtion that checks if a specified cell is empty of the game goard grid.
        :param 1: grid_cell_location as the key of the cell in the board_coordinates dictionary to return
        """
        return self.board_coordinates[grid_cell_location]

def read_game_moves_file():
    """
    This helper function reads in the game moves input file 4-moves.txt
    :returns: the games moves input as a list()-->[]
    """
    game_moves_list = []
    with open('./4-moves.txt', mode='rt') as game_moves:
        game_move_lines = game_moves.readlines()
		for line in game_move_lines:
			game_moves_list.append(line.strip().split())
    # end of withblock, close open file reading
    return game_moves_list

def main():
    columns = [1, 2, 3, 4, 5, 6, 7]
    rows = [1, 2, 3, 4, 5, 6]

    board_coordinates = {}
    for column in columns:
        for row in rows:
            coordinate = str(column) + str(row)
            board_coordinates[coordinate] = ' '

main()


















































        #
