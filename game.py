"""A number-guessing game."""

#Type your code here
import random
from random import randint
    
secret_number = random.randint(1, 100)
guess = None
too_low = 0
too_high = 101
guess_count = 0
    
print("Howdy, what's your name?")
user_name = input()
print(user_name, "I'm thinking of a number between 1 and 100.")
print("Try to guess my number")
number = input()
guess = int(number) 

#print(f'Your guess?, {guess}')

while secret_number != guess:
        guess_count = guess_count + 1
        if guess < secret_number:
            print("Your guess is too low, try again")
            guess = int(input("Your guess?"))
        elif guess > secret_number:
            print("Your guess is too high, try again")
            guess = int(input("Your guess? "))

print("Well, done ", user_name) 
print(f"You found my number in {guess_count} tries")
        

# print(f"Your guess is too high, try again = {too_high}, Your guess is too low, try again = {too_low}, Your guess = {guess}")

if guess > secret_number:
    too_high = guess
if guess < secret_number:
    too_low = guess