```python
ADULT_AGE:int = 18

def is_adult(age:int):
  if age >= ADULT_AGE:
    return True
  else:
    return False
def main():
  print("00_choosing_returns")
  age:str = int(input("How old is this person?: "))
  print(is_adult(age))

if __name__=='__main__':
  main()
```

    00_choosing_returns
    How old is this person?: 12
    False
    
