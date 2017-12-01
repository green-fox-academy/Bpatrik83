"""Exercise
Write a program where the program chooses a number between 1 and 100.
The player is then asked to enter a guess. If the player guesses wrong,
then the program gives feedback and ask to enter an other guess until the guess is correct.
    Make the range customizable (ask for it before starting the guessing).
    You can add lives. (optional)
Example
I've the number between 1-100. You have 5 lives.
    20
Too high. You have 4 lives left.
    10
Too low. You have 3 lives left.
    15
Congratulations. You won!"""

from random import randint
original_number = (randint(1, 100))
check = True
lives = 5

while check:
    try:
        guess = int(input("Enter your tip: "))
        if guess < 1 or guess > 100:
            raise ValueError
        else:
            if guess == original_number:
                check = False
                print("Congratulations. You won!")
            if guess > original_number:
                lives -= 1
                if lives > 0:
                    print("Too high. You have", lives, "lives left.")
            if guess < original_number:
                lives -= 1
                if lives > 0:
                    print("Too low. You have", lives, "lives left.")
            if lives < 1:
                print("You lost. No more lives left", "The number was", original_number)
                check = False
    except ValueError:
        print("Please enter only a number between 1 and 100")

