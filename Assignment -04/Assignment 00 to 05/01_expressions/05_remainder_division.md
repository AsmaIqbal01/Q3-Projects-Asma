```python
from IPython.display import display, Markdown
def main():
  print("05_remainder_division")
  dividend:int=int(input("Please enter an integer to be divided: "))
  divisor:int=int(input("Please enter an integer to divide by: "))
  quotient:int = dividend // divisor
  remainder:int = dividend % divisor
  display(Markdown(f"{dividend} divided by {divisor} is **_{quotient}_** with a remainder of **_{remainder}_**"))
if __name__ == '__main__':
  main()
```

    05_remainder_division
    Please enter an integer to be divided: 447
    Please enter an integer to divide by: 7
    


447 divided by 7 is **_63_** with a remainder of **_6_**

