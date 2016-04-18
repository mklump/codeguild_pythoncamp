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
4) Show the user previously guessed incorrect letters
5) Limit the maximum number of guessed letters to six (6) hard coded
6) Let the user enter each new letter
7) Can only make six (6) missed guesses, then reveal the remaining correct answers
word: _A_
wrong: B
mistakes remaining: 5
"""
import os
import sys
import random

def game_intro():
    """
    Prints out to standard out an introduction for the game startup
    """
    print('In this version of Hangman: I have a secret word, and you get 6 guesses before I must reveal.')
    print('Press enter to continue:')
    input()

def print_guessed(remaining_letters):
    """
    This helper function prints to console standard out the letter correctly guessed of the specified word being guessed
    :param 2: remaining_letters is characters of the secret word that have been revealed as a list
    """
    print_out = ''.join('{} '.format(letter) for letter in remaining_letters)
    print_out = print_out.strip()
    print('word: {}'.format(print_out))

def print_wrongletters(guessed_letter, guessed_letter_list = [], secret_word = ''):
    """
    Prints to console standard out the letters guessed wrong
    :param 1: guessed_letter as the last letter that was guessed of the secret word
    :param 2: guessed_letter_list as the list of previously guessed letters list
    :param 3: secret_word as the secret word not yet guessed as a string
    :returns: the current list of letters guessed wrong
    """
    wrong_letter_string = ''
    if guessed_letter not in secret_word or 0 == len(guessed_letter_list):
        guessed_letter_list.append(guessed_letter.upper())
        wrong_letter_string.join( '{} '.format(wrong_letter.upper()) for wrong_letter in guessed_letter_list )
        print('wrong: {}'.format(wrong_letter_string))
    return guessed_letter_list

def print_mistakes(num_guess_remain, secret_word, remaining_letters):
    """
    Prints to console standard out the number of remaining mistakes allowed before the secret word is revealed
    :param 1: num_guess_remain is the remaining number of guesses as integer
    :param 2: secret_word as the secret word not yet guessed as a string
    :param 2: remaining_letters is characters of the secret word that have been revealed as a list
    """
    if 0 == num_guess_remain:
        for i in range(len(secret_word)):
            if '_' == remaining_letters[i]:
                remaining_letters[i] = secret_word[i].upper()

    print('mistakes remaining: {}'.format(num_guess_remain))

def get_random_word(word_tuple):
    """
    Accepts a tuple of predefined words, and returns the selected random word
    :param 1: word_tuple is a data structure tuple of predefined words as a tuple
    :returns: the selected random word as a string
    """
    word = random.choice(list(word_tuple))
    return word

def hide_secret_word(secret_word, hidden_word):
    """
    Takes the secret word as the word parameter, and hides all the characters using '_' based on the length of the word
    :param 1: word as the secret word to be hidden as a string
    :returns: secret hidden word as a string
    """
    wordlist = list(secret_word)
    for i in range(len(wordlist)): # Operation on a temporary list
        #if wordlist[i]:
        wordlist[i] = '_'
    hidden_word = ''.join(wordlist).strip()
    return hidden_word

def guess_letter():
    """
    Prompt the user for a letter in the secret word at the console
    :returns: the guessed letter as a string
    """
    print('Enter a letter to guess:')
    return input()

def match_guesses_to_secret_word(guessed_letter, secret_word, remaining_letters=[]):
    """
    The helper function matches each letter guessed of the secret word to the remaining letters
    that have not been guessed, and returns the remaining letters not yet guessed as a list.
    :param 1: guessed_letter as the last letter that was guessed of the secret word
    :param 2: secret_word as the secret word not yet guessed as a string
    :param 3: remaining_letters is characters of the secret word that have been revealed as a list
    :returns: the remaining letters left over after the last guess of the secret word as a list
    """
    for i in range(len(secret_word)):
        if guessed_letter.lower() == secret_word[i].lower():
            remaining_letters[i] = guessed_letter.upper()
    return remaining_letters

def get_number_guesses(guessed_letter_list):
    """
    This helper function accepts the remaining letters left of the secret word, and internally
    tracks the numbers of guesses remaining before the word is revealed after 6 guesses.
    :param 1: guessed_letter_list as the list of previously guessed letters list
    :returns: the number of guesses remaining of the secret word
    """
    number_guesses = 6 - len(guessed_letter_list)
    return number_guesses

def main():
    words_smalltuple = (#'.NET',
    'Agile',
    #'AJAX',
    #'Apache',
    #'Apache Foundation',
    #'API',
    #'ASCII',
    'bash'
    #'bus numbers',
    #'C',
    #'C#',
    #'C++',
    #'cloud service',
    )
    game_intro()
    number_of_guesses = 6
    guessed_letter_list = []
    secret_word = get_random_word(words_smalltuple)
    hidden_word = ''
    hidden_word = list(hide_secret_word(secret_word, hidden_word))
    while 0 < number_of_guesses:
        guessed_letter = guess_letter()
        remaining_letters = match_guesses_to_secret_word(guessed_letter, secret_word, hidden_word)
        number_of_guesses = get_number_guesses(guessed_letter_list)
        print_guessed(remaining_letters)
        guessed_letter_list = print_wrongletters(guessed_letter, guessed_letter_list, secret_word)
        print_mistakes(number_of_guesses, secret_word, remaining_letters)

if __name__ == "__main__":
    sys.exit(int(main() or 0))

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
