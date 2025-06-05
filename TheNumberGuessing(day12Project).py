from random import randint
from art import logo

print(logo)

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

number = randint(1,100)

attempts = 0

op = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if op == 'easy':
    attempts = 10
elif op == 'hard':
    attempts = 5
else:
    print("The option is 'easy' or 'hard'.")

while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    
    if number == guess:
        attempts = -1
        print("You win!")
    elif number < guess:
        attempts -=1
        print("Too high.")
    else:
        attempts -=1
        print("Too low.")
        
    if attempts > 0:
        print("Guess again.")
    elif attempts == 0:
        print("You've run out of guesses. Refresh the page to run again.")