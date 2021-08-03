__author__ = 'Eliya Gindi'

def start_print():
		"""print the stating picture that of the game and the MAX TRIES.
		"""
		HANGMAN_ASCII_ART =r"""    _    _
   | |  | |
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
   |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \
   | |  | | (_| | | | | (_| | | | | | | (_| | | | |
   |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |
                       |___/"""
		print(HANGMAN_ASCII_ART ,"\nMAX_TRIES = 6")

def choose_word(file_path, index):
		"""choose a secret word according the index number in the file. 
		:param file_path: a path of file with options secret words     
		:param index: chosen number from input 
		:type file_path: str 
		:type index: int 
		:return: chosen secret word from the file 
		:rtype: str 
		"""
		open_file = open(file_path, 'r')
		file_text = open_file.read()
		file_text.replace('\n', ' ')
		words_list = []
		main_words_list = []
		words_list = file_text.split(' ')
		for word in words_list:
			if word not in main_words_list:
				main_words_list.append(word)
		if index > len(words_list):
			while index > len(words_list):
				index -= len(words_list)
		secret_word= words_list[index-1]
		open_file.close()
		return secret_word

def print_hangman(num_of_tries):
		"""print the picture that matching to numbers of tries. 
		:param num_of_tries:  numbers of wrong tries  
		:type num_of_tries: int 
		""" 
		HANGMAN_PHOTOS ={\
		'picture 1':'\tx-------x',\
		'picture 2':'\tx-------x\n\t|\t\n\t|\n\t|\n\t|\n\t|',\
		'picture 3':'\tx-------x\n\t|\t|\n\t|\t0\n\t|\n\t|\n\t|',\
		'picture 4':'\tx-------x\n\t|\t|\n\t|\t0\n\t|\t|\n\t|\n\t|',\
		'picture 5':'\tx-------x\n\t|\t|\n\t|\t0\n\t|      /|\\\n\t|\n\t|',\
		'picture 6':'\tx-------x\n\t|\t|\n\t|\t0\n\t|      /|\\\n\t|      /\n\t|',\
		'picture 7':'\tx-------x\n\t|\t|\n\t|\t0\n\t|      /|\\\n\t|      / \\\n\t|',}
		if num_of_tries == 1:
				print(HANGMAN_PHOTOS['picture 1'])
		elif num_of_tries == 2:
				print(HANGMAN_PHOTOS['picture 2'])
		elif num_of_tries == 3:
				print(HANGMAN_PHOTOS['picture 3'])        
		elif num_of_tries == 4:
				print(HANGMAN_PHOTOS['picture 4'])
		elif num_of_tries == 5:
				print(HANGMAN_PHOTOS['picture 5'])
		elif num_of_tries == 6:
				print(HANGMAN_PHOTOS['picture 6'])
		elif num_of_tries == 7:
				print(HANGMAN_PHOTOS['picture 7'])
				
def check_win(secret_word, old_letters_guessed):
		"""check if the list have all the letters of the secret word. 
		:param secret_word: secret word   
		:param old_letters_guessed:  old guessed of the program 
		:type secret_word: str 
		:type old_letters_guessed: list 
		:return: True or False if the they have a match
		:rtype: bool 
		""" 
		for lett in secret_word:
			if lett in old_letters_guessed:
				continue
			else:
				return False
		return True
		
def try_update_letter_guessed(letter_guessed, old_letters_guessed):
		"""check if the letter is ok and  not already guessed it's print 'X' and list of guessed letter and give False,
		if not it's add the letter to old letters list and giVE True. 
		:param letter_guess:  letter guess from input  
		:param old_letters_guessed:  old guessed of letters
		:type letter_guess: str 
		:type old_letters_guessed: list 
		:return: bool answer if the letter is ok and not already guessed
		:rtype: bool 
		"""
		if  not check_valid_input(letter_guessed, old_letters_guessed) or letter_guessed.lower() in old_letters_guessed :
			print('X\n' + ' -> '.join(sorted(old_letters_guessed)))
			return False
		else:
			old_letters_guessed.append(letter_guessed.lower())
			return True
		
def check_valid_input(letter_guessed, old_letters_guessed):
		"""check if the letter is ok and  not already guessed. 
		:param letter_guess:  letter guess from input  
		:param old_letters_guessed:  old guessed of the program 
		:type letter_guess: str 
		:type old_letters_guessed: list 
		:return: bool answer if the letter_guess is ok and not already guessed
		:rtype: bool 
		""" 
		if len(letter_guessed) > 1:
			return False
		elif not letter_guessed.isalpha():
			return False 
		else:
			return True 

def show_hidden_word(secret_word, old_letters_guessed):
		"""print the correct letters guessed of the secret word. 
		:param secret_word: secret word  
		:param old_letters_guessed:  old guessed of the program 
		:type secret_word: str 
		:type old_letters_guessed: list 
		:return: return the temporarily answer wuth the correct letters and _
		:rtype: str 
		""" 
		temporarily_answer = ''
		for i in secret_word:
				if i in  old_letters_guessed:
					temporarily_answer = temporarily_answer + i + ' '
				else:
					temporarily_answer += '_ '	
		return temporarily_answer	

def main():
		start_print()
		old_letters = []
		secret_word = choose_word(input("enter words file path: "),int(input("enter word index: ")))
		"""secret_word ="abba" """
		MAX_TRIES = 7
		num_of_tries = 1
		print("\nLet’s start!\n")
		print_hangman(num_of_tries)
		print("_ " * len(secret_word))
		while num_of_tries < MAX_TRIES:
				letter_guess = input("\nguess a letter: ")
				if ' ' in letter_guess:
					letter_guess = letter_guess.replace(' ', '')
				if letter_guess.lower() not in secret_word and\
					check_valid_input(letter_guess, old_letters) and\
					letter_guess.lower() not in old_letters:
						num_of_tries +=  1
						print(':(\n')
						print_hangman(num_of_tries)
				try_update_letter_guessed(letter_guess, old_letters)
				print(show_hidden_word(secret_word, old_letters))
				if check_win(secret_word, old_letters):
					print("WIN")
					break
		if num_of_tries == MAX_TRIES:
			print("LOSE")
		input()	
if __name__ == "__main__":        
		main()
