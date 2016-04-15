# -*- coding: utf-8 -*-
"""
Python Coding Bootcamp (pdxcodeguild)
Program exercise file input/output in Python
by: Matthew James K
LAB/STEP requirements:

Write unit tests case conversion and tictactoe

Practice: Test Case Conversion

-Create a test module for your case change program. Import your case change program. Create a test case class.
-Write a test for your snake case to camel case functions. Run the test via VS's testing run config.
-Test your other transformations in the case change.
-Test one of the Tic-Tac-Toe board classes.
-Duplicate those tests for the other board classes.

4/14 status - 6 tests failed out of 11 - change tests or fix code
"""

import unittest
import practise_tictactoe_interface


class Test_practise_tictactoe(unittest.TestCase):
    #def test_A(self):
    #    self.fail("Not implemented")

    def test_dictttboard_class_place_function(self):
        place_test = practise_tictactoe_interface.DictTTTBoard()
        place_test.place(1, 1, 'X')
        try:
            assert place_test.pos_to_token == {'a1': ' ', 'a2': ' ', 'a3': ' ', 'b1': ' ', 'b2': 'X',
                                              'b3': ' ', 'c1': ' ', 'c2': ' ', 'c3': ' '}
        except AssertionError:
            self.fail('The place operation on the DictTTTBoard DID NOT SUCCEED! ERROR! \
            - TODO FIX NOW THE DictTTTBoard.place()')

    def test_dictttboard_class_won_function(self):
        won_test = practise_tictactoe_interface.DictTTTBoard()
        won_test.place(1, 0, 'X')
        won_test.place(0, 1, 'O')
        won_test.place(1, 1, 'X')
        won_test.place(0, 2, 'O')
        won_test.place(1, 2, 'X')
        player = won_test.won()
        try:
            assert 'X' == player
        except AssertionError:
            self.fail('DictTTTBoard won test did not succeed. The player X was NOT the winner. \
            X was expected. Place/Won call series failled with value {} returned from won()'.format(player))

    def test_dictttboard_class_str_function(self):
        str_test = practise_tictactoe_interface.DictTTTBoard()
        str_test.place(0, 0, 'X')
        str_test.place(2, 1, '0')
        str_test.place(1, 1, 'X')
        try:
            assert str_test.pos_to_token == 'O| | \n |X|O\n | | \n'
        except AssertionError:
            self.fail('The string representation of the DictTTTBoard class did not pass.')

        
    def test_listlisttttboard_class_place_function(self):
        place_test = practise_tictactoe_interface.ListListTTTBoard()
        place_test.place(1, 0, 'X')
        try:
            assert place_test.rows == [[' ', 'X', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        except AssertionError:
            self.fail('The place operation on the ListListTTTBoard DID NOT SUCCEED! ERROR! \
            - TODO FIX NOW THE ListListTTTBoard.place()')
            
    def test_listlisttttboard_class_won_function(self):
        won_test = practise_tictactoe_interface.ListListTTTBoard()
        won_test.place(1, 0, 'X')
        won_test.place(0, 1, 'O')
        won_test.place(1, 1, 'X')
        won_test.place(0, 2, 'O')
        won_test.place(1, 2, 'X')
        player = won_test.won()
        try:
            assert 'X' == player
        except AssertionError:
            self.fail('ListListTTTBoard won test did not succeed. The player X was NOT the winner. \
            X was expected. Place/Won call series failed with value {} returned from won()'.format(player))

    def test_listlisttttboard_class_str_function(self):
        str_test = practise_tictactoe_interface.ListListTTTBoard()
        str_test.place(0, 0, 'X')
        str_test.place(2, 1, '0')
        str_test.place(1, 1, 'X')
        try:
            assert str_test.rows == 'O| | \n |X|O\n | | \n'
        except AssertionError:
            self.fail('The string representation of the ListListTTTBoard class did not pass.')

    def test_coordstttboard_class_place_function(self):
        place_test = practise_tictactoe_interface.CoordsTTTBoard()
        place_test.place(1, 0, 'X')
        try:
            assert place_test.x_y_token_triplets == [[' ', 'X', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        except AssertionError:
            self.fail('The place operation on the CoordsTTTBoard DID NOT SUCCEED! ERROR! \
            - TODO FIX NOW THE ListListTTTBoard.place()')
            
    def test_coordstttboard_class_won_function(self):
        won_test = practise_tictactoe_interface.CoordsTTTBoard()
        won_test.place(1, 0, 'X')
        won_test.place(0, 1, 'O')
        won_test.place(1, 1, 'X')
        won_test.place(0, 2, 'O')
        won_test.place(1, 2, 'X')
        player = won_test.won()
        try:
            assert 'X' == player
        except AssertionError:
            self.fail('CoordsTTTBoard won test did not succeed. The player X was NOT the winner. \
            X was expected. Place/Won call series failed with value {} returned from won()'.format(player))

    def test_coordstttboard_class_str_function(self):
        str_test = practise_tictactoe_interface.CoordsTTTBoard()
        str_test.place(0, 0, 'X')
        str_test.place(2, 1, '0')
        str_test.place(1, 1, 'X')
        try:
            assert str_test.x_y_token_triplets == 'O| | \n |X|O\n | | \n'
        except AssertionError:
            self.fail('The string representation of the CoordsTTTBoard class did not pass.')

if __name__ == '__main__':
    unittest.main()
