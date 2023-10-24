""" My first quintessential "python number game"
Built by Phil Cifone 2023-01-10. philcif@gmailcom.
First project I did myself! I used my own brain!"""

import random # for random number generation
import time # for dramatic pauses

MAX_GUESSES = 10 #	adjust integer according to desired difficulty level

# this generates random number
def getNumber():
	number = (random.randint(1, 1000)) #	adjust the second integer according to desired difficulty level
	return number

#	intro text
def main():
	print('Welcome to Phil\'s quintessential python number game!')
	time.sleep(1)
	print('I have a random number between 1 and 1000.')
	time.sleep(1)
	print(f'You have {MAX_GUESSES} attempts to guess the random number.')
	time.sleep(1)

#	this stores the random number the player needs to guess, I included a spot for manual entry.
#	if using manual entry the number randomizes after the player guesses your manual entry correctly
#	number = getNumber()
	number = 420 #	MANUAL ENTRY
	numGuesses = 1
	gameIsDone = False

# 	main game loop
	while True:
		guess = int(input('Guess #{}:\n> '.format(numGuesses)))

	#	too high, too low hints
		if guess > number:
			print('Too high, try again.')
		if guess < number:
			print('Too low, try again.')

	#	haha funny sex and weed numbers
		if (number == 69 or number == 420 or number == 42069 or number == 69420) and guess == number:
			print(f'niiiiice...you win!\nThe number was {number}!')
			time.sleep(.5)
			gameIsDone = True

	#	they got it right! :)
		elif guess == number:
			print(f'!!! You won!!!\nThe number was {number}!')
			gameIsDone = True

	#	they got it wrong :(
		else:
			numGuesses += 1 #	add guess since they need to try again
			if numGuesses > MAX_GUESSES: #	check if they reached their guess limit, if so they gotta go:
				if number > guess:
					difference = (number - guess)
				if number < guess:
					difference = (guess - number)
				time.sleep(.5)
				print(f'Sorry, you have run out of guesses. The answer was {number}. You were {difference} away!')
				gameIsDone = True

	#	ask to play again if game is over
		if gameIsDone == True:
				response = input('Play again? (y)es or (n)o?\n> ')
				if response.startswith('y'):
					number = getNumber() #	reset the number
					numGuesses = 1 #	reset the guess counter
					gameIsDone = False
					continue
				elif response.startswith('n'):
					print('Goodbye.')
					exit()
				else:
					print('Ah you broke me! Please enter a valid entry next time!') #	rare use case - game exits after here. i've accepted it.
					exit()

# if this program was run (instead of imported), run the program:
if __name__ == '__main__':
	main()
