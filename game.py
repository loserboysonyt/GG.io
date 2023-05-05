import random

print("Welcome to the Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("Can you guess what it is?")

number = random.randint(1, 100)
guess = int(input("Enter your guess: "))

while guess != number:
    if guess < number:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")
    guess = int(input("Enter another guess: "))

print("Congratulations! You guessed the number correctly.")
