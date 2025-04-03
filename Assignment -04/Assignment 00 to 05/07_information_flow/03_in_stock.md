```python
def num_in_stock(fruit):
  fruit_stock={
    "banana":6,
    "apple":10,
    "orange":32,
    "pear":15
  }
  if fruit in fruit_stock:
    return fruit_stock[fruit]
  else:
    print("We don't have {}".format(fruit))
    return 0

def main():
  print("03_in_stock")
  fruit=str(input("Enter a fruit: "))
  stock=num_in_stock(fruit)
  if stock == 0:
    print("We dont have any fruit in stock")
  else:
    print("We have {} in stock".format(stock))

if __name__=='__main__':
  main()
```

    03_in_stock
    Enter a fruit: apple
    We have 10 in stock
    
