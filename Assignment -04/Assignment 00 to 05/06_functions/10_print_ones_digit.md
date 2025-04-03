```python
def print_ones_digit(number):
  ones_digit = number % 10
  print(ones_digit)
def main():
  print("10_print_ones_digit")
  user_input = int(input("Enter a number: "))
  print_ones_digit(user_input)
if __name__=='__main__':
  main()
```

    10_print_ones_digit
    Enter a number: 27
    7
    
