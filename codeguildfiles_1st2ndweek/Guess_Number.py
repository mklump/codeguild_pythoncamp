# -*- coding: utf-8 -*-
"""
Python Coding Bootcamp (pdxcodeguild)
Program exercise to ask to a secret number between 1 and 10, then try to guess the secret number in 3 tries.
by Matthew James K
Accept three random words, and create a random constructed string with the three words.
"""
import random

guess = 0
numGuesses = 3

def get_secret_number():
	"""
	:returns: The secret number after asking for it
	"""
	print('I have a secret number between 1 and 10, guess higher or lower.')
	return random.randint(1, 10)

def guess_secret_number(number_guessus = 0, secret = 0):
	"""
	Performs the logic to guess the specified secret number
	"""
	guess = 0
	while secret != guess and number_guessus > 0:
		print('Guess? ')
		guess = int(input())
		if guess < secret:
			print('My secret number is higher.')
		elif guess > secret:
			print('My secret number is lower.')
		number_guessus -= 1
		print('You have ', number_guessus, ' remaining!')

if 0 == numGuesses:
    print('No more guesses remaining.')
elif 0 < numGuesses and secret == guess:
    print('You found my secret number!')

secret = get_secret_number()