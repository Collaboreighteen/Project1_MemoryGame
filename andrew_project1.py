import random
import os

word_list = [
	"dog",
	"hamster", 
	"girraffe",
	"goat",
	"fish"
]


def countdown(t):
    import time
    print('This window will remain open for', t, ' more seconds...')
    time.sleep(t)
    print('Goodbye! \n \n \n \n \n')


def generate_letter_key(word_List):
	letter_key = {}
	for word in word_list:
		first_letter = word[0].lower()
		if first_letter in letter_key:

			letter_key[first_letter].append(word)
		else:
			letter_key[first_letter] = [word]

	return letter_key

def is_answer_correct(answer, letter_list): 
	print(answer)
	print(letter_list)
	return answer.lower in letter_list



# Letter Key just keys all the words in the list by their first letter for easier checking later
letter_key = generate_letter_key(word_list)

print('Remember these words:', ', '.join(word_list))
countdown(5)
os.system('clear')

# Randomly pick one of the letters in the list to ask about
random_letter = random.choice(list(letter_key.keys()))
question = 'Alright, give me a word that begins with:', random_letter

answer = input(question)

if is_answer_correct(answer, letter_key[random_letter]):
	print('🎉 Woah You got it 🎉')
else: 
	print('Aww that wasn\'t it ☹️ , try again maybe?')

