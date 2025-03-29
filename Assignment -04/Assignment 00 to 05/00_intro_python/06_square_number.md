```python
from IPython.display import display, Markdown
def main():
  print("06_square_number")
  num:float=float(input("Type a number to see its square: "))
  squared_num:float= float(num *2)
  display(Markdown(f"{num} squared is **_{squared_num}_**"))
if __name__=='__main__':
  main()
```

    06_square_number
    Type a number to see its square: 4.2
    


4.2 squared is **_8.4_**

