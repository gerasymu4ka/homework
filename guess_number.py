#Guess the number
#Guess the number: 10 Wrong, guessed is greater.
#Next guess? 50 Wrong, guessed is greater. Next guess? 34 Right!

from random import randint

print('Guess the number (0 - 100). You have 5 guesses.')
num = randint(0, 100)

for i in range(1, 6):
    print 'Guess', i
    guess = int(raw_input('Enter the number: '))
    if num > guess:
        print("%r Nope! Bigger." % guess)
    elif num < guess:
        print("%r Nope! Lower." % guess)   
    else:
        num == guess
        print('HURRAH! YOU WIN!')
        break
    i += 1
else:
    print('LOOSER!')
