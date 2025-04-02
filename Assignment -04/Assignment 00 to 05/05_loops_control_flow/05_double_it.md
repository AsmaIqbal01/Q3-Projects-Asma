```python
MAX_VALUE = 100

def main():
    print("05_double_it")
    curr_value = int(input("Enter any value less than 100: "))

    # Ensure the user enters a value less than 100
    if curr_value >= MAX_VALUE:
        print("Please enter a value less than 100.")
        return  # Exit the program if the input is invalid

    # Loop to double the value until it is 100 or greater
    while curr_value <= MAX_VALUE:
        print(curr_value)  # Print the current value
        curr_value = curr_value * 2  # Double the current value

    print(curr_value)  # Print the final value that is >= 100

if __name__ == "__main__":
    main()
```

    05_double_it
    Enter any value less than 100: 4
    4
    8
    16
    32
    64
    128
    
