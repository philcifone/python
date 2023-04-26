# Phil's Totally Not Wordle Guessing Game!
# by Phil Cifone 2023-01-15

import random, time

# main words list referencing from system file
# download "words" from your pack-man if not on system already
WORDS = list(open("/usr/share/dict/words"))

# format list to have no symbols, possessives, newline, or uppercase
WORDS = [element.replace("'s", "").replace("\n", "").replace("'", "").replace("é", "").lower() for element in WORDS]

# working lists for each length of word
WORDS_4 = []
WORDS_5 = []
WORDS_6 = []
WORDS_7 = []
WORDS_8 = []

# not in use - for checking if user response is word in list
# trying to combine all into separate list
GAME_WORDS = ([WORDS_4] + [WORDS_5] + [WORDS_6] + [WORDS_7] + [WORDS_8])

# this generates the lists of only x letter words from main WORD list
for WORD in WORDS:
    if len(WORD) == 4:
        WORDS_4.append(WORD)
    if len(WORD) == 5:
        WORDS_5.append(WORD)
    if len(WORD) == 6:
        WORDS_6.append(WORD)
    if len(WORD) == 7:
        WORDS_7.append(WORD)
    if len(WORD) == 8:
        WORDS_8.append(WORD)

# removes duplicates from lists ??? not sure if doing anything
# in program without a variable / reference ???
[*set(WORDS_4)]
[*set(WORDS_5)]
[*set(WORDS_6)]
[*set(WORDS_7)]
[*set(WORDS_8)]

# set game parameters
numGuesses = 1
gameOver = False

# intro & set userLetterCount variable
print("Welcome to Phil's Totally Not Wordle Guessing Game!")
time.sleep(1)
print("Words with 4, 5, and 6 letters get 6 guesses.")
time.sleep(2)
print("Words with 7 and 8 letters get 10 guesses.")
time.sleep(2)
print("How many letters do you want your word to be?")
time.sleep(1)
userLetterCount = int(input("Select a number: [4, 5, 6, 7, or 8]\n > "))
print(f"The word contains {userLetterCount} letters.")

# get random word from WORDS_4-8 lists
if userLetterCount == 4:
    secretWord = (random.choice(WORDS_4))
if userLetterCount == 5:
    secretWord = (random.choice(WORDS_5))
if userLetterCount == 6:
    secretWord = (random.choice(WORDS_6))
if userLetterCount == 7:
    secretWord = (random.choice(WORDS_7))
if userLetterCount == 8:
    secretWord = (random.choice(WORDS_8))
if userLetterCount <= 3:
    print("Ah you broke me! Please enter a valid entry next time.")
    exit()
if userLetterCount >= 9:
    print("Ah you broke me! Please enter a valid entry next time.")
    exit()
#secretWord = ('tests') # MANUAL ENTRY - resets after first game

while True:

    # set guess limit
    if (userLetterCount == 7 or userLetterCount == 8):
        MAX_GUESSES = 10
    elif (userLetterCount == 4 or userLetterCount == 5 or userLetterCount == 6):
        MAX_GUESSES = 6
    else:
        print("Please enter a valid entry.")
        exit()

    response = input(f"Guess #{numGuesses}/{MAX_GUESSES}:\n > ").lower()

    # check input for correct length
    if len(response) != userLetterCount:
        print("Please enter a valid input.")
        continue

    # check input for valid word !?!i cant get this to work?!?
#    if response in GAME_WORDS:
#        pass
#    else:
#        print('Please enter a valid input.')
#        continue

    # check if they won
    if response == secretWord:
        print('\n!!! You win !!!\n')
        gameOver = True # game over - continue to: play again?

    # add guess if incorrect
    else:
        numGuesses += 1

    # check if player is out of guesses
    if numGuesses > MAX_GUESSES:
        print(f"You have run out of guesses. The answer was {secretWord}.")
        gameOver = True # game over - continue to: play again?

    # print lines for incorrect / print characters for correct
    for char in secretWord:
        if char in response:
            print(char, end="\n")
        else:
            print("_")
            continue

    # play again - ask player if they want to play again
    if gameOver:
        playAgain = input("Play again? y or n\n > ").lower()
        if playAgain.startswith('y'):
            # reset game parameters
            userLetterCount = int(input("How many letters do you want your word to be? Select a number: 4-8\n > "))
            # get random word from WORDS_4-8 lists
            # duplicate from above - finally got this to work
            # had to recopy the whole thing in this section
            # duh, why would i think it would work up top
            if userLetterCount == 4:
                secretWord = (random.choice(WORDS_4))
            if userLetterCount == 5:
                secretWord = (random.choice(WORDS_5))
            if userLetterCount == 6:
                secretWord = (random.choice(WORDS_6))
            if userLetterCount == 7:
                secretWord = (random.choice(WORDS_7))
            if userLetterCount == 8:
                secretWord = (random.choice(WORDS_8))
            if userLetterCount < 4:
                print("Ah you broke me! Please enter a valid entry next time.")
                exit()
            if userLetterCount > 8:
                print("Ah you broke me! Please enter a valid entry next time.")
                exit()
            numGuesses = 1
            gameOver = False
            print(f"The word contains {userLetterCount} letters.")
            continue
        else:
            print("Thank you for playing! Goodbye.")
            exit()
