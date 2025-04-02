```python
import random
def main():
  print("00_guess_my_number")
  secret_number = random.randint(1,99)
  print("I am thinking of a number between 1 and 99.")
  guess=int(input("Enter a guess: "))
  while guess != secret_number:
    if guess > secret_number:
      print("Your guess is too high")
    else:
      print("Your guess is too low")
    print()
    guess=int(input("Enter a guess: "))
  print("You got it! The number was :" + str(secret_number))
if __name__ == "__main__":
  main()
```

    00_guess_my_number
    I am thinking of a number between 1 and 99.
    Enter a guess: 23
    Your guess is too low
    
    Enter a guess: 67
    Your guess is too high
    
    Enter a guess: 44
    Your guess is too high
    
    Enter a guess: 33
    Your guess is too high
    
    Enter a guess: 31
    Your guess is too high
    
    Enter a guess: 29
    Your guess is too high
    
    Enter a guess: 23
    Your guess is too low
    
    Enter a guess: 25
    Your guess is too high
    
    Enter a guess: 24
    You got it! The number was :24
    
