```python
from IPython.display import display, Markdown
def main():
  print("05_triangle_perimeter")
  side1=float(input("What is the length of side 1? "))
  side2=float(input("What is the length of side 2? "))
  side3=float(input("What is the length of side 3? "))
  triangle_perimeter=side1+side2+side3
  display(Markdown(f"The perimeter of triangle is **_{triangle_perimeter}_**"))
if __name__=='__main__':
  main()
```

    05_triangle_perimeter
    What is the length of side 1? 3
    What is the length of side 2? 4
    What is the length of side 3? 5.5
    


The perimeter of triangle is **_12.5_**

