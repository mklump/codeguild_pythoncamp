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
"""

import unittest
import practise_tictactoe_interface


class Test_practise_tictactoe(unittest.TestCase):
    #def test_A(self):
    #    self.fail("Not implemented")

    def test_dictttboard_class(self):
        tictactoe = practise_tictactoe_interface.DictTTTBoard()
        tictactoe.place(1, 1, 'X')
        try:
            assert tictactoe.pos_to_token == {'a1': ' ', 'a2': ' ', 'a3': ' ', 'b1': ' ', 'b2': 'X',
                                              'b3': ' ', 'c1': ' ', 'c2': ' ', 'c3': ' '}
        except AssertionError:
            self.fail('The place operation on the DictTTTBoard DID NOT SUCCEED! ERROR! - TODO FIX NOW THE DictTTTBoard.place()')
        
    def test_listlisttttboard_class(self):
        tictactoe = practise_tictactoe_interface.ListListTTTBoard()
        tictactoe.place(1, 0, 'X')
        try:
            assert tictactoe.rows == [[' ', 'X', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        except AssertionError:
            self.fail('The place operation on the ListListTTTBoard DID NOT SUCCEED! ERROR! - TODO FIX NOW THE ListListTTTBoard.place()')

if __name__ == '__main__':
    unittest.main()
