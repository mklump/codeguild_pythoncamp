# -*- coding: utf-8 -*-
"""
Python Coding Bootcamp (pdxcodeguild)
PIG LATIN TRANSLATION exercise
by Matthew James K
Instructions:
	1) Take first letter
	2) move the first letter to the end
	3) add 'ay' on new end eg. 'cat' becomes --> 'atcay'
	4) Enter a sentence
	5) Convert each word to Pig Latin
	6) Print the output to console
	7) Handle Pig Latin vowels
	8) Handle punctuation
	9) Handle capilalization
"""

def main():
    print('Please enter a sentence to translate to pig latin:')
    sentence = input()

    VOWELS = ('a', 'e', 'i', 'o', 'u')
    PUNCTUATION = (',','.','!','?')

    word_list = sentence.split(' ')
    sentence = ''
    for word in word_list:
        if word[0] in VOWELS:
            word = word.join('hay')
            continue

        if word[0] in PUNCTUATION:
            word.insert(len(word) - 1, word[0])
        else:
            word = word.join(word[0].lower())

        word = word[1:] #removes the first character at index 0, returns rest of string

        if word[0] in PUNCTUATION:
            word.insert(len(word) - 1, 'ay')
        else:
            word = word.join('ay')

        sentence = sentence.join(word)
        #end of for word in word_list:
    print('Your sentence tranlated to pig latin is: {}', sentence)

if __name__ == "__main__":
    sys.exit(int(main() or 0))