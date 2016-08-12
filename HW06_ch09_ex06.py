#!/usr/bin/env python3
# HW06_ch09_ex05.py

# (1)
# Write a function called is_abecedarian that returns True if the letters in a
# word appear in alphabetical order (double letters are ok).
#   - write is_abecedarian
# (2)
# How many abecedarian words are there?
#   - write additional function(s) to assist you
#   - number of abecedarian words: 596
##############################################################################
# Imports

# Body
def is_abecedarian(word):
	flag = True
	if len(word) == 1:
		return flag
	if word[0] <= word[1]:
		flag = is_abecedarian(word[1:])
	else:
		flag = False

	return flag

def how_many_abecedarian():
	abecedarian_list = list()
	fin = open('words.txt', 'r')
	for word in fin:
		if is_abecedarian(word.strip()) == True:
			abecedarian_list.append(word.strip())
	# print(abecedarian_list)
	return len(abecedarian_list)


##############################################################################
def main():
	# print(is_abecedarian('aa'))
	print(how_many_abecedarian())
	pass  # Call your function(s) here.

if __name__ == '__main__':
    main()
