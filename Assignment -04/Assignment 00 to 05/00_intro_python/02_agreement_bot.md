```python
from IPython.display import display, Markdown
def main():
  print("02_agreement_bot")
  fav_animal=input("What's your favorite animal? ")
  display(Markdown(f"My <b><i>favourite animal</b><i> is also <b><i>{fav_animal}</b></i>!"))
if __name__=='__main__':
  main()
```

    02_agreement_bot
    What's your favorite animal? goat
    


My <b><i>favourite animal</b><i> is also <b><i>goat</b></i>!

