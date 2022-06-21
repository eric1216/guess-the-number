import random

from soupsieve import select

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    count = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')
        count+=1
    
    print(f'CORRECT! It took you {count} attempts to correctly guess the number {guess}.')

def computer_guess(x):
    low = 1
    high = x
    count = 0
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low #could also be high b/c low = high
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        count+=1

    print(f'I WIN! The computer took {count} attempts to correctly guess the number {guess}.')

gamemode = input('Would you like to guess the computers number (1) or let the computer guess your number (2)? ')
while gamemode != '1' and gamemode != '2':
    gamemode = input('Select a proper gamemode. Enter 1 or 2: ')
upper_limit = int(input('Selet the upper limit to guess: '))
if int(gamemode) == 1:
    guess(int(upper_limit))
elif int(gamemode) == 2:
    computer_guess(upper_limit)
