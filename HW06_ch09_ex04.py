#!/usr/bin/env python
# HW06_ch09_ex04.py

# (1)
# Write a function named uses_only that takes a word and a string of letters,
# and that returns True if the word contains only letters in the list.
#   - write uses_only
# (2)
# Can you make a sentence using only the letters acefhlo? Other than "Hoe
# alfalfa?"
#   - write function to assist you
#   - type favorite sentence(s) here:
#       1:
#       2:
#       3:
##############################################################################
# Imports

# Body

def uses_only(user_word, user_letters):
    
    occur_user_leter = 0
    for letter_in_list in list(user_letters):
        occur_user_leter += user_word.count(letter_in_list)		#Adds the number of occurences that each letter has
        # if user_word.count(letter_in_list) == 0:
        #     occur_user_leter += 1				# When the letter does not existe in the word, it also add it up, that will make it go greater form the 
                                                # letters that actually exists.
    if occur_user_leter == len(user_word):
        return True
    return False


	# fin = open('words2.txt', 'r')

def sentence_acefhlo():
    fin = open("words2.txt", 'r')
    potential_words = []
    for word in fin:
        if uses_only(word.strip(), 'acefhlo'):
            potential_words.append(word.strip()) 
    # print("Potential Words: {}".format(potential_words))
    make_sentence(potential_words)

def make_sentence(words_list):
    sentence = list()
    for word1 in words_list:
        # print("Word: {}".format(word))
        t1 = (word1,)
        for word2 in words_list:
            t2 = (word2,)
            sentence.append(t1 + t2)

    print(sentence)
    for idx, each in enumerate(sentence):
        print("{} : {} {} ".format(idx, each[0], each[1]))



##############################################################################
def main():
    # user_word = input('Please introduce a word: ')
    # user_letters = input('Please introduce the letters to search: ')
    # print(uses_only(user_word, user_letters))

    # print(uses_only('alfalfa', 'acefhlo'))

    sentence_acefhlo()

if __name__ == '__main__':
    main()
