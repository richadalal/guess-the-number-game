import random

number = random.randint(1, 30)

player_name = input("Please enter your name: ")

number_of_guesses = 0

print('Hey '+ player_name + '! Guess a number between 1 and 30:')

while number_of_guesses < 3:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print('The guess is a little low')
    if guess > number:
        print('The guess is a little high')
    if guess == number:
        break

if guess == number:
    print('Yay! You guess the number in just ' + str(number_of_guesses) + ' tries!')

else:
    print('Sorry, you did not guess the number, it was: ' + str(number))
