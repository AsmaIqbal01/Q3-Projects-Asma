```python
import random
def chaotic_counting():
  for i in range(10):
    curr_num= i+1
    if done():
      return
    print(curr_num)
def done():
  if random.random() < DONE_LIKELIHOOD:
    return True
  return False

def main():
  print("01_chaotic_counting")
  print("I am going to count untill I feel like stopping, whichever comes first.")
  chaotic_counting()
  print("I am done!")
if __name__ == "__main__":
  main()
```

    01_chaotic_counting
    I am going to count untill I feel like stopping, whichever comes first.
    1
    2
    3
    I am done!
    
