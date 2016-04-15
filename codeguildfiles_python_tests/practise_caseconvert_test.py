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
import practise_case_conversion

class Test_practise_caseconvert(unittest.TestCase):
    #def test_A(self):
    #    self.fail("Not implemented")

    def test_convert_snake_case_to_camel_case(self):
        case_convert = practise_case_conversion.convert_snake_case_to_camel_case('convert_snake_case_to_camel_case')
        try:
            assert case_convert == 'ConvertSnakeCaseToCamelCase'
        except AssertionError:
            self.fail('The function convert_snake_case_to_camel_case() did not succeed, please fix.')

    def test_convert_camel_case_to_snake_case(self):
        case_convert = practise_case_conversion.convert_camel_case_to_snake_case('ConvertSnakeCaseToCamelCase')
        try:
            assert case_convert == 'convert_snake_case_to_camel_case'
        except AssertionError:
            self.fail('The function test_convert_camel_case_to_snake_case() did not succeed, please fix.')

if __name__ == '__main__':
    unittest.main()
