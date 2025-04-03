```python
MAX_VALUE:int=100
def double_num(num):
  curr_value = num
  while curr_value <= MAX_VALUE:
    print(curr_value,end=" ")
    curr_value= curr_value*2
def main():
  print("01_double_it")
  user_input:int=int(input("Enter any number: "))
  double_num(user_input)
if __name__ == "__main__":
  main()
```

    01_double_it
    Enter any number: 2
    2 4 8 16 32 64 
