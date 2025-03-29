```python
NUM_SIDES = 6

import random

def main():
  print("06_rolldice")
  die1:int=random.randint(1,NUM_SIDES)
  die2:int=random.randint(1,NUM_SIDES)
  print(f"Total sides of a dice : {NUM_SIDES} ")
  print(f"Die1 : {die1}")
  print(f"Die2 : {die2}")
  print(f"Total : {die1+die2}")

if __name__ == '__main__':
  main()
```

    06_rolldice
    Total sides of a dice : 6 
    Die1 : 3
    Die2 : 5
    Total : 8
    
