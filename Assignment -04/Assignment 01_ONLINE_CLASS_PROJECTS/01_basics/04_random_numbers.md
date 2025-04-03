```python
import random

MIN_NUM = 0
MAX_NUM = 100
N_NUM = 10

def in_range():
   return random.sample(range(MIN_NUM,MAX_NUM +1),N_NUM)
def main():
    print("04_random_numbers")
    random_numbers = in_range()  # Get the list of random numbers
    print(random_numbers)  # Print the list of random numbers

if __name__ == '__main__':
    main()
```

    04_random_numbers
    [35, 82, 6, 79, 2, 5, 26, 28, 64, 15]
    
