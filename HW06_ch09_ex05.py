#!/usr/bin/env python3
# HW06_ch09_ex05.py

# (1)
# Write a function named uses_all that takes a word and a string of required
# letters, and that returns True if the word uses all the required letters at
# least once.
#   - write uses_all
# (2)
# How many words are there that use all the vowels aeiou? How about
# aeiouy?
#   - write functions(s) to assist you
#   - # of words that use all aeiou: 598
#   - # of words that use all aeiouy: 42
##############################################################################
# Imports

# Body
def uses_all(word, req_letters):
	flag = True
	for letter in req_letters:
		if word.find(letter) == -1:
			flag = False
			break

	return flag


def uses_all_vowels(vowels):
	fin = open('words.txt', 'r')
	list_words = list()
	for word in fin:
		if uses_all(word, vowels):
			list_words.append(word)

	# for idx, word in enumerate(list_words):
	# 	print("{} : {} ".format(idx, word.strip()))

	return len(list_words)
	

##############################################################################
def main():
	# print(uses_all('selenne', 's'))
	print(uses_all_vowels('aeiou'))
	print(uses_all_vowels('aeiouy'))
	pass  # Call your function(s) here.

if __name__ == '__main__':
    main()
