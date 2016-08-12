
def uses_only():
	user_word = input('Please introduce a word: ')
	user_letters = input('Please introduce the letters to search: ')
	occur_user_leter = 0
	for letter_in_list in list(user_letters):
		occur_user_leter += user_word.count(letter_in_list)
		if user_word.count(letter_in_list) == 0:
			occur_user_leter += 1
	if occur_user_leter == len(user_word):
		return True
	return False

def main():
	print(uses_only())
if __name__ == '__main__':
	main()