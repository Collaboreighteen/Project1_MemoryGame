import random
import os
import platform

operatingSystem = platform.system()

print("Hello and welcome to our memory game")

wordList = [
	"dog",
	"hamster",
	"giraffe"]



def letsPlay():
	print("Remember these words plz " + str(wordList))

	ready = input("Got that? (Y/N)\n")

	if str.lower(ready) == "y":
		if os == "Windows":
			os.system('cls')

		else:
			os.system('clear')
	else:
		print("Seriously?")
		letsPlay()
	
	return

letsPlay()

testword = random.choice(wordList)

firstLetter = testword[0]

answer = input("Which of the words started with " + firstLetter + "?\n")
answer = str.lower(answer)

if answer[0] == firstLetter and any(answer in s for s in wordList):
	print("You're right!")
else:
	print("Wow you're bad at this")


