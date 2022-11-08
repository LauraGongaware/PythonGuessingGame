"""A number-guessing game."""

#Type your code here
import random
from random import randint

def play_game():

    secret_number = random.randint(1, 100)
    # guess = None
    # too_low = 0
    # too_high = 101
    guess_count = 0
    
    print("Howdy, what's your name?")
    user_name = input()
    print(user_name, "I'm thinking of a number between 1 and 100.")
    print("Try to guess my number")
    
  
    while True:
        number = input("What is your guess? ")
    # while secret_number != number:
        #guess = int(input("Your guess? "))
        # number = input()
        # guess = int(guess) 
        try:
            guess = int(number)
        except ValueError:
            print(f'{number} is not a valid number, try again.')
            continue

        if int(number) < 0 or int(number) > 100:
            print(f"{number} is not between 0 and 100.")

        guess_count = guess_count + 1
        
        if guess < secret_number:
            print("Your guess is too low, try again")
            # guess = int(input("Your guess? "))
        elif guess > secret_number:
            print("Your guess is too high, try again")
            # guess = int(input("Your guess? "))
        else:
            print("Well, done ", user_name) 
            print(f"You found my number in {guess_count} tries.")
            break

play_game()