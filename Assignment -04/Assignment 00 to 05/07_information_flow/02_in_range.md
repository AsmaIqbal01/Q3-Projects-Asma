```python
def in_range(num,low,high):
  if num >= low and num <= high:
    print(f"{num} is in range of {low} and {high}")
  else:
    print(f"{num} is not in range of {low} and {high}")
def main():
  print("02_in_range")
  num = int(input("Enter a number: "))
  low = int(input("Enter a lower bound: "))
  high = int(input("Enter a higher bound: "))
  in_range(num,low,high)


if __name__ == "__main__":
  main()


```

    02_in_range
    Enter a number: 56
    Enter a lower bound: 10
    Enter a higher bound: 100
    56 is in range of 10 and 100
    
