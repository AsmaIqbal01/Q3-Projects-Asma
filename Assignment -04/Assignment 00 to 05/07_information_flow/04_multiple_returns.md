```python

```


```python
def get_user_data():
   fname:str=input("What is your firstname: ")
   lname:str=input("What is your lastname: ")
   email:str=input("What is your email address: ")
   return fname,lname,email

def main():
  print("04_multiple_returns")

  print("Recieved the following user data: ",get_user_data())
if __name__=='__main__':
  main()
```

    04_multiple_returns
    What is your firstname: sara
    What is your lastname: inam
    What is your email address: sad@asda.cdoc
    Recieved the following user data:  ('sara', 'inam', 'sad@asda.cdoc')
    
