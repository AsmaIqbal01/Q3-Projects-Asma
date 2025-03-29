```python
INCHES_IN_FOOT:int=12
def main():
  print("03_feet_to_inches")
  feet:float=float(input("Enter in feet: "))
  inches:float = feet * INCHES_IN_FOOT
  print(f"{feet} feet is {inches} inches")
if __name__=='__main__':
  main()
```

    03_feet_to_inches
    Enter in feet: 120
    120.0 feet is 1440.0 inches
    
