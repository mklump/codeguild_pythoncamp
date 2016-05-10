# -*- coding: utf-8 -*-
"""
Python Coding Bootcamp (pdxcodeguild)
Mad library string construction program excerise
by Matthew James K
Accept three random words, and create a random constructed string with the three words.
"""

def get_3_random_words():
	"""
	Prompts the user for three random words individually one at a time.
	:returns: A list of the 3 random words
	"""
	three_words_list = []
	print('Please input first word: ')
	three_words_list.append(input())
	print('Please input second word: ')
	three_words_list.append(input())
	print('Please input third word: ')
	three_words_list.append(input())
	return three_words_list

def get_madlib_str(three_words_list):
	"""
	Accepts the three random word list, and gives back the madlib
	:param 1: A list of the 3 random words not more than 3 words long
	:returns: The madlib string
	"""
	words = three_words_list
	return 'Your {}, your {}, and your {} are accepted!'.format(words[0], words[1], words[2])

def print_madlib(madlib):
	"""
	Prints the madlib string to console standard out
	:param l: madlib is the constructed string ready for printing
	"""
	print(madlib)

def main():
    word_list = get_3_random_words()
    madlib = get_madlib_str()
    print_madlib(madlib)

if __name__ == "__main__":
    sys.exit(int(main() or 0))