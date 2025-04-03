```python
def is_odd():
  for i in range(10,20):
    if i % 2== 0:
       print(i,"even",end=" ")
    else:
       print(i,"odd",end=" ")

def main():
  print("06_is_odd")
  is_odd()
if __name__ == "__main__":
  main()


```

    06_is_odd
    10 even 11 odd 12 even 13 odd 14 even 15 odd 16 even 17 odd 18 even 19 odd 
