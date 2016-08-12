#!/usr/bin/env python3
# HW06_ch09_ex03.py

# (1)
# Write a function named avoids that takes a word and a string of forbidden
# letters, and that returns True if the word doesn't use any of the forbidden
# letters.
#   - write avoids
# (2)
# Modify your program to prompt the user to enter a string of forbidden
# letters and then print the number of words that don't contain any of them.
#   - write forbidden_prompt and
#   - modify to create forbidden_param that accepts the string as an argument
# (3)
# Can you find a combination of 5 forbidden letters that excludes the smallest
# number of words?
#   - write a function that finds this combination of letters: find_five
#   - have that function print the letters and print the # of words excluded
##############################################################################
# Imports

# Body


def avoids(word, forbidden):
    """ return True if word NOT forbidden"""
    flag = True
    letter_list = list(forbidden)
    for letter_in_list in letter_list:
        if word.find(letter_in_list) != -1:
            flag = False
            break

    return flag


def forbidden_prompt():
    """ print count of words NOT forbidden by input"""
    fin = open('words.txt', 'r')
    forbidden_param = input('Enter the forbidden letters: ')
    count = 0
    letter_list = list(forbidden_param)

    for line in fin:
        word = line.strip()
        flag = True
        # print(word)
        for letter_in_list in letter_list:
            # print(letter_in_list)
            if word.find(letter_in_list) == -1:
                flag = False
        if flag == False:
            count += 1
    print(count)


def forbidden_param(words, forbidden_letters):
    """ return count of words NOT forbidden by param"""
    count = 0
    letter_list = list(forbidden_letters)

    for line in words:
        word = line.strip()
        flag = True
        # print(word)
        for letter_in_list in letter_list:
            # print(letter_in_list)
            if word.find(letter_in_list) == -1:
                flag = False
        if flag == False:
            count += 1
    return count

# import string
# def find_five():
    # fin = open('words2.txt', 'r')
    # count = 0
    # letter_count_lst = list()


    # for letter_in_list in string.ascii_lowercase:
    #     for line in fin:
    #         word = line.strip()
    #         print(word)
    #         if word.find(letter_in_list) != -1:
    #             count += 1  
        
    #     letter_count_lst.append(count)
    #     count = 0
    # print(letter_count_lst)

def find_five():
    count_clean = 0
    excludes_smallest = []
    with open('words.txt', 'r') as f:
        words = f.readlines() #113809
    combos = list(itertools.combinations(string.ascii_lowercase, 5)) # 65780
    for each in combos:
        print(each)
        tmp_clean = forbidden_param(words, each)
        if tmp_clean > count_clean:
            count_clean = tmp_clean
            excludes_smallest = each
    print(count_clean, excludes_smallest)


##############################################################################
def main():
    # print(avoids('Selenne', 'km'))

    # forbidden_prompt()

    # forbidden_letters = input('Enter the forbidden letters: ')

    # fin = open('words2.txt', 'r')
    # words = fin.readlines() 
    # print(forbidden_param(words, 'kb'))

    # find_five()
    pass

if __name__ == '__main__':
    main()
