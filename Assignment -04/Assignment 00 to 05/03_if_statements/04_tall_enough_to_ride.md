```python
from IPython.display import display, Markdown
MINIMUM_HEIGHT:int=50
def main():
  print("04_tall_enough_to_ride")
  user_height:int=int(input("How tall are you? "))
  if user_height>=MINIMUM_HEIGHT:
    display(Markdown(f"**_You are tall enough to ride_**"))
  else:
    display(Markdown(f"**_You are not tall enough to ride_**"))
if __name__=="__main__":
  main()
```

    04_tall_enough_to_ride
    How tall are you? 56
    


**_You are tall enough to ride_**

