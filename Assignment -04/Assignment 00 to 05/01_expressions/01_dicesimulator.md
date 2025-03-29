```python
import random
NUM_SIDES=6
def roll_dice():
  die1=random.randint(1,NUM_SIDES)
  die2=random.randint(1,NUM_SIDES)
  return die1,die2

def main():
  print("01_dicesimulator")
  for i in range(3):
    die1,die2=roll_dice()
    print(f'Roll{i+1}:  Die1={die1} + Die2={die2} = {die1+die2}')

if __name__=='__main__':
  main()

```

    01_dicesimulator
    Roll1:  Die1=5 + Die2=6 = 11
    Roll2:  Die1=2 + Die2=3 = 5
    Roll3:  Die1=5 + Die2=5 = 10
    
