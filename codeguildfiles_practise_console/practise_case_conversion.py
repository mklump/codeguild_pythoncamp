# -*- coding: utf-8 -*-
"""
Python Coding Bootcamp (pdxcodeguild)
Program exercise file input/output in Python
by: Matthew James K
LAB/STEP requirements:

Practice: Case Conversion
Write a program that prompts the user for a word in snake_case, then converts and prints it out in CamelCase. Also do the reverse conversion.

Advanced

Write functions to handle kebab-case and CONSTANT_CASE.
Write functions to auto-detect which case is input.
Automatically print out all other cases on input.
Come up with a original-case-agnostic intermediate representation.
"""
def prompt_user_for_snake_case_variable():
    """
    The helper function asks the user to enter a text sequence for a variable that is snake case.
    :returns: the texted as a UTF-8 string the user entered as snake case.
    """
    print('Please enter a variable name in the form of snake case to be converted to camel case.')
    return input()

def convert_snake_case_to_camel_case(snake_case):
    """
    This helper function converts the specified snake_case name to camel case.
    :param 1: snake_case to be converted to camel_case
    :returns: the converted camel_case name
    """
    camel = snake_case.split('_')
    count_variable = 0
    for word in camel:
        for letter in word:
            camel[count_variable] = word.capitalize()
            count_variable += 1
            break
    camel_case = ''
    for word in camel:
        camel_case += word
    return camel_case

def print_camel_case(camel_case):
    """
    This helper function prints the converted snake case to camel case variable name to stardard out.
    :param 1: camel_case as the converted snake case to camel case text variable name
    """
    print(camel_case)

def main():
    snake_case = prompt_user_for_snake_case_variable()
    camel_case = convert_snake_case_to_camel_case(snake_case)
    print_camel_case(camel_case)

main()