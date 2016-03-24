# -*- coding: utf-8 -*-
"""
Python Coding Bootcamp (pdxcodeguild)
Program exercise file input/output in Python
by Matthew James K
LAB/STEP requirements:
Find a book on Project Gutenberg. Download it as a UTF-8 text file.
	• Count how often each unique word is used, then print the most frequent top 10 out with their counts.
	• Count how often each unique pair of words is used, then print the most frequent top 10 out with their counts.
Pairs of words overlap.
The cat in the hat. -> The cat, cat in, in the, the hat.
	• Store the pair counts as a dict of dicts, where the first key is the first word in the pair and the second key is the second word.
	Allow the user to enter a word and get the most likely words to follow the given word.
Input? Mr.The most likely pair is "Mr. Darcy".
Advanced:
	• Normalize all of the words so differences in captialization and punctuation attached to words don't affect the counts.
	• Redo the pair counts: normalize the probablities in the inner dict by the count of pairs that start with the first word.
	• Chain together that ability to generate random sentences, one word at a time. From a given starting word. This is a language model.
"""

def get_book_words(book_title):
	"""
	Accepts a book title that is a flat text file as a full path, and then
	returns the words of that book text file as a dictionary structure
	:param 1: book_title as the full path to the text file of words to read in
	:returns: text word contents of book_title as dict type structure
	"""
	retval_dict = {}
	line_list = []
	with open(book_title) as book:		data_book = book.readlines()
		for line in data_book:			line_list = line.strip().split()			for word in line_list:
				if word not in retval_dict:
					retval_dict[word] = 1
				else:
					retval_dict[word] += 1
	# end with block/close file
	return retval_dict
# end def get_book_words(book_title):

# begin program main/test
data = get_book_words('./Clarissa_BigBook.txt')
# end program main/test