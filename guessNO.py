#/usr/bin/env  python3.7
import random
print("This program is to guess a number between 1 and 20")

no=int(random.randint(1,20))
while True:
    print('')
    print('')
    guess = int(input("Kindly enter your guess: "))
    if guess < no:
        print('')
        print(guess)
        print("Guess is too low, try again")
        continue
    elif guess > no:
        print('')
        print(guess)
        print("Guess is too high, try again")
    else:
        print(guess)
        print("You\'ve guess the correct number")
        break
