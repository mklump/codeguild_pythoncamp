# -*- coding: utf-8 -*-
"""
Python Coding Bootcamp (pdxcodeguild)
Mad library string construction program excerise
by Matthew James K
Accept three random words, and create a random constructed string with the three words.
"""

def get_3_random_words():
	"""
	Prompts the user three random words individually one at a time.
	"""
	print('Please input first word: ')
	word1 = input()
	print('Please input second word: ')
	word2 = input()
	print('Please input third word: ')
	word3 = input()
	return word1 + ' ' + word2 + ' ' + word3

def print_madlib(word_list = []):
	"""
	Accepts 3 random supplied words as a list for the returned random string construction.
	:param l: Is a list of 3 expected random supplied words, and the type is list().
	:returns: The randomized string
	"""
	return 'Your ' + word_list[0] + ', your ' + word_list[1] + ', and your ' + word_list[2] + ', are accepted!'

word_list = get_3_random_words().split(' ')

print(print_madlib(word_list))