""" Rock Paper Scissors by Phil Cifone 2022-01-12
Schoolyard Rules. Best out of three. """

import random # for random number
import time # for dramatic pauses

WIN, LOSE = 2, -2 #   win/lose counter

ROCK, PAPER, SCISSORS = 4, 5, 6 #   assign values to each gesture for random.choice

def main():

    print('Lets play Rock, Paper, Scissors!')
    time.sleep(1)
    print('Schoolyard rules, best out of 3.\n')

    bestOfWin, bestOfLose, match = 0, 0, 1 #   set win/lose/match counters to starting position

#   game loop
    while True:
        time.sleep(1)
        hand = input(f'(R)ock, (P)aper, (S)cissors, shoot!\n\n[{match}/3] > ').lower()
        time.sleep(1)

        #   rock
        if hand.startswith('r'):
            shoot = random.choice([5, 6])
            if shoot == SCISSORS:
                bestOfWin += 1
                match += 1
                print(f'They threw scissors. You smashed them!\n\n\tWins:{bestOfWin} Loses:{abs(bestOfLose)}\n')
                if bestOfWin >= 2:
                    time.sleep(1)
                    print('\nYou won the game!')
                    time.sleep(1)
                    again = input('Play again? (Y)es or (N)o?\n> ') #   replay game
                    if again.startswith('n'):
                        print('Thanks for playing! Goodbye.')
                        exit()
                    if again.startswith('y'):
                        bestOfWin = 0 # reset counter for new game
                        match = 1 # reset counter for new game
                        continue
                else:
                    continue
            else:
                bestOfLose -= 1
                match += 1
                print(f'They threw paper. You got covered.\n\n\tWins:{bestOfWin} Loses:{abs(bestOfLose)}\n')
                if bestOfLose <= -2:
                    time.sleep(1)
                    print('\nYou lost the game.')
                    time.sleep(1)
                    again = input('Play again? (Y)es or (N)o?\n> ') #   replay game
                    if again.startswith('n'):
                        print('Thanks for playing! Goodbye.')
                        exit()
                    if again.startswith('y'):
                        bestOfLose = 0 # reset counter for new game
                        match = 1 # reset counter for new game
                        continue
                else:
                    continue

        #   paper
        if hand.startswith('p'):
            shoot = random.choice([6, 4])
            if shoot == ROCK:
                bestOfWin += 1
                match += 1
                print(f'They threw rock. You covered it!\n\n\tWins:{bestOfWin} Loses:{abs(bestOfLose)}\n')
                if bestOfWin >= 2:
                    time.sleep(1)
                    print('You won the game!')
                    time.sleep(1)
                    again = input('Play again? (Y)es or (N)o?\n> ') #   replay game
                    if again.startswith('n'):
                        print('Thanks for playing! Goodbye.')
                        exit()
                    if again.startswith('y'):
                        bestOfWin = 0 # reset counter for new game
                        match = 1 # reset counter for new game
                        continue
                else:
                    continue
            else:
                bestOfLose -= 1
                match += 1
                print(f'They threw scissors. You got cut up.\n\n\tWins:{bestOfWin} Loses:{abs(bestOfLose)}\n')
                if bestOfLose <= -2:
                    time.sleep(1)
                    print('You lost the game.')
                    time.sleep(1)
                    again = input('Play again? (Y)es or (N)o?\n> ') #   replay game
                    if again.startswith('n'):
                        print('Thanks for playing! Goodbye.')
                        exit()
                    if again.startswith('y'):
                        bestOfLose = 0 # reset counter for new game
                        match = 1 # reset counter for new game
                        continue
                else:
                    continue

        #   scissors
        if hand.startswith('s'):
            shoot = random.choice([4, 5])
            if shoot == PAPER:
                bestOfWin += 1
                match += 1
                print(f'They threw paper. You cut it up!\n\n\tWins:{bestOfWin} Loses:{abs(bestOfLose)}\n')
                if bestOfWin >= 2:
                    time.sleep(1)
                    print('You won the game!')
                    time.sleep(1)
                    again = input('Play again? (Y)es or (N)o?\n> ') #   replay game
                    if again.startswith('n'):
                        print('Thanks for playing! Goodbye.')
                        exit()
                    if again.startswith('y'):
                        bestOfWin = 0 # reset counter for new game
                        match = 1 # reset counter for new game
                        continue
                else:
                    continue
            else:
                bestOfLose -= 1
                match += 1
                print(f'They threw rock. You got smashed.\n\n\tWins:{bestOfWin} Loses:{abs(bestOfLose)}\n')
                if bestOfLose <= -2:
                    time.sleep(1)
                    print('You lost the game.')
                    time.sleep(1)
                    again = input('Play again? (Y)es or (N)o?\n> ') #   replay game
                    if again.startswith('n'):
                        print('Thanks for playing! Goodbye.')
                        exit()
                    if again.startswith('y'):
                        bestOfLose = 0 # reset counter for new game
                        match = 1 # reset counter for new game
                        continue
                else:
                    continue

# idk what this means but if this program was run (instead of imported), run the program:
if __name__ == '__main__':
	main()

