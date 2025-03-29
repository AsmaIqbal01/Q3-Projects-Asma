```python
import random
N_NUMBERS:int = 10
MIN_NUMBER :int = 1
MAX_NUMBER :int = 100
def main():
  print("05_random_numbers")
  for i in range(N_NUMBERS):
    print(random.randint(MIN_NUMBER, MAX_NUMBER))

if __name__ == '__main__':
  main()
```

    05_random_numbers
    73
    62
    80
    14
    47
    32
    4
    45
    32
    51
    
