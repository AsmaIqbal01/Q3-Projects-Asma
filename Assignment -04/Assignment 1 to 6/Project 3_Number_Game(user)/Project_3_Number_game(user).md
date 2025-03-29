```python
import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("You have 5 attempts to guess the number between 50 and 100! Let's start the game!")

    number_to_guess:int =int(input("Enter number to guess :")) # Random number between 50 and 100
    chances = 5

    for guess_counter in range(1, chances + 1):
        while True:
            try:
                my_guess = int(input(f"Attempt {guess_counter}: Please enter a number from 50 to 100: "))
                if 50 <= my_guess <= 100:
                    break  # Valid input, exit the loop
                else:
                    print("Invalid input! Please enter a number between 50 and 100.")
            except ValueError:
                print("Invalid input! Please enter a valid integer.")

        if my_guess == number_to_guess:
            print(f"Congratulations! The number was {number_to_guess}. You guessed it right in {guess_counter} attempts!")
            break
        elif my_guess < number_to_guess:
            print("Your guess is too low, try again.")
        else:
            print("Your guess is too high, try again.")

    else:  # This else corresponds to the for loop, not the if statement
        print(f"Oops, sorry! The number was {number_to_guess}. Better luck next time!")

# Start the game
number_guessing_game()

if __name__ == "__main__":
    number_guessing_game()
```

    Welcome to the Number Guessing Game!
    You have 5 attempts to guess the number between 50 and 100! Let's start the game!
    Enter number to guess :78
    Attempt 1: Please enter a number from 50 to 100: 67
    Your guess is too low, try again.
    Attempt 2: Please enter a number from 50 to 100: 98
    Your guess is too high, try again.
    Attempt 3: Please enter a number from 50 to 100: 77
    Your guess is too low, try again.
    Attempt 4: Please enter a number from 50 to 100: 87
    Your guess is too high, try again.
    Attempt 5: Please enter a number from 50 to 100: 78
    Congratulations! The number was 78. You guessed it right in 5 attempts!
    Welcome to the Number Guessing Game!
    You have 5 attempts to guess the number between 50 and 100! Let's start the game!
    Enter number to guess :65
    Attempt 1: Please enter a number from 50 to 100: 54
    Your guess is too low, try again.
    Attempt 2: Please enter a number from 50 to 100: 98
    Your guess is too high, try again.
    Attempt 3: Please enter a number from 50 to 100: 76
    Your guess is too high, try again.
    Attempt 4: Please enter a number from 50 to 100: 56
    Your guess is too low, try again.
    Attempt 5: Please enter a number from 50 to 100: 67
    Your guess is too high, try again.
    Oops, sorry! The number was 65. Better luck next time!
    
