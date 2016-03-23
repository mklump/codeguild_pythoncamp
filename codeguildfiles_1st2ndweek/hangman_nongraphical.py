# -*- coding: utf-8 -*-
"""
Python Coding Bootcamp (pdxcodeguild)
Program exercise select a hidden word from a predefined TUPLE list, and attempt to guess the hidden word
in the form of a hangman game.
by Matthew James K
Accept three random words, and create a random constructed string with the three words.
Requirements to perform step by step:
1) Select a predefined word from a tuple imutable ordered sequence datastructure
2) Show the user blank signs (_ underscore character) for every letter not guessed
3) Show the user correctly guessed letters by filling in each correctly guessed space
4) Show the user previously guesses incorrect letters
5) Limit the maximum number of guessed letters to six (6) hard coded
6) Let the user enter each new letter
7) Can only make six (6) missed guesses, then reveal the remaining correct answers
word: _A_
wrong: B
mistakes remaining: 5
"""
import random

def get_random_word(word_tuple):
	"""
	Accepts a tuple of predefined words, and returns the selected random word
	:param 1: word_tuple is a data structure tuple of predefined words as a tuple
	:returns: the selected random word as a string
	"""
	return random.choice(word_tuple)

def print_notguessed(word, remaining):
	"""
	Prints to console standard out the words not guessed of the specified word being guessed
	:param 1: secret word not yet guessed as a string
	:param 2: remaining is characters of the secret word not yet revealed as a string
	"""
	printout = ''
	while i in range(len(word)):
		if remaining[i] not in word:
			printout += '_'
		else:
			printout += remaining[i]
	print('word: {}'.format(printout))

def print_guessed(word, remaining):
	"""
	Prints to console standard out the words correctly guessed of the specified word being guessed
	:param 1: secret word not yet guessed as a string
	:param 2: remaining is characters of the secret word that have been revealed as a string
	"""
	return None

def print_wrongletters(guesswrong):
	"""
	Prints to console standard out the letters guessed wrong
	:param 1: guesswrong is a string type of capital letter not correctly guess in the secret word
	:returns: guesswrong string of letters not guessed correct
	"""
	print('wrong: {}'.format(guesswrong))
	return guesswrong;

def print_mistakes(num_guess_remain):
	"""
	Prints to console standard out the number of remaining mistakes allowed before the secret word is revealed
	:param 1: num_guess_remain is the remaining number of guesses as integer
	"""
	print('mistakes remaining: {}'.format(num_guess_remain))

# begin main program/test
words_smalltuple = (
'bash'
#'.NET',
#'Agile',
#'AJAX',
#'Apache',
#'Apache Foundation',
#'API',
#'ASCII',
#'bus numbers',
#'C',
#'C#',
#'C++',
#'cloud service'
)

secret_word = get_random_word()

# end main program/test

words_largetuple = (
'.NET',
'Agile',
'AJAX',
'Apache',
'Apache Foundation',
'API',
'ASCII',
'bash',
'bus numbers',
'C',
'C#',
'C++',
'cloud service',
'client-side language',
'client-server architecture',
'Clojure',
'console interface',
'cookies',
'CouchDB',
'CPython',
'Cython',
'Django',
'Docker',
'docstrings',
'Document Object Model (DOM)',
'event driven programming',
'event loop',
'Extreme Programming (XP)',
'filesystem',
'Flask',
'Food Cart Pod',
'FTP',
'garbage collection',
'Git',
'graph',
'GUI',
'HTML / CSS',
'HTTP',
'HTTPS',
'IDE',
'IDLE',
'IronPython',
'Java',
'JavaScript',
'JQuery',
'JuJu',
'JVM',
'Jython',
'LAMP',
'LIFO',
'Linux',
'Mono',
'MongoDB',
'MySQL',
'NNTP',
'Node.js',
'noSQL',
'ORM',
'POSIX',
'PostgreSQL',
'Python Enhancement Proposal (PEP)',
'Planet Python',
'protocol',
'Pycon',
'Python',
'python.org',
'Python Software Foundation (PSF)',
'queue',
'REPL',
'RSA',
'scala',
'server-side language',
'SMTP',
'Structured Query Language (SQL)',
'stack',
'symmetric key',
'tcl',
'TCP / IP',
'thick vs thin client',
'Tk',
'tree',
'Ubuntu',
'Unicode',
'VCS',
'version control',
'virtual machine',
'wiki',
'web browser',
'XML'
)