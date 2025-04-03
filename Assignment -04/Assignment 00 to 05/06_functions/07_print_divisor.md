```python
def print_divisor(num:int):
  print("Here are the divisors of ",num)
  for i in range(num):
    curr_divisor= i + 1
    if num % curr_divisor == 0:
      print(curr_divisor)

def main():
  print("07_print_divisor")
  num = int(input("Enter any integer: "))
  print_divisor(num)

if __name__ == '__main__':
  main()
```

    07_print_divisor
    Enter any integer: 32
    Here are the divisors of  32
    1
    2
    4
    8
    16
    32
    
