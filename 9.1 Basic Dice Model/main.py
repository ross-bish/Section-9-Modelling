# ----------------------
# Title:
# Date:
# ----------------------


import random

def roll_dice():
  # Simulate a dice roll (generate a random number between 1-6)
  dice_result = random.randint(1,6)
  return dice_result


def check_guess(user_guess):
  # Ensure user guess is within range 1-6
  if 1 <= user_guess <= 6:
    dice_result = roll_dice()
    print(f"The dice shows: {dice_result}")

    # Check if user guess matches result
    if user_guess == dice_result:
     print("Congratulations!")
    else:
     print("Sorry, you lose.")

  else:
    print("Invalid guess. Please choose a number between 1 - 6.")



# Prompt user to enter a guess
user_guess = int(input("Enter your guess (1 - 6): "))


# Call the check_guess() function and pass it user_guess 
check_guess(user_guess)

### Part B
# Test the function with several user inputs
user_inputs = [2, 4, 6, 70, 3, -1]

for i in user_inputs:
    print()
    check_guess(i)
    print("-" * 40)



