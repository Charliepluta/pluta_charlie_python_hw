import random

random_number = random.randint(1, 9)

guess = int(input("Guess a number between 1 and 9: "))

if guess < random_number:
    print("Your guess is too low.")
elif guess > random_number:
    print("Your guess is too high.")
else:
    print("Congratulations! You guessed exactly right.")