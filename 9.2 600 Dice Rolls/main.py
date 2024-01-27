# ---------------
# Title: 
# Date:
# ---------------

import random

def roll_dice():
    # Simulate a dice roll (generate a random number between 1-6)
    return random.randint(1, 6)

def check_guess(user_guess):
    # Ensure users guess is within range
    if 1 <= user_guess <= 6:
        dice_result = roll_dice()
        print(f"The dice shows: {dice_result}")

        # Check if guess matches dice result
        if user_guess == dice_result:
            print("Congratulations!")
            return True
        else:
            print("Sorry, your guess is incorrect. Please try again.")
            return False
    else:
        print("Invalid guess. Please choose a number between 1 - 6.")


# Hard code user_guess to 3
user_guess = 3

# Run the check 600 times and count the number of correct guesses
correct_guesses = 0
for _ in range(600):
    if check_guess(user_guess):
        correct_guesses += 1

# Check for bias by comparing the number of correct guesses to the expected value
print()

expected_value = 600 / 6  # Since there are 6 possible outcomes
print(f"Number of correct guesses: {correct_guesses}")
print(f"Expected value: {expected_value}")

# Check if the system is biased
if correct_guesses > expected_value:
    print("The system is biased towards the user's guess.")
else:
    print("The system is not biased.")
