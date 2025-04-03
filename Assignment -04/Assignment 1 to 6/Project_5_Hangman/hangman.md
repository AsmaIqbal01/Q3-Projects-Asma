```python
import random
import string
words=[ "discomfort",
  "discontent",
  "discover",
  "discovery",
  "discuss",
  "discussion",
  "disease",
  "disgust",
  "dish",
  "dismiss",
  "disregard",
  "disrespect",
  "dissatisfaction",
  "dissatisfy",
  "distance",
  "distant",
  "distinguish",
  "district",
  "disturb",
  "ditch",
  "dive",
  "divide",
  "division",
  "do",
  "doctor",
  "dog",
  "dollar",
  "donkey",
  "door",
  "dot",
  "double",
  "doubt",
  "down",
  "dozen",
  "drag",
  "draw",
  "drawer",
  "dream",
  "dress",
  "drink",
  "drive",
  "drop",
  "drown",
  "drum",
  "dry",
  "duck",
  "due",
  "dull",
  "during",
  "dust",
  "duty",
  "each",
  "eager",
  "ear",
  "early",
  "earn",
  "earnest",
  "earth",
  "ease",
  "east",
  "eastern",
  "easy",
  "eat",
  "edge",
  "educate",
  "education",
  "educator",
  "effect",
  "effective",
  "efficiency",
  "efficient",
  "effort",
  "egg",
  "either",
  "elastic",
  "elder",
  "elect",
  "election"]
def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:  # Ensure the word does not contain hyphens or spaces
        word = random.choice(words)
    return word

def hangman():
    word = get_valid_word(words)  # Get a random valid word
    word_letters = set(word)  # Create a set of letters in the word
    alphabet = set(string.ascii_lowercase)  # Set of all uppercase letters
    used_letters = set()  # Set to keep track of used letters
    attempts = 6  # Number of allowed incorrect attempts

    print("Welcome to Hangman!")

    while attempts > 0 and word_letters:  # Continue until no attempts left or word is guessed
        # Show the current state of the word
        print("Current word: ", ' '.join([letter if letter in used_letters else '-' for letter in word]))
        print(f"Used Letters: {', '.join(sorted(used_letters))}")
        print(f"Attempts remaining: {attempts}")

        user_letter = input("Guess a letter: ").lower()  # Get user input and convert to uppercase

        # Debugging output
        print(f"Word: {word}, Word Letters: {word_letters}, User Letter: {user_letter}")

        if user_letter in alphabet - used_letters:  # Check if the letter is valid and not used
            used_letters.add(user_letter)  # Add letter to used letters
            if user_letter in word_letters:  # Check if the letter is in the word
                word_letters.remove(user_letter)  # Remove the letter from the set
                print(f"Good job! '{user_letter}' is in the word.")
            else:
                attempts -= 1  # Decrease attempts if the letter is not in the word
                print(f"Sorry, '{user_letter}' is not in the word.")
        elif user_letter in used_letters:
            print("You have already used that character. Try again!")
        else:
            print("Invalid character. Please enter a letter from A-Z.")

    if not word_letters:  # If all letters are guessed
        print(f"Congratulations! You guessed the word: {word}")
    else:  # If attempts run out
        print(f"Sorry, you've run out of attempts. The word was: {word}")

if __name__ == '__main__':
    hangman()
```

    Welcome to Hangman!
    Current word:  - - - -
    Used Letters: 
    Attempts remaining: 6
    Guess a letter: a
    Word: east, Word Letters: {'t', 's', 'e', 'a'}, User Letter: a
    Good job! 'a' is in the word.
    Current word:  - a - -
    Used Letters: a
    Attempts remaining: 6
    Guess a letter: e
    Word: east, Word Letters: {'t', 's', 'e'}, User Letter: e
    Good job! 'e' is in the word.
    Current word:  e a - -
    Used Letters: a, e
    Attempts remaining: 6
    Guess a letter: g
    Word: east, Word Letters: {'t', 's'}, User Letter: g
    Sorry, 'g' is not in the word.
    Current word:  e a - -
    Used Letters: a, e, g
    Attempts remaining: 5
    Guess a letter: l
    Word: east, Word Letters: {'t', 's'}, User Letter: l
    Sorry, 'l' is not in the word.
    Current word:  e a - -
    Used Letters: a, e, g, l
    Attempts remaining: 4
    Guess a letter: s
    Word: east, Word Letters: {'t', 's'}, User Letter: s
    Good job! 's' is in the word.
    Current word:  e a s -
    Used Letters: a, e, g, l, s
    Attempts remaining: 4
    Guess a letter: y
    Word: east, Word Letters: {'t'}, User Letter: y
    Sorry, 'y' is not in the word.
    Current word:  e a s -
    Used Letters: a, e, g, l, s, y
    Attempts remaining: 3
    Guess a letter: i
    Word: east, Word Letters: {'t'}, User Letter: i
    Sorry, 'i' is not in the word.
    Current word:  e a s -
    Used Letters: a, e, g, i, l, s, y
    Attempts remaining: 2
    Guess a letter: o
    Word: east, Word Letters: {'t'}, User Letter: o
    Sorry, 'o' is not in the word.
    Current word:  e a s -
    Used Letters: a, e, g, i, l, o, s, y
    Attempts remaining: 1
    Guess a letter: n
    Word: east, Word Letters: {'t'}, User Letter: n
    Sorry, 'n' is not in the word.
    Sorry, you've run out of attempts. The word was: east
    
