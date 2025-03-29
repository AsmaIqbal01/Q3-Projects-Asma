```python
from IPython.display import display, Markdown
def main():
  print("03_fahrenheit_to_celsius")
  degrees_fahrenheit=float(input("Enter Temperature in Fahrenheit: "))
  degrees_celsius=(degrees_fahrenheit - 32) * 5.0/9.0
  display(Markdown(f"Temperature : **_{degrees_fahrenheit}F_**: **_{degrees_celsius}C_**"))
if __name__ == '__main__':
    main()
```

    03_fahrenheit_to_celsius
    Enter Temperature in Fahrenheit: 76
    


Temperature : **_76.0F_**: **_24.444444444444443C_**

