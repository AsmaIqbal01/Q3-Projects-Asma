```python
def avg_number(a: float, b: float) -> float:
    """
    Calculate the average of two numbers.

    Parameters:
    a (float): The first number.
    b (float): The second number.

    Returns:
    float: The average of the two numbers.
    """
    sum = a + b
    return sum / 2

def main():
    print("00_averages")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print(f"The average of {num1} and {num2} is: {avg_number(num1, num2)}")

if __name__ == '__main__':
    main()
```

    00_averages
    Enter the first number: 5
    Enter the second number: 7
    The average of 5.0 and 7.0 is: 6.0
    
