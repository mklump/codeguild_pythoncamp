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
	• Allow the user to enter a word and get the most likely words to follow the given word.
Input? Mr.
The most likely pair is "Mr. Darcy".
Advanced:
	• Normalize all of the words so differences in captialization and punctuation attached to words don't affect the counts.
	• Redo the pair counts: normalize the probablities in the inner dict by the count of pairs that start with the first word.
	• Chain together that ability to generate random sentences, one word at a time. From a given starting word. This is a language model.
"""
import operator

def show_program_intro():
	"""
	Prints to console standard out an introduction for this program
	"""
	print('This program will read in a book title text file, and perform calculations on it.')

def read_booktxt_to_dictionary(book_title, pairing=False): # Note: Do not add additional boolean flag to execute additional logic, instead refactor again.
	"""
	This helper function accepts a book title that is a flat text file as a relative path, and then
	returns the words and the unique count of each word of that book text file as a dictionary.
	:param 1: book_title as the full path to the text file of words to read in as a string
	:param 2: pairing bool flag set to False if reading single words, or True if reading pairing
	:returns: text word contents of book_title as a dict
	"""
	dictionary_of_collected_keywords_and_their_counts = {}
	line_of_raw_booktext_list = []
	with open(book_title) as book:
		data_book = book.readlines()
		for line in data_book:
			line_of_raw_booktext_list = line.strip().split()
			if True == pairing:
				line_of_raw_booktext_list = get_word_pairs_sep_by_space_not_single_words(line_of_raw_booktext_list)
			dictionary_of_collected_keywords_and_their_counts = get_count_by_each_parsed_word_as_dictionary_key(line_of_raw_booktext_list)
	# end with block/close file
	return dictionary_of_collected_keywords_and_their_counts
# end def read_booktxt_to_dictionary(book_title):

def get_word_pairs_sep_by_space_not_single_words(line_of_raw_singlewords_list):
	"""
	This helper function is called only if we are collecting pairs of words, not single words from the book text.
	:param 1: line_of_raw_booktext_list as raw text data read in from the book as a list
	:returns: word pairs required for the word pairs list processing as list
	"""
	line_of_parsed_wordpairs_list = [' '.join(line_of_raw_singlewords_list[i:i+2]) for i in range(0, len(line_of_raw_singlewords_list), 2)]
	removed_singles_parsed_wordpairs_list = remove_singlewords_from_pairings(line_of_parsed_wordpairs_list)
	return removed_singles_parsed_wordpairs_list

def get_count_by_each_parsed_word_as_dictionary_key(list_of_each_line_split_words):
	"""
	This helper function accepts each parsed line from the book text, and counts each individual word as each word or phrase occurs.
	:param 1: list_of_each_line_split_words is the parsed incomming text line already split up by delimited spaces
	:returns: The dictionary of individual words as the keys collected and each individual one word's count occurance.
	"""
	individual_words_dictionary_collector = {}
	for word in list_of_each_line_split_words:
		if word not in individual_words_dictionary_collector:
			individual_words_dictionary_collector[word] = 1
		else:
			individual_words_dictionary_collector[word] += 1
	return individual_words_dictionary_collector

def remove_singlewords_from_pairings(word_pairs_with_singles):
	"""
	Accepts a single line of the book read in as a list, and checks to see if the elements
	of that list of extracted word pairings are in fact valid pairings. If the word pairing
	is not a valid pair, but if fact is a single word, then that single word is removed.
	:param 1: The line of which to perform the word pair checking as a list
	:returns: The corrected word pairing as a list
	"""
	for word_pair in word_pairs_with_singles:
		word_pair = word_pair.strip()
		if ' ' not in word_pair:
			word_pairs_with_singles.remove(word_pair)
	word_pairs_without_singles = word_pairs_with_singles
	return word_pairs_without_singles

def sort_dict_data(data):
	"""
	This helper function sorts the unsorted dictionary data structure
	:param 1: data as the unsorted dictionary as a dict
	:returns: the sorted dictionary data as a list
	"""
	listsort = sorted(data.items(), key=operator.itemgetter(1), reverse=True) # Do not leave space on KEY assignment here only
	#listsort.reverse()
	return listsort

def print_top_ten_frequent(data, pairing=False):
	"""
	This helper function sccepts the sorted dictionary book counted words data structure,
	and prints out to console standard out the top ten found most frequent words in the
	book words counted data.
	:param 1: data as the sorted dict data structure as list
	:param 2: pairing boolean flags if paired words are being printed or not
	"""
	if False == pairing:
		print('The top ten most frequest words are:')
	else:
		print()
		print('The top ten most frequest word pairings are:')
	for item in range(10):
		print('{} : occured {} times'.format(data[item][0], data[item][1]))

def prompt_for_txt_book_file_to_load(text_file_book):
	"""
	Asks the user for what book file to load, then returns that file as a string
	:param 1: The default text book file to load
	:returns: The book text file to load as a string
	"""
	print('Press enter to accept default text book, {}, or other text file to load:'.format(text_file_book))
	default = text_file_book
	text_file_book = input()
	if default != text_file_book and '' != text_file_book:
		return text_file_book
	else:
		return default

def get_dict_of_dicts_from_pairings(list_of_pairs):
	"""
	This helper function accepts a list of the word pairings and their counts, and constructs
	a dict of dicts where the first key is the first word in the pair and the second key is the
	second word.
	:param 1: list_of_pairs is the list of word pairings as list of word pairs and their counts
	:returns: the constructs a dict of dicts as specified
	"""
	list1 = [] # List of the first key that is the first word
	list2 = [] # List of the second key that is the second word
	list3 = [] # List of the respective counts
	for index in range(len(list_of_pairs)):
		words = list_of_pairs[index][0].split(' ')
		list1.append(words[0])
		list2.append(words[1])
		list3.append(list_of_pairs[index][1])
	retval = { x: {y, z} for x, y, z in zip(list1, list2, list3) }
	#retval = { x : [y, z, t] for x,y,z,t in zip(list1, list3, list2, list3) }
	return retval

def print_first_ten_on_dict_of_dicts(dicts):
	"""
	This help function prints to console standard out the first ten data elements of the
	dictionary of dictionaries data structure.
	:param 1: dictionary of dictionary data structure to print
	"""
	print('\nThe first ten data elements of the constructed dictonary were:')
	print_count = 0
	for element in dicts:
		print('{ '+ '{} : {}'.format(element, dicts[element]) + ' }')
		print_count += 1
		if print_count > 10:
			break

def get_next_most_frequent_word(word_input, list_word_pairings):
	"""
	This helper function accepts a word input, and returns the next most freqent word following
	that word based on the pairings word output.
	:param 1: word_input for which to look for the next following from the pairing data
	:param 2: sorted list of word pairings outputed from last main loop execution
	:returns: the next most likely appearing word that follows the input_word as a string
	"""
	for leftword in list_word_pairings:
		if word_input == leftword[0].split()[0]:
			return leftword

def print_word_pair(word_pair):
	"""
	This helper function prints the next most likely word pair.
	"""
	print('The most likely pair is \"{}\".'.format(word_pair))

def get_word_input_for_print_next():
	"""
	This helper function ask the user for a word input, and return that as a string.
	:returns: word input for print next pairing as a string
	"""
	print('Input word before as most likely pairing?:')
	return input()

def execute_main_loop():
	"""
	Executes the main loop body of the main/test program
	"""
	text_file_book = './Clarissa_BigBook.txt' # Default text book to load currently testing with
	listsort = []
	for x in range(2):
		text_file_book = prompt_for_txt_book_file_to_load(text_file_book)
		data = read_booktxt_to_dictionary(text_file_book, 0 != x % 2)
		listsort = sort_dict_data(data)
		print_top_ten_frequent(listsort, 0 != x % 2)

	dictionary = get_dict_of_dicts_from_pairings(listsort)
	print_first_ten_on_dict_of_dicts(dictionary)
	word_before = get_word_input_for_print_next()
	word_after = get_next_most_frequent_word(word_before, listsort)  # listsort variable should still contain the dual word list as pairs
	print_word_pair(word_after)

# end def execute_main_loop():

# begin program main/test
show_program_intro()
execute_main_loop()
# end program main/test