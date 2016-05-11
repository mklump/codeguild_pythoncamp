# -*- coding: utf-8 -*-
"""
Python Coding Bootcamp (pdxcodeguild)
First python hello world console program
by Matthew James K
First python hello world console program with documentation.
"""

def get_username():
	"""Prompts the user for their name."""
	print('What is your name')
	return input()

def print_helloworld(name = ''):
	""" Prints you name so you can say 'hello world' to the world... """
	greeting = 'So nice to meet you, ' + name
	return greeting

def main():
    print(print_helloworld(get_username()))

if __name__ == "__main__":
    sys.exit(int(main() or 0))