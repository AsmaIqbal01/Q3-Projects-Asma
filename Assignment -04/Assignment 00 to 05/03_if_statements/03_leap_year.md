```python
def main():
  print("03_leap_year")
  year=int(input("Enter a year: "))
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        print(year,"is a leap year")
      else:
        print(year,"is not a leap year")
    else:
      print(year,"is a leap year")
  else:
     print(year,"is not a leap year")

if __name__=='__main__':
  main()
```

    03_leap_year
    Enter a year: 2025
    2025 is not a leap year
    
