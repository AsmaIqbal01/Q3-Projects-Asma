```python
import random
def main():
  print("03_guess_my_number")
  secret_int:int=random.randint(0,99)
  print("Guess My Number")
  print("I am thinking of a number between 0 to 99")
  guess=int(input("Enter a new number: "))
  while guess != secret_int:
    if guess > secret_int:
      print("Your guess is too high")
    else:
      print("Your guess is too low")
    print()
    guess:int=int(input("Enter a new number: "))
  print("You got it")
if __name__ == "__main__":
  main()
```

    03_guess_my_number
    Guess My Number
    I am thinking of a number between 0 to 99
    Enter a new number: 34
    Your guess is too high
    
    Enter a new number: 23
    Your guess is too low
    
    Enter a new number: 32
    Your guess is too high
    
    Enter a new number: 30
    Your guess is too high
    
    Enter a new number: 28
    Your guess is too low
    
    Enter a new number: 29
    You got it
    
