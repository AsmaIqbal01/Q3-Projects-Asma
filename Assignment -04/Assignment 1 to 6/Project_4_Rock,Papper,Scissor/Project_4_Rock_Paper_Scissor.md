```python
import random

def play():
    user = input("'r' for rock, 'p' for paper, 's' for scissors\n").lower()
    computer = random.choice(['r', 'p', 's'])

    print(f"Computer chose: {computer}")

    if user == computer:
        return "It's a tie!"

    if is_win(user, computer):
        return "You won!"

    return "You lost!"

def is_win(player, opponent):
    # Returns True if player wins
    return (player == 'r' and opponent == 's') or \
           (player == 's' and opponent == 'p') or \
           (player == 'p' and opponent == 'r')

if __name__ == '__main__':
    while True:
        result = play()
        print(result)

        # Ask if the user wants to play again
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            break
```

    'r' for rock, 'p' for paper, 's' for scissors
    p
    Computer chose: s
    You lost!
    Do you want to play again? (y/n): y
    'r' for rock, 'p' for paper, 's' for scissors
    r
    Computer chose: s
    You won!
    Do you want to play again? (y/n): n
    
