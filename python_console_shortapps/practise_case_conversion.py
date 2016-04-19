# -*- coding: utf-8 -*-
"""
Python Coding Bootcamp (pdxcodeguild)
Program exercise file input/output in Python
by: Matthew James K
LAB/STEP requirements:

Practice: Case Conversion
Write a program that prompts the user for a word in snake_case, then converts and prints it out in CamelCase.
Also do the reverse conversion.

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

def convert_snake_case_to_camel_case(snake_case = ''):
    """
    This helper function converts the specified snake_case name to CamelCase.
    :param 1: snake_case to be converted to camel_case
    :returns: the converted camel_case name
    """
    camel = snake_case.split('_')
    index_variable = 0
    for word in camel: # THERE ARE TWO STATEMENTS HERE THAT MUST EXECUTE NOT ONE! List comp does NOT apply.
        camel[index_variable] = word.capitalize()
        index_variable += 1 # index_variable MUST INCREMENT
    camel_case = ''
    camel_case = camel_case.join(camel)
    return camel_case

def convert_camel_case_to_snake_case(camel_case = ''):
    """
    This helper function converts the specified CamelCase name to snake_case
    :param 1: camel_case to be converted to snake_case
    :returns: the converted snake_case name
    """
    list_of_case = []
    for letter in camel_case:
        list_of_case.append(letter)
    for item in list_of_case:
        if True == item.isupper():
            index_of_item = list_of_case.index(item)
            list_of_case[index_of_item] = item.lower()
            list_of_case.insert(index_of_item, '_')
    str_of_case = ''.join(item for item in list_of_case if item)
    snake_case = str_of_case.strip('_')
    return snake_case

#def convert_kebab_case_to_constant_case(kebab_case):
#    """
#    This helper function accepts a kebab-case input and converts that case to CONSTANT_CASE caps underscore case.
#    :param 1: kebab_case as this-kebab-case-is-a-sample-kebab-case input
#    """
#    pass

def print_case_output(case_input):
    """
    This helper function prints the case_input to stardard out.
    :param 1: case_input as the text name to be printed out.
    """
    print(case_input)

def main():
    #snake_case = prompt_user_for_snake_case_variable()
    camel_case = convert_snake_case_to_camel_case('convert_snake_case_to_camel_case')
    print_case_output(camel_case)
    snake_case = convert_camel_case_to_snake_case(camel_case)
    print_case_output(snake_case)

main()