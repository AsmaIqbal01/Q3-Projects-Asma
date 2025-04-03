```python
def subtract_seven(inp):
    # Subtract 7 from the input number
    inp = inp - 7
    return inp

def main():
    print("05_subtract_7")
    # Prompt the user for a number and convert it to an integer
    num = int(input("Enter a number: "))  # Convert input to int

    # Call the subtract_seven function
    result = subtract_seven(num)

    # Print the result
    print("Result after subtracting 7:", result)

if __name__ == '__main__':
    main()
```

    05_subtract_7
    Enter a number: 35
    Result after subtracting 7: 28
    
