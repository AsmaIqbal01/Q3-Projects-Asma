```python
def count_even(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1
    return count

def get_even_lst():
    lst = []
    while True:
        user_input = input("Enter a number or 'enter' to stop: ")
        if user_input == '':
            break
        try:
            num = int(user_input)
            if num % 2 == 0:
                lst.append(num)  # Append even numbers to the list
        except ValueError:
            print("Please enter a valid integer or 'enter' to stop.")
    return lst

def main():
    print("02_count_even")
    lst = get_even_lst()  # Get the list of even numbers
    print(lst)  # Print the list of even numbers
    print(count_even(lst))  # Print the count of even numbers

if __name__ == "__main__":
    main()
```

    02_count_even
    Enter a number or 'enter' to stop: 2
    Enter a number or 'enter' to stop: 6
    Enter a number or 'enter' to stop: 12
    Enter a number or 'enter' to stop: 16
    Enter a number or 'enter' to stop: 32
    Enter a number or 'enter' to stop: 13
    Enter a number or 'enter' to stop: 17
    Enter a number or 'enter' to stop: 1
    Enter a number or 'enter' to stop: 
    [2, 6, 12, 16, 32]
    5
    
