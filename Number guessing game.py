import random
import sys
print('welcome to the number guessing game. A random number between 1 to 100 will be generated and you have to guess which on it is.')
print('you have three tries!')
number=random.randint(1,100)
guess1=int(input('enter your first guess:'))
if guess1==number:
    print('you guessed it on the first try! good job.\n you won! \n Thanku for playing this game.')
    sys.exit()
elif guess1 > number:
    print('your guess is too high. Try again')
else:
    print('your guess is too low. Try again')

guess2=int(input('enter you second guess:'))
if guess2==number:
    print('you guesses it on the second try! good. \n you won! \n Thanku for playing this game.')
    sys.exit()
elif guess2>number:
    print('your guess is too high. Try again')
else:
    print('your guess is too low. Try again')

guess3=int(input('enter your third guess:'))
if guess3==number:
    print('you guessed it on the third try! not bad. \n you won!\n Thanku for playing this game.')
    sys.exit()
elif guess3 > number:
    print("your guess is too high. \n it's okay. \n you lose! \n Thanku for playing this game.")
else:
    print("your guess is too low. \n it's okay.\n Thanku for playing this game.")